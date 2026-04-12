import os

# PyMuPDF 메시지 출력 경로는 fitz import 전에 설정해야 합니다.
# 기본값은 /dev/null로 보내 콘솔에 MuPDF 내부 경고가 찍히지 않게 합니다.
os.environ.setdefault("PYMUPDF_MESSAGE", f"path:{os.devnull}")

import re
import sys
import argparse
import io
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import fitz  # PyMuPDF
from google import genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API 키를 찾을 수 없습니다. .env 파일에 GEMINI_API_KEY를 설정해 주세요.")

client = genai.Client(api_key=api_key)
MODEL_ID = "gemini-2.5-flash"

_mupdf_lock = threading.Lock()

# POSTECH 컴퓨터공학과(CSE) CSED 과목별 특화 프롬프트 컨텍스트
# 출처: https://cse.postech.ac.kr/csepostech/admissions/under-subjects.do
COURSE_CONTEXTS = {
    # --- 기초 ---
    "CSED101": "이 슬라이드는 프로그래밍과 문제해결 (CSED101) 강의 자료입니다. Python 기초 문법, 변수, 조건문, 반복문, 함수, 재귀 등 프로그래밍 입문 개념이 주로 다뤄집니다.",
    "CSED103": "이 슬라이드는 프로그래밍 입문 (CSED103) 강의 자료입니다. 파이썬 또는 C 언어 기반의 프로그래밍 기초 문법과 알고리즘 사고법이 주로 다뤄집니다.",
    "CSED105": "이 슬라이드는 인공지능 기초 (CSED105) 강의 자료입니다. AI의 역사, 탐색 알고리즘, 기계학습 기초 개념, 신경망 입문 등이 주로 다뤄집니다.",
    # --- 2학년 ---
    "CSED211": "이 슬라이드는 컴퓨터시스템개론 (CSED211) 강의 자료입니다. C 언어, 어셈블리, 프로세서 구조, 메모리 계층, 시스템 호출, 링킹 등 컴퓨터 시스템 전반이 주로 다뤄집니다.",
    "CSED212": "이 슬라이드는 프로그래밍 스튜디오 (CSED212) 강의 자료입니다. 실제 소프트웨어 개발 경험, 협업 도구(Git), 테스트, 코드 품질 등이 주로 다뤄집니다.",
    "CSED226": "이 슬라이드는 데이터분석 입문 (CSED226) 강의 자료입니다. NumPy, pandas, matplotlib, scikit-learn 등의 라이브러리와 머신러닝 기초 개념이 주로 다뤄집니다.",
    "CSED232": "이 슬라이드는 소프트웨어 작성 원리 (CSED232) 강의 자료입니다. C++ 기반의 객체지향 프로그래밍, 클래스, 상속, 다형성, 제네릭, 메모리 관리 등이 주로 다뤄집니다.",
    "CSED233": "이 슬라이드는 데이터구조 (CSED233) 강의 자료입니다. 배열, 연결 리스트, 스택, 큐, 트리, 힙, 해시 테이블, 그래프 등의 자료구조와 시간/공간 복잡도 분석이 주로 다뤄집니다.",
    "CSED261": "이 슬라이드는 전산수학 (CSED261) 강의 자료입니다. 이산수학, 논리, 집합, 수열, 그래프 이론, 조합론, 확률 기초 등 CS에 필요한 수학적 기반이 주로 다뤄집니다.",
    "CSED273": "이 슬라이드는 디지털시스템 설계 (CSED273) 강의 자료입니다. 불 대수, 논리 게이트, 조합 회로, 순차 회로, FSM, Verilog HDL 등 디지털 회로 설계가 주로 다뤄집니다.",
    # --- 3학년 ---
    "CSED312": "이 슬라이드는 운영체제 (CSED312) 강의 자료입니다. 프로세스/스레드, CPU 스케줄링, 동기화, 교착상태, 메모리 관리, 가상 메모리, 파일 시스템 등이 주로 다뤄집니다.",
    "CSED321": "이 슬라이드는 프로그래밍언어 (CSED321) 강의 자료입니다. 언어 패러다임(함수형, 논리형, 객체지향), 타입 시스템, 파싱, 인터프리터/컴파일러 개요 등이 주로 다뤄집니다.",
    "CSED331": "이 슬라이드는 알고리즘 (CSED331) 강의 자료입니다. 분할정복, 탐욕 알고리즘, 동적 프로그래밍, 그래프 알고리즘(BFS/DFS/최단경로/MST), NP-완전성 등이 주로 다뤄집니다.",
    "CSED332": "이 슬라이드는 소프트웨어 설계방법 (CSED332) 강의 자료입니다. 소프트웨어 설계 원칙(SOLID), 디자인 패턴, UML, 리팩터링, 테스트 주도 개발(TDD) 등이 주로 다뤄집니다.",
    "CSED341": "이 슬라이드는 오토마타 및 형식언어 (CSED341) 강의 자료입니다. DFA/NFA, 정규 언어, 문맥 자유 문법, 푸시다운 오토마타, 튜링 기계, 결정 불가능성 등이 주로 다뤄집니다.",
    "CSED342": "이 슬라이드는 인공지능 (CSED342) 강의 자료입니다. 탐색 알고리즘, 게임 트리, 제약 충족, 베이즈 네트워크, 강화학습 기초, 자연어 처리 개요 등이 주로 다뤄집니다.",
    "CSED343": "이 슬라이드는 기계학습을 위한 수학 (CSED343) 강의 자료입니다. 선형대수(행렬, 고유값), 미적분(편미분, 연쇄법칙), 확률/통계, 최적화 이론 등 ML에 필요한 수학이 주로 다뤄집니다.",
    "CSED352": "이 슬라이드는 데이터통신 (CSED352) 강의 자료입니다. OSI/TCP-IP 모델, 신호 인코딩, 오류 제어, MAC 프로토콜, 라우팅 등 네트워크 하위 계층이 주로 다뤄집니다.",
    "CSED353": "이 슬라이드는 컴퓨터네트워크 (CSED353) 강의 자료입니다. TCP/UDP, HTTP, DNS, 소켓 프로그래밍, 혼잡 제어, 보안 기초 등 네트워크 응용 계층이 주로 다뤄집니다.",
    "CSED355": "이 슬라이드는 전산신호처리 (CSED355) 강의 자료입니다. 푸리에 변환, 샘플링, 필터 설계, FFT, 이산 신호 시스템 등이 주로 다뤄집니다.",
    "CSED356": "이 슬라이드는 인간-컴퓨터 상호작용 (CSED356) 강의 자료입니다. HCI 원칙, 사용자 중심 설계, 프로토타이핑, 사용성 평가, 접근성 등이 주로 다뤄집니다.",
    "CSED357": "이 슬라이드는 데이터베이스시스템 (CSED357) 강의 자료입니다. 관계형 모델, SQL, ER 다이어그램, 정규화, 트랜잭션, 인덱스, 쿼리 최적화 등이 주로 다뤄집니다.",
    # --- 4학년 / 고급 ---
    "CSED401": "이 슬라이드는 컴퓨터와 사회 (CSED401) 강의 자료입니다. AI 윤리, 개인정보, 지식재산권, 사이버 보안 사회적 영향, 기술과 사회의 관계 등이 주로 다뤄집니다.",
    "CSED403": "이 슬라이드는 블록체인 및 암호화폐 (CSED403) 강의 자료입니다. 암호학 기초(해시, 공개키), 비트코인/이더리움 구조, 스마트 컨트랙트, 합의 알고리즘 등이 주로 다뤄집니다.",
    "CSED404": "이 슬라이드는 모바일 및 유비쿼터스 컴퓨팅 (CSED404) 강의 자료입니다. 모바일 OS, 무선 네트워크, 위치 서비스, IoT 프로토콜, 에너지 효율성 등이 주로 다뤄집니다.",
    "CSED405": "이 슬라이드는 GPU 및 가속컴퓨팅 (CSED405) 강의 자료입니다. CUDA 프로그래밍, GPU 아키텍처, 병렬 알고리즘, 메모리 최적화, AI 가속 등이 주로 다뤄집니다.",
    "CSED415": "이 슬라이드는 컴퓨터보안 (CSED415) 강의 자료입니다. 암호화(대칭/비대칭), 네트워크 보안, 웹 취약점(XSS, SQLi), 악성코드, 보안 프로토콜(TLS) 등이 주로 다뤄집니다.",
    "CSED416": "이 슬라이드는 P2P 네트워킹 (CSED416) 강의 자료입니다. P2P 아키텍처, DHT, BitTorrent, 오버레이 네트워크, 분산 시스템 개념 등이 주로 다뤄집니다.",
    "CSED417": "이 슬라이드는 사물인터넷 (CSED417) 강의 자료입니다. IoT 플랫폼, 센서/액추에이터, MQTT/CoAP 프로토콜, 엣지 컴퓨팅, IoT 보안 등이 주로 다뤄집니다.",
    "CSED420": "이 슬라이드는 소프트웨어 검증 (CSED420) 강의 자료입니다. 정적 분석, 모델 체킹, 프로그램 검증, 퍼징, 기호 실행(symbolic execution) 등이 주로 다뤄집니다.",
    "CSED423": "이 슬라이드는 컴파일러 설계 (CSED423) 강의 자료입니다. 어휘 분석, 파싱(LL/LR), 의미 분석, 중간 코드 생성, 최적화, 코드 생성 등이 주로 다뤄집니다.",
    "CSED425": "이 슬라이드는 임베디드시스템 프로그래밍 (CSED425) 강의 자료입니다. ARM 아키텍처, RTOS, 인터럽트, 드라이버 개발, 저전력 설계 등이 주로 다뤄집니다.",
    "CSED426": "이 슬라이드는 빅데이터 (CSED426) 강의 자료입니다. Hadoop, Spark, MapReduce, 분산 파일시스템, 스트림 처리, NoSQL 데이터베이스 등이 주로 다뤄집니다.",
    "CSED433": "이 슬라이드는 전산논리 (CSED433) 강의 자료입니다. 명제논리, 1차 논리, SAT 솔버, 자동 정리 증명, 논리 프로그래밍(Prolog) 등이 주로 다뤄집니다.",
    "CSED434": "이 슬라이드는 고급 프로그래밍 (CSED434) 강의 자료입니다. 함수형 프로그래밍(Haskell/Scala), 모나드, 타입 추론, 동시성 프로그래밍 등 고급 프로그래밍 패러다임이 주로 다뤄집니다.",
    "CSED441": "이 슬라이드는 컴퓨터비전 개론 (CSED441) 강의 자료입니다. 이미지 처리, 에지 검출, 특징 추출, CNN 기반 인식, 객체 탐지, 세그멘테이션 등이 주로 다뤄집니다.",
    "CSED451": "이 슬라이드는 컴퓨터그래픽스 (CSED451) 강의 자료입니다. 렌더링 파이프라인, 래스터화, 광선 추적, 변환 행렬, 셰이더, OpenGL/WebGL 등이 주로 다뤄집니다.",
}


def configure_pymupdf(show_messages: bool = False) -> None:
    """PyMuPDF / MuPDF 내부 메시지 표시 여부를 설정합니다."""
    fitz.TOOLS.mupdf_display_errors(show_messages)
    fitz.TOOLS.mupdf_display_warnings(show_messages)


def get_course_context(pdf_path: Path) -> str:
    """경로에서 과목 코드를 감지하고 해당 컨텍스트를 반환합니다."""
    for part in pdf_path.parts:
        if part.upper() in COURSE_CONTEXTS:
            return COURSE_CONTEXTS[part.upper()]
    return "이 슬라이드는 컴퓨터공학 전공 강의 자료입니다."


def build_prompt(course_context: str) -> str:
    return f"""당신은 POSTECH 컴퓨터공학과 전공 튜터입니다.
{course_context}

첨부된 슬라이드를 분석하여 다음 형식으로 마크다운 노트를 작성해 주세요:
- **핵심 개념**: 슬라이드의 주요 개념을 명확하게 설명
- **코드/수식 해설**: 코드는 코드 블록(```)을 사용하고, 수식은 반드시 LaTeX 문법($ 또는 $$)을 사용하여 작성해 주세요.
- **구체적 예시**: 실제 동작 예시나 실생활 비유를 통해 이해를 도움
- **시험 포인트**: 시험에 나올 만한 핵심 내용을 ⭐ 표시와 함께 강조

**[수식 작성 규칙 — 반드시 준수]**
1. 수식은 항상 `$...$`(인라인) 또는 `$$...$$`(블록)으로만 표기하세요.
2. 백틱(`) 코드 스팬 안에 수식 기호를 절대 넣지 마세요.
   - 잘못된 예: `` `$x_i$` ``, `` `i_{{\\bar{{A}}}}$` ``, `` `$x_i`, `$y_j` ``
   - 올바른 예: `$x_i$`, `$i_{{\\bar{{A}}}}$`
3. 수식을 코드 블록(```) 안에 넣지 마세요 — 코드 블록 내 주석에도 $ LaTeX을 쓰지 마세요.
4. 수학 변수·기호는 백틱 코드 스팬이 아닌 `$...$` 수식으로 표기하세요.
5. 백틱과 달러 기호를 절대 혼용하지 마세요 (예: `` `...$ `` 또는 `` $...` ``).

불필요한 인사말 없이 바로 본론만 작성해 주세요."""


def _parse_md_sections(md_text: str) -> tuple[str, dict[int, str]]:
    """md 파일을 (헤더, {슬라이드번호: 섹션텍스트}) 로 파싱합니다.
    기존에 생성된 md 파일 형식과 호환됩니다."""
    parts = re.split(r"\n(?=## Slide \d+\n)", md_text)
    header = parts[0] + "\n"
    sections: dict[int, str] = {}
    for part in parts[1:]:
        m = re.match(r"## Slide (\d+)\n", part)
        if m:
            sections[int(m.group(1))] = part
    return header, sections


def find_failed_slides(output_md: Path) -> set[int]:
    """기존 .md에서 오류가 발생했던 슬라이드 번호 집합을 반환합니다."""
    if not output_md.exists():
        return set()

    _, sections = _parse_md_sections(output_md.read_text(encoding="utf-8"))
    return {
        num
        for num, text in sections.items()
        if "*오류 발생으로 해설을 생성하지 못했습니다.*" in text
        or "*빈 슬라이드이거나 응답을 생성할 수 없었습니다.*" in text
    }


def _extract_page_warning(page_num: int) -> str | None:
    """현재까지 누적된 MuPDF warnings 중 마지막 경고를 가져옵니다."""
    warnings_text = fitz.TOOLS.mupdf_warnings().strip()
    if not warnings_text:
        return None
    return f"[페이지 {page_num}] {warnings_text}"


def _process_slide(
    page: fitz.Page,
    prompt: str,
    page_num: int,
    delay: float,
    warning_logs: list[str] | None = None,
) -> str:
    """슬라이드 한 장을 처리하고 마크다운 섹션 텍스트를 반환합니다."""
    try:
        with _mupdf_lock:
            fitz.TOOLS.reset_mupdf_warnings()
            pix = page.get_pixmap(dpi=150)
            warning = _extract_page_warning(page_num)

        if warning and warning_logs is not None:
            warning_logs.append(warning)

        img = Image.open(io.BytesIO(pix.tobytes("png")))
        response = client.models.generate_content(model=MODEL_ID, contents=[prompt, img])

        if response.text:
            content = response.text
        else:
            finish_reason = "unknown"
            if response.candidates:
                finish_reason = str(response.candidates[0].finish_reason)
            print(f"  [경고] 슬라이드 {page_num}: 빈 응답 (finish_reason={finish_reason})")
            content = "*빈 슬라이드이거나 응답을 생성할 수 없었습니다.*"

        time.sleep(delay)
    except Exception as e:
        print(f"  [오류] 슬라이드 {page_num}: {e}")
        content = "*오류 발생으로 해설을 생성하지 못했습니다.*"

    return f"## Slide {page_num}\n\n{content}\n\n---\n\n"


def explain_pdf(
    pdf_path: Path,
    output_md: Path,
    delay: float = 2.0,
    target_slides: set[int] | None = None,
    save_warning_log: bool = False,
    label: str = "",
):
    tag = f"[{label or pdf_path.name}]"
    print(f"\n{tag} 분석을 시작합니다... ({pdf_path})")

    warning_logs: list[str] = []
    course_context = get_course_context(pdf_path)
    prompt = build_prompt(course_context)

    with fitz.open(str(pdf_path)) as doc:
        if target_slides:
            if not output_md.exists():
                print(f"{tag} [오류] '{output_md}'이 없습니다. 먼저 전체 처리를 실행하세요.")
                return

            print(f"{tag} 슬라이드 {sorted(target_slides)} 재처리 중...")
            header, sections = _parse_md_sections(output_md.read_text(encoding="utf-8"))

            for num in sorted(target_slides):
                if num < 1 or num > len(doc):
                    print(f"{tag} [경고] 슬라이드 {num}은 범위를 벗어납니다 (총 {len(doc)}장). 건너뜁니다.")
                    continue

                print(f"{tag} -> 슬라이드 {num}/{len(doc)} 재처리 중...")
                sections[num] = _process_slide(
                    doc.load_page(num - 1),
                    prompt,
                    num,
                    delay,
                    warning_logs,
                )

            full_notes = header + "".join(sections[n] for n in sorted(sections))
        else:
            course_code = next(
                (p.upper() for p in pdf_path.parts if p.upper() in COURSE_CONTEXTS),
                "CS",
            )
            full_notes = f"# {course_code} - {pdf_path.stem} 상세 해설 노트\n\n"
            full_notes += "> 이 노트는 Gemini 2.5 Flash를 이용해 자동 생성되었습니다.\n\n---\n\n"

            for page_num in range(len(doc)):
                print(f"{tag} -> 슬라이드 {page_num + 1}/{len(doc)} 처리 중...")
                full_notes += _process_slide(
                    doc.load_page(page_num),
                    prompt,
                    page_num + 1,
                    delay,
                    warning_logs,
                )

    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_md.write_text(full_notes, encoding="utf-8")
    print(f"{tag} 완료 -> [{output_md}]")

    if save_warning_log and warning_logs:
        warning_path = output_md.with_suffix(".mupdf_warnings.log")
        warning_path.write_text("\n\n".join(warning_logs), encoding="utf-8")
        print(f"{tag} MuPDF 경고 로그 저장 -> [{warning_path}]")


def collect_pdfs(targets: list[str]) -> list[tuple[Path, Path]]:
    """
    타겟 경로 목록을 받아 (pdf_path, output_md_path) 쌍의 리스트를 반환합니다.
    타겟이 디렉토리면 그 안의 모든 PDF를, 파일이면 그 파일 하나를 처리합니다.
    """
    pairs: list[tuple[Path, Path]] = []
    for target in targets:
        p = Path(target)
        if p.is_dir():
            for pdf in sorted(p.glob("**/*.pdf")):
                pairs.append((pdf, pdf.with_suffix(".md")))
        elif p.is_file() and p.suffix.lower() == ".pdf":
            pairs.append((p, p.with_suffix(".md")))
        else:
            print(f"[경고] '{target}'은 PDF 파일이나 디렉토리가 아닙니다. 건너뜁니다.")
    return pairs


def main():
    parser = argparse.ArgumentParser(
        description="PDF 강의 슬라이드를 Gemini AI로 자동 해설하여 마크다운 노트를 생성합니다.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
사용 예시:
  python script.py CSED226/numpy.pdf                    # 단일 파일 처리 (numpy.md 생성)
  python script.py CSED226/                             # 디렉토리 내 모든 PDF 처리
  python script.py CSED226/numpy.pdf CSED226/pandas.pdf # 여러 파일 처리
  python script.py CSED226/numpy.pdf -o notes/numpy_note.md
  python script.py CSED226/ --delay 3
  python script.py CSED226/numpy.pdf --retry
  python script.py CSED226/numpy.pdf --slides 3,7,12
  python script.py CSED233/ --save-warning-log          # MuPDF 경고는 파일로만 저장
  python script.py CSED233/ --show-mupdf-messages       # MuPDF 메시지를 콘솔에 표시
        """,
    )
    parser.add_argument(
        "targets",
        nargs="+",
        help="처리할 PDF 파일 또는 디렉토리 경로 (여러 개 지정 가능)",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="출력 마크다운 파일 경로 (단일 파일 처리 시에만 사용 가능)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=2.0,
        help="슬라이드 처리 간 대기 시간(초), 기본값: 2.0",
    )
    parser.add_argument(
        "--retry",
        action="store_true",
        help="기존 .md에서 오류가 발생한 슬라이드를 자동으로 감지해 재처리",
    )
    parser.add_argument(
        "--slides",
        help="재처리할 슬라이드 번호 (쉼표 구분, 예: 3,7,12)",
    )
    parser.add_argument(
        "--show-mupdf-messages",
        action="store_true",
        help="기본적으로 숨기는 MuPDF 내부 경고/오류 메시지를 콘솔에 표시",
    )
    parser.add_argument(
        "--save-warning-log",
        action="store_true",
        help="MuPDF 내부 경고를 콘솔 대신 .mupdf_warnings.log 파일로 저장",
    )
    parser.add_argument(
        "--workers", "-j",
        type=int,
        default=1,
        metavar="N",
        help="PDF 파일을 병렬 처리할 워커 수 (기본값: 1)",
    )

    args = parser.parse_args()

    configure_pymupdf(show_messages=args.show_mupdf_messages)

    pairs = collect_pdfs(args.targets)
    if not pairs:
        print("처리할 PDF 파일이 없습니다.")
        sys.exit(1)

    if args.output:
        if len(pairs) > 1:
            print("[오류] -o/--output 옵션은 단일 파일 처리 시에만 사용할 수 있습니다.")
            sys.exit(1)
        pairs = [(pairs[0][0], Path(args.output))]

    manual_slides: set[int] = set()
    if args.slides:
        try:
            manual_slides = {int(s.strip()) for s in args.slides.split(",")}
        except ValueError:
            print("[오류] --slides 인자는 쉼표로 구분된 숫자여야 합니다. 예: 3,7,12")
            sys.exit(1)

    workers = min(args.workers, len(pairs))
    print(f"총 {len(pairs)}개 파일을 처리합니다." + (f" (워커 {workers}개 병렬)" if workers > 1 else ""))

    def process_one(idx_pair):
        idx, (pdf_path, output_md) = idx_pair
        label = f"{idx}/{len(pairs)} {pdf_path.name}"
        target_slides: set[int] | None = None
        if args.retry or manual_slides:
            target_slides = manual_slides.copy()
            if args.retry:
                failed = find_failed_slides(output_md)
                if failed:
                    print(f"[{label}] 오류 슬라이드 감지: {sorted(failed)}")
                target_slides |= failed

            if not target_slides:
                print(f"[{label}] 재처리할 슬라이드 없음, 건너뜁니다.")
                return

        explain_pdf(
            pdf_path,
            output_md,
            delay=args.delay,
            target_slides=target_slides,
            save_warning_log=args.save_warning_log,
            label=label,
        )

    if workers <= 1:
        for item in enumerate(pairs, 1):
            process_one(item)
    else:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(process_one, item): item for item in enumerate(pairs, 1)}
            for future in as_completed(futures):
                exc = future.exception()
                if exc:
                    _, (pdf_path, _) = futures[future]
                    print(f"[오류] {pdf_path}: {exc}")

    print("\n모든 작업이 완료되었습니다!")


if __name__ == "__main__":
    main()
