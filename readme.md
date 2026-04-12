# Autonotes

POSTECH CSE 강의 슬라이드(PDF)를 Gemini 2.5 Flash로 페이지별 자동 해설하고, PDF와 노트를 나란히 볼 수 있는 뷰어입니다.

**온라인 뷰어 →** [junnnnnw00.github.io/autonotes](https://junnnnnw00.github.io/autonotes/)

> 강의자료 저작권 이슈로 외부 유출은 자제해 주세요.
> 새 노트를 추가해 PR을 보내거나, 다른 과목에 맞게 포크하는 것을 환영합니다.

---

## 설치

```bash
git clone https://github.com/junnnnnw00/autonotes.git
cd autonotes
pip install -r requirements.txt
```

`.env` 파일을 생성하고 [Google AI Studio](https://aistudio.google.com/)에서 발급한 API 키를 입력합니다.

```
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

---

## 노트 생성

```bash
# 단일 파일
python script.py CSED233/8_sorting.pdf

# 디렉토리 전체
python script.py CSED233/

# 여러 파일
python script.py CSED226/numpy.pdf CSED226/pandas.pdf
```

PDF와 같은 위치에 동일한 이름의 `.md` 파일이 생성됩니다.
디렉토리 이름에 과목 코드(예: `CSED233/`)가 포함되면 과목 특화 프롬프트가 자동 적용됩니다.

각 슬라이드마다 **핵심 개념**, **코드/수식 해설**, **구체적 예시**, **시험 포인트(⭐)** 가 포함됩니다.

### 옵션

| 옵션 | 기본값 | 설명 |
|---|---|---|
| `--delay N` | `2.0` | 슬라이드 처리 간 대기 시간(초) — Rate Limit 방지 |
| `-j N`, `--workers N` | `1` | 파일 단위 병렬 처리 워커 수 |
| `--retry` | — | 이전에 오류가 발생한 슬라이드만 재처리 |
| `--slides 3,7,12` | — | 특정 슬라이드 번호만 재처리 |
| `-o`, `--output <path>` | — | 출력 경로 지정 (단일 파일 처리 시에만) |
| `--save-warning-log` | — | MuPDF 경고를 `.mupdf_warnings.log`에 저장 |

```bash
# 3개 워커로 병렬 처리
python script.py CSED226/ -j 3

# 오류 슬라이드만 재처리
python script.py CSED226/numpy.pdf --retry

# 특정 슬라이드 재처리
python script.py CSED226/numpy.pdf --slides 3,7,12
```

---

## 로컬 뷰어

```bash
python viewer.py
```

브라우저가 자동으로 열리고 `http://localhost:7788`에서 PDF와 노트를 나란히 볼 수 있습니다.

### 단축키

| 키 | 동작 |
|---|---|
| `[` / `]` | 이전 / 다음 슬라이드 |
| `Ctrl + ←` / `→` | 이전 / 다음 슬라이드 (PDF 동기화) |
| `t` | 목차(TOC) 열기/닫기 |
| `p` | 인쇄 / PDF 저장 |
| `Ctrl + \` | 사이드바 접기/펼치기 |

### 주요 기능

| 기능 | 설명 |
|---|---|
| 분할 화면 | 가운데 구분선 드래그로 비율 조절, 더블클릭으로 노트 전체화면 |
| PDF↔노트 동기화 | PDF 페이지 이동 시 해당 슬라이드 노트로 자동 스크롤 (⇄ 버튼으로 토글) |
| 목차(TOC) | 오른쪽 가장자리의 `‹` 탭 클릭 — 스크롤 위치 자동 하이라이트 |
| 줌 | `−` / `+` 버튼, 퍼센트 클릭으로 100% 초기화 |
| 테마 | `☀/☾` 버튼으로 라이트/다크 모드 전환 |
| PWA | 홈 화면에 추가하여 앱처럼 사용 가능 |

---

## 배포 (GitHub Pages)

`viewer.py`의 HTML을 수정한 뒤:

```bash
python build_static.py
git add index.html pdfview.html files.json
git commit -m "chore: rebuild static site"
git push
```

Push 후 방문자에게 업데이트 알림이 표시됩니다 (PWA Service Worker 기반).

---

## 지원 과목

[POSTECH CSE 교과목](https://cse.postech.ac.kr/csepostech/admissions/under-subjects.do) 전체를 지원합니다.
새 과목은 `script.py`의 `COURSE_CONTEXTS` 딕셔너리에 항목을 추가하면 됩니다.

<details>
<summary>전체 목록 펼치기</summary>

| 과목 코드 | 과목명 | 학년 |
|---|---|---|
| CSED101 | 프로그래밍과 문제해결 | 1 |
| CSED103 | 프로그래밍 입문 | 1 |
| CSED105 | 인공지능 기초 | 1 |
| CSED211 | 컴퓨터시스템개론 | 2 |
| CSED212 | 프로그래밍 스튜디오 | 2 |
| CSED226 | 데이터분석 입문 | 2 |
| CSED232 | 소프트웨어 작성 원리 | 2 |
| CSED233 | 데이터구조 | 2 |
| CSED261 | 전산수학 | 2 |
| CSED273 | 디지털시스템 설계 | 2 |
| CSED312 | 운영체제 | 3 |
| CSED321 | 프로그래밍언어 | 3 |
| CSED331 | 알고리즘 | 3 |
| CSED332 | 소프트웨어 설계방법 | 3 |
| CSED341 | 오토마타 및 형식언어 | 3 |
| CSED342 | 인공지능 | 3 |
| CSED343 | 기계학습을 위한 수학 | 3 |
| CSED352 | 데이터통신 | 3 |
| CSED353 | 컴퓨터네트워크 | 3 |
| CSED355 | 전산신호처리 | 3 |
| CSED356 | 인간-컴퓨터 상호작용 | 3 |
| CSED357 | 데이터베이스시스템 | 3 |
| CSED401 | 컴퓨터와 사회 | 4 |
| CSED403 | 블록체인 및 암호화폐 | 4 |
| CSED404 | 모바일 및 유비쿼터스 컴퓨팅 | 4 |
| CSED405 | GPU 및 가속컴퓨팅 | 4 |
| CSED415 | 컴퓨터보안 | 4 |
| CSED416 | P2P 네트워킹 | 4 |
| CSED417 | 사물인터넷 | 4 |
| CSED420 | 소프트웨어 검증 | 4 |
| CSED423 | 컴파일러 설계 | 4 |
| CSED425 | 임베디드시스템 프로그래밍 | 4 |
| CSED426 | 빅데이터 | 4 |
| CSED433 | 전산논리 | 4 |
| CSED434 | 고급 프로그래밍 | 4 |
| CSED441 | 컴퓨터비전 개론 | 4 |
| CSED451 | 컴퓨터그래픽스 | 4 |

</details>
