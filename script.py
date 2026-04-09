import os
import sys
import argparse
import fitz  # PyMuPDF
import google.generativeai as genai
from PIL import Image
import io
import time
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API 키를 찾을 수 없습니다. .env 파일에 GEMINI_API_KEY를 설정해 주세요.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

# CSED 과목별 특화 프롬프트 컨텍스트
COURSE_CONTEXTS = {
    "CSED226": "이 슬라이드는 데이터분석 입문 (CSED226) 강의 자료입니다. NumPy, pandas, scikit-learn 등의 라이브러리와 머신러닝 기초 개념이 주로 다뤄집니다.",
    "CSED211": "이 슬라이드는 자료구조 (CSED211) 강의 자료입니다. 알고리즘 복잡도, 배열, 연결 리스트, 트리, 그래프 등의 자료구조가 주로 다뤄집니다.",
    "CSED232": "이 슬라이드는 객체지향 프로그래밍 (CSED232) 강의 자료입니다. C++, 클래스, 상속, 다형성 등의 개념이 주로 다뤄집니다.",
    "CSED233": "이 슬라이드는 이산수학 (CSED233) 강의 자료입니다. 논리, 집합, 그래프 이론, 조합론 등이 주로 다뤄집니다.",
    "CSED312": "이 슬라이드는 운영체제 (CSED312) 강의 자료입니다. 프로세스, 스케줄링, 메모리 관리, 파일 시스템 등이 주로 다뤄집니다.",
    "CSED321": "이 슬라이드는 프로그래밍 언어 (CSED321) 강의 자료입니다. 언어 패러다임, 타입 시스템, 인터프리터 구현 등이 주로 다뤄집니다.",
    "CSED331": "이 슬라이드는 알고리즘 (CSED331) 강의 자료입니다. 정렬, 탐색, 동적 프로그래밍, 그래프 알고리즘 등이 주로 다뤄집니다.",
    "CSED404": "이 슬라이드는 딥러닝 (CSED404) 강의 자료입니다. 신경망, 역전파, CNN, RNN, Transformer 등이 주로 다뤄집니다.",
}

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
- **코드/수식 해설**: 코드나 수식이 있다면 한 줄씩 상세히 풀이 (코드 블록 사용)
- **구체적 예시**: 실제 동작 예시나 실생활 비유를 통해 이해를 도움
- **시험 포인트**: 시험에 나올 만한 핵심 내용을 ⭐ 표시와 함께 강조

불필요한 인사말 없이 바로 본론만 작성해 주세요."""

def explain_pdf(pdf_path: Path, output_md: Path, delay: float = 2.0):
    print(f"\n[{pdf_path}] 분석을 시작합니다...")

    doc = fitz.open(str(pdf_path))
    course_context = get_course_context(pdf_path)
    prompt = build_prompt(course_context)

    course_code = next(
        (p.upper() for p in pdf_path.parts if p.upper() in COURSE_CONTEXTS),
        "CS"
    )
    topic = pdf_path.stem

    full_notes = f"# {course_code} - {topic} 상세 해설 노트\n\n"
    full_notes += f"> 이 노트는 Gemini 2.5 Flash를 이용해 자동 생성되었습니다.\n\n---\n\n"

    for page_num in range(len(doc)):
        print(f"  -> 슬라이드 {page_num + 1}/{len(doc)} 처리 중...")

        page = doc.load_page(page_num)
        pix = page.get_pixmap(dpi=150)
        img = Image.open(io.BytesIO(pix.tobytes()))

        try:
            response = model.generate_content([prompt, img])
            full_notes += f"## Slide {page_num + 1}\n\n"
            full_notes += response.text + "\n\n---\n\n"
            time.sleep(delay)
        except Exception as e:
            print(f"  [오류] 슬라이드 {page_num + 1}: {e}")
            full_notes += f"## Slide {page_num + 1}\n\n*오류 발생으로 해설을 생성하지 못했습니다.*\n\n---\n\n"

    output_md.parent.mkdir(parents=True, exist_ok=True)
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(full_notes)

    print(f"  완료 -> [{output_md}]")

def collect_pdfs(targets: list[str]) -> list[tuple[Path, Path]]:
    """
    타겟 경로 목록을 받아 (pdf_path, output_md_path) 쌍의 리스트를 반환합니다.
    타겟이 디렉토리면 그 안의 모든 PDF를, 파일이면 그 파일 하나를 처리합니다.
    """
    pairs = []
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
  python script.py CSED226/numpy.pdf           # 단일 파일 처리 (numpy.md 생성)
  python script.py CSED226/                    # 디렉토리 내 모든 PDF 처리
  python script.py CSED226/numpy.pdf CSED226/pandas.pdf  # 여러 파일 처리
  python script.py CSED226/numpy.pdf -o notes/numpy_note.md  # 출력 경로 지정
  python script.py CSED226/ --delay 3          # API 호출 간격 3초로 설정
        """
    )
    parser.add_argument(
        "targets",
        nargs="+",
        help="처리할 PDF 파일 또는 디렉토리 경로 (여러 개 지정 가능)"
    )
    parser.add_argument(
        "-o", "--output",
        help="출력 마크다운 파일 경로 (단일 파일 처리 시에만 사용 가능)"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=2.0,
        help="슬라이드 처리 간 대기 시간(초), 기본값: 2.0"
    )

    args = parser.parse_args()

    pairs = collect_pdfs(args.targets)

    if not pairs:
        print("처리할 PDF 파일이 없습니다.")
        sys.exit(1)

    if args.output:
        if len(pairs) > 1:
            print("[오류] -o/--output 옵션은 단일 파일 처리 시에만 사용할 수 있습니다.")
            sys.exit(1)
        pairs = [(pairs[0][0], Path(args.output))]

    print(f"총 {len(pairs)}개 파일을 처리합니다.")
    for pdf_path, output_md in pairs:
        explain_pdf(pdf_path, output_md, delay=args.delay)

    print("\n모든 작업이 완료되었습니다!")

if __name__ == "__main__":
    main()
