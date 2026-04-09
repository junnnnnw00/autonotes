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

다음 과목 코드가 경로에 포함되어 있으면 과목 특화 프롬프트가 자동 적용됩니다.

| 과목 코드 | 과목명 |
|-----------|--------|
| CSED226 | 데이터분석 입문 |
| CSED211 | 자료구조 |
| CSED232 | 객체지향 프로그래밍 |
| CSED233 | 이산수학 |
| CSED312 | 운영체제 |
| CSED321 | 프로그래밍 언어 |
| CSED331 | 알고리즘 |
| CSED404 | 딥러닝 |

경로에 과목 코드가 없으면 일반 컴퓨터공학 전공 프롬프트가 사용됩니다.  
`script.py`의 `COURSE_CONTEXTS` 딕셔너리에 과목을 추가하면 됩니다.

## 📝 생성 노트 형식

각 슬라이드마다 다음 항목이 자동으로 포함됩니다:
- **핵심 개념** 설명
- **코드/수식 해설** (코드 블록 포함)
- **구체적 예시** (실생활 비유)
- **시험 포인트** (⭐ 표시)
