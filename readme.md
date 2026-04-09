# 📒 AUTONOTES

POSTECH CSED 과목 강의 슬라이드(PDF)를 **Gemini 2.5 Flash**로 페이지별 자동 해설하는 도구입니다.  
노트는 자유롭게 활용하시고, 코드 보완이나 다른 과목 추가도 환영합니다!

## 💾 과목 리스트

| 과목 코드 | 과목명 | 담당 교수 |
|-----------|--------|-----------|
| CSED226 | 데이터분석 입문 | 한욱신 교수님 |

## ⚙️ 설치 방법

1. 이 저장소를 클론합니다.
   ```bash
   git clone <repo-url>
   cd autonotes
   ```
2. 필요한 라이브러리를 설치합니다.
   ```bash
   pip install -r requirements.txt
   ```
3. `.env` 파일에 Gemini API 키를 설정합니다.
   ```
   GEMINI_API_KEY=YOUR_API_KEY_HERE
   ```

## 🚀 사용법

`script.py`를 **직접 수정하지 않고** 명령줄 인자로 처리할 파일을 지정합니다.

### 단일 파일 처리
```bash
python script.py CSED226/numpy.pdf
# → CSED226/numpy.md 생성
```

### 출력 경로 직접 지정
```bash
python script.py CSED226/numpy.pdf -o notes/numpy_note.md
```

### 디렉토리 내 PDF 전체 처리
```bash
python script.py CSED226/
# → CSED226/ 안의 모든 PDF에 대해 .md 파일 생성
```

### 여러 파일 한 번에 처리
```bash
python script.py CSED226/numpy.pdf CSED226/pandas.pdf CSED226/kNN.pdf
```

### API 호출 간격 조정 (Rate Limit 방지)
```bash
python script.py CSED226/ --delay 3
```

## 🤖 CSED 과목별 최적화

디렉토리 이름에 과목 코드(예: `CSED226/`)가 포함되어 있으면 과목 특화 프롬프트가 자동 적용됩니다.  
경로에 과목 코드가 없으면 일반 컴퓨터공학 전공 프롬프트가 사용됩니다.

지원 과목 목록 ([POSTECH CSE 교과목 안내](https://cse.postech.ac.kr/csepostech/admissions/under-subjects.do) 기준):

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

새 과목을 추가하려면 `script.py`의 `COURSE_CONTEXTS` 딕셔너리에 항목을 추가하면 됩니다.

## 📝 생성 노트 형식

각 슬라이드마다 다음 항목이 자동으로 포함됩니다:
- **핵심 개념** 설명
- **코드/수식 해설** (코드 블록 포함)
- **구체적 예시** (실생활 비유)
- **시험 포인트** (⭐ 표시)
