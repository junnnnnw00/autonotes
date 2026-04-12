# CSED226 - pandas 상세 해설 노트

> 이 노트는 Gemini 2.5 Flash를 이용해 자동 생성되었습니다.

---

## Slide 1

**핵심 개념**:
*   **Pandas 라이브러리**: Python에서 데이터 분석 및 조작을 위한 핵심 오픈소스 라이브러리입니다. 특히 테이블 형태의 구조화된 데이터를 효율적으로 다루는 데 특화되어 있습니다.
*   **데이터 조작 (Data Manipulation)**: 데이터를 분석 가능한 형태로 만들고, 필요한 정보를 추출하며, 구조를 변경하는 모든 과정을 포함합니다. Pandas는 이 과정에서 데이터를 읽고(read), 선택하고(select), 필터링하며(filter), 정렬하고(sort), 그룹화(group)하는 등의 다양한 기능을 제공합니다.
*   **Pandas I**: 이번 슬라이드 세트는 Pandas의 기본적인 개념과 가장 필수적인 데이터 조작 기법에 대한 입문 과정을 다룹니다.

**코드/수식 해설**:
본 슬라이드는 강의의 제목 슬라이드이므로, 포함된 코드나 수식은 없습니다. Pandas 라이브러리의 기본적인 활용법은 추후 슬라이드에서 코드 예시와 함께 다루어질 예정입니다.

**구체적 예시**:
Pandas는 우리가 엑셀(Excel)이나 구글 스프레드시트(Google Sheets)에서 데이터를 정리하고 분석하는 작업을 파이썬 환경에서 프로그래밍 방식으로 수행할 수 있게 해준다고 생각하면 이해하기 쉽습니다. 예를 들어, 다음과 같은 상황에서 Pandas를 사용합니다:
*   CSV 파일이나 데이터베이스에서 데이터를 불러와 테이블 형태로 변환하기
*   특정 조건에 맞는 행이나 열을 선택하여 필터링하기 (예: 2023년 데이터만 보기)
*   누락된 값(missing values)을 처리하거나 잘못된 데이터를 수정하기
*   데이터를 합치거나 재구성하여 새로운 정보를 만들기

**시험 포인트**:
*   ⭐ **Pandas의 중요성**: 데이터 분석 과정에서 Pandas가 왜 필수적인 라이브러리인지, 어떤 유형의 데이터 조작에 주로 사용되는지 이해해야 합니다. 특히 데이터 전처리(preprocessing) 단계의 핵심 도구임을 강조합니다.
*   ⭐ **Pandas의 주요 자료구조 (예고)**: Pandas의 핵심 자료구조인 `Series`와 `DataFrame`에 대해 이 강의 이후에 깊이 있게 다룰 것이며, 이들이 어떻게 데이터를 표현하고 조작하는지 개념을 잡는 것이 중요합니다. (다음 강의에서 자세히 다룰 예정)

---

## Slide 2

POSTECH 컴퓨터공학과 전공 튜터입니다. CSED226 데이터분석 입문 강의의 'Pandas I: Introduction to Data Manipulation' 슬라이드 아웃라인에 대한 마크다운 노트를 작성해 드립니다.

---

### 1. Learning Objectives (학습 목표)

*   **핵심 개념**: 이 강의의 목표는 학생들에게 Python pandas 라이브러리를 사용하여 표 형식(tabular) 데이터를 다루는 기본적인 개념과 기술을 습득하게 하는 것입니다. CSV 파일 로딩부터 데이터 구조 이해, 기본적인 데이터 조작 및 선택 방법을 배우게 됩니다.
*   **코드/수식 해설**: N/A (학습 목표 자체에 대한 코드는 없음)
*   **구체적 예시**: 강의를 성공적으로 마치면, 여러분은 실제 데이터셋(예: 특정 지역의 날씨 데이터)을 pandas DataFrame으로 불러와서, 원하는 기간의 데이터를 선택하고, 평균 기온을 계산하는 등의 기본적인 분석 작업을 수행할 수 있게 됩니다.
*   **시험 포인트**: ⭐ 이 강의를 통해 얻게 될 핵심 역량들(예: DataFrame 생성, 데이터 선택 및 필터링, 기본적인 통계량 계산)을 이해하고 있어야 합니다.

### 2. Tabular Data (표 형식 데이터)

*   **핵심 개념**: 표 형식 데이터는 행(row)과 열(column)로 구성된 구조화된 데이터 형태를 말합니다. 각 열은 특정 속성(feature)을 나타내고, 각 행은 하나의 독립적인 관측치(observation) 또는 레코드(record)를 나타냅니다.
*   **코드/수식 해설**: N/A (개념 설명)
*   **구체적 예시**: 엑셀 스프레드시트, 관계형 데이터베이스의 테이블, CSV(Comma Separated Values) 파일 등이 대표적인 표 형식 데이터입니다. 예를 들어, 한 학급 학생들의 '이름', '학번', '성별', '점수' 등의 정보가 각 열에 있고, 각 학생이 하나의 행을 이루는 것이 표 형식 데이터의 전형적인 예시입니다.
*   **시험 포인트**: ⭐ 표 형식 데이터의 정의와 특징(행, 열, 속성, 관측치)을 정확히 이해하고, 다양한 데이터 소스에서 표 형식 데이터를 인식할 수 있어야 합니다.

### 3. Why Pandas? (왜 Pandas인가?)

*   **핵심 개념**: pandas는 Python에서 표 형식 데이터를 효율적이고 편리하게 다루기 위한 강력한 오픈소스 라이브러리입니다. 기존 Python의 리스트나 딕셔너리, NumPy 배열보다 구조화된 데이터(특히 표 형식)를 처리하는 데 특화되어 있으며, 데이터 정제, 변환, 분석, 시각화에 이르는 전 과정에 필수적인 기능을 제공합니다.
*   **코드/수식 해설**: N/A (개념 설명)
*   **구체적 예시**: 일반적인 Python 리스트로 대용량 CSV 파일을 처리하려면 복잡한 반복문과 조건문을 직접 작성해야 하지만, pandas를 사용하면 `pd.read_csv()` 한 줄로 데이터를 불러오고, `df.groupby()`나 `df.filter()`와 같은 직관적인 메서드로 복잡한 데이터 조작을 쉽게 수행할 수 있습니다.
*   **시험 포인트**: ⭐ pandas를 사용하는 주된 이유(데이터 조작의 용이성, 높은 효율성, 풍부한 내장 기능, 결측치 처리 등)를 설명할 수 있어야 합니다.

### 4. Data Structures (데이터 구조)

*   **핵심 개념**: pandas의 핵심 데이터 구조는 `Series`와 `DataFrame`입니다.
    *   **Series**: 1차원 배열과 유사한 객체로, 데이터와 인덱스(label)로 구성됩니다. 각 요소에 접근할 때 인덱스를 사용할 수 있습니다.
    *   **DataFrame**: 2차원 테이블 형태의 객체로, 여러 개의 `Series`가 열(column)로 모여 행과 열을 이룹니다. 행 인덱스(index)와 열 이름(columns)을 모두 가집니다.
*   **코드/수식 해설**:
    ```python
    import pandas as pd
    import numpy as np

    # Series 생성 예시
    s = pd.Series([10, 20, 30, np.nan, 50], index=['a', 'b', 'c', 'd', 'e'])
    print("Series:\n", s)

    # DataFrame 생성 예시 (딕셔너리로부터)
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'Los Angeles', 'Chicago']}
    df = pd.DataFrame(data)
    print("\nDataFrame:\n", df)
    ```
*   **구체적 예시**: `Series`는 엑셀 스프레드시트의 단일 열(예: 학생들의 키 목록)에 비유할 수 있습니다. `DataFrame`은 전체 엑셀 시트(예: 학생들의 이름, 키, 몸무게, 나이 등 모든 정보)에 해당합니다. `Series`는 `DataFrame`의 한 열이기도 합니다.
*   **시험 포인트**: ⭐ `Series`와 `DataFrame`의 정의, 차이점(차원, 구성 요소), 그리고 각 데이터 구조를 생성하는 기본적인 방법을 설명하고 예시 코드를 작성할 수 있어야 합니다.

### 5. Working with Series (Series 다루기)

*   **핵심 개념**: `Series`는 단일 열 데이터를 다루기 위한 객체로, 인덱스를 이용한 접근, 슬라이싱, 불리언 인덱싱을 통한 조건부 선택, 그리고 벡터화된 연산(arithmetic operations)을 지원합니다.
*   **코드/수식 해설**:
    ```python
    import pandas as pd
    s = pd.Series([10, 20, 30, 40, 50], index=['A', 'B', 'C', 'D', 'E'])

    # 인덱스를 이용한 접근
    print(f"Index 'B' value: {s['B']}") # 출력: 20

    # 위치를 이용한 접근 (인덱스는 정수)
    print(f"Position 2 value: {s[2]}") # 출력: 30

    # 슬라이싱
    print("\nSliced Series (index 'B' to 'D'):\n", s['B':'D']) # 출력: B 20, C 30, D 40 (종료 인덱스 포함)
    print("\nSliced Series (position 1 to 3, exclusive):\n", s[1:4]) # 출력: B 20, C 30, D 40

    # 조건부 선택 (불리언 인덱싱)
    print("\nValues greater than 30:\n", s[s > 30]) # 출력: D 40, E 50

    # 벡터화 연산
    print("\nSeries * 2:\n", s * 2) # 각 요소에 2를 곱함
    ```
*   **구체적 예시**: 특정 도시의 월별 평균 강수량 데이터가 `Series`로 있다고 가정해 봅시다. `s['July']`로 7월 강수량을 확인하고, `s[s > 100]`으로 강수량이 100mm를 초과하는 월만 필터링할 수 있습니다.
*   **시험 포인트**: ⭐ `Series`의 인덱싱(라벨 및 정수 위치), 슬라이싱, 그리고 불리언 인덱싱을 이용한 조건부 선택 방법을 자유롭게 사용할 수 있어야 합니다.

### 6. Working with DataFrames (DataFrame 다루기)

*   **핵심 개념**: `DataFrame`은 2차원 표 형식 데이터를 다루는 주요 객체입니다. 열(column) 선택, 행(row) 선택, 새로운 열 추가, 기존 열 수정, 그리고 `head()`, `info()`, `describe()` 등과 같은 탐색적 데이터 분석(EDA)을 위한 유용한 메서드를 제공합니다.
*   **코드/수식 해설**:
    ```python
    import pandas as pd
    data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [25, 30, 35, 40],
            'City': ['NY', 'LA', 'SF', 'NY'],
            'Salary': [70000, 80000, 90000, 75000]}
    df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])

    # 특정 열 선택 (Series 반환)
    print("Selected 'Name' column:\n", df['Name'])

    # 여러 열 선택 (DataFrame 반환)
    print("\nSelected 'Name' and 'City' columns:\n", df[['Name', 'City']])

    # 새로운 열 추가
    df['Years_Exp'] = [2, 7, 12, 5]
    print("\nDataFrame with new 'Years_Exp' column:\n", df)

    # 기본 통계량 요약
    print("\nDescriptive statistics:\n", df.describe())
    ```
*   **구체적 예시**: 고객 데이터 `DataFrame`에서 '주문 금액' 열만 선택하여 총합을 구하거나, '고객 등급'이 VIP인 고객들에게 새로운 할인율 열을 추가할 수 있습니다. `df.head()`를 사용하여 데이터의 상위 몇 행을 빠르게 확인하는 것은 데이터 탐색의 첫 단계입니다.
*   **시험 포인트**: ⭐ `DataFrame`에서 특정 열 또는 여러 열을 선택하는 방법, 새로운 열을 추가하거나 기존 열을 수정하는 방법, `describe()`, `info()`, `head()` 등 기본적인 데이터 탐색 함수들의 활용법을 숙지해야 합니다.

### 7. Data Selection (데이터 선택)

*   **핵심 개념**: `DataFrame`에서 특정 행, 열 또는 특정 조건을 만족하는 데이터를 정확하게 선택하기 위해 `loc`, `iloc`, 그리고 불리언 인덱싱을 사용합니다.
    *   `df.loc[]`: 라벨(index/column name) 기반으로 데이터를 선택합니다. `df.loc[row_label, col_label]` 형식입니다.
    *   `df.iloc[]`: 정수 위치(integer position) 기반으로 데이터를 선택합니다. `df.iloc[row_position, col_position]` 형식입니다.
    *   **불리언 인덱싱**: 조건을 만족하는 행만 선택하는 강력한 방법입니다.
*   **코드/수식 해설**:
    ```python
    import pandas as pd
    data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [25, 30, 35, 40],
            'City': ['NY', 'LA', 'SF', 'NY'],
            'Salary': [70000, 80000, 90000, 75000]}
    df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])

    # loc를 이용한 라벨 기반 선택
    print("df.loc['a', 'Name']:", df.loc['a', 'Name']) # 출력: Alice
    print("\ndf.loc[['a', 'c'], 'Salary']:\n", df.loc[['a', 'c'], 'Salary']) # 출력: a 70000, c 90000

    # iloc를 이용한 정수 위치 기반 선택
    print("\ndf.iloc[0, 1]:", df.iloc[0, 1]) # 출력: 25 (0번째 행, 1번째 열)
    print("\ndf.iloc[1:3, 0:2]:\n", df.iloc[1:3, 0:2]) # 1,2번째 행과 0,1번째 열 선택

    # 불리언 인덱싱 (나이가 30 이상인 데이터 선택)
    print("\nEmployees with Age >= 30:\n", df[df['Age'] >= 30])

    # 여러 조건을 결합한 불리언 인덱싱 (City가 NY이고 Salary가 70000 초과)
    print("\nEmployees in NY with Salary > 70000:\n", df[(df['City'] == 'NY') & (df['Salary'] > 70000)])
    ```
*   **구체적 예시**: 특정 부서('HR')에 속하면서 급여가 5000만원 이상인 직원의 이름만 조회하거나, 특정 기간(예: 2023년 1월)의 주문 내역만 필터링하여 분석할 때 `loc`, `iloc`, 불리언 인덱싱을 활용합니다.
*   **시험 포인트**: ⭐ `loc`, `iloc`의 정확한 사용법과 차이점, 그리고 복수 조건을 포함한 불리언 인덱싱을 사용하여 원하는 데이터를 효율적으로 추출하는 능력이 매우 중요합니다.

### 8. Professional Development (전문 역량 개발)

*   **핵심 개념**: 데이터 분석가로서의 역량을 강화하기 위한 실용적인 조언, 효율적인 코드 작성법, 문제 해결 전략, 그리고 지속적인 학습 방법을 다룹니다. 이는 단순히 문법을 아는 것을 넘어 실제 프로젝트에 적용하고 발전시키는 데 필요한 부분입니다.
*   **코드/수식 해설**: N/A (이론 및 팁 위주)
*   **구체적 예시**:
    *   **효율적인 코드 작성**: `for` 루프 대신 pandas의 벡터화된 연산이나 내장 메서드를 활용하여 코드 성능을 최적화하는 방법.
    *   **디버깅 및 에러 처리**: 자주 발생하는 pandas 오류의 종류와 해결 방법.
    *   **추가 학습 리소스**: pandas 공식 문서, Stack Overflow, 데이터 과학 커뮤니티 등을 활용하는 방법.
    *   **버전 관리**: Git과 GitHub를 이용한 코드 관리 및 협업의 중요성.
*   **시험 포인트**: ⭐ 직접적인 코딩 문제보다는 데이터 분석 프로젝트를 수행하는 과정에서 발생할 수 있는 문제에 대한 접근 방식이나 효율적인 학습/작업 방법에 대한 이해도를 평가할 수 있습니다.

### 9. Summary (요약)

*   **핵심 개념**: 이번 강의에서 학습한 pandas의 주요 개념과 기술들을 간략하게 요약하고, 다음 강의로 이어지는 내용을 예고합니다. `Series`와 `DataFrame`의 이해, 데이터 생성 및 기본적인 조작, `loc`, `iloc`, 불리언 인덱싱을 통한 데이터 선택이 핵심 내용입니다.
*   **코드/수식 해설**: N/A (요약)
*   **구체적 예시**: "이번 강의를 통해 여러분은 pandas의 `Series`와 `DataFrame`이라는 강력한 데이터 구조를 이해하고, `pd.read_csv()`로 데이터를 불러와 `df.loc[]`와 불리언 인덱싱을 사용하여 필요한 데이터를 추출하는 방법을 배웠습니다. 다음 강의에서는 데이터 정제, 그룹화, 데이터 병합 등 좀 더 복잡한 데이터 조작 기법을 다룰 예정입니다." 와 같이 전체 내용을 간략히 되짚어줍니다.
*   **시험 포인트**: ⭐ 강의의 모든 핵심 개념들이 어떻게 연결되는지 큰 그림을 그릴 수 있어야 하며, 각 주제별로 가장 중요한 개념과 코드를 상기할 수 있어야 합니다.

---

## Slide 3

---
**핵심 개념**

*   **표 형식 데이터(Tabular Data)**:
    *   데이터 과학에서 가장 흔하게 접하고 중요한 데이터 형태로, 행(row)과 열(column)로 구성된 테이블 형태의 데이터를 의미합니다. 관계형 데이터베이스의 테이블, 엑셀 스프레드시트, CSV 파일 등이 대표적인 예시입니다.
    *   각 행은 개별적인 관측치(observation) 또는 레코드(record)를 나타내고, 각 열은 특정 속성(attribute) 또는 변수(variable)를 나타냅니다.
    *   데이터 분석의 시작점이자 많은 머신러닝 알고리즘의 입력 형태로 사용되므로, 이를 이해하고 다루는 능력이 매우 중요합니다.

*   **Pandas의 세 가지 기본 데이터 구조**:
    *   **Series**: 1차원 배열(array)과 유사한 객체로, 데이터(values)와 각 데이터에 연결된 인덱스(index)로 구성됩니다. 한 종류의 데이터 타입으로 구성되는 것이 일반적입니다.
    *   **DataFrame**: 2차원 테이블 형태의 데이터 구조로, 여러 개의 Series가 모여서 행과 열을 이룹니다. 각 열은 서로 다른 데이터 타입을 가질 수 있으며, 스프레드시트나 SQL 테이블과 유사하게 데이터를 표현합니다.
    *   **Index**: Pandas 객체의 각 데이터 항목을 고유하게 식별하는 레이블 또는 위치를 제공하는 객체입니다. Series와 DataFrame의 행(row) 레이블로 사용되며, 데이터 접근, 정렬, 병합 등의 연산에 핵심적인 역할을 합니다.

*   **DataFrame 생성**:
    *   다양한 소스(예: 파이썬 딕셔너리, NumPy 배열, CSV 파일, SQL 쿼리 등)로부터 DataFrame을 생성하는 방법을 학습합니다.

*   **데이터 선택(Selection) 및 슬라이싱(Slicing)**:
    *   DataFrame에서 특정 행, 열 또는 특정 조건을 만족하는 데이터를 추출하는 작업을 의미합니다. `loc`, `iloc`, 불리언 인덱싱(Boolean indexing)과 같은 메서드를 사용하여 데이터를 효율적으로 탐색하고 추출하는 기법을 다룹니다.

*   **전문적인 데이터 조작(Data Manipulation) 기법**:
    *   결측치 처리, 데이터 타입 변환, 데이터 병합, 그룹화, 피벗팅 등 실제 데이터 분석 과정에서 필요한 다양한 데이터 전처리 및 변환 기술을 학습합니다.

**코드/수식 해설**

이 슬라이드는 학습 목표를 제시하므로 직접적인 코드나 수식은 포함되어 있지 않습니다. 하지만 앞으로 다루게 될 핵심적인 pandas 코드 패턴은 다음과 같습니다.

*   **Pandas 라이브러리 임포트**:
    ```python
    import pandas as pd
    ```

*   **Series 생성 (예시)**:
    ```python
    s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
    print(s)
    ```

*   **DataFrame 생성 (딕셔너리 예시)**:
    ```python
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'London', 'Paris']}
    df = pd.DataFrame(data)
    print(df)
    ```

*   **데이터 선택 및 슬라이싱 (`.loc` 예시)**:
    ```python
    # 'Name' 컬럼 선택
    print(df['Name'])

    # 인덱스 '0'과 '1' 행 선택
    print(df.loc[0:1])

    # 조건에 따른 행 선택
    print(df[df['Age'] > 28])
    ```
수식은 해당 강의에서 Pandas를 활용한 통계적 분석이나 머신러닝 모델의 수학적 배경을 다룰 때 등장할 수 있습니다. 예를 들어, 평균($\bar{x}$), 표준편차($\sigma$), 상관계수($r$) 등의 통계량이 Pandas를 통해 계산될 수 있습니다.

**구체적 예시**

*   **표 형식 데이터**: 여러분의 학번, 이름, 전공, 학점, 수강 과목 점수 등이 엑셀 파일이나 CSV 파일 형태로 저장되어 있다고 상상해보세요. 이것이 바로 전형적인 표 형식 데이터입니다.
*   **Pandas 데이터 구조**:
    *   **Series**: 한 학생의 특정 과목 점수들(`[90, 85, 92]`)을 인덱스(`['중간', '기말', '과제']`)와 함께 저장한 것이 Series의 예시가 될 수 있습니다.
    *   **DataFrame**: 여러 학생의 이름, 학번, 전공, 각 과목 점수 등의 정보가 하나의 표로 정리된 것이 DataFrame입니다. 각 학생은 한 행(row)이 되고, 이름, 학번, 전공 등은 각 열(column)이 됩니다.
    *   **Index**: DataFrame에서 각 학생의 고유한 학번을 인덱스로 사용하여, 특정 학번으로 바로 해당 학생의 정보를 찾아볼 수 있습니다.
*   **데이터 선택 및 슬라이싱**: CSED226 과목을 수강하는 학생들 중에서 컴퓨터공학과 학생들만 필터링하거나, 중간고사 점수가 90점 이상인 학생들의 이름만 선택하는 것 등이 데이터 선택 및 슬라이싱의 예시입니다.
*   **전문적인 데이터 조작**: 설문조사 데이터에서 응답하지 않은 문항(결측치)을 평균값으로 채우거나, '학년' 데이터를 '정수형'으로 변환하고, 특정 지역별로 데이터를 그룹화하여 평균 점수를 계산하는 등의 작업이 여기에 해당합니다.

**시험 포인트**

*   ⭐ **Pandas Series와 DataFrame의 개념, 특징, 그리고 각각 어떤 상황에서 주로 사용되는지 명확히 이해하고 구분할 수 있어야 합니다.** 특히 1차원 vs 2차원, 단일 데이터 타입 vs 혼합 데이터 타입의 차이를 알아두세요.
*   ⭐ **DataFrame을 생성하는 다양한 방법 (예: 딕셔너리, 리스트의 리스트, CSV 파일 읽기)을 숙지하고, 각 방법의 장단점을 설명할 수 있어야 합니다.**
*   ⭐ **`.loc`, `.iloc` 메서드를 이용한 데이터 선택 및 슬라이싱 방법에 대한 이해는 필수입니다.** 이들의 차이점(레이블 기반 vs 정수 위치 기반)과 올바른 사용법을 코드 예시와 함께 설명할 수 있어야 합니다. 불리언 인덱싱을 활용한 조건부 선택도 중요합니다.
*   ⭐ **실제 데이터셋이 주어졌을 때, 학습 목표에 해당하는 데이터 조작(선택, 필터링, 컬럼 추가/삭제 등) 코드를 작성할 수 있는 실습 능력이 요구됩니다.**
---

---

## Slide 4

---
### **핵심 개념**
*   **표 형식 데이터(Tabular Data)의 정의**: 데이터 과학에서 정보를 저장하는 가장 일반적이고 유연한 방식 중 하나로, 행(rows)과 열(columns)의 형태로 구성된 표 형식의 데이터를 의미합니다.

*   **표 형식 데이터의 구조**:
    *   **행(Rows)**: 각각의 행은 하나의 **관측치(observation)** 또는 **인스턴스(instance)**를 나타냅니다. 예를 들어, 한 명의 학생 정보나 특정 거래 내역 하나를 의미할 수 있습니다.
    *   **열(Columns)**: 각각의 열은 하나의 **특징(feature)** 또는 **특성(characteristic)**을 나타냅니다. 예를 들어, 학생의 학번, 이름, 성적, 키 등을 의미할 수 있습니다.
    *   **유연성(Flexibility)**: 표 형식 데이터는 직관적이어서 이해하기 쉽고, 데이터를 조작(manipulate)하거나 분석(analyze)하는 데 매우 용연합니다.

### **코드/수식 해설**
해당 슬라이드에는 직접적인 코드나 수식 해설 내용이 포함되어 있지 않습니다.

### **구체적 예시**
학생 성적 데이터를 예로 들어 보겠습니다.

| 학번 | 이름 | 과목 A | 과목 B | 총점 |
|---|---|---|---|---|
| 20230001 | 김철수 | 90 | 85 | 175 |
| 20230002 | 이영희 | 78 | 92 | 170 |
| 20230003 | 박민준 | 95 | 88 | 183 |

이 예시에서:
*   **행**: '20230001 김철수 90 85 175'와 같이 각 학생의 전체 정보가 하나의 **관측치(observation)** 또는 **인스턴스(instance)**에 해당합니다.
*   **열**: '학번', '이름', '과목 A', '과목 B', '총점'과 같이 각 학생을 설명하는 개별 **특징(feature)** 또는 **특성(characteristic)**에 해당합니다.

### **시험 포인트**
*   ⭐ **표 형식 데이터의 정의**를 명확히 설명할 수 있어야 합니다. (행과 열로 구성된 표 형식의 정보)
*   ⭐ **행(Row)**이 무엇을 의미하고(**observation**, **instance**), **열(Column)**이 무엇을 의미하는지(**feature**, **characteristic**) 정확하게 구분하고 설명할 수 있어야 합니다.
*   ⭐ 데이터 과학에서 표 형식 데이터가 **가장 일반적이고 유연한** 데이터 저장 방식 중 하나인 이유(이해, 조작, 분석 용이성)를 이해하고 있어야 합니다.

---

## Slide 5

- **핵심 개념**:
이 슬라이드는 데이터 분석에서 일반적으로 사용되는 테이블 형태의 데이터셋 구조를 "Elections Dataset"이라는 실제 사례를 통해 설명합니다.
*   **각 행 (Each row)**: 특정 연도의 한 대통령 후보자를 나타냅니다. 즉, 각 행은 분석의 대상이 되는 개별 "관측치(observation)" 또는 "샘플(sample)"입니다. 예를 들어, '2020년 조 바이든' 또는 '2016년 도널드 트럼프'와 같은 하나의 독립적인 정보를 담고 있습니다.
*   **각 열 (Each column)**: 후보자에 대한 특정 정보(특성, feature)를 나타냅니다. 여기에는 `Year` (연도), `Name` (후보자 이름), `Party` (소속 정당), `Popular Vote` (득표수), `Result` (선거 결과), `Percentage` (득표율) 등이 포함됩니다. 각 열은 모든 후보자에 대해 동일한 종류의 데이터를 제공합니다.

- **코드/수식 해설**:
본 슬라이드에는 직접적인 코드나 수식이 제시되어 있지 않습니다. 하지만 이러한 데이터셋 구조는 `pandas` 라이브러리의 `DataFrame` 객체와 직접적으로 매핑됩니다.
각 행은 `DataFrame`의 인덱스(또는 특정 키)에 해당하는 관측치를, 각 열은 `DataFrame`의 컬럼 이름에 해당하는 특성(피처)을 나타냅니다.

- **구체적 예시**:
"Elections Dataset"이 실제로 어떻게 구성될 수 있는지 간단한 표 형태로 시각화하면 다음과 같습니다.

| Year | Name          | Party         | Popular Vote | Result | Percentage |
| :--- | :------------ | :------------ | :----------- | :----- | :--------- |
| 2020 | Joe Biden     | Democratic    | 81284778     | Won    | 51.3%      |
| 2020 | Donald Trump  | Republican    | 74223369     | Lost   | 46.8%      |
| 2016 | Donald Trump  | Republican    | 62984828     | Won    | 46.1%      |
| 2016 | Hillary Clinton | Democratic    | 65853514     | Lost   | 48.2%      |

위 표에서 각 줄(row)은 한 명의 후보자를 나타내며, 각 칸(column)은 해당 후보자의 특정 정보를 나타냅니다. 예를 들어, 첫 번째 행은 2020년 선거에 출마한 Joe Biden 후보의 정보를 담고 있습니다.

- **시험 포인트**:
*   ⭐ **데이터셋의 기본 구조 이해**: 데이터 분석에서 '행(row)'과 '열(column)'이 각각 무엇을 의미하는지 명확히 이해하는 것이 가장 중요합니다. 행은 '관측치(observation)', 열은 '특성(feature)' 또는 '변수(variable)'로 해석됩니다.
*   ⭐ **실제 데이터셋 예시 분석**: 주어진 실제 데이터셋(예: 선거 데이터셋)에 대해 "각 행이 무엇을 나타내는가?", "각 열이 무엇을 나타내는가?"와 같은 질문에 답할 수 있어야 합니다. 이는 향후 데이터 로딩 및 전처리 과정에서 데이터를 올바르게 해석하고 조작하는 데 필수적인 능력입니다.

---

## Slide 6

### **핵심 개념**
Pandas는 데이터 분석 및 조작을 위한 Python의 핵심 라이브러리입니다. 특히 표 형식(tabular) 데이터 처리의 **업계 표준 도구**로, 학계와 산업계 모두에서 널리 사용됩니다. Pandas의 주요 강점은 데이터를 효율적으로 구성하고, 특정 조건을 기반으로 정보를 추출하며, 통찰력을 얻기 위한 다양한 데이터 연산을 수행하는 능력에 있습니다. 또한, NumPy 함수를 효율적으로 활용하고 벡터화된 연산을 통해 빠른 데이터 처리를 지원합니다.

### **코드/수식 해설**

**1. Pandas DataFrame 기본 생성 및 확인**
Pandas는 주로 `DataFrame`이라는 2차원 표 형식 데이터 구조를 사용합니다.

```python
import pandas as pd
import numpy as np

# 딕셔너리를 이용한 DataFrame 생성 예시
data = {
    '이름': ['김철수', '이영희', '박지성', '최민수'],
    '나이': [25, 30, 28, 32],
    '도시': ['서울', '부산', '서울', '제주'],
    '점수': [85, 92, 78, 95]
}
df = pd.DataFrame(data)
print("--- 기본 DataFrame ---")
print(df)
```

**2. 특정 조건으로 데이터 추출**
DataFrame에서 특정 조건을 만족하는 행(row)을 쉽게 필터링할 수 있습니다.

```python
# '나이'가 30세 이상인 데이터 추출
df_older_than_30 = df[df['나이'] >= 30]
print("\n--- 나이가 30세 이상인 데이터 ---")
print(df_older_than_30)

# '도시'가 '서울'인 데이터 추출
df_seoul = df[df['도시'] == '서울']
print("\n--- 도시가 서울인 데이터 ---")
print(df_seoul)
```

**3. 데이터 연산 및 NumPy 함수 적용**
데이터프레임의 열(Series)에 대해 통계 연산이나 NumPy 함수를 직접 적용할 수 있습니다.

```python
# '점수' 컬럼의 평균 계산
average_score = df['점수'].mean()
print(f"\n--- 평균 점수: {average_score} ---")

# 모든 '점수'에 5점 추가 (벡터화 연산)
df['조정_점수'] = df['점수'] + 5
print("\n--- 점수 조정 후 DataFrame ---")
print(df)

# NumPy의 log 함수 적용 예시
df['점수_로그'] = np.log(df['점수'])
print("\n--- 점수에 log 함수 적용 후 DataFrame ---")
print(df)
```

**수식 해설 (평균)**
데이터 연산을 통해 통찰력을 얻는 예시로, 특정 컬럼의 평균을 계산하는 것은 가장 기본적인 통계 연산 중 하나입니다. $N$개의 데이터 포인트 $x_1, x_2, \ldots, x_N$에 대한 산술 평균($\mu$)은 다음과 같이 계산됩니다.

$$ \mu = \frac{1}{N} \sum_{i=1}^{N} x_i $$
Pandas에서는 `df['컬럼명'].mean()`과 같이 간결하게 이 연산을 수행할 수 있습니다.

### **구체적 예시**

*   **표 형식 데이터 정리**: 학교에서 학생들의 학번, 이름, 전공, 수강 과목, 성적 정보를 Excel 스프레드시트처럼 행과 열로 깔끔하게 정리하는 것이 Pandas DataFrame의 역할입니다. 각 컬럼은 특정 속성을, 각 행은 개별 학생의 데이터를 나타냅니다.
*   **특정 조건 정보 추출**: 전공이 '컴퓨터공학'인 학생들만 보거나, 'A+' 학점을 받은 학생들만 골라내는 작업을 Pandas의 조건부 필터링 기능으로 손쉽게 할 수 있습니다.
*   **데이터 연산으로 통찰력**: 특정 과목의 전체 평균 점수를 계산하거나, 각 학생의 총점 대비 전공 과목 점수 비율을 계산하여 성적 추이를 분석하는 등의 작업을 Pandas로 수행할 수 있습니다.
*   **NumPy 함수 효율적 적용**: 대량의 숫자 데이터를 담고 있는 컬럼(예: 주식 가격 시계열 데이터)에 대해 제곱근, 로그 스케일링 등 복잡한 수치 연산을 NumPy의 기능을 활용하여 빠르게 적용할 수 있습니다.
*   **벡터화 연산의 속도**: 만약 수백만 줄의 데이터에서 모든 값에 10을 더해야 한다면, `for` 루프를 사용하면 매우 느릴 수 있습니다. Pandas는 `df['column'] + 10`과 같이 단 한 줄의 코드로 모든 요소에 동시에 연산을 적용하여 훨씬 빠르게 처리합니다. 이는 내부적으로 C/Fortran으로 구현된 효율적인 연산을 사용하기 때문입니다.

### **시험 포인트**

*   **Pandas의 역할과 중요성**: 데이터 분석 및 조작에 있어 왜 Pandas가 표준 도구로 인정받는지 ⭐ 설명할 수 있어야 합니다. (효율적인 표 형식 데이터 처리, 광범위한 기능 지원)
*   **Pandas의 주요 기능 5가지**: 슬라이드에 제시된 5가지 핵심 기능(표 형식 데이터 정리, 조건부 정보 추출, 데이터 연산, NumPy 연동, 벡터화 연산) ⭐을 정확히 이해하고 설명할 수 있어야 합니다.
*   **DataFrame과 Series**: Pandas의 핵심 데이터 구조인 DataFrame과 Series의 개념을 이해하고, 이들이 표 형식 데이터를 어떻게 표현하는지 ⭐ 알고 있어야 합니다.
*   **벡터화 연산의 이점**: 벡터화 연산이 무엇이며, 왜 데이터 처리 속도를 향상시키는 데 중요한지 ⭐ 설명할 수 있어야 합니다. (반복문 사용 대비 성능 우위)
*   **Pandas와 NumPy의 관계**: Pandas가 NumPy 위에 구축되어 있으며, NumPy 함수를 효율적으로 활용하는 방법에 대해 ⭐ 설명할 수 있어야 합니다.

---

## Slide 7

## Pandas의 세 가지 핵심 데이터 구조

### 1. Series

*   **핵심 개념**: Series는 **1차원 레이블이 있는 배열 데이터**입니다. 마치 하나의 열(column)처럼 생각할 수 있으며, 모든 값은 **동일한 데이터 타입**을 가집니다. 각 값에는 고유한 **인덱스(labels)**가 연결되어 있습니다.

*   **코드/수식 해설**:
    ```python
    import pandas as pd

    # 리스트로부터 Series 생성 (기본 정수 인덱스)
    s1 = pd.Series([10, 20, 30, 40])
    print("Series s1:\n", s1)
    # 출력:
    # Series s1:
    # 0    10
    # 1    20
    # 2    30
    # 3    40
    # dtype: int64

    # 딕셔너리로부터 Series 생성 (키가 인덱스가 됨)
    data = {'a': 100, 'b': 200, 'c': 300}
    s2 = pd.Series(data)
    print("\nSeries s2:\n", s2)
    # 출력:
    # Series s2:
    # a    100
    # b    200
    # c    300
    # dtype: int64
    ```

*   **구체적 예시**: 한 학급 학생들의 수학 점수 목록을 생각해보세요. 각 점수(값)는 특정 학생(인덱스)에게 해당하며, 모든 데이터는 "점수"라는 동일한 타입을 가집니다. 엑셀 스프레드시트에서 특정 한 열의 데이터와 유사합니다.

*   **시험 포인트**:
    *   ⭐Series는 **1차원** 데이터 구조이다.
    *   ⭐각 요소는 **레이블(인덱스)**을 가진다.
    *   ⭐Series 내의 모든 값은 **동일한 데이터 타입**이어야 한다.

### 2. DataFrame

*   **핵심 개념**: DataFrame은 **2차원 테이블 형식 데이터**입니다. 여러 개의 Series들이 동일한 **Index**를 공유하며 모여있는 형태이며, **행(rows)과 열(columns)의 구조**를 가집니다. Pandas에서 데이터를 다룰 때 가장 기본적이고 많이 사용되는 **주요 작업 데이터 구조**입니다.

*   **코드/수식 해설**:
    ```python
    import pandas as pd

    # 딕셔너리로부터 DataFrame 생성 (키가 컬럼 이름이 됨)
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Paris', 'London']
    }
    df = pd.DataFrame(data)
    print("DataFrame df:\n", df)
    # 출력:
    # DataFrame df:
    #       Name  Age      City
    # 0    Alice   25  New York
    # 1      Bob   30     Paris
    # 2  Charlie   35    London

    # 특정 컬럼 선택 (Series 반환)
    print("\nDataFrame df['Age']:\n", df['Age'])
    # 출력:
    # DataFrame df['Age']:
    # 0    25
    # 1    30
    # 2    35
    # Name: Age, dtype: int64
    ```

*   **구체적 예시**: 학생들의 정보를 담은 표를 생각해보세요. "이름", "학번", "점수", "전공" 등의 여러 열(Series)이 있고, 각 행은 한 명의 학생 정보(레코드)를 나타냅니다. 엑셀 스프레드시트 전체 또는 관계형 데이터베이스의 테이블과 유사합니다.

*   **시험 포인트**:
    *   ⭐DataFrame은 **2차원** 테이블 형태의 데이터이다.
    *   ⭐**동일한 Index**를 공유하는 **Series들의 컬렉션**이다.
    *   ⭐**행과 열 구조**를 가지며, Pandas의 **주요 작업 데이터 구조**이다.

### 3. Index

*   **핵심 개념**: Index는 Series나 DataFrame의 **행(row) 또는 열(column)을 식별하는 레이블들의 시퀀스**입니다. 정수, 문자열, 날짜/시간 등 **다양한 데이터 타입**을 가질 수 있습니다. 매우 중요한 특징은 이 레이블들이 **유일(unique)할 필요가 없다**는 것입니다. Index는 데이터를 효율적으로 **정렬(alignment)하고 선택(selection)하는 기능**을 제공합니다.

*   **코드/수식 해설**:
    ```python
    import pandas as pd

    s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
    print("Series index:", s.index)
    # 출력: Series index: Index(['a', 'b', 'c'], dtype='object')

    df = pd.DataFrame({'Data': [1, 2, 3]}, index=['row1', 'row2', 'row3'])
    print("DataFrame index:", df.index)
    # 출력: DataFrame index: Index(['row1', 'row2', 'row3'], dtype='object')

    # 인덱스가 유일하지 않은 예시
    s_non_unique = pd.Series([100, 200, 300], index=['x', 'y', 'x'])
    print("\nSeries with non-unique index:\n", s_non_unique)
    # 출력:
    # Series with non-unique index:
    # x    100
    # y    200
    # x    300
    # dtype: int64

    # 인덱스를 이용한 데이터 선택
    print("\nSelecting data by index 'x':\n", s_non_unique['x'])
    # 출력:
    # Selecting data by index 'x':
    # x    100
    # x    300
    # dtype: int64
    ```

*   **구체적 예시**: 책의 "목차"나 "색인"을 떠올려 보세요. 특정 주제(레이블)를 찾으면 해당 페이지(데이터)로 바로 이동할 수 있습니다. 주민등록번호나 학번처럼 유일한 식별자로 사용될 수도 있지만, 같은 학급의 여러 학생이 '홍길동'이라는 이름을 가질 수 있듯이, 인덱스 레이블은 중복될 수도 있습니다.

*   **시험 포인트**:
    *   ⭐Index는 행/열의 **레이블 시퀀스**이다.
    *   ⭐인덱스 값은 정수, 문자열 등 **다양한 타입**이 가능하다.
    *   ⭐가장 중요한 특징은 Index 레이블은 **유일(unique)할 필요가 없다**.
    *   ⭐데이터 **정렬(alignment)과 선택(selection)**에 핵심적인 역할을 한다.

---

## Slide 8

---
### **핵심 개념**

pandas `Series`는 1차원 배열(array-like) 형태의 데이터 구조로, 각 데이터 요소가 인덱스(label)를 가집니다. 슬라이드에서 강조하는 `Series`의 핵심 해부학적 구성 요소는 다음과 같습니다:

1.  **`values`**: `Series`가 실제로 저장하는 데이터 값들의 배열입니다. 이는 내부적으로 NumPy `ndarray` 형태로 저장됩니다.
2.  **`index`**: 각 `values`에 대응하는 레이블(label) 또는 이름입니다. 기본적으로 0부터 시작하는 정수 인덱스가 부여되지만, 사용자가 지정할 수 있습니다. `index` 자체도 `pandas.Index` 객체입니다.
3.  **`name`**: `Series` 전체에 부여된 이름입니다. 특히 여러 `Series`를 병합하거나 `DataFrame`으로 변환할 때 유용합니다.
4.  **`index.name`**: `Series`의 `index` 자체에 부여된 이름입니다. 이는 `DataFrame`으로 변환될 때 컬럼 이름으로 사용될 수 있어, 인덱스 축의 의미를 명확히 합니다.

### **코드/수식 해설**

```python
import pandas as pd
import numpy as np

# Series 생성 예시
s = pd.Series([4, 2, 4, 6],
              index=['cat', 'penguin', 'dog', 'butterfly'],
              name='legs')
# Series의 인덱스에 이름(name)을 부여
s.index.name = 'animal'

print(s)
# 출력:
# animal
# cat          4
# penguin      2
# dog          4
# butterfly    6
# Name: legs, dtype: int64

# Series 및 그 구성 요소의 타입과 값 확인
print(f"type(s): {type(s)}") # <class 'pandas.core.series.Series'>
print(f"s.index: {s.index}") # Index(['cat', 'penguin', 'dog', 'butterfly'], dtype='object', name='animal')
print(f"type(s.index): {type(s.index)}") # <class 'pandas.core.indexes.base.Index'>
print(f"s.index.name: {s.index.name}") # 'animal' (인덱스 축의 이름)
print(f"s.name: {s.name}") # 'legs' (Series 자체의 이름)
print(f"s.values: {s.values}") # [4 2 4 6] (데이터 값들을 담는 NumPy 배열)
print(f"type(s.values): {type(s.values)}") # <class 'numpy.ndarray'>

# Series의 값을 NumPy 배열로 얻는 권장 방식 (확장 dtypes를 고려)
print(f"s.to_numpy(): {s.to_numpy()}")
```

*   `pd.Series([...])`: `pandas` 라이브러리의 `Series` 객체를 생성합니다.
    *   첫 번째 인자 `[4, 2, 4, 6]`는 `Series`가 담을 데이터(`values`)입니다.
    *   `index=['cat', 'penguin', 'dog', 'butterfly']`는 각 데이터 값에 할당될 사용자 정의 인덱스(`index`)를 지정합니다.
    *   `name='legs'`는 생성될 `Series` 객체 자체에 `'legs'`라는 이름을 부여합니다.
*   `s.index.name = 'animal'`: `Series` 객체 `s`의 `index` 속성에 접근하여, 그 `index` 자체에 `'animal'`이라는 이름을 부여합니다. 이는 인덱스가 무엇을 의미하는지 명확히 해줍니다.
*   `type(s)`: `s`가 `pandas.Series` 타입임을 보여줍니다.
*   `s.index`: `s`의 인덱스 객체를 반환합니다. 이 객체는 `pd.Index` 타입이며, `name` 속성을 가질 수 있습니다.
*   `s.index.name`: 인덱스 객체에 부여된 이름을 반환합니다.
*   `s.name`: `Series` 객체 자체에 부여된 이름을 반환합니다.
*   `s.values`: `Series`가 담고 있는 실제 데이터 값들을 NumPy `ndarray` 형태로 반환합니다.
*   `s.to_numpy()`: `s.values`와 유사하게 NumPy 배열을 반환하지만, pandas 1.0부터 도입된 확장 데이터 타입(Extension Dtypes)과의 호환성을 위해 `s.values`보다 더 권장되는 방법입니다.

### **구체적 예시**

어떤 사람이 동물원 관리자이고, 각 동물들이 가진 다리(legs)의 수를 기록하고 싶다고 상상해 봅시다.

*   **데이터 (`values`)**: `[4, 2, 4, 6]` (고양이 4개, 펭귄 2개, 개 4개, 나비 6개)
*   **인덱스 (`index`)**: `['cat', 'penguin', 'dog', 'butterfly']` (각 다리 수에 해당하는 동물 이름)
*   **Series의 이름 (`s.name`)**: `'legs'` (이 데이터 묶음이 "다리 수"를 나타낸다는 의미)
*   **인덱스의 이름 (`s.index.name`)**: `'animal'` (인덱스가 "동물"을 나타낸다는 의미)

이 `Series`는 "다리 수"(`name='legs'`)라는 주제로 "동물"(`index.name='animal'`)을 인덱스로 삼아 각 동물의 다리 수를 저장한 작은 표와 같습니다.

### **시험 포인트**

*   **`pandas.Series`의 세 가지 핵심 구성 요소는 무엇인가?** ⭐
    *   `values` (실제 데이터), `index` (데이터의 레이블), `name` (Series 자체의 이름)
*   **`s.name`과 `s.index.name`의 차이점을 설명하고, 각각이 어떤 역할을 하는가?** ⭐
    *   `s.name`: `Series` 전체의 이름 (예: `legs`)
    *   `s.index.name`: `Series`의 `index` 축의 이름 (예: `animal`)
    *   `DataFrame`으로 변환될 때 `s.name`은 컬럼 이름이 될 수 있고, `s.index.name`은 `DataFrame`의 인덱스 이름이 됩니다.
*   **`s.values`와 `s.to_numpy()`의 역할 및 `s.to_numpy()`가 권장되는 이유?** ⭐
    *   둘 다 `Series`의 데이터 값을 NumPy `ndarray`로 반환합니다.
    *   `s.to_numpy()`는 확장 데이터 타입(Extension Dtypes)과의 일관성 및 잠재적인 미래 호환성을 위해 `s.values`보다 권장됩니다.
*   `pd.Series()` 생성 시 `index`와 `name` 파라미터를 사용하여 사용자 정의 `Series`를 생성하는 방법을 알아야 합니다.

---

## Slide 9

본 강의 자료는 `pandas.Series` 객체의 핵심 연산들을 다룹니다. 데이터 분석에서 단일 컬럼 데이터를 효율적으로 다루기 위한 다양한 기능들을 학습합니다.

---

### **핵심 개념**: Series Index
`pandas.Series`는 1차원 배열 형태의 데이터 구조로, 각 데이터 항목은 인덱스(Index)와 연결됩니다. 이 인덱스는 데이터에 접근하고 데이터를 정렬하는 데 사용됩니다. 기본적으로 0부터 시작하는 정수형 위치 인덱스를 가집니다.

-   **코드/수식 해설**:
    ```python
    import pandas as pd
    s = pd.Series([10, 20, 30, 40])
    print(s)
    # Output:
    # 0    10
    # 1    20
    # 2    30
    # 3    40
    # dtype: int64
    print(s.index)
    # Output: RangeIndex(start=0, stop=4, step=1)
    ```
-   **구체적 예시**: 백화점 영수증의 상품 목록에서 각 상품이 '첫 번째 상품', '두 번째 상품' 등으로 번호가 매겨지는 것과 유사합니다.
-   **시험 포인트**: ⭐ Series 인덱스의 기본적인 역할은 데이터에 대한 접근 및 식별자이며, 데이터와 항상 함께 존재합니다.

### **핵심 개념**: Series with Custom Index
사용자는 Series 생성 시 기본 정수 인덱스 대신 원하는 레이블(문자열, 숫자 등)로 구성된 사용자 정의 인덱스를 지정할 수 있습니다. 이를 통해 데이터의 의미를 명확히 하고, 레이블을 이용한 직관적인 데이터 접근이 가능해집니다.

-   **코드/수식 해설**:
    ```python
    s_custom = pd.Series([100, 200, 300], index=['apple', 'banana', 'cherry'])
    print(s_custom)
    # Output:
    # apple     100
    # banana    200
    # cherry    300
    # dtype: int64
    ```
-   **구체적 예시**: 각 나라의 인구수를 저장할 때, '0번 인구', '1번 인구' 대신 '한국', '미국', '중국'과 같은 나라 이름을 인덱스로 사용하는 것과 같습니다.
-   **시험 포인트**: 사용자 정의 인덱스를 통해 데이터의 가독성을 높이고, 추후 데이터 정렬 및 병합 시 중요한 기준이 됩니다.

### **핵심 개념**: Series: Label vs. Position Indexing
Pandas Series는 데이터에 접근하는 두 가지 주요 방법을 제공합니다: 레이블 기반 인덱싱 (`.loc`)과 위치 기반 인덱싱 (`.iloc`).
-   `.loc`: 인덱스 레이블을 사용하여 데이터를 선택합니다. 슬라이싱 시 끝점을 포함합니다.
-   `.iloc`: 정수 위치(0부터 시작)를 사용하여 데이터를 선택합니다. 슬라이싱 시 끝점을 포함하지 않습니다 (Python 표준 슬라이싱과 동일).

-   **코드/수식 해설**:
    ```python
    s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
    print(s.loc['b'])        # 레이블 'b'의 값
    # Output: 20
    print(s.iloc[1])       # 1번 위치의 값
    # Output: 20
    print(s.loc['a':'c'])    # 레이블 'a'부터 'c'까지 (c 포함)
    # Output:
    # a    10
    # b    20
    # c    30
    # dtype: int64
    print(s.iloc[0:3])     # 0번 위치부터 2번 위치까지 (3번 위치 미포함)
    # Output:
    # a    10
    # b    20
    # c    30
    # dtype: int64
    ```
-   **구체적 예시**: 도서관에서 책을 찾을 때, 책 제목('레이블')으로 찾는 것이 `.loc`, 서가 번호('위치')로 찾는 것이 `.iloc`에 해당합니다.
-   **시험 포인트**: ⭐ `.loc`와 `.iloc`의 정확한 사용법과 차이점을 이해하는 것이 매우 중요하며, 특히 슬라이싱 시 끝점 포함 여부를 명확히 알아야 합니다.

### **핵심 개념**: Boolean Filtering Idioms (isin, between)
불리언 마스킹(Boolean Masking)은 특정 조건을 만족하는 데이터를 필터링하는 강력한 방법입니다. `isin()` 메서드는 Series의 각 요소가 주어진 값 목록에 포함되는지 여부를, `between()` 메서드는 특정 범위 내에 있는지 여부를 확인하여 불리언 Series를 반환합니다. 이 불리언 Series를 사용하여 원본 Series에서 조건에 맞는 데이터를 선택할 수 있습니다.

-   **코드/수식 해설**:
    ```python
    s = pd.Series([10, 20, 30, 40, 50])
    # isin() 사용 예시
    print(s[s.isin([20, 40])])
    # Output:
    # 1    20
    # 3    40
    # dtype: int64

    # between() 사용 예시
    print(s[s.between(25, 45)])
    # Output:
    # 2    30
    # 3    40
    # dtype: int64
    ```
-   **구체적 예시**: 학생들 점수 목록에서 'A 학점' 또는 'B 학점'을 받은 학생(isin)을 찾거나, '80점 이상 90점 미만'인 학생(between)을 찾는 것과 같습니다.
-   **시험 포인트**: 불리언 인덱싱의 기본 원리를 이해하고, `isin()` 및 `between()`과 같은 편리한 메서드를 활용하여 복잡한 필터링 조건을 효율적으로 구현하는 방법을 알아야 합니다.

### **핵심 개념**: Take by Labels or Positions
데이터를 레이블(`.loc`)이나 위치(`.iloc`)를 통해 선택하는 것은 매우 기본적인 작업입니다. `.take()` 메서드는 정수 위치 배열을 받아 해당 위치의 요소를 반환하며, 이는 주로 특정 위치의 여러 요소를 효율적으로 선택할 때 사용될 수 있습니다. (Pandas Series에서는 `.iloc`를 통해 위치 기반 선택이 더 일반적으로 사용됩니다.)

-   **코드/수식 해설**:
    ```python
    s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
    # 위치 1, 3의 값 선택 (iloc 활용이 더 일반적)
    print(s.iloc[[1, 3]])
    # Output:
    # b    20
    # d    40
    # dtype: int64

    # 레이블 'a', 'c'의 값 선택
    print(s.loc[['a', 'c']])
    # Output:
    # a    10
    # c    30
    # dtype: int64
    ```
-   **구체적 예시**: 상품 진열대에서 '세 번째'와 '다섯 번째' 상품을 고르거나, '우유'와 '계란'이라는 이름을 가진 상품을 선택하는 것과 유사합니다.
-   **시험 포인트**: 특정 레이블 또는 위치 목록을 사용하여 여러 항목을 선택하는 다양한 방법을 이해해야 합니다.

### **핵심 개념**: Index Edits: Assign, Sort, Reset, Delete
Series의 인덱스를 수정하거나 재구성하는 다양한 방법이 있습니다.
-   **Assign**: 새로운 인덱스를 할당하여 변경합니다.
-   **Sort**: `sort_index()` 메서드를 사용하여 인덱스를 기준으로 Series를 정렬합니다.
-   **Reset**: `reset_index()` 메서드는 현재 인덱스를 데이터 컬럼으로 변환하고, 새로운 기본 정수 인덱스를 생성합니다.
-   **Delete**: 인덱스 레이블에 해당하는 데이터를 삭제하는 것은 주로 Series에서 불리언 마스킹을 이용해 특정 값을 제외하거나, `.drop()` 메서드를 사용하여 이루어집니다.

-   **코드/수식 해설**:
    ```python
    s = pd.Series([10, 20, 30], index=['c', 'a', 'b'])
    print("Original Series:\n", s)

    # Assign (인덱스 변경)
    s.index = ['x', 'y', 'z']
    print("After assign index:\n", s)

    # Sort (인덱스 정렬)
    s_sorted = s.sort_index()
    print("After sort_index:\n", s_sorted)

    # Reset (인덱스를 컬럼으로)
    s_reset = s_sorted.reset_index()
    print("After reset_index:\n", s_reset)

    # Delete (레이블 'y'의 데이터 삭제 - drop 활용)
    s_deleted = s_sorted.drop('y')
    print("After drop 'y':\n", s_deleted)
    ```
-   **구체적 예시**: 전화번호부에서 사람 이름 순서를 바꾸거나(정렬), 기존의 이름 목록을 없애고 새로운 순서로 번호를 매기는(리셋) 것과 같습니다.
-   **시험 포인트**: 인덱스 변경이 원본 Series에 직접 적용되는지 (`inplace` 옵션) 또는 새로운 Series를 반환하는지 여부를 ⭐ 주의깊게 확인해야 합니다. `reset_index()`는 `DataFrame`을 반환할 수 있다는 점도 기억해야 합니다.

### **핵심 개념**: Find Element by Value (Vector vs. Indexed Lookup)
Series에서 특정 값을 가진 요소를 찾는 것은 두 가지 방식으로 가능합니다.
-   **값 기반(Vectorized lookup)**: 불리언 마스킹을 사용하여 Series 전체에서 조건에 맞는 값을 찾습니다. 이는 Series의 모든 요소를 순회하므로, 대규모 데이터에서 특정 값을 찾을 때 인덱스가 없는 경우 유용합니다.
-   **인덱스 기반(Indexed lookup)**: 만약 인덱스가 유니크하고 찾는 값이 인덱스에 있다면, `.loc`를 통해 훨씬 빠르게 접근할 수 있습니다.

-   **코드/수식 해설**:
    ```python
    s = pd.Series([10, 20, 30, 20, 40], index=['a', 'b', 'c', 'd', 'e'])

    # 값 기반 (Vectorized lookup)
    print("Elements with value 20:\n", s[s == 20])
    # Output:
    # b    20
    # d    20
    # dtype: int64

    # 인덱스 기반 (Indexed lookup, 값이 인덱스에 있을 때)
    print("Element at index 'c':", s.loc['c'])
    # Output: Element at index 'c': 30
    ```
-   **구체적 예시**: 학생들 점수 목록에서 '100점'을 받은 학생이 누구인지 찾는 것(값 기반)과, '철수'의 점수가 몇 점인지 찾는 것(인덱스 기반)에 비유할 수 있습니다.
-   **시험 포인트**: 대규모 데이터에서 특정 값을 찾을 때, 인덱스가 잘 구성되어 있다면 인덱스 기반 조회가 값 기반 조회보다 ⭐ 훨씬 빠르고 효율적이라는 것을 이해해야 합니다.

### **핵심 개념**: Missing Values: dtypes and isna()
결측치(Missing Values)는 데이터셋에서 값이 없는 부분을 의미하며, Pandas에서는 주로 `NaN` (Not a Number)으로 표현됩니다. 결측치는 데이터 타입에 영향을 미칠 수 있습니다. 예를 들어, 정수형(int) Series에 `NaN`이 들어가면 자동으로 실수형(float)으로 변환됩니다. `isna()` 또는 `isnull()` 메서드는 Series의 각 요소가 결측치인지 여부를 나타내는 불리언 Series를 반환합니다.

-   **코드/수식 해설**:
    ```python
    import numpy as np
    s_int = pd.Series([1, 2, 3])
    print("Original int Series dtype:", s_int.dtype)
    # Output: Original int Series dtype: int64

    s_with_nan = pd.Series([1, np.nan, 3])
    print("Series with NaN:\n", s_with_nan)
    # Output:
    # 0    1.0
    # 1    NaN
    # 2    3.0
    # dtype: float64
    print("dtype after adding NaN:", s_with_nan.dtype)
    # Output: dtype after adding NaN: float64

    print("Is NaN?:\n", s_with_nan.isna())
    # Output:
    # 0    False
    # 1     True
    # 2    False
    # dtype: bool
    ```
-   **구체적 예시**: 설문조사에서 응답자가 특정 질문에 응답하지 않아 비어있는 칸이 생기는 경우를 생각할 수 있습니다.
-   **시험 포인트**: ⭐ `NaN`이 Series에 포함될 경우, 정수형 데이터라도 자동으로 실수형(`float64`)으로 변환된다는 사실을 반드시 기억해야 합니다. `isna()`와 `notna()`를 이용한 결측치 식별 방법도 중요합니다.

### **핵심 개념**: Missing Values II: Fill or Interpolate
결측치를 처리하는 일반적인 방법은 다음 두 가지입니다.
-   **Fill (채우기)**: `fillna()` 메서드를 사용하여 결측치를 특정 값(예: 0, 평균, 중앙값 등)으로 채웁니다.
-   **Interpolate (보간)**: `interpolate()` 메서드를 사용하여 인접한 유효한 값들을 기반으로 결측치를 추정하여 채웁니다 (예: 선형 보간). 이는 시계열 데이터에서 특히 유용합니다.

-   **코드/수식 해설**:
    ```python
    s_nan = pd.Series([1, np.nan, 3, np.nan, 5])

    # 0으로 채우기
    s_filled_zero = s_nan.fillna(0)
    print("Filled with 0:\n", s_filled_zero)
    # Output:
    # 0    1.0
    # 1    0.0
    # 2    3.0
    # 3    0.0
    # 4    5.0
    # dtype: float64

    # 선형 보간
    s_interpolated = s_nan.interpolate()
    print("Interpolated:\n", s_interpolated)
    # Output:
    # 0    1.0
    # 1    2.0
    # 2    3.0
    # 3    4.0
    # 4    5.0
    # dtype: float64
    ```
-   **구체적 예시**: 온도 측정 기록 중 센서 오류로 누락된 값이 있을 때, 이전 값과 다음 값의 평균으로 채우거나(보간), 그냥 0으로 처리하는(채우기) 것과 같습니다.
-   **시험 포인트**: `fillna()`와 `interpolate()`의 사용법과 각각의 방법이 어떤 상황에서 더 적합한지 (예: 단순 값 대체 vs. 추세 고려) 이해하는 것이 중요합니다.

### **핵심 개념**: Missing Values III: Reductions with NaN
Series에서 `sum()`, `mean()`, `max()` 등과 같은 통계 연산(Reduction methods)을 수행할 때 결측치(`NaN`)는 기본적으로 무시됩니다. 즉, 결측치를 제외한 유효한 값들만으로 연산을 수행합니다. 이 동작은 `skipna` 파라미터를 통해 제어할 수 있습니다.

-   **코드/수식 해설**:
    ```python
    s_nan = pd.Series([1, np.nan, 3, 5])

    # 기본적으로 NaN 무시
    print("Sum (skipna=True by default):", s_nan.sum())
    # Output: Sum (skipna=True by default): 9.0
    print("Mean (skipna=True by default):", s_nan.mean())
    # Output: Mean (skipna=True by default): 3.0

    # NaN을 포함하여 연산 (결과도 NaN)
    print("Sum (skipna=False):", s_nan.sum(skipna=False))
    # Output: Sum (skipna=False): nan
    ```
-   **구체적 예시**: 반 학생들의 시험 점수 평균을 낼 때, 결석한 학생의 점수(NaN)는 제외하고 나머지 학생들의 점수로 평균을 계산하는 것과 같습니다.
-   **시험 포인트**: ⭐ Series의 통계 연산 시 `NaN`이 기본적으로 `skipna=True`로 처리되어 무시된다는 점을 명확히 알아야 합니다. `skipna=False`로 설정했을 때의 결과도 이해해야 합니다.

### **핵심 개념**: Missing Values IV: Alignment in Arithmetic
두 Series 간에 산술 연산(덧셈, 뺄셈 등)을 수행할 때, Pandas는 기본적으로 인덱스를 기준으로 데이터를 정렬(Align)한 후 연산을 수행합니다. 만약 두 Series에 동일한 인덱스 레이블이 없는 경우, 해당 위치의 결과는 `NaN`으로 채워집니다.

-   **코드/수식 해설**:
    ```python
    s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
    s2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])

    # 인덱스 'b', 'c'는 정렬되어 연산되고, 'a', 'd'는 NaN이 됨
    print(s1 + s2)
    # Output:
    # a    NaN
    # b    6.0
    # c    8.0
    # d    NaN
    # dtype: float64
    ```
-   **구체적 예시**: 두 학생의 과목별 점수를 더할 때, 한 학생이 수강하지 않은 과목(다른 인덱스)은 점수를 더할 수 없어 결과적으로 '알 수 없음'(NaN)이 되는 것과 같습니다.
-   **시험 포인트**: ⭐ Pandas의 Series/DataFrame 연산은 항상 인덱스 정렬(Alignment)을 먼저 시도하며, 일치하지 않는 인덱스에 대해서는 `NaN`이 발생한다는 점을 이해해야 합니다. 이는 데이터 병합 및 연산 시 매우 중요한 개념입니다.

### **핵심 개념**: Sort, Rank, Top-k, Quantiles
데이터를 분석하는 데 유용한 여러 통계 및 정렬 기능들입니다.
-   **Sort**: `sort_values()` 메서드로 Series의 값을 기준으로 데이터를 정렬합니다.
-   **Rank**: `rank()` 메서드로 Series 내 값들의 순위를 부여합니다. 동일한 값에 대한 순위 처리 방식(`method`)을 지정할 수 있습니다.
-   **Top-k**: `nlargest(k)` 및 `nsmallest(k)` 메서드를 사용하여 Series에서 가장 크거나 작은 k개의 값을 효율적으로 찾습니다.
-   **Quantiles (분위수)**: `quantile(q)` 메서드로 Series의 분위수를 계산합니다. (예: 중앙값은 0.5 분위수).

-   **코드/수식 해설**:
    ```python
    s = pd.Series([30, 10, 50, 20, 40])

    # 값 정렬
    print("Sorted values:\n", s.sort_values())
    # Output:
    # 1    10
    # 3    20
    # 0    30
    # 4    40
    # 2    50
    # dtype: int64

    # 순위 부여
    print("Rank:\n", s.rank())
    # Output:
    # 0    3.0
    # 1    1.0
    # 2    5.0
    # 3    2.0
    # 4    4.0
    # dtype: float64

    # 상위 2개 값
    print("Top 2 values:\n", s.nlargest(2))
    # Output:
    # 2    50
    # 4    40
    # dtype: int64

    # 0.5 분위수 (중앙값)
    print("0.5 Quantile:", s.quantile(0.5))
    # Output: 30.0
    ```
-   **구체적 예시**: 학교에서 학생들의 성적을 높은 순으로 정렬하거나(Sort), 석차를 매기고(Rank), 상위 5명을 선발하거나(Top-k), 중간 등수가 몇 점인지(Quantile) 확인하는 것과 같습니다.
-   **시험 포인트**: 각 메서드의 반환 값(정렬된 Series, 순위 Series, 부분 Series, 스칼라 값)과 주요 `method` 인자 (특히 `rank`에서)를 이해하는 것이 중요합니다.

### **핵심 개념**: Cumulative, Difference, Lag, Return
시계열 데이터 분석에 유용한 연산들입니다.
-   **Cumulative (누적)**: `cumsum()`, `cumprod()` 등으로 누적 합계, 누적 곱을 계산합니다.
-   **Difference (차분)**: `diff(periods=n)` 메서드로 현재 값과 n 기간 전의 값의 차이를 계산합니다.
-   **Lag (지연)**: `shift(periods=n)` 메서드로 Series의 값을 n 기간만큼 이동시킵니다. 과거 값이나 미래 값을 참조할 때 사용됩니다.
-   **Return (수익률)**: `pct_change()` 메서드로 현재 값과 이전 값 사이의 백분율 변화(수익률)를 계산합니다.

-   **코드/수식 해설**:
    ```python
    s = pd.Series([10, 12, 11, 15, 14])

    # 누적 합
    print("Cumulative sum:\n", s.cumsum())
    # Output:
    # 0    10
    # 1    22
    # 2    33
    # 3    48
    # 4    62
    # dtype: int64

    # 차분 (현재 값 - 이전 값)
    print("Difference:\n", s.diff())
    # Output:
    # 0     NaN
    # 1     2.0
    # 2    -1.0
    # 3     4.0
    # 4    -1.0
    # dtype: float64

    # Lag (1칸 이동, 이전 값)
    print("Shifted (lag 1):\n", s.shift(1))
    # Output:
    # 0     NaN
    # 1    10.0
    # 2    12.0
    # 3    11.0
    # 4    15.0
    # dtype: float64

    # 수익률 ((현재 - 이전) / 이전)
    print("Percentage change:\n", s.pct_change())
    # Output:
    # 0         NaN
    # 1    0.200000
    # 2   -0.083333
    # 3    0.363636
    # 4   -0.066667
    # dtype: float64
    ```
-   **구체적 예시**: 일별 판매량의 총 누적 판매량을 계산하거나(Cumulative), 어제 대비 주가 변동폭을 확인하거나(Difference), 어제 주가와 오늘 주가를 비교하거나(Lag), 주식의 일별 수익률을 계산하는(Return) 데 사용됩니다.
-   **시험 포인트**: 시계열 데이터 분석에서 각 연산이 어떤 의미를 가지며, 언제 활용되는지 이해해야 합니다. 특히 `shift()`와 `diff()`는 첫 번째 값에 `NaN`이 생긴다는 점을 기억해야 합니다.

### **핵심 개념**: Where/Mask, Clip, Replace
Series의 값을 조건에 따라 변경하거나 제한하는 메서드들입니다.
-   **Where/Mask**: `where(condition, other)`는 조건이 `True`인 곳의 값을 유지하고 `False`인 곳의 값을 `other`로 대체합니다. `mask(condition, other)`는 `where`와 반대로 조건이 `True`인 곳의 값을 `other`로 대체하고 `False`인 곳의 값을 유지합니다.
-   **Clip**: `clip(lower=min, upper=max)`는 Series의 모든 값을 주어진 최소값(lower)과 최대값(upper) 범위 내로 제한합니다.
-   **Replace**: `replace(to_replace, value)`는 Series 내 특정 값(또는 값들)을 다른 값으로 대체합니다.

-   **코드/수식 해설**:
    ```python
    s = pd.Series([-5, 10, 20, -15, 30])

    # where: 양수만 남기고 나머지는 0으로 (조건이 False인 값 변경)
    print("Where (positive values only):\n", s.where(s > 0, 0))
    # Output:
    # 0     0
    # 1    10
    # 2    20
    # 3     0
    # 4    30
    # dtype: int64

    # clip: 값을 0에서 25 사이로 제한
    print("Clipped (0 to 25):\n", s.clip(0, 25))
    # Output:
    # 0     0
    # 1    10
    # 2    20
    # 3     0
    # 4    25
    # dtype: int64

    # replace: -5를 5로, 30을 35로 변경
    print("Replaced:\n", s.replace({-5: 5, 30: 35}))
    # Output:
    # 0     5
    # 1    10
    # 2    20
    # 3   -15
    # 4    35
    # dtype: int64
    ```
-   **구체적 예시**: 고객 점수가 음수가 나왔을 때 0점으로 처리하거나(clip, where), 너무 높은 점수를 상한선으로 제한하고(clip), 특정 코드 값(예: '미응답')을 표준 값(예: 'NaN')으로 변경하는(replace) 데 활용됩니다.
-   **시험 포인트**: `where`와 `mask`의 동작 방식 차이, `clip`을 이용한 데이터 범위 제한, `replace`로 여러 값을 한 번에 변경하는 딕셔너리 사용법을 숙지해야 합니다.

### **핵심 개념**: Map, Astype, To-NumPy
Series의 데이터 형태나 타입을 변환하는 기능들입니다.
-   **Map**: `map()` 메서드는 Series의 각 요소에 함수(또는 딕셔너리, Series)를 적용하여 새로운 Series를 반환합니다. 데이터 변환이나 매핑에 강력합니다.
-   **Astype**: `astype(dtype)` 메서드는 Series의 데이터 타입을 변경합니다 (예: `int`에서 `float`으로, `float`에서 `int`로). 변환이 불가능한 경우 오류가 발생할 수 있습니다.
-   **To-NumPy**: `to_numpy()` 메서드는 Series를 NumPy 배열로 변환합니다. Pandas의 기능을 넘어 NumPy 배열의 기능을 사용해야 할 때 유용합니다.

-   **코드/수식 해설**:
    ```python
    s = pd.Series([1, 2, 3, 4])

    # map: 각 값에 10을 곱하기
    print("Mapped (multiply by 10):\n", s.map(lambda x: x * 10))
    # Output:
    # 0    10
    # 1    20
    # 2    30
    # 3    40
    # dtype: int64

    # astype: float64로 변환
    print("As float:\n", s.astype(float))
    # Output:
    # 0    1.0
    # 1    2.0
    # 2    3.0
    # 3    4.0
    # dtype: float64

    # to_numpy: NumPy 배열로 변환
    arr = s.to_numpy()
    print("To NumPy array:", arr)
    # Output: To NumPy array: [1 2 3 4]
    print("NumPy array dtype:", type(arr))
    # Output: NumPy array dtype: <class 'numpy.ndarray'>
    ```
-   **구체적 예시**: 시험 점수를 등급(A, B, C)으로 변환하거나(map), 숫자로 된 코드를 문자열 코드로 변경하거나(astype), 머신러닝 모델에 입력하기 위해 Pandas Series를 순수한 NumPy 배열로 변환하는(to_numpy) 경우에 사용됩니다.
-   **시험 포인트**: `map`의 유연성 (함수, 딕셔너리, Series 모두 적용 가능), `astype` 사용 시 데이터 손실 또는 오류 발생 가능성, `to_numpy`를 통한 NumPy와의 연동을 이해해야 합니다.

### **핵심 개념**: Accessors: .str, .dt, .cat
Pandas는 Series의 `dtype`에 따라 특정 데이터 타입에 특화된 편리한 접근자(Accessor)를 제공합니다.
-   `.str`: Series가 문자열(`object` 또는 `string` dtype)을 포함할 때, 문자열 관련 메서드(예: `upper()`, `contains()`, `split()`)를 사용할 수 있습니다.
-   `.dt`: Series가 날짜/시간(`datetime`)을 포함할 때, 날짜/시간 관련 속성(예: `year`, `month`, `day`)과 메서드(예: `day_name()`)를 사용할 수 있습니다.
-   `.cat`: Series가 범주형(`category` dtype)일 때, 범주형 데이터 관련 속성(예: `codes`, `categories`)과 메서드(예: `as_ordered()`)를 사용할 수 있습니다.

-   **코드/수식 해설**:
    ```python
    # .str accessor
    s_str = pd.Series(['apple', 'banana', 'cherry'])
    print("String upper:\n", s_str.str.upper())
    # Output:
    # 0     APPLE
    # 1    BANANA
    # 2    CHERRY
    # dtype: object

    # .dt accessor
    s_dt = pd.Series(pd.to_datetime(['2023-01-01', '2023-05-15', '2024-11-30']))
    print("Year from datetime:\n", s_dt.dt.year)
    # Output:
    # 0    2023
    # 1    2023
    # 2    2024
    # dtype: int32

    # .cat accessor
    s_cat = pd.Series(['low', 'medium', 'low', 'high'], dtype='category')
    print("Category codes:\n", s_cat.cat.codes)
    # Output:
    # 0    1
    # 1    2
    # 2    1
    # 3    0
    # dtype: int8
    ```
-   **구체적 예시**: 고객 이름 리스트에서 모두 대문자로 변경하거나(str), 주문 날짜에서 '년도'만 추출하거나(dt), 설문조사 응답('매우 좋음', '좋음', '보통')을 수치 코드(0, 1, 2)로 변환하는(cat) 데 사용됩니다.
-   **시험 포인트**: 각 접근자가 어떤 `dtype`에 사용되는지, 그리고 각 접근자를 통해 어떤 종류의 연산을 수행할 수 있는지 ⭐ 정확히 이해해야 합니다.

### **핵심 개념**: Windows: Rolling, Expanding, EWM
시계열 데이터에서 특정 구간(윈도우)에 대한 통계량을 계산하는 기능입니다.
-   **Rolling (이동 윈도우)**: `rolling(window_size)`는 지정된 크기의 윈도우를 이동시키면서 통계량(예: `mean()`, `sum()`)을 계산합니다. 각 시점의 통계량은 해당 시점을 포함한 이전 `window_size - 1`개의 데이터로 계산됩니다.
-   **Expanding (확장 윈도우)**: `expanding()`은 윈도우 크기가 데이터가 늘어남에 따라 계속 확장되면서 통계량을 계산합니다. 각 시점의 통계량은 첫 번째 데이터부터 해당 시점까지의 모든 데이터를 포함합니다.
-   **EWM (지수 가중 이동 윈도우)**: `ewm(span=n)`은 최근 데이터에 더 큰 가중치를 부여하여 통계량(예: `mean()`)을 계산합니다. `span`은 가중치를 결정하는 데 사용되는 기간입니다.

-   **코드/수식 해설**:
    ```python
    s = pd.Series([10, 12, 11, 15, 14, 16])

    # 3일 이동 평균 (Rolling mean)
    print("Rolling mean (window=3):\n", s.rolling(window=3).mean())
    # Output:
    # 0     NaN
    # 1     NaN
    # 2    11.0  # (10+12+11)/3
    # 3    12.666667 # (12+11+15)/3
    # 4    13.333333 # (11+15+14)/3
    # 5    15.0      # (15+14+16)/3
    # dtype: float64

    # 누적 합 (Expanding sum)
    print("Expanding sum:\n", s.expanding().sum())
    # Output:
    # 0     10.0
    # 1     22.0
    # 2     33.0
    # 3     48.0
    # 4     62.0
    # 5     78.0
    # dtype: float64

    # 지수 가중 이동 평균 (EWM mean, span=3)
    print("EWM mean (span=3):\n", s.ewm(span=3).mean())
    # Output:
    # 0    10.000000
    # 1    11.333333
    # 2    11.142857
    # 3    13.238095
    # 4    13.619048
    # 5    15.238095
    # dtype: float64
    ```
-   **구체적 예시**: 주식 시장에서 5일 이동 평균선을 계산하거나(Rolling), 특정 상품의 출시 이후 총 판매량을 누적하여 계산하거나(Expanding), 최근 판매량에 더 비중을 두어 평균 판매량을 추정하는(EWM) 경우에 사용됩니다.
-   **시험 포인트**: ⭐ 각 윈도우 함수의 정의와 시계열 데이터 분석에서의 활용 차이점을 명확히 이해해야 합니다. 특히 `rolling()`은 처음 `window_size - 1`개 결과가 `NaN`이라는 점을 기억해야 합니다.

### **핵심 개념**: Fast Scalars; Value Counts; Sampling
데이터를 빠르고 효율적으로 요약하고 탐색하는 기능들입니다.
-   **Fast Scalars (빠른 스칼라 연산)**: Series의 `sum()`, `mean()`, `min()`, `max()` 등은 C/C++로 구현되어 있어 매우 빠르게 스칼라 값을 계산합니다.
-   **Value Counts (값 빈도 계산)**: `value_counts()` 메서드는 Series 내의 고유한 값들의 빈도수를 계산하여 Series 형태로 반환합니다. 데이터 분포를 파악하는 데 매우 유용합니다.
-   **Sampling (샘플링)**: `sample(n=..., frac=..., random_state=...)` 메서드는 Series에서 임의로 데이터를 추출(샘플링)합니다. `n`은 추출할 개수, `frac`은 비율, `random_state`는 재현 가능한 결과를 위해 난수 시드를 설정합니다.

-   **코드/수식 해설**:
    ```python
    s = pd.Series(['A', 'B', 'A', 'C', 'B', 'A'])

    # Fast Scalars (예: 합계)
    s_num = pd.Series([10, 20, 30])
    print("Sum of numbers:", s_num.sum())
    # Output: Sum of numbers: 60

    # Value Counts (고유 값 빈도)
    print("Value counts:\n", s.value_counts())
    # Output:
    # A    3
    # B    2
    # C    1
    # dtype: int64

    # Sampling (2개 랜덤 추출)
    print("Sample 2:\n", s.sample(n=2, random_state=42)) # random_state로 재현성 확보
    # Output:
    # 1    B
    # 2    A
    # dtype: object
    ```
-   **구체적 예시**: 고객 설문조사에서 가장 많은 응답을 받은 항목이 무엇인지 확인하거나(Value Counts), 대규모 데이터셋 중 일부를 무작위로 선택하여 시범 분석을 진행하는(Sampling) 데 활용됩니다.
-   **시험 포인트**: `value_counts()`는 데이터 탐색의 핵심 도구이며, `sample()` 사용 시 `random_state`의 중요성을 이해하여 결과의 재현성을 확보하는 방법을 알아야 합니다.

---

## Slide 10

**핵심 개념**

*   **Pandas Series의 구조**: `pd.Series` 객체는 크게 두 부분으로 구성됩니다: 데이터를 식별하는 `Index`와 실제 데이터 값인 `Values`.
    *   `s.index`: Series의 인덱스를 나타내며, `pd.Index` 타입의 객체입니다.
    *   `s.values`: Series의 값을 나타내며, `numpy.ndarray` 타입의 객체입니다.
    *   `s.index.name`: 인덱스 자체에 이름을 부여할 수 있습니다.
    *   `s.name`: Series의 값에 이름을 부여할 수 있습니다 (DataFrame의 컬럼 이름과 유사).
*   **인덱스의 불변성(Immutability)**: Pandas의 Index 객체는 생성된 후에는 개별 요소를 직접 수정할 수 없습니다. 인덱스를 변경하려면 전체 인덱스를 새로운 `pd.Index` 객체로 교체해야 합니다.
*   **인덱스의 유일성(Uniqueness)**: Series의 인덱스는 중복될 수 있습니다. `s.index.is_unique` 속성으로 인덱스의 유일성을 확인할 수 있습니다. 인덱스가 중복될 경우, 해당 레이블로 데이터를 선택(`s.loc['label']`)하면 여러 개의 값을 가진 `Series`가 반환됩니다.
*   **데이터 타입(Types)**: Series의 값(`s.values`)은 `s.dtype` 속성으로 데이터 타입을 확인하며, 인덱스 레이블(`s.index`)은 `s.index.dtype` 속성으로 데이터 타입을 확인합니다. 이 두 `dtype`이 일치하지 않거나 예상과 다를 경우 데이터 선택이나 연산에서 버그가 발생할 수 있습니다.

**코드/수식 해설**

*   **Series 생성 및 기본 속성 접근**
    ```python
    import pandas as pd
    import numpy as np

    # 예시 Series 생성
    s = pd.Series([4, 2, 4, 6], index=['cat', 'penguin', 'dog', 'butterfly'])
    s.index.name = 'animal' # 인덱스에 이름 부여
    s.name = 'legs'         # Series 값에 이름 부여

    print("Series s:\n", s)
    print("\ns.index (타입: {}):".format(type(s.index)), s.index)
    print("s.values (타입: {}):".format(type(s.values)), s.values)
    print("s.index.name:", s.index.name)
    print("s.name:", s.name)
    print("s.dtype (값의 데이터 타입):", s.dtype)
    print("s.index.dtype (인덱스 레이블의 데이터 타입):", s.index.dtype)
    ```
    *출력 예시:*
    ```
    Series s:
     animal
    cat          4
    penguin      2
    dog          4
    butterfly    6
    Name: legs, dtype: int64

    s.index (타입: <class 'pandas.core.indexes.base.Index'>): Index(['cat', 'penguin', 'dog', 'butterfly'], dtype='object', name='animal')
    s.values (타입: <class 'numpy.ndarray'>): [4 2 4 6]
    s.index.name: animal
    s.name: legs
    s.dtype (값의 데이터 타입): int64
    s.index.dtype (인덱스 레이블의 데이터 타입): object
    ```

*   **인덱스 불변성 예시**
    ```python
    # 인덱스 개별 요소 수정 시도 (오류 발생)
    # try:
    #     s.index[0] = 'lion'
    # except TypeError as e:
    #     print(f"\nTypeError: {e}")

    # 인덱스 전체를 새로운 객체로 교체
    new_index = pd.Index(['lion', 'bear', 'tiger', 'zebra'], name='new_animal_index')
    s.index = new_index
    print("\nSeries s after index replacement:\n", s)
    ```

*   **중복 인덱스 처리 예시**
    ```python
    s_dup = pd.Series([10, 20, 30, 40], index=['A', 'B', 'A', 'C'])
    print("\nSeries with duplicate index:\n", s_dup)
    print("s_dup.index.is_unique:", s_dup.index.is_unique) # False가 출력됨

    # 중복 인덱스로 데이터 접근 시 여러 값이 담긴 Series 반환
    print("s_dup.loc['A']:\n", s_dup.loc['A'])
    ```

*   **데이터 타입 불일치 및 `object` dtype 예시**
    ```python
    # 숫자와 문자열이 혼합된 인덱스
    s_mixed_index = pd.Series([100, 200, 300], index=['first', 2, 'third'])
    print("\nSeries with mixed index types:\n", s_mixed_index)
    print("s_mixed_index.index.dtype:", s_mixed_index.index.dtype) # object가 출력됨
    ```
    `object` dtype은 다양한 파이썬 객체를 담을 수 있는 일반적인 타입으로, 여러 종류의 데이터가 섞여 있을 때 나타나며, 이는 성능 저하를 야기하거나 특정 연산에서 예상치 못한 동작을 보일 수 있습니다.

**구체적 예시**

여러분은 도서관의 책을 정리하는 사서라고 상상해 봅시다.
*   **Pandas Series**: 각 책꽂이에 꽂힌 책들(Series)입니다.
*   **`s.index` (인덱스)**: 책꽂이의 각 칸에 붙어 있는 분류 번호나 책 제목(예: '파이썬', '머신러닝', '자료구조')입니다. 이 번호(레이블)를 통해 원하는 책을 찾습니다.
*   **`s.values` (값)**: 분류 번호에 해당하는 실제 책의 내용물(데이터)입니다.
*   **`s.index.name`**: 책꽂이 전체에 붙어있는 "컴퓨터 과학"과 같은 대분류 이름입니다.
*   **`s.name`**: 책꽂이에 꽂힌 책들이 "전공 서적"임을 나타내는 이름입니다.
*   **인덱스 불변성**: 한 번 부여된 분류 번호(인덱스)는 직접 수정할 수 없습니다. 어떤 책의 분류 번호를 바꾸고 싶다면, 해당 책을 기존 분류 번호에서 빼내고 새로운 분류 번호로 다시 넣는(새로운 인덱스 할당) 방식입니다.
*   **중복 인덱스**: 만약 "인공지능"이라는 분류 번호가 붙은 책이 여러 권(판본이 다르거나) 있다면, 그 "인공지능"이라는 분류 번호로 찾았을 때 여러 권의 책이 동시에 반환됩니다. `s.index.is_unique`는 이 분류 번호가 오직 한 권의 책에만 사용되는지 알려줍니다.
*   **데이터 타입 불일치**: 분류 번호(인덱스)가 숫자인데, 실수형으로 저장되거나 문자열로 저장되면, 나중에 "100번" 책을 찾을 때 숫자로 검색해야 할지, 문자열로 검색해야 할지 혼란이 생길 수 있습니다. 이처럼 인덱스와 값의 `dtype` 관리는 매우 중요합니다.

**시험 포인트**

*   ⭐ **Pandas `Series`의 핵심 구성 요소인 `Index`와 `Values`의 역할 및 관계를 정확히 이해해야 합니다.** (예: `s.index`, `s.values`, `pd.Index`와 `np.ndarray`의 관계)
*   ⭐ **`pd.Index` 객체의 불변성(Immutability)**은 Pandas의 중요한 특성이므로 반드시 기억해야 합니다. 인덱스 요소를 직접 수정할 수 없으며, 새로운 `Index` 객체를 할당하여 변경해야 합니다.
*   ⭐ **중복 인덱스 처리 방식**: `s.index.is_unique`를 사용하여 중복 여부를 확인하고, 중복된 인덱스 레이블(`s.loc['label']`)로 데이터를 선택했을 때 어떤 결과(단일 스칼라 vs. `Series`)가 반환되는지 알아야 합니다.
*   ⭐ **`s.dtype`과 `s.index.dtype`의 차이점**을 이해하고, 이들이 데이터 선택 및 연산에 미치는 영향, 특히 `object` 타입 인덱스의 의미를 숙지해야 합니다.

---

## Slide 11

---
### 핵심 개념

이 슬라이드는 **Labeled Array 모델 (Pandas)**과 **Relational 모델 (SQL)** 간의 근본적인 차이점과 공통점을 비교합니다. 데이터의 추상화 방식, 식별자 관리, 결측치 처리, 그리고 핵심 데이터 조작 연산에서의 유사성을 이해하는 것이 중요합니다.

1.  **데이터 추상화 (Data Abstraction)**
    *   **Labeled Array (Pandas)**: `pd.Series`와 `pd.DataFrame`과 같이 **인덱스(index)와 컬럼(columns)이라는 레이블을 가진 배열** 형태의 데이터 구조입니다. 데이터의 논리적인 순서(order)가 중요하게 고려되고 보존됩니다.
    *   **Relational (SQL)**: **명명된 속성(attributes)을 가진 튜플(tuples)들의 집합 또는 묶음(bag)으로 구성된 관계(relations, 즉 테이블)** 입니다. 논리적 순서는 기본적으로 중요하지 않으며, `ORDER BY` 절을 통해서만 순서를 지정할 수 있습니다.

2.  **식별자 및 키 (Identity & Keys)**
    *   **Labeled Array**: 인덱스(index)가 각 데이터 요소에 대한 **레이블**을 제공하며, 이는 메모리 주소 공간처럼 동작합니다. 인덱스는 **유일하지 않을 수 있습니다.**
    *   **Relational**: 기본 키(Primary Key, PK) 또는 후보 키(Candidate Key, CK)와 같은 **키(keys)** 를 사용하여 튜플(행)을 유일하게 식별합니다. 키에는 유일성(uniqueness) 및 참조 무결성(referential integrity)과 같은 제약 조건(constraints)이 강제됩니다.

3.  **결측치 (Missing Data)**
    *   **Labeled Array**: `NaN` (Not a Number) 또는 `pd.NA`로 표현됩니다. `sum()`과 같은 많은 축소(reduction) 연산은 기본적으로 `skipna=True` 옵션을 통해 결측치를 **무시하고 계산**합니다.
    *   **Relational**: `NULL`로 표현되며, 일반적인 논리 연산과 달리 **세 값 논리(three-valued logic: TRUE, FALSE, UNKNOWN)** 를 따릅니다. 대부분의 집계 함수(aggregates)는 정의상 `NULL` 값을 **무시하고 계산**합니다.

4.  **핵심 연산 (Mental Mapping)**
    Pandas의 데이터 조작 연산들은 SQL의 관계형 대수(relational algebra) 개념과 직접적으로 매핑될 수 있습니다.

### 코드/수식 해설 및 구체적 예시

1.  **Series 간 연산 ($s1 + s2$)**
    *   **Pandas**: 두 Series의 **인덱스(labels)를 기준으로 먼저 정렬(align)한 후** 요소별(vectorized) 수학 연산을 수행합니다.
    *   **SQL 유사 개념**: 이는 마치 키(여기서는 인덱스)를 기준으로 `FULL OUTER JOIN`을 수행한 후 계산하는 것과 유사합니다.
    ```python
    import pandas as pd
    s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
    s2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])
    result = s1 + s2
    print(result)
    # 출력:
    # a    NaN
    # b    6.0
    # c    8.0
    # d    NaN
    # dtype: float64
    ```
    `a`와 `d` 인덱스는 한 Series에만 존재하므로, 다른 Series에서는 해당 인덱스에 매칭되는 값이 없어 `NaN`이 됩니다. 이는 `FULL OUTER JOIN` 시 매칭되지 않는 레코드에 `NULL`이 채워지는 것과 유사합니다.

2.  **DataFrame 병합 ($df.merge$)**
    *   **Pandas**: 하나 또는 여러 컬럼을 기준으로 두 DataFrame을 병합합니다. `how` 인자(inner, left, right, outer, cross)를 통해 SQL의 조인(JOIN)과 동일한 기능을 제공합니다.
    *   **SQL 유사 개념**: $df.merge \approx \text{SQL JOIN}$ (INNER, LEFT, RIGHT, FULL OUTER, CROSS JOIN).
    ```python
    df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
    df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value2': [4, 5, 6]})
    merged_df = df1.merge(df2, on='key', how='inner') # INNER JOIN
    print(merged_df)
    # 출력:
    #   key  value1  value2
    # 0   B       2       4
    # 1   C       3       5
    ```

3.  **그룹화 및 집계 ($df.groupby(...).agg(...)$)**
    *   **Pandas**: 특정 컬럼(들)을 기준으로 데이터를 그룹화하고, 각 그룹에 대해 합계, 평균, 개수 등 집계 함수를 적용합니다.
    *   **SQL 유사 개념**: $df.groupby(...).agg(...) \approx \text{SQL GROUP BY aggregates}$.
    ```python
    df = pd.DataFrame({'category': ['A', 'B', 'A', 'B'], 'value': [10, 20, 15, 25]})
    grouped_df = df.groupby('category').agg({'value': 'mean'})
    print(grouped_df)
    # 출력:
    #           value
    # category
    # A          12.5
    # B          22.5
    ```
    이는 SQL의 `SELECT category, AVG(value) FROM df GROUP BY category;`와 동일한 개념입니다.

4.  **데이터 연결 ($pd.concat$)**
    *   **Pandas**: 여러 DataFrame이나 Series를 특정 축(axis)을 따라 연결합니다.
        *   `axis=0` (기본값): 행을 기준으로 데이터를 쌓아 올립니다.
        *   `axis=1`: 컬럼을 기준으로 데이터를 옆으로 붙입니다. 이때 인덱스를 기준으로 정렬됩니다.
    *   **SQL 유사 개념**:
        *   $pd.concat(axis=0) \approx \text{UNION ALL}$ (단순히 행을 추가).
        *   $pd.concat(axis=1) \approx \text{행 인덱스를 기준으로 하는 조인}$ (like a join on row labels).
    ```python
    df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
    concatenated_rows = pd.concat([df1, df2], axis=0)
    print("Rows concatenated (axis=0):\n", concatenated_rows)
    # 출력:
    # Rows concatenated (axis=0):
    #    A  B
    # 0  1  3
    # 1  2  4
    # 0  5  7
    # 1  6  8

    s1 = pd.Series([1, 2], index=['a', 'b'])
    s2 = pd.Series([3, 4], index=['b', 'c'])
    concatenated_cols = pd.concat([s1, s2], axis=1) # 인덱스에 따라 정렬, 마치 JOIN
    print("\nColumns concatenated (axis=1):\n", concatenated_cols)
    # 출력:
    # Columns concatenated (axis=1):
    #      0    1
    # a  1.0  NaN
    # b  2.0  3.0
    # c  NaN  4.0
    ```

### 시험 포인트

*   ⭐ **데이터 모델의 근본적인 차이**: Pandas의 순서 보존 및 레이블링과 SQL의 순서 비의존성 및 집합/묶음 기반 데이터 모델을 명확히 구분할 수 있어야 합니다.
*   ⭐ **식별자/키의 차이**: Pandas 인덱스는 중복될 수 있는 '레이블'이지만, SQL의 기본 키(Primary Key)는 반드시 유일해야 하며 데이터 무결성을 강제하는 '제약 조건'이라는 점을 이해해야 합니다.
*   ⭐ **결측치 처리 방식**: Pandas의 `NaN`/`pd.NA`와 SQL의 `NULL`이 어떻게 표현되고, 특히 집계(aggregation) 연산에서 어떻게 다르게 (혹은 유사하게) 처리되는지 알아야 합니다. SQL의 3-값 논리(`TRUE`, `FALSE`, `UNKNOWN`)가 `NULL` 처리 방식에 미치는 영향을 숙지하세요.
*   ⭐ **Pandas-SQL 연산 매핑**: `pd.Series` 간 연산(인덱스 정렬), `df.merge()`, `df.groupby().agg()`, `pd.concat()` 함수가 각각 SQL의 `JOIN`, `GROUP BY`, `UNION ALL` (혹은 인덱스 기반 조인)에 어떻게 매핑되는지 정확히 이해하고 관련 코드를 작성할 수 있어야 합니다. 특히 `pd.concat`의 `axis` 파라미터가 SQL 연산에 미치는 영향을 주목하세요.

---

## Slide 12

- **핵심 개념**:
    *   **pandas Series**: `pd.Series`는 1차원 레이블링된 배열로, 다양한 데이터 타입을 담을 수 있으며, 각 데이터 포인트에 인덱스(레이블)가 붙습니다.
    *   **Label-based Indexing (`.loc`)**: 데이터의 명시적인 레이블(이름)을 사용하여 데이터를 선택하거나 슬라이싱하는 방법입니다. 슬라이싱 시 시작 레이블과 끝 레이블을 모두 포함합니다.
    *   **Position-based Indexing (`.iloc`)**: 데이터의 0부터 시작하는 정수 위치(인덱스)를 사용하여 데이터를 선택하거나 슬라이싱하는 방법입니다. 슬라이싱 시 시작 위치는 포함하고 끝 위치는 포함하지 않습니다.
    *   **Boolean Masking (조건부 선택)**: 특정 조건을 만족하는 데이터만을 선택하는 방법입니다. 조건식을 통해 생성된 True/False Series(또는 배열)를 사용하여 데이터를 필터링합니다.
    *   **값 설정 모범 사례**: `.loc`을 명시적으로 사용하여 값을 설정하는 것은 "chained assignment" 관련 경고를 피하고 의도된 대로 동작하도록 하는 좋은 습관입니다.

- **코드/수식 해설**:

    *   **pandas Series 생성**:
        ```python
        import pandas as pd
        grades = pd.Series([85, 92, 78, 96],
                           index=['Alice', 'Bob', 'Charlie', 'Diana'],
                           name='grades')
        ```
        `pd.Series()`를 사용하여 이름과 인덱스가 있는 Series 객체를 생성합니다. `index` 인자를 통해 각 값에 대한 레이블을 지정하고, `name` 인자를 통해 Series 자체의 이름을 설정합니다.

    *   **Label-based Indexing (`.loc`)**:
        `grades.loc[label / list / slice]`
        *   `label`: 단일 레이블 (예: `grades.loc['Alice']`)
        *   `list`: 레이블 리스트 (예: `grades.loc[['Alice', 'Diana']]`)
        *   `slice`: 레이블 범위 (예: `grades.loc['Alice':'Charlie']`)
            *   ⭐ **슬라이싱 시 끝 레이블(예: 'Charlie')을 포함합니다.**
            *   존재하지 않는 레이블을 `.loc`으로 조회 시 `KeyError` 발생. `reindex`를 사용하면 없는 레이블에 `NaN`을 채울 수 있습니다.

    *   **Position-based Indexing (`.iloc`)**:
        `grades.iloc[pos / list / slice]`
        *   `pos`: 단일 위치 (예: `grades.iloc[0]`)
        *   `list`: 위치 리스트 (예: `grades.iloc[[0, 3]]`)
        *   `slice`: 위치 범위 (예: `grades.iloc[0:2]`)
            *   ⭐ **슬라이싱 시 끝 위치(예: 2)를 포함하지 않습니다.** (파이썬 리스트 슬라이싱과 동일)
            *   인덱스가 정수형일 때 `grades[0]`과 같은 모호함을 피하기 위해 `iloc` 사용을 권장합니다.

    *   **Boolean Mask (조건부 선택)**:
        `grades[mask]` 또는 `grades.loc[mask]`
        *   `mask`는 `grades`와 같은 길이를 가지는 `bool` 타입의 Series/array입니다.
        *   예시: `grades >= 90`은 각 원소가 90 이상인지 여부를 True/False로 반환하는 Series를 생성합니다.
        *   여러 조건을 조합할 때는 `&` (AND), `|` (OR), `~` (NOT) 비트 연산자를 사용하며, 각 조건은 반드시 괄호로 묶어야 합니다.
        *   예시: `(grades >= 90) & (grades < 95)`

- **구체적 예시**:

    다음 `grades` Series를 가정합니다:
    ```
    Alice      85
    Bob        92
    Charlie    78
    Diana      96
    Name: grades, dtype: int64
    ```

    *   **Label-based Indexing (`.loc`)**:
        ```python
        print(grades.loc['Bob'])       # Bob의 점수
        # 출력: 92

        print(grades.loc['Alice':'Charlie']) # Alice부터 Charlie까지의 점수 (Charlie 포함)
        # 출력:
        # Alice      85
        # Bob        92
        # Charlie    78
        # Name: grades, dtype: int64
        ```

    *   **Position-based Indexing (`.iloc`)**:
        ```python
        print(grades.iloc[1])          # 두 번째 위치 (인덱스 1)의 점수 (Bob)
        # 출력: 92

        print(grades.iloc[0:2])        # 첫 번째 위치부터 세 번째 위치 직전까지 (0, 1)의 점수 (Alice, Bob)
        # 출력:
        # Alice    85
        # Bob      92
        # Name: grades, dtype: int64
        ```

    *   **Boolean Mask (조건부 선택)**:
        ```python
        print(grades[grades >= 90])    # 90점 이상인 학생들의 점수
        # 출력:
        # Bob      92
        # Diana    96
        # Name: grades, dtype: int64

        print(grades[(grades >= 90) & (grades < 95)]) # 90점 이상 95점 미만인 학생들의 점수
        # 출력:
        # Bob    92
        # Name: grades, dtype: int64
        ```

    *   **값 설정 예시**:
        ```python
        grades.loc['Alice'] = 90 # Alice의 점수를 90으로 변경
        print(grades.loc['Alice'])
        # 출력: 90
        ```

- **시험 포인트**:

    *   ⭐ **`.loc`은 레이블 기반, `.iloc`은 위치 기반 인덱싱임을 정확히 구분해야 합니다.**
    *   ⭐ **슬라이싱에서 `.loc`은 `stop` 레이블을 포함하지만, `.iloc`은 `stop` 위치를 포함하지 않는다는 점이 중요합니다.** (파이썬 슬라이싱 규칙과 `.iloc`은 동일)
    *   ⭐ **`.loc`으로 존재하지 않는 레이블에 접근하면 `KeyError`가 발생하며, 이를 `NaN`으로 처리하고 싶다면 `reindex`를 고려해야 합니다.**
    *   ⭐ **인덱스가 정수형인 경우, `grades[0]`과 같은 기본 인덱싱 대신 `grades.iloc[0]`을 사용하여 명확성을 확보하는 것이 좋습니다.**
    *   ⭐ **Boolean masking에서 여러 조건을 조합할 때는 반드시 비트 연산자 (`&`, `|`, `~`)를 사용하고, 각 조건을 괄호 `()`로 묶어야 합니다.** (예: `(condition1) & (condition2)`) 파이썬의 `and`, `or`, `not` 키워드는 pandas Series에서는 동작하지 않습니다.
    *   ⭐ **Series나 DataFrame의 특정 값(들)을 변경할 때, `df.loc[row_label, col_label] = value`와 같이 `.loc`을 왼쪽에 사용하여 "chained assignment" 경고를 방지하고 올바른 동작을 보장하는 것이 모범 사례입니다.**

---

## Slide 13

**핵심 개념**

이 슬라이드는 `pandas.Series` 객체에서 데이터를 선택(Selection)하는 다양한 방법을 설명합니다. 주로 **레이블(Label) 기반**, **위치(Position) 기반**, 그리고 **불리언 마스크(Boolean Mask) (조건) 기반** 세 가지 방식으로 데이터를 추출하는 방법을 다룹니다. 이 방법들은 데이터 분석 시 특정 조건을 만족하거나 특정 위치/레이블에 해당하는 데이터를 신속하게 찾아내고 조작하는 데 필수적입니다.

**코드/수식 해설**

**1. 초기 Series 설정 (Setup)**

```python
import pandas as pd

grades = pd.Series([85, 92, 78, 96],
                   index=['Alice', 'Bob', 'Charlie', 'Diana'],
                   name='grades')
```
- `pd.Series()`: pandas Series 객체를 생성합니다.
- `[85, 92, 78, 96]`: Series의 값(data)입니다.
- `index=['Alice', 'Bob', 'Charlie', 'Diana']`: 각 값에 해당하는 사용자 정의 레이블 인덱스입니다.
- `name='grades'`: Series 자체에 부여된 이름입니다.

**2. 레이블 기반 선택 (`.loc`)**

`.loc` 접근자는 Series의 레이블 인덱스를 사용하여 데이터를 선택합니다.

```python
grades.loc['Alice']        # 단일 레이블 선택
grades.loc[['Alice', 'Diana']] # 여러 레이블을 리스트로 선택
grades.loc['Alice':'Charlie'] # 레이블 슬라이싱 (시작 레이블부터 끝 레이블까지 포함)

# grades.loc['Eve'] # 존재하지 않는 레이블을 선택 시 KeyError 발생
```
- `grades.loc['Alice']`: 'Alice'라는 레이블에 해당하는 값(85)을 반환합니다.
- `grades.loc[['Alice', 'Diana']]`: 'Alice'와 'Diana' 레이블에 해당하는 값(85, 96)을 Series 형태로 반환합니다.
- `grades.loc['Alice':'Charlie']`: 'Alice'부터 'Charlie'까지의 모든 레이블에 해당하는 값(85, 92, 78)을 Series 형태로 반환합니다.
    - ⭐ **`.loc`을 이용한 슬라이싱은 시작 레이블과 끝 레이블을 모두 포함(inclusive)합니다.**

**3. 위치 기반 선택 (`.iloc`)**

`.iloc` 접근자는 Series의 정수 위치(0부터 시작하는 인덱스)를 사용하여 데이터를 선택합니다.

```python
grades.iloc[0]          # 단일 위치 선택 (첫 번째 항목)
grades.iloc[[0, 3]]       # 여러 위치를 리스트로 선택 (첫 번째, 네 번째 항목)
grades.iloc[0:2]          # 위치 슬라이싱 (0번 위치부터 2번 위치 직전까지)
```
- `grades.iloc[0]`: 0번 위치(첫 번째)에 해당하는 값(85)을 반환합니다.
- `grades.iloc[[0, 3]]`: 0번 위치와 3번 위치에 해당하는 값(85, 96)을 Series 형태로 반환합니다.
- `grades.iloc[0:2]`: 0번 위치부터 2번 위치 직전까지(즉, 0번과 1번 위치)의 값(85, 92)을 Series 형태로 반환합니다.
    - ⭐ **`.iloc`을 이용한 슬라이싱은 시작 위치는 포함하고 끝 위치는 포함하지 않습니다(exclusive), 이는 Python 리스트 슬라이싱과 동일합니다.**
- 슬라이드 코멘트: "Prefer `iloc` over `[]` when the index is integer-like (avoids ambiguity)"
    - 만약 Series의 인덱스가 정수(예: `pd.Series([10, 20], index=[0, 1])`)인 경우, `series[0]`과 같은 직접 인덱싱은 레이블 기반인지 위치 기반인지 모호할 수 있습니다. 이러한 모호성을 피하기 위해 **인덱스가 정수인 경우에도 `.loc` 또는 `.iloc`을 명시적으로 사용하는 것이 좋습니다.**

**4. 불리언 마스크 (조건) 기반 선택 (`[]` 또는 `.loc[]`)**

불리언 마스크는 Series와 동일한 길이의 `True`/`False` 값으로 구성된 Series(또는 배열)를 사용하여 `True`에 해당하는 값만 선택하는 방법입니다.

```python
mask = grades >= 90 # 조건에 따라 True/False 불리언 Series 생성
grades[mask]        # 불리언 마스크를 직접 적용

# 여러 조건 결합 시 괄호 필수
grades.loc[(grades >= 90) & (grades < 95)] # grades가 90 이상이고 95 미만인 항목 선택
```
- `mask = grades >= 90`: 각 성적이 90점 이상인지 확인하여 `[False, True, False, True]`와 같은 불리언 Series를 생성합니다.
- `grades[mask]`: `mask`가 `True`인 위치의 값만 선택하여 Series로 반환합니다 (여기서는 Bob의 92, Diana의 96).
- `(grades >= 90) & (grades < 95)`: 여러 조건을 결합할 때, 각 조건은 괄호로 묶어야 하며, 논리 연산자 `&` (AND), `|` (OR), `~` (NOT)을 사용합니다.
    - Python의 기본 논리 연산자 `and`, `or`, `not`은 Series 전체에 적용되지 않고 스칼라 값에만 작동하므로, pandas에서는 비트wise 연산자 `&`, `|`, `~`를 사용해야 합니다.
    - ⭐ **여러 조건을 결합할 때는 각 개별 조건을 반드시 괄호 `()`로 묶어야 합니다.**

**구체적 예시**

`grades` Series:
```
Alice      85
Bob        92
Charlie    78
Diana      96
Name: grades, dtype: int64
```

*   **Alice의 성적 확인**: `grades.loc['Alice']`는 `85`를 반환합니다.
*   **처음 두 학생의 성적 확인 (레이블)**: `grades.loc['Alice':'Bob']`는 `Alice`와 `Bob`의 성적 `(85, 92)`을 반환합니다.
*   **처음 두 학생의 성적 확인 (위치)**: `grades.iloc[0:2]`는 `Alice`와 `Bob`의 성적 `(85, 92)`을 반환합니다. (0번과 1번 위치)
*   **90점 이상인 학생들만 보기**:
    `mask = grades >= 90`
    `print(mask)`
    ```
    Alice      False
    Bob         True
    Charlie    False
    Diana       True
    Name: grades, dtype: bool
    ```
    `grades[mask]`
    ```
    Bob      92
    Diana    96
    Name: grades, dtype: int64
    ```

**시험 포인트**

*   ⭐ **`.loc`은 레이블 기반, `.iloc`은 위치 기반**이라는 것을 명확히 이해하고 구분해야 합니다.
*   ⭐ **`.loc`을 이용한 슬라이싱은 종료 레이블을 포함(inclusive)하고, `.iloc`을 이용한 슬라이싱은 종료 위치를 포함하지 않습니다(exclusive).** 이 차이점을 반드시 기억해야 합니다.
*   ⭐ 불리언 마스크를 이용한 조건부 선택 시, 여러 조건을 결합할 때는 **반드시 각 개별 조건을 괄호로 묶고 `&`, `|`, `~` 연산자를 사용해야 합니다.** (예: `(condition1) & (condition2)`)
*   Series의 인덱스가 정수형일 때, `[]` 대신 `.loc` 또는 `.iloc`을 명시적으로 사용하는 것이 모호성을 피하고 코드를 명확하게 만드는 데 중요합니다.

---

## Slide 14

**핵심 개념**

Pandas Series에서 데이터를 선택하는 방법은 크게 두 가지로 나뉩니다: **레이블(label) 기반 인덱싱**과 **위치(position) 기반 인덱싱**. 이 슬라이드는 이 두 가지 방식의 차이를 설명하고, 코드의 명확성 및 잠재적 오류 방지를 위해 `.loc` (레이블 기반)과 `.iloc` (위치 기반)을 사용하는 것을 강력히 권장합니다.

*   **레이블 기반 인덱싱**: Series의 `index`에 명시된 이름(레이블)을 사용하여 특정 요소를 선택하거나 범위를 지정합니다.
*   **위치 기반 인덱싱**: 0부터 시작하는 정수 위치(순서)를 사용하여 요소를 선택하거나 범위를 지정합니다. 이는 파이썬 리스트의 인덱싱과 유사합니다.
*   **`[]` 연산자의 모호성**: 일반적인 대괄호 `[]`를 사용한 인덱싱은 레이블과 위치 인덱싱 모두에 사용될 수 있어, 특히 정수형 레이블이 있을 때 혼란을 야기할 수 있습니다.

**코드/수식 해설**

예시 Series `s`를 먼저 생성합니다.

```python
import pandas as pd

# Series 생성: 각 도시에 대한 값과 함께 명시적인 레이블(index)을 부여
s = pd.Series([0.6, 0.7, 2.2, 10.5], index=['Athens', 'Oslo', 'Paris', 'Bangkok'])
print(s)
# Output:
# Athens      0.6
# Oslo        0.7
# Paris       2.2
# Bangkok    10.5
# dtype: float64
```

1.  **단일 요소 선택 (Single Element Selection)**:
    *   **레이블로 선택**:
        ```python
        # s['Paris']: 'Paris' 레이블의 요소 선택
        print(f"s['Paris']: {s['Paris']}") # Output: s['Paris']: 2.2

        # s.loc['Paris']: 명확하게 'Paris' 레이블의 요소 선택
        print(f"s.loc['Paris']: {s.loc['Paris']}") # Output: s.loc['Paris']: 2.2
        ```
    *   **위치로 선택**:
        ```python
        # s[2]: 위치 2 (세 번째 요소)의 요소 선택. (레이블 '2'가 없을 경우)
        print(f"s[2]: {s[2]}") # Output: s[2]: 2.2

        # s.iloc[2]: 명확하게 위치 2 (세 번째 요소)의 요소 선택
        print(f"s.iloc[2]: {s.iloc[2]}") # Output: s.iloc[2]: 2.2
        ```

2.  **슬라이싱 (Slicing)**:
    *   **레이블 기반 슬라이싱 (`.loc`)**:
        시작 레이블과 **끝 레이블 모두를 포함($\text{inclusive}$)**하여 선택합니다.
        ```python
        # s.loc['Oslo':'Paris']: 'Oslo' 레이블부터 'Paris' 레이블까지 모두 포함
        print("s.loc['Oslo':'Paris']:\n", s.loc['Oslo':'Paris'], sep='')
        # Output:
        # Oslo    0.7
        # Paris   2.2
        # dtype: float64

        # s.loc[:'Oslo']: 시작부터 'Oslo' 레이블까지 모두 포함
        print("s.loc[:'Oslo']:\n", s.loc[:'Oslo'], sep='')
        # Output:
        # Athens    0.6
        # Oslo      0.7
        # dtype: float64
        ```
    *   **위치 기반 슬라이싱 (`.iloc`)**:
        시작 위치는 포함하고, **끝 위치는 제외($\text{exclusive}$)**하여 선택합니다. 파이썬 리스트 슬라이싱 규칙과 동일합니다.
        ```python
        # s.iloc[1:3]: 위치 1부터 3 이전까지 (즉, 위치 1과 2)
        print("s.iloc[1:3]:\n", s.iloc[1:3], sep='')
        # Output:
        # Oslo    0.7
        # Paris   2.2
        # dtype: float64

        # s.iloc[:2]: 시작(위치 0)부터 2 이전까지 (즉, 위치 0과 1)
        print("s.iloc[:2]:\n", s.iloc[:2], sep='')
        # Output:
        # Athens    0.6
        # Oslo      0.7
        # dtype: float64
        ```
    *   **일반 `[]` 연산자를 이용한 슬라이싱 (모호성 주의)**:
        레이블을 사용하면 끝 레이블을 포함하지만, 정수(위치)를 사용하면 끝 위치를 제외합니다.
        ```python
        # s['Oslo':'Paris']: 레이블 슬라이싱 (끝 레이블 포함)
        print("s['Oslo':'Paris']:\n", s['Oslo':'Paris'], sep='')
        # Output:
        # Oslo    0.7
        # Paris   2.2
        # dtype: float64

        # s[1:3]: 위치 슬라이싱 (끝 위치 제외)
        print("s[1:3]:\n", s[1:3], sep='')
        # Output:
        # Oslo    0.7
        # Paris   2.2
        # dtype: float64
        ```

**구체적 예시**

어떤 서점에서 책을 찾는다고 가정해봅시다.

*   `s.loc['데이터 과학 입문']`: 책꽂이에서 "데이터 과학 입문"이라는 제목의 책을 찾습니다. 책의 **제목(레이블)**을 정확히 알고 찾아가는 방식입니다.
*   `s.iloc[7]`: 책꽂이의 왼쪽에서부터 8번째(0부터 세어서 7번째) 책을 찾습니다. 책의 **물리적인 위치(포지션)**를 세어서 찾아가는 방식입니다.
*   `s.loc['선형대수':'미적분학']`: "선형대수" 책부터 "미적분학" 책까지 (**두 책 모두 포함**) 모든 책을 가져옵니다.
*   `s.iloc[3:6]`: 왼쪽에서 4번째 책부터 6번째 책까지 (**6번째 책은 제외**) 가져옵니다.
*   만약 책 제목이 '1', '2', '3'과 같은 숫자였다면, `s[2]`라고 했을 때, 이것이 '2'라는 제목의 책을 찾은 것인지, 아니면 왼쪽에서 3번째 책(위치 2)을 찾은 것인지 헷갈릴 수 있습니다. `.loc[2]`는 반드시 '2'라는 레이블을, `.iloc[2]`는 반드시 위치 2의 요소를 찾으므로 의도가 명확해집니다.

**시험 포인트**

*   ⭐ **`.loc`와 `.iloc`의 핵심 차이**:
    *   `.loc`: **레이블(label)** 기반 인덱싱 (예: `s.loc['Paris']`)
    *   `.iloc`: **위치(position)** 기반 인덱싱 (예: `s.iloc[2]`)
*   ⭐ **슬라이싱 규칙의 차이점**:
    *   `.loc`를 사용한 레이블 슬라이싱: 시작 레이블과 **끝 레이블 모두 포함 ($\text{inclusive}$)**.
    *   `.iloc`를 사용한 위치 슬라이싱: 시작 위치는 포함하고, **끝 위치는 제외 ($\text{exclusive}$)**. (Python 리스트 슬라이싱과 동일)
*   ⭐ **`[]` 연산자의 모호성**:
    *   정수형 레이블이 존재할 경우, `s[1]`과 같이 정수로 인덱싱할 때, `[]`는 레이블 `1`을 의미하는지, 아니면 위치 `1` (두 번째 요소)을 의미하는지 **모호성(ambiguity)**이 발생할 수 있습니다.
    *   슬라이싱에서도 `[]`는 레이블 슬라이싱 시 끝 레이블을 포함하고, 위치 슬라이싱 시 끝 위치를 제외하므로 일관성이 부족합니다.
    *   이러한 모호성을 피하고 코드의 명확성을 높이기 위해 `.loc`와 `.iloc`를 사용하는 것이 강력히 권장됩니다.

---

## Slide 15

본 슬라이드는 Pandas Series에서 불리언 마스킹을 이용하여 데이터를 선택하는 방법을 다룹니다. 특히 `isin()` 및 `between()` 메서드를 활용한 값(value) 기반 필터링에 중점을 둡니다.

---

### **핵심 개념**

*   **불리언 마스킹 (Boolean Masking)**: Pandas Series 또는 DataFrame에서 특정 조건을 만족하는 데이터를 효율적으로 선택(필터링)하는 기법입니다. 조건을 평가하여 True/False 값으로 이루어진 불리언 Series(마스크)를 생성하고, 이 마스크의 True에 해당하는 위치의 데이터만 원본 Series/DataFrame에서 추출합니다.
*   **`Series.isin(values)`**: Series의 각 요소가 주어진 `values` 리스트(또는 배열) 안에 포함되어 있는지 여부를 확인하는 불리언 마스크를 생성합니다. 여러 개의 특정 값 중 하나라도 일치하는 데이터를 필터링할 때 매우 유용합니다. 이는 논리합(OR) 조건과 유사하게 작동합니다.
*   **`Series.between(lower, upper, inclusive=True)`**: Series의 각 요소가 `lower`와 `upper` 사이에 포함되는지 여부를 확인하는 불리언 마스크를 생성합니다. 기본적으로 `inclusive=True`로 설정되어 `lower <= value <= upper` 조건을 만족하는 요소를 선택합니다. 숫자형 데이터의 특정 범위 필터링에 특화되어 있습니다. 이는 논리곱(AND) 조건과 유사하게 작동합니다.
*   **값(Values) 기준 필터링 vs. 인덱스(Labels) 기준 필터링**:
    *   **값 기준 필터링**: Series의 실제 데이터 값을 기반으로 조건을 설정하여 데이터를 선택합니다 (예: `s[s == 'cat']`).
    *   **인덱스 기준 필터링**: Series의 인덱스(레이블)를 기반으로 조건을 설정하여 데이터를 선택합니다 (예: `s.loc[s.index == 'a']`).

### **코드/수식 해설**

1.  **기본 불리언 조건 및 논리 연산자**:
    ```python
    import pandas as pd

    s_str = pd.Series(['cat', 'dog', 'panda', 'cat', 'dragon'], index=list('abcde'))
    s_num = pd.Series([5, 2, 7, 4, 9], index=list('abcde'))

    # 문자열 값 비교 (요소별 비교)
    mask_cat = (s_str == 'cat') # True, False, False, True, False
    mask_dog = (s_str == 'dog') # False, True, False, False, False

    # 논리합 (OR) 연산: |
    # (s_str == 'cat') | (s_str == 'dog')
    # 결과: [ True,  True, False,  True, False]
    print("Mask for 'cat' or 'dog':\n", (mask_cat | mask_dog))

    # 숫자 값 범위 비교 (논리곱 AND 연산: &)
    # s_num의 값이 3 이상 7 이하인 경우
    # (s_num >= 3) & (s_num <= 7)
    # 결과: [ True, False,  True,  True, False]
    ```
    *   `==`, `>=`, `<=` 와 같은 비교 연산자는 Series의 각 요소를 개별적으로 비교하여 불리언 Series(마스크)를 반환합니다.
    *   두 개 이상의 불리언 조건을 결합할 때는 논리곱 `&` (AND) 또는 논리합 `|` (OR) 연산자를 사용합니다. 이때 **각 개별 조건을 반드시 괄호 `()`로 묶어야 합니다.** 이는 파이썬의 연산자 우선순위 때문입니다.

2.  **`Series.isin()` 메서드**:
    ```python
    # s_str에서 'cat' 또는 'dog'인 값을 선택
    s_str_filtered_isin = s_str[s_str.isin(['cat', 'dog'])]
    print("\nFiltered string Series (isin):\n", s_str_filtered_isin)
    ```
    *   `s_str.isin(['cat', 'dog'])`는 `s_str`의 각 값이 리스트 `['cat', 'dog']` 안에 포함되는지 여부를 불리언 Series로 반환합니다. 이 마스크를 사용하여 `s_str`을 필터링합니다.

3.  **`Series.between()` 메서드**:
    ```python
    # s_num에서 값이 3 이상 7 이하인 값을 선택
    s_num_filtered_between = s_num[s_num.between(3, 7)]
    print("\nFiltered numeric Series (between):\n", s_num_filtered_between)
    ```
    *   `s_num.between(3, 7)`는 `s_num`의 각 값이 $3 \le \text{value} \le 7$ 범위에 있는지 여부를 불리언 Series로 반환합니다. 이 마스크를 사용하여 `s_num`을 필터링합니다. 기본적으로 `inclusive=True`입니다.

4.  **인덱스(레이블) 기준 필터링**:
    ```python
    # s_str에서 인덱스가 'a' 또는 'd'인 데이터를 선택
    s_str_filtered_by_label_isin = s_str.loc[s_str.index.isin(['a', 'd'])]
    print("\nFiltered string Series (by label isin):\n", s_str_filtered_by_label_isin)

    # s_num에서 인덱스가 'a'인 데이터를 선택
    s_num_filtered_by_label_eq = s_num.loc[s_num.index == 'a']
    print("\nFiltered numeric Series (by label == 'a'):\n", s_num_filtered_by_label_eq)
    ```
    *   `s.loc[]` 인덱서와 `s.index`를 활용하여 인덱스 값을 기준으로 조건을 설정합니다. `s.index`는 Series의 인덱스 객체를 반환하며, 여기에 `isin()` 또는 `==` 등의 비교 연산자를 적용할 수 있습니다.

### **구체적 예시**

어떤 쇼핑몰의 주문 데이터(`orders`) Series가 있다고 가정해 봅시다. 인덱스는 주문 ID, 값은 주문 상품명입니다.

```python
import pandas as pd

orders = pd.Series({
    'ORDER_001': 'Laptop',
    'ORDER_002': 'Mouse',
    'ORDER_003': 'Keyboard',
    'ORDER_004': 'Laptop',
    'ORDER_005': 'Monitor',
    'ORDER_006': 'Mouse'
})
print("Original Orders:\n", orders)

# 1. 'Laptop' 또는 'Monitor' 주문만 필터링 (isin 활용)
# 고객이 전자기기 품목 중 특정 품목에만 관심 있을 때 사용
electronic_orders = orders[orders.isin(['Laptop', 'Monitor'])]
print("\nLaptop or Monitor Orders:\n", electronic_orders)

# 2. 주문 ID가 'ORDER_002'부터 'ORDER_005' 사이에 있는 주문 필터링 (between 활용 - 인덱스가 숫자처럼 순서가 있는 경우)
# 실제 인덱스가 문자열일 경우 between은 동작하지 않으므로, 숫자 인덱스 Series를 예로 들어본다.
# 또는 슬라이드와 같이 숫자형 Series에 between을 적용한다.
# 예시를 위해 주문 금액 Series를 생성
order_amounts = pd.Series({
    'ORDER_001': 1200, 'ORDER_002': 25, 'ORDER_003': 80,
    'ORDER_004': 1100, 'ORDER_005': 300, 'ORDER_006': 30
})
print("\nOriginal Order Amounts:\n", order_amounts)

# 30 이상 500 이하의 주문 금액 필터링
mid_range_orders = order_amounts[order_amounts.between(30, 500)]
print("\nOrders with amount between 30 and 500:\n", mid_range_orders)
```
이 예시를 통해 실제 데이터에서 특정 조건에 맞는 데이터를 손쉽게 추출하고 분석할 수 있음을 확인할 수 있습니다.

### **시험 포인트**

*   ⭐ **불리언 마스킹의 기본 동작 원리**: 조건을 만족하는 True 값이 있는 위치의 데이터만 선택된다는 것을 정확히 이해해야 합니다.
*   ⭐ **`isin()`과 `between()`의 사용 목적과 기능적 차이**:
    *   `isin()`은 **이산적인 여러 값** 중 하나라도 해당하는 경우 (OR 조건)에 사용합니다. (예: 특정 상품 목록, 특정 지역 코드)
    *   `between()`은 **연속적인 숫자 범위**에 해당하는 경우 (AND 조건)에 사용합니다. (예: 특정 점수대, 특정 나이대)
*   ⭐ **값(Values) 기준 필터링과 인덱스(Labels) 기준 필터링의 차이점 및 구문**:
    *   값 필터링: `s[s.isin(...)]`, `s[s == value]` 등 Series의 *값*에 조건을 적용합니다.
    *   인덱스 필터링: `s.loc[s.index.isin(...)]`, `s.loc[s.index == label]` 등 `s.index` 객체에 조건을 적용하고 `loc`를 사용합니다.
*   ⭐ **복합 조건 사용 시 `&` (AND), `|` (OR) 연산자와 괄호 `()`의 필수 사용**: 파이썬의 비트wise 연산자 `&`, `|`가 비교 연산자보다 우선순위가 높기 때문에, 각 개별 조건을 괄호로 묶지 않으면 예상치 못한 결과가 발생할 수 있습니다.
*   `s == 'value'`와 같은 비교는 인덱스가 아닌 `values`를 element-wise로 비교하여 불리언 마스크를 생성합니다.

---

## Slide 16

---
### Find by Value — Vector scan vs Indexed lookup

**핵심 개념**:
데이터프레임이나 Series에서 특정 값을 찾거나, 특정 인덱스에 해당하는 값을 찾는 두 가지 주요 접근 방식인 **Vector scan**과 **Indexed lookup**에 대해 다룹니다.

*   **Vector scan (값 $\rightarrow$ 인덱스/위치)**:
    *   Series의 *값(values)*을 기반으로 해당 값의 *인덱스(labels)* 또는 *위치(positions)*를 찾아내는 방법입니다.
    *   데이터 전체를 순회하며(스캔) 원하는 값을 찾아냅니다. 이는 특히 인덱스가 아닌 데이터 내용 자체를 탐색할 때 사용됩니다.
*   **Indexed lookup (인덱스 $\rightarrow$ 값)**:
    *   Series의 *인덱스(keys)*를 기반으로 해당 인덱스에 저장된 *값(values)*을 찾아내는 방법입니다.
    *   이는 인덱스(레이블)를 통한 직접 접근 방식이며, 일반적으로 해시 테이블이나 트리 구조를 사용하여 매우 효율적입니다.
    *   값이 주어졌을 때 해당 값의 인덱스를 효율적으로 찾기 위해 역매핑(reverse map)을 한 번 구축하여 재사용할 수 있습니다.

**코드/수식 해설**:

*   **Vector scan 예시**:
    *   **특정 값 `v`와 일치하는 모든 항목의 인덱스(label) 또는 위치(position) 찾기**:
        ```python
        import pandas as pd
        s = pd.Series([10, 20, 10, 30, 20], index=['A', 'B', 'C', 'D', 'E'])
        v = 20

        # 불리언 마스크를 사용하여 값이 v인 위치를 True로 표시
        mask = s.eq(v) # 또는 s == v
        print(f"Mask: {mask.to_list()}") # 출력: Mask: [False, True, False, False, True]

        # 마스크를 사용하여 원본 Series의 인덱스에서 일치하는 인덱스 추출
        result_labels = s.index[mask]
        print(f"Matching labels: {list(result_labels)}") # 출력: Matching labels: ['B', 'E']

        # 또는 마스크의 True인 위치(numpy 배열 인덱스)를 얻음
        result_positions = mask.to_numpy().nonzero()[0]
        print(f"Matching positions (0-indexed): {list(result_positions)}") # 출력: Matching positions (0-indexed): [1, 4]
        ```
    *   **최댓값 또는 최솟값의 인덱스(label) 찾기**:
        ```python
        max_label = s.idxmax() # 최댓값(30)을 가진 항목의 인덱스 'D' 반환
        min_label = s.idxmin() # 최솟값(10)을 가진 항목의 인덱스 'A' 반환
        print(f"Label of max value: {max_label}") # 출력: Label of max value: D
        print(f"Label of min value: {min_label}") # 출력: Label of min value: A
        ```
    *   **정렬된 데이터에서 특정 값 `v`가 삽입될 위치 찾기**:
        ```python
        # Series의 값을 numpy 배열로 변환 후 searchsorted 사용 (정렬된 데이터에 효율적)
        sorted_values = s.sort_values().values # [10, 10, 20, 20, 30]
        insertion_pos = sorted_values.searchsorted(15) # 15가 들어갈 위치
        print(f"Insertion position for 15 in sorted values: {insertion_pos}") # 출력: Insertion position for 15 in sorted values: 2
        ```

*   **Indexed lookup 예시**:
    *   **특정 인덱스 `key`에 해당하는 값 찾기**:
        ```python
        value_at_C = s.loc['C'] # 인덱스 'C'에 해당하는 값 10 반환
        print(f"Value at index 'C': {value_at_C}") # 출력: Value at index 'C': 10
        ```
    *   **값(value)으로 인덱스(label)를 효율적으로 찾기 위한 역매핑 Series 생성**:
        ```python
        # s의 값을 새로운 Series의 인덱스로, s의 인덱스를 새로운 Series의 값으로 설정
        # 중복된 값이 있을 경우, 기본적으로 마지막 값으로 덮어써지거나 에러 발생 가능성이 있으므로 주의
        # 예: s에 10이 두 번('A', 'C') 나오지만 rev에는 10: 'C'만 남을 수 있음.
        rev_series_simple = pd.Series(s.index, index=s.values)
        print(f"Simple reverse series:\n{rev_series_simple}")
        # 출력 (예시):
        # 10    C
        # 20    E
        # 30    D
        # dtype: object

        # ⭐ 중복된 값에 대한 모든 인덱스를 얻기 위한 처리 (group map to lists)
        rev_series_with_duplicates = s.groupby(s.values).apply(lambda x: list(x.index))
        print(f"Reverse series with duplicates:\n{rev_series_with_duplicates}")
        # 출력:
        # 10    [A, C]
        # 20    [B, E]
        # 30       [D]
        # dtype: object
        print(f"Labels for value 10: {rev_series_with_duplicates[10]}") # 출력: Labels for value 10: ['A', 'C']
        ```

**구체적 예시**:
쇼핑몰 구매 내역 데이터 `purchases = pd.Series([12000, 5000, 12000, 20000], index=['UserA', 'UserB', 'UserC', 'UserD'])`가 있다고 가정해 봅시다.

*   **Vector scan 예시**:
    *   **12000원을 지출한 모든 사용자 찾기**:
        ```python
        users_spent_12k = purchases.index[purchases == 12000]
        print(f"Users who spent 12000: {list(users_spent_12k)}")
        # 출력: Users who spent 12000: ['UserA', 'UserC']
        ```
    *   **가장 많이 지출한 사용자 찾기**:
        ```python
        top_spender = purchases.idxmax()
        print(f"Top spender: {top_spender}")
        # 출력: Top spender: UserD
        ```
*   **Indexed lookup 예시**:
    *   **'UserB'의 지출액 확인하기**:
        ```python
        userb_spend = purchases.loc['UserB']
        print(f"UserB spent: {userb_spend}")
        # 출력: UserB spent: 5000
        ```
    *   **20000원을 지출한 사용자가 누구인지 역매핑으로 찾기**:
        ```python
        # 실제 사용에서는 중복 값 처리를 고려한 역매핑 (위 코드/수식 해설 참조)
        # 예시로 rev_series_with_duplicates를 사용
        rev_map = purchases.groupby(purchases.values).apply(lambda x: list(x.index))
        spender_20k = rev_map[20000]
        print(f"User(s) who spent 20000: {spender_20k}")
        # 출력: User(s) who spent 20000: ['UserD']
        ```

**시험 포인트**:
*   ⭐ **Vector scan**은 `values`를 기반으로 `labels` 또는 `positions`를 찾는 것이고, **Indexed lookup**은 `keys` (index labels)를 기반으로 `values`를 찾는 것임을 명확히 구분해야 합니다.
*   ⭐ `s.eq(v)` 또는 `s == v`를 이용한 불리언 마스크는 특정 값을 가진 모든 항목의 인덱스를 찾는 데 사용되는 핵심 기법입니다.
*   ⭐ `s.idxmax()`와 `s.idxmin()`은 최댓값/최솟값의 *인덱스(label)*를 반환하며, 이는 *값(value)*이 아님에 유의해야 합니다.
*   ⭐ **Pitfall**: `value`를 검색하는 것은 `s.loc`과 같이 `index label`로 검색하는 것과 다릅니다. 이 둘을 혼동하지 않도록 주의하세요. `s.loc`은 `label-based` 인덱싱에 사용됩니다.
*   ⭐ 중복된 값을 처리하여 역매핑(값 $\rightarrow$ 인덱스) Series를 만들 때는 `groupby().apply(list)`와 같은 방법을 활용해야 모든 해당 인덱스를 얻을 수 있습니다.

---

## Slide 17

POSTECH 컴퓨터공학과 전공 튜터입니다. 데이터분석 입문 강의 자료 슬라이드 "Find by Value — Quick Examples"에 대한 마크다운 노트입니다.

---

### **핵심 개념**
이 슬라이드는 `pandas.Series` 객체에서 **값(value)**을 기준으로 데이터를 검색하고 추출하는 다양한 방법을 소개합니다. 특정 값을 가진 데이터의 인덱스(label)를 찾거나, 시리즈 내 최댓값/최솟값의 인덱스를 확인하고, 심지어 특정 값의 물리적 위치(position)를 찾는 기법들을 다룹니다.

### **코드/수식 해설**

```python
import pandas as pd
import numpy as np

# 기본 Series 생성
# 학생들의 점수(값)와 이름(인덱스)을 포함하는 Series 's'를 생성합니다.
s = pd.Series([85, 92, 78, 92, 96], index=['Alice', 'Bob', 'Charlie', 'Eve', 'Diana'])
```
`s` Series는 다음과 같습니다:
```
Alice      85
Bob        92
Charlie    78
Eve        92
Diana      96
dtype: int64
```

1.  **Vector scan: who scored 92? (특정 값을 가진 인덱스 찾기)**
    ```python
    who = s.index[s.eq(92)].tolist()
    # 결과: ['Bob', 'Eve']
    ```
    *   `s.eq(92)`: Series `s`의 각 요소가 92와 같은지 비교하여 불리언 Series를 반환합니다. (예: `[False, True, False, True, False]`)
    *   `s.index[...]`: 이 불리언 Series를 사용하여 `s`의 인덱스에서 `True`에 해당하는 인덱스(이름)만 추출합니다.
    *   `.tolist()`: 추출된 인덱스 컬렉션을 Python 리스트로 변환합니다.

2.  **Label of max / min (최댓값/최솟값의 인덱스 찾기)**
    ```python
    top, low = s.idxxmax(), s.idxxmin()
    # 결과: ('Diana', 'Charlie')
    ```
    *   `s.idxxmax()`: Series `s`에서 최댓값을 가지는 인덱스(label)를 반환합니다. (96점의 Diana)
    *   `s.idxxmin()`: Series `s`에서 최솟값을 가지는 인덱스(label)를 반환합니다. (78점의 Charlie)

3.  **Reverse map (one-to-one only!) (값으로 인덱스를 역매핑 - 단일 값 대응)**
    ```python
    rev = pd.Series(s.index, index=s.values)
    rev.loc[96]
    # 결과: 'Diana'
    ```
    *   `pd.Series(s.index, index=s.values)`: `s`의 인덱스(`s.index`)를 새로운 Series의 값으로, `s`의 값(`s.values`)을 새로운 Series의 인덱스로 사용하여 `rev` Series를 생성합니다.
    *   `rev.loc[96]`: `rev` Series에서 인덱스 96에 해당하는 값을 찾습니다. 이는 원본 `s`에서 96점을 받은 학생의 이름을 찾는 것과 같습니다.
    *   **주의**: 이 방법은 원본 `s`의 값들이 고유할 때만 정확하게 작동합니다. 만약 중복된 값이 있다면, 나중에 생성된 값으로 인덱스가 덮어쓰여질 수 있습니다.

    **For duplicates -> list map: (중복 값을 포함하는 역매핑 처리)**
    ```python
    rev_multi = s.reset_index().groupby(0)['index'].apply(list)
    rev_multi.loc[92]
    # 결과: ['Bob', 'Eve']
    ```
    *   `s.reset_index()`: `s` Series를 DataFrame으로 변환합니다. 기존 인덱스('Alice', 'Bob' 등)는 'index'라는 새로운 컬럼이 되고, 기존 값(85, 92 등)은 숫자 인덱스(0, 1, 2, ...)를 가진 '0'이라는 컬럼이 됩니다.
        ```
           index   0
        0  Alice  85
        1    Bob  92
        2  Charlie  78
        3    Eve  92
        4  Diana  96
        ```
    *   `.groupby(0)`: 이 DataFrame을 '0' 컬럼(원본 Series의 값)을 기준으로 그룹화합니다.
    *   `['index']`: 각 그룹에서 'index' 컬럼(원본 Series의 인덱스)을 선택합니다.
    *   `.apply(list)`: 선택된 'index' 컬럼의 값들을 리스트로 묶어 각 그룹에 적용합니다. 이렇게 하면 중복된 값(예: 92)에 해당하는 모든 원본 인덱스(예: 'Bob', 'Eve')를 리스트로 얻을 수 있습니다.
    *   `rev_multi.loc[92]`: 결과 `rev_multi` Series에서 인덱스 92에 해당하는 리스트를 찾습니다.

4.  **Position(s) of a value (값의 물리적 위치(인덱스) 찾기)**
    ```python
    pos = np.flatnonzero(s.to_numpy() == 92)
    # 결과: array([1, 3])
    ```
    *   `s.to_numpy()`: `s` Series의 값들을 NumPy 배열로 변환합니다. (예: `array([85, 92, 78, 92, 96])`)
    *   `s.to_numpy() == 92`: 이 NumPy 배열에서 각 요소가 92와 같은지 비교하여 불리언 배열을 생성합니다. (예: `array([False, True, False, True, False])`)
    *   `np.flatnonzero(...)`: 이 불리언 배열에서 `True`인 요소들의 0-기반 인덱스(위치)를 반환합니다. `Bob`은 1번째 위치, `Eve`는 3번째 위치에 해당합니다.

### **구체적 예시**

어떤 교수님이 학생들의 중간고사 성적(`s`)을 관리하고 있다고 가정해 봅시다.

1.  **Vector scan**: "92점을 받은 학생이 누구였지?"라고 물을 때, `s.index[s.eq(92)].tolist()`를 사용하여 'Bob'과 'Eve'라는 답을 얻을 수 있습니다.
2.  **Label of max / min**: "이번 시험에서 최고점과 최저점을 받은 학생은?"이라는 질문에 `s.idxxmax()`와 `s.idxxmin()`으로 'Diana'와 'Charlie'를 바로 찾아낼 수 있습니다.
3.  **Reverse map**:
    *   "96점은 누가 받았더라?" (단일 값일 때): `rev.loc[96]`으로 'Diana'를 찾습니다.
    *   "92점을 받은 학생은 누가 있었지?" (중복 값일 때): `rev_multi.loc[92]`를 사용해 'Bob'과 'Eve' 모두를 정확하게 확인할 수 있습니다.
4.  **Position(s) of a value**: 데이터 배열에서 "92점이라는 값이 몇 번째 위치에 나타나는가?"를 알고 싶을 때 `np.flatnonzero(s.to_numpy() == 92)`를 사용하여 1번, 3번 위치라는 결과를 얻습니다. (이는 내부적인 데이터 저장 순서를 의미할 수 있습니다.)

### **시험 포인트**

*   ⭐ `pandas.Series`에서 **불리언 인덱싱**(`s[condition]`)은 특정 조건을 만족하는 데이터를 효율적으로 필터링하는 강력한 방법임을 이해해야 합니다. 특히 `s.eq(value)`와 같은 메서드와 함께 사용됩니다.
*   ⭐ `idxxmax()`와 `idxxmin()`은 최댓값/최솟값 **자체**가 아니라 그 값에 해당하는 **인덱스(label)**를 반환한다는 점을 기억하세요.
*   ⭐ 중복된 값이 있는 경우, 단순히 `pd.Series(values, index=labels)` 형태의 역매핑은 문제를 일으킬 수 있습니다. 중복 값을 모두 처리하려면 `reset_index().groupby().apply(list)`와 같은 패턴을 활용해야 한다는 것을 ⭐**매우 중요하게**⭐ 알아두어야 합니다. 이는 실제 데이터 분석에서 흔히 발생하는 시나리오입니다.
*   ⭐ NumPy의 `np.flatnonzero()` 함수는 불리언 배열에서 `True` 값의 **0-기반 위치(인덱스)**를 찾는 데 사용됩니다. Series의 값을 NumPy 배열로 변환(`to_numpy()`)하여 활용하는 방법을 이해해야 합니다.

---

## Slide 18

### 핵심 개념

데이터 분석에서 결측값(Missing Values)은 중요한 이슈입니다. Pandas는 결측값을 표현하고 다루기 위한 여러 방법을 제공합니다. 전통적인 NumPy 기반의 `np.nan` 외에, Pandas 1.0부터는 `pd.NA`라는 새로운 결측값 표기자를 도입하여 다양한 데이터 타입에서 결측값을 보다 일관성 있게 처리할 수 있게 되었습니다.

*   **결측값 표기자**:
    *   `np.nan`: NumPy의 float NaN (Not a Number)입니다. 주로 실수형 데이터의 결측값을 나타내며, 정수형 데이터에 `np.nan`이 포함되면 해당 Series는 자동으로 float 타입으로 **업캐스팅(upcasting)**됩니다.
    *   `pd.NA`: Pandas의 NA-aware 데이터 타입(`Int64`, `Float64`, `boolean`, `string`)에서 결측값을 표현하는 스칼라입니다. 이는 특정 데이터 타입의 본래 형식을 유지하면서 결측값을 처리할 수 있도록 돕습니다 (Three-valued logic).
*   **NA-aware dtypes**: Pandas는 `Int64`, `Float64`, `boolean`, `string`과 같은 NA-aware 데이터 타입을 제공하여 `pd.NA`를 통해 결측값이 포함되어도 해당 타입의 본래 형식을 유지합니다. 이는 정수형 데이터가 결측값 때문에 실수형으로 변환되는 것을 방지합니다.
*   **결측값 탐지 및 계산**: `isna()` 메서드는 Series 내의 각 요소가 결측값인지 여부를 나타내는 boolean Series를 반환합니다. `sum()` 메서드를 함께 사용하여 결측값의 총 개수를 쉽게 계산할 수 있습니다.

### 코드/수식 해설

슬라이드에 제시된 코드 예시들을 통해 결측값 처리의 특성을 이해합니다.

1.  **기본 Series 생성 및 dtype 변환**:
    `pd.Series`에 `None`을 포함시키면, 기본적으로 `np.nan`으로 처리되며, 해당 Series의 `dtype`은 `float64`로 업캐스팅됩니다.
    ```python
    import pandas as pd
    import numpy as np

    s1 = pd.Series([1., None, 3.])
    print(s1)
    print(s1.dtype)
    ```
    출력:
    ```
    0    1.0
    1    NaN
    2    3.0
    dtype: float64
    ```

2.  **NA-aware dtype을 사용한 Series 생성**:
    `dtype='Int64'`를 명시적으로 지정하면, 정수형 데이터를 유지하면서 `None`은 `pd.NA`로 처리됩니다.
    ```python
    s2 = pd.Series([1, None, 3], dtype='Int64')
    print(s2)
    print(s2.dtype)
    ```
    출력:
    ```
    0       1
    1    <NA>
    2       3
    dtype: Int64
    ```

3.  **문자열 Series에서 결측값 처리**:
    문자열 Series에 `None`이 포함되면, `dtype`은 `object`가 되며 `None`은 그대로 `None`으로 유지될 수 있습니다. (Pandas 1.0+ 버전의 `string` dtype을 사용하면 `pd.NA`로 처리됩니다.)
    ```python
    s3 = pd.Series(['a', None, 'b'])
    print(s3)
    print(s3.dtype)
    ```
    출력:
    ```
    0       a
    1    None
    2       b
    dtype: object
    ```

4.  **결측값 탐지 및 개수 계산**:
    `isna()` 메서드는 각 원소가 결측값인지 여부를 나타내는 boolean Series를 반환합니다. `sum()` 메서드를 이 boolean Series에 적용하면 `True` (1)의 개수를 세어 결측값의 총 개수를 얻을 수 있습니다.
    ```python
    print(s2.isna())
    print(s2.isna().sum())
    ```
    출력:
    ```
    0    False
    1     True
    2    False
    dtype: boolean
    1
    ```
    *   `s.isna()`: Series `s`의 각 원소가 결측값인지(`True`) 아닌지(`False`)를 알려주는 boolean Series를 반환합니다. `pd.isna(s)`와 `s.isnull()`도 동일한 역할을 합니다.
    *   `s.notna()`: 결측값이 아닌 원소를 찾아주는 메서드이며, `s.notnull()`과 동일합니다.
    *   `s.count()`: 결측값을 제외한 유효한(non-missing) 데이터의 개수를 반환합니다.

### 구체적 예시

설문조사 데이터를 예시로 들어봅시다. 학생들의 점수(정수형)와 특정 과목 수강 여부(부울형)를 기록하는데, 일부 학생은 답변하지 않았을 수 있습니다.

**예시 시나리오**: 10명의 학생이 있고, 수학 점수와 프로그래밍 과목 수강 여부를 조사했습니다. 몇몇 학생은 점수를 제출하지 않았고, 몇몇은 수강 여부에 답변하지 않았습니다.

```python
import pandas as pd
import numpy as np

# 학생들의 수학 점수 (정수형, 결측값 포함)
math_scores = pd.Series([85, 92, None, 78, 65, None, 90, None, 75, 88], dtype='Int64')
print("수학 점수 Series:")
print(math_scores)
print(f"수학 점수 dtype: {math_scores.dtype}")
print(f"수학 점수 결측값 개수: {math_scores.isna().sum()}") # pd.NA 처리
print(f"유효한 수학 점수 개수: {math_scores.count()}\n")

# 프로그래밍 과목 수강 여부 (부울형, 결측값 포함)
programming_taken = pd.Series([True, False, True, None, False, True, False, None, True, False], dtype='boolean')
print("프로그래밍 수강 여부 Series:")
print(programming_taken)
print(f"프로그래밍 수강 여부 dtype: {programming_taken.dtype}")
print(f"프로그래밍 수강 여부 결측값 개수: {programming_taken.isna().sum()}") # pd.NA 처리
print(f"유효한 프로그래밍 수강 여부 개수: {programming_taken.count()}\n")

# 실수형 데이터의 결측값 (np.nan)
heights = pd.Series([170.5, 180.2, 165.0, np.nan, 175.8])
print("학생 키 Series (np.nan 포함):")
print(heights)
print(f"학생 키 dtype: {heights.dtype}") # float64
print(f"학생 키 결측값 개수: {heights.isna().sum()}\n")
```

이 예시에서 `Int64`와 `boolean` dtype을 사용하여 정수형 및 부울형 데이터를 결측값(`pd.NA`)과 함께 원래의 형태로 유지하는 것을 볼 수 있습니다. `heights` 예시에서는 `np.nan`이 사용되었고, 이에 따라 `dtype`이 `float64`로 유지됩니다. 각 Series에서 `isna().sum()`을 통해 결측값의 개수를 정확히 파악할 수 있습니다.

### 시험 포인트

*   ⭐ **`np.nan`과 `pd.NA`의 차이점**:
    *   `np.nan`은 float 타입에만 사용되며, 정수형 Series에 포함되면 Series를 `float64`로 업캐스팅시킵니다.
    *   `pd.NA`는 `Int64`, `Float64`, `boolean`, `string`과 같은 NA-aware dtype과 함께 사용되어 해당 데이터 타입의 본래 형식을 유지하면서 결측값을 표현합니다.
*   ⭐ **NA-aware dtypes의 중요성**: `dtype='Int64'` 또는 `'boolean'`과 같이 명시적으로 NA-aware dtypes를 지정하면, 결측값으로 인해 의도치 않게 `float64`로 업캐스팅되는 것을 방지하고 데이터의 의미론적 정확성을 유지할 수 있습니다.
*   ⭐ **결측값 탐지 메서드**: `s.isna()`와 `s.notna()`의 사용법과 반환 값(boolean Series)을 이해해야 합니다.
*   ⭐ **결측값 개수 계산**: `s.isna().sum()`을 이용하여 Series 내의 결측값 개수를 효율적으로 계산하는 방법을 알아야 합니다. `s.count()`는 결측값을 제외한 유효한 값의 개수를 반환합니다.
*   ⭐ **데이터 타입 유의**: `pd.Series`를 생성할 때 `None`을 포함하는 경우, 기본 `dtype` 추론 방식이 어떻게 작동하는지(예: `int`와 `None`이 섞이면 `float64`로 업캐스팅) 이해하고, 이를 피하기 위해 `dtype`을 명시적으로 지정하는 방법을 알아야 합니다.

---

## Slide 19

### 핵심 개념

*   **결측치 (Missing Values)**: 데이터에 값이 존재하지 않을 때 사용되는 특별한 값입니다. pandas에서는 주로 NumPy의 `np.nan` (Not a Number)과 pandas 고유의 `pd.NA` (Not Applicable)를 사용합니다.
*   **`isna()` / `notna()` 메서드**: pandas Series 또는 DataFrame의 각 원소가 결측치(missing value)인지 여부를 True/False로 반환하는 불리언(Boolean) 객체를 생성합니다. `isna()`는 결측치이면 `True`, 아니면 `False`를 반환하며, `notna()`는 그 반대입니다.
*   **데이터 타입 (Data Types, `dtypes`)**: pandas 객체(Series, DataFrame)의 각 원소나 컬럼이 어떤 종류의 데이터를 저장하는지를 명시합니다.
    *   **Upcasting (자동 형 변환)**: NumPy의 `np.nan`은 부동 소수점(float) 타입입니다. 따라서, 정수(integer)로 구성된 pandas Series에 `np.nan`이 하나라도 포함되면, Series 전체의 `dtype`이 `float64`와 같은 부동 소수점 타입으로 자동 변환(Upcasting)됩니다. 이는 정수와 `np.nan`을 동시에 표현하기 위함입니다.
    *   **NA-aware dtypes (결측치를 인식하는 데이터 타입)**: pandas 1.0부터 도입된 새로운 데이터 타입으로, `Int64`, `Float64`, `Boolean` 등이 있습니다. 이 타입들은 `np.nan` 대신 `pd.NA`를 사용하여 결측치를 표현하며, 정수형 데이터에 결측치가 포함되더라도 `Int64`와 같이 원래의 정수 타입을 유지할 수 있도록 합니다. 이는 불필요한 `float` 타입으로의 변환을 방지하여 데이터 타입의 일관성을 유지하는 데 유용합니다.
*   **DataFrame 결측치 분석**: `DataFrame.isna()`는 DataFrame 전체의 결측치 맵을 불리언 DataFrame 형태로 반환합니다. 여기에 `sum()`을 연쇄적으로 적용하면 각 컬럼별 결측치 개수를 손쉽게 파악할 수 있습니다. `notna().all()`은 각 컬럼의 모든 값이 결측치가 아닌지(즉, 해당 컬럼에 결측치가 하나도 없는지) 확인합니다.

### 코드/수식 해설

```python
import numpy as np, pandas as pd

# Upcasting with NumPy NaN
s = pd.Series([1, 2, np.nan, 4])
# 정수형 데이터를 가진 Series에 np.nan이 포함됩니다.
s.dtype
# 출력: dtype('float64')
# np.nan으로 인해 Series의 dtype이 int64에서 float64로 Upcasting 됩니다.

s.isna()
# 출력:
# 0    False
# 1    False
# 2     True
# 3    False
# dtype: bool
# Series 's'의 각 원소가 결측치(np.nan)인지 여부를 불리언 Series로 반환합니다.
# 인덱스 2번의 np.nan은 True로 표시됩니다.

# NA-aware integer dtype keeps integers + NA
t = pd.Series([1, pd.NA, 3], dtype="Int64")
# NA-aware integer dtype "Int64"를 명시적으로 사용하여 Series를 생성합니다.
# pd.NA를 사용하여 결측치를 표현합니다.
t, t.dtype
# 출력:
# 0       1
# 1    <NA>
# 2       3
# dtype: Int64
# Series 't'는 정수형 값과 pd.NA를 포함하면서도 dtype이 Int64를 유지합니다.
# <NA>는 pd.NA의 문자열 표현입니다.

# DataFrame-wide missing map and counts
df = pd.DataFrame({"a":[1, pd.NA, 3], "b":[np.nan, 2.0, 3.0]})
# 두 컬럼 'a', 'b'를 가지는 DataFrame을 생성합니다.
# 'a' 컬럼은 pd.NA를, 'b' 컬럼은 np.nan을 결측치로 가집니다.

df.isna()
# 출력:
#        a      b
# 0  False   True
# 1   True  False
# 2  False  False
# DataFrame 'df' 전체의 각 원소가 결측치인지 여부를 불리언 DataFrame으로 반환합니다.

df.isna().sum()
# # per column
# 출력:
# a    1
# b    1
# dtype: int64
# df.isna()의 결과인 불리언 DataFrame에서 True(결측치)의 개수를 컬럼별로 합산합니다.
# 'a' 컬럼에 1개, 'b' 컬럼에 1개의 결측치가 있음을 보여줍니다.

df.notna().all()
# # no missing in a column?
# 출력:
# a    False
# b    False
# dtype: bool
# df.notna()는 결측치가 아닌 원소를 True로 표시합니다. 여기에 .all()을 적용하면
# 각 컬럼의 모든 원소가 결측치가 아닌지 (즉, 해당 컬럼에 결측치가 하나도 없는지) 확인합니다.
# 'a'와 'b' 컬럼 모두 결측치가 있으므로 둘 다 False를 반환합니다.
```

### 구체적 예시

1.  **`np.nan`과 `float64` Upcasting**:
    당신이 친구들의 시험 점수(정수)를 Series로 관리하고 있다고 가정해 봅시다.
    `scores = pd.Series([90, 85, 78, 100])`
    만약 한 친구가 시험을 보지 않아 점수가 비어있어 `np.nan`을 추가한다면:
    `scores_with_nan = pd.Series([90, 85, np.nan, 100])`
    이 Series의 `dtype`은 `float64`가 됩니다. 원래는 정수형이었던 90, 85, 100도 내부적으로는 90.0, 85.0, 100.0처럼 부동 소수점으로 저장됩니다. 이는 모든 요소를 `np.nan`과 호환되게 만들기 위한 pandas의 자동 형 변환 동작입니다.

2.  **`pd.NA`와 `Int64` (NA-aware dtype)**:
    이번에는 친구들의 나이(정수)를 관리하는데, `np.nan`으로 인해 `float`으로 바뀌는 것을 원치 않는다고 가정해 봅시다.
    `ages = pd.Series([23, pd.NA, 25, 22], dtype="Int64")`
    이렇게 `dtype="Int64"`를 명시하고 `pd.NA`를 사용하면, Series는 `23, <NA>, 25, 22`와 같이 정수 타입을 유지하면서 결측치를 표현할 수 있습니다. 이는 데이터의 의미를 더 명확하게 유지하고, 불필요한 소수점 연산을 방지하는 데 도움을 줍니다.

### 시험 포인트

*   ⭐ **`np.nan`과 `pd.NA`의 차이점**: `np.nan`은 `float` 타입이며, `int` Series에 포함되면 `float`으로 Upcasting을 유발합니다. `pd.NA`는 pandas 전용 결측치 값으로, `Int64`, `BooleanDtype` 등 NA-aware dtypes와 함께 사용될 때 원래의 데이터 타입을 유지할 수 있게 합니다.
*   ⭐ **`np.nan`을 포함한 `Series`의 `dtype` 변화 (Upcasting)**: 왜 정수형 Series에 `np.nan`이 들어가면 `float64`가 되는지 그 이유를 설명할 수 있어야 합니다.
*   ⭐ **NA-aware `dtypes` (예: `Int64`)의 필요성 및 사용법**: 기존 `np.nan`의 한계를 극복하고 데이터 타입의 일관성을 유지하는 NA-aware dtypes의 개념과 `dtype="Int64"`와 같이 명시하여 사용하는 방법을 이해해야 합니다.
*   ⭐ **`isna()` 및 `notna()` 메서드의 활용**: Series와 DataFrame에서 결측치를 식별하는 기본적인 방법입니다. 특히 `df.isna().sum()`을 통해 컬럼별 결측치 개수를 파악하는 방법은 데이터 전처리 과정에서 매우 중요합니다.
*   ⭐ `all()` 메서드: `df.notna().all()`처럼 사용될 때, 특정 축(기본값은 컬럼)의 모든 원소가 조건을 만족하는지(즉, 모든 값이 결측치가 아닌지) 확인하는 방법을 이해해야 합니다.

---

## Slide 20

**핵심 개념**:
*   **결측값 처리 방법 (Filling and Interpolation)**: pandas에서 `NaN` (Not a Number)으로 표현되는 결측값을 단순히 제거하는 대신, 의미 있는 값으로 채워 넣는 방법들을 다룹니다. 크게 직접 값으로 채우는 `fillna`와 주변 데이터를 기반으로 추정하는 `interpolate`로 나눌 수 있습니다.
*   **`fillna()`**: 특정 상수, 통계량(평균, 중앙값 등), 또는 이전에 관측된 값(forward fill), 이후에 관측된 값(backward fill) 등으로 결측값을 직접 대체하는 함수입니다.
*   **`ffill()` / `bfill()`**: `fillna()`의 특수한 경우로, `ffill()`은 바로 이전의 유효한 값으로 결측값을 채우고, `bfill()`은 바로 이후의 유효한 값으로 결측값을 채웁니다. 주로 시계열 데이터와 같이 순서에 의미가 있는 경우에 사용됩니다.
*   **`interpolate()`**: 주변의 유효한 데이터 포인트를 기반으로 결측값을 추정하여 채우는 함수입니다. 선형 보간(linear interpolation)이 가장 일반적이며, 데이터의 추세를 반영하여 값을 예측할 때 유용합니다.

**코드/수식 해설**:
*   **`s.fillna(value)`**:
    `Series` 또는 `DataFrame`의 결측값을 지정된 `value`로 채웁니다.
    ```python
    import pandas as pd
    import numpy as np

    s = pd.Series([1., np.nan, 2., 3., np.nan])
    s_filled_zero = s.fillna(0)
    print(s_filled_zero)
    # 0    1.0
    # 1    0.0
    # 2    2.0
    # 3    3.0
    # 4    0.0
    # dtype: float64
    ```
    `DataFrame`의 경우 `df.fillna({'col1': val1, 'col2': val2})`와 같이 각 컬럼에 다른 값을 지정하여 채울 수 있습니다. `method='ffill'` 또는 `method='bfill'` 인자를 사용하면 `ffill()`/`bfill()`과 동일하게 동작하며, `limit` 인자를 통해 연속적으로 채울 결측값의 개수를 제한할 수 있습니다.

*   **`s.ffill()` / `s.bfill()`**:
    `ffill()` (forward fill)은 이전 유효값으로 결측값을 채웁니다. `bfill()` (backward fill)은 이후 유효값으로 결측값을 채웁니다.
    ```python
    s = pd.Series([1., np.nan, 2., 3., np.nan])

    s_ffill = s.ffill()
    print("Forward fill:\n", s_ffill)
    # Forward fill:
    # 0    1.0
    # 1    1.0
    # 2    2.0
    # 3    3.0
    # 4    3.0
    # dtype: float64

    s_bfill = s.bfill()
    print("Backward fill:\n", s_bfill)
    # Backward fill:
    # 0    1.0
    # 1    2.0
    # 2    2.0
    # 3    3.0
    # 4    NaN  # 다음 유효한 값이 없으므로 마지막 NaN은 채워지지 않음
    # dtype: float64
    ```

*   **`s.interpolate(method='linear')`**:
    주변 데이터 포인트의 선형 관계를 이용하여 결측값을 추정합니다.
    ```python
    s = pd.Series([1., np.nan, 2., 3., np.nan])

    s_interpolated = s.interpolate(method='linear')
    print("Interpolated (linear):\n", s_interpolated)
    # Interpolated (linear):
    # 0    1.0
    # 1    1.5  # (1.0 + 2.0) / 2
    # 2    2.0
    # 3    3.0
    # 4    NaN  # 기본적으로 외삽(extrapolation)은 하지 않으므로 마지막 NaN은 남음
    # dtype: float64
    ```
    선형 보간 수식: 두 점 $(x_1, y_1)$과 $(x_2, y_2)$ 사이의 점 $(x, y)$에 대해
    $$ y = y_1 + (x - x_1) \frac{y_2 - y_1}{x_2 - x_1} $$
    `method` 인자로는 `'linear'` 외에도 `'index'`, `'time'`, `'polynomial'` 등 다양한 보간법을 지정할 수 있습니다. `'index'`나 `'time'`을 사용하려면 인덱스가 단조 증가(monotonic)해야 합니다. `limit_direction` 파라미터를 사용하면 보간 방향(forward, backward, both)과 외삽(extrapolation) 여부를 제어할 수 있습니다. (슬라이드 예시에서 마지막 `NaN`이 `3.0`으로 채워진 것은 `limit_direction='both'` 등의 특정 설정 또는 보간 후 `ffill()`이 적용된 결과일 수 있습니다.)

**구체적 예시**:
주식 시장 데이터에서 가격 변동이 있을 때, 장중에 잠깐 데이터가 누락될 수 있습니다.
```python
import pandas as pd
import numpy as np

# 주식 종가 데이터 (일부 결측)
stock_prices = pd.Series([100, 102, np.nan, 105, np.nan, np.nan, 110, 112])
print("Original Stock Prices:\n", stock_prices)

# 1. 특정 값으로 채우기 (예: 결측치를 0으로) - 권장되지 않음 (데이터 의미 왜곡)
# 그러나 결측치임을 명확히 나타내는 -1 등 특정 Sentinel Value로 채울 수는 있습니다.
filled_with_zero = stock_prices.fillna(0)
# print("\nFilled with 0:\n", filled_with_zero)

# 2. 이전 값으로 채우기 (ffill) - 가장 최근에 관측된 가격으로 채움 (시세 유지)
# 주식 시장이 열려있지 않아 가격 변동이 없는 기간의 데이터 결측에 적합
filled_ffill = stock_prices.ffill()
print("\nForward Filled Prices (ffill):\n", filled_ffill)
# 2: 102 (이전 102)
# 4: 105 (이전 105)
# 5: 105 (이전 105)

# 3. 보간법으로 채우기 (interpolate) - 가격 추세를 반영하여 추정
# 시장이 활발히 움직이는 도중 발생한 단기적인 결측치에 대해, 추세에 따른 합리적인 추정치 제공
interpolated_prices = stock_prices.interpolate(method='linear')
print("\nInterpolated Prices (linear):\n", interpolated_prices)
# 2: 103.5  (102와 105의 중간)
# 4: 106.66 (105와 110 사이의 첫 번째 결측, 두 칸 중 첫 칸)
# 5: 108.33 (105와 110 사이의 두 번째 결측, 두 칸 중 두 번째 칸)
```
주식 가격 데이터에서는 `ffill()`이 가장 보편적으로 사용되며, `interpolate()`는 가격 변동의 추세를 좀 더 부드럽게 반영하고 싶을 때 고려해볼 수 있습니다.

**시험 포인트**:
*   ⭐ **`fillna()`, `ffill()`, `bfill()`, `interpolate()`** 각 함수의 기본적인 사용법과 그들이 결측값을 처리하는 방식의 차이를 정확히 이해해야 합니다.
*   ⭐ **각 방법의 적절한 사용 시나리오**: 주어진 데이터의 특성(상수 대체, 이전/이후 값 전파, 추세 기반 추정)에 따라 어떤 함수를 사용해야 하는지 구분할 수 있어야 합니다.
    *   특정 상수/센티넬 값으로 대체: `s.fillna(value)`
    *   이전 유효값으로 채우기 (forward fill): `s.ffill()` 또는 `s.fillna(method='ffill')`
    *   이후 유효값으로 채우기 (backward fill): `s.bfill()` 또는 `s.fillna(method='bfill')`
    *   주변 데이터의 추세를 고려하여 추정: `s.interpolate(method='linear')`
*   ⭐ `interpolate()`는 값을 **추정**하는 방식이므로, 단순 대체인 `fillna`와는 본질적인 차이가 있음을 인지해야 합니다. `method` (linear, index, time 등) 및 `limit_direction` 파라미터의 의미를 알아두는 것이 좋습니다. 특히 `'index'`나 `'time'` method 사용 시 인덱스가 단조 증가(monotonic)해야 한다는 조건도 중요합니다.
*   `limit` 인자를 사용하여 연속된 결측치 중 몇 개까지 채울지 제한할 수 있다는 점도 기억해두세요.

---

## Slide 21

### 핵심 개념

데이터 분석에서 결측치(Missing Values, `NaN`)는 흔하게 발생하며, 이를 적절히 처리하는 것은 데이터 품질과 분석 결과의 신뢰성에 큰 영향을 미칩니다. `pandas` 라이브러리는 결측치를 효과적으로 다루기 위한 다양한 메서드를 제공합니다.

*   **`fillna()`**: `NaN` 값을 특정 값(스칼라), 특정 메서드(예: `ffill`, `bfill`), 또는 각 컬럼에 대해 다른 값을 사용하여 채울 수 있는 범용적인 메서드입니다.
*   **`ffill()` (Forward Fill)**: 이전에 관측된 유효한 값을 사용하여 `NaN`을 채웁니다. 주로 시계열 데이터에서 이전 시점의 값을 그대로 유지해야 할 때 유용합니다.
*   **`bfill()` (Backward Fill)**: 이후에 관측될 유효한 값을 사용하여 `NaN`을 채웁니다. `ffill()`과 유사하지만, 미래의 값을 사용하여 현재의 결측치를 채우는 방식입니다.
*   **`interpolate()`**: `NaN` 값을 주변 값들로부터 추정하여 채우는 메서드입니다. 단순히 값을 복사하는 `ffill`/`bfill`과 달리, 수학적인 방법을 통해 더 부드러운 값으로 보간할 수 있습니다. 특히 `DatetimeIndex`와 함께 `method='time'`을 사용하면 시간 간격을 고려한 선형 보간을 수행합니다.

### 코드/수식 해설

```python
import pandas as pd
import numpy as np

# 1. 초기 Series 생성
s = pd.Series([1.0, np.nan, np.nan, 4.0, np.nan])
# 결과: Series([1.0, nan, nan, 4.0, nan])

# 2. fillna(scalar)
# 모든 NaN 값을 0으로 채웁니다.
s_filled_0 = s.fillna(0)
# 결과: Series([1.0, 0.0, 0.0, 4.0, 0.0])

# 3. ffill() (Forward Fill)
# 이전에 관측된 유효한 값으로 NaN을 채웁니다.
# 첫 번째 NaN은 1.0으로 채워지고, 두 번째 NaN도 1.0으로 채워집니다.
# 마지막 NaN은 4.0으로 채워집니다.
s_ffilled = s.ffill()
# 결과: Series([1.0, 1.0, 1.0, 4.0, 4.0])

# 4. bfill(limit=1) (Backward Fill with limit)
# 이후에 관측된 유효한 값으로 NaN을 채웁니다. limit=1은 최대 1개의 NaN만 채우도록 제한합니다.
# 첫 번째 NaN은 다음 유효값인 4.0으로 채워집니다. limit=1이므로 첫 번째 NaN만 채워집니다.
# 두 번째 NaN은 채워지지 않습니다 (앞서 첫 번째 NaN이 4.0으로 채워졌지만,
# 원본에서 다음 유효값인 4.0까지 두 칸이므로 limit=1에 의해 두 번째 NaN은 채워지지 않음).
# 마지막 NaN은 이후 유효값이 없으므로 채워지지 않습니다.
s_bfilled_limit1 = s.bfill(limit=1)
# 결과: Series([1.0, 4.0, nan, 4.0, nan])
# 주석에 따르면 "only first gap filled due to limit=1"
# 이 예시에서는 1.0 다음의 첫 번째 np.nan이 4.0으로 채워지고, 두 번째 np.nan은 그 뒤 4.0까지 두 칸 떨어져 있으므로 limit=1에 의해 채워지지 않습니다.

# 5. Time-aware interpolation
# 날짜 인덱스를 가진 Series를 생성합니다.
idx = pd.date_range("2024-01-01", periods=5, freq="D")
t = pd.Series([1.0, np.nan, 4.0, np.nan, 9.0], index=idx)
# 결과:
# 2024-01-01    1.0
# 2024-01-02    NaN
# 2024-01-03    4.0
# 2024-01-04    NaN
# 2024-01-05    9.0
# Dtype: float64

# method="time"을 사용하여 시간 간격을 고려한 선형 보간을 수행합니다.
# 2024-01-02의 NaN은 (2024-01-01, 1.0)과 (2024-01-03, 4.0) 사이를 선형 보간하여 (1.0 + 4.0) / 2 = 2.5가 됩니다.
# 2024-01-04의 NaN은 (2024-01-03, 4.0)과 (2024-01-05, 9.0) 사이를 선형 보간하여 (4.0 + 9.0) / 2 = 6.5가 됩니다.
t_interpolated_time = t.interpolate(method="time")
# 결과:
# 2024-01-01    1.0
# 2024-01-02    2.5
# 2024-01-03    4.0
# 2024-01-04    6.5
# 2024-01-05    9.0
# Dtype: float64

# 선형 보간 수식 (두 점 (x1, y1)과 (x2, y2) 사이의 x 값에 대한 y 값):
# y = y1 + (x - x1) * ((y2 - y1) / (x2 - x1))
# method="time"의 경우 x는 시간 값, y는 데이터 값입니다.
# 예를 들어, t[2024-01-02]의 경우:
# x1 = 2024-01-01, y1 = 1.0
# x2 = 2024-01-03, y2 = 4.0
# x = 2024-01-02
# 일 단위로 간격이 동일하므로, (x - x1) / (x2 - x1) = 1/2
# 따라서, y = 1.0 + (1/2) * (4.0 - 1.0) = 1.0 + 1.5 = 2.5

# 6. Per-column fills with a dict (DataFrame에서 컬럼별 fillna)
# DataFrame을 생성합니다.
df = pd.DataFrame({"a": [1, np.nan, 3], "b": [np.nan, 2.5, np.nan]})
# 결과:
#      a    b
# 0  1.0  NaN
# 1  NaN  2.5
# 2  3.0  NaN

# 'a' 컬럼의 NaN은 0으로, 'b' 컬럼의 NaN은 'b' 컬럼의 평균값으로 채웁니다.
df_filled = df.fillna({"a": 0, "b": df["b"].mean()})
# 'b' 컬럼의 평균은 (2.5) / 1 = 2.5 입니다. (NaN은 평균 계산 시 무시됨)
# 결과:
#      a    b
# 0  1.0  2.5  ('b' 컬럼의 NaN이 2.5로 채워짐)
# 1  0.0  2.5  ('a' 컬럼의 NaN이 0으로 채워짐)
# 2  3.0  2.5  ('b' 컬럼의 NaN이 2.5로 채워짐)
```

### 구체적 예시

1.  **`fillna(scalar)`**: 어떤 센서가 오작동하여 데이터를 기록하지 못했을 때 (`NaN`), 해당 시간대의 값을 임시로 0으로 채우거나 (측정 안 됨), 직전/직후의 정상 값으로 채울 수 있습니다. `fillna(0)`는 측정값이 없으면 0으로 간주하겠다는 의미가 됩니다.
2.  **`ffill()` / `bfill()`**:
    *   **주가 데이터**: 특정 시점의 주가 데이터가 누락되었을 때, 이전 거래일의 종가를 사용하여 채우는 것은 합리적인 접근이 될 수 있습니다 (ffill).
    *   **재고 관리**: 재고 수량이 기록되지 않았을 때, 마지막으로 알려진 재고 수량으로 채울 수 있습니다 (ffill).
    *   `limit` 파라미터는 "최대 며칠까지 데이터를 복사할 것인가?"와 같은 시나리오에 활용됩니다. 예를 들어, 3일까지는 직전 값을 사용하고, 그 이상이면 여전히 `NaN`으로 남기는 경우.
3.  **`interpolate(method="time")`**:
    *   **기상 관측 데이터**: 시간별 온도 기록에서 특정 시간의 데이터가 누락되었을 때, 이전 시간과 이후 시간의 온도 값을 바탕으로 선형적으로 온도를 추정하는 것이 단순히 직전 값을 복사하는 것보다 더 정확한 예측이 될 수 있습니다. 특히 `method="time"`을 사용하면 실제 시간 간격을 고려하여 보간하므로, 불규칙한 시간 간격의 데이터에서도 유용합니다.
    *   $$ \text{Interpolated Value} = \text{Value}_1 + \frac{\text{Missing Time} - \text{Time}_1}{\text{Time}_2 - \text{Time}_1} \times (\text{Value}_2 - \text{Value}_1) $$
        (여기서 $\text{Time}_1, \text{Value}_1$는 이전 유효 데이터, $\text{Time}_2, \text{Value}_2$는 다음 유효 데이터입니다.)
4.  **컬럼별 `fillna`**:
    *   **고객 설문 데이터**: '나이' 컬럼의 결측치는 평균 나이로 채우고, '성별' 컬럼의 결측치는 '알 수 없음'과 같은 문자열로 채우거나, 가장 많은 비중을 차지하는 성별(최빈값)로 채울 수 있습니다. 이는 각 컬럼의 데이터 특성에 따라 다른 결측치 처리 전략이 필요할 때 유용합니다.

### 시험 포인트

*   ⭐ **`fillna()`, `ffill()`, `bfill()`의 차이점과 사용 시나리오**를 명확히 이해하고 구분할 수 있어야 합니다. `fillna()`는 일반적인 값 채우기, `ffill()`은 이전 값 복사, `bfill()`은 다음 값 복사입니다.
*   ⭐ **`limit` 파라미터**의 역할과 사용법을 숙지해야 합니다. `ffill()` 또는 `bfill()` 시 연속된 `NaN` 중 몇 개까지 채울지 제한할 때 사용됩니다.
*   ⭐ `interpolate()` 메서드, 특히 **`method="time"` 옵션의 중요성**을 이해해야 합니다. `DatetimeIndex`와 함께 사용될 때, 시간 간격을 고려하여 선형적으로 보간한다는 점이 핵심입니다. 이는 단순히 인덱스 위치에 따른 선형 보간보다 더 실제적인 추정값을 제공합니다.
*   ⭐ `DataFrame`에서 **딕셔너리를 사용하여 컬럼별로 다른 `fillna` 전략**을 적용하는 방법을 이해해야 합니다. 이는 다양한 데이터 타입과 특성을 가진 컬럼들이 혼재하는 `DataFrame`에서 매우 유용합니다.
*   ⭐ 모든 결측치 처리 메서드는 기본적으로 **새로운 `Series` 또는 `DataFrame` 객체를 반환**합니다. 원본 객체를 직접 수정하려면 `inplace=True` 파라미터를 사용해야 하지만, 이는 일반적으로 권장되지 않습니다. (슬라이드에는 `inplace`가 없지만, 중요한 pandas 개념이므로 함께 알아두면 좋습니다.)

---

## Slide 22

### 핵심 개념

이 슬라이드는 Pandas에서 누락된 값(Missing Values), 즉 `NaN` (Not a Number)을 포함하는 Series나 DataFrame에 대해 `min()`, `sum()`, `mean()`, `var()`, `std()`와 같은 통계적 집계(reduction) 함수들이 어떻게 동작하는지 설명합니다.

*   **기본 NA-skipping 동작**: 대부분의 Pandas 통계 함수(예: `sum()`, `mean()`, `min()`, `max()`, `var()`, `std()`)는 기본적으로 `NaN` 값을 건너뛰고(skip) 계산합니다. 이는 해당 함수들이 `skipna=True` 인자를 기본값으로 사용하기 때문입니다.
*   **`skipna` 인자를 통한 제어**: `skipna=False`로 설정하면, 데이터에 `NaN`이 하나라도 있을 경우 해당 집계 결과도 `NaN`이 됩니다. 이는 "완전한 데이터"를 요구하는 엄격한 계산에 사용됩니다.
*   **특정 함수의 `NaN` 처리 예외**:
    *   모든 값이 `NaN`인 Series에 대해 `mean()`은 `NaN`을 반환하지만, `sum()`은 `0`을 반환합니다 (숫자형 데이터의 경우).
    *   `count()` 함수는 `NaN`이 아닌(non-missing) 요소의 개수만 셉니다.
*   **누락된 값의 개수 세기**: `s.isna().sum()`을 사용하여 Series 내의 `NaN` 값의 총 개수를 정확하게 셀 수 있습니다.
*   **고유값(Unique Values) 처리**: `s.nunique()` 함수는 기본적으로 `NaN`을 고유값 계산에서 제외합니다(`dropna=True`). `dropna=False`로 설정하면 `NaN`도 하나의 고유값으로 포함됩니다.
*   **Boolean 집계 함수**: `s.any()` (하나라도 True면 True)와 `s.all()` (모두 True여야 True) 같은 불리언 집계 함수들도 기본적으로 `skipna=True`를 사용하여 `NaN`을 무시합니다. `skipna=False`로 설정하면 `NaN`의 존재가 결과에 `NaN`을 전파할 수 있습니다.

### 코드/수식 해설

`import pandas as pd` 및 `import numpy as np`를 사용합니다.

```python
import pandas as pd
import numpy as np

# 예시 Series 1
s1 = pd.Series([np.nan, 2, 3], index=['a', 'b', 'c'])
print(f"Series 1:\n{s1}\n")

# min(), sum(), var() 예시
print(f"s1.min(): {s1.min()}") # NaN을 제외한 [2, 3]에서 최소값 -> 2
print(f"s1.sum(): {s1.sum()}") # NaN을 제외한 [2, 3]에서 합계 -> 5
print(f"s1.var(): {s1.var()}\n") # NaN을 제외한 [2, 3]에서 분산 -> 0.5

# 예시 Series 2
s2 = pd.Series([1, 2, np.nan], index=['a', 'b', 'c'])
print(f"Series 2:\n{s2}\n")

# max(), mean(), std() 예시
print(f"s2.max(): {s2.max()}") # NaN을 제외한 [1, 2]에서 최대값 -> 2
print(f"s2.mean(): {s2.mean()}") # NaN을 제외한 [1, 2]에서 평균 -> 1.5
print(f"s2.std(): {s2.std()}\n") # NaN을 제외한 [1, 2]에서 표준편차 -> 약 0.7

# skipna 인자 제어
s3 = pd.Series([1, 2, np.nan])
print(f"s3.sum(skipna=True): {s3.sum(skipna=True)}") # 기본값, NaN 무시 -> 3
print(f"s3.sum(skipna=False): {s3.sum(skipna=False)}\n") # NaN 있으면 결과도 NaN -> nan

# 모든 값이 NaN인 Series의 동작
s_all_nan = pd.Series([np.nan, np.nan, np.nan])
print(f"s_all_nan.mean(): {s_all_nan.mean()}") # 모든 값이 NaN이면 평균은 NaN -> nan
print(f"s_all_nan.sum(): {s_all_nan.sum()}\n") # 모든 값이 NaN이라도 합계는 0 (Pandas의 특정 동작) -> 0.0

# NaN이 아닌 요소 개수 세기
print(f"s3.count(): {s3.count()}") # NaN을 제외한 개수 -> 2
print(f"s_all_nan.count(): {s_all_nan.count()}\n") # NaN만 있으므로 0 -> 0

# 누락된 값의 개수 세기
print(f"s3.isna().sum(): {s3.isna().sum()}\n") # 1, 2, NaN 중 NaN 개수 -> 1

# 고유값(Uniques) 처리
s_unique = pd.Series([1, 2, 1, np.nan, 3, np.nan])
print(f"s_unique.nunique(dropna=True): {s_unique.nunique(dropna=True)}") # NaN 무시, 1, 2, 3 -> 3
print(f"s_unique.nunique(dropna=False): {s_unique.nunique(dropna=False)}\n") # NaN 포함, 1, 2, 3, NaN -> 4

# Boolean reduction 예시
s_bool = pd.Series([True, False, np.nan])
print(f"s_bool.any(): {s_bool.any()}") # True (NaN 무시)
print(f"s_bool.all(): {s_bool.all()}") # False (True, False, NaN에서 True가 아닌 값이 있으므로)
print(f"s_bool.all(skipna=False): {s_bool.all(skipna=False)}\n") # False (NaN이 있으면 False로 간주되고, False가 하나라도 있으면 all은 False)
# 만약 s_all_true_nan = pd.Series([True, True, np.nan]) 라면, all(skipna=False)는 True가 아닌 NaN이 존재하여 False가 됨
```

**분산(Variance) 수식 해설**:
데이터 $x_1, x_2, \dots, x_n$이 주어졌을 때, 표본 분산(sample variance)은 다음과 같이 계산됩니다. Pandas의 `var()` 함수는 기본적으로 표본 분산을 계산합니다 (즉, `ddof=1`). `NaN` 값이 있는 경우, 해당 값들은 계산에서 제외되고 `n`은 `NaN`이 아닌 값의 개수가 됩니다.

$$
s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2
$$

여기서 $\bar{x}$는 `NaN`을 제외한 데이터의 평균입니다.
슬라이드의 예시 `[NaN, 2, 3]`의 경우, `NaN`을 제외하면 `[2, 3]`이 됩니다.
평균 $\bar{x} = (2+3)/2 = 2.5$
분산 $s^2 = \frac{1}{(2-1)} [(2 - 2.5)^2 + (3 - 2.5)^2] = \frac{1}{1} [(-0.5)^2 + (0.5)^2] = 0.25 + 0.25 = 0.5$

**표준편차(Standard Deviation) 수식 해설**:
표준편차는 분산의 양의 제곱근입니다.
$$
s = \sqrt{s^2}
$$
위 예시에서 $s = \sqrt{0.5} \approx 0.7071$로, 슬라이드의 `0.7`과 일치합니다.

### 구체적 예시

대학생 성적 데이터를 예로 들어 봅시다. 어떤 학생이 특정 과목 시험을 응시하지 않아 성적이 `NaN`으로 기록되었다고 가정해 봅니다.

| 학번 | 과목1 | 과목2 | 과목3 |
| :--- | :--- | :--- | :--- |
| 101 | 85 | 90 | 78 |
| 102 | 92 | NaN | 88 |
| 103 | 70 | 75 | NaN |

*   **`skipna=True` (기본 동작)**: 과목2의 평균을 계산할 때, 학생 102의 `NaN` 성적은 자동으로 무시되고, 학생 101과 103의 성적(90, 75)만을 가지고 평균을 냅니다. `(90+75)/2 = 82.5`
*   **`skipna=False`**: 만약 과목2의 평균을 `skipna=False`로 계산한다면, 학생 102의 `NaN` 때문에 과목2의 평균은 `NaN`이 됩니다. 이는 "모든 학생의 성적이 있어야만 평균을 낼 수 있다"는 엄격한 규칙을 적용하는 것과 같습니다.
*   **`count()`**: 과목3의 `count()`는 학생 101과 102의 성적만 세서 2가 됩니다. (103은 NaN)
*   **`isna().sum()`**: 과목3에 대해 `isna().sum()`을 실행하면 103번 학생의 `NaN`이 카운트되어 1을 반환합니다. 이는 해당 과목에 몇 명의 결시생이 있는지 파악하는 데 유용합니다.

### 시험 포인트

*   ⭐ **기본 동작**: Pandas의 대부분의 통계 집계 함수(min, max, sum, mean, var, std 등)는 기본적으로 `NaN` 값을 건너뛰고 계산합니다 (`skipna=True`가 기본값).
*   ⭐ **`skipna=False`의 역할**: `skipna=False`로 설정하면 데이터에 `NaN`이 하나라도 있을 경우 결과값이 `NaN`이 됩니다. 이는 데이터 완전성을 요구할 때 사용됩니다.
*   ⭐ **`sum()`과 `mean()`의 all-NaN 동작 차이**:
    *   모든 값이 `NaN`인 Series에 대해 `s.mean()`은 `NaN`을 반환합니다.
    *   모든 값이 `NaN`인 Series에 대해 `s.sum()`은 `0`을 반환합니다. 이 차이점을 기억해야 합니다.
*   ⭐ **`s.count()`와 `s.isna().sum()`**:
    *   `s.count()`: `NaN`이 아닌(non-missing) 요소의 개수를 반환합니다.
    *   `s.isna().sum()`: `NaN`인 요소의 개수를 반환합니다. 두 함수는 서로 보완적인 관계입니다.
*   ⭐ **`s.nunique(dropna=...)`**: `dropna=True` (기본값)는 `NaN`을 고유값에서 제외하고, `dropna=False`는 `NaN`을 하나의 고유값으로 포함합니다.
*   ⭐ **Boolean Reduction의 `skipna` 동작**: `s.any()`나 `s.all()`에서 `skipna=True` (기본값)는 `NaN`을 무시하지만, `skipna=False`는 `NaN`의 존재가 결과에 `NaN`을 전파할 수 있다는 것을 이해해야 합니다.

---

## Slide 23

**핵심 개념**
이 슬라이드는 NumPy의 `np.nan` (Not a Number) 및 pandas의 `pd.NA`와 같은 결측치가 포함된 데이터에 대한 pandas Series 및 DataFrame의 축소(Reduction) 연산(예: `sum`, `mean`, `count`, `any`, `all`)의 동작 방식을 설명합니다. 특히 `skipna` 파라미터가 이 연산들에 미치는 영향을 강조합니다.

**코드/수식 해설**

1.  **Series에서의 결측치 처리 (기본 동작)**
    ```python
    import numpy as np
    import pandas as pd

    s = pd.Series([1.0, np.nan, 3.0, np.nan])
    s.sum()    # 결과: 4.0
    s.mean()   # 결과: 2.0
    s.count()  # 결과: 2
    ```
    *   `s.sum()`: 결측치(`np.nan`)를 제외한 유효한 숫자들의 합을 계산합니다 (1.0 + 3.0 = 4.0).
    *   `s.mean()`: 결측치를 제외한 유효한 숫자들의 평균을 계산합니다 ((1.0 + 3.0) / 2 = 2.0).
    *   `s.count()`: 결측치를 제외한 유효한 값들의 개수를 셉니다 (1.0, 3.0 두 개).
    *   **⭐ 대부분의 축소 연산은 `skipna=True`가 기본값이므로, 결측값을 자동으로 건너뛰고 계산합니다.**

2.  **`skipna=False` 옵션**
    ```python
    s.mean(skipna=False) # 결과: nan
    ```
    *   `skipna=False`로 설정하면, Series 내에 단 하나라도 결측치가 있으면 해당 연산의 결과는 `nan`이 됩니다. 이는 모든 데이터가 완전해야만 연산을 수행하겠다는 의미입니다.

3.  **모든 값이 결측치인 경우**
    ```python
    pd.Series([np.nan, np.nan]).sum() # 결과: 0.0
    pd.Series([np.nan, np.nan]).mean() # 결과: nan
    ```
    *   `sum()`: 모든 값이 `np.nan`일 때, `sum()`은 `0.0`을 반환합니다. 이는 덧셈의 항등원인 0을 반환하는 특수한 경우입니다.
    *   `mean()`: 모든 값이 `np.nan`일 때, `mean()`은 `nan`을 반환합니다. 평균을 계산할 유효한 숫자가 없기 때문입니다.

4.  **DataFrame에서의 결측치 처리**
    ```python
    df = pd.DataFrame({"a":[1, np.nan, 3], "b":[2, 4, np.nan]})
    df.mean(axis=0) # Column "a"의 평균: 2.0, Column "b"의 평균: 3.0
    df.mean(axis=1) # Row 0의 평균: 1.5, Row 1의 평균: 4.0, Row 2의 평균: 3.0
    ```
    *   `df.mean(axis=0)`: 각 열(Column)별로 평균을 계산합니다. (기본값 `axis=0`)
        *   'a' 열: `np.nan`을 제외한 (1, 3)의 평균 = 2.0
        *   'b' 열: `np.nan`을 제외한 (2, 4)의 평균 = 3.0
    *   `df.mean(axis=1)`: 각 행(Row)별로 평균을 계산합니다.
        *   0번 행: (1, 2)의 평균 = 1.5
        *   1번 행: (np.nan, 4) 중 `np.nan`을 제외한 4의 평균 = 4.0
        *   2번 행: (3, np.nan) 중 `np.nan`을 제외한 3의 평균 = 3.0
    *   **⭐ `axis` 파라미터는 DataFrame 연산의 방향을 결정합니다. `axis=0`은 열(컬럼) 방향, `axis=1`은 행(로우) 방향입니다.**

5.  **Boolean 타입 결측치 처리 (`pd.NA`)**
    ```python
    b = pd.Series([True, pd.NA, False], dtype="boolean")
    b.any() # 결과: True
    b.all() # 결과: False
    ```
    *   `pd.NA`: `np.nan`과 유사하게 pandas에서 결측값을 나타내지만, `boolean`이나 `integer` 같은 특정 데이터 타입에서 더 유연하게 사용됩니다.
    *   `b.any()`: Series 내에 하나라도 `True`가 있으면 `True`를 반환합니다. `pd.NA`는 `skipna=True`로 인해 무시됩니다.
    *   `b.all()`: Series 내의 모든 값이 `True`여야 `True`를 반환합니다. `False`가 존재하므로 `False`를 반환합니다. `pd.NA`는 무시됩니다.

**구체적 예시**

*   **성적 평균 계산:** 한 학급의 학생들 성적(Series)이 있는데, 어떤 학생은 시험을 안 봐서 성적란에 `np.nan`이 있을 수 있습니다. `s.mean()`을 사용하면 시험을 본 학생들만의 평균 성적을 쉽게 계산할 수 있습니다. 만약 `s.mean(skipna=False)`를 사용한다면, 한 명이라도 시험을 안 본 학생이 있으면 전체 평균이 `nan`이 되어버리는데, 이는 "모두가 시험을 봐야만 평균을 낼 수 있다"는 엄격한 규칙을 적용하는 것과 같습니다.
*   **상품 판매량 집계:** 여러 지점의 일별 상품 판매량 데이터(DataFrame)가 있을 때, 특정 지점에서 데이터 입력 오류로 `np.nan` 값이 있을 수 있습니다. `df.sum(axis=0)`으로 각 상품별 총 판매량을 계산하면, 오류 데이터는 제외하고 실제 판매된 양만 집계할 수 있습니다. `df.mean(axis=1)`은 각 지점의 일일 평균 판매량을 계산할 수 있습니다.

**시험 포인트**

*   **⭐ pandas의 축소 연산(sum, mean, count 등)은 기본적으로 `skipna=True`로 동작하여 결측치(`np.nan`, `pd.NA`)를 자동으로 건너뛴다.**
*   **⭐ `skipna=False`로 설정하면, 하나라도 결측치가 있을 경우 연산 결과는 `nan`이 된다.**
*   **⭐ `sum()` 메소드는 모든 값이 `np.nan`일 경우 `0.0`을 반환하는 특수한 동작을 한다. (반면 `mean()`은 `nan` 반환)**
*   **⭐ DataFrame에서 `axis` 파라미터의 의미를 정확히 이해해야 한다. `axis=0`은 컬럼 방향, `axis=1`은 로우 방향으로 연산을 수행한다.**
*   **⭐ `pd.NA`와 같은 pandas의 결측값도 기본적으로 `skipna=True` 설정 하에 `any()`, `all()`과 같은 불리언 축소 연산에서 무시된다.**

---

## Slide 24

### 핵심 개념
*   **데이터 정렬 (Alignment)**: Pandas의 Series 및 DataFrame 객체 간 산술 연산(이항 연산) 시, 데이터는 해당 객체의 레이블(Series는 인덱스, DataFrame은 인덱스와 컬럼)을 기준으로 자동으로 정렬됩니다. 연산의 결과 레이블은 두 객체의 레이블 집합의 합집합(union)이 됩니다.
*   **결측치 (NaN) 발생**: 정렬 과정에서 한쪽에만 존재하는 레이블에 대해서는 해당 위치의 값이 `NaN` (Not a Number)으로 채워집니다. 이는 두 데이터 구조에 공통으로 존재하는 데이터만 연산하고, 나머지 부분은 결측치로 처리한다는 의미입니다.
*   **`fill_value`를 사용한 결측치 처리**: `.add()`, `.sub()`, `.mul()`, `.div()` 등 메서드 형태의 산술 연산을 사용할 때 `fill_value` 인자를 지정하면, 정렬 과정에서 한쪽에만 존재하는 레이블에 대해 `NaN` 대신 지정된 `fill_value`로 값을 채워 연산을 수행할 수 있습니다.
*   **DataFrame 정렬**: DataFrame 간 연산 시에는 인덱스와 컬럼 레이블 모두를 기준으로 정렬이 발생합니다.
*   **브로드캐스팅 (Broadcasting)과 정렬**: DataFrame과 Series 간의 연산 시에도 레이블 정렬이 기본적으로 적용됩니다. 이때 `axis` 인자를 사용하여 Series를 DataFrame의 인덱스 또는 컬럼 레이블 중 어느 축에 맞춰 정렬하고 브로드캐스팅할지 지정할 수 있습니다.
*   **사전 준비 (Preparation)**: 확정적인(deterministic) 연산 결과를 얻기 위해서는 연산 전에 `reindex` 메서드를 사용하여 공통의 인덱스/컬럼으로 명시적으로 재색인하고, 필요시 `fill_value`를 적용하여 `NaN` 발생을 미리 제어하는 것이 좋습니다.

### 코드/수식 해설

**1. Series 간 정렬 연산 (기본)**
```python
import pandas as pd
import numpy as np

s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([20, 30, 40], index=['b', 'c', 'd'])

# 일반적인 덧셈 연산: 레이블이 일치하는 경우에만 연산되고,
# 일치하지 않는 레이블(a, d)은 NaN이 됨
result_default = s1 + s2
print("s1 + s2:\n", result_default)
```
출력:
```
s1 + s2:
 a     NaN
b    22.0
c    33.0
d     NaN
dtype: float64
```
해설:
*   'b', 'c'는 양쪽에 모두 존재하므로 `s1['b'] + s2['b'] = 2 + 20 = 22`와 같이 연산됩니다.
*   'a'는 `s1`에만 존재하고 `s2`에는 없으므로 결과는 `NaN`이 됩니다.
*   'd'는 `s2`에만 존재하고 `s1`에는 없으므로 결과는 `NaN`이 됩니다.

**2. `fill_value`를 사용한 Series 간 연산**
```python
# .add() 메서드를 사용하고 fill_value=0 지정
# 한쪽에만 있는 레이블에 대해 없는 쪽의 값을 0으로 간주하여 연산
result_filled = s1.add(s2, fill_value=0)
print("\ns1.add(s2, fill_value=0):\n", result_filled)
```
출력:
```
s1.add(s2, fill_value=0):
 a     1.0
b    22.0
c    33.0
d    40.0
dtype: float64
```
해설:
*   'a': `s1['a']` (1) + `s2`에서 'a'에 해당하는 `fill_value` (0) = $1 + 0 = 1$
*   'd': `s1`에서 'd'에 해당하는 `fill_value` (0) + `s2['d']` (40) = $0 + 40 = 40$
*   'b', 'c': 기존과 동일하게 연산됩니다.

**3. DataFrame 간 정렬 연산**
```python
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['x', 'y'])
df2 = pd.DataFrame({'B': [5, 6], 'C': [7, 8]}, index=['y', 'z'])

# DataFrame 간 덧셈: 인덱스와 컬럼 레이블 모두를 기준으로 정렬
# 일치하지 않는 부분은 NaN이 됨
result_df_default = df1 + df2
print("\ndf1 + df2:\n", result_df_default)
```
출력:
```
df1 + df2:
      A    B   C
x  NaN  NaN NaN
y  NaN  9.0 NaN
z  NaN  NaN NaN
```
해설:
*   `df1`과 `df2` 모두에 존재하는 (인덱스, 컬럼) 쌍은 `('y', 'B')` 뿐입니다. 따라서 $df1['y']['B'] + df2['y']['B'] = 4 + 5 = 9$.
*   나머지 모든 (인덱스, 컬럼) 쌍은 한쪽에만 존재하거나 양쪽에 모두 없으므로 `NaN`이 됩니다.

**4. 브로드캐스팅과 `axis` 옵션**
```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['r1', 'r2', 'r3'])
s_cols = pd.Series([10, 20], index=['A', 'B']) # 컬럼 레이블과 동일한 인덱스를 가진 Series

# df의 각 행에 s_cols를 컬럼 기준으로 정렬하여 더하기
# axis='columns' (또는 axis=1)는 Series의 인덱스를 DataFrame의 컬럼에 맞춰 정렬하라는 의미
result_broadcast_cols = df.add(s_cols, axis='columns')
print("\ndf.add(s_cols, axis='columns'):\n", result_broadcast_cols)

s_index = pd.Series([100, 200, 300], index=['r1', 'r2', 'r3']) # 인덱스 레이블과 동일한 인덱스를 가진 Series

# df의 각 컬럼에 s_index를 인덱스 기준으로 정렬하여 더하기
# axis='index' (또는 axis=0)는 Series의 인덱스를 DataFrame의 인덱스에 맞춰 정렬하라는 의미
result_broadcast_index = df.add(s_index, axis='index') # 이 경우 Series는 각 컬럼에 브로드캐스팅 됨
print("\ndf.add(s_index, axis='index'):\n", result_broadcast_index)
```
출력:
```
df.add(s_cols, axis='columns'):
      A   B
r1  11  24
r2  12  25
r3  13  26

df.add(s_index, axis='index'):
        A    B
r1  101  104
r2  202  205
r3  303  306
```
해설:
*   `df.add(s_cols, axis='columns')`: `s_cols`의 인덱스 `['A', 'B']`가 `df`의 컬럼 `['A', 'B']`와 매칭됩니다. `s_cols['A']` (10)는 `df`의 'A' 컬럼 전체에, `s_cols['B']` (20)는 `df`의 'B' 컬럼 전체에 더해집니다.
*   `df.add(s_index, axis='index')`: `s_index`의 인덱스 `['r1', 'r2', 'r3']`가 `df`의 인덱스 `['r1', 'r2', 'r3']`와 매칭됩니다. `s_index['r1']` (100)은 `df`의 'r1' 행 전체에, `s_index['r2']` (200)는 'r2' 행 전체에 더해집니다.

### 구체적 예시

**시나리오**: 당신은 두 팀의 프로젝트 참여도를 점수화한 데이터를 가지고 있습니다. 각 팀원은 프로젝트별로 점수를 받습니다.

**데이터**:
*   **Team A 참여도 (Series)**:
    *   `'Alpha'`: 8점
    *   `'Beta'`: 7점
    *   `'Gamma'`: 9점
*   **Team B 참여도 (Series)**:
    *   `'Beta'`: 6점
    *   `'Gamma'`: 8점
    *   `'Delta'`: 10점

```python
team_a_scores = pd.Series({'Alpha': 8, 'Beta': 7, 'Gamma': 9})
team_b_scores = pd.Series({'Beta': 6, 'Gamma': 8, 'Delta': 10})

# 1. 두 팀의 점수를 단순 합산 (기본 정렬)
# 'Alpha'와 'Delta'는 한쪽에만 있으므로 NaN이 됩니다.
total_scores_default = team_a_scores + team_b_scores
print("1. 단순 합산 결과:\n", total_scores_default)
# 출력:
# Alpha     NaN
# Beta     13.0
# Delta     NaN
# Gamma    17.0
# dtype: float64

# 2. 두 팀의 점수를 합산하되, 없는 팀원은 0점으로 간주하여 합산 (fill_value 활용)
# 'Alpha'는 Team B에 없으므로 8 + 0 = 8
# 'Delta'는 Team A에 없으므로 0 + 10 = 10
total_scores_filled = team_a_scores.add(team_b_scores, fill_value=0)
print("\n2. fill_value=0을 이용한 합산:\n", total_scores_filled)
# 출력:
# Alpha     8.0
# Beta     13.0
# Delta    10.0
# Gamma    17.0
# dtype: float64
```
이 예시를 통해 Pandas가 어떻게 레이블을 기준으로 데이터를 정렬하고, `fill_value`가 `NaN`을 어떻게 효과적으로 처리하여 유의미한 연산 결과를 도출하는지 명확히 이해할 수 있습니다.

### 시험 포인트
*   ⭐ **Pandas 데이터 정렬의 기본 원리**: Series는 인덱스, DataFrame은 인덱스와 컬럼 레이블을 기준으로 자동 정렬되며, 일치하지 않는 레이블은 `NaN`이 된다는 것을 이해해야 합니다. 이는 Pandas 데이터 처리의 핵심 개념 중 하나입니다.
*   ⭐ **`fill_value` 인자의 활용**: `add()`, `sub()`, `mul()`, `div()` 등의 메서드에서 `fill_value`를 사용하여 결측치를 어떻게 처리하고 연산 결과를 제어하는지 파악하는 것이 중요합니다. 특히, `fill_value`가 적용되는 시점(정렬 후, 연산 전)과 방법에 대한 이해가 필수입니다.
*   ⭐ **브로드캐스팅과 `axis` 옵션**: Series와 DataFrame 간 연산 시 `axis` 인자를 통해 정렬 기준 축(`'index'` 또는 `'columns'`)을 지정하는 방법을 정확히 알아야 합니다. 이 옵션이 연산 결과에 어떤 영향을 미치는지 다양한 예시를 통해 연습해 보세요.
*   ⭐ **`NaN`의 발생과 전파**: 산술 연산에서 `NaN`이 어떻게 발생하는지, 그리고 `NaN`을 포함한 연산 결과가 일반적으로 `NaN`으로 전파되는 원리를 이해해야 합니다. 이는 데이터 클리닝 및 전처리 과정에서 중요한 고려사항이 됩니다.
*   ⭐ **`+` 연산자와 `.add()` 메서드의 차이점**: 기본적으로 동일한 기능을 하지만, `.add()` 메서드는 `fill_value`와 같은 추가 옵션을 제공하여 `+` 연산자보다 더 세밀한 제어가 가능하다는 점을 기억하세요.

---

## Slide 25

**핵심 개념**:
Pandas Series의 산술 연산은 **인덱스 정렬(Index Alignment)**을 기반으로 합니다. 두 Series 간에 산술 연산을 수행할 때, Pandas는 자동으로 인덱스 레이블을 기준으로 데이터를 정렬합니다.

*   **기본 산술 연산자 (`+`, `-`, `*`, `/`)**: 두 Series에 **모두 존재하는 인덱스(교집합)**에 대해서만 연산을 수행합니다. 어느 한쪽 Series에만 존재하는 인덱스의 경우, 해당 위치의 결과는 **`NaN` (Not a Number)**으로 채워집니다.
*   **메서드를 통한 산술 연산 (`.add()`, `.sub()`, `.mul()`, `.div()`)**: 기본 연산자와 동일하게 인덱스 정렬을 수행하지만, `fill_value` 인자를 통해 인덱스가 일치하지 않아 값이 누락된 경우 해당 위치에 대체할 값을 지정할 수 있습니다. 이를 통해 `NaN`을 방지하고 특정 기본값으로 연산을 수행할 수 있습니다.

**코드/수식 해설**:

*   **초기 Series 생성**:
    ```python
    import pandas as pd

    s1 = pd.Series({"a": 1.0, "b": 2.0})
    s2 = pd.Series({"b": 10.0, "c": 100.0})
    ```
    `s1`은 인덱스 `['a', 'b']`를, `s2`는 인덱스 `['b', 'c']`를 가집니다. 두 Series에 공통으로 존재하는 인덱스는 `'b'`입니다.

*   **기본 산술 연산 (`s1 + s2`)**:
    ```python
    # s1 + s2
    # a      NaN
    # b     12.0
    # c      NaN
    # dtype: float64
    ```
    `+` 연산자는 인덱스를 기준으로 정렬합니다.
    *   `'b'` 인덱스: `s1`의 `2.0`과 `s2`의 `10.0`이 더해져 `12.0`이 됩니다.
    *   `'a'` 인덱스: `s1`에만 존재하고 `s2`에는 없으므로, `s2`의 값이 `NaN`으로 간주되어 `1.0 + NaN`의 결과는 `NaN`이 됩니다.
    *   `'c'` 인덱스: `s2`에만 존재하고 `s1`에는 없으므로, `s1`의 값이 `NaN`으로 간주되어 `NaN + 100.0`의 결과는 `NaN`이 됩니다.
    결과 Series는 두 Series의 모든 고유 인덱스(`'a', 'b', 'c'`)를 포함합니다.

*   **메서드를 통한 산술 연산 (`s1.add(s2, fill_value=0)`)**:
    ```python
    # s1.add(s2, fill_value=0)
    # a      1.0
    # b     12.0
    # c    100.0
    # dtype: float64
    ```
    `.add()` 메서드를 사용하고 `fill_value=0`으로 설정하면, 인덱스가 일치하지 않는 경우 누락된 값을 `0`으로 채워서 연산을 수행합니다.
    *   `'b'` 인덱스: `2.0 + 10.0 = 12.0` (동일)
    *   `'a'` 인덱스: `s1`의 `1.0`과 `s2`의 `0` (fill_value)이 더해져 `1.0 + 0 = 1.0`이 됩니다.
    *   `'c'` 인덱스: `s1`의 `0` (fill_value)과 `s2`의 `100.0`이 더해져 `0 + 100.0 = 100.0`이 됩니다.
    `fill_value` 덕분에 `NaN` 없이 모든 인덱스에 대한 연산 결과를 얻을 수 있습니다.

**구체적 예시**:
두 학생의 과목별 점수를 합산하는 상황을 생각해 봅시다.

*   **학생 A (`s1`)**: 국어 80점, 영어 90점
*   **학생 B (`s2`)**: 영어 70점, 수학 95점

1.  **`s1 + s2` (기본 합산)**:
    *   국어: 학생 A만 점수가 있으므로, 학생 B의 국어 점수를 알 수 없어 총점은 `NaN`.
    *   영어: 학생 A (90점) + 학생 B (70점) = 160점.
    *   수학: 학생 B만 점수가 있으므로, 학생 A의 수학 점수를 알 수 없어 총점은 `NaN`.
    결과는 국어 `NaN`, 영어 160점, 수학 `NaN`이 됩니다.

2.  **`s1.add(s2, fill_value=0)` (결시 과목 0점 처리 후 합산)**:
    *   국어: 학생 A (80점) + 학생 B (0점, 결시로 간주) = 80점.
    *   영어: 학생 A (90점) + 학생 B (70점) = 160점.
    *   수학: 학생 A (0점, 결시로 간주) + 학생 B (95점) = 95점.
    결과는 국어 80점, 영어 160점, 수학 95점이 되어 모든 과목의 합산 점수를 얻을 수 있습니다.

**시험 포인트**:
*   ⭐ **Pandas Series 및 DataFrame의 산술 연산 시 발생하는 인덱스 정렬(Index Alignment) 개념을 정확히 이해하고 설명할 수 있어야 합니다.** 특히, 기본 연산자(`+`) 사용 시와 메서드(`.add()`) 사용 시 `NaN` 처리 방식의 차이점을 강조해야 합니다.
*   ⭐ **`fill_value` 인자의 역할과 그 효과**를 실제 코드 예시와 함께 설명하고, `fill_value` 사용 여부에 따른 결과 변화를 비교할 수 있어야 합니다. 이는 데이터 분석에서 결측치(`NaN`)를 다루는 중요한 방법 중 하나입니다.
*   ⭐ Series와 DataFrame 간의 연산에서도 동일하게 인덱스/컬럼 정렬 규칙이 적용되므로, 이 개념이 Pandas의 핵심적인 동작 방식임을 인지해야 합니다.

---

## Slide 26

안녕하세요, POSTECH 컴퓨터공학과 전공 튜터입니다. 데이터분석 입문 강의의 "Sort, Rank, Top-k, Quantiles" 슬라이드에 대한 마크다운 노트입니다.

---

### 핵심 개념

*   **정렬 (Sort)**: pandas Series의 데이터를 특정 기준(값 또는 인덱스)에 따라 오름차순 또는 내림차순으로 재배열하는 기능입니다.
    *   `sort_values()`: Series의 **값(values)**을 기준으로 정렬합니다. 동일한 값이 있을 경우 기존 순서를 유지하는 `stable` 정렬 특성을 가집니다. 인덱스는 값과 함께 이동하며 보존됩니다.
    *   `sort_index()`: Series의 **인덱스(labels)**를 기준으로 정렬합니다. 인덱스가 문자열일 경우 알파벳 순서, 숫자일 경우 숫자 크기 순서로 정렬됩니다. 이 또한 `stable` 정렬이며, 값은 인덱스와 함께 이동하여 보존됩니다.
*   **순위 부여 (Rank)**: Series의 각 값에 대해 상대적인 순위를 매기는 기능입니다.
    *   `rank()`: 각 값의 순위를 `float` 타입으로 할당합니다. `method` 인자를 통해 동일한 값이 있을 때 순위를 처리하는 방식을 지정할 수 있습니다. `dense`는 동일한 값에 대해 연속적인 순위를 부여합니다 (예: 1, 2, 2, 3).
*   **Top-k / Bottom-k 추출**: Series에서 가장 크거나 작은 K개의 값을 효율적으로 찾아내는 기능입니다.
    *   `nlargest(k)`: Series에서 값이 가장 큰 상위 `k`개를 반환합니다.
    *   `nsmallest(k)`: Series에서 값이 가장 작은 하위 `k`개를 반환합니다.
    *   이 두 함수는 Series를 완전히 정렬하는 것보다 훨씬 빠르게 상위/하위 `k`개의 값을 찾을 수 있으며, 결과는 정렬된 Series 형태로 반환됩니다.
*   **분위수 (Quantiles)**: 데이터셋을 동일한 비율로 나누는 기준이 되는 값입니다. 예를 들어, 중앙값(median)은 0.5 분위수에 해당합니다.
    *   `quantile(q)`: `q`에 해당하는 분위수 값을 계산합니다. `q`는 0에서 1 사이의 실수(비율)입니다.
        *   `q`가 단일 실수일 경우, 해당 분위수 값(scalar)을 반환합니다.
        *   `q`가 리스트 형태일 경우, 각 분위수에 해당하는 값들을 Series 형태로 반환하며, 인덱스는 `q` 리스트의 값으로 설정됩니다.

### 코드/수식 해설

예시를 위한 초기 Series `s`는 다음과 같습니다.
```python
import pandas as pd
s = pd.Series([5, 2, 7, 4, 9], index=list('abcde'))
# s:
# a    5
# b    2
# c    7
# d    4
# e    9
# dtype: int64
```

*   **`s.sort_values(ascending=...)`**
    ```python
    # 값을 오름차순으로 정렬 (기본값)
    print(s.sort_values())
    # b    2
    # d    4
    # a    5
    # c    7
    # e    9
    # dtype: int64

    # 값을 내림차순으로 정렬
    print(s.sort_values(ascending=False))
    # e    9
    # c    7
    # a    5
    # d    4
    # b    2
    # dtype: int64
    ```
    이 함수는 Series의 `값`을 기준으로 정렬하며, 인덱스는 값과 함께 이동합니다.

*   **`s.sort_index(ascending=...)`**
    ```python
    # 인덱스를 오름차순으로 정렬 (기본값)
    print(s.sort_index())
    # a    5
    # b    2
    # c    7
    # d    4
    # e    9
    # dtype: int64

    # 인덱스를 내림차순으로 정렬
    print(s.sort_index(ascending=False))
    # e    9
    # d    4
    # c    7
    # b    2
    # a    5
    # dtype: int64
    ```
    이 함수는 Series의 `인덱스`를 기준으로 정렬하며, 값은 인덱스와 함께 이동합니다.

*   **`s.rank(method='dense', ascending=...)`**
    ```python
    # 값을 기준으로 순위를 부여 (기본은 오름차순, dense 방식)
    # 2(b) -> 1, 4(d) -> 2, 5(a) -> 3, 7(c) -> 4, 9(e) -> 5
    print(s.rank(method='dense'))
    # a    3.0
    # b    1.0
    # c    4.0
    # d    2.0
    # e    5.0
    # dtype: float64

    # 내림차순으로 순위 부여
    # 9(e) -> 1, 7(c) -> 2, 5(a) -> 3, 4(d) -> 4, 2(b) -> 5
    print(s.rank(method='dense', ascending=False))
    # a    3.0
    # b    5.0
    # c    2.0
    # d    4.0
    # e    1.0
    # dtype: float64
    ```
    `dense` 방식은 공동 순위가 있어도 다음 순위를 건너뛰지 않고 연속적으로 부여합니다. 예를 들어, `[10, 20, 20, 30]`의 순위는 `[1, 2, 2, 3]`이 됩니다.

*   **`s.nlargest(k)` / `s.nsmallest(k)`**
    ```python
    # 가장 큰 2개의 값
    print(s.nlargest(2))
    # e    9
    # c    7
    # dtype: int64

    # 가장 작은 2개의 값
    print(s.nsmallest(2))
    # b    2
    # d    4
    # dtype: int64
    ```
    반환되는 Series는 상위/하위 K개의 값으로 구성되며, 해당 값들은 정렬된 상태입니다.

*   **`s.quantile(q)`**
    데이터 $X = \{x_1, x_2, ..., x_N\}$에 대해 $p$ 분위수 $Q(p)$는 데이터를 오름차순으로 정렬했을 때, 대략 $(N-1)p$ 번째 위치에 해당하는 값입니다.
    ```python
    # 중앙값 (0.5 분위수) 계산
    print(s.quantile(0.5))
    # 5.0 (정렬된 Series: 2, 4, 5, 7, 9. 중앙값은 5)

    # 1사분위수 (0.25)와 3사분위수 (0.75) 계산
    print(s.quantile([0.25, 0.75]))
    # 0.25    3.5
    # 0.75    7.5
    # dtype: float64
    ```
    `q`가 리스트일 경우 반환되는 Series의 인덱스는 `q` 값들로 이루어집니다.

### 구체적 예시

1.  **학생 시험 성적 처리**:
    *   `s.sort_values(ascending=False)`: 전체 학생의 시험 점수를 높은 순서대로 나열하여 등수를 확인합니다.
    *   `s.sort_index()`: 학생들의 학번(인덱스)을 기준으로 오름차순으로 정렬하여 학생 명단을 확인합니다.
    *   `s.rank(method='dense')`: 학생들의 시험 점수에 따라 등수를 부여합니다. 예를 들어, 100점 2명이 있으면 둘 다 1등으로 처리하고, 다음 점수는 2등이 아니라 3등으로 매기는 방식입니다 (`dense`가 아닐 경우 1등, 1등, 3등 이런 식).
    *   `s.nlargest(3)`: 전체 학생 중 시험 성적이 가장 좋은 상위 3명의 학생과 그 점수를 빠르게 확인합니다.
    *   `s.quantile(0.5)`: 전체 학생의 시험 점수 중앙값을 계산하여, 절반의 학생은 이 점수보다 낮고 절반의 학생은 이 점수보다 높다는 것을 파악합니다.

2.  **주식 가격 데이터 분석**:
    *   `s.sort_values()`: 주식 일일 변동률을 오름차순으로 정렬하여 급락한 주식들을 파악합니다.
    *   `s.nlargest(5)`: 특정 기간 동안 가장 많이 상승한 상위 5개 주식을 빠르게 찾습니다.
    *   `s.quantile([0.05, 0.95])`: 특정 주식의 가격 변동폭에 대한 5% 하위 분위수와 95% 상위 분위수를 계산하여, 극단적인 가격 변동 지점을 파악합니다.

### 시험 포인트

*   ⭐ `s.sort_values()`는 **값**을 기준으로, `s.sort_index()`는 **인덱스**를 기준으로 정렬합니다. 두 함수의 역할과 사용 시점을 명확히 구분해야 합니다.
*   ⭐ `s.rank()` 함수의 `method` 인자 중 `'dense'`는 공동 순위가 있을 때 다음 순위를 건너뛰지 않고 연속적으로 부여한다는 점을 이해해야 합니다. (`average`, `min`, `max`, `first` 등의 다른 `method`와의 차이점도 알아두면 좋습니다.)
*   ⭐ `s.nlargest(k)`와 `s.nsmallest(k)`는 Series 전체를 정렬하는 것보다 훨씬 효율적으로 상위/하위 K개의 값을 찾아줍니다. 또한, 반환되는 Series는 이미 **정렬된 상태**입니다.
*   ⭐ `s.quantile(q)`에서 `q`가 **단일 float**일 때와 **리스트**일 때 반환되는 데이터 타입(scalar vs. Series)을 명확히 구분해야 합니다.
*   ⭐ 대부분의 정렬 및 순위 부여 함수는 `ascending` 인자를 통해 오름차순/내림차순 정렬을 제어할 수 있습니다. 기본값은 `ascending=True` (오름차순)입니다.
*   ⭐ 판다스 Series의 주요 메서드들은 원본 Series를 직접 변경하지 않고, 변경된 내용을 담은 새로운 Series를 반환한다는 점 (immutable operation)을 기억해야 합니다.

---

## Slide 27

**핵심 개념**
이 슬라이드는 pandas Series 객체에서 데이터의 정렬, 순위 부여, 상위/하위 K개 항목 추출, 그리고 분위수 계산에 사용되는 주요 메서드들을 소개합니다. 이러한 기능들은 데이터의 분포를 이해하고 특정 기준에 따라 데이터를 재구성하는 데 필수적입니다.

**코드/수식 해설**

1.  **`s.sort_values(ascending=False)`**
    *   **설명**: Series의 **값**을 기준으로 정렬합니다. `ascending=False`는 내림차순(값이 큰 것부터)으로 정렬하라는 의미입니다.
    *   **코드**:
        ```python
        s.sort_values(ascending=False)
        # 예시 출력:
        # e    9
        # c    7
        # a    5
        # ...
        ```
    *   **참고**: 원본 Series는 변경되지 않고, 정렬된 새로운 Series를 반환합니다.

2.  **`s.sort_index()`**
    *   **설명**: Series의 **인덱스**를 기준으로 정렬합니다. 기본적으로 오름차순(인덱스 값이 작은 것부터)으로 정렬됩니다.
    *   **코드**:
        ```python
        s.sort_index()
        # 예시 출력:
        # a    5
        # b    2
        # c    7
        # ...
        ```
    *   **참고**: `ascending=True`가 기본값입니다.

3.  **`s.rank(method='dense', ascending=False)`**
    *   **설명**: Series의 각 값에 순위를 부여합니다.
        *   `method`: 동일한 값이 있을 때 순위를 어떻게 처리할지 지정합니다.
            *   `'average'` (기본값): 동점일 경우 평균 순위를 부여합니다. (예: 1, 2, 2, 3 -> 1.0, 2.5, 2.5, 4.0)
            *   `'min'`: 동점일 경우 가장 낮은 순위를 부여합니다. (예: 1, 2, 2, 3 -> 1.0, 2.0, 2.0, 4.0)
            *   `'max'`: 동점일 경우 가장 높은 순위를 부여합니다. (예: 1, 2, 2, 3 -> 1.0, 3.0, 3.0, 4.0)
            *   `'dense'`: 동점일 경우 연속적인 순위를 부여합니다. (예: 1, 2, 2, 3 -> 1.0, 2.0, 2.0, 3.0)
            *   `'first'`: 동점일 경우 Series에 나타난 순서대로 순위를 부여합니다.
        *   `ascending=False`: 값이 클수록 더 높은(낮은 숫자) 순위가 부여됩니다.
    *   **코드**:
        ```python
        s.rank(method='dense', ascending=False)
        # 예시 출력 (부분):
        # a    3.0
        # b    5.0
        # ...
        # e    1.0
        ```

4.  **`s.nlargest(2)`**
    *   **설명**: Series에서 값이 가장 큰 상위 `n`개(여기서는 2개)의 항목을 반환합니다.
    *   **코드**:
        ```python
        s.nlargest(2)
        # 예시 출력:
        # e    9
        # c    7
        ```

5.  **`s.nsmallest(2)`**
    *   **설명**: Series에서 값이 가장 작은 하위 `n`개(여기서는 2개)의 항목을 반환합니다.
    *   **코드**:
        ```python
        s.nsmallest(2)
        # 예시 출력 (슬라이드에 없음, 가정):
        # b    2
        # a    5
        ```

6.  **`s.quantile([0.25, 0.50, 0.75])`**
    *   **설명**: Series의 분위수(Quantile)를 계산합니다. 분위수는 데이터를 오름차순으로 정렬했을 때 특정 백분율에 해당하는 값입니다.
        *   $Q(p)$는 전체 데이터 중 $p$ 비율이 그 값보다 작거나 같음을 의미합니다.
    *   **코드**:
        ```python
        s.quantile([0.25, 0.50, 0.75])
        # 예시 출력:
        # 0.25    4.0
        # 0.50    5.0
        # 0.75    7.0
        ```
    *   **참고**: `0.25`는 1사분위수(Q1), `0.50`은 2사분위수(중앙값, Q2), `0.75`는 3사분위수(Q3)를 의미합니다. `s.median()`은 `s.quantile(0.5)`와 동일합니다.

**구체적 예시**

학생들의 시험 점수 `s = pd.Series({'a': 85, 'b': 92, 'c': 78, 'd': 92, 'e': 65})`가 있다고 가정해 봅시다.

*   **`s.sort_values(ascending=False)`**: 성적 우수자 순으로 학생들을 정렬하여 `b: 92, d: 92, a: 85, c: 78, e: 65`와 같이 보여줍니다.
*   **`s.sort_index()`**: 학생들의 이름을 알파벳 순서대로 정렬하여 `a: 85, b: 92, c: 78, d: 92, e: 65`와 같이 보여줍니다.
*   **`s.rank(method='dense', ascending=False)`**:
    *   'b', 'd' 학생이 92점으로 동점일 때, `dense` 방식은 둘 다 1등으로 처리하고 다음 학생('a')을 2등으로 처리합니다. (실제로는 `b, d`가 1.0, 1.0, `a`가 2.0, `c`가 3.0, `e`가 4.0)
    *   `average` 방식이었다면 'b', 'd'는 (1+2)/2 = 1.5등이 되고, 'a'는 3등이 되었을 것입니다.
*   **`s.nlargest(2)`**: 성적 상위 2명(b, d)과 그 점수(92)를 빠르게 찾아줍니다.
*   **`s.nsmallest(1)`**: 성적이 가장 낮은 학생(e)과 그 점수(65)를 찾아줍니다.
*   **`s.quantile([0.25, 0.50, 0.75])`**: 전체 학생 중 하위 25%, 50%(중앙값), 75%에 해당하는 점수를 계산하여 점수 분포를 파악할 수 있습니다. 예를 들어 0.50 분위수가 85점이라면, 학생 절반이 85점 이하라는 것을 의미합니다.

**시험 포인트**

*   ⭐ `sort_values()`와 `sort_index()`의 **차이점**을 정확히 이해하고 각각 어떤 상황에서 사용되는지 알아두세요.
*   ⭐ `rank()` 메서드의 다양한 `method` 옵션(특히 `average`, `dense`, `min`, `max`)이 **동점일 때 순위를 어떻게 처리하는지** 그 차이를 숙지해야 합니다. `ascending` 파라미터의 역할도 중요합니다.
*   ⭐ `nlargest()`와 `nsmallest()`는 대량의 데이터에서 **Top-k 또는 Bottom-k** 데이터를 효율적으로 추출할 때 유용합니다. 정렬 후 슬라이싱하는 것보다 성능상 이점이 있을 수 있습니다.
*   ⭐ 분위수(Quantile)의 개념, 특히 **사분위수(Q1, Q2, Q3)**가 데이터 분포 분석에 어떻게 활용되는지 이해해야 합니다. `median()`이 `quantile(0.5)`와 같다는 것을 기억하세요.

---

## Slide 28

### 핵심 개념

이 슬라이드는 Pandas Series 객체에서 시계열 데이터 분석 및 변환에 유용한 함수들을 소개합니다. 주로 누적 연산, 시점 이동(지연/선행), 그리고 변화량 및 변화율 계산에 사용되는 메서드들입니다.

*   **누적 연산 (Cumulative Operations)**:
    *   `s.cumsum()`: Series의 각 시점까지의 누적 합을 계산합니다.
    *   `s.cummax()`: Series의 각 시점까지의 누적 최댓값(running maximum)을 계산합니다.
    *   `s.cummin()`: Series의 각 시점까지의 누적 최솟값(running minimum)을 계산합니다.
    *   `s.cumprod()`: Series의 각 시점까지의 누적 곱을 계산합니다.

*   **시점 이동 (Shifting)**:
    *   `s.shift(periods=k, fill_value=None)`: Series의 값을 `k`만큼 이동(move)시킵니다.
        *   `k > 0`일 경우, `k`만큼 지연(lag)시킵니다. 즉, 현재 위치에 `k` 시점 이전의 값을 가져옵니다. 새로운 데이터가 채워지는 상위 `k`개 위치는 `NaN`이 됩니다.
        *   `k < 0`일 경우, `|k|`만큼 선행(lead)시킵니다. 즉, 현재 위치에 `|k|` 시점 이후의 값을 가져옵니다. 새로운 데이터가 채워지는 하위 `|k|`개 위치는 `NaN`이 됩니다.
        *   `fill_value`를 지정하면, `NaN` 대신 해당 값으로 채워집니다. 인덱스는 그대로 유지됩니다.

*   **변화량 계산 (Difference)**:
    *   `s.diff(periods=k)`: `k` 시점 이전의 값과의 차이(절대 변화량)를 계산합니다. `s - s.shift(k)`와 동일한 연산입니다. 첫 `k`개의 값은 `NaN`이 됩니다. `k`가 음수면 미래 값과의 차이를 계산(forward difference)합니다.

*   **변화율 계산 (Percentage Change)**:
    *   `s.pct_change(periods=k)`: `k` 시점 이전의 값 대비 상대적 변화율을 계산합니다. $\frac{s}{s.\text{shift}(k)} - 1$ 와 동일한 연산입니다. 첫 `k`개의 값은 `NaN`이 됩니다. 0으로 나누기가 발생할 경우 `inf` 또는 `NaN`이 될 수 있습니다.

### 코드/수식 해설

다음 예시 Series `s`를 통해 각 함수들을 설명합니다.

```python
import pandas as pd
import numpy as np

s = pd.Series([10, 12, 11, 15, 14, 18], name='data')
print("Original Series:")
print(s)
print("-" * 30)

# 1. 누적 연산
print("s.cumsum():\n", s.cumsum())
print("s.cummax():\n", s.cummax())
print("s.cummin():\n", s.cummin())
print("s.cumprod():\n", s.cumprod())
print("-" * 30)

# 2. 시점 이동 (shift)
print("s.shift(periods=1): (lag by 1)")
print(s.shift(periods=1))
# Output:
# 0     NaN
# 1    10.0
# 2    12.0
# 3    11.0
# 4    15.0
# 5    14.0
# Name: data, dtype: float64

print("\ns.shift(periods=-1): (lead by 1)")
print(s.shift(periods=-1))
# Output:
# 0    12.0
# 1    11.0
# 2    15.0
# 3    14.0
# 4    18.0
# 5     NaN
# Name: data, dtype: float64

print("\ns.shift(periods=2, fill_value=0): (lag by 2, fill NaN with 0)")
print(s.shift(periods=2, fill_value=0))
# Output:
# 0     0.0
# 1     0.0
# 2    10.0
# 3    12.0
# 4    11.0
# 5    15.0
# Name: data, dtype: float64
print("-" * 30)

# 3. 변화량 계산 (diff)
print("s.diff(periods=1): (difference from previous element)")
print(s.diff(periods=1))
# Output:
# 0    NaN
# 1    2.0
# 2   -1.0
# 3    4.0
# 4   -1.0
# 5    4.0
# Name: data, dtype: float64
# 수식: diff_i = s_i - s_{i-k}
# 예시 (k=1):
# s[1] - s[0] = 12 - 10 = 2
# s[2] - s[1] = 11 - 12 = -1

print("\ns.diff(periods=-1): (forward difference - difference from next element)")
print(s.diff(periods=-1))
# Output:
# 0   -2.0
# 1    1.0
# 2   -4.0
# 3    1.0
# 4   -4.0
# 5    NaN
# Name: data, dtype: float64
# 수식: diff_i = s_i - s_{i-(-k)} = s_i - s_{i+k} (여기서 k는 양수로 생각)
# 예시 (k=1):
# s[0] - s[1] = 10 - 12 = -2
# s[1] - s[2] = 12 - 11 = 1
print("-" * 30)

# 4. 변화율 계산 (pct_change)
print("s.pct_change(periods=1): (percentage change from previous element)")
print(s.pct_change(periods=1))
# Output:
# 0         NaN
# 1    0.200000
# 2   -0.083333
# 3    0.363636
# 4   -0.066667
# 5    0.285714
# Name: data, dtype: float64
# 수식: pct_change_i = (s_i - s_{i-k}) / s_{i-k} = s_i / s_{i-k} - 1
# 예시 (k=1):
# (s[1] - s[0]) / s[0] = (12 - 10) / 10 = 2 / 10 = 0.2
# (s[2] - s[1]) / s[1] = (11 - 12) / 12 = -1 / 12 = -0.0833...

# 0으로 나누기 예시
s_zero = pd.Series([10, 0, 20])
print("\ns_zero.pct_change(): (division by zero)")
print(s_zero.pct_change())
# Output:
# 0         NaN
# 1   -1.000000
# 2         inf
# dtype: float64
# 2번째 값은 (20 - 0) / 0 이 되어 inf가 됨
```

### 구체적 예시

주식 시장의 일일 종가(`s`)를 가정해 봅시다.

*   **`s.cumsum()`**: 특정 시점까지의 총 주가 합계. 실제 분석에서는 주가 자체보다 거래량의 누적 합 등에 더 자주 사용됩니다.
*   **`s.cummax()` / `s.cummin()`**: 특정 시점까지 주가가 기록한 최고점/최저점. "이 주식은 지금까지 최고 얼마까지 올랐었지?" 또는 "최저 얼마까지 떨어졌었지?"를 확인할 때 유용합니다.
*   **`s.shift(periods=1)`**: 어제 종가. 오늘의 종가와 비교하여 전일 대비 변동을 계산할 때 사용됩니다.
*   **`s.shift(periods=-1)`**: 내일 종가. (현재 시점에서 보면 미래값이지만) 분석에서는 미래 시점 데이터 예측 모델을 만들 때, 목표 변수로 사용될 수 있습니다.
*   **`s.diff(periods=1)`**: 일일 주가 변동폭. 오늘의 종가에서 어제의 종가를 뺀 값으로, 주가가 얼마나 변했는지 절대적인 크기를 보여줍니다.
    *   예: `s.diff()`가 2라면 어제보다 2원 올랐다는 의미입니다.
*   **`s.pct_change(periods=1)`**: 일일 주가 수익률. 오늘의 종가가 어제 대비 몇 퍼센트 변했는지 나타냅니다.
    *   예: `s.pct_change()`가 0.2라면 어제보다 20% 올랐다는 의미입니다. 투자 수익률 계산에 필수적입니다.

### 시험 포인트

*   ⭐ **`shift()` 함수의 역할과 `periods` 파라미터**: `periods`가 양수일 때는 과거 값을 가져오는 `lag` 연산, 음수일 때는 미래 값을 가져오는 `lead` 연산임을 정확히 이해해야 합니다. 또한, `fill_value`가 `NaN` 값을 어떻게 처리하는지 알아두세요.
*   ⭐ **`diff()`와 `pct_change()`의 계산 방식**: 각각 $s_i - s_{i-k}$와 $s_i / s_{i-k} - 1$ 라는 수식을 정확히 알고 있어야 합니다. 특히 `pct_change`는 상대적 변화율, `diff`는 절대적 변화량을 나타냄을 구분해야 합니다.
*   ⭐ **초기 `NaN` 값의 발생**: `shift`, `diff`, `pct_change` 모두 `periods=k`일 때, 처음 `k`개의 값이 `NaN`으로 채워진다는 것을 기억하세요. 이는 연산을 위해 `k` 시점 이전/이후의 값이 필요하지만 존재하지 않기 때문입니다.
*   ⭐ **`pct_change()`의 0으로 나누기**: 분모가 0이 되는 경우(`s.shift(k)` 값이 0인 경우) `inf` (무한대) 또는 `NaN`이 발생할 수 있음을 인지하고 있어야 합니다.
*   ⭐ **`cum*` 계열 함수의 의미**: `cumsum`, `cummax`, `cummin`, `cumprod`가 각각 누적 합, 누적 최댓값, 누적 최솟값, 누적 곱을 의미하며, 각 시점까지의 연산 결과를 반환한다는 것을 숙지해야 합니다.

---

## Slide 29

---

### pandas 시계열 데이터 조작: `diff`, `shift`, `pct_change`

이 슬라이드에서는 pandas Series 객체에서 시계열 데이터의 변화를 분석하는 데 유용한 세 가지 핵심 메서드 `shift`, `diff`, `pct_change`에 대해 알아봅니다. 이 함수들은 금융 데이터, 센서 데이터 등 시간에 따라 변화하는 데이터를 다룰 때 필수적입니다.

---

#### 1. `shift()`

-   **핵심 개념**:
    `shift()` 메서드는 Series의 데이터를 특정 칸 수만큼 위 또는 아래로 이동(lag 또는 lead)시킵니다. 인덱스는 그대로 유지되며, 이동으로 인해 비게 되는 위치는 `NaN` (Not a Number)으로 채워집니다.

-   **코드/수식 해설**:

    *   데이터 초기화:
        ```python
        import pandas as pd
        s = pd.Series([100, 110, 121], index=['t0', 't1', 't2'])
        print(s)
        # t0    100
        # t1    110
        # t2    121
        # dtype: int64
        ```

    *   `s.shift(1)`: 양수 인자는 데이터를 아래로 이동(lag)시킵니다.
        ```python
        s.shift(1) # move values down by 1 (lag)
        # t0     NaN
        # t1   100.0
        # t2   110.0
        # dtype: float64
        ```
        `t0`의 원래 값 100이 `t1` 위치로, `t1`의 원래 값 110이 `t2` 위치로 이동합니다. `t0`에는 이전 데이터가 없으므로 `NaN`이 됩니다.

    *   `s.shift(-1)`: 음수 인자는 데이터를 위로 이동(lead)시킵니다.
        ```python
        s.shift(-1) # lead: pull next value up
        # t0    110.0
        # t1    121.0
        # t2      NaN
        # dtype: float64
        ```
        `t1`의 원래 값 110이 `t0` 위치로, `t2`의 원래 값 121이 `t1` 위치로 이동합니다. `t2`에는 다음 데이터가 없으므로 `NaN`이 됩니다.

-   **구체적 예시**:
    주식 시장 데이터에서 `shift(1)`은 '전날 종가'를 구하는 것과 같습니다. 오늘(현재 인덱스) 데이터와 비교하여 전날 데이터를 가져올 때 유용합니다. `shift(-1)`은 '다음날 종가'를 미리 가져오는 것과 비슷합니다.

-   **시험 포인트**:
    ⭐ `shift()`의 양수 인자는 lag(이전 값), 음수 인자는 lead(다음 값)를 의미함을 정확히 이해하고 있어야 합니다. 이동으로 인해 생성되는 `NaN` 처리 방식도 중요합니다.

---

#### 2. `diff()`

-   **핵심 개념**:
    `diff()` 메서드는 Series의 현재 값과 이전 값(기본적으로 1칸 전)의 차이를 계산합니다. 이는 시계열 데이터의 절대적인 변화량을 측정할 때 사용됩니다.

-   **코드/수식 해설**:

    *   `s.diff(1)`: 현재 값과 1칸 전 값의 차이를 계산합니다.
        ```python
        s.diff(1) # == s - s.shift(1)
        # t0     NaN
        # t1    10.0  (110 - 100)
        # t2    11.0  (121 - 110)
        # dtype: float64
        ```
        수식적으로는 $S_t - S_{t-1}$ 과 같습니다.
        `t0`에는 이전 값이 없으므로 `NaN`이 됩니다.

    *   `s.diff(2)`: 현재 값과 2칸 전 값의 차이를 계산합니다.
        ```python
        s.diff(2) # difference vs. two steps back
        # t0     NaN
        # t1     NaN
        # t2    21.0  (121 - 100)
        # dtype: float64
        ```
        수식적으로는 $S_t - S_{t-2}$ 과 같습니다.
        `t0`, `t1`에는 2칸 전 값이 없으므로 `NaN`이 됩니다.

-   **구체적 예시**:
    일별 주식 종가 데이터가 있을 때, `s.diff(1)`은 '일일 변동폭'을 나타냅니다. 예를 들어, 어제 100원, 오늘 110원이라면, `diff(1)` 결과는 10원이 됩니다.

-   **시험 포인트**:
    ⭐ `diff(n)`은 현재 값에서 `n` 칸 이전 값을 뺀다는 것을 기억하세요. `NaN`이 발생하는 위치를 이해하는 것이 중요합니다.

---

#### 3. `pct_change()`

-   **핵심 개념**:
    `pct_change()` 메서드는 Series의 현재 값과 이전 값(기본적으로 1칸 전)의 **백분율 변화**를 계산합니다. 이는 데이터의 상대적인 변화율을 측정할 때 사용됩니다.

-   **코드/수식 해설**:

    *   `s.pct_change(1)`: 현재 값과 1칸 전 값의 백분율 변화를 계산합니다.
        ```python
        s.pct_change(1) # == (s / s.shift(1)) - 1
        # t0     NaN
        # t1    0.10  (110/100 - 1)
        # t2    0.10  (121/110 - 1)
        # dtype: float64
        ```
        수식적으로는 다음과 같습니다:
        $$ \frac{S_t - S_{t-1}}{S_{t-1}} = \frac{S_t}{S_{t-1}} - 1 $$
        `t0`에는 이전 값이 없으므로 `NaN`이 됩니다.

-   **구체적 예시**:
    일별 주식 종가 데이터에서 `s.pct_change(1)`은 '일일 수익률'을 나타냅니다. 어제 100원, 오늘 110원이라면, `pct_change(1)` 결과는 (110-100)/100 = 0.10 (즉, 10% 상승)이 됩니다.

-   **시험 포인트**:
    ⭐ `pct_change(n)`은 현재 값과 `n` 칸 이전 값 사이의 백분율 변화를 계산하며, 금융 데이터 분석에서 수익률을 계산하는 데 매우 중요하게 사용됩니다. 분모가 0이 될 경우 `inf` 또는 `NaN`이 될 수 있다는 점도 염두에 두어야 합니다.

---

---

## Slide 30

**핵심 개념**

*   **`s.where(cond, other)`**: `pd.Series` 객체 `s`에 대해 조건 `cond`가 참(True)인 위치의 값은 `s`의 원래 값을 유지하고, 조건이 거짓(False)인 위치의 값은 `other`로 지정된 값으로 대체하여 새로운 Series를 반환합니다. 데이터 필터링 및 조건부 값 변경에 사용됩니다.
*   **`s.mask(cond, other)`**: `s.where()`와 정확히 반대되는 동작을 합니다. 조건 `cond`가 참(True)인 위치의 값은 `other`로 대체하고, 조건이 거짓(False)인 위치의 값은 `s`의 원래 값을 유지하여 새로운 Series를 반환합니다. 특정 조건을 만족하는 값들을 가리거나 제거할 때 유용합니다.
*   **`s.clip(lower, upper)`**: `pd.Series`의 각 값을 지정된 하한 `lower`와 상한 `upper` 범위 내로 제한합니다. 즉, `lower`보다 작은 값은 `lower`로, `upper`보다 큰 값은 `upper`로 조정하고, 범위 내의 값은 그대로 유지합니다. 데이터의 이상치를 처리하거나 값의 범위를 정규화할 때 사용됩니다.
*   **`s.replace(to_replace, value)`**: `pd.Series` 내에서 특정 값(또는 값들) `to_replace`를 다른 값 `value`로 변경합니다. 데이터 정제, 범주형 변수 인코딩, 누락된 값 처리 등 다양한 데이터 전처리 작업에 활용됩니다.

**코드/수식 해설**

```python
import pandas as pd
import numpy as np

# 예시 Series 생성
s = pd.Series([10, 20, 30, 40, 50, 60, 70])
print("Original Series:\n", s)

# s.where(cond, other)
# s > 40인 경우 원래 값 유지, 그렇지 않으면 0으로 대체
s_where = s.where(s > 40, 0)
print("\ns.where(s > 40, 0):\n", s_where)
# 결과: [ 0,  0,  0,  0, 50, 60, 70]

# s.mask(cond, other)
# s > 40인 경우 0으로 대체, 그렇지 않으면 원래 값 유지
s_mask = s.mask(s > 40, 0)
print("\ns.mask(s > 40, 0):\n", s_mask)
# 결과: [10, 20, 30, 40,  0,  0,  0]

# s.clip(lower, upper)
# 값의 범위를 25와 65 사이로 제한
s_clip = s.clip(lower=25, upper=65)
print("\ns.clip(lower=25, upper=65):\n", s_clip)
# 결과: [25, 25, 30, 40, 50, 60, 65]

# 수식 해설 (s.clip): 각 원소 $x_i$에 대해
# lower <= upper를 가정합니다.
# clip_value(x_i) = max(lower, min(x_i, upper))
# 또는 다음과 같이 표현할 수 있습니다:
# $$
# \text{clip}(x_i) = \begin{cases}
# \text{lower} & \text{if } x_i < \text{lower} \\
# x_i & \text{if } \text{lower} \le x_i \le \text{upper} \\
# \text{upper} & \text{if } x_i > \text{upper}
# \end{cases}
# $$

# s.replace(to_replace, value)
# 30을 300으로, 50을 500으로 변경
s_replace = s.replace({30: 300, 50: 500})
print("\ns.replace({30: 300, 50: 500}):\n", s_replace)
# 결과: [ 10,  20, 300,  40, 500,  60,  70]
```

**구체적 예시**

*   **`s.where()`**: 학생들의 시험 점수 Series가 있을 때, `점수.where(점수 >= 60, 'F')`를 사용하면 60점 이상은 점수를 그대로 두고 60점 미만은 'F'로 대체하여 합격/불합격 여부를 표시할 수 있습니다.
*   **`s.mask()`**: 센서 데이터 Series가 있을 때, `데이터.mask(데이터.isna(), 0)`를 사용하면 누락된 값(NaN)을 0으로 대체하고 정상적인 값은 유지할 수 있습니다.
*   **`s.clip()`**: 어떤 제품의 가격 데이터가 있을 때, `가격.clip(lower=1000, upper=10000)`를 사용하면 1000원 미만의 가격은 1000원으로, 10000원 초과의 가격은 10000원으로 제한하여 비정상적인 가격 데이터를 정제할 수 있습니다.
*   **`s.replace()`**: 설문조사 응답 Series에 '매우 좋음', '좋음', '보통', '나쁨', '매우 나쁨'과 같은 문자열이 있을 때, `응답.replace({'매우 좋음': 5, '좋음': 4, '보통': 3, '나쁨': 2, '매우 나쁨': 1})`을 통해 이를 숫자로 인코딩하여 통계 분석에 활용할 수 있습니다.

**시험 포인트**

*   ⭐ **`s.where()`와 `s.mask()`의 차이점**: `where`는 조건이 True일 때 원본 값을 유지하고, `mask`는 조건이 True일 때 `other` 값으로 대체합니다. 즉, 서로 반대되는 동작을 합니다. 이 둘의 사용법과 결과를 명확히 구분할 수 있어야 합니다.
*   ⭐ **`s.clip()`**: 데이터의 범위를 특정 구간으로 제한(Clamp)하는 중요한 전처리 기법입니다. 이상치(Outlier)를 특정 값으로 고정하거나 데이터 스케일링 전 단계에서 활용될 수 있습니다. `lower` 또는 `upper` 중 하나만 지정할 수도 있음을 알아두세요.
*   ⭐ **`s.replace()`**: 단일 값, 리스트, 딕셔너리 등 다양한 형태로 `to_replace`와 `value` 인자를 지정하여 복잡한 값 매핑을 수행할 수 있다는 점을 이해하는 것이 중요합니다. 특히 딕셔너리 형태의 매핑은 실무에서 매우 자주 사용됩니다.

---

## Slide 31

**핵심 개념**
이 슬라이드는 pandas Series 객체에서 데이터를 조건부로 처리하거나 값을 변경하는 네 가지 중요한 메서드인 `where`, `mask`, `clip`, `replace`를 소개합니다.

*   **`Series.where(condition, other)`**: `condition`이 `True`인 경우 원본 Series의 값을 유지하고, `False`인 경우 `other`로 지정된 값으로 대체합니다.
*   **`Series.mask(condition, other)`**: `condition`이 `True`인 경우 `other`로 지정된 값으로 대체하고, `False`인 경우 원본 Series의 값을 유지합니다. 이는 `where` 메서드와 반대되는 동작을 합니다.
*   **`Series.clip(lower, upper)`**: Series의 값을 지정된 `lower` 및 `upper` 경계 내로 제한(클리핑)합니다. `lower`보다 작은 값은 `lower`로, `upper`보다 큰 값은 `upper`로 변경됩니다.
*   **`Series.replace(to_replace, value)`**: Series 내의 특정 값(들)을 다른 값으로 대체합니다. 단일 값, 리스트, 딕셔너리 등 다양한 형태로 `to_replace` 인자를 지정할 수 있습니다.

**코드/수식 해설**

```python
import pandas as pd

# 1. Series s 초기 설정
s = pd.Series([5, -2, 7, -1, 9], index=list("abcde"))
# s_output:
# a    5
# b   -2
# c    7
# d   -1
# e    9

# 2. where: s의 값이 0 이상인 경우(True) 원본 값을 유지하고, 그렇지 않은 경우(False) 0으로 대체합니다.
s_where = s.where(s >= 0, 0)
# s_where_output:
# a    5 (5 >= 0 -> True, keep 5)
# b    0 (-2 >= 0 -> False, replace with 0)
# c    7 (7 >= 0 -> True, keep 7)
# d    0 (-1 >= 0 -> False, replace with 0)
# e    9 (9 >= 0 -> True, keep 9)

# 3. mask: s의 값이 0 미만인 경우(True) 0으로 대체하고, 그렇지 않은 경우(False) 원본 값을 유지합니다.
# mask는 where의 역 연산으로, condition이 True인 곳을 '마스크'해서 대체합니다.
s_mask = s.mask(s < 0, 0)
# s_mask_output:
# a    5 (5 < 0 -> False, keep 5)
# b    0 (-2 < 0 -> True, replace with 0)
# c    7 (7 < 0 -> False, keep 7)
# d    0 (-1 < 0 -> True, replace with 0)
# e    9 (9 < 0 -> False, keep 9)

# 4. clip: s의 값을 [0, 6] 범위 내로 제한합니다.
# 0보다 작은 값은 0으로, 6보다 큰 값은 6으로 변경됩니다.
s_clip = s.clip(lower=0, upper=6)
# s_clip_output:
# a    5 (5 is in [0, 6], keep 5)
# b    0 (-2 is < 0, replace with 0)
# c    6 (7 is > 6, replace with 6)
# d    0 (-1 is < 0, replace with 0)
# e    6 (9 is > 6, replace with 6)

# 5. replace: 특정 값들을 다른 값으로 대체합니다.
# 여기서는 딕셔너리를 사용하여 -2를 0으로, -1을 0으로 한 번에 대체합니다.
s_repl = s.replace({-2: 0, -1: 0})
# s_repl_output:
# a    5 (no change)
# b    0 (-2 replaced with 0)
# c    7 (no change)
# d    0 (-1 replaced with 0)
# e    9 (no change)
```

**구체적 예시**

학생들의 시험 점수 Series `grades = pd.Series([85, 45, 92, 60, 30])`가 있다고 가정해 봅시다.

1.  **`where` 활용**: 60점 이상인 점수만 유지하고, 60점 미만은 '재시험'을 의미하는 0점으로 처리하고 싶을 때:
    `grades.where(grades >= 60, 0)`
    결과: `[85, 0, 92, 60, 0]`

2.  **`mask` 활용**: 60점 미만인 점수만 '재시험'을 의미하는 0점으로 바꾸고 싶을 때:
    `grades.mask(grades < 60, 0)`
    결과: `[85, 0, 92, 60, 0]` (위의 `where`와 동일한 결과지만, 조건의 관점이 반대입니다.)

3.  **`clip` 활용**: 점수를 최소 40점, 최대 100점으로 제한하고 싶을 때 (예: 40점 미만은 40점으로, 100점 초과는 100점으로 처리):
    `grades.clip(lower=40, upper=100)`
    결과: `[85, 45, 92, 60, 40]` (30점은 40점으로 상향 조정됨)

4.  **`replace` 활용**: 특정 점수 '45'를 '50'으로, '30'을 '40'으로 변경하고 싶을 때:
    `grades.replace({45: 50, 30: 40})`
    결과: `[85, 50, 92, 60, 40]`

**시험 포인트**

*   ⭐ **`where`와 `mask`의 차이점**: `where`는 조건이 `True`일 때 값을 유지하고, `mask`는 조건이 `True`일 때 값을 대체합니다. 서로 조건의 해석이 반대라는 점을 정확히 이해하고 있어야 합니다. (`s.where(cond, other)` vs `s.mask(cond, other)`)
*   ⭐ **`clip`의 동작 방식**: `lower`와 `upper` 인자를 사용하여 어떻게 값을 특정 범위 내로 제한하는지 (경계값 포함) 알아두세요.
*   ⭐ **`replace`의 유연성**: 단일 값 대체, 리스트를 이용한 다중 값 대체, 딕셔너리를 이용한 매핑 기반 대체 등 다양한 `replace` 사용법을 숙지하세요. 특히 딕셔너리를 사용한 다중 값 교체가 유용합니다.
*   이러한 메서드들은 기본적으로 새로운 Series 객체를 반환하며, 원본 Series를 직접 수정하지 않습니다 (immutable by default).

---

## Slide 32

**핵심 개념**
이 슬라이드는 pandas Series 객체에서 데이터를 변환하거나 다른 형식으로 추출하는 세 가지 핵심 메서드인 `s.map()`, `s.astype()`, `s.to_numpy()`에 대해 설명합니다.

1.  **`s.map(func | dict)`**: Series의 각 원소에 함수를 적용하거나, 딕셔너리를 사용하여 원소를 다른 값으로 매핑합니다. 결과는 원본 인덱스를 보존하는 새로운 pandas Series입니다. 딕셔너리에 매치되지 않는 키는 `NaN`이 됩니다.
2.  **`s.astype(dtype)`**: Series의 모든 원소를 지정된 새로운 데이터 타입(`dtype`)으로 변환합니다. 변환 결과는 새로운 pandas Series입니다. 변환이 불가능할 경우 기본적으로 오류가 발생합니다.
3.  **`s.to_numpy(copy=False)`**: Series의 값들을 NumPy 배열(`np.ndarray`)로 변환합니다. 이는 `s.values`보다 더 권장되는 방법이며, 특히 pandas의 확장 데이터 타입(Extension dtypes)과 일관성 있게 작동합니다.

**코드/수식 해설**

1.  **`s.map()`**
    *   `s.map(func)`: Series의 각 원소 `x`에 대해 `func(x)`를 적용합니다.
    *   `s.map(dict)`: Series의 원소를 딕셔너리의 키로 사용하여 해당 값으로 매핑합니다.
    ```python
    import pandas as pd
    import numpy as np

    s = pd.Series([1, 2, 3, 4, 5])

    # 람다 함수를 사용하여 각 원소에 10을 곱하기
    s_mapped_func = s.map(lambda x: x * 10)
    print("s_mapped_func:\n", s_mapped_func)

    # 딕셔너리를 사용하여 값 매핑
    # 딕셔너리에 없는 키(4, 5)는 NaN으로 처리됨
    mapping_dict = {1: 'One', 2: 'Two', 3: 'Three'}
    s_mapped_dict = s.map(mapping_dict)
    print("\ns_mapped_dict:\n", s_mapped_dict)

    # NaN 값 채우기
    s_mapped_dict_filled = s_mapped_dict.fillna('Unknown')
    print("\ns_mapped_dict_filled:\n", s_mapped_dict_filled)
    ```

2.  **`s.astype(dtype)`**
    *   `s.astype(dtype)`: `dtype`은 'float64', 'int64', 'Int64' (nullable integer), 'string', 'bool' 등 원하는 데이터 타입 문자열이나 NumPy/Python 타입입니다.
    ```python
    import pandas as pd
    import numpy as np

    s_str = pd.Series(['10', '20', '30.5', '40'])
    s_mix = pd.Series([1, 2, '3', np.nan]) # Mixed type, and contains NaN

    # 문자열 Series를 float64로 변환
    s_to_float = s_str.astype('float64')
    print("s_to_float:\n", s_to_float)

    # NaN이 포함될 수 있는 정수형 ('Int64'는 pandas의 nullable integer dtype)
    # pd.to_numeric을 사용하면 변환 불가능한 값은 NaN으로 처리할 수 있습니다.
    s_converted_numeric = pd.to_numeric(s_mix, errors='coerce').astype('Int64')
    print("\ns_converted_numeric (with NaN as Int64):\n", s_converted_numeric)

    # 주의: 슬라이드에 'errors="ignore" to skip' 언급이 있지만, s.astype() 메서드 자체에는 errors 인자가 없습니다.
    # 변환 실패 시 에러가 발생하며, 이를 피하려면 pd.to_numeric()의 errors='coerce' 옵션을 활용해야 합니다.
    # 예시: pd.to_numeric(s_invalid, errors='coerce')
    ```

3.  **`s.to_numpy()`**
    *   `s.to_numpy(copy=False)`: Series의 값들을 NumPy 배열로 반환합니다. `copy=False`는 가능한 경우 원본 데이터를 복사하지 않고 뷰(view)를 반환하여 메모리 효율성을 높입니다.
    ```python
    import pandas as pd
    import numpy as np

    s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

    # Series를 NumPy 배열로 변환
    numpy_array = s.to_numpy()
    print("numpy_array:\n", numpy_array)
    print("Type of numpy_array:", type(numpy_array))

    # Extension dtype Series를 NumPy 배열로 변환
    s_nullable_int = pd.Series([1, 2, np.nan, 4], dtype='Int64')
    numpy_array_nullable = s_nullable_int.to_numpy()
    print("\nnumpy_array_nullable (from nullable Int64 Series):\n", numpy_array_nullable)
    print("Type of numpy_array_nullable:", type(numpy_array_nullable))
    ```

**구체적 예시**

*   **`s.map()`**:
    *   **실생활 비유**: 시험 점수 Series가 있을 때, 각 점수를 등급(A, B, C...)으로 매기기 위해 딕셔너리(`{90: 'A', 80: 'B', ...}`)를 `map`에 전달하거나, 점수에 따라 가산점을 부여하는 함수를 `map`에 적용할 수 있습니다.
    *   **동작 예시**: `pd.Series(['M', 'F', 'M', 'O']).map({'M': 'Male', 'F': 'Female', 'O': 'Other'})`는 성별 코드를 완전한 단어로 변환합니다.

*   **`s.astype()`**:
    *   **실생활 비유**: 엑셀에서 숫자로 입력된 데이터가 실제로는 텍스트 형식으로 저장되어 있어 계산이 안 될 때, 이를 숫자 형식으로 변경하는 것과 유사합니다.
    *   **동작 예시**: 웹 크롤링 등으로 얻은 가격 데이터 Series (`pd.Series(['1000', '2500', '300.5'])`)를 `astype('float64')`로 변환하여 실제 숫자 계산에 활용할 수 있습니다. 결측치(NaN)를 포함하는 정수형 데이터를 다룰 때는 `Int64`와 같은 pandas Extension dtype으로 변환하여 오류 없이 처리할 수 있습니다.

*   **`s.to_numpy()`**:
    *   **실생활 비유**: DataFrame이나 Series는 표 형태의 데이터를 다루는 데 최적화되어 있지만, 데이터를 특정 공식에 넣어 계산하거나 머신러닝 모델에 학습시킬 때는 일반적으로 순수한 숫자 배열 형태가 필요합니다. `to_numpy()`는 이러한 "계산용 원본 데이터"를 꺼내는 과정입니다.
    *   **동작 예시**: Scikit-learn 라이브러리의 선형 회귀 모델 `LinearRegression().fit(X_df.to_numpy(), y_series.to_numpy())`처럼, pandas 객체를 머신러닝 모델의 입력으로 사용하기 전에 `to_numpy()`를 통해 NumPy 배열로 변환해야 합니다.

**시험 포인트**

*   ⭐ `s.map()`은 Series의 **개별 원소에 대한 변환 또는 매핑**에 사용되며, 함수와 딕셔너리 모두 인자로 받을 수 있습니다. 딕셔너리 매핑 시 매치되지 않는 값은 `NaN`이 된다는 점을 기억하고, `fillna()`와 함께 활용하는 방법을 알아두세요.
*   ⭐ `s.astype()`은 Series 전체의 **데이터 타입을 변경**하는 데 사용됩니다. 변환이 불가능할 경우 오류가 발생하며, `NaN`을 포함할 수 있는 정수형을 다룰 때는 `int64` 대신 **`Int64` (대문자 I)**와 같은 pandas Extension dtype을 사용해야 합니다. (슬라이드에 언급된 `errors='ignore'`는 `s.astype()` 자체의 인자가 아니므로 혼동하지 않도록 주의하세요. 대신 `pd.to_numeric(..., errors='coerce')`를 활용할 수 있습니다.)
*   ⭐ `s.to_numpy()`는 Series의 데이터를 **NumPy 배열로 추출**하는 공식적이고 권장되는 방법입니다. `s.values`보다 확장 데이터 타입(Extension dtypes)에 대해 더 일관된 동작을 보여줍니다. ⭐ 머신러닝 라이브러리와 같은 NumPy 기반의 도구에 데이터를 전달할 때 반드시 필요한 과정입니다.

---

## Slide 33

## 데이터 분석 입문 (CSED226) - Pandas 데이터 조작: map, astype, to_numpy

### 핵심 개념

*   **`Series.map(mapper)`**: `pandas.Series`의 각 값에 대해 매핑 함수나 딕셔너리를 적용하여 값을 변환합니다. `mapper`에 존재하지 않는 키에 해당하는 값은 `NaN`으로 처리됩니다.
*   **`Series.fillna(value)`**: `pandas.Series` 내의 결측치(`NaN`)를 특정 값으로 채웁니다.
*   **`Series.astype(dtype)`**: `pandas.Series`의 데이터 타입을 변경합니다. 예를 들어, 정수를 실수로, 또는 문자열을 특정 타입으로 변환할 때 사용됩니다.
*   **`Series.to_numpy(copy=False)`**: `pandas.Series`를 NumPy 배열(ndarray)로 변환합니다. `copy=False` 인자는 가능한 경우 데이터를 복사하지 않고 원본 데이터에 대한 뷰를 반환하여 메모리 효율성을 높입니다.

### 코드/수식 해설

이 슬라이드에서는 명시적인 수학 수식이 제시되지 않으며, 주로 Pandas 라이브러리의 데이터 조작 메서드 사용법을 다룹니다.

```python
import pandas as pd

# 1. 딕셔너리 정의: 국가 코드(key)를 국가 이름(value)으로 매핑
code2name = {'US':'United States', 'KR':'Korea'}

# 2. 국가 코드를 포함하는 pandas Series 생성
country = pd.Series(['US', 'KR', 'XX'])

# 3. Series.map()을 사용하여 코드2이름 딕셔너리에 따라 국가 코드 변환
#    'XX'는 딕셔너리에 없으므로 NaN이 됨
# 4. .fillna('Unknown')을 사용하여 NaN 값을 'Unknown'으로 채움
country_name = country.map(code2name).fillna('Unknown')
# 결과:
# 0    United States
# 1            Korea
# 2          Unknown
# dtype: object

# 5. 숫자 값을 포함하고, 사용자 정의 인덱스를 갖는 pandas Series 's' 생성
s = pd.Series([5, 2, 7], index=list('abc'))
# 6. .astype('float64')를 사용하여 Series 's'의 데이터 타입을 float64(실수)로 변경
s = s.astype('float64')
# 결과:
# a    5.0
# b    2.0
# c    7.0
# dtype: float64

# 7. Series 's'를 NumPy 배열 'a'로 변환
#    copy=False는 가능한 경우 데이터 복사 없이 뷰를 반환하려고 시도
a = s.to_numpy(copy=False)
# 결과:
# array([5., 2., 7.])
```

### 구체적 예시

*   **`map` 및 `fillna`**: 설문조사 응답에서 '1'은 '매우 만족', '2'는 '만족' 등으로 인코딩된 데이터를 사람이 읽기 쉬운 형태로 변환할 때 `map`을 사용할 수 있습니다. 만약 응답 중 '99'와 같이 정의되지 않은 코드가 있다면 `fillna`를 사용하여 '기타'나 '응답 없음'으로 처리할 수 있습니다. 예를 들어, `pd.Series([1, 2, 99]).map({1: '매우 만족', 2: '만족'}).fillna('기타')`와 같이 활용됩니다.
*   **`astype`**: 데이터 분석 과정에서 숫자형 데이터를 계산에 사용하기 위해 `object` 타입의 문자열 숫자를 `int`나 `float`으로 변환하거나, 메모리 효율성을 위해 `float64`를 `float32`로 변경할 때 유용합니다.
*   **`to_numpy`**: 머신러닝 모델에 데이터를 입력할 때, 많은 라이브러리(예: scikit-learn, TensorFlow, PyTorch)는 Pandas Series나 DataFrame이 아닌 NumPy 배열 형태의 입력을 요구합니다. 이때 `to_numpy()`를 사용하여 데이터를 쉽게 변환할 수 있습니다.

### 시험 포인트

*   ⭐ **`map()`과 `apply()`의 차이점**: `map()`은 Series의 요소별 변환에 최적화되어 있고 주로 딕셔너리나 Series, 또는 단일 인자를 받는 함수를 적용할 때 사용됩니다. 반면 `apply()`는 Series나 DataFrame의 행/열에 더 복잡한 함수를 적용할 때 유연하게 사용될 수 있습니다. (DataFrame에 딕셔너리 매핑을 할 때는 `replace`나 `apply`를 고려할 수 있습니다.)
*   ⭐ **`fillna()`의 다양한 활용**: `fillna()`는 스칼라 값, 딕셔너리, Series 등 다양한 방식으로 결측치를 채울 수 있으며, `method='ffill'` (앞의 값으로 채우기) 또는 `method='bfill'` (뒤의 값으로 채우기)과 같은 옵션도 중요합니다.
*   ⭐ **데이터 타입의 중요성 및 `astype()`의 역할**: 데이터 분석에서 올바른 데이터 타입은 계산의 정확성, 메모리 사용 효율성, 그리고 특정 연산 가능성에 영향을 미칩니다. `astype()`을 통해 명시적으로 타입을 변환하는 방법은 매우 중요합니다.
*   ⭐ **`to_numpy(copy=False)`의 의미**: `copy=False`는 불필요한 메모리 복사를 방지하여 성능을 최적화할 수 있지만, 원본 Series의 데이터가 변경되면 NumPy 배열도 함께 변경될 수 있음을 의미합니다. (원본 데이터 보호가 필요하면 `copy=True` 또는 명시적으로 복사해야 합니다.)

---

## Slide 34

**핵심 개념**

Pandas Series에서 특정 데이터 타입(문자열, 날짜/시간, 범주형)에 특화된 연산을 벡터화된 방식으로 수행할 수 있도록 해주는 특별한 접근자(Accessor)들입니다. 이 접근자들은 일반적인 파이썬 메서드를 시리즈의 각 요소에 효율적으로 적용할 수 있게 돕습니다.

1.  **`.str` Accessor**: Series의 각 요소가 문자열(string) 또는 객체(object) 타입일 때, 문자열 관련 메서드(예: `strip()`, `lower()`, `split()`, `contains()`, `extract()`)를 벡터화된 방식으로 적용할 수 있게 합니다. 이는 파이썬의 기본 `str` 메서드와 유사하지만, 시리즈 전체에 대해 한 번에 연산을 수행하여 성능을 향상시킵니다.
2.  **`.dt` Accessor**: Series의 각 요소가 날짜/시간(datetime) 타입일 때, 날짜/시간의 구성 요소(예: `year`, `month`, `day`, `hour`)를 추출하거나, 날짜/시간에 특화된 연산(예: `to_period()`, `floor()`, `ceil()`, `day_name()`)을 수행할 수 있게 합니다.
3.  **`.cat` Accessor**: Series의 각 요소가 범주형(category) 타입일 때, 범주(category)를 관리하는 메서드(예: `add_categories()`, `remove_categories()`, `reorder_categories()`, `codes`, `as_ordered()`)를 제공합니다. 범주형 데이터는 메모리 효율성을 높이고, 특정 머신러닝 알고리즘에 적합한 형태로 데이터를 표현하는 데 유용합니다.

**코드/수식 해설**

*   **`.str` Accessor**
    ```python
    import pandas as pd

    s_str = pd.Series(['  apple ', 'bAnana  ', ' cherry pie '])

    # 공백 제거 및 소문자로 변환
    cleaned_s_str = s_str.str.strip().str.lower()
    print("Cleaned strings:\n", cleaned_s_str)

    # 특정 문자열 포함 여부 확인
    contains_an = s_str.str.contains('an', case=False) # 대소문자 무시
    print("\nContains 'an':\n", contains_an)

    # 특정 구분자로 분리 (리스트 Series 반환)
    parts = s_str.str.split(' ')
    print("\nSplit by space:\n", parts)
    ```

*   **`.dt` Accessor**
    ```python
    import pandas as pd

    s_dt = pd.Series(pd.to_datetime(['2023-01-15 10:30', '2024-02-29 14:00', '2023-07-01 08:00']))

    # 연도, 월, 요일 이름 추출
    years = s_dt.dt.year
    months = s_dt.dt.month
    day_names = s_dt.dt.day_name()
    print("Years:\n", years)
    print("\nMonths:\n", months)
    print("\nDay Names:\n", day_names)

    # 윤년 여부 확인
    is_leap = s_dt.dt.is_leap_year
    print("\nIs Leap Year:\n", is_leap)

    # 날짜를 월 단위로 내림 (Floor)
    floored_date = s_dt.dt.floor('M')
    print("\nFloored to Month:\n", floored_date)
    ```

*   **`.cat` Accessor**
    ```python
    import pandas as pd

    s_cat = pd.Series(['Small', 'Medium', 'Small', 'Large', 'Medium']).astype('category')
    print("Original categories:\n", s_cat.cat.categories)

    # 새로운 범주 추가 (기존 데이터에 없더라도 추가 가능)
    s_cat = s_cat.cat.add_categories('X-Large')
    print("\nCategories after adding 'X-Large':\n", s_cat.cat.categories)

    # 범주 순서 변경 (ordered=True로 변경 시 순서가 의미를 가짐)
    s_cat_ordered = s_cat.cat.reorder_categories(['Small', 'Medium', 'Large', 'X-Large'], ordered=True)
    print("\nReordered categories:\n", s_cat_ordered.cat.categories)

    # 범주를 숫자 코드로 변환 (머신러닝 모델 입력 시 유용)
    codes = s_cat_ordered.cat.codes
    print("\nCategorical codes:\n", codes)
    ```

**구체적 예시**

1.  **`.str` 예시**: 온라인 쇼핑몰의 사용자 리뷰 데이터가 있다고 가정해 봅시다. 리뷰 텍스트 컬럼에 사용자들이 대소문자를 섞어 쓰고, 불필요한 공백을 추가하는 경우가 많습니다. `reviews.str.lower().str.strip()`를 사용하여 모든 리뷰를 소문자로 통일하고 앞뒤 공백을 제거함으로써 텍스트를 정규화할 수 있습니다. 또한, `reviews.str.contains('불만')`을 사용하여 '불만'이라는 단어가 포함된 리뷰를 쉽게 찾아낼 수 있습니다.
2.  **`.dt` 예시**: 고객 주문 데이터에 `order_date` 컬럼이 datetime 타입으로 있다고 가정해 봅시다. `order_date.dt.year`와 `order_date.dt.month`를 사용하여 연간/월간 매출을 집계하거나, `order_date.dt.day_name()`을 통해 요일별 주문 패턴을 분석할 수 있습니다. 특정 요일(예: 주말)에 프로모션을 진행하는 것이 효과적인지 판단하는 데 활용될 수 있습니다.
3.  **`.cat` 예시**: 설문조사 응답에 '매우 불만', '불만', '보통', '만족', '매우 만족'과 같은 Likert 척도 데이터가 있다고 가정해 봅시다. 이를 `pd.Series(['만족', '불만', '매우 만족']).astype('category')`로 변환하고 `reorder_categories`를 사용하여 '매우 불만'부터 '매우 만족'까지 순서를 지정하면, 데이터가 차지하는 메모리를 줄일 수 있을 뿐만 아니라, 순서가 있는 범주형 데이터로 인식되어 분석 및 일부 머신러닝 모델에서 더 의미 있게 사용될 수 있습니다. 만약 데이터에 `pd.Series(['매우 불만', '불만족'])`와 같이 '불만족'이 들어왔는데 기존 카테고리에 없다면, 기본적으로 `NaN`으로 처리되므로, 미리 `add_categories`로 추가해 주어야 합니다.

**시험 포인트**

*   ⭐ **각 접근자의 목적과 적용 대상 데이터 타입을 정확히 이해하는 것이 중요합니다.**
    *   `.str`: 문자열 (string/object dtype)
    *   `.dt`: 날짜/시간 (datetime dtype)
    *   `.cat`: 범주형 (category dtype)
*   ⭐ **`s.str.method()` 형태는 파이썬 `str.method()`와 달리 시리즈의 모든 요소에 벡터화된 연산을 적용한다는 점을 명확히 알아야 합니다.** 이는 효율성 면에서 큰 이점을 가집니다.
*   ⭐ **`.cat` 접근자는 반드시 해당 Series가 `category` dtype일 때만 사용 가능합니다.** 다른 타입의 Series에 `.cat`을 바로 사용하면 `AttributeError`가 발생합니다.
*   ⭐ **범주형 데이터의 활용 목적:** 메모리 효율성, 특정 머신러닝 알고리즘에 적합한 데이터 표현 방식 (예: 순서 유무 지정), 유효한 범주 목록 관리 등을 이해해야 합니다.
*   ⭐ **`.cat`에서 범주는 고정(fixed)되어 있으므로, 새로운 범주 값을 추가하려면 `add_categories()` 메서드를 사용해야 합니다.** 그렇지 않으면 `NaN`으로 처리될 수 있습니다.

---

## Slide 35

---

### pandas Series Accessor (.str, .dt, .cat) 활용

이 슬라이드는 pandas Series 객체에 대해 문자열 (`.str`), 날짜/시간 (`.dt`), 그리고 범주형 (`.cat`) 데이터를 효율적으로 다루기 위한 특별한 접근자(accessor)들을 소개합니다. 이 접근자들은 Series의 각 요소에 대해 벡터화된(vectorized) 연산을 가능하게 하여, 반복문 없이 빠르고 간결하게 데이터를 처리할 수 있도록 돕습니다.

---

**핵심 개념**

*   **벡터화된 연산 (Vectorized Operations)**: pandas Series의 각 요소에 대해 파이썬의 `for` 루프 없이 한 번의 연산으로 작업을 수행하는 방식입니다. 이는 성능을 향상시키고 코드를 간결하게 만듭니다.
*   **`.str` 접근자**: `dtype`이 `string` (또는 `object`)인 Series의 요소들에 대해 문자열 메서드(예: `strip()`, `lower()`, `split()`)를 적용할 수 있게 합니다.
*   **`.dt` 접근자**: `dtype`이 `datetime` 또는 `Period`인 Series의 요소들에 대해 날짜/시간 관련 속성(예: `year`, `month`)이나 메서드(예: `to_period()`)를 추출하거나 변환할 수 있게 합니다.
*   **`.cat` 접근자**: `dtype`이 `category`인 Series의 요소들에 대해 범주형 데이터의 속성(예: `categories`)을 관리하거나 메서드(예: `add_categories()`, `remove_unused_categories()`)를 적용할 수 있게 합니다. 범주형 데이터는 메모리 효율성과 특정 통계 및 머신러닝 알고리즘에서 유용합니다.

---

**코드/수식 해설**

```python
import pandas as pd

# .str 접근자 예시: 이메일 도메인 추출
email = pd.Series(['A@X.com', 'B@Y.com', None], dtype='string')
# 문자열 공백 제거 -> 소문자 변환 -> '@' 기준으로 분리 -> 분리된 리스트의 마지막 요소(도메인) 추출
domain = email.str.strip().str.lower().str.split('@').str[-1]
# 출력:
# 0    x.com
# 1    y.com
# 2     <NA>
# dtype: string

# .dt 접근자 예시: 날짜/시간 정보 추출 및 변환
dt = pd.to_datetime(pd.Series(['2025-09-01', '2025-09-12']))
# 날짜에서 연도만 추출
years = dt.dt.year
# 출력:
# 0    2025
# 1    2025
# dtype: int64
# 날짜를 월(M) 단위의 기간(Period)으로 변환
periods = dt.dt.to_period('M')
# 출력:
# 0    2025-09
# 1    2025-09
# dtype: period[M]

# .cat 접근자 예시: 범주형 데이터 관리
cat = pd.Series(['a', 'b', 'a'], dtype='category')
# 기존 범주에 'c'를 추가 (데이터에는 없지만, 가능한 범주로 등록)
cat = cat.cat.add_categories(['c'])
# # add an unused 'c'
# 실제 데이터에 사용되지 않는 범주('c')를 제거
cat2 = cat.cat.remove_unused_categories()
# 출력:
# 0    a
# 1    b
# 2    a
# dtype: category
# Categories (2, object): ['a', 'b']  # 'c' 범주가 제거됨을 확인
```

---

**구체적 예시**

*   **`.str`**:
    *   **텍스트 데이터 클리닝**: 사용자 입력 필드에서 공백을 제거하거나, 모든 텍스트를 소문자로 통일하여 검색 및 분석의 일관성을 확보할 때 유용합니다.
    *   **정보 추출**: 파일 경로에서 파일 확장자를 추출하거나, 상품 코드에서 특정 식별 번호를 분리할 때 사용됩니다. 예를 들어, `filename_series.str.split('.').str[-1]`을 사용해 `.csv`, `.txt`와 같은 확장자를 쉽게 얻을 수 있습니다.
*   **`.dt`**:
    *   **시계열 데이터 분석**: 특정 월의 판매량 합계를 구하거나, 요일별 트래픽 변화를 분석하기 위해 날짜 데이터에서 월, 요일 등의 정보를 추출할 때 필수적입니다.
    *   **기간 계산**: 두 날짜 사이의 기간을 계산하거나, 특정 시간 단위(예: 분기, 연도)로 데이터를 집계할 때 사용됩니다.
*   **`.cat`**:
    *   **메모리 최적화**: 성별, 지역 코드 등 반복되는 문자열 데이터가 많은 경우 `category` dtype으로 변환하면 메모리 사용량을 크게 줄일 수 있습니다.
    *   **머신러닝 전처리**: 일부 머신러닝 알고리즘은 범주형 데이터를 특정 형식(예: 원-핫 인코딩)으로 요구하며, `category` dtype을 사용하면 이러한 전처리를 더 쉽게 관리할 수 있습니다. 또한, 학습 데이터에는 없는 범주를 추가하거나, 학습 데이터에만 있는 범주를 정리할 때 유용합니다.

---

**시험 포인트**

*   ⭐ **각 접근자(`.str`, `.dt`, `.cat`)가 어떤 `dtype`의 Series에 적용되며, 각각 어떤 종류의 연산을 수행하는지 명확히 이해해야 합니다.**
*   ⭐ **`.str`의 체이닝(Chaining) 기법 (예: `strip().lower().split('@').str[-1]`)을 통해 여러 문자열 연산을 한 줄로 효율적으로 수행하는 방법을 알아야 합니다.**
*   ⭐ **`.dt`를 사용하여 `datetime` 객체에서 연도, 월, 일 등의 속성을 추출하거나 `to_period()`와 같이 다른 시간 단위로 변환하는 방법을 숙지해야 합니다.**
*   ⭐ **`.cat`의 `add_categories()`와 `remove_unused_categories()` 메서드의 차이점과 사용 목적을 정확히 파악해야 합니다.** `add_categories()`는 데이터에는 없지만 가능한 범주를 추가하고, `remove_unused_categories()`는 데이터에 실제로 나타나지 않는 범주를 제거하여 범주 목록을 정리합니다.
*   ⭐ **이러한 접근자들이 왜 벡터화된 연산을 가능하게 하는지, 그리고 이로 인해 얻는 이점(성능, 코드 간결성)을 설명할 수 있어야 합니다.**

---

---

## Slide 36

## 데이터 분석 입문 (CSED226) - Windows: Rolling, Expanding, EWM

### 핵심 개념

*   **윈도우 함수 (Window Functions)**: 시계열 데이터나 순서가 있는 데이터에서 특정 '창'(window)을 정의하여 해당 창 내의 데이터에 통계 연산(평균, 합, 표준편차 등)을 적용하는 기법입니다. 데이터의 추세나 패턴을 분석하는 데 유용합니다.
*   **Rolling (이동 연산)**: 고정된 크기 `w`의 윈도우를 데이터 위로 이동시키면서 연산을 수행합니다. 주로 이동 평균(Moving Average), 이동 합(Moving Sum) 등에 사용됩니다.
*   **Expanding (확장 연산)**: 데이터의 시작점부터 현재 시점까지 점진적으로 윈도우의 크기를 늘려가며 연산을 수행합니다. 누적 합(Cumulative Sum), 누적 평균(Cumulative Mean) 등과 유사합니다.
*   **EWMA (Exponentially Weighted Moving Average, 지수 가중 이동 평균)**: 최근 데이터에 더 큰 가중치를 부여하여 계산하는 이동 평균입니다. 오래된 데이터일수록 가중치가 지수적으로 감소하여 최신 트렌드를 더 잘 반영합니다.

### 코드/수식 해설

*   **Rolling Mean (이동 평균)**
    *   Pandas 코드:
        ```python
        s.rolling(w, min_periods).mean()
        ```
        *   `w`: 윈도우의 크기(기간).
        *   `min_periods`: 윈도우 내 최소 관측치 수. 이 값보다 적은 데이터가 윈도우에 있으면 `NaN`을 반환합니다. 초기 시점에 윈도우 크기가 채워지지 않았을 때 유용합니다.
    *   수식:
        $$ \text{rollMean}_w[t] = \frac{1}{n_t} \sum_{i=t-n_t+1}^{t} s[i] \quad \text{where } n_t = \min(w, \text{#seen}) $$
        $s[i]$는 시계열 데이터의 $i$번째 값, $n_t$는 현재 시점 $t$에서 실제로 계산에 포함된 관측치의 개수입니다. 이는 윈도우 크기 $w$와 현재까지 본 데이터의 개수(`\#seen`) 중 최솟값으로 결정됩니다.

*   **Expanding Sum (누적 합)**
    *   Pandas 코드:
        ```python
        s.expanding().sum()
        ```
        *   `min_periods` 파라미터를 사용하여 초기 `NaN` 값을 제어할 수 있습니다.
    *   수식:
        $$ \text{expandSum}[t] = \sum_{i \le t} s[i] $$
        $s[i]$는 시계열 데이터의 $i$번째 값이며, $i \le t$는 데이터의 시작부터 현재 시점 $t$까지의 모든 값을 포함한다는 의미입니다.

*   **EWMA (Exponentially Weighted Moving Average)**
    *   Pandas 코드:
        ```python
        s.ewm(alpha, adjust=False).mean()
        ```
        *   `alpha`: 평활 계수(smoothing factor). 0과 1 사이의 값으로, 클수록 최근 데이터에 더 큰 가중치를 부여합니다.
        *   `adjust=False`: Pandas의 기본 `adjust=True`와 달리, 초기값 처리 방식을 변경하여 슬라이드에 제시된 수식($y_0=x_0$)과 일치시킵니다.
        *   `alpha`는 `span`, `com`(center of mass), `halflife` 파라미터를 통해 간접적으로 설정할 수도 있습니다.
    *   수식:
        $$ y_t = \alpha x_t + (1 - \alpha) y_{t-1} \quad \text{with } y_0 = x_0 $$
        $y_t$는 시점 $t$의 EWMA 값, $x_t$는 시점 $t$의 실제 데이터 값, $y_{t-1}$는 이전 시점의 EWMA 값입니다. $y_0$는 첫 번째 데이터 $x_0$로 초기화됩니다.

### 구체적 예시

주어진 데이터 `s = [5, 2, 7, 4, 9]` (인덱스 `a, b, c, d, e`)

*   **Rolling Mean (w=3, min_periods=1)**
    *   `a`: $5 / 1 = 5.0$
    *   `b`: $(5+2) / 2 = 3.5$
    *   `c`: $(5+2+7) / 3 = 4.6667$
    *   `d`: $(2+7+4) / 3 = 4.3333$
    *   `e`: $(7+4+9) / 3 = 6.6667$

*   **Expanding Sum**
    *   `a`: $5 = 5$
    *   `b`: $5+2 = 7$
    *   `c`: $5+2+7 = 14$
    *   `d`: $5+2+7+4 = 18$
    *   `e`: $5+2+7+4+9 = 27$

*   **EWMA (alpha=0.5, adjust=False)**
    *   `a`: $y_0 = x_0 = 5.0000$
    *   `b`: $y_b = 0.5 \cdot x_b + (1-0.5) \cdot y_a = 0.5 \cdot 2 + 0.5 \cdot 5 = 1 + 2.5 = 3.5000$
    *   `c`: $y_c = 0.5 \cdot x_c + 0.5 \cdot y_b = 0.5 \cdot 7 + 0.5 \cdot 3.5 = 3.5 + 1.75 = 5.2500$
    *   `d`: $y_d = 0.5 \cdot x_d + 0.5 \cdot y_c = 0.5 \cdot 4 + 0.5 \cdot 5.25 = 2 + 2.625 = 4.6250$
    *   `e`: $y_e = 0.5 \cdot x_e + 0.5 \cdot y_d = 0.5 \cdot 9 + 0.5 \cdot 4.625 = 4.5 + 2.3125 = 6.8125$

### 시험 포인트

*   ⭐ **Rolling, Expanding, EWMA의 개념 및 동작 방식 차이점**을 명확히 이해하고 설명할 수 있어야 합니다. (예: 윈도우 크기의 변화, 가중치 적용 여부)
*   ⭐ 각 윈도우 함수의 **핵심 파라미터 (예: `w`, `min_periods`, `alpha`, `adjust`)의 역할**과 이들이 결과에 미치는 영향을 알아야 합니다.
*   ⭐ **주어진 데이터와 파라미터를 사용하여 각 윈도우 함수의 결과를 직접 계산**할 수 있어야 합니다. 특히 EWMA의 초기값 설정 ($y_0 = x_0$)과 `adjust=False`의 의미를 이해하는 것이 중요합니다.
*   ⭐ `min_periods` 파라미터가 **초기 데이터 부족 시 발생하는 `NaN` 값을 어떻게 처리하는지** 설명할 수 있어야 합니다.
*   ⭐ EWMA에서 `alpha` 값의 의미와 **최근 데이터에 더 큰 가중치를 부여하는 원리**를 이해하고 설명할 수 있어야 합니다. 또한 `span`, `com`, `halflife`를 통해 `alpha`가 어떻게 계산될 수 있는지 파악하는 것도 좋습니다.

---

## Slide 37

### 핵심 개념

-   **Window Functions (윈도우 함수)**: 시계열 데이터나 순서가 있는 데이터에서 특정 "윈도우(창)" 내의 데이터를 기반으로 통계량을 계산하는 함수입니다. 이 윈도우는 데이터 위를 이동하며(rolling), 확장되며(expanding), 혹은 가중치를 적용하며(EWM) 데이터를 분석합니다. 데이터의 추세 파악, 평활화, 노이즈 제거 등에 활용됩니다.
    -   **Rolling Window (이동 평균/이동 통계)**: 고정된 크기(`window`)의 윈도우를 데이터 위로 이동시키면서 각 윈도우 내의 통계량(평균, 합계, 표준편차 등)을 계산합니다. 데이터의 단기적인 추세를 파악하고 노이즈를 제거하는 데 유용합니다.
    -   **Expanding Window (누적 통계)**: 윈도우의 시작점은 고정되어 있고, 윈도우의 끝점이 데이터의 현재 지점까지 확장되면서 통계량을 계산합니다. 즉, 현재까지의 모든 데이터를 포함하여 통계량을 계산하는 방식입니다 (예: 누적 합계, 누적 평균). 데이터의 전체적인 변화량이나 총계를 파악하는 데 적합합니다.
    -   **Exponentially Weighted Moving (EWM) Window (지수 가중 이동 평균)**: 가장 최근 데이터 포인트에 더 큰 가중치를 부여하고, 오래된 데이터에는 지수적으로 감소하는 가중치를 부여하여 통계량을 계산합니다. 최신 트렌드를 더 민감하게 반영하면서도 이동 평균처럼 노이즈를 줄이는 효과가 있습니다. `alpha` 파라미터는 가중치 감소율을 결정합니다.

### 코드/수식 해설

```python
import pandas as pd

# Pandas Series 생성: 5개의 데이터와 'a'부터 'e'까지의 인덱스를 가집니다.
s = pd.Series([5, 2, 7, 4, 9], index=list('abcde'))

# 1. Rolling Window (이동 평균)
# s.rolling(3, min_periods=1): 윈도우 크기를 3으로 설정합니다.
#                              min_periods=1은 윈도우 크기(3)만큼의 데이터가 채워지지 않아도 최소 1개 데이터만 있으면 계산을 허용합니다.
# .mean(): 각 윈도우 내의 평균을 계산합니다.
# .round(4): 결과를 소수점 4자리까지 반올림합니다.
roll3 = s.rolling(3, min_periods=1).mean().round(4)

# 2. Expanding Window (누적 합계)
# s.expanding(): 윈도우가 데이터의 시작부터 현재 위치까지 계속 확장됩니다.
# .sum(): 확장된 윈도우 내의 모든 값의 합계를 계산합니다 (누적 합계).
expd = s.expanding().sum()

# 3. Exponentially Weighted Moving (지수 가중 이동 평균)
# s.ewm(alpha=0.5, adjust=False): alpha=0.5로 지수 가중치(감쇠 인자)를 설정합니다.
#                                 adjust=False는 초기 가중치 계산 방식을 지정하며, 슬라이드에서는 간단한 재귀식을 따릅니다.
# .mean(): 지수 가중 평균을 계산합니다.
# .round(4): 결과를 소수점 4자리까지 반올림합니다.
expo = s.ewm(alpha=0.5, adjust=False).mean().round(4)
```

**EWM (Exponentially Weighted Moving) 수식 해설 (with `adjust=False`):**

`adjust=False` 옵션을 사용할 때 지수 가중 이동 평균 ($y_t$)은 다음의 재귀적인 공식으로 계산됩니다.

$$y_t = (1 - \alpha) y_{t-1} + \alpha x_t$$

여기서:
-   $y_t$: 현재 시점 $t$에서의 EWM 값
-   $y_{t-1}$: 이전 시점 $t-1$에서의 EWM 값 (바로 직전 EWM 결과)
-   $x_t$: 현재 시점 $t$에서의 원본 데이터 값
-   $\alpha$: 가중치 감쇠 인자 (0 < $\alpha$ < 1). $\alpha$ 값이 1에 가까울수록 최신 데이터에 더 큰 가중치를 부여하고, 0에 가까울수록 과거 데이터의 영향을 많이 받습니다.

초기값은 보통 첫 번째 데이터 포인트 $x_0$와 동일하게 설정합니다. 즉, $y_0 = x_0$입니다.

슬라이드의 `expo` 결과 계산 과정 (원본 Series `s` = `[5, 2, 7, 4, 9]` 및 `alpha = 0.5`):
1.  **idx 'a'**: $y_a = x_a = 5.0000$ (시드값)
2.  **idx 'b'**: $y_b = (1 - 0.5) y_a + 0.5 x_b = 0.5 \times 5.0 + 0.5 \times 2 = 2.5 + 1.0 = 3.5000$
3.  **idx 'c'**: $y_c = (1 - 0.5) y_b + 0.5 x_c = 0.5 \times 3.5 + 0.5 \times 7 = 1.75 + 3.5 = 5.2500$
4.  **idx 'd'**: $y_d = (1 - 0.5) y_c + 0.5 x_d = 0.5 \times 5.25 + 0.5 \times 4 = 2.625 + 2.0 = 4.6250$
5.  **idx 'e'**: $y_e = (1 - 0.5) y_d + 0.5 x_e = 0.5 \times 4.625 + 0.5 \times 9 = 2.3125 + 4.5 = 6.8125$

### 구체적 예시

-   **Rolling Window (이동 평균)**:
    -   **주식 시장 분석**: 5일 이동 평균선, 20일 이동 평균선 등을 사용하여 단기/중기적인 주가 추세를 파악합니다. 예시의 `roll3`는 3일 이동 평균과 유사하며, 'c' 지점의 `4.6667`은 인덱스 'a', 'b', 'c' (값 5, 2, 7)의 평균입니다.
    -   **스포츠 선수 성적 분석**: 최근 10경기 타율이나 득점 평균 등을 계산하여 선수의 현재 컨디션을 평가할 때 사용됩니다.

-   **Expanding Window (누적 합계)**:
    -   **판매 실적 누적**: 월별 또는 분기별 판매액을 연초부터 현재까지 누적하여 총 판매 실적을 확인하는 데 사용됩니다. 예시의 `expd`에서 'd' 지점의 `18`은 인덱스 'a'부터 'd'까지 (값 5, 2, 7, 4)의 누적 합입니다.
    -   **예산 소진율**: 프로젝트 시작부터 현재까지의 누적 지출액을 계산하여 남은 예산을 파악합니다.

-   **EWM (지수 가중 이동 평균)**:
    -   **제품 수요 예측**: 최신 판매 데이터에 더 큰 가중치를 두어 미래 수요를 예측할 때 사용됩니다. 최근 트렌드 변화에 더 민감하게 반응하여 빠르게 예측 모델을 업데이트할 수 있습니다.
    -   **온도 센서 데이터**: 실시간으로 측정되는 온도 데이터에서 노이즈를 줄이면서도 갑작스러운 온도 변화에 빠르게 반응하는 평균값을 얻고자 할 때 사용됩니다.

### 시험 포인트

-   ⭐ **Rolling, Expanding, EWM의 개념적 차이점**과 각각이 어떤 데이터 분석 시나리오에 적합한지 **예시와 함께 설명**할 수 있어야 합니다.
-   ⭐ **`rolling()` 함수의 `window` 및 `min_periods` 파라미터의 역할**을 정확히 이해하고, 특정 조건(예: `min_periods`가 `window`보다 작을 때)에서의 계산 결과를 예측할 수 있어야 합니다.
-   ⭐ **`ewm()` 함수의 `alpha` 파라미터가 가중치에 미치는 영향**과, `adjust=True` (기본값)와 `adjust=False`일 때 **EWM 계산 방식의 차이**를 이해해야 합니다. 특히 슬라이드 예시와 같은 `adjust=False` 상황에서의 재귀적 계산 과정을 파악하는 것이 중요합니다.
-   ⭐ **주어진 데이터와 윈도우 함수 파라미터를 바탕으로 각 지점의 결과값을 직접 계산할 수 있어야 합니다.** 특히 `rolling`의 첫 몇 지점과 `ewm`의 재귀적 계산 과정을 연습하는 것이 좋습니다.
-   Pandas `Series` 또는 `DataFrame`에 윈도우 함수를 적용하는 기본적인 문법 (`.rolling().mean()`, `.expanding().sum()`, `.ewm().mean()`)을 숙지해야 합니다.

---

## Slide 38

---
### **핵심 개념**

*   **Fast Scalars (빠른 스칼라 접근)**: Pandas Series에서 특정 위치의 단일 스칼라 값을 매우 빠르게 조회하기 위한 기능입니다. `.loc`과 `.iloc`에 비해 단일 값 접근 시 성능 이점이 있습니다.
    *   `s.at[label]`: Series의 **인덱스 라벨(label)**을 사용하여 스칼라 값을 조회합니다. 해당 라벨이 없으면 `KeyError`를 발생시킵니다.
    *   `s.iat[pos]`: Series의 **정수 위치(position, 0-based)**를 사용하여 스칼라 값을 조회합니다. 유효하지 않은 위치인 경우 `IndexError`를 발생시킵니다.
*   **Value Counts (값 빈도 계산)**: Series 내의 고유한 값들이 각각 몇 번 나타나는지 빈도수를 계산합니다. 범주형 데이터의 분포를 파악하는 데 매우 유용합니다.
    *   `s.value_counts()`: 각 고유 값의 빈도수를 담은 Series를 반환합니다. 결과 Series의 인덱스는 원본 Series의 고유 값, 값은 해당 값의 빈도수가 됩니다.
*   **Sampling (샘플링)**: Series 또는 DataFrame에서 무작위로 일부 데이터를 추출하는 기능입니다. 데이터 서브셋 생성, 교차 검증, 부트스트랩 등의 통계적 분석에 활용됩니다.
    *   `s.sample()`: 지정된 개수(`n`) 또는 비율(`frac`)에 따라 데이터를 무작위로 추출합니다.

### **코드/수식 해설**

**1. Fast Scalars: `s.at` 및 `s.iat`**

```python
import pandas as pd

# 예시 Series 생성
s = pd.Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D'])
print("Original Series:\n", s)

# s.at[label]: 라벨 'C'에 해당하는 값 조회
value_at_c = s.at['C']
print(f"\nValue at label 'C' using s.at: {value_at_c}")

# s.iat[pos]: 0-based position 1에 해당하는 값 조회 (두 번째 값)
value_at_pos_1 = s.iat[1]
print(f"Value at position 1 using s.iat: {value_at_pos_1}")

# 존재하지 않는 라벨/위치 접근 시 에러 발생 예시 (주석 처리)
# try:
#     s.at['E'] # KeyError 발생
# except KeyError as e:
#     print(f"\nError using s.at['E']: {e}")
#
# try:
#     s.iat[5] # IndexError 발생
# except IndexError as e:
#     print(f"Error using s.iat[5]: {e}")
```

**2. Value Counts: `s.value_counts()`**

```python
import pandas as pd
import numpy as np

# 예시 Series 생성
grades = pd.Series(['A', 'B', 'A', 'C', 'B', 'A', np.nan, 'D', 'C', 'B'])
print("Original Grades Series:\n", grades)

# 기본 사용: 각 값의 빈도수 계산 (NaN은 기본적으로 제외)
counts = grades.value_counts()
print(f"\nValue counts (default, dropna=True):\n{counts}")

# dropna=False: NaN 값도 빈도수에 포함
counts_with_nan = grades.value_counts(dropna=False)
print(f"\nValue counts (dropna=False, including NaN):\n{counts_with_nan}")

# normalize=True: 각 값의 상대 빈도(비율) 계산
proportions = grades.value_counts(normalize=True)
print(f"\nValue counts (normalize=True, proportions):\n{proportions}")

# normalize=True, dropna=False: NaN을 포함한 전체 데이터에 대한 비율
proportions_with_nan = grades.value_counts(normalize=True, dropna=False)
print(f"\nValue counts (normalize=True, dropna=False):\n{proportions_with_nan}")
```

`normalize=True`일 때 계산되는 비율은 다음과 같습니다:
$$ \text{proportion}_i = \frac{\text{count}_i}{\sum_{j} \text{count}_j \text{ (excluding NaN if dropna=True)}} $$
또는 `dropna=False`일 경우:
$$ \text{proportion}_i = \frac{\text{count}_i}{\text{Total number of elements in Series}} $$

**3. Sampling: `s.sample()`**

```python
import pandas as pd
import numpy as np

# 예시 Series 생성
students = pd.Series([f'Student_{i}' for i in range(1, 21)]) # 20명의 학생
print("Original Students Series:\n", students)

# n을 사용하여 3명 무작위 샘플링 (비복원 추출이 기본)
sample_n = students.sample(n=3, random_state=42) # random_state로 결과 재현 가능
print(f"\nSample of 3 students (n=3):\n{sample_n}")

# frac을 사용하여 25% 비율로 샘플링
sample_frac = students.sample(frac=0.25, random_state=42)
print(f"\nSample of 25% students (frac=0.25):\n{sample_frac}")

# replace=True: 복원 추출 (동일한 데이터가 여러 번 뽑힐 수 있음, 부트스트랩 시 사용)
sample_replace = students.sample(n=5, replace=True, random_state=42)
print(f"\nSample of 5 students with replacement (replace=True):\n{sample_replace}")
```

### **구체적 예시**

*   **`s.at` / `s.iat`**:
    *   어떤 회사의 직원 데이터가 직원 ID(인덱스 라벨)와 월급(값)으로 구성된 Series로 있다고 가정해 봅시다. 특정 직원 ID `emp_007`의 월급을 빠르게 조회하려면 `employee_salaries.at['emp_007']`을 사용합니다.
    *   직원 리스트에서 인덱스 순서로 5번째 직원의 정보를 빨리 가져오고 싶다면 `employee_list.iat[4]` (0-based 인덱스이므로 4)를 사용할 수 있습니다.
*   **`s.value_counts()`**:
    *   설문조사 데이터에서 응답자의 거주 지역(예: 서울, 부산, 대구)을 담은 Series가 있다면, `survey_data['region'].value_counts()`를 통해 각 지역에 몇 명이 거주하는지 쉽게 파악할 수 있습니다. `normalize=True`를 사용하면 각 지역의 응답자 비율을 알 수 있습니다.
*   **`s.sample()`**:
    *   전체 고객 10만 명 중 1,000명에게 신제품에 대한 설문조사를 하고자 할 때, `customers.sample(n=1000, random_state=SEED)`를 사용하여 무작위로 1,000명의 고객을 선정할 수 있습니다.
    *   머신러닝 모델을 훈련할 때, 전체 데이터셋의 80%를 훈련 데이터로 사용하고 싶다면 `dataset.sample(frac=0.8, random_state=SEED)`를 사용할 수 있습니다. `replace=True`는 부트스트랩 샘플링(동일한 데이터가 여러 번 추출될 수 있는 방식)에 사용되어 모델의 안정성을 평가하는 데 쓰입니다.

### **시험 포인트**

*   **`s.at`과 `s.iat`의 차이점**: ⭐`at`은 **라벨 기반** 인덱싱, `iat`은 **정수 위치 기반** 인덱싱이라는 것을 명확히 이해하고 구별해야 합니다. 단일 스칼라 값 접근 시 `loc`/`iloc`보다 성능이 빠르다는 점도 기억하세요.
*   **`s.value_counts()` 파라미터**: ⭐`dropna=False`가 NaN 값도 카운트한다는 것, 그리고 `normalize=True`가 빈도수가 아닌 비율(상대 빈도)을 반환한다는 것을 숙지해야 합니다. 특히, `normalize=True`일 때 `dropna`가 최종 비율 계산에 어떻게 영향을 미치는지 이해하는 것이 중요합니다.
*   **`s.sample()` 파라미터**: ⭐`n`과 `frac`으로 샘플링할 개수 또는 비율을 지정하는 방법을 알고, 특히 `replace=True`와 `replace=False`의 차이점(복원 추출 vs. 비복원 추출)을 정확히 이해해야 합니다. 부트스트랩과 같은 통계적 기법에서 `replace=True`의 역할은 중요합니다.
*   **`random_state`의 중요성**: ⭐`s.sample()`과 같은 무작위 연산에서 `random_state`를 설정하는 이유(결과의 재현성 확보)를 알아야 합니다.

---

## Slide 39

**핵심 개념**

*   **Fast Scalars (`.at`, `.iat`)**: `pandas` Series나 DataFrame에서 단일 값을 매우 빠르게 추출하기 위한 접근자(accessor)입니다.
    *   `.at`: 레이블(인덱스 이름)을 기반으로 값을 접근할 때 사용합니다. Python의 일반적인 딕셔너리 접근(`[]`)보다 빠릅니다.
    *   `.iat`: 정수 위치(0부터 시작하는 인덱스 번호)를 기반으로 값을 접근할 때 사용합니다. Python의 일반적인 리스트 접근(`[]`)보다 빠릅니다.
*   **Value Counts (`.value_counts()`)**: Series 내의 고유한 값들과 각 값의 출현 빈도를 계산하는 메서드입니다.
    *   `dropna=False` 옵션을 통해 결측치(`NaN`)도 빈도 계산에 포함시킬 수 있습니다.
    *   `normalize=True` 옵션을 통해 빈도가 아닌 비율(상대 빈도)을 계산할 수 있습니다.
*   **Sampling (`.sample()`)**: Series나 DataFrame에서 무작위로 일부 데이터를 추출하는 메서드입니다.
    *   `n`: 추출할 샘플의 개수를 지정합니다.
    *   `random_state`: 랜덤 샘플링의 결과를 재현 가능하게 하기 위한 시드(seed) 값을 설정합니다. 동일한 `random_state` 값을 사용하면 항상 같은 결과를 얻습니다.

**코드/수식 해설**

```python
import pandas as pd

# 1. Series s 생성: 인덱스가 'a'부터 'e'까지인 정수형 Series
s = pd.Series([5, 2, 7, 4, 9], index=list('abcde'))
# s의 내용: a 5, b 2, c 7, d 4, e 9

# 2. Series vals 생성: 문자열과 결측치(None)를 포함하는 Series
vals = pd.Series(['x', 'x', 'y', None, 'x'])
# vals의 내용: 0 x, 1 x, 2 y, 3 NaN, 4 x

# 3. .at을 이용한 레이블 기반 스칼라 접근
c = s.at['c']
# s['c']와 동일하게 인덱스 'c'에 해당하는 값 7을 빠르게 추출합니다.
# c의 값은 7

# 4. .iat을 이용한 정수 위치 기반 스칼라 접근
p = s.iat[2]
# s[2]와 동일하게 0부터 시작하는 세 번째(인덱스 2) 값 7을 빠르게 추출합니다.
# p의 값은 7

# 5. vals Series의 값별 빈도 계산
counts = vals.value_counts(dropna=False)
# dropna=False 옵션으로 NaN 값도 포함하여 빈도를 계산합니다.
# 결과 (counts):
# x      3
# y      1
# NaN    1
# dtype: int64

# 6. vals Series의 값별 비율 계산 및 반올림
props = vals.value_counts(normalize=True, dropna=False).round(2)
# normalize=True 옵션으로 빈도 대신 비율을 계산합니다. (전체 5개 중 x: 3/5, y: 1/5, NaN: 1/5)
# dropna=False 옵션으로 NaN 값도 포함하여 비율을 계산합니다.
# .round(2)로 소수점 둘째 자리까지 반올림합니다.
# 결과 (props):
# x      0.60 (3/5)
# y      0.20 (1/5)
# NaN    0.20 (1/5)
# dtype: float64

# 7. s Series에서 1개의 샘플 추출 (재현 가능하도록 random_state 지정)
one = s.sample(n=1, random_state=0)
# s Series에서 무작위로 1개의 항목을 추출합니다.
# random_state=0을 사용하여 실행할 때마다 동일한 결과(여기서는 'e' 인덱스의 9)를 얻습니다.
# 결과 (one):
# e    9
# dtype: int64
```

**구체적 예시**

*   **Fast Scalars (`.at`, `.iat`)**: 대규모 데이터셋에서 특정 인덱스/위치의 단일 값을 자주 조회해야 할 때 매우 유용합니다. 예를 들어, 100만 줄짜리 학생 성적 데이터(`pd.DataFrame`)에서 특정 학생의 학번(`index`)으로 그 학생의 점수(`column`)를 빠르게 확인하거나, 가장 첫 번째 학생(`0`)의 정보를 가져올 때 `df.at[학번, '점수']`나 `df.iat[0, 1]`와 같이 사용할 수 있습니다. 이는 일반적인 `df.loc[학번, '점수']`나 `df.iloc[0, 1]`보다 성능상 이점이 있습니다.
*   **Value Counts (`.value_counts()`)**: 설문조사 데이터에서 응답자들이 가장 선호하는 항목이 무엇인지 (빈도수), 또는 전체 응답자 중 몇 퍼센트가 특정 항목을 선택했는지 (비율)를 분석할 때 활용됩니다. 예를 들어, "가장 좋아하는 과일은?" 이라는 질문에 대한 응답 Series가 있다면, `fruit_series.value_counts()`로 각 과일의 선호도를 파악할 수 있습니다.
*   **Sampling (`.sample()`)**: 전체 모집단 데이터가 너무 커서 모두 분석하기 어려울 때, 통계적으로 유의미한 표본을 추출하여 분석할 때 사용합니다. 예를 들어, 1000만 명의 고객 데이터 중 1만 명을 무작위로 추출하여 마케팅 전략을 테스트하거나, 머신러닝 모델 학습을 위해 데이터 일부를 사용할 때 `df.sample(n=10000, random_state=42)`와 같이 활용할 수 있습니다.

**시험 포인트**

*   **`.at`과 `.iat`의 차이점**: ⭐`.at`은 레이블(인덱스 이름) 기반, `.iat`은 정수 위치 기반 접근이라는 점을 정확히 구분할 수 있어야 합니다.
*   **`.value_counts()`의 `dropna` 및 `normalize` 옵션**: ⭐각 옵션이 어떤 역할을 하는지, 그리고 이들을 조합했을 때 결과가 어떻게 달라지는지 이해하는 것이 중요합니다. (특히 `NaN` 처리와 비율 계산)
*   **`.sample()`의 `n` 및 `random_state` 옵션**: `n`은 추출 개수, `random_state`는 재현성을 위한 시드값임을 기억하세요. ⭐`random_state`를 설정하는 이유와 그 효과를 설명할 수 있어야 합니다.
*   **결측치(NaN) 처리**: `None`이 `pandas`에서 `NaN`으로 처리되는 방식과 `dropna=False`가 `NaN` 값을 포함시키는 역할을 인지해야 합니다.

---

## Slide 40

## Working with DataFrames - Core operations

---

### 핵심 개념

이 슬라이드는 `pandas` DataFrame 객체를 다루는 핵심적인 연산들을 소개합니다. 데이터 탐색 및 진단부터, 특정 데이터 선택, 결측치 처리, 데이터 정렬 및 변형에 이르기까지 데이터 분석의 기반이 되는 다양한 기능을 다룹니다.

### 코드/수식 해설

#### 1. Anatomy & Diagnostics
DataFrame의 구조와 기본적인 정보를 확인하는 메서드입니다.
*   `df.index`: DataFrame의 행 인덱스(row labels)를 반환합니다.
*   `df.columns`: DataFrame의 열 인덱스(column labels)를 반환합니다.
*   `df.dtypes`: 각 컬럼의 데이터 타입을 `Series` 형태로 반환합니다.
*   `df.info()`: DataFrame의 요약 정보를 출력합니다. (인덱스 타입, 컬럼 수, 각 컬럼의 Non-Null 값 수, 데이터 타입, 메모리 사용량 등)
*   `df.select_dtypes(include=[...])`: 특정 데이터 타입(`int`, `float`, `object` 등)을 가진 컬럼만 선택합니다.

#### 2. Column Picks
DataFrame에서 컬럼을 선택하고 추가하는 방법입니다.
*   `df['col']`: 단일 컬럼을 선택하며, 결과는 `pandas.Series` 객체입니다.
*   `df[['col']]`: 단일 컬럼을 선택하지만, 결과는 `pandas.DataFrame` 객체입니다 (리스트 형태로 컬럼을 전달했기 때문). 여러 컬럼 선택 시 `df[['col1', 'col2']]`와 같이 사용합니다.
*   `df.assign(new_col=...)`: 새로운 컬럼을 추가하거나 기존 컬럼을 수정합니다. 원본 DataFrame을 변경하지 않고 새로운 DataFrame을 반환하는 방식입니다.

```python
import pandas as pd
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# 컬럼 선택
print(type(df['A']))       # <class 'pandas.core.series.Series'>
print(type(df[['A']]))     # <class 'pandas.core.frame.DataFrame'>

# 새로운 컬럼 추가
df_new = df.assign(C=df['A'] + df['B'])
print(df_new)
```

#### 3. Label vs. Position Indexing
데이터를 선택할 때 라벨(이름)을 기반으로 할지, 위치(정수 인덱스)를 기반으로 할지 결정하는 방법입니다.
*   `df.loc[row_labels, col_labels]`: 라벨(이름)을 사용하여 데이터에 접근합니다. 슬라이싱(`start:end`) 시 `end` 라벨을 포함합니다 (inclusive).
*   `df.iloc[row_pos, col_pos]`: 정수 위치를 사용하여 데이터에 접근합니다. 슬라이싱(`start:end`) 시 `end` 위치는 포함하지 않습니다 (exclusive), 파이썬의 기본 슬라이싱 규칙과 동일합니다.

```python
df = pd.DataFrame({'col1': [10, 20, 30], 'col2': [40, 50, 60]},
                  index=['r1', 'r2', 'r3'])

print(df.loc['r1':'r2', 'col1']) # 'r1'부터 'r2'까지 (포함)
print(df.iloc[0:2, 0])          # 0부터 2 미만까지 (0, 1 인덱스)
```

#### 4. Fast Scalars
단일 셀(스칼라 값)에 빠르게 접근하거나 수정할 때 사용합니다.
*   `df.at[row_label, col_label]`: 라벨 기반으로 단일 값에 접근. `loc`보다 빠릅니다.
*   `df.iat[row_pos, col_pos]`: 정수 위치 기반으로 단일 값에 접근. `iloc`보다 빠릅니다.

```python
df = pd.DataFrame({'A': [10, 20], 'B': [30, 40]}, index=['r1', 'r2'])
print(df.at['r1', 'A'])  # 10
df.at['r1', 'A'] = 100   # 값 변경
print(df)
```

#### 5. Boolean Filtering
특정 조건을 만족하는 행을 선택하는 방법입니다.
*   `df[condition]`: `condition`은 `True`/`False`로 구성된 `Series` (마스크)이며, `True`인 행만 선택합니다.
*   `&`, `|`, `~`: 여러 조건을 조합할 때 사용되는 논리 연산자 (AND, OR, NOT). 각 조건은 반드시 괄호로 묶어야 합니다.
*   `.isin(values)`: 특정 컬럼의 값이 주어진 리스트 안에 있는지 확인합니다.
*   `.between(lower, upper)`: 특정 컬럼의 값이 주어진 범위 (양 끝 값 포함) 내에 있는지 확인합니다.
*   `.query('expression')`: 문자열 표현식을 사용하여 복잡한 필터링 조건을 지정할 수 있습니다.

```python
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]})
print(df[(df['A'] > 2) & (df['B'] < 40)]) # 'A' > 2 이고 'B' < 40 인 행
print(df[df['A'].isin([1, 3])])          # 'A'가 1 또는 3인 행
print(df.query('A > 2 and B < 40'))      # query 메서드 사용
```

#### 6. Across-Columns Tests
DataFrame 전체 또는 여러 컬럼에 걸쳐 조건을 테스트하고 집계합니다.
*   `df.isna()`: DataFrame의 각 셀이 결측치인지 여부를 불리언 DataFrame으로 반환합니다.
*   `.any(axis=1)`: 행(axis=1) 방향으로, 해당 행에 `True` 값이 하나라도 있으면 `True`를 반환합니다. (예: 어떤 컬럼이라도 결측치인 행)
*   `.all(axis=1)`: 행(axis=1) 방향으로, 해당 행의 모든 값이 `True`여야 `True`를 반환합니다. (예: 모든 컬럼의 값이 0보다 큰 행)
*   `axis=0`: 컬럼 방향 연산 (기본값). `axis=1`: 행 방향 연산.

```python
import numpy as np
df = pd.DataFrame({'A': [1, np.nan, 3], 'B': [10, 20, np.nan]})
print(df.isna().any(axis=1)) # 어느 컬럼이라도 결측치가 있는 행
print(df.gt(0).all(axis=1))   # 모든 컬럼의 값이 0보다 큰 행
```

#### 7. Safe Assignment
`SettingWithCopyWarning`을 방지하고 데이터 정합성을 유지하며 값을 할당하는 방법입니다.
*   `df.loc[mask, 'col'] = value`: 특정 조건(`mask`)을 만족하는 행과 특정 컬럼에 값을 할당할 때 `loc`을 명시적으로 사용합니다. 체인 인덱싱(Chained Indexing)을 피하여 경고를 방지합니다.
*   `.copy()` after subsetting: DataFrame의 서브셋을 만들 때 `.copy()`를 명시적으로 호출하여 원본과 독립적인 복사본을 생성합니다.
*   `align with reindex`: 두 객체 간 연산 시 인덱스 불일치 문제를 해결하기 위해 `reindex()`를 사용하여 인덱스를 정렬합니다.

```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30]})
# 안전한 할당 (SettingWithCopyWarning 방지)
df.loc[df['A'] > 1, 'B'] = 99
print(df)

# .copy()를 사용한 독립적인 서브셋 생성
df_subset = df[df['A'] > 1].copy()
df_subset['B'] = 0 # 원본 df에 영향을 주지 않음
```

#### 8. Missing Values
결측치(NaN)를 감지하고 처리하는 방법입니다.
*   `df.isna()`: 각 셀의 결측치 여부를 불리언 DataFrame으로 반환합니다 (`df.isnull()`과 동일).
*   `df.fillna(value)`: 결측치를 특정 `value`로 채웁니다. 딕셔너리를 사용하여 컬럼별로 다른 값으로 채울 수도 있습니다 (`df.fillna({'col1': val1, 'col2': val2})`).
*   `df.ffill(axis=0/1)`: Forward fill. 이전 유효한 값으로 결측치를 채웁니다.
*   `df.bfill(axis=0/1)`: Backward fill. 다음 유효한 값으로 결측치를 채웁니다.
*   `df.interpolate()`: 선형 보간 등 다양한 방법으로 결측치를 보간합니다. 시계열 데이터에 유용합니다.

```python
import numpy as np
df = pd.DataFrame({'A': [1, np.nan, 3, 4], 'B': [np.nan, 20, np.nan, 40]})
print("Original:\n", df)
print("\nFilled with 0:\n", df.fillna(0))
print("\nForward Fill:\n", df.ffill())
print("\nInterpolated:\n", df.interpolate())
```

#### 9. Alignment & Broadcasting
`pandas` 객체 간의 이진 연산(+, -, *, /) 시 발생하는 인덱스 정렬 및 브로드캐스팅 규칙입니다.
*   **Binary ops align on both axes**: 두 DataFrame 간의 연산 시, 행 인덱스와 열 컬럼이 모두 일치하는 위치에서 연산이 수행됩니다. 일치하지 않는 부분은 `NaN`으로 채워집니다.
*   `df.add/sub/mul(other, fill_value=0)`: 일반 연산자 대신 메서드를 사용하면, 인덱스 정렬 후 일치하지 않는 부분에 `fill_value`를 적용하여 `NaN`이 발생하는 것을 방지할 수 있습니다.
*   `df.add(series, axis='index'|'columns')`: DataFrame과 Series 간의 연산 시, `axis` 파라미터를 사용하여 Series를 DataFrame의 특정 축에 맞춰 브로드캐스팅(반복 적용)할 수 있습니다.
    *   `axis='columns'` (또는 `axis=1`): Series의 인덱스를 DataFrame의 컬럼에 맞춰 각 행에 적용.
    *   `axis='index'` (또는 `axis=0`): Series의 인덱스를 DataFrame의 인덱스에 맞춰 각 컬럼에 적용.

```python
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'B': [10, 20], 'C': [30, 40]})
print("df1 + df2 (NaN due to misalignment):\n", df1 + df2)
print("df1.add(df2, fill_value=0):\n", df1.add(df2, fill_value=0))

s = pd.Series([100, 200], index=['A', 'B'])
print("df1.add(s, axis='columns'):\n", df1.add(s, axis='columns'))
```

#### 10. Sorting & Top-k
데이터를 정렬하거나 상위/하위 `k`개의 값을 찾는 방법입니다.
*   `df.sort_values(by=['col1', 'col2'], ascending=True)`: 하나 또는 여러 컬럼의 값을 기준으로 DataFrame을 정렬합니다. `ascending`으로 오름차순/내림차순을 지정합니다.
*   `df.sort_index(axis=0/1)`: 행 인덱스(`axis=0`) 또는 컬럼 인덱스(`axis=1`)를 기준으로 DataFrame을 정렬합니다.
*   `df.nlargest(k, 'col')`: 특정 컬럼에서 값이 가장 큰 `k`개의 행을 반환합니다.
*   `df.nsmallest(k, 'col')`: 특정 컬럼에서 값이 가장 작은 `k`개의 행을 반환합니다.

```python
df = pd.DataFrame({'A': [3, 1, 2], 'B': [6, 5, 4]})
print("Sorted by 'A':\n", df.sort_values(by='A'))
print("Top 2 in 'B':\n", df.nlargest(2, 'B'))
```

#### 11. Reshape (Index/Columns)
DataFrame의 구조(인덱스와 컬럼)를 변경하여 데이터를 재구성하는 방법입니다. 주로 Wide format과 Long format 간의 변환에 사용됩니다.
*   `df.set_index('col_name')`: 특정 컬럼을 DataFrame의 새로운 인덱스로 설정합니다.
*   `df.reset_index()`: 현재 인덱스를 일반 컬럼으로 변환하고 새로운 기본 정수 인덱스를 생성합니다.
*   `pd.pivot(index, columns, values)`: 데이터를 재구성하여 `columns`로 지정된 컬럼의 고유값을 새 컬럼으로 만들고, `values` 컬럼의 값으로 채웁니다. `(index, columns)` 쌍이 유일해야 합니다.
*   `pd.pivot_table(index, columns, values, aggfunc='mean')`: `pivot`과 유사하지만, `(index, columns)` 쌍이 중복될 경우 `aggfunc` (평균, 합계 등)를 사용하여 값을 집계할 수 있습니다.
*   `pd.melt(df, id_vars=['id_col'], value_vars=['col1', 'col2'])`: Wide format의 DataFrame을 Long format으로 변환합니다. 여러 컬럼의 값을 하나의 컬럼으로 쌓습니다.

```python
df_wide = pd.DataFrame({
    'City': ['Seoul', 'Busan'],
    'Temp_Jan': [1, 5],
    'Temp_Jul': [25, 30]
})
print("Wide format:\n", df_wide)

# Wide -> Long 변환
df_long = pd.melt(df_wide, id_vars=['City'], var_name='Month_Temp', value_name='Temperature')
print("\nLong format (melt):\n", df_long)

# Long -> Wide 변환 (pivot_table 사용)
df_pivot = df_long.pivot_table(index='City', columns='Month_Temp', values='Temperature')
print("\nPivoted back to wide:\n", df_pivot)
```

### 구체적 예시

**데이터 분석 파이프라인에서의 활용**:
여러분은 고객 구매 기록 데이터 (`DataFrame`)를 가지고 있습니다.
1.  **진단**: `df.info()`와 `df.dtypes`로 데이터 구조와 결측치를 빠르게 파악합니다.
2.  **선택**: `df.loc[df['Age'] > 30, ['CustomerID', 'ProductCategory']]`를 사용하여 30세 이상 고객의 ID와 구매 카테고리를 추출합니다.
3.  **결측치 처리**: 구매 금액(`PurchaseAmount`)에 `NaN`이 있다면 `df['PurchaseAmount'].fillna(df['PurchaseAmount'].mean())`으로 평균값으로 채웁니다.
4.  **정렬**: 가장 많이 구매한 고객(`df.sort_values(by='PurchaseCount', ascending=False).head(10)`)을 찾거나, 특정 상품 카테고리의 데이터를 `df.nlargest(5, 'Rating', subset='ProductCategory' == 'Electronics')`로 찾아봅니다.
5.  **재구성**: 월별 판매액 데이터가 컬럼으로 나뉘어(`Sales_Jan`, `Sales_Feb`) 있다면 `pd.melt()`를 이용해 월별 판매 데이터를 하나의 컬럼으로 모아 시계열 분석에 용이한 형태로 변환할 수 있습니다.

### 시험 포인트

*   ⭐**`loc`과 `iloc`의 차이점**: 라벨 기반 vs. 위치 기반, 슬라이싱 시 범위 포함 여부 (`loc`은 끝 라벨 포함, `iloc`은 끝 위치 미포함).
*   ⭐**컬럼 선택 시 반환 타입**: `df['col']` (Series) vs. `df[['col']]` (DataFrame).
*   ⭐**불리언 필터링**: `&`, `|`, `~` 연산자 사용 시 각 조건은 반드시 괄호로 묶어야 합니다. `isin()`, `between()`, `query()`의 활용법을 알아야 합니다.
*   ⭐**`SettingWithCopyWarning`**: 이 경고가 발생하는 원인과 `df.loc[...] = value` 또는 `.copy()`를 사용하여 안전하게 값을 할당하는 방법을 정확히 이해해야 합니다.
*   ⭐**결측치 처리**: `fillna()`, `ffill()`, `bfill()`, `interpolate()` 등 다양한 결측치 처리 메서드의 사용법과 상황에 맞는 선택 기준을 알아야 합니다. `axis` 파라미터의 역할도 중요합니다.
*   ⭐**인덱스 정렬 및 브로드캐스팅**: `pandas`의 연산 시 인덱스 정렬 규칙을 이해하고, `fill_value` 파라미터와 `df.add(series, axis=...)`와 같은 메서드를 사용하여 연산 방식을 제어하는 방법을 숙지해야 합니다.
*   ⭐**데이터 재구성**: `set_index`/`reset_index`, `pivot`/`pivot_table`, `melt`를 이용하여 Wide-to-Long, Long-to-Wide 변환을 자유자재로 할 수 있어야 합니다. `pivot`과 `pivot_table`의 주요 차이점(집계 함수 사용 여부)을 구분할 수 있어야 합니다.

---

## Slide 41

### DataFrame Anatomy: axes, columns, dtypes, index

**핵심 개념**:
pandas DataFrame은 2차원 테이블 형태의 자료구조로, 행(row)과 열(column)을 가지고 있습니다. 각 열은 고유한 데이터 타입을 가질 수 있으며, 행과 열에는 각각 레이블(index와 columns)이 부여됩니다.

*   **Axes (축)**:
    *   `axis=0`: 행(row)을 따라 동작하는 축입니다. 주로 수직 방향 연산(예: 각 열의 평균 계산)에 사용됩니다.
    *   `axis=1`: 열(column)을 따라 동작하는 축입니다. 주로 수평 방향 연산(예: 각 행의 합계 계산)에 사용됩니다.
*   **Labels (레이블)**:
    *   `df.index`: DataFrame의 행 레이블(인덱스)을 나타내며, `pd.Index` 객체입니다. 기본적으로 0부터 시작하는 정수형 인덱스가 부여됩니다.
    *   `df.columns`: DataFrame의 열 레이블(컬럼명)을 나타내며, `pd.Index` 객체입니다.
*   **Types (데이터 타입)**:
    *   `df.dtypes`: DataFrame의 각 열(컬럼)에 대한 데이터 타입을 보여줍니다. pandas의 각 컬럼은 `pd.Series` 객체이며, Series는 하나의 단일 데이터 타입을 가집니다 (예: `object`, `np.int32`, `np.float64`).
*   **NumPy 변환**: DataFrame이나 특정 Series의 데이터를 내부적으로는 NumPy 배열(`np.array`)로 저장하며, 필요한 경우 명시적으로 NumPy 배열로 변환할 수 있습니다.

**코드/수식 해설**:
DataFrame의 각 구성 요소에 접근하는 방법과 NumPy 변환 예시입니다.

```python
import pandas as pd
import numpy as np

# 예시 DataFrame 생성
data = {
    'city': ['Oslo', 'Vienna', 'Tokyo'],
    'population': [698660, 1911191, 14043239],
    'area': [480.8, 414.8, 2194.1]
}
df = pd.DataFrame(data)

print("--- DataFrame (df) ---")
print(df)
print("\n")

# 1. df.index: 행 레이블(인덱스) 접근
print("--- df.index ---")
print(df.index) # Output: RangeIndex(start=0, stop=3, step=1)
print("\n")

# 2. df.columns: 열 레이블(컬럼명) 접근
print("--- df.columns ---")
print(df.columns) # Output: Index(['city', 'population', 'area'], dtype='object')
print("\n")

# 3. df.dtypes: 각 열의 데이터 타입 확인
print("--- df.dtypes ---")
print(df.dtypes)
# Output:
# city           object
# population      int64
# area          float64
# dtype: object
print("\n")

# 4. 특정 컬럼(Series)의 데이터 타입: 각 컬럼은 Series이므로 Series의 dtype도 확인 가능
print("--- df['population'].dtype ---")
print(df['population'].dtype) # Output: int64
print("\n")

# 5. DataFrame 전체를 NumPy 배열로 변환
print("--- df.to_numpy() ---")
print(df.to_numpy())
# Output:
# [['Oslo' 698660 480.8]
#  ['Vienna' 1911191 414.8]
#  ['Tokyo' 14043239 2194.1]]
print("\n")

# 6. 특정 컬럼(Series)을 NumPy 배열로 변환
print("--- df['population'].to_numpy() ---")
print(df['population'].to_numpy()) # Output: [  698660  1911191 14043239]
```

**구체적 예시**:
우리가 엑셀 스프레드시트를 사용한다고 상상해 봅시다.
*   **DataFrame**은 전체 스프레드시트입니다.
*   **`axis=0`**는 스프레드시트의 각 행을 아래로 훑어보면서(예: 각 열의 합계를 구할 때) 작업하는 방향입니다.
*   **`axis=1`**는 스프레드시트의 각 열을 오른쪽으로 훑어보면서(예: 각 행의 평균을 구할 때) 작업하는 방향입니다.
*   **`df.index`**는 엑셀의 '1, 2, 3...'과 같은 행 번호입니다.
*   **`df.columns`**는 엑셀의 'A, B, C...' 또는 사용자가 지정한 '이름', '나이'와 같은 열 제목입니다.
*   **`df.dtypes`**는 '이름' 열은 텍스트(문자열), '나이' 열은 숫자(정수) 등 각 열에 어떤 종류의 데이터가 들어있는지를 나타냅니다.
*   **NumPy 변환**은 엑셀 데이터를 복사하여 다른 통계 프로그램(예: MATLAB)에 붙여넣어 순수 숫자 배열로 다루는 것과 유사합니다.

**시험 포인트**:
*   ⭐ **`axis=0`와 `axis=1`의 의미를 정확히 구분**: `axis=0`은 행(rows), `axis=1`은 열(columns)을 나타냅니다. 데이터 조작 시 이 개념의 이해가 필수적입니다.
*   ⭐ **DataFrame의 주요 구성 요소**: `index`, `columns`, `dtypes`가 무엇을 의미하는지, 그리고 이들에 어떻게 접근하는지 (예: `df.index`, `df.columns`, `df.dtypes`)를 숙지해야 합니다.
*   ⭐ **각 컬럼은 `pd.Series` 객체이며, 고유한 `dtype`을 가진다는 사실**: 이는 Series와 DataFrame 간의 관계를 이해하는 데 중요합니다.
*   **NumPy 배열로의 변환 방법**: `df.to_numpy()` 또는 `df['col'].to_numpy()`를 사용하여 데이터를 효율적으로 NumPy 연산에 활용하는 방법을 알아야 합니다.

---

## Slide 42

- - -
**핵심 개념**
이 슬라이드는 `pandas` DataFrame의 기본적인 구조(`Anatomy`)를 파이썬 코드를 통해 설명합니다. 특히 DataFrame을 생성하고, 인덱스(행)와 컬럼(열)에 접근하며, 각 컬럼의 데이터 타입을 확인하는 방법을 다룹니다. 또한, DataFrame의 데이터를 `NumPy` 배열로 변환하는 방법과 `axis` 인자를 사용하여 행 또는 열 방향으로 연산을 수행하는 개념을 소개합니다.

**코드/수식 해설**

```python
import pandas as pd
import numpy as np

# DataFrame 생성: 명시적인 dtypes와 함께 예시 테이블 재구성
df = pd.DataFrame({
    "city": pd.Series(["Oslo", "Vienna", "Tokyo"], dtype="object"),
    "population": pd.Series([698660, 1911191, 14043239], dtype=np.int32),
    "area": pd.Series([480.8, 414.8, 2194.1], dtype=np.float64)
})
```
- `pd.DataFrame({...})`: 딕셔너리를 사용하여 DataFrame을 생성합니다. 딕셔너리의 키는 컬럼 이름이 되고, 값은 각 컬럼의 데이터를 담는 `pd.Series` 객체가 됩니다.
- `pd.Series([...], dtype=...)`: 각 컬럼의 데이터를 `Series`로 정의하며, `dtype` 인자를 통해 명시적으로 데이터 타입을 지정합니다. `object`는 문자열, `np.int32`는 32비트 정수, `np.float64`는 64비트 부동소수점 수를 의미합니다.

```python
# 축(axis=0 행, axis=1 열) 및 레이블 검사
print("index (axis=0) :", df.index)
print("columns (axis=1) :", df.columns)
```
- `df.index`: DataFrame의 행 인덱스(labels)를 반환합니다. 기본적으로 `RangeIndex(start=0, stop=3, step=1)`와 같이 생성됩니다.
- `df.columns`: DataFrame의 열 인덱스(labels), 즉 컬럼 이름을 반환합니다. 예시에서는 `Index(['city', 'population', 'area'], dtype='object')`가 됩니다.
- `axis=0`: 행(row) 방향을 나타냅니다. (위에서 아래)
- `axis=1`: 열(column) 방향을 나타냅니다. (왼쪽에서 오른쪽)

```python
# 각 컬럼은 자체 dtype을 가진 Series입니다.
print("\nColumn dtypes:\n", df.dtypes)
```
- `df.dtypes`: DataFrame의 각 컬럼별 데이터 타입을 반환합니다. `Series` 형태로 출력됩니다.

```python
# NumPy로 변환 (Series는 1D, DataFrame은 2D)
print("\ncity -> numpy:", df["city"].to_numpy())
print("\npop+area -> numpy:\n", df[["population", "area"]].to_numpy())
```
- `df["city"].to_numpy()`: 특정 컬럼(`city`)을 선택하면 `Series` 객체가 되며, `.to_numpy()` 메서드를 사용하여 해당 `Series`를 1차원 `NumPy` 배열로 변환합니다.
- `df[["population", "area"]].to_numpy()`: 여러 컬럼(`population`, `area`)을 리스트로 선택하면 `DataFrame` 객체가 되며, `.to_numpy()` 메서드를 사용하여 해당 `DataFrame`을 2차원 `NumPy` 배열로 변환합니다.

```python
# 숫자형 컬럼에 대한 간단한 axis 데모
num = df[["population", "area"]]
print("\nColumn-wise sum (axis=0):\n", num.sum(axis=0))
print("\nRow-wise sum (axis=1):\n", num.sum(axis=1))
```
- `num.sum(axis=0)`: `axis=0`은 열(column) 방향으로 연산을 수행하라는 의미입니다. 각 컬럼의 모든 행 값들을 합산하여 결과를 `Series` 형태로 반환합니다.
- `num.sum(axis=1)`: `axis=1`은 행(row) 방향으로 연산을 수행하라는 의미입니다. 각 행의 모든 열 값들을 합산하여 결과를 `Series` 형태로 반환합니다.

**구체적 예시**
`df`는 '도시', '인구', '면적'이라는 세 가지 정보를 담고 있는 표와 같습니다.
- 'city' 컬럼은 도시 이름(문자열)을 담고 있고, 'population' 컬럼은 도시의 인구수(정수)를, 'area' 컬럼은 면적(실수)을 담고 있습니다. 각 정보의 종류에 따라 `dtype`을 다르게 지정하는 것은 엑셀에서 셀 서식을 지정하는 것과 유사합니다.
- `df.index`는 표의 왼쪽에 있는 행 번호(예: 0, 1, 2)와 같고, `df.columns`는 표의 맨 위에 있는 제목(예: city, population, area)과 같습니다.
- `df.dtypes`는 각 제목 아래의 정보가 어떤 형식(문자, 숫자 등)으로 되어있는지 한눈에 보여줍니다.
- `.to_numpy()`를 사용하면 이 표 형태의 데이터를 계산하기 편리한 순수한 숫자 배열로 바꿀 수 있습니다. 예를 들어, 'population'과 'area' 컬럼만 뽑아서 2D NumPy 배열로 만든 뒤, `num.sum(axis=0)`으로 각 컬럼별 총합(예: 전체 도시의 총 인구수, 총 면적)을 구하거나, `num.sum(axis=1)`으로 각 도시별 인구와 면적을 합친 값(이는 실제 데이터에서는 의미가 없을 수 있지만, `axis` 개념을 설명하기 위한 예시입니다)을 구할 수 있습니다.

**시험 포인트**
- ⭐ DataFrame을 딕셔너리(`dict`)와 `pd.Series`를 활용하여 생성하는 방법과 이때 `dtype`을 명시하는 방법을 이해해야 합니다.
- ⭐ `axis=0`이 행(row) 방향, `axis=1`이 열(column) 방향을 의미한다는 것을 정확히 숙지해야 합니다. 이는 pandas와 NumPy에서 데이터 연산의 기본 개념입니다.
- ⭐ `df.index`, `df.columns`, `df.dtypes`를 사용하여 DataFrame의 구조와 데이터 타입을 확인하는 방법을 알아야 합니다.
- ⭐ `Series`와 `DataFrame` 객체를 `.to_numpy()` 메서드를 사용하여 각각 1차원 또는 2차원 `NumPy` 배열로 변환하는 과정을 이해해야 합니다.
- ⭐ `DataFrame.sum()`과 같은 연산에서 `axis` 인자가 결과에 미치는 영향을 코드 예시와 함께 설명할 수 있어야 합니다. (예: `axis=0`은 열별 합계, `axis=1`은 행별 합계)
- ⭐ `Series`는 1차원 데이터 구조, `DataFrame`은 2차원 데이터 구조라는 점을 이해해야 합니다.

---

## Slide 43

**핵심 개념**
Pandas DataFrame은 2차원 테이블 형태의 데이터 구조로, 데이터를 효율적으로 저장하고 조작하는 데 사용됩니다. 이 슬라이드는 DataFrame을 생성하는 두 가지 주요 방법을 설명합니다: 외부 CSV 파일에서 데이터를 읽어오는 방법과 Python 딕셔너리로부터 직접 생성하는 방법입니다.

**코드/수식 해설**

1.  **CSV 파일로부터 DataFrame 생성**
    CSV(Comma Separated Values) 파일은 데이터를 쉼표로 구분하여 저장하는 일반적인 텍스트 파일 형식입니다. `pandas` 라이브러리의 `read_csv()` 함수를 사용하여 이 파일을 DataFrame으로 쉽게 불러올 수 있습니다.
    ```python
    import pandas as pd # pandas 라이브러리를 pd라는 별칭으로 임포트
    
    # "elections.csv" 파일을 읽어와 DataFrame 객체 'elections'에 할당
    elections = pd.read_csv("elections.csv") 
    
    # DataFrame의 상위 2개 행을 출력하여 데이터 확인
    print(elections.head(2))
    ```
    *   `pd.read_csv(filename)`: 지정된 `filename` (경로 포함)의 CSV 파일을 읽어와 pandas DataFrame 객체로 반환합니다.
    *   `DataFrame.head(n)`: DataFrame의 첫 `n`개 행을 반환합니다. `n`을 생략하면 기본값으로 5개 행을 반환합니다. 데이터가 올바르게 로드되었는지 빠르게 확인하는 데 유용합니다.

2.  **딕셔너리로부터 DataFrame 생성**
    Python 딕셔너리는 키(key)-값(value) 쌍으로 이루어진 데이터 구조입니다. 딕셔너리를 사용하여 DataFrame을 생성할 때는 딕셔너리의 키가 DataFrame의 컬럼 이름이 되고, 해당 키의 값이 리스트 형태여야 하며 각 리스트는 해당 컬럼의 데이터를 나타냅니다. 모든 리스트의 길이는 동일해야 합니다.
    ```python
    # 학생 데이터를 담은 딕셔너리 생성
    student_data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Math': [85, 92, 78],
        'Science': [88, 95, 82]
    }
    
    # 딕셔너리 'student_data'를 사용하여 DataFrame 객체 'df' 생성
    df = pd.DataFrame(student_data)
    
    # 생성된 DataFrame 출력
    print(df)
    ```
    *   `pd.DataFrame(data_dict)`: 딕셔너리 `data_dict`를 인자로 받아 DataFrame 객체를 생성합니다. 딕셔너리의 키는 DataFrame의 컬럼 이름이 되고, 값은 해당 컬럼의 데이터 리스트가 됩니다.

**구체적 예시**

*   **CSV 파일 예시**: `elections.csv`라는 파일에 연도(Year), 후보(Candidate), 정당(Party), 득표수(Popular vote), 결과(Result) 등의 선거 데이터가 행과 열의 형태로 저장되어 있다고 가정합니다. `pd.read_csv("elections.csv")`를 실행하면, 이 파일의 내용이 `elections`라는 이름의 DataFrame으로 메모리에 로드되어 마치 스프레드시트처럼 다룰 수 있게 됩니다. `elections.head(2)`는 데이터의 상단 두 줄을 보여주어 데이터가 예상대로 로드되었는지 시각적으로 확인할 수 있게 합니다.

*   **딕셔너리 예시**: 세 명의 학생(Alice, Bob, Charlie)의 이름, 수학 점수, 과학 점수를 가지고 있다면, 이를 `student_data`라는 딕셔너리로 구성할 수 있습니다. `pd.DataFrame(student_data)`를 호출하면, 'Name', 'Math', 'Science' 세 개의 컬럼과 각 학생에 해당하는 세 개의 행으로 이루어진 테이블 형태의 DataFrame이 생성됩니다. 이 DataFrame은 학생별 성적을 한눈에 파악하고 분석하는 데 유용하게 사용됩니다.

**시험 포인트**

*   ⭐`pd.read_csv()` 함수의 사용법과, 데이터를 외부 파일에서 로드하는 가장 기본적인 방법임을 반드시 이해해야 합니다. 파일 경로 지정에 유의하세요.
*   ⭐Python 딕셔너리를 사용하여 DataFrame을 생성하는 방법도 중요합니다. 딕셔너리의 '키'가 DataFrame의 '컬럼 이름'이 되고, '값'이 해당 컬럼의 '데이터 리스트'가 된다는 점, 그리고 모든 데이터 리스트의 길이가 같아야 한다는 제약 조건을 기억하세요.
*   ⭐데이터 로드 후 `DataFrame.head()` 메서드를 사용하여 데이터의 초기 부분을 확인하는 습관은 데이터 분석 과정에서 매우 중요하며, 오류를 초기에 발견하는 데 도움이 됩니다.

---

## Slide 44

**핵심 개념**
*   **CSV (Comma-Separated Values)**: 쉼표(,)로 구분된 텍스트 파일 형식으로, 테이블 형태의 데이터를 저장하는 데 널리 사용됩니다. 각 줄은 하나의 데이터 레코드를 나타내고, 레코드 내의 각 필드는 쉼표로 구분됩니다.
*   **`pandas.read_csv()`**: Python의 pandas 라이브러리에서 CSV 파일을 읽어 DataFrame 객체로 변환하는 핵심 함수입니다. 이 함수는 데이터를 빠르고 효율적으로 불러올 수 있게 해줍니다.
*   **헤더(Header)**: CSV 파일의 첫 번째 줄은 종종 각 열의 이름을 정의하는 헤더(컬럼명)로 사용됩니다. `pd.read_csv()`는 기본적으로 첫 번째 줄을 헤더로 간주하여 DataFrame의 컬럼명으로 사용합니다.
*   **데이터 타입 추론 (dtype inference)**: `pd.read_csv()`는 데이터를 불러올 때 각 컬럼의 내용을 분석하여 적절한 데이터 타입(예: 문자열, 정수, 실수)을 자동으로 추론합니다.

**코드/수식 해설**

*   **기본 CSV 파일 읽기**:
    `pd.read_csv()` 함수를 사용하여 CSV 파일을 DataFrame으로 로드합니다.

    ```python
    import pandas as pd

    # cities.csv 파일이 'name,population,area\nOslo,698660,480.8\nVienna,1911191,414.8\nTokyo,14043239,2194.1' 라고 가정
    df = pd.read_csv('cities.csv')
    ```
    위 코드를 실행하면 `cities.csv` 파일의 첫 번째 줄(`name,population,area`)이 DataFrame의 컬럼명으로 사용되고, 이어지는 줄들이 데이터로 로드됩니다.

*   **헤더가 없는 CSV 파일 처리**:
    만약 CSV 파일에 헤더(컬럼명)가 없다면, `header=None` 옵션을 사용하여 첫 번째 줄을 데이터로 간주하고 pandas가 기본 정수 인덱스(0, 1, 2...)를 컬럼명으로 할당하도록 지시합니다.

    ```python
    # cities_no_header.csv 파일이 'Oslo,698660,480.8\nVienna,1911191,414.8\nTokyo,14043239,2194.1' 라고 가정
    df_no_header = pd.read_csv('cities_no_header.csv', header=None)
    ```
    이 경우, DataFrame의 컬럼명은 0, 1, 2와 같은 숫자가 됩니다.

**구체적 예시**

`cities.csv` 파일 내용이 다음과 같다고 가정해 봅시다:
```
name,population,area
Oslo,698660,480.8
Vienna,1911191,414.8
Tokyo,14043239,2194.1
```

1.  **파일 생성 (예시를 위한 가상 작업)**:
    ```python
    # 실제 파일로 저장한다고 가정
    with open('cities.csv', 'w') as f:
        f.write('name,population,area\n')
        f.write('Oslo,698660,480.8\n')
        f.write('Vienna,1911191,414.8\n')
        f.write('Tokyo,14043239,2194.1\n')
    ```

2.  **`pd.read_csv()` 실행**:
    ```python
    import pandas as pd
    df = pd.read_csv('cities.csv')
    print(df)
    ```
    결과는 다음과 같은 DataFrame이 됩니다:
    ```
         name  population    area
    0    Oslo      698660   480.8
    1  Vienna     1911191   414.8
    2   Tokyo    14043239  2194.1
    ```
    여기서 `name`, `population`, `area`는 `cities.csv`의 첫 줄에서 가져온 컬럼명입니다. `population`은 `int64`, `area`는 `float64` 등으로 데이터 타입이 자동으로 추론됩니다.

3.  **헤더 없는 CSV 예시**:
    `cities_no_header.csv` 파일 내용이 다음과 같다고 가정해 봅시다:
    ```
    Oslo,698660,480.8
    Vienna,1911191,414.8
    Tokyo,14043239,2194.1
    ```
    ```python
    # 실제 파일로 저장한다고 가정
    with open('cities_no_header.csv', 'w') as f:
        f.write('Oslo,698660,480.8\n')
        f.write('Vienna,1911191,414.8\n')
        f.write('Tokyo,14043239,2194.1\n')

    df_no_header = pd.read_csv('cities_no_header.csv', header=None)
    print(df_no_header)
    ```
    결과는 다음과 같습니다. pandas가 자동으로 0부터 시작하는 숫자 컬럼명을 부여했습니다:
    ```
          0         1       2
    0    Oslo    698660   480.8
    1  Vienna   1911191   414.8
    2   Tokyo  14043239  2194.1
    ```

**시험 포인트**
*   ⭐`pd.read_csv()` 함수는 CSV 파일을 DataFrame으로 로드하는 데 사용되는 **가장 기본적이고 중요한 함수**입니다.
*   ⭐`pd.read_csv()`는 기본적으로 **CSV 파일의 첫 번째 줄을 헤더(컬럼명)로 간주**합니다.
*   ⭐CSV 파일에 헤더가 없는 경우, `pd.read_csv()` 함수에 **`header=None` 인자를 사용하여 첫 줄을 데이터로 처리**하도록 해야 합니다.
*   ⭐pandas는 CSV 파일을 읽을 때 각 컬럼의 내용을 바탕으로 **적절한 데이터 타입(dtypes)을 자동으로 추론**합니다. (예: 정수, 실수, 문자열 등)
*   ⭐CSV는 **Comma-Separated Values**의 약자로, 쉼표로 값이 구분된 텍스트 파일 형식이라는 점을 이해하고 있어야 합니다.

---

## Slide 45

---
**핵심 개념**:
`pandas.read_csv()` 함수는 CSV(Comma Separated Values) 형식의 파일을 읽어 DataFrame으로 변환하는 데 사용됩니다. 이 슬라이드는 특히 비표준적인 구분자, 숫자 형식(로캘), 주석 처리된 줄, 불필요한 공백 등 다양한 CSV 파일 형식을 유연하게 처리하기 위한 `read_csv()`의 주요 파싱 옵션들을 설명합니다.

*   **필드 구분자 (Field Separator)**: 데이터의 각 필드를 구분하는 문자 (예: 쉼표 `,`, 세미콜론 `;`, 탭 `\t`).
*   **로캘(Locale) 기반 숫자 형식**: 유럽식 숫자 형식처럼 천 단위 구분자로 아포스트로피(`'`)나 마침표(`.`)를 사용하고, 소수점 구분자로 쉼표(`,`)를 사용하는 경우를 처리합니다.
*   **초기 공백 무시 (Initial Space Skipping)**: 구분자 뒤에 오는 불필요한 공백을 무시하여 데이터가 올바르게 파싱되도록 합니다.
*   **줄 건너뛰기/주석 처리 (Line Skipping/Commenting)**: 파일의 시작 부분에 있는 불필요한 정보 줄(예: 메타데이터, 헤더 정보)을 건너뛰거나 특정 문자로 시작하는 줄을 주석으로 처리하여 파싱에서 제외합니다.

**코드/수식 해설**:
본 슬라이드에는 직접적인 수식은 포함되어 있지 않습니다.
`pandas.read_csv()` 함수의 주요 인자들은 다음과 같습니다:

*   `sep` 또는 `delimiter`: 필드를 구분하는 문자열입니다. 기본값은 쉼표(`,`)입니다.
*   `thousands`: 숫자 데이터에서 천 단위 구분자로 사용되는 문자열입니다. 파싱 시 이 문자를 제거합니다.
*   `decimal`: 숫자 데이터에서 소수점 구분자로 사용되는 문자열입니다. 파싱 시 이 문자를 표준 마침표(`.`)로 변환합니다.
*   `skipinitialspace`: `True`로 설정하면 구분자 뒤의 공백(whitespace)을 건너뜁니다.
*   `skiprows`: 파일의 시작 부분에서 건너뛸 줄의 개수를 지정합니다. 정수(예: `skiprows=1`) 또는 리스트(예: `skiprows=[0, 2]`)로 지정할 수 있습니다.
*   `comment`: 이 문자로 시작하는 줄을 주석으로 처리하고 파싱에서 제외합니다.

**구체적 예시**:

다음과 같은 유럽식 형식의 데이터가 포함된 CSV 파일(또는 문자열)이 있다고 가정해 봅시다.

```
# 2020 census
name; population; area
Oslo; 698'660; 480,8
Vienna; 1'911'191; 414,8
Tokyo; 14'043'239; 2'194,1
```

이 데이터를 `pandas`로 올바르게 읽어오려면, 세미콜론(`;`)을 구분자로, 아포스트로피(`'`)를 천 단위 구분자로, 쉼표(`,`)를 소수점 구분자로, 첫 번째 줄(`#`)을 주석으로 처리해야 합니다.

```python
import pandas as pd
import io

csv_data = """# 2020 census
name; population; area
Oslo; 698'660; 480,8
Vienna; 1'911'191; 414,8
Tokyo; 14'043'239; 2'194,1
"""

# read_csv() 함수를 사용하여 데이터 파싱
df = pd.read_csv(
    io.StringIO(csv_data),
    sep=';',              # 필드 구분자: 세미콜론
    comment='#',          # 주석 문자: #
    thousands="'",        # 천 단위 구분자: 아포스트로피
    decimal=',',          # 소수점 구분자: 쉼표
    skipinitialspace=True # 구분자 뒤의 공백 무시
)

print(df)
```

**출력 결과**:

```
     name  population     area
0    Oslo      698660    480.8
1  Vienna     1911191    414.8
2   Tokyo    14043239   2194.1
```

결과 DataFrame을 보면 `population`과 `area` 컬럼의 숫자 데이터가 올바르게 파싱되어 숫자(정수 및 실수) 타입으로 변환되었음을 알 수 있습니다. 특히 `thousands`와 `decimal` 옵션 덕분에 유럽식 숫자 형식이 표준 Python/pandas 숫자 형식으로 변환되었습니다. `comment` 옵션 덕분에 첫 줄인 `# 2020 census`는 무시되었습니다.

**시험 포인트**:
*   ⭐ **`pandas.read_csv()` 함수의 다양한 파라미터(특히 `sep`, `thousands`, `decimal`, `skiprows`, `comment`, `skipinitialspace`)의 역할과 사용법을 정확히 이해하고 있어야 합니다.**
*   ⭐ **각 파라미터가 어떤 종류의 CSV 파일 문제(예: 다른 구분자, 유럽식 숫자 형식, 불필요한 헤더/푸터, 주석)를 해결하는 데 사용되는지 연결 지어 설명할 수 있어야 합니다.**
*   ⭐ **주어진 CSV 데이터의 특정 포맷에 맞춰 `read_csv()` 함수 호출 시 적절한 파라미터를 선택하여 적용하는 문제**가 출제될 수 있습니다. (예: "다음 CSV 파일을 pandas DataFrame으로 올바르게 읽기 위한 `read_csv` 호출 코드를 작성하시오.")
---

---

## Slide 46

## pd.read_csv / df.to_csv: 필수 인자

### 핵심 개념
Pandas 라이브러리는 데이터 분석에서 가장 흔히 사용되는 CSV (Comma Separated Values) 파일을 DataFrame으로 읽어오거나 DataFrame을 CSV 파일로 저장하는 강력한 기능을 제공합니다. `pd.read_csv()`는 CSV 파일을 메모리의 DataFrame 객체로 변환하고, `df.to_csv()`는 DataFrame 객체를 지정된 경로에 CSV 파일로 저장합니다. 이 두 함수는 데이터 입출력의 기본이 되며, 다양한 옵션을 통해 데이터를 효율적으로 제어할 수 있습니다.

### 코드/수식 해설

#### `pd.read_csv()` 필수 인자 및 설명
```python
pd.read_csv(
    filename,             # 필수: 읽어올 CSV 파일의 경로 (문자열)
    sep=',',              # 필드(열) 구분자. 기본값은 쉼표(','), 탭('\t') 또는 파이프('|') 등을 사용할 수 있음
    skipinitialspace=False, # 구분자(sep) 뒤의 공백을 건너뛸지 여부. True인 경우 "A, B"에서 B 앞의 공백 무시
    quotechar='"',        # 따옴표로 묶인 문자열을 처리할 때 사용되는 따옴표 문자. 기본값은 큰따옴표('"')
    skiprows=n,           # 파일의 첫 n줄을 건너뛰고 데이터를 읽음 (0부터 시작).
    usecols=columns,      # 특정 열만 선택하여 읽어올 때 사용. 열 이름 리스트 또는 인덱스 리스트 전달
    nrows=n,              # 파일의 첫 n개의 행만 읽어옴. 대용량 파일에서 샘플링이나 청크 단위로 읽을 때 유용
    index_col=columns,    # 특정 열(들)을 DataFrame의 인덱스로 설정. 열 이름 또는 인덱스 리스트 전달
    ...                   # 약 50개 이상의 추가 인자들이 있음 (encoding, dtype, na_values 등)
)
```

#### `df.to_csv()` 필수 인자 및 설명
```python
df.to_csv(
    filename,             # 필수: 저장할 CSV 파일의 경로 (문자열)
    index=True/False,     # DataFrame의 인덱스를 CSV 파일에 첫 번째 열로 저장할지 여부. 기본값은 True
    sep=',',              # 필드(열) 구분자. 기본값은 쉼표(',')
    na_rep='',            # NaN(결측값)을 CSV 파일에 어떤 문자열로 표현할지 지정. 기본값은 빈 문자열
    ...                   # 추가 인자들 (encoding, header 등)
)
```

### 구체적 예시

**1. CSV 파일 생성 (예시용)**
`data.csv` 파일을 다음과 같이 생성한다고 가정합니다:
```csv
id,name,score,grade
1,Alice,85,A
2,Bob,72,B
3,Charlie,,C
4,David,90,A
# This is a comment line
5,Eve,68,D
```
여기서 세 번째 행의 Charlie는 score가 비어있고, `#`으로 시작하는 주석 라인이 있습니다.

**2. `pd.read_csv()` 예시**

*   **기본 읽기:**
    ```python
    import pandas as pd
    df_basic = pd.read_csv('data.csv')
    print(df_basic)
    ```
    ```
       id     name  score grade
    0   1    Alice   85.0     A
    1   2      Bob   72.0     B
    2   3  Charlie    NaN     C
    3   4    David   90.0     A
    4   5      Eve   68.0     D
    ```
    (주석 라인은 자동으로 무시되지 않을 수 있으므로 주의. `comment='#'` 인자를 사용해야 함)

*   **특정 열만 읽기 (`usecols`) 및 첫 n행 건너뛰기 (`skiprows`):**
    `id`와 `name` 열만 읽고, 첫 번째 데이터 행과 주석을 건너뛰려면 (`skiprows=2`는 첫 줄 헤더, 두 번째 줄 데이터 무시):
    ```python
    df_subset = pd.read_csv('data.csv', usecols=['name', 'score'], skiprows=[0, 4]) # 0번(헤더), 4번(주석) 행 건너뛰기
    print(df_subset)
    ```
    ```
          name  score
    0      Bob   72.0
    1  Charlie    NaN
    2    David   90.0
    3      Eve   68.0
    ```
    이 예시에서는 `skiprows=[0, 4]`를 사용하여 첫 행(헤더)과 5번째 행(주석)을 건너뛰었습니다. (실제 데이터 읽기에서는 `skiprows`와 `comment` 인자를 적절히 조합하여 사용합니다.)

*   **인덱스 열 설정 (`index_col`) 및 일부 행만 읽기 (`nrows`):**
    `id` 열을 인덱스로 사용하고 처음 3개의 데이터 행만 읽어옵니다.
    ```python
    df_indexed_chunk = pd.read_csv('data.csv', index_col='id', nrows=3)
    print(df_indexed_chunk)
    ```
    ```
         name  score grade
    id                    
    1   Alice   85.0     A
    2     Bob   72.0     B
    3 Charlie    NaN     C
    ```

**3. `df.to_csv()` 예시**

*   **DataFrame을 CSV로 저장 (인덱스 포함):**
    ```python
    # 위에서 생성된 df_basic DataFrame을 사용
    df_basic.to_csv('output_with_index.csv')
    ```
    `output_with_index.csv` 파일 내용:
    ```csv
    ,id,name,score,grade
    0,1,Alice,85.0,A
    1,2,Bob,72.0,B
    2,3,Charlie,,C
    3,4,David,90.0,A
    4,5,Eve,68.0,D
    ```
    (첫 번째 열은 DataFrame의 인덱스)

*   **DataFrame을 CSV로 저장 (인덱스 제외 및 결측값(`na_rep`) 처리):**
    ```python
    df_basic.to_csv('output_no_index_na_filled.csv', index=False, na_rep='N/A')
    ```
    `output_no_index_na_filled.csv` 파일 내용:
    ```csv
    id,name,score,grade
    1,Alice,85.0,A
    2,Bob,72.0,B
    3,Charlie,N/A,C
    4,David,90.0,A
    5,Eve,68.0,D
    ```
    (DataFrame의 인덱스가 저장되지 않고, NaN 값이 'N/A'로 대체됨)

### 시험 포인트
*   ⭐ **`pd.read_csv()`의 핵심 기능**: CSV 파일을 DataFrame으로 변환.
*   ⭐ **`df.to_csv()`의 핵심 기능**: DataFrame을 CSV 파일로 저장.
*   ⭐ **데이터 로딩/저장 시 유용한 인자**:
    *   `pd.read_csv()`:
        *   `sep`: 데이터 구분자 지정 (콤마, 탭, 세미콜론 등).
        *   `skiprows`: 특정 행을 건너뛰어 읽기 (헤더 없는 파일, 주석 등).
        *   `usecols`: 특정 열만 선택하여 읽기 (메모리 및 처리 시간 절약).
        *   `nrows`: 지정된 수만큼의 행만 읽기 (대용량 파일 미리보기, 청크 처리).
        *   `index_col`: 특정 열을 DataFrame의 인덱스로 설정.
    *   `df.to_csv()`:
        *   `index=False`: DataFrame 인덱스를 파일에 저장하지 않도록 설정 (가장 흔히 사용).
        *   `na_rep`: 결측값(NaN)을 파일에 저장할 때 사용할 문자열 지정.
*   ⭐ **데이터 분석 워크플로우에서 이 함수들의 역할**: 데이터 준비 단계에서 외부 데이터를 불러오고, 처리된 데이터를 저장하는 가장 기본적인 방법.

---

## Slide 47

**핵심 개념**
Pandas DataFrame에서 인덱스를 설정하는 방법은 크게 두 가지가 있습니다. 첫째는 CSV 파일과 같은 데이터를 읽어오는 시점에 인덱스를 지정하는 것이고, 둘째는 데이터를 DataFrame으로 불러온 후에 특정 컬럼을 인덱스로 재설정하는 것입니다. 두 방법 모두 결과적으로 동일한 형태의 DataFrame을 생성하지만, 내부적인 처리 효율성에서 차이가 있습니다.

**코드/수식 해설**

1.  **데이터를 읽은 후 인덱스 설정**:
    ```python
    import pandas as pd

    # 1. CSV 파일 읽기 (기본 정수 인덱스 사용)
    df = pd.read_csv('cities.csv')
    print("DataFrame after initial read:")
    print(df)

    # 2. 'name' 컬럼을 인덱스로 설정
    df = df.set_index('name')
    print("\nDataFrame after df.set_index('name'):")
    print(df)
    ```
    이 방법은 `cities.csv` 파일을 먼저 읽어 기본 인덱스(0, 1, 2...)를 가진 DataFrame을 생성한 후, `set_index()` 메서드를 사용하여 'name' 컬럼을 새로운 인덱스로 지정합니다. `set_index()`는 기본적으로 새로운 DataFrame을 반환하므로, `df = ...`와 같이 다시 할당해 주어야 합니다.

2.  **데이터를 읽는 시점에 인덱스 설정**:
    ```python
    import pandas as pd

    # CSV 파일을 읽는 동시에 'name' 컬럼을 인덱스로 지정
    df_optimized = pd.read_csv('cities.csv', index_col='name')
    print("\nDataFrame after pd.read_csv(index_col='name'):")
    print(df_optimized)
    ```
    이 방법은 `pd.read_csv()` 함수 호출 시 `index_col` 파라미터를 사용하여 'name' 컬럼을 DataFrame의 인덱스로 직접 지정합니다.

**구체적 예시**
`cities.csv` 파일이 다음과 같이 구성되어 있다고 가정합니다:
```csv
name,population,area
Oslo,698660,480.8
Vienna,1911191,414.8
Tokyo,14043239,2194.1
```

1.  **데이터를 읽은 후 인덱스 설정 (`df = pd.read_csv('cities.csv'); df = df.set_index('name')`)**
    처음 `pd.read_csv('cities.csv')`를 실행하면 DataFrame은 다음과 같습니다:
    ```
       name  population      area
    0  Oslo      698660     480.8
    1  Vienna   1911191     414.8
    2  Tokyo  14043239    2194.1
    ```
    이후 `df.set_index('name')`을 적용하면 DataFrame은 다음과 같이 변경됩니다:
    ```
               population      area
    name
    Oslo           698660     480.8
    Vienna        1911191     414.8
    Tokyo        14043239    2194.1
    ```

2.  **데이터를 읽는 시점에 인덱스 설정 (`df = pd.read_csv('cities.csv', index_col='name')`)**
    이 코드를 실행하면 처음부터 'name' 컬럼이 인덱스로 설정된 DataFrame이 생성됩니다:
    ```
               population      area
    name
    Oslo           698660     480.8
    Vienna        1911191     414.8
    Tokyo        14043239    2194.1
    ```
    결과적으로 두 방법 모두 최종 DataFrame의 형태는 동일합니다.

**시험 포인트**
*   ⭐ **`pd.read_csv()` 함수의 `index_col` 파라미터의 중요성:** 데이터를 파일에서 읽어올 때 특정 컬럼을 DataFrame의 인덱스로 바로 지정할 수 있는 매우 유용한 기능입니다.
*   ⭐ **성능 및 효율성 차이:** `pd.read_csv(..., index_col='컬럼명')`을 사용하는 것이 데이터를 먼저 읽은 후 `df.set_index('컬럼명')`을 호출하는 것보다 효율적입니다. `index_col`을 사용하면 데이터 프레임을 한 번만 생성하며, 불필요한 "추가 복사(extra copy)"를 피할 수 있어 대용량 데이터를 처리할 때 메모리 사용량과 처리 시간을 절약할 수 있습니다.
*   ⭐ 두 방식 모두 최종적으로는 동일한 구조의 DataFrame을 생성하지만, 내부 처리 방식의 차이로 인해 특히 성능이 중요한 상황에서는 `index_col` 사용이 권장됩니다.

---

## Slide 48

**핵심 개념**
Pandas `DataFrame`은 데이터를 테이블 형태로 저장하는 2차원 자료구조입니다. 이 슬라이드는 Python의 기본 자료구조인 리스트(List)와 Pandas의 1차원 자료구조인 Series를 사용하여 DataFrame을 생성하는 두 가지 추가적인 방법을 설명합니다.

1.  **2차원 리스트(Nested Lists)로부터 DataFrame 생성**: 데이터를 행(row) 단위로 구성된 중첩 리스트 형태로 준비하고, `pd.DataFrame()` 함수의 `data` 인수에 리스트를 전달하여 DataFrame을 만듭니다. 이때 `columns` 인수를 사용하여 각 열의 이름을 지정할 수 있습니다.
2.  **Series 객체들로부터 DataFrame 생성**: 각각의 열(column)이 될 데이터를 `pd.Series` 객체로 생성한 후, 이 Series 객체들을 사전(dictionary) 형태로 묶어 `pd.DataFrame()` 함수에 전달하여 DataFrame을 만듭니다. 사전의 키(key)가 DataFrame의 열 이름이 되고, 값(value)이 해당 Series 데이터가 됩니다.

**코드/수식 해설**
(이 슬라이드에는 수식이 없습니다.)

**1. 2차원 리스트로부터 DataFrame 생성**
```python
import pandas as pd

# Creating DataFrame from nested lists
data = [['Alice', 85, 88], ['Bob', 92, 95], ['Charlie', 78, 82]]
df = pd.DataFrame(data, columns=['Name', 'Math', 'Science'])
print(df)
```
*   `data`: `[['Alice', 85, 88], ...]`는 3개의 행을 가진 중첩 리스트입니다. 각 내부 리스트는 한 사람의 이름과 두 과목 점수를 나타냅니다.
*   `pd.DataFrame(data, columns=['Name', 'Math', 'Science'])`: `data` 리스트를 기반으로 DataFrame을 생성합니다. `columns` 인수에 리스트를 전달하여 각 열의 이름을 'Name', 'Math', 'Science'로 지정합니다. 이 순서는 `data` 리스트의 각 내부 리스트 요소의 순서와 일치해야 합니다.

**2. Series 객체들로부터 DataFrame 생성**
```python
import pandas as pd

# Combining Series into DataFrame
names = pd.Series(['Alice', 'Bob', 'Charlie'])
math_scores = pd.Series([85, 92, 78])
df = pd.DataFrame({'Name': names, 'Math': math_scores})
print(df)
```
*   `names = pd.Series(...)`: 이름 데이터를 담는 Series를 생성합니다. 기본적으로 0부터 시작하는 정수형 인덱스를 가집니다.
*   `math_scores = pd.Series(...)`: 수학 점수 데이터를 담는 Series를 생성합니다. 이 또한 기본 인덱스를 가집니다.
*   `pd.DataFrame({'Name': names, 'Math': math_scores})`: 사전 `{'Name': names, 'Math': math_scores}`를 `pd.DataFrame()`에 전달하여 DataFrame을 생성합니다. 사전의 키('Name', 'Math')는 DataFrame의 열 이름이 되고, 값(Series `names`, `math_scores`)은 해당 열의 데이터가 됩니다. Series의 인덱스가 자동으로 맞춰져 DataFrame의 행 인덱스로 사용됩니다.

**구체적 예시**

**1. 2차원 리스트로부터 DataFrame 생성 예시 출력:**

```
      Name  Math  Science
0    Alice    85       88
1      Bob    92       95
2  Charlie    78       82
```
위 코드를 실행하면, `data` 리스트의 각 내부 리스트가 한 행이 되고, `columns`로 지정된 이름이 각 열의 헤더가 되어 학생들의 성적표와 같은 테이블 형태의 데이터가 생성됩니다. 'Alice'의 데이터는 첫 번째 행(인덱스 0), 'Bob'은 두 번째 행(인덱스 1)에 해당합니다.

**2. Series 객체들로부터 DataFrame 생성 예시 출력:**

```
      Name  Math
0    Alice    85
1      Bob    92
2  Charlie    78
```
이 예시에서는 `names` Series의 인덱스와 `math_scores` Series의 인덱스가 자동으로 맞춰져 DataFrame의 행이 구성됩니다. `names` Series의 0번 인덱스 'Alice'와 `math_scores` Series의 0번 인덱스 85가 첫 번째 행을 이루는 식입니다. 만약 두 Series의 인덱스가 다르다면, pandas는 해당 인덱스에 매칭되는 값이 없는 경우 `NaN` (Not a Number)으로 채워서 DataFrame을 생성합니다.

**시험 포인트**

*   ⭐ **DataFrame 생성 방법의 이해**: 2차원 리스트와 Series 객체를 활용한 `DataFrame` 생성 방법의 차이점과 공통점을 정확히 이해해야 합니다.
*   ⭐ **`columns` 인수의 역할**: 2차원 리스트로 생성 시 `columns` 인수를 사용하여 열 이름을 지정하는 방법을 알아야 합니다.
*   ⭐ **Series를 이용한 생성 시 딕셔너리 구조**: Series 객체들을 딕셔너리로 묶어 DataFrame을 만들 때, 딕셔너리의 키가 열 이름이 된다는 것을 숙지해야 합니다.
*   ⭐ **인덱스 매칭**: Series 객체들로 DataFrame을 생성할 때, pandas가 Series의 인덱스를 기반으로 데이터를 자동으로 정렬하고 매칭한다는 점을 이해해야 합니다. (다른 인덱스를 가진 Series 결합 시 `NaN` 발생 가능성도 중요)

---

## Slide 49

**핵심 개념**

*   **DataFrame 속성 (Attributes)**: pandas DataFrame 객체는 데이터를 구성하는 핵심 요소(데이터 값) 외에도 데이터의 구조와 특성을 파악하는 데 필수적인 다양한 속성(attributes)을 제공합니다. 이 속성들을 통해 DataFrame의 행 및 열 레이블, 차원, 각 컬럼의 데이터 타입 등을 쉽게 확인할 수 있으며, 데이터 분석의 초기 단계에서 데이터를 이해하는 데 매우 중요합니다.
*   **`df.index`**: DataFrame의 행(row) 레이블(index) 정보를 담고 있는 객체입니다. 별도로 지정하지 않으면 0부터 시작하는 정수형 `RangeIndex`가 기본으로 사용됩니다.
*   **`df.columns`**: DataFrame의 열(column) 레이블 정보를 담고 있는 객체입니다. DataFrame 생성 시 딕셔너리의 키(key)가 컬럼 이름이 됩니다.
*   **`df.shape`**: DataFrame의 차원(dimensionality)을 나타내는 튜플을 반환합니다. `(행의 개수, 열의 개수)` 순서로 구성됩니다.
*   **`df.dtypes`**: 각 컬럼의 데이터 타입을 나타내는 pandas Series를 반환합니다. `object` (문자열), `int64` (정수), `float64` (실수) 등이 주요 데이터 타입입니다.

**코드/수식 해설**

```python
import pandas as pd

# 1. 샘플 DataFrame 생성
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 92, 78],
    'Science': [88, 95, 82]
})
```
*   `import pandas as pd`: 데이터 분석을 위한 pandas 라이브러리를 `pd`라는 별칭으로 불러옵니다.
*   `pd.DataFrame({...})`: 딕셔너리를 인자로 사용하여 DataFrame을 생성합니다. 딕셔너리의 키(`'Name'`, `'Math'`, `'Science'`)는 DataFrame의 컬럼 이름이 되고, 해당 키의 값(리스트)은 각 컬럼의 데이터가 됩니다.

```python
print("Index:", df.index)
# 출력: Index: RangeIndex(start=0, stop=3, step=1)
```
*   `df.index`: DataFrame `df`의 행 인덱스 객체를 반환합니다. 출력된 `RangeIndex(start=0, stop=3, step=1)`는 인덱스가 0부터 시작하여 3 미만까지(즉, 0, 1, 2) 1씩 증가하는 정수임을 의미합니다.

```python
print("Columns:", df.columns)
# 출력: Columns: Index(['Name', 'Math', 'Science'], dtype='object')
```
*   `df.columns`: DataFrame `df`의 컬럼 이름들을 담고 있는 `Index` 객체를 반환합니다. `['Name', 'Math', 'Science']`는 생성된 DataFrame의 컬럼 이름들이며, `dtype='object'`는 이 컬럼 이름들이 문자열(객체) 타입임을 나타냅니다.

```python
print("Shape:", df.shape)
# 출력: Shape: (3, 3)
```
*   `df.shape`: DataFrame `df`의 차원을 `(행의 수, 열의 수)` 형태의 튜플로 반환합니다. 이 예시에서는 3개의 행과 3개의 열로 구성된 DataFrame임을 나타냅니다.

```python
print("Data types:")
print(df.dtypes)
# 출력:
# Name       object
# Math        int64
# Science     int64
# dtype: object
```
*   `df.dtypes`: DataFrame `df`의 각 컬럼별 데이터 타입을 Series 형태로 반환합니다.
    *   `Name`: `object`는 일반적으로 문자열 데이터를 나타냅니다.
    *   `Math`: `int64`는 64비트 정수형 데이터를 나타냅니다.
    *   `Science`: `int64`는 64비트 정수형 데이터를 나타냅니다.
*   반환되는 `Series` 자체의 `dtype: object`는 해당 Series의 값들이(여기서는 `object`, `int64`) 문자열로 표현되는 객체라는 의미입니다.

**구체적 예시**

어떤 반의 학생 3명에 대한 이름, 수학 점수, 과학 점수가 기록된 성적표를 DataFrame으로 생각해보세요.

```
       Name  Math  Science
0     Alice    85       88
1       Bob    92       95
2   Charlie    78       82
```

*   **`df.index`**: 이 성적표에서 `0, 1, 2`는 각 학생을 식별하는 번호(행 인덱스) 역할을 합니다.
*   **`df.columns`**: `Name`, `Math`, `Science`는 성적표의 각 열이 무엇을 나타내는지를 알려주는 항목(컬럼 이름)입니다.
*   **`df.shape`**: 이 성적표에는 3명의 학생(행)과 이름, 수학 점수, 과학 점수 3가지 정보(열)가 있으므로 `(3, 3)`이라는 `shape`을 가집니다.
*   **`df.dtypes`**: 'Name' 컬럼에는 'Alice', 'Bob'과 같은 문자열이 있으므로 데이터 타입은 `object`입니다. 'Math'와 'Science' 컬럼에는 85, 92와 같은 정수형 점수가 있으므로 데이터 타입은 `int64`입니다. `dtypes`를 통해 각 컬럼에 어떤 종류의 데이터가 저장되어 있는지 빠르게 파악할 수 있어, 예를 들어 점수 컬럼의 평균을 계산하거나 이름 컬럼을 검색하는 등의 작업에 앞서 데이터 타입을 확인하는 데 유용합니다.

**시험 포인트**

*   ⭐ **DataFrame의 주요 속성(`index`, `columns`, `shape`, `dtypes`)의 역할과 반환 값**: 각 속성이 DataFrame의 어떤 정보를 제공하고 어떤 형식(예: 튜플, Series)으로 반환하는지 정확히 이해하고 있어야 합니다. 데이터 분석의 첫 걸음이므로 개념을 명확히 익히는 것이 중요합니다.
*   ⭐ **`df.shape`의 순서**: `(행의 개수, 열의 개수)` 순서로 튜플이 반환됨을 기억하세요. 종종 `(열, 행)`으로 혼동하는 경우가 있으니 주의해야 합니다.
*   ⭐ **데이터 타입(`dtypes`)의 의미**: `object`는 주로 문자열 데이터를 나타내며, `int64`, `float64`는 각각 정수와 실수를 의미한다는 것을 알아야 합니다. 특정 컬럼의 데이터 타입을 확인하는 것은 향후 데이터 클리닝 및 분석 방법론을 결정하는 데 필수적입니다.
*   `index`와 `columns`는 데이터프레임 내 특정 데이터를 선택하거나 조작할 때 기준이 되는 '주소' 역할을 하므로 중요합니다.

---

## Slide 50

**핵심 개념**
`head()`와 `tail()` 메서드는 pandas DataFrame에서 데이터를 빠르게 탐색하고 확인하는 데 사용됩니다. 이들은 데이터프레임의 상위 또는 하위 일부 행을 반환하여 전체 데이터를 로드하지 않고도 데이터의 구조, 값 분포, 이상치 여부 등을 대략적으로 파악할 수 있게 해줍니다.

**코드/수식 해설**

*   **상위 n개 행 조회**:
    ```python
    df.head(n)
    ```
    이 메서드는 DataFrame `df`의 첫 `n`개 행을 반환합니다. `n`을 지정하지 않으면 기본값으로 상위 5개 행을 반환합니다.

*   **하위 n개 행 조회**:
    ```python
    df.tail(n)
    ```
    이 메서드는 DataFrame `df`의 마지막 `n`개 행을 반환합니다. `n`을 지정하지 않으면 기본값으로 하위 5개 행을 반환합니다.

**구체적 예시**

```python
import pandas as pd
import numpy as np

# 예시 DataFrame 생성
data = {
    '이름': ['김철수', '이영희', '박지민', '최현우', '정수연', '강민준', '윤서진', '한지우', '신동현', '오수아'],
    '나이': [23, 22, 25, 24, 23, 26, 22, 25, 24, 23],
    '성별': ['남', '여', '여', '남', '여', '남', '여', '남', '남', '여'],
    '점수': [88, 92, 78, 85, 95, 70, 89, 91, 75, 83]
}
df = pd.DataFrame(data)

print("--- DataFrame 전체 ---")
print(df)

print("\n--- df.head() (기본 5개 행) ---")
print(df.head())

print("\n--- df.head(3) (상위 3개 행) ---")
print(df.head(3))

print("\n--- df.tail() (기본 5개 행) ---")
print(df.tail())

print("\n--- df.tail(2) (하위 2개 행) ---")
print(df.tail(2))
```

**시험 포인트**

*   ⭐ `df.head(n)`과 `df.tail(n)` 메서드의 기본 `n` 값은 **5**입니다. (즉, 인자 없이 호출 시 상위/하위 5개 행 반환)
*   ⭐ 이 메서드들은 데이터의 초기 탐색(Initial data exploration), 데이터 조작 후 검증(Verification after data operations), 빠른 데이터 품질 확인(Quick quality checks), 샘플 데이터 제시(Presentation of sample data) 등에 유용하게 사용됩니다. 데이터 과학자가 데이터를 분석하기 전 가장 먼저 사용하는 방법 중 하나입니다.
*   `head()`와 `tail()`은 원본 DataFrame을 변경하지 않고, 선택된 행들로 구성된 새로운 DataFrame (또는 뷰)을 반환합니다.

---

## Slide 51

**핵심 개념**
`df.loc`는 pandas DataFrame에서 **레이블(label) 기반**으로 데이터를 선택(indexing)하고 슬라이싱(slicing)하는 데 사용되는 강력한 접근자입니다. 행 인덱스와 열 이름을 직접 사용하여 원하는 데이터를 정확히 추출할 수 있습니다. `loc`는 정수 위치 인덱스(`iloc`와 다름)가 아닌, 명시적인 행 인덱스 값과 열 이름(레이블)을 기준으로 작동합니다.

**코드 해설**

1.  **데이터 준비**
    ```python
    # Sample data
    df = elections.head()
    ```
    `elections`라는 DataFrame의 상위 5개 행을 가져와 `df`라는 변수에 저장합니다. 이는 예시를 위한 기본적인 데이터셋을 준비하는 과정입니다.

2.  **단일 값 선택 (Single value selection)**
    ```python
    candidate = df.loc[0, 'Candidate']
    print(candidate) # Andrew Jackson
    ```
    *   `df.loc[0, 'Candidate']`: DataFrame `df`에서 행 인덱스(레이블)가 `0`이고, 열 이름(레이블)이 `'Candidate'`인 셀의 값을 선택합니다.
    *   결과로 `'Andrew Jackson'`이라는 단일 문자열 값이 반환됩니다.

3.  **여러 행, 단일 열 선택 (Multiple rows, single column)**
    ```python
    candidates = df.loc[0:2, 'Candidate']
    print(candidates)
    # 0    Andrew Jackson
    # 1    John Quincy Adams
    # 2    Andrew Jackson
    # Name: Candidate, dtype: object
    ```
    *   `df.loc[0:2, 'Candidate']`: 행은 인덱스 `0`부터 `2`까지 (⭐**슬라이싱 시 마지막 인덱스를 포함합니다!**), 열은 `'Candidate'` 하나만 선택합니다.
    *   결과로 'Candidate' 열의 인덱스 0, 1, 2에 해당하는 값들을 포함하는 pandas `Series` 객체가 반환됩니다.

4.  **여러 행, 여러 열 선택 (Multiple rows and columns)**
    ```python
    subset = df.loc[0:2, 'Year':'Party']
    print(subset)
    #    Year          Candidate            Party
    # 0  1824     Andrew Jackson  Democratic-Republican
    # 1  1824  John Quincy Adams  Democratic-Republican
    # 2  1828     Andrew Jackson             Democratic
    ```
    *   `df.loc[0:2, 'Year':'Party']`: 행은 인덱스 `0`부터 `2`까지 (포함), 열은 `'Year'`부터 `'Party'`까지 (⭐**슬라이싱 시 마지막 열도 포함합니다!**) 선택합니다.
    *   결과로 지정된 행과 열로 이루어진 새로운 pandas `DataFrame` 객체가 반환됩니다.

**구체적 예시**

도서관에서 책을 찾는 상황을 생각해 봅시다.
*   **`df`**: 도서관 전체 책장이라고 상상해 보세요. 각 책은 하나의 행이고, 책의 정보(제목, 저자, 출판년도 등)는 열이 됩니다.
*   **`df.loc[0, 'Candidate']`**: 첫 번째 칸에 있는 책(인덱스 0)의 '저자'(Candidate) 정보만 찾아보는 것과 같습니다.
*   **`df.loc[0:2, 'Candidate']`**: 첫 번째 칸부터 세 번째 칸까지(인덱스 0, 1, 2)의 책들에 대해서, '저자'(Candidate) 정보만 쭉 살펴보는 것입니다.
*   **`df.loc[0:2, 'Year':'Party']`**: 첫 번째 칸부터 세 번째 칸까지의 책들에 대해, '출판년도'(Year)부터 '출판사'(Party)까지의 모든 정보를 확인하는 것과 같습니다.

**시험 포인트**

*   ⭐**`df.loc`의 가장 큰 특징은 레이블(행 인덱스 값, 열 이름) 기반으로 동작한다는 것입니다.**
*   ⭐**`loc`를 사용한 슬라이싱(예: `0:2`, `'Year':'Party'`)은 시작 레이블과 끝 레이블을 **모두 포함**합니다.** 이는 파이썬 리스트 슬라이싱(끝 인덱스 미포함)과 다른 점이므로 특히 주의해야 합니다.
*   ⭐단일 값을 선택할 때는 `df.loc[행레이블, 열레이블]` 형태를 사용합니다.
*   ⭐여러 행/열을 선택할 때는 슬라이싱(`시작:끝`) 또는 리스트(`[레이블1, 레이블2, ...]`) 형태를 사용합니다.
*   `loc`는 주로 데이터프레임에서 특정 이름의 열이나 인덱스 값을 가진 행을 선택할 때 유용하게 사용됩니다.

---

## Slide 52

**핵심 개념**
이 슬라이드는 `pandas` 라이브러리의 `DataFrame.loc` 접근자를 활용한 데이터 선택 및 필터링의 고급 예시를 다룹니다. 특히, 특정 열 선택, 조건부 행 선택, 그리고 불리언 인덱싱(Boolean Indexing)을 통한 복잡한 데이터 필터링 방법을 설명합니다. `loc`는 레이블 기반(label-based) 인덱싱을 제공하여, 행과 열을 이름(또는 인덱스 레이블)으로 접근할 때 사용됩니다.

**코드/수식 해설**

1.  **모든 행과 특정 열 선택**:
    ```python
    # Select all rows, specific columns
    winners = df.loc[:, ['Candidate', 'Result']]
    print(winners)
    ```
    *   `df.loc`: `DataFrame` `df`에서 레이블 기반 인덱싱을 시작합니다.
    *   `:`: 행 선택 부분에 콜론(`:`)을 사용하여 모든 행을 선택합니다.
    *   `['Candidate', 'Result']`: 열 선택 부분에 리스트를 사용하여 'Candidate'와 'Result' 열만 선택합니다.

2.  **조건부 선택 (Conditional Selection)**:
    ```python
    # Conditional selection with .loc
    winners_only = df.loc[df['Result'] == 'win', ['Candidate', 'Year']]
    print(winners_only)
    ```
    *   `df['Result'] == 'win'`: 'Result' 열의 값이 'win'인지를 검사하여 불리언 Series를 생성합니다. 이 Series는 `df.loc`의 첫 번째 인자(행 선택)로 사용되어 'win'인 행만 필터링합니다.
    *   `['Candidate', 'Year']`: 두 번째 인자(열 선택)로 'Candidate'와 'Year' 열만 선택합니다.
    *   결과적으로 'Result'가 'win'인 행들 중에서 'Candidate'와 'Year' 열만 가져오게 됩니다.

3.  **불리언 인덱싱 (Boolean Indexing)과 문자열 메소드**:
    ```python
    # Boolean indexing
    democratic = df.loc[df['Party'].str.contains('Democratic')]
    print(democratic.shape) # (3, 6)
    ```
    *   `df['Party'].str.contains('Democratic')`: 'Party' 열의 각 문자열에 'Democratic'이라는 문자열이 포함되어 있는지 검사하여 불리언 Series를 생성합니다. `str` 접근자를 통해 Series의 원소별 문자열 메소드를 적용할 수 있습니다.
    *   `df.loc[...]`: 이 불리언 Series를 `loc`의 행 선택 인자로 사용하여 'Party' 열에 'Democratic'이 포함된 행만 필터링합니다. 열 선택을 생략하면 해당 행의 모든 열을 가져옵니다.
    *   `democratic.shape`: 필터링된 `DataFrame`의 행과 열의 크기를 출력합니다. (3, 6)은 3개의 행과 6개의 열을 의미합니다.

**구체적 예시**

*   **모든 행, 특정 열 선택**: 학교 성적표 `df`에서 모든 학생의 '이름'과 '총점'만 보고 싶을 때 `df.loc[:, ['이름', '총점']]`을 사용할 수 있습니다.
*   **조건부 선택**: `df`에서 '합격'한 학생들 중 '이름'과 '학과'만 보고 싶을 때 `df.loc[df['결과'] == '합격', ['이름', '학과']]`와 같이 조건을 적용하여 원하는 정보를 추출할 수 있습니다.
*   **불리언 인덱싱**: 주소록 `df`에서 '서울'에 거주하는 사람들만 찾고 싶을 때 `df.loc[df['주소'].str.contains('서울')]`을 사용하여 '주소' 열에 '서울'이 포함된 모든 사람들의 정보를 쉽게 필터링할 수 있습니다.

**시험 포인트**

*   ⭐`DataFrame.loc`의 기본적인 사용법 (행과 열 선택)을 정확히 이해하고 있어야 합니다. `df.loc[row_indexer, column_indexer]`
*   ⭐행 인덱서로 불리언 Series를 사용하는 **조건부 선택(Conditional Selection)** 방식은 매우 중요합니다. `df.loc[df['column'] == value, ...]`
*   ⭐`str` 접근자를 활용한 **문자열 기반 불리언 인덱싱** (예: `.str.contains()`, `.str.startswith()`, `.str.endswith()`)은 실제 데이터 분석에서 자주 사용되므로 숙지해야 합니다.
*   `loc`를 사용할 때 행/열 인덱서로 단일 레이블, 레이블 리스트, 슬라이싱, 불리언 Series를 자유자재로 활용할 수 있는지 묻는 문제가 출제될 수 있습니다.

---

## Slide 53

**핵심 개념**
`pandas` 라이브러리의 `DataFrame`에서 데이터를 선택하는 방법 중 하나인 **`.iloc` (integer-location based indexing)**에 대해 다룹니다. `.iloc`은 데이터프레임의 행과 열을 **정수(integer) 위치**를 기반으로 선택할 때 사용됩니다. 이는 파이썬 리스트의 인덱싱 및 슬라이싱과 유사하게 작동하며, 슬라이싱 시 `end` 인덱스는 포함되지 않는 (exclusive) 특징을 가집니다.

**코드/수식 해설**

```python
# df = elections.head()
# 데이터프레임의 처음 몇 행을 사용하여 예시 데이터프레임 df를 생성합니다.
# 실제 elections 데이터프레임의 구조를 가정하면 다음과 같습니다.
#    Year         Candidate               Party  Popular vote
# 0  1824    Andrew Jackson  Democratic-Republican        151271
# 1  1824  John Quincy Adams  Democratic-Republican        113142
# 2  1828    Andrew Jackson             Democratic        642806
# ...
```

```python
# Single value by position
first_candidate = df.iloc[0, 1]  # Row 0, Column 1
print(first_candidate)
```
이 코드는 `df` 데이터프레임에서 첫 번째 행(인덱스 0)과 두 번째 열(인덱스 1)에 해당하는 단일 값을 선택합니다. `first_candidate` 변수에는 'Andrew Jackson'이 저장됩니다.

```python
# First 3 rows, first 4 columns (exclusive of endpoint)
subset = df.iloc[0:3, 0:4]
print(subset)
```
이 코드는 첫 번째부터 세 번째 행(인덱스 0, 1, 2)까지와 첫 번째부터 네 번째 열(인덱스 0, 1, 2, 3)까지를 선택합니다. 슬라이싱 `0:3`은 0, 1, 2 인덱스를 포함하고, `0:4`는 0, 1, 2, 3 인덱스를 포함합니다. 결과는 다음 예시와 유사합니다.
```
   Year         Candidate               Party  Popular vote
0  1824    Andrew Jackson  Democratic-Republican        151271
1  1824  John Quincy Adams  Democratic-Republican        113142
2  1828    Andrew Jackson             Democratic        642806
```

```python
# Last 2 rows, all columns
last_rows = df.iloc[-2:, :]
print(last_rows.shape)  # (2, 6)
```
이 코드는 뒤에서 두 번째 행부터 마지막 행까지(즉, 마지막 두 행)를 선택하고, 모든 열(`:`)을 선택합니다. `shape` 속성을 출력하여 결과 데이터프레임의 차원(행, 열)을 확인합니다. 예시 출력 `(2, 6)`은 원본 `df`가 6개의 열을 가졌다고 가정합니다.

```python
# Every other row, specific columns
every_other = df.iloc[::2, [1, 4]]  # Columns 1 and 4
```
이 코드는 모든 행 중에서 두 칸씩 건너뛰며(즉, 짝수 인덱스 행: 0, 2, 4...) 선택하고, 동시에 특정 열들(인덱스 1과 4)만을 선택합니다. `[1, 4]`는 리스트를 사용하여 비연속적인 열들을 선택할 수 있음을 보여줍니다.

**구체적 예시**
여러분 집의 책장을 생각해보세요. `.iloc`은 책을 "위에서 첫 번째 칸, 왼쪽에서 두 번째 책" 또는 "아래에서 두 번째 칸의 모든 책"과 같이 **물리적인 위치**로 찾아내는 것과 같습니다.
*   `df.iloc[0, 1]`은 '책장 제일 위 칸의 왼쪽에서 두 번째 책'을 집어드는 행위와 같습니다.
*   `df.iloc[0:3, 0:4]`은 '제일 위에서 세 칸까지, 왼쪽에서 네 권까지의 모든 책'을 한 번에 꺼내는 것과 같습니다.
*   `df.iloc[-2:, :]`은 '맨 아래 두 칸의 모든 책'을 선택하는 것입니다.

**시험 포인트**
*   ⭐ **`.iloc`과 `.loc`의 차이점을 명확히 이해하고 구분할 수 있어야 합니다.** `.iloc`은 정수 위치(integer position) 기반, `.loc`은 레이블(label) 기반입니다.
*   ⭐ **파이썬 슬라이싱 규칙 (`start:end:step`, `end` 인덱스 불포함)이 `.iloc`에도 동일하게 적용된다는 것을 기억해야 합니다.**
*   음수 인덱싱 (`-1`은 마지막, `-2`는 뒤에서 두 번째)도 `.iloc`에서 유효하게 사용될 수 있음을 알아야 합니다.
*   ⭐ 특정 행/열을 선택할 때, 단일 값, 슬라이스, 또는 정수 리스트 `[1, 3, 5]`를 사용하여 비연속적인 선택이 가능하다는 점을 알아두세요.

---

## Slide 54

**핵심 개념**:
`[]` 연산자는 pandas DataFrame에서 데이터를 선택하는 데 사용되는 강력하고 문맥 의존적인(Context-Dependent) 선택자입니다. 이 연산자는 입력되는 인자의 타입(정수 슬라이스, 문자열, 문자열 리스트 등)에 따라 행(row)을 선택하거나 열(column)을 선택하는 방식으로 동작합니다. 높은 간결성(conciseness) 덕분에 특히 열 선택 작업에서 가장 흔하게 사용됩니다.

**코드/수식 해설**:

1.  **행 슬라이싱 (Row Slicing)**:
    `df[시작_인덱스:끝_인덱스]` 형식으로 사용되며, `시작_인덱스`부터 `끝_인덱스-1`까지의 행을 선택합니다. Python의 일반적인 슬라이싱 규칙을 따릅니다.

    ```python
    df[0:4] # 첫 4개의 행 (인덱스 0, 1, 2, 3)을 선택합니다.
    ```

2.  **다중 열 선택 (Column Selection - List)**:
    열 이름(문자열)의 리스트를 전달하여 여러 개의 열을 선택합니다. 이 경우 반환되는 값은 DataFrame 형태입니다.

    ```python
    df[['Year', 'Candidate', 'Party']] # 'Year', 'Candidate', 'Party' 세 개의 열을 선택합니다.
    ```

3.  **단일 열 선택 (Single Column Selection)**:
    열 이름(문자열) 하나를 직접 전달하여 해당 열을 선택합니다. 이 경우 반환되는 값은 pandas Series 형태입니다.

    ```python
    df['Candidate'] # 'Candidate' 열을 선택합니다. 이 결과는 Series 타입입니다.
    ```

**구체적 예시**:
다음과 같은 `DataFrame`이 있다고 가정해 봅시다.

```python
import pandas as pd

data = {
    'Year': [2020, 2020, 2016, 2016, 2012],
    'Candidate': ['Biden', 'Trump', 'Clinton', 'Trump', 'Obama'],
    'Party': ['Democrat', 'Republican', 'Democrat', 'Republican', 'Democrat'],
    'Votes': [81284666, 74224673, 65853514, 62984828, 65915795]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# 1. 행 슬라이싱 예시
print("\nFirst three rows (df[0:3]):")
print(df[0:3])

# 2. 다중 열 선택 예시
print("\n'Candidate' and 'Votes' columns (df[['Candidate', 'Votes']]):")
print(df[['Candidate', 'Votes']])

# 3. 단일 열 선택 예시
print("\n'Party' column (df['Party']):\n", df['Party'])
print(f"Type of df['Party']: {type(df['Party'])}")
```

**시험 포인트**:
*   ⭐ `[]` 연산자의 **문맥 의존성(Context-Dependence)**을 이해하는 것이 중요합니다. 인자의 타입에 따라 행 또는 열을 선택합니다.
*   ⭐ **행 슬라이싱** (`df[start:end]`)은 Python의 리스트 슬라이싱과 동일하게 `end` 인덱스 전까지를 포함합니다.
*   ⭐ **열 선택**에서 단일 열을 선택할 때는 `df['ColumnName']` (Series 반환), 여러 열을 선택할 때는 `df[['Column1', 'Column2']]` (DataFrame 반환)와 같이 **대괄호의 중첩 여부**에 주의해야 합니다. 반환되는 객체의 타입(Series vs. DataFrame)을 구분하는 것이 중요합니다.
*   ⭐ `loc`이나 `iloc`과 같은 명시적인 선택자와 비교하여 `[]`의 사용법과 장단점을 설명할 수 있어야 합니다 (간결성).

---

## Slide 55

이 슬라이드는 `pandas` 라이브러리를 활용한 데이터 분석 워크플로우의 실제 예시를 보여줍니다. CSV 파일 로드부터 데이터 탐색, 조건에 따른 필터링 및 특정 컬럼 선택, 그리고 요약 통계량 계산까지 단계별로 설명하고 있습니다.

---

### **핵심 개념**

*   **데이터 분석 워크플로우 (Data Analysis Workflow)**: 데이터를 준비하고, 탐색하며, 분석하고, 결과를 요약하는 체계적인 과정. 이 슬라이드에서는 4단계(로드 및 검사, 기본 탐색, 특정 분석, 요약 통계)로 구성된 기본적인 워크플로우를 제시합니다.
*   **Pandas DataFrame**: 2차원 테이블 형태의 데이터를 다루는 핵심 자료구조. 각 컬럼은 서로 다른 데이터 타입을 가질 수 있습니다.
*   **데이터 로드 (Data Loading)**: `pd.read_csv()`와 같이 외부 파일(CSV, Excel 등)로부터 데이터를 DataFrame으로 불러오는 과정.
*   **데이터 검사 및 탐색 (Data Inspection & Exploration)**: 데이터의 크기(`shape`), 컬럼명(`columns`), 그리고 처음 몇 줄(`head()`)을 확인하여 데이터의 구조와 내용을 파악하는 단계.
*   **데이터 필터링 (Data Filtering)**: 특정 조건을 만족하는 행(row)만 추출하는 과정. 불리언 인덱싱(Boolean Indexing)을 사용합니다.
*   **컬럼 선택 (Column Selection)**: 분석에 필요한 특정 컬럼(column)만 선택하는 과정.
*   **요약 통계 (Summary Statistics)**: 데이터의 특징을 대표하는 통계량(예: 고유값 개수)을 계산하는 과정.

### **코드/수식 해설**

```python
# Step 1: Load and inspect data
# 'elections.csv' 파일을 읽어 'elections'라는 이름의 DataFrame으로 저장
elections = pd.read_csv("elections.csv") 
# DataFrame의 행과 열의 개수(차원) 출력
print(f"Dataset shape: {elections.shape}") 
# DataFrame의 모든 컬럼 이름 목록 출력
print(f"Columns: {list(elections.columns)}") 

# Step 2: Basic exploration
print("First few rows:")
# DataFrame의 상위 3개 행 출력 (기본값은 5개)
print(elections.head(3)) 

# Step 3: Specific analysis
print("Recent winners (2020-2024):")
# 2020년 이후의 데이터 중 'Result' 컬럼이 'win'인 행을 필터링하고,
# 필터링된 데이터에서 'Year', 'Candidate', 'Party' 컬럼만 선택하여 'recent_winners' DataFrame 생성
recent_winners = elections[ 
    (elections['Year'] >= 2020) & # 'Year' 컬럼이 2020 이상인 조건
    (elections['Result'] == 'win') # 'Result' 컬럼이 'win'인 조건
][['Year', 'Candidate', 'Party']] # 위 조건을 만족하는 행에서 'Year', 'Candidate', 'Party' 컬럼만 선택
print(recent_winners) # 결과 출력

# Step 4: Summary statistics
# 'Year' 컬럼의 고유한 값의 개수(총 선거 연도 수) 출력
print(f"Total elections covered: {elections['Year'].nunique()}") 
# 'Candidate' 컬럼의 고유한 값의 개수(총 고유 후보자 수) 출력
print(f"Unique candidates: {elections['Candidate'].nunique()}") 
```

*   **수식**: 이 슬라이드에는 명시적인 수학적 수식은 없습니다. 그러나 `elections['Year'] >= 2020`와 같은 비교 연산, `&`와 같은 논리 연산, 그리고 `nunique()`와 같은 통계 함수는 데이터에 대한 정량적인 조작을 포함합니다.

### **구체적 예시**

`elections.csv` 파일이 다음과 같은 구조를 가진다고 가정해 봅시다:

| Year | Candidate | Party | Votes | Result |
| :--- | :-------- | :---- | :---- | :----- |
| 2018 | Alice     | A     | 1000  | win    |
| 2018 | Bob       | B     | 900   | lose   |
| 2020 | Charlie   | C     | 1200  | win    |
| 2020 | David     | D     | 1100  | lose   |
| 2022 | Eve       | A     | 1500  | win    |
| 2022 | Frank     | B     | 1450  | lose   |

1.  **Step 1**에서 이 CSV 파일을 불러오면, `elections`라는 DataFrame이 생성됩니다. `elections.shape`는 `(6, 5)`가 될 것이고, `elections.columns`는 `['Year', 'Candidate', 'Party', 'Votes', 'Result']`가 됩니다.
2.  **Step 2**에서 `elections.head(3)`을 호출하면 위 표의 상위 3개 행이 출력되어 데이터의 대략적인 모습을 파악할 수 있습니다.
3.  **Step 3**에서는 2020년 이후의 선거 중 당선자(`Result == 'win'`)만을 필터링하고, 그중 `Year`, `Candidate`, `Party` 컬럼만 선택합니다. 이 예시에서는 Charlie (2020, C), Eve (2022, A)가 `recent_winners`로 출력될 것입니다.
4.  **Step 4**에서는 전체 데이터셋에 포함된 고유한 선거 연도(`elections['Year'].nunique()`, 결과: 3 (2018, 2020, 2022))와 고유한 후보자 수(`elections['Candidate'].nunique()`, 결과: 6 (Alice, Bob, Charlie, David, Eve, Frank))를 계산하여 요약 정보를 제공합니다.

### **시험 포인트**

*   ⭐ **Pandas 기본 함수 활용**: `pd.read_csv()`, `DataFrame.shape`, `DataFrame.columns`, `DataFrame.head()` 등 데이터 로드 및 초기 탐색에 사용되는 기본 함수들의 용법과 반환 값을 정확히 이해해야 합니다.
*   ⭐ **조건부 필터링**: `DataFrame[조건]` 형식의 불리언 인덱싱을 이용한 데이터 필터링 방법과 여러 조건을 `&` (AND) 연산자로 결합하는 방법을 반드시 숙지해야 합니다. (OR 조건은 `|` 사용).
*   ⭐ **컬럼 선택**: 단일 컬럼 선택 (`df['col']`)과 다중 컬럼 선택 (`df[['col1', 'col2']]`)의 차이점과 사용법을 알아야 합니다.
*   ⭐ **고유값 계산**: `Series.nunique()` 함수를 사용하여 특정 컬럼의 고유한 값의 개수를 효율적으로 계산하는 방법을 이해해야 합니다. 이는 데이터의 다양성을 파악하는 데 중요합니다.
*   ⭐ **데이터 분석 워크플로우의 이해**: 데이터 로드부터 요약까지 각 단계가 어떤 목적으로 수행되는지, 그리고 각 단계에 어떤 pandas 함수들이 주로 활용되는지 흐름을 파악하는 것이 중요합니다.

---

## Slide 56

**핵심 개념**
Pandas에서 DataFrame이나 Series의 특정 데이터를 선택하고 접근하는 인덱싱(Indexing)은 데이터 분석의 기본입니다. 슬라이드는 주로 사용되는 세 가지 인덱싱 방법인 `.loc`, `.iloc`, 그리고 기본 대괄호 `[]`의 특징을 요약합니다.

*   **`.loc`**: **레이블 기반(Label-based) 선택**에 사용됩니다. 행과 열의 이름(레이블)을 사용하여 데이터를 선택합니다. 슬라이싱(slicing) 시 지정된 시작 레이블과 끝 레이블 **모두 포함(inclusive)**합니다. 입력 타입은 레이블(문자열, 숫자 등)입니다.
*   **`.iloc`**: **위치 기반(Position-based) 선택**에 사용됩니다. 0부터 시작하는 정수형 위치(인덱스)를 사용하여 데이터를 선택합니다. 슬라이싱 시 시작 위치는 포함하고 끝 위치는 **포함하지 않습니다(exclusive)**. 입력 타입은 정수(integers)입니다.
*   **`[]` (대괄호)**: **상황 의존적(Context-dependent)**입니다. 단일 컬럼 선택, 여러 컬럼 선택, 불리언 인덱싱 등 다양한 방식으로 사용될 수 있습니다. 슬라이싱 동작은 입력 타입과 문맥에 따라 다릅니다.

**코드/수식 해설**
이 슬라이드에서는 특별한 수학적 수식이 다뤄지지 않습니다. 대신 각 인덱싱 메서드의 파이썬 코드 사용법을 설명합니다.

```python
import pandas as pd

# 예시 DataFrame 생성
data = {'City': ['Seoul', 'Busan', 'Jeju', 'Daegu'],
        'Population_Millions': [9.7, 3.4, 0.6, 2.4],
        'Area_sq_km': [605, 770, 1849, 884]}
df = pd.DataFrame(data, index=['SEOUL', 'BUSAN', 'JEJU', 'DAEGU'])

print("Original DataFrame:")
print(df)
print("-" * 40)

# .loc 예시: 레이블 기반 선택 (행, 열 모두 레이블 사용)
# 1. 단일 행 레이블 선택
print("df.loc['SEOUL'] (단일 행 선택):")
print(df.loc['SEOUL'])
print("-" * 40)

# 2. 행 레이블 슬라이싱 (끝 레이블 포함) 및 특정 열 선택
print("df.loc['BUSAN':'DAEGU', 'Population_Millions'] (행 슬라이싱 및 열 선택):")
print(df.loc['BUSAN':'DAEGU', 'Population_Millions']) # 'BUSAN', 'JEJU', 'DAEGU' 행 포함
print("-" * 40)

# .iloc 예시: 위치 기반 선택 (행, 열 모두 정수 인덱스 사용)
# 1. 단일 행 위치 선택 (0번 인덱스)
print("df.iloc[0] (단일 행 위치 선택):")
print(df.iloc[0])
print("-" * 40)

# 2. 행 위치 슬라이싱 (끝 인덱스 미포함) 및 특정 열 선택
print("df.iloc[0:3, 1] (행 슬라이싱 및 열 위치 선택):")
print(df.iloc[0:3, 1]) # 0, 1, 2번 인덱스 행, 1번 인덱스 열 ('Population_Millions')
print("-" * 40)

# [] (대괄호) 예시: 상황 의존적
# 1. 단일 컬럼 선택 (Series 반환)
print("df['City'] (단일 컬럼 선택):")
print(df['City'])
print("-" * 40)

# 2. 여러 컬럼 선택 (DataFrame 반환)
print("df[['City', 'Area_sq_km']] (여러 컬럼 선택):")
print(df[['City', 'Area_sq_km']])
print("-" * 40)

# 3. 불리언 인덱싱 (Population_Millions가 3백만 이상인 도시)
print("df[df['Population_Millions'] > 3.0] (불리언 인덱싱):")
print(df[df['Population_Millions'] > 3.0])
print("-" * 40)

# 4. 행 슬라이싱 (기본 대괄호는 행 슬라이싱 시 .iloc와 유사하게 끝 인덱스 미포함)
print("df[0:2] (행 슬라이싱):")
print(df[0:2]) # 0, 1번 인덱스 행
print("-" * 40)
```

**구체적 예시**
위 코드 예시와 더불어 실생활 비유를 통해 이해를 돕겠습니다.
*   **`.loc`**는 마치 도서관에서 책을 찾을 때, "정치학 섹션의 '민주주의의 역사'라는 제목의 책"처럼 책의 분류 번호, 제목, 저자와 같은 **고유한 정보(레이블)**를 사용하여 찾는 방식과 같습니다. 우리는 데이터프레임의 인덱스(SEOUL, BUSAN 등)나 컬럼 이름(City, Population_Millions 등)을 직접 명시하여 원하는 데이터를 정확히 지목합니다.
*   **`.iloc`**는 "두 번째 줄의 세 번째 칸에 있는 책"처럼, 책이 놓여있는 **물리적인 순서(위치)**를 세어 찾는 방식과 같습니다. 데이터프레임의 0부터 시작하는 정수형 인덱스나 컬럼 위치를 사용하여 데이터를 선택합니다.
*   **`[]` (대괄호)**는 유연하게 특정 조건으로 책을 찾는 것과 유사합니다. 예를 들어, "제목에 '데이터'가 들어가는 모든 책을 찾아줘"와 같이 특정 컬럼을 선택하거나, "인구가 300만 이상인 도시 목록"처럼 조건을 만족하는 행을 필터링하는 데 사용됩니다.

**시험 포인트**
*   ⭐ **`.loc`는 레이블 기반, `.iloc`는 위치 기반**이라는 핵심 차이를 정확히 이해하고 구분할 수 있어야 합니다.
*   ⭐ **슬라이싱(Slicing) 동작**: `.loc`은 시작 레이블과 끝 레이블 **모두 포함(inclusive)**하지만, `.iloc`은 시작 인덱스는 포함하고 끝 인덱스는 **포함하지 않는(exclusive)**다는 점을 반드시 기억해야 합니다.
    *   `df.loc['A':'C']`는 'A', 'B', 'C' 레이블의 데이터를 모두 포함합니다.
    *   `df.iloc[0:3]`는 0, 1, 2번 인덱스의 데이터를 포함하고 3번 인덱스는 제외합니다.
*   ⭐ `[]`는 DataFrame에서 **주로 컬럼 선택**에 사용되며, 특히 **불리언 인덱싱(Boolean Indexing)**에 매우 강력하게 활용될 수 있습니다. (예: `df[df['Population_Millions'] > 3.0]`)
*   ⭐ 두 차원(행과 열)을 동시에 인덱싱할 때는 `df.loc[row_indexer, col_indexer]` 또는 `df.iloc[row_indexer, col_indexer]`와 같이 쉼표(`,`)를 사용하여 구분하는 방식에 익숙해야 합니다.

---

## Slide 57

**핵심 개념**

*   **`.loc` (Label-based operations)**: 데이터프레임의 행과 열을 **레이블(이름)**을 기반으로 선택할 때 사용합니다. 행 인덱스 이름과 열 이름으로 접근하며, 슬라이싱 시에도 시작 레이블과 끝 레이블을 모두 포함합니다. `.loc`은 명시적인 레이블을 사용하므로 데이터의 순서가 바뀌어도 항상 동일한 레이블의 데이터를 가져와 **더 안전(safer)**합니다.
*   **`.iloc` (Position-based logic)**: 데이터프레임의 행과 열을 **정수 위치(순서)**를 기반으로 선택할 때 사용합니다. 파이썬의 리스트 인덱싱과 유사하게 0부터 시작하는 정수 인덱스를 사용하며, 슬라이싱 시에는 시작 위치는 포함하고 끝 위치는 포함하지 않습니다 (exclusive).
*   **`[]` (Simple column selection)**: 단일 컬럼 또는 여러 컬럼을 선택할 때 주로 사용합니다. `df['column_name']` 또는 `df[['col1', 'col2']]` 형태로 사용됩니다. 불리언 인덱싱을 통해 특정 조건에 맞는 행을 선택할 때도 유용하게 사용됩니다.
*   **데이터 정렬 고려 (`.iloc` 사용 시)**: `.iloc`은 데이터의 물리적인 순서에 의존하기 때문에, 데이터프레임의 행 순서가 변경(예: `sort_values()`, `reset_index()` 등)되면 동일한 `.iloc` 호출이라도 다른 결과를 반환할 수 있습니다. 따라서 `.iloc`을 사용할 때는 현재 데이터의 정렬 상태를 항상 염두에 두어야 합니다.

**코드/수식 해설**

아래 코드는 `pandas` 데이터프레임에서 `.loc`, `.iloc`, `[]`의 사용법을 보여주며, `.iloc` 사용 시 데이터 정렬을 고려해야 하는 이유를 설명합니다.

```python
import pandas as pd
import numpy as np

# 예시 데이터프레임 생성
data = {'A': [10, 20, 30, 40, 50],
        'B': [100, 200, 300, 400, 500],
        'C': [1000, 2000, 3000, 4000, 5000]}
index_labels = ['row1', 'row2', 'row3', 'row4', 'row5']
df = pd.DataFrame(data, index=index_labels)
print("Original DataFrame:")
print(df)
print("-" * 30)

# 1. .loc 예시: 레이블 기반 선택 (행 레이블, 열 레이블 사용)
# 'row2' 행과 'B' 컬럼의 단일 값 선택
print(".loc['row2', 'B']:")
print(df.loc['row2', 'B']) # 200
print("-" * 30)

# 'row1'부터 'row3'까지의 행과 'A', 'C' 컬럼 선택 (슬라이싱 시 끝 레이블 포함)
print(".loc['row1':'row3', ['A', 'C']]:")
print(df.loc['row1':'row3', ['A', 'C']])
#       A     C
# row1 10  1000
# row2 20  2000
# row3 30  3000
print("-" * 30)

# 2. .iloc 예시: 위치 기반 선택 (0부터 시작하는 정수 위치 사용)
# 인덱스 1번 행 (두 번째 행), 인덱스 0번 컬럼 (첫 번째 컬럼)의 단일 값 선택
print(".iloc[1, 0]:")
print(df.iloc[1, 0]) # 20
print("-" * 30)

# 인덱스 0번부터 2번까지의 행 (첫 세 행), 인덱스 0번과 2번 컬럼 선택 (슬라이싱 시 끝 위치 미포함)
print(".iloc[0:3, [0, 2]]:")
print(df.iloc[0:3, [0, 2]])
#       A     C
# row1 10  1000
# row2 20  2000
# row3 30  3000
print("-" * 30)

# 3. [] 예시: 단순 컬럼 선택 및 불리언 인덱싱
# 'B' 컬럼 선택 (Series 반환)
print("df['B']:")
print(df['B'])
# row1    100
# row2    200
# row3    300
# row4    400
# row5    500
# Name: B, dtype: int64
print("-" * 30)

# 'A', 'C' 컬럼 선택 (DataFrame 반환)
print("df[['A', 'C']]:")
print(df[['A', 'C']])
#       A     C
# row1 10  1000
# row2 20  2000
# row3 30  3000
# row4 40  4000
# row5 50  5000
print("-" * 30)

# 'A' 컬럼 값이 30보다 큰 행 선택 (불리언 인덱싱)
print("df[df['A'] > 30]:")
print(df[df['A'] > 30])
#       A    B     C
# row4 40  400  4000
# row5 50  500  5000
print("-" * 30)

# 4. .iloc 사용 시 데이터 정렬 고려 예시
# 데이터프레임의 순서를 'A' 컬럼 기준으로 내림차순으로 변경
df_sorted = df.sort_values(by='A', ascending=False)
print("DataFrame after sorting by 'A' descending:")
print(df_sorted)
#       A    B     C
# row5 50  500  5000
# row4 40  400  4000
# row3 30  300  3000
# row2 20  200  2000
# row1 10  100  1000
print("-" * 30)

# 정렬 전 df.iloc[0]와 정렬 후 df_sorted.iloc[0] 비교
print("Original df.iloc[0] (first row before sorting):")
print(df.iloc[0]) # row1 데이터
print("\nSorted df_sorted.iloc[0] (first row after sorting):")
print(df_sorted.iloc[0]) # row5 데이터. 결과가 다름을 확인
print("-" * 30)
```

**구체적 예시**

*   **도서관 서가 비유**:
    *   **`.loc`**: 도서관에서 원하는 책을 찾을 때 **"데이터 분석 입문"이라는 책 제목**을 보고 찾는 것과 같습니다. 책의 물리적인 위치가 바뀌어도 "데이터 분석 입문"이라는 레이블(제목)만 알면 항상 그 책을 찾을 수 있습니다.
    *   **`.iloc`**: 도서관에서 원하는 책을 찾을 때 **"다섯 번째 칸의 세 번째 줄에 있는 책"**을 집어 드는 것과 같습니다. 만약 서가의 책 순서가 바뀌면, 동일한 "다섯 번째 칸의 세 번째 줄" 위치라도 다른 책을 가져오게 됩니다. 따라서 현재 서가의 배열 상태를 정확히 알고 있어야 합니다.
    *   **`[]`**: 특정 주제의 책이 모여있는 **"데이터 과학" 코너 전체**를 가져오는 것과 비슷합니다. 특정 컬럼(주제)의 모든 데이터를 한 번에 가져올 때 유용합니다.

*   **쇼핑몰 주문 내역 비유**:
    *   **`.loc`**: 고객 주문 내역에서 **'ORD001'이라는 주문 번호**를 가진 주문의 상세 정보를 찾는 것.
    *   **`.iloc`**: 고객 주문 내역 리스트에서 **'세 번째로 기록된 주문'**의 정보를 찾는 것. 만약 주문 내역이 최신순으로 정렬되거나 이전 주문이 취소되어 목록에서 삭제되면, 세 번째 주문은 다른 주문이 될 수 있습니다.
    *   **`[]`**: 모든 주문에 대한 **'상품명' 정보**만 따로 모아서 보는 것.

**시험 포인트**

*   ⭐ **`.loc`과 `.iloc`의 핵심 차이점**: `.loc`은 **레이블(label)**, `.iloc`은 **위치(position/integer-location)**를 기반으로 한다는 점을 명확히 이해하고 설명할 수 있어야 합니다.
*   ⭐ **`.loc`의 "safer" 의미**: 레이블 기반이므로 데이터 순서 변화에 독립적이며, 의도치 않은 결과를 방지할 수 있다는 점을 알고 있어야 합니다.
*   ⭐ **슬라이싱(Slicing) 동작 방식 차이**:
    *   `.loc`은 슬라이싱 시 **시작 레이블과 끝 레이블을 모두 포함($start\_label:end\_label$)**합니다.
    *   `.iloc`은 슬라이싱 시 **시작 위치는 포함하고 끝 위치는 포함하지 않습니다($start\_pos:end\_pos$)** (Python 리스트 슬라이싱과 동일).
*   ⭐ **`[]`의 주요 용도**: 주로 컬럼 선택에 사용되며, 불리언 인덱싱에도 강력하게 사용될 수 있음을 알아두세요.
*   ⭐ **`.iloc` 사용 시 주의사항**: 데이터프레임의 순서가 변경(예: 정렬, 행 삭제/삽입)될 경우 `.iloc`의 결과가 달라질 수 있으므로, 항상 데이터의 현재 정렬 상태를 고려해야 한다는 점을 강조하세요. `.iloc`은 명시적인 레이블이 아닌 순서에 의존하기 때문에 예상치 못한 오류나 잘못된 분석으로 이어질 수 있습니다.

---

## Slide 58

## 전문 개발 역량 및 학습 접근법

이 슬라이드는 데이터 분석가로서 성장하기 위한 필수적인 역량과 효과적인 학습 전략을 제시합니다. CSED226 강의에서 다루는 라이브러리(NumPy, pandas, matplotlib, scikit-learn)를 숙달하고 머신러닝 기초 개념을 습득하는 데 있어 어떤 자세로 임해야 하는지를 안내합니다.

---

### **핵심 개념**

1.  **문서 활용 능력 (Documentation Skills)**:
    데이터 과학 분야에서 문제를 해결하고 새로운 기술을 습득하는 데 있어 공식 문서, 커뮤니티 자료, 검색 엔진을 효과적으로 활용하는 능력은 핵심 역량입니다. 특히 `pandas`와 같은 라이브러리는 기능이 방대하므로 공식 문서를 이해하고 적용하는 것이 필수적입니다.

2.  **효과적인 학습 접근법 (Learning Approach)**:
    이론적 기반을 튼튼히 다지고, 실제 데이터를 통한 반복적인 실습을 통해 지식을 내재화하는 것이 중요합니다. 이는 단순히 지식을 암기하는 것을 넘어 문제 해결 능력을 향상시키는 데 기여합니다.

---

### **코드/수식 해설**

이 슬라이드는 특정 코드나 수식을 직접적으로 다루지 않고, 데이터 분석 학습 및 전문성 개발에 필요한 방법론과 태도를 제시합니다. 따라서 슬라이드 자체에서 파생되는 코드나 수식 해설은 없습니다. 그러나 아래 구체적 예시에서 문서 활용을 통해 얻을 수 있는 코드 예시를 간략히 제시합니다.

---

### **구체적 예시**

**1. 문서 활용 능력 예시:**

*   **Pandas 문서 활용**: `pandas.DataFrame`에서 특정 조건에 맞는 행을 선택하는 방법을 모른다고 가정해 봅시다.
    *   공식 문서에서 "indexing and selecting data" 섹션을 찾아 `df[df['column_name'] > value]` 와 같은 구문을 학습하고 적용할 수 있습니다.
*   **Stack Overflow 활용**: `KeyError: 'column_name'` 같은 오류 메시지가 발생했을 때, 해당 오류 메시지를 Stack Overflow에 검색하여 같은 문제를 겪었던 다른 개발자들의 해결책을 참고할 수 있습니다.
*   **Google 검색 활용**: "pandas group by multiple columns example" 또는 "matplotlib custom legend" 와 같이 구체적인 키워드로 검색하여 원하는 기능의 사용법과 예시 코드를 빠르게 찾을 수 있습니다.

**2. 효과적인 학습 접근법 예시:**

*   **기본 개념부터 시작**: `pandas.Series`와 `pandas.DataFrame`의 구조, 인덱싱, 데이터 타입 같은 기초 개념을 먼저 이해한 후, `groupby()`, `merge()`와 같은 복잡한 연산으로 나아갑니다.
*   **실제 데이터셋으로 연습**: 캐글(Kaggle)에서 제공하는 타이타닉 생존자 예측 데이터셋이나 주택 가격 예측 데이터셋을 다운로드하여 데이터 로딩부터 결측치 처리, 시각화, 모델링까지 전 과정을 직접 수행해 봅니다.
*   **반복을 통한 익숙해지기**: Jupyter Notebook에서 동일한 데이터셋으로 여러 번 다른 분석 방법을 시도해보고, 자주 사용하는 함수(`df.head()`, `df.info()`, `df.describe()`, `df['col'].value_counts()`)는 타이핑하지 않고도 바로 사용할 수 있도록 반복 연습합니다.

---

### **시험 포인트**

*   **⭐ 데이터 과학자에게 있어 '문서 활용 능력'이 왜 핵심 역량인지 설명하고, 그 중요성을 뒷받침하는 구체적인 예시를 3가지 이상 들어보세요.** (예: Pandas 공식 문서의 역할, Stack Overflow의 실용적 활용, 효과적인 Google 검색 전략)
*   **⭐ CSED226 강의에서 다루는 데이터 분석 라이브러리(예: pandas)를 효과적으로 학습하기 위한 '학습 접근법' 3가지 이상을 제시하고 각각의 중요성을 설명하세요.** (예: 기본 개념 숙지, 실제 데이터셋 활용, 반복 실습)
*   **⭐ 주어진 문제 상황에서 (예: 특정 라이브러리 사용법을 모를 때) 어떤 순서로 정보 탐색 및 문제 해결을 시도할 것인지 설명하는 주관식 문제가 출제될 수 있습니다.** (문서 활용 능력과 학습 접근법을 종합적으로 적용)

---

## Slide 59

**핵심 개념**

*   **정형 데이터 (Tabular data)**: 데이터 과학의 기본적인 데이터 형식으로, 행과 열로 구성된 표 형태의 데이터를 의미합니다. 스프레드시트나 관계형 데이터베이스의 테이블과 유사하며, 각 행은 고유한 관측치(observation)를, 각 열은 특정 속성(feature)을 나타냅니다. `pandas`는 이러한 정형 데이터를 효율적으로 다루기 위한 강력한 도구입니다.

*   **`pandas` 핵심 데이터 구조**:
    *   **Series**: 1차원 배열 형태의 객체로, 하나의 데이터 타입(예: 숫자, 문자열)을 가지며 각 요소에 고유한 레이블(Index)을 부여할 수 있습니다.
    *   **DataFrame**: 2차원 테이블 형태의 객체로, 여러 개의 Series가 모여 열(column)을 형성합니다. 각 열은 독립적인 Series처럼 서로 다른 데이터 타입을 가질 수 있으며, 스프레드시트와 가장 유사한 형태입니다.
    *   **Index**: Series나 DataFrame의 각 행을 식별하는 레이블 또는 키입니다. 데이터 접근, 정렬, 병합 등의 작업에 중요한 역할을 합니다.

*   **다양한 데이터 생성 방법**: Python의 리스트, 딕셔너리, NumPy 배열뿐만 아니라 CSV, Excel, SQL 데이터베이스 등 다양한 외부 데이터 소스로부터 `Series`나 `DataFrame`을 생성할 수 있습니다. 데이터의 원본 형태에 따라 적절한 `pandas` 생성 함수를 사용합니다.

*   **데이터 선택 (Selection) 접근 방식**: `pandas` 객체에서 특정 행, 열 또는 특정 조건을 만족하는 데이터를 추출하는 세 가지 주요 방법이 있습니다.
    *   `.loc[]`: 레이블(label)을 기반으로 데이터를 선택합니다. 행과 열 모두 레이블을 사용합니다.
    *   `.iloc[]`: 정수(integer) 위치를 기반으로 데이터를 선택합니다. NumPy 배열 인덱싱과 유사하게 0부터 시작하는 정수 위치를 사용합니다.
    *   `[] (브래킷 노테이션)`: 주로 단일 열 선택에 사용되거나, 부울(boolean) 배열을 이용한 조건부 필터링에 사용됩니다.

*   **문서 활용 능력**: 실무적인 데이터 분석 작업에서는 `pandas`의 방대한 기능과 API를 능숙하게 사용하기 위해 공식 문서를 찾아보고 이해하는 능력이 매우 중요합니다. 문제 해결 및 새로운 기능 학습의 핵심 자원입니다.

**코드/수식 해설**

*   **Series 생성 예시**:
    ```python
    import pandas as pd
    import numpy as np

    # 리스트로부터 Series 생성 (자동 인덱스)
    s1 = pd.Series([10, 20, 30])
    print("Series 1:\n", s1)

    # 딕셔너리로부터 Series 생성 (키가 인덱스)
    s2 = pd.Series({'a': 100, 'b': 200, 'c': 300})
    print("\nSeries 2:\n", s2)
    ```

*   **DataFrame 생성 예시**:
    ```python
    # 딕셔너리로부터 DataFrame 생성
    data = {
        '이름': ['김철수', '박영희', '이민호'],
        '학과': ['컴퓨터공학', '전자공학', '화학공학'],
        '학점': [3.8, 4.2, 3.5]
    }
    df = pd.DataFrame(data, index=['A1', 'B2', 'C3'])
    print("DataFrame:\n", df)

    # CSV 파일로부터 DataFrame 불러오기 (예시)
    # df_csv = pd.read_csv('student_data.csv')
    ```

*   **`.loc[]`를 이용한 데이터 선택 (레이블 기반)**:
    ```python
    # 'A1' 행 전체 선택
    print("\n'A1' 행:\n", df.loc['A1'])

    # 'B2' 행의 '이름'과 '학점' 열 선택
    print("\n'B2' 행의 '이름', '학점':\n", df.loc['B2', ['이름', '학점']])

    # 'A1'부터 'C3'까지의 모든 행에서 '학과' 열 선택 (슬라이싱)
    print("\n'A1'~'C3' 행의 '학과' 열:\n", df.loc['A1':'C3', '학과'])
    ```

*   **`.iloc[]`를 이용한 데이터 선택 (정수 위치 기반)**:
    ```python
    # 첫 번째 행 (인덱스 0) 전체 선택
    print("\n첫 번째 행:\n", df.iloc[0])

    # 두 번째 행 (인덱스 1)의 첫 번째(0)와 세 번째(2) 열 선택
    print("\n두 번째 행의 첫, 세 번째 열:\n", df.iloc[1, [0, 2]])

    # 첫 번째부터 세 번째 행 (인덱스 0, 1, 2)까지의 두 번째 열 (인덱스 1) 선택
    print("\n0~2번째 행의 1번째 열:\n", df.iloc[0:3, 1])
    ```

*   **`[]` (브래킷 노테이션)을 이용한 데이터 선택**:
    ```python
    # '이름' 열 선택 (Series 반환)
    print("\n'이름' 열:\n", df['이름'])

    # 여러 열 선택 (DataFrame 반환)
    print("\n'학과'와 '학점' 열:\n", df[['학과', '학점']])

    # '학점'이 4.0 이상인 학생 필터링 (부울 인덱싱)
    print("\n학점 4.0 이상인 학생:\n", df[df['학점'] >= 4.0])
    ```

*   수식은 해당 슬라이드에 포함되어 있지 않아 해설할 내용이 없습니다.

**구체적 예시**

여러분이 POSTECH 재학생 성적 관리 시스템을 구축한다고 상상해 봅시다.
*   **정형 데이터**: 각 학생의 학번, 이름, 전공, 이수 과목, 과목별 점수 등은 모두 정형 데이터입니다. 이는 하나의 큰 Excel 파일 또는 데이터베이스 테이블로 관리될 것입니다.
*   **DataFrame**: 이 성적 데이터를 `pd.DataFrame`으로 로드하면, 각 행은 한 학생의 전체 정보를, 각 열은 '학번', '이름', 'CSED226_점수'와 같은 특정 속성을 나타냅니다.
*   **Series**: 특정 과목, 예를 들어 'CSED226 (데이터분석입문)'의 모든 학생 점수만 따로 추출하면 이는 `Series` 객체가 됩니다.
*   **Index**: 각 학생의 고유한 학번을 `DataFrame`의 `Index`로 설정하면, 특정 학번으로 학생 정보를 빠르게 찾아낼 수 있습니다.
*   **데이터 선택 예시**:
    *   `성적_df.loc['20230001']`: 학번이 '20230001'인 학생의 모든 성적 정보를 조회합니다. (레이블 기반)
    *   `성적_df.iloc[5]`: 데이터프레임에서 위에서 여섯 번째(0부터 시작하는 인덱스로 5) 학생의 정보를 조회합니다. (위치 기반)
    *   `성적_df['CSED226_점수']`: 모든 학생의 '데이터분석입문' 과목 점수를 조회합니다.
    *   `성적_df[성적_df['CSED226_점수'] < 60]`: '데이터분석입문' 점수가 60점 미만인 학생들만 필터링하여 재수강 대상 목록을 뽑아낼 수 있습니다.

**시험 포인트**

*   ⭐ **Series, DataFrame, Index의 명확한 구분**: 이 세 가지 `pandas` 핵심 구조의 정의, 차이점(차원, 구성 요소), 각각의 사용 시기를 정확히 이해하고 설명할 수 있어야 합니다. (예: Series는 1차원, DataFrame은 2차원, Index는 레이블).
*   ⭐ **`.loc[]`와 `.iloc[]`의 비교**: 레이블 기반 인덱싱(`loc`)과 정수 위치 기반 인덱싱(`iloc`)의 개념적 차이점과 실제 코드에서의 사용법을 완벽히 숙지해야 합니다. 슬라이싱(slicing) 시 `.loc`는 끝점 포함, `.iloc`는 끝점 미포함이라는 미묘한 차이도 중요합니다.
*   ⭐ **`[]` (브래킷 노테이션)의 활용**: 단일/복수 열 선택, 그리고 부울(boolean) 인덱싱을 이용한 조건부 필터링 방법을 정확히 알고 코드로 구현할 수 있어야 합니다. 이는 데이터 분석의 핵심적인 부분입니다.
*   ⭐ **Pandas 데이터 조작의 중요성**: 왜 `pandas`와 같은 라이브러리를 사용하여 정형 데이터를 다루는 것이 데이터 과학에서 필수적인지 개념적으로 이해하고 설명할 수 있어야 합니다. (효율성, 구조화, 다양한 데이터 소스 처리 능력 등).
*   ⭐ **공식 문서 활용 능력의 강조**: 문제 해결이나 새로운 기능 학습 시 `pandas` 공식 문서를 참고하는 습관의 중요성을 인지하고, 필요할 때 스스로 정보를 찾아낼 수 있는 능력을 키워야 합니다.

---

## Slide 60

**핵심 개념**:
본 슬라이드는 "Pandas I: Introduction to Data Manipulation" 강의의 마지막을 알리며, 다음 세션에서 진행될 "실제 데이터셋을 활용한 실습"의 중요성을 강조하고 있습니다. 데이터 분석은 이론적 지식 습득뿐만 아니라, 실제 데이터를 직접 다루면서 문제 해결 능력을 키우는 것이 핵심입니다. 이는 지금까지 학습한 Pandas 라이브러리의 다양한 기능을 실질적인 시나리오에 적용하는 기회를 제공하며, 데이터 조작 및 분석 역량을 강화하는 데 필수적입니다.

**코드/수식 해설**:
이 슬라이드에는 직접적인 코드나 수식이 제시되어 있지 않습니다. 하지만 다음 세션의 실습을 위해 Pandas를 이용한 기본적인 데이터 로딩 및 탐색 코드를 숙지하는 것이 중요합니다. 예를 들어, 가장 흔한 데이터 형식인 CSV 파일을 읽어와 `DataFrame`으로 생성하는 과정은 다음과 같습니다.
```python
import pandas as pd

# 'sample_data.csv' 파일을 읽어와 DataFrame으로 생성
# 실제 데이터셋의 경로와 파일명은 달라질 수 있습니다.
df = pd.read_csv('sample_data.csv')

# DataFrame의 상위 5개 행을 출력하여 데이터 구조를 빠르게 확인
print(df.head())

# DataFrame의 기본 정보(컬럼, Non-null 개수, 데이터 타입) 확인
print(df.info())
```
실습에서는 이처럼 데이터를 불러온 후 특정 컬럼 선택, 조건 필터링, 결측치 처리, 그룹별 통계 계산 등 다양한 데이터 조작 및 분석 작업을 수행하게 됩니다.

**구체적 예시**:
"실제 데이터셋으로 실습"은 단순히 Pandas 함수의 문법을 익히는 것을 넘어, 특정 목표를 가지고 데이터를 탐색하고 가공하는 과정을 의미합니다.
*   **예시**: 타이타닉(Titanic) 승객 데이터셋을 활용한 생존 분석 실습
    *   **목표**: 승객의 나이, 성별, 탑승 등급 등이 생존 여부에 미치는 영향을 분석
    *   **과정**:
        1.  `pd.read_csv('titanic.csv')`로 데이터 로드
        2.  `df.info()`와 `df.describe()`로 데이터의 전반적인 특성 파악
        3.  `df['Age'].fillna(df['Age'].median(), inplace=True)`로 결측치 처리
        4.  `df.groupby('Sex')['Survived'].mean()`으로 성별 생존율 비교
        5.  `pd.crosstab(df['Pclass'], df['Survived'])`로 탑승 등급별 생존자 수 분석

이러한 실습을 통해 Pandas가 실제 데이터 분석 파이프라인에서 어떻게 활용되는지 깊이 이해할 수 있습니다.

**시험 포인트**:
⭐ 다음 실습 세션을 준비하라는 내용은 이전에 학습한 Pandas의 핵심 개념들이 시험에서도 중요하게 다루어질 것임을 시사합니다. 특히 다음과 같은 사항들은 실제 데이터셋을 다루는 능력과 직결되므로 시험에 출제될 가능성이 높습니다.
*   **DataFrame과 Series의 구조 및 차이점**: 각 데이터 구조의 특성을 이해하고 활용하는 능력.
*   **데이터 로딩 및 저장**: `pd.read_csv()`, `df.to_csv()` 등 외부 파일과의 연동.
*   **기본적인 데이터 탐색**: `df.head()`, `df.info()`, `df.describe()`, `df.shape`, `df.dtypes` 등의 활용.
*   **데이터 선택 및 필터링**: 라벨/위치 기반 인덱싱 (`.loc`, `.iloc`) 및 조건 필터링.
*   **결측치 처리**: `isnull()`, `dropna()`, `fillna()`를 이용한 결측 데이터 관리.
*   **그룹화 및 집계**: `groupby()`를 이용한 데이터 요약.

⭐ 실제 데이터 분석 문제 해결 능력을 평가하는 실습 또는 서술형 문제가 나올 수 있으므로, 단순 문법 암기보다는 Pandas 기능을 활용하여 데이터를 분석하는 과정을 이해하는 것이 중요합니다.

---

