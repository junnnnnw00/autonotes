# 📒 AUTONOTES

POSTECH CSED 과목 강의 슬라이드(PDF)를 **Gemini 2.5 Flash**로 페이지별 자동 해설하는 도구입니다.

> 🌐 **온라인 뷰어**: [junnnnnw00.github.io/autonotes](https://junnnnnw00.github.io/autonotes/)

- 강의자료 저작권 등의 이슈로 외부 유출은 자제 부탁드립니다.
- 새로운 노트를 추가하여 풀 리퀘스트 넣거나, 다른 과 과목에 맞게 포크하는 것을 적극 권장합니다.

---

## ⚙️ 설치

```bash
git clone https://github.com/junnnnnw00/autonotes.git
cd autonotes
pip install -r requirements.txt
```

`.env` 파일에 Gemini API 키를 설정합니다.

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

---

## 🚀 노트 생성 (`script.py`)

```bash
# 단일 파일
python script.py CSED226/numpy.pdf

# 디렉토리 내 PDF 전체
python script.py CSED226/

# 여러 파일
python script.py CSED226/numpy.pdf CSED226/pandas.pdf

# 출력 경로 지정 (단일 파일 시에만)
python script.py CSED226/numpy.pdf -o notes/numpy_note.md
```

디렉토리 이름에 과목 코드(예: `CSED226/`)가 포함되면 과목 특화 프롬프트가 자동 적용됩니다.

### 옵션

| 옵션 | 기본값 | 설명 |
|------|--------|------|
| `--delay N` | `2.0` | 슬라이드 처리 간 대기 시간(초), Rate Limit 방지 |
| `--workers N` / `-j N` | `1` | PDF 파일 단위 병렬 처리 워커 수 |
| `--retry` | — | 기존 .md에서 오류 슬라이드를 자동 감지해 재처리 |
| `--slides 3,7,12` | — | 특정 슬라이드만 재처리 |
| `--save-warning-log` | — | MuPDF 경고를 `.mupdf_warnings.log` 파일로 저장 |
| `--show-mupdf-messages` | — | MuPDF 내부 경고/오류를 콘솔에 표시 |

### 사용 예시

```bash
# 폴더 전체를 3개 워커로 병렬 처리
python script.py CSED226/ -j 3

# 오류 슬라이드 재처리 (병렬)
python script.py CSED226/ --retry -j 3

# 특정 슬라이드 + 오류 슬라이드 함께 재처리
python script.py CSED226/numpy.pdf --retry --slides 12

# API 호출 간격 늘리기
python script.py CSED226/ --delay 3
```

---

## 👀 뷰어 (`viewer.py`)

```bash
python viewer.py          # 현재 디렉토리 기준
python viewer.py CSED226  # 특정 폴더 지정
```

브라우저가 자동으로 열리고 PDF와 노트를 나란히 볼 수 있습니다.

| 기능 | 설명 |
|------|------|
| 파일 탐색 | 왼쪽 사이드바에서 클릭 → PDF(왼쪽) + 노트(오른쪽) 동시 표시 |
| 패널 크기 조절 | 가운데 구분선 드래그 / 더블클릭으로 노트 전체화면 |
| 사이드바 | `◀/▶` 버튼으로 열고 닫기, `⊘` 버튼으로 노트 없는 파일 숨기기 |
| 목차(TOC) | 오른쪽 가장자리에 마우스 올리면 목차 오버레이 표시, 스크롤 위치 자동 하이라이트 |
| PDF↔노트 동기화 | PDF 페이지 이동 시 해당 Slide 섹션으로 노트 자동 스크롤 (⇄ 버튼으로 토글) |
| 라이트/다크 모드 | `☀/☾` 버튼으로 노트 라이트모드 + PDF 다크모드 동시 전환, 설정 저장됨 |
| 마지막 파일 복원 | 다음 실행 시 마지막으로 열었던 파일 자동 복원 |

### 온라인 뷰어 (GitHub Pages)

`main` 브랜치에 push하면 GitHub Actions가 자동으로 정적 사이트를 빌드합니다.
수동 빌드:

```bash
python build_static.py
# → index.html, pdfview.html, files.json 생성
```

---

## 📝 생성 노트 형식

각 슬라이드마다 다음 항목이 자동으로 포함됩니다.

- **핵심 개념** 설명
- **코드/수식 해설** (코드 블록 + LaTeX 수식)
- **구체적 예시** (실생활 비유)
- **시험 포인트** (⭐ 표시)

---

## 📚 지원 과목

[POSTECH CSE 교과목 안내](https://cse.postech.ac.kr/csepostech/admissions/under-subjects.do) 기준으로 지원되며, 새 과목 추가는 `script.py`의 `COURSE_CONTEXTS`에 항목을 추가하면 됩니다.

| 과목 코드 | 과목명 | 분류 |
|-----------|--------|------|
| CSED101 | 프로그래밍과 문제해결 | 기초 |
| CSED103 | 프로그래밍 입문 | 기초 |
| CSED105 | 인공지능 기초 | 기초 |
| CSED211 | 컴퓨터시스템개론 | 2학년 |
| CSED212 | 프로그래밍 스튜디오 | 2학년 |
| CSED226 | 데이터분석 입문 | 2학년 |
| CSED232 | 소프트웨어 작성 원리 | 2학년 |
| CSED233 | 데이터구조 | 2학년 |
| CSED261 | 전산수학 | 2학년 |
| CSED273 | 디지털시스템 설계 | 2학년 |
| CSED312 | 운영체제 | 3학년 |
| CSED321 | 프로그래밍언어 | 3학년 |
| CSED331 | 알고리즘 | 3학년 |
| CSED332 | 소프트웨어 설계방법 | 3학년 |
| CSED341 | 오토마타 및 형식언어 | 3학년 |
| CSED342 | 인공지능 | 3학년 |
| CSED343 | 기계학습을 위한 수학 | 3학년 |
| CSED352 | 데이터통신 | 3학년 |
| CSED353 | 컴퓨터네트워크 | 3학년 |
| CSED355 | 전산신호처리 | 3학년 |
| CSED356 | 인간-컴퓨터 상호작용 | 3학년 |
| CSED357 | 데이터베이스시스템 | 3학년 |
| CSED401 | 컴퓨터와 사회 | 4학년 |
| CSED403 | 블록체인 및 암호화폐 | 4학년 |
| CSED404 | 모바일 및 유비쿼터스 컴퓨팅 | 4학년 |
| CSED405 | GPU 및 가속컴퓨팅 | 4학년 |
| CSED415 | 컴퓨터보안 | 4학년 |
| CSED416 | P2P 네트워킹 | 4학년 |
| CSED417 | 사물인터넷 | 4학년 |
| CSED420 | 소프트웨어 검증 | 4학년 |
| CSED423 | 컴파일러 설계 | 4학년 |
| CSED425 | 임베디드시스템 프로그래밍 | 4학년 |
| CSED426 | 빅데이터 | 4학년 |
| CSED433 | 전산논리 | 4학년 |
| CSED434 | 고급 프로그래밍 | 4학년 |
| CSED441 | 컴퓨터비전 개론 | 4학년 |
| CSED451 | 컴퓨터그래픽스 | 4학년 |
