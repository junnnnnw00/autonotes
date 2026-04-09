# CSED226 - pandasII 상세 해설 노트

> 이 노트는 Gemini 2.5 Flash를 이용해 자동 생성되었습니다.

---

## Slide 1

---
**핵심 개념**:
이 슬라이드는 Pandas 라이브러리에서 `DataFrame` 객체를 다루는 핵심 연산인 CRUD (Create, Read, Update, Delete)와 데이터 쿼리(Query)에 대해 다룰 것임을 소개합니다. `Pandas II`라는 제목에서 알 수 있듯이, 기본적인 DataFrame 생성 및 조작을 넘어선 좀 더 심화된 데이터 관리 및 추출 기법을 학습하는 모듈입니다.

*   **CRUD**: 데이터베이스 관리 시스템에서 주로 사용되는 용어로, 데이터 객체의 기본적인 4가지 연산을 의미합니다.
    *   **Create (생성)**: 새로운 DataFrame을 만들거나, 기존 DataFrame에 새로운 행(row) 또는 열(column)을 추가하는 연산.
    *   **Read (읽기/조회)**: DataFrame에서 특정 데이터를 선택하거나 조회하는 연산. 이는 데이터를 필터링하고 슬라이싱하는 것을 포함합니다.
    *   **Update (갱신)**: DataFrame의 특정 셀, 행, 또는 열의 값을 변경하는 연산.
    *   **Delete (삭제)**: DataFrame에서 특정 행 또는 열을 제거하는 연산.
*   **Query (쿼리)**: 특정 조건을 만족하는 데이터를 DataFrame에서 찾아내는 연산을 의미합니다. SQL의 `SELECT ... WHERE ...` 구문과 유사하게, 논리적인 조건식을 사용하여 원하는 부분집합의 데이터를 추출하는 방법입니다.

**코드/수식 해설**:
이 슬라이드는 제목이므로, 실제 코드는 다음 슬라이드부터 구체적으로 다루어질 예정입니다. 그러나 각 개념에 대한 기본적인 Pandas DataFrame 연산의 예시를 미리 생각해 볼 수 있습니다.

*   **Create (생성)**:
    ```python
    import pandas as pd
    # 새로운 DataFrame 생성
    df = pd.DataFrame({'Name': ['Alice'], 'Age': [25]})
    # 새로운 열 추가
    df['City'] = ['Seoul']
    # 새로운 행 추가 (append 또는 loc/iloc 사용)
    new_row = pd.DataFrame([{'Name': 'Bob', 'Age': 30, 'City': 'Busan'}])
    df = pd.concat([df, new_row], ignore_index=True)
    ```

*   **Read (읽기/조회)**:
    ```python
    # 특정 열 선택
    names = df['Name']
    # 특정 행 선택 (index 이용)
    first_row = df.loc[0]
    # 조건에 맞는 행 선택 (쿼리)
    young_people = df[df['Age'] < 30]
    ```

*   **Update (갱신)**:
    ```python
    # 특정 셀 값 변경
    df.loc[0, 'Age'] = 26
    # 조건에 맞는 모든 값 변경
    df.loc[df['City'] == 'Seoul', 'City'] = 'Incheon'
    ```

*   **Delete (삭제)**:
    ```python
    # 특정 열 삭제
    df = df.drop(columns=['City'])
    # 특정 행 삭제
    df = df.drop(index=0)
    ```

*   **Query (쿼리)**: (Read의 예시와 중복되지만, 조건식에 초점)
    ```python
    # 나이가 25세 이상 30세 미만인 사람 찾기
    filtered_df = df[(df['Age'] >= 25) & (df['Age'] < 30)]
    ```

**구체적 예시**:
회사의 고객 정보를 담은 스프레드시트(DataFrame)를 관리한다고 상상해 봅시다.
*   **Create**: 새로 가입한 고객의 정보를 스프레드시트에 한 줄(행) 추가하거나, 새로운 분석을 위해 '구매 등급'과 같은 새 열을 추가하는 것입니다.
*   **Read**: 1000명의 고객 중 특정 지역(예: 서울)에 거주하는 고객들의 이름만 확인하는 것입니다.
*   **Update**: 어떤 고객이 이사를 가서 주소 정보를 변경하거나, 전화번호가 바뀌어 업데이트하는 것입니다.
*   **Delete**: 더 이상 서비스를 이용하지 않는 탈퇴 고객의 정보를 스프레드시트에서 완전히 제거하는 것입니다.
*   **Query**: VIP 등급이면서 지난달 구매 금액이 100만원 이상인 고객 목록을 찾는 것과 같습니다.

**시험 포인트**:
*   ⭐ **DataFrame CRUD 연산의 각 의미를 정확히 이해하는 것이 중요합니다.** 특히 Pandas에서 각 연산을 수행하는 기본적인 메서드나 문법(예: `loc`, `iloc`, `drop`, 불리언 인덱싱)을 알아야 합니다.
*   ⭐ **불리언 인덱싱(Boolean Indexing)을 이용한 데이터 쿼리가 시험에 자주 출제됩니다.** 여러 조건을 조합하여 데이터를 필터링하는 방식($`&`$ (AND), $`|`$ (OR), $`~`$ (NOT))에 익숙해져야 합니다.
*   DataFrame이 불변(immutable)이 아닌 가변(mutable) 객체임을 이해하고, 연산 시 원본 DataFrame이 변경될 수 있는지 (in-place) 또는 새로운 DataFrame이 반환되는지 구분하는 것이 중요합니다.

---

## Slide 2

본 슬라이드는 데이터프레임 조작의 핵심인 CRUD(Create, Update, Delete, Query) 개념과 관계형 대수(ERA) 연산자를 pandas에서 어떻게 활용하는지에 대한 학습 목표를 제시합니다. 특히 그룹화 및 피벗 테이블의 중요성과 코드 작성 전 의미론적 사고의 필요성을 강조합니다.

---

### **핵심 개념**

*   **CRUD for pandas**: 데이터프레임을 생성(Create), 수정(Update), 삭제(Delete), 조회/질의(Query)하는 기본적인 데이터 조작 방법을 학습합니다. 이는 데이터 관리의 가장 근간이 되는 작업들입니다.
*   **ERA Operators**: 관계형 대수(Extended Relational Algebra, ERA) 연산자의 형식적인 정의를 이해하고, 이들이 pandas의 어떤 기능(메서드)에 대응되는지 매핑하는 방법을 배웁니다. 이는 데이터 조작의 이론적 배경을 제공합니다.
*   **Grouping/Pivoting**: ERA 연산자 중 특히 **$\gamma$ (감마) 연산자**가 나타내는 그룹화(grouping) 및 집계(aggregation) 개념을 심층적으로 다룹니다. 이를 pandas의 `groupby()` 메서드와 `pivot_table()`을 통해 실제 데이터 분석에 적용하는 방법을 학습합니다.
*   **Semantics**: 코드를 작성하기 전에 ERA 쿼리나 명확한 설명을 통해 데이터 조작의 **의미(Semantics)**를 먼저 정의하는 것의 중요성을 강조합니다. 이는 복잡한 데이터 분석 문제 해결 시 논리적이고 체계적인 접근을 가능하게 합니다.

### **코드/수식 해설**

*   **CRUD 기본 연산자 (pandas)**:
    *   **Create**: 새로운 DataFrame 또는 Series 생성
        ```python
        import pandas as pd
        df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        # 또는 기존 데이터에 새로운 열 추가
        df['C'] = [5, 6]
        ```
    *   **Query (Read)**: 데이터 선택 및 필터링
        ```python
        # 열 선택
        df['A']
        # 행 선택 (조건 필터링)
        df[df['A'] > 1]
        # loc / iloc을 이용한 선택
        df.loc[0, 'B'] # 특정 라벨 인덱스 기반 선택
        df.iloc[0, 1]  # 특정 정수 인덱스 기반 선택
        ```
    *   **Update**: 기존 데이터 수정
        ```python
        df.loc[0, 'A'] = 10 # 0번 행의 'A' 열 값 수정
        ```
    *   **Delete**: 데이터 삭제 (행 또는 열)
        ```python
        df_dropped_col = df.drop(columns=['C']) # 'C' 열 삭제
        df_dropped_row = df.drop(index=[0])   # 0번 행 삭제
        ```

*   **ERA $\gamma$ (Grouping/Aggregation) 연산자**:
    관계형 대수에서 그룹화 및 집계는 다음과 같이 표현될 수 있습니다.
    $$ \gamma_{A_1, ..., A_k, F_1(B_1), ..., F_m(B_m)}(R) $$
    여기서:
    *   $A_1, ..., A_k$는 그룹화 기준이 되는 속성(열)들입니다.
    *   $F_1(B_1), ..., F_m(B_m)$은 각 그룹에 대해 적용될 집계 함수($F_i$)와 해당 함수가 적용될 속성($B_i$)입니다 (예: SUM(수량), AVG(점수), COUNT(ID)).
    *   $R$은 원본 관계(테이블/DataFrame)입니다.

### **구체적 예시**

*   **그룹화/집계 (ERA $\gamma$ 및 `groupby()`):**
    학교 성적 데이터가 있다고 가정해 봅시다. 각 학생의 과목별 성적이 기록된 DataFrame이 있습니다.
    | 학생ID | 과목 | 점수 |
    | :----- | :--- | :--- |
    | 101    | 수학 | 90   |
    | 101    | 영어 | 85   |
    | 102    | 수학 | 78   |
    | 102    | 영어 | 92   |

    이 데이터에서 "각 학생ID별 평균 점수"를 구하고 싶다면 ERA $\gamma$ 연산자를 사용하여 다음과 같이 표현할 수 있습니다.
    $$ \gamma_{학생ID, AVG(점수)}(성적데이터) $$
    이를 pandas 코드로 구현하면 다음과 같습니다.
    ```python
    data = {'학생ID': [101, 101, 102, 102],
            '과목': ['수학', '영어', '수학', '영어'],
            '점수': [90, 85, 78, 92]}
    df_grades = pd.DataFrame(data)

    # 학생ID별 평균 점수 계산
    average_scores = df_grades.groupby('학생ID')['점수'].mean()
    print(average_scores)
    # 출력:
    # 학생ID
    # 101    87.5
    # 102    85.0
    # Name: 점수, dtype: float64
    ```

*   **피벗 테이블 (`pivot_table()`):**
    "과목을 열로, 학생ID를 행으로 하여 각 학생의 과목별 점수를 한눈에 보고 싶을 때" 유용합니다.
    ```python
    # 과목별 학생 점수를 피벗 테이블로 정리
    pivot_grades = df_grades.pivot_table(index='학생ID', columns='과목', values='점수')
    print(pivot_grades)
    # 출력:
    # 과목    영어  수학
    # 학생ID
    # 101   85  90
    # 102   92  78
    ```

### **시험 포인트**

*   pandas에서 데이터를 생성, 조회, 수정, 삭제하는 다양한 메서드(`pd.DataFrame()`, `df[...]`, `df.loc[]`, `df.iloc[]`, `df.drop()`)를 정확히 이해하고 활용할 수 있는가? ⭐
*   관계형 대수(ERA)의 $\gamma$ 연산자가 그룹화 및 집계(aggregation)를 의미함을 이해하고, 이를 pandas의 `groupby()` 메서드와 연결하여 설명할 수 있는가? ⭐
*   `groupby()`와 `pivot_table()`의 차이점과 각 기능이 어떤 상황에서 더 적합하게 사용되는지 설명하고 예시 코드를 작성할 수 있는가? ⭐
*   데이터 분석 문제 해결 시, 코딩에 앞서 요구사항을 ERA 쿼리나 명확한 언어로 먼저 정의하는 "Semantics"의 중요성에 대해 서술할 수 있는가? ⭐

---

## Slide 3

**핵심 개념**
*   **Pandas DataFrame 생성**: 파이썬 딕셔너리를 활용하여 `pandas.DataFrame` 객체를 생성하는 방법을 보여줍니다. 딕셔너리의 키(key)는 DataFrame의 컬럼 이름이 되고, 값(value)은 해당 컬럼의 데이터가 됩니다.
*   **Toy Dataset**: 실습 및 학습 목적으로 사용되는 작고 간단한 데이터셋을 의미합니다. 실제 복잡한 데이터를 다루기 전에 특정 기능이나 개념을 이해하는 데 유용합니다.
*   **`.shape` 속성**: DataFrame의 차원(dimension)을 나타내는 튜플(tuple)을 반환합니다. `(행의 수, 열의 수)` 형식으로 구성됩니다.

**코드/수식 해설**

```python
import pandas as pd
import numpy as np

# 데이터 딕셔너리 생성
# 각 키는 DataFrame의 컬럼 이름이 되고, 값은 해당 컬럼의 데이터 리스트가 됩니다.
# ['CA']*4는 ['CA', 'CA', 'CA', 'CA'] 리스트를 생성합니다.
data = {'State': ['CA']*4, 
        'Sex': ['F']*4, 
        'Year': [1910]*4,
        'Name': ['Mary', 'Helen', 'Dorothy', 'Margaret'],
        'Count': [295, 239, 220, 163]}

# 딕셔너리 'data'를 사용하여 pandas DataFrame을 생성합니다.
# 이 DataFrame은 'State', 'Sex', 'Year', 'Name', 'Count'의 5개 컬럼을 가집니다.
babynames = pd.DataFrame(data)

# babynames DataFrame의 차원(행, 열)을 출력합니다.
# 위 data 딕셔너리의 리스트 길이를 보면 4개의 행과 5개의 컬럼이 있음을 알 수 있습니다.
print(babynames.shape)
```
이 코드를 실행하면 다음과 같은 출력이 예상됩니다:
```
(4, 5)
```

**구체적 예시**
`babynames = pd.DataFrame(data)` 실행 후 `babynames` DataFrame은 다음과 같은 형태를 가질 것입니다:

| State | Sex | Year | Name    | Count |
| :---- | :-- | :--- | :------ | :---- |
| CA    | F   | 1910 | Mary    | 295   |
| CA    | F   | 1910 | Helen   | 239   |
| CA    | F   | 1910 | Dorothy | 220   |
| CA    | F   | 1910 | Margaret| 163   |

`.shape`를 호출하면 이 DataFrame이 4개의 행과 5개의 열로 구성되어 있음을 알려주는 `(4, 5)`라는 튜플을 반환합니다. 이는 마치 4줄짜리 명부가 있고, 각 줄마다 5가지 정보(주, 성별, 연도, 이름, 횟수)가 기록된 것과 같습니다.

**시험 포인트**
*   ⭐ **Pandas DataFrame 생성 방법**: 딕셔너리를 이용한 DataFrame 생성 문법 (`pd.DataFrame(dictionary)`)을 정확히 이해하고 있어야 합니다.
*   ⭐ **`.shape` 속성의 역할**: DataFrame의 `.shape`가 무엇을 반환하는지 (행, 열 튜플) 그리고 데이터셋의 크기를 파악하는 데 어떻게 사용되는지 알고 있어야 합니다.
*   ⭐ **Python 리스트 연산**: `['CA']*4`와 같이 리스트에 정수를 곱하는 연산의 결과를 이해해야 합니다. (리스트를 반복하여 새로운 리스트를 생성)
*   ⭐ `import pandas as pd`와 같은 표준 라이브러리 임포트 구문이 왜 필요한지, `pd`가 무엇을 의미하는지 이해해야 합니다.

---

## Slide 4

이 슬라이드는 pandas DataFrame에서 데이터를 생성(Create), 수정(Update), 삭제(Delete)하는 다양한 API와 그 동작 방식을 설명합니다. 특히 각 작업이 어떻게 데이터프레임을 변경하는지(mutation 여부)와 관계형 대수(Extended Relational Algebra, ERA) 개념과 연결하여 이해를 돕습니다.

### 핵심 개념
*   **CRUD in pandas**: pandas DataFrame에서 데이터를 생성(Create), 수정(Update), 삭제(Delete)하는 기본적인 연산들을 의미합니다. "Read"는 주로 인덱싱, 필터링 등으로 슬라이드 범위 밖이지만, 여기서는 CUD에 중점을 둡니다.
*   **API 및 동작**: 각 pandas 함수(API)가 실제로 데이터프레임에 어떤 변화를 주는지(새로운 DataFrame 반환 vs. 원본 DataFrame 변경)를 명확히 이해하는 것이 중요합니다.
*   **Mutable vs. Immutable Operations**: 일부 연산은 원본 DataFrame을 직접 변경(in-place modification 또는 mutation)하는 반면, 다른 연산은 변경된 내용이 반영된 새로운 DataFrame을 반환하고 원본은 그대로 둡니다.
*   **관계형 대수(ERA) 매핑**: pandas의 데이터 조작 연산이 관계형 데이터베이스의 기본적인 연산(합집합, 프로젝트, 선택 등)과 어떻게 대응되는지 보여줍니다.

### 코드/수식 해설

**1. Create Operations (생성)**

*   **`pd.concat([df1, df2], axis=0)`**: 두 DataFrame을 행(row) 방향으로 이어 붙여 새로운 DataFrame을 생성합니다. 인덱스가 중복될 수 있으며, `drop_duplicates()`와 함께 사용하여 집합 의미의 합집합을 만들 수 있습니다.
    *   ERA: $\cup + \delta$ (Union with duplicates)
*   **`pd.concat([df1, df2], axis=1)`**: 두 DataFrame을 열(column) 방향으로 인덱스를 기준으로 정렬하여 이어 붙입니다.
    *   ERA: reshape / attribute extension
*   **`df.assign(new_col=expression, ...)`**: 기존 DataFrame을 변경하지 않고, 새로운 계산된 열(column)을 추가하여 새로운 DataFrame을 반환합니다.
    *   ERA: generalized projection $\pi^*$
*   **`df.loc[new_idx] = row_data`**: 지정된 `new_idx` 라벨에 해당하는 새 행을 삽입하거나, 기존 행이 있다면 덮어씁니다. 이 작업은 원본 DataFrame을 직접 변경(mutation)합니다.
    *   ERA: Not pure RA
*   **`df.insert(pos, "col_name", values)`**: 특정 위치(`pos`)에 새로운 열을 삽입합니다. 이 작업은 원본 DataFrame을 직접 변경(mutation)합니다.
    *   ERA: $\pi^*$
*   **`df.reindex(new_index, columns=new_columns)`**: 지정된 `new_index`와 `new_columns`에 맞게 DataFrame의 형태를 재구성합니다. 없는 행이나 열은 `NaN`으로 채워집니다.
    *   ERA: reshape

**2. Update Operations (수정)**

*   **`df.loc[keys, cols] = values`**: 라벨(`keys`)과 열(`cols`)을 사용하여 특정 셀 또는 슬라이싱된 부분에 `values`를 할당합니다. 벡터화된 연산이며 인덱스에 따라 정렬됩니다. 이 작업은 원본 DataFrame을 직접 변경(mutation)합니다.
*   **`df.at[row, col] = scalar_value`**: `df.loc`과 유사하지만, 단일 셀의 값을 라벨로 빠르게 설정할 때 사용합니다. 이 작업은 원본 DataFrame을 직접 변경(mutation)합니다.
*   **`df.where(condition, other)`**: `condition`이 `True`인 경우의 값을 유지하고, `False`인 경우 `other`의 값(기본값은 `NaN`)으로 대체한 새로운 DataFrame을 반환합니다.
    *   ERA: selection as guard $\sigma$
*   **`df.mask(condition, other)`**: `df.where`와 반대로, `condition`이 `True`인 경우 `other`의 값으로 대체하고, `False`인 경우의 값을 유지한 새로운 DataFrame을 반환합니다. (즉, `where`의 역)
*   **`df.replace(old_value, new_value)`**: DataFrame 내의 특정 `old_value`를 `new_value`로 대체한 새로운 DataFrame을 반환합니다. 딕셔너리, 리스트 또는 정규식을 사용할 수 있습니다.
*   **`df.assign(col=f(df))`**: `Create` 섹션의 `assign`과 동일하게, 함수 `f`를 적용하여 열을 계산하고 새로운 DataFrame을 반환합니다. 기능적 업데이트(functional update)로 원본은 변경되지 않습니다.
    *   ERA: $\pi^*$

**3. Delete Operations (삭제)**

*   **`df.drop(labels, axis=0)`**: 지정된 `labels`에 해당하는 행(기본값 `axis=0`)을 삭제하고, 변경된 새로운 DataFrame을 반환합니다. `inplace=True` 옵션으로 원본을 변경할 수 있습니다.
*   **`df.drop(labels, axis=1)`**: 지정된 `labels`에 해당하는 열(column, `axis=1`)을 삭제하고, 변경된 새로운 DataFrame을 반환합니다. `inplace=True` 옵션으로 원본을 변경할 수 있습니다.
*   **`df.dropna(subset=[col1, ...])`**: 지정된 `subset` 열에 `NA`(결측치)가 있는 행을 삭제하고 새로운 DataFrame을 반환합니다.
    *   ERA: $\sigma$ on `is_not_null`
*   **`df.pop("col_name")`**: 지정된 "col\_name" 열을 DataFrame에서 삭제하고, 삭제된 열을 `Series` 형태로 반환합니다. 이 작업은 원본 DataFrame을 직접 변경(in-place)합니다.
*   **`del df["col_name"]`**: 지정된 "col\_name" 열을 DataFrame에서 삭제합니다. `pop`과 달리 아무것도 반환하지 않습니다. 이 작업은 원본 DataFrame을 직접 변경(in-place)합니다.

### 구체적 예시

```python
import pandas as pd
import numpy as np

# 초기 DataFrame 생성
data = {'col1': [1, 2, 3, 4],
        'col2': ['A', 'B', 'C', 'D'],
        'col3': [True, False, True, False]}
df = pd.DataFrame(data, index=['r1', 'r2', 'r3', 'r4'])
print("Original DataFrame:\n", df)

# --- Create Operations ---
print("\n--- Create Operations ---")
# 1. pd.concat (axis=0) - 행 추가
df_new_row = pd.DataFrame({'col1': [5], 'col2': ['E'], 'col3': [True]}, index=['r5'])
df_concat_row = pd.concat([df, df_new_row], axis=0)
print("\nAfter pd.concat (axis=0):\n", df_concat_row)

# 2. df.assign - 새 열 추가 (원본 변경 X)
df_assigned = df.assign(col4=[10, 20, 30, 40], col5=df['col1'] * 10)
print("\nAfter df.assign (new cols):\n", df_assigned)
print("Original DataFrame (unchanged after assign):\n", df)

# 3. df.loc - 새 행 삽입 (원본 변경 O)
df_loc_mutate = df.copy() # 원본 보존을 위해 복사
df_loc_mutate.loc['r5'] = [5, 'E', False]
print("\nAfter df.loc['r5'] = [...] (mutation):\n", df_loc_mutate)

# --- Update Operations ---
print("\n--- Update Operations ---")
# 1. df.loc - 특정 값 업데이트 (원본 변경 O)
df_loc_update = df.copy()
df_loc_update.loc['r2', 'col1'] = 99
print("\nAfter df.loc['r2', 'col1'] = 99 (mutation):\n", df_loc_update)

# 2. df.at - 단일 셀 업데이트 (원본 변경 O)
df_at_update = df.copy()
df_at_update.at['r3', 'col2'] = 'Z'
print("\nAfter df.at['r3', 'col2'] = 'Z' (mutation):\n", df_at_update)

# 3. df.where - 조건에 따라 값 유지/변경 (원본 변경 X)
df_where = df.where(df['col1'] > 2, 0)
print("\nAfter df.where(df['col1'] > 2, 0):\n", df_where)

# 4. df.replace - 값 대체 (원본 변경 X)
df_replaced = df.replace({'A': 'X', 'C': 'Y'})
print("\nAfter df.replace({'A':'X', 'C':'Y'}):\n", df_replaced)

# --- Delete Operations ---
print("\n--- Delete Operations ---")
# 1. df.drop (axis=0) - 행 삭제 (원본 변경 X)
df_dropped_row = df.drop('r1', axis=0)
print("\nAfter df.drop('r1', axis=0):\n", df_dropped_row)

# 2. df.drop (axis=1) - 열 삭제 (원본 변경 X)
df_dropped_col = df.drop('col3', axis=1)
print("\nAfter df.drop('col3', axis=1):\n", df_dropped_col)

# 3. df.dropna - 결측치 있는 행 삭제 (원본 변경 X)
df_na = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})
df_dropna = df_na.dropna()
print("\nOriginal DataFrame with NA:\n", df_na)
print("After df_na.dropna():\n", df_dropna)

# 4. df.pop - 열 삭제 및 반환 (원본 변경 O)
df_pop_mutate = df.copy()
popped_col2 = df_pop_mutate.pop('col2')
print("\nAfter df_pop_mutate.pop('col2') (mutation):\n", df_pop_mutate)
print("Popped Series:\n", popped_col2)

# 5. del df["col"] - 열 삭제 (원본 변경 O)
df_del_mutate = df.copy()
del df_del_mutate['col3']
print("\nAfter del df_del_mutate['col3'] (mutation):\n", df_del_mutate)
```

### 시험 포인트

*   ⭐ **In-place 연산 vs. 새로운 DataFrame 반환 연산 구분**:
    *   원본 DataFrame을 직접 변경하는 연산(mutation): `df.loc[...] = value`, `df.at[...,...] = value`, `df.insert()`, `df.pop()`, `del df[...]`.
    *   새로운 DataFrame을 반환하고 원본은 그대로 두는 연산: `pd.concat()`, `df.assign()`, `df.where()`, `df.mask()`, `df.replace()`, `df.drop()`, `df.dropna()`. `inplace=True` 옵션을 통해 일부 연산을 in-place로 만들 수 있음에 유의.
*   ⭐ **`axis=0` (행)과 `axis=1` (열)의 의미**: `pd.concat`, `df.drop` 등에서 `axis` 파라미터가 행 방향 연산과 열 방향 연산을 구분함을 이해해야 합니다.
*   ⭐ **`df.loc`과 `df.at`의 차이점**: `df.loc`은 라벨 기반의 다중 행/열 선택 및 업데이트에 사용되며, `df.at`은 단일 셀 값을 라벨로 빠르게 접근하고 업데이트할 때 최적화되어 있습니다.
*   ⭐ **`df.where`와 `df.mask`의 차이점**: `where`는 조건이 참인 경우 유지, `mask`는 조건이 참인 경우 대체입니다. 서로 역의 관계입니다.
*   ⭐ **`df.pop()`과 `del df[...]`의 차이점**: 둘 다 열을 삭제하지만, `df.pop()`은 삭제된 열(Series)을 반환하는 반면, `del`은 아무것도 반환하지 않습니다.

---

## Slide 5

이 슬라이드는 pandas DataFrame에서 데이터를 조회하고 조작하는 다양한 API와 그에 해당하는 Relational Algebra(관계 대수) 연산을 설명합니다.

---

### **핵심 개념**

*   **`df.loc[]`**: 불리언 마스크를 사용하여 DataFrame의 행을 선택하고, 필요에 따라 특정 열을 추출하는 데 사용됩니다. 이는 관계 대수의 **선택(selection)** 연산($\sigma$)에 해당합니다.
*   **`df.query()`**: SQL의 `WHERE` 절과 유사하게 문자열 표현식을 사용하여 DataFrame의 행을 필터링합니다. 이 또한 관계 대수의 **선택(selection)** 연산($\sigma$)입니다.
*   **`pd.merge()`**: 두 DataFrame을 특정 키(key)를 기준으로 결합(join)합니다. `inner`, `left`, `right`, `outer`, `cross` 등 다양한 조인 방식을 지원하며, 이는 관계 대수의 **조인($\bowtie$)** 또는 **카르테시안 곱($\times$)** 연산에 해당합니다.
*   **`df.groupby().agg()`**: 하나 이상의 열을 기준으로 DataFrame을 그룹화한 후, 각 그룹에 대해 합계, 평균 등과 같은 집계(aggregation) 함수를 적용합니다. 이는 관계 대수의 **그룹화 및 집계($\gamma_{G,f(. )}$)** 연산입니다.
*   **`df.drop_duplicates()`**: DataFrame에서 중복된 행을 제거합니다. 특정 열의 조합을 기준으로 중복을 제거할 수도 있습니다. 이는 관계 대수의 **중복 제거($\delta$)** 연산에 해당합니다.
*   **`df.sort_values()`**: 하나 이상의 열을 기준으로 DataFrame의 행들을 오름차순 또는 내림차순으로 정렬합니다. 이는 확장된 관계 대수의 **정렬($\tau$)** 연산입니다.
*   **`pd.concat()`**: 여러 DataFrame이나 Series를 특정 축(axis)을 따라 이어 붙입니다. `axis=0`은 행을 기준으로 스택하고, `axis=1`은 열을 기준으로 이어 붙입니다. 이는 관계 대수의 **합집합($\cup$)** 연산과 유사하며, 중복을 제거하면 집합의 합집합이 됩니다.
*   **`pd.crosstab()`**: 두 개 이상의 범주형 변수 간의 빈도를 교차표 형태로 계산합니다. 이는 관계 대수에서 `count(*)` 함수를 사용한 **피벗(PIVOT)** 연산에 해당합니다.
*   **`df.pivot_table()`**: `crosstab`보다 더 일반적인 피벗 기능을 제공합니다. 특정 열을 인덱스, 열, 값으로 지정하고 다양한 집계 함수(`aggfunc`)를 적용하여 데이터를 재구성합니다. 이는 일반적인 집계 함수 $f$를 사용한 **피벗(PIVOT)** 연산에 해당합니다.

### **코드/수식 해설**

*   **선택 (Selection)**:
    *   불리언 인덱싱:
        ```python
        filtered_df = df.loc[df['score'] > 80]
        ```
    *   쿼리 문자열:
        ```python
        filtered_df = df.query("score > 80 and grade == 'A'")
        ```
    *   관계 대수: $\sigma_{P}(R)$ (여기서 $P$는 조건, $R$은 릴레이션)

*   **조인 (Join)**:
    *   `pd.merge`:
        ```python
        merged_df = pd.merge(df1, df2, on='common_id', how='inner')
        ```
    *   관계 대수: $R \bowtie_P S$ (여기서 $P$는 조인 조건, $R, S$는 릴레이션)

*   **그룹화 및 집계 (Grouping and Aggregation)**:
    *   `df.groupby().agg()`:
        ```python
        summary_df = df.groupby('category')['value_column'].mean()
        # 여러 집계 함수 적용
        summary_df_multi = df.groupby('category').agg(
            total_sales=('sales', 'sum'),
            avg_price=('price', 'mean')
        )
        ```
    *   관계 대수: $\gamma_{G,f_1(A_1), f_2(A_2), ...}(R)$ (여기서 $G$는 그룹화 기준 속성, $f_i(A_i)$는 집계 함수와 속성)

*   **중복 제거 (Duplicate Elimination)**:
    *   `df.drop_duplicates()`:
        ```python
        unique_df = df.drop_duplicates(subset=['user_id', 'product_id'])
        ```
    *   관계 대수: $\delta(R)$

*   **정렬 (Sorting)**:
    *   `df.sort_values()`:
        ```python
        sorted_df = df.sort_values(by=['score', 'name'], ascending=[False, True])
        ```
    *   관계 대수 (확장): $\tau_{A \text{ desc}, B \text{ asc}}(R)$

*   **결합 (Concatenation)**:
    *   `pd.concat()`:
        ```python
        combined_df = pd.concat([df_q1, df_q2, df_q3, df_q4], axis=0)
        ```
    *   관계 대수: $R \cup S$ (집합 합집합, pandas는 기본적으로 멀티셋 합집합처럼 동작하며, `drop_duplicates`를 적용하면 집합 합집합이 됨)

*   **피벗 테이블 (Pivot Table)**:
    *   `pd.crosstab()`:
        ```python
        contingency_table = pd.crosstab(df['gender'], df['education_level'])
        ```
    *   `df.pivot_table()`:
        ```python
        pivot_table_df = df.pivot_table(
            index='Date',
            columns='ProductCategory',
            values='SalesAmount',
            aggfunc='sum'
        )
        ```
    *   관계 대수: `PIVOT` 연산 (특정 집계 함수와 함께)

### **구체적 예시**

어떤 쇼핑몰의 고객 구매 데이터를 `df`라는 DataFrame으로 가지고 있다고 가정해 봅시다. 이 데이터에는 `customer_id`, `product_category`, `price`, `purchase_date` 등의 컬럼이 있습니다.

*   **특정 기간의 고가 상품 구매 내역 조회**: `df.query("purchase_date >= '2023-01-01' and purchase_date < '2023-02-01' and price > 100")`
*   **카테고리별 총 판매액 및 평균 구매 가격 계산**: `df.groupby('product_category').agg(total_sales=('price', 'sum'), avg_price=('price', 'mean'))`
*   **최근 가장 많이 구매한 고객 10명 찾기**: `df.sort_values(by='purchase_date', ascending=False).drop_duplicates(subset=['customer_id']).head(10)`
*   **고객 성별과 제품 카테고리 간의 구매 빈도 분석**: `pd.crosstab(df['customer_gender'], df['product_category'])`

### **시험 포인트**

*   ⭐ **각 pandas API가 어떤 관계 대수 연산에 해당하는지 정확히 매칭할 수 있어야 합니다.** (예: `df.loc`과 `df.query`는 $\sigma$, `pd.merge`는 $\bowtie$ 또는 $\times$, `df.groupby`는 $\gamma$, `df.drop_duplicates`는 $\delta$, `df.sort_values`는 $\tau$, `pd.concat`는 $\cup$ (with $\delta$), `pd.crosstab`/`df.pivot_table`은 PIVOT).
*   ⭐ **각 API의 핵심 인자와 그 역할(예: `pd.merge`의 `on`, `how`, `df.groupby`의 `keys`, `aggfunc`, `df.pivot_table`의 `index`, `columns`, `values`, `aggfunc`)을 이해하고 활용할 수 있어야 합니다.**
*   ⭐ **주어진 데이터 분석 요구사항(예: 특정 조건에 맞는 데이터 필터링, 두 테이블 결합, 그룹별 통계 계산)에 맞는 적절한 pandas API를 선택하고 코드를 작성할 수 있어야 합니다.**
*   `pd.crosstab`과 `df.pivot_table`의 차이점 및 활용 시나리오를 설명할 수 있어야 합니다. (`crosstab`은 주로 빈도수 계산, `pivot_table`은 더 일반적인 집계 가능).

---

## Slide 6

이 슬라이드는 Pandas DataFrame에 새로운 행(row)과 열(column)을 추가하는 다양한 방법을 설명합니다. 특히, 데이터 분석 과정에서 데이터를 확장하고 변형하는 핵심적인 기법들을 다룹니다.

---

### **핵심 개념**

*   **DataFrame에 행 추가**: Pandas DataFrame에 새로운 데이터를 행 단위로 추가하는 방법은 단일 행을 추가하는 방식과 여러 행을 일괄적으로 추가하는 배치(batch) 방식이 있습니다. 특히 여러 행을 추가할 때는 효율성을 고려한 `pd.concat` 함수 사용이 권장됩니다.
*   **DataFrame에 열 추가**: 기존 열의 데이터를 활용하여 새로운 파생 열(derived column)을 생성하거나, 여러 열의 데이터를 결합하여 새로운 열을 만들어 특정 위치에 삽입할 수 있습니다.
*   **데이터프레임의 변경 (Mutation)**: 슬라이드 노트에서 언급되었듯이, Pandas의 `Create` 연산은 기존 DataFrame 객체를 직접 변경(mutate)합니다. 이는 데이터베이스의 ERA (Entity-Relationship-Attribute) 쿼리 연산과 유사합니다.

### **코드/수식 해설**

```python
# 1. 단일 행 추가: DataFrame의 마지막에 새로운 행을 추가합니다.
babynames.loc[len(babynames)] = ["CA", "F", 2023, "Nova", 12]
```
*   `babynames.loc[len(babynames)]`: `.loc` 인덱서를 사용하여 DataFrame의 `len(babynames)` 위치에 접근합니다. `len(babynames)`는 현재 DataFrame의 마지막 인덱스 다음 위치가 되므로, 새로운 행을 추가하는 효과가 있습니다.
*   `[...]`: 추가할 행의 데이터를 리스트 형태로 제공하며, 이 리스트의 요소들은 DataFrame의 각 열에 대응됩니다.

```python
# 2. 여러 행 배치 추가 (권장 방식): 여러 행을 한 번에 효율적으로 추가합니다.
rows = [("CA", "M", 2023, "Atlas", 9), ("CA", "F", 2024, "Mira", 7)]
babynames = pd.concat([babynames, pd.DataFrame(rows, columns=babynames.columns)], ignore_index=True)
```
*   `rows = [...]`: 추가할 여러 행의 데이터를 튜플 또는 리스트의 리스트 형태로 준비합니다.
*   `pd.DataFrame(rows, columns=babynames.columns)`: `rows` 리스트를 사용하여 새로운 DataFrame을 생성합니다. 이때 `columns=babynames.columns`를 지정하여 기존 `babynames` DataFrame과 동일한 열 이름을 갖도록 합니다.
*   `pd.concat([...], ignore_index=True)`: 기존 `babynames` DataFrame과 새로 생성한 DataFrame을 수직으로 결합(concatenation)합니다.
    *   `[babynames, new_df]`: 결합할 DataFrame들의 리스트입니다.
    *   `ignore_index=True`: ⭐ **매우 중요**합니다. 결합 후 인덱스가 중복되지 않도록 새롭고 연속적인 인덱스를 자동으로 생성합니다. 이를 생략하면 원본 DataFrame과 새로 추가된 DataFrame의 인덱스가 유지되어 중복 문제가 발생할 수 있습니다.

```python
# 3. 새로운 열 파생 및 삽입: 기존 열을 활용하여 새로운 열을 만듭니다.
babynames["decade"] = (babynames["Year"] // 10) * 10
```
*   `babynames["decade"] = ...`: `decade`라는 이름의 새로운 열을 DataFrame에 추가하거나, 이미 존재한다면 해당 열의 값을 업데이트합니다.
*   `(babynames["Year"] // 10) * 10`: "Year" 열의 각 값에 대해 정수 나눗셈(`//`)과 곱셈을 수행하여 해당 연도가 속한 10년 단위의 시작 연도를 계산합니다 (예: 2023 -> (2023 // 10) * 10 = 202 * 10 = 2020).

```python
# 4. 특정 위치에 새로운 열 삽입: 기존 문자열 열을 결합하여 새로운 열을 만들고 특정 위치에 삽입합니다.
babynames.insert(0, "state_sex", babynames["State"].str.cat(babynames["Sex"], sep="-"))
```
*   `babynames.insert(0, "state_sex", ...)`: DataFrame에 새로운 열을 특정 위치에 삽입하는 메서드입니다.
    *   `0`: 삽입할 열의 위치 (0은 가장 왼쪽 열).
    *   `"state_sex"`: 새로 생성될 열의 이름.
    *   `babynames["State"].str.cat(babynames["Sex"], sep="-")`: `State` 열과 `Sex` 열의 문자열 값들을 결합하여 새로운 Series를 생성합니다.
        *   `.str`: Pandas Series의 문자열 메서드를 사용할 수 있게 해주는 accessor입니다.
        *   `.cat()`: 두 문자열 Series를 연결합니다.
        *   `sep="-"`: 연결할 때 사용할 구분자(separator)를 지정합니다 (예: "CA"와 "F"가 "CA-F"로 결합됨).

### **구체적 예시**

`babynames` DataFrame이 각 아기의 출생 주(State), 성별(Sex), 연도(Year), 이름(Name), 출생아 수(Count) 정보를 담고 있다고 가정해 봅시다.

*   **단일 행 추가**: "2023년 캘리포니아(CA) 주에서 'Nova'라는 이름의 여아(F)가 12명 태어났다"는 새로운 기록을 `babynames.loc[len(babynames)] = ["CA", "F", 2023, "Nova", 12]` 코드를 통해 한 줄 추가할 수 있습니다.
*   **여러 행 배치 추가**: "2023년 캘리포니아(CA) 주에서 'Atlas'라는 남아(M) 9명"과 "2024년 캘리포니아(CA) 주에서 'Mira'라는 여아(F) 7명"이라는 두 개의 새로운 기록을 한 번에 효율적으로 추가하려면 `pd.concat`을 사용합니다.
*   **'decade' 열 생성**: 2023년 데이터가 있다면, 이 아기의 출생 연도 `2023`을 이용해 `(2023 // 10) * 10` 계산을 통해 `2020`이라는 'decade' 값을 갖는 새로운 열을 만들 수 있습니다. 이를 통해 아기가 태어난 10년 단위의 연도 그룹을 파악할 수 있습니다.
*   **'state_sex' 열 삽입**: 캘리포니아 주에서 태어난 여아(CA-F) 데이터가 있다면, `babynames["State"].str.cat(babynames["Sex"], sep="-")`를 통해 "CA-F"라는 문자열을 만들어 'state_sex'라는 새로운 열로 추가하고, 이 열을 가장 왼쪽(0번 인덱스)에 배치하여 데이터의 식별성을 높일 수 있습니다.

### **시험 포인트**

*   ⭐ **Pandas DataFrame에 새로운 행을 추가하는 두 가지 주요 방법(단일 vs. 배치)을 설명하고, 각 방법의 장단점을 비교하시오.** 특히, `pd.concat` 사용 시 `ignore_index=True` 옵션의 필요성과 역할에 대해 정확히 이해하고 있어야 합니다.
*   ⭐ **기존 열을 기반으로 새로운 파생 열을 생성하는 방법과 특정 위치에 새로운 열을 삽입하는 방법 (`.insert()` 메서드)을 코드 예시와 함께 설명하시오.**
*   ⭐ **Pandas에서 문자열 데이터를 다룰 때 `Series.str` accessor가 제공하는 기능(예: `.str.cat()`)과 그 활용법에 대해 설명하시오.**
*   ⭐ `babynames.loc[len(babynames)] = [...]`와 같이 `len(df)`를 인덱스로 사용하여 행을 추가하는 방식의 원리를 설명하시오.
*   ⭐ **Pandas DataFrame을 조작하는 `Create` 연산이 원본 DataFrame 객체를 변경(mutate)한다는 점을 인지하고 있어야 합니다.** 이는 데이터 처리의 중요한 개념입니다.

---

## Slide 7

**핵심 개념**:
*   **Pandas DataFrame 업데이트**: `pandas` DataFrame의 특정 셀 또는 여러 셀의 값을 조건에 따라 변경하는 다양한 방법을 설명합니다. 이는 SQL의 `UPDATE` 문과 유사하게 기존 데이터를 수정하는 작업입니다.
*   **ERA 쿼리와의 차이점**: 슬라이드에서 언급된 대로, 데이터프레임의 업데이트는 ERA(Entity-Relationship Algebra) 쿼리가 아닙니다. ERA 쿼리는 보통 새로운 관계(테이블)를 생성하며 원본 데이터를 직접 수정하지 않는 반면, 데이터프레임 업데이트는 기존 데이터프레임의 튜플(행)과 속성(열)을 직접 수정합니다. 이는 데이터 조작의 근본적인 차이를 나타냅니다.
*   **Boolean 인덱싱 기반 업데이트**: 특정 조건을 만족하는 행(튜플)을 선택하기 위해 불리언(Boolean) 시리즈를 인덱스로 활용하여 데이터를 업데이트하는 방식이 가장 흔하며 강력합니다.

**코드/수식 해설**:

1.  **Point update (특정 지점 업데이트)**
    ```python
    ix = (babynames["Name"]=="Mary") & (babynames["Year"]==1910)
    babynames.loc[ix, "Count"] = babynames.loc[ix, "Count"] + 1
    ```
    *   첫 번째 줄은 `babynames` DataFrame에서 "Name"이 "Mary"이고 "Year"가 1910인 모든 행을 찾는 불리언 인덱스 `ix`를 생성합니다. 두 조건은 `&` (AND) 연산자로 결합됩니다.
    *   두 번째 줄은 `loc` 인덱서를 사용하여 `ix`로 선택된 행들의 "Count" 컬럼 값을 기존 값에 1을 더하여 업데이트합니다.

2.  **Conditional update (조건부 업데이트)**
    ```python
    low = babynames["Count"] < 10
    babynames.loc[low, "Count"] = 0
    ```
    *   첫 번째 줄은 `babynames` DataFrame에서 "Count" 컬럼의 값이 10 미만인 모든 행을 찾는 불리언 인덱스 `low`를 생성합니다.
    *   두 번째 줄은 `low`로 선택된 행들의 "Count" 컬럼 값을 모두 0으로 설정하여 업데이트합니다.

3.  **Map / replace (매핑/교체)**
    ```python
    babynames["Sex"] = babynames["Sex"].replace({"F":"Female", "M":"Male"})
    ```
    *   `replace()` 메서드를 사용하여 "Sex" 컬럼의 특정 값을 다른 값으로 일괄 변경합니다. 여기서는 딕셔너리 `{"F":"Female", "M":"Male"}`를 사용하여 'F'는 'Female'로, 'M'은 'Male'로 바꿉니다.

4.  **Where/Mask idiom (`np.where` 사용)**
    ```python
    high = babynames["Count"] >= 100
    babynames["pop_flag"] = np.where(high, "popular", "normal")
    ```
    *   첫 번째 줄은 "Count" 컬럼의 값이 100 이상인 모든 행을 찾는 불리언 인덱스 `high`를 생성합니다.
    *   두 번째 줄은 `numpy.where()` 함수를 사용하여 "pop_flag"라는 새로운 컬럼을 생성하거나 기존 컬럼을 업데이트합니다. `np.where(condition, x, y)`는 `condition`이 True이면 `x`를, False이면 `y`를 반환합니다. 따라서, `high`가 True인 행에는 "popular"를, False인 행에는 "normal"을 "pop_flag" 컬럼에 할당합니다.

**구체적 예시**:
`babynames` DataFrame이 아기 이름, 출생 연도, 성별, 출생아 수를 담고 있다고 가정해봅시다.

*   **Point update**: "1910년에 태어난 'Mary'의 출생아 수가 데이터 입력 오류로 인해 실제보다 1명 적게 기록되어 있어, 해당 레코드의 `Count` 값을 1 증가시켜 정확한 값으로 수정합니다."
*   **Conditional update**: "출생아 수가 10명 미만인 희귀 이름들은 통계적 의미가 적다고 판단하여, 해당 레코드들의 `Count` 값을 모두 0으로 초기화하여 분석에서 제외합니다."
*   **Map / replace**: "데이터의 일관성과 가독성을 높이기 위해 성별 코드가 'F'와 'M'으로 약어 처리된 것을 각각 'Female'과 'Male'이라는 전체 이름으로 변경합니다."
*   **Where/Mask idiom**: "출생아 수가 100명 이상인 이름에는 'popular'라는 플래그를, 그렇지 않은 이름에는 'normal'이라는 플래그를 'pop_flag'라는 새로운 컬럼에 부여하여, 이름의 인기도를 기준으로 쉽게 데이터를 분류하고 분석할 수 있도록 합니다."

**시험 포인트**:
*   ⭐ **Pandas DataFrame에서 특정 조건에 맞는 데이터를 업데이트하는 다양한 방법(`loc`를 활용한 point/conditional update, `replace()` 메서드, `numpy.where()` 함수)을 이해하고, 각 방법의 적절한 사용 시점을 설명할 수 있어야 합니다.**
*   ⭐ **`DataFrame.loc[row_indexer, column_indexer]`를 사용하여 데이터를 선택하고 업데이트하는 문법을 정확히 사용할 수 있어야 합니다.** 특히, 불리언 인덱싱을 활용한 복합 조건 업데이트가 중요합니다.
*   ⭐ **`Series.replace()` 메서드와 `numpy.where()` 함수의 기능 및 사용법을 숙지하고, 이들이 데이터를 어떻게 변형하는지 예시와 함께 설명할 수 있어야 합니다.**
*   ⭐ **데이터프레임 업데이트가 ERA 쿼리와 어떤 점에서 다른지 (원본 데이터 수정 여부) 그 근본적인 차이점을 설명할 수 있어야 합니다.**

---

## Slide 8

이 슬라이드는 pandas DataFrame에서 컬럼 또는 행 데이터를 삭제하는 다양한 방법을 예시와 함께 보여줍니다.

---

### **핵심 개념**

*   **데이터 삭제**: pandas DataFrame에서 특정 컬럼(속성) 또는 행(튜플)을 제거하는 방법입니다. 슬라이드 노트에서 "Delete removes tuples/attributes; not an ERA query"라고 명시하듯이, 이는 데이터베이스의 ERA(Entity-Relationship-Attribute) 모델에서의 쿼리 개념보다는 실제 데이터 구조에서 요소를 물리적으로 제거하는 연산을 의미합니다.
*   **컬럼 삭제 (`.pop()`)**: 특정 컬럼을 DataFrame에서 제거하고, 제거된 컬럼의 데이터를 pandas Series 형태로 반환하는 메서드입니다. 원본 DataFrame을 직접 변경(in-place)합니다.
*   **행 삭제 (`.drop()`)**: 지정된 인덱스 레이블에 해당하는 행을 DataFrame에서 제거하는 메서드입니다. 기본적으로 새로운 DataFrame을 반환하며, 원본 DataFrame을 변경하려면 반환값을 재할당하거나 `inplace=True` 옵션을 사용해야 합니다.
*   **조건부 삭제**: 불리언 마스킹(Boolean Masking)을 사용하여 특정 조건을 만족하는 행들의 인덱스를 추출한 후, `.drop()` 메서드를 이용해 해당 행들을 삭제할 수 있습니다.

---

### **코드/수식 해설**

```python
# Column removal with return
# "Count" 컬럼을 DataFrame에서 제거하고, 제거된 데이터를 cnt 변수에 Series로 저장합니다.
# babynames DataFrame은 이제 "Count" 컬럼이 없습니다.
cnt = babynames.pop("Count") # returns Series

# 필요하다면, 제거했던 컬럼을 다시 추가할 수 있습니다.
babynames["Count"] = cnt # add back (if needed)

# Drop rows by labels
# babynames DataFrame의 인덱스 중 첫 두 개(인덱스 0과 1)를 선택하여 to_remove 변수에 저장합니다.
to_remove = babynames.index[:2]
# to_remove에 지정된 인덱스 레이블에 해당하는 행들을 DataFrame에서 삭제합니다.
# .drop()은 새로운 DataFrame을 반환하므로, 원본에 적용하려면 재할당해야 합니다.
babynames = babynames.drop(index=to_remove)

# Drop rows by condition
# "Year" 컬럼 값이 1920 미만이면서 동시에 "Count" 컬럼 값이 5 미만인 행들을 찾습니다.
# 이 조건에 맞는 행들에 대해 True를, 그렇지 않은 행들에 대해 False를 가지는 불리언 Series를 생성합니다.
old_rare = (babynames["Year"] < 1920) & (babynames["Count"] < 5)
# old_rare 불리언 Series를 사용하여 조건에 맞는 행들을 선택하고, 그 행들의 인덱스를 추출합니다.
# 추출된 인덱스에 해당하는 행들을 DataFrame에서 삭제합니다.
babynames = babynames.drop(index=babynames[old_rare].index)
```

---

### **구체적 예시**

*   **컬럼 제거**: 고객 데이터셋에서 `주민등록번호` 컬럼이 보안상 민감하여 분석 전에 일시적으로 제거하거나, 또는 모델 학습에 불필요하다고 판단되는 `고객ID` 컬럼을 제거할 때 `pop()`을 사용할 수 있습니다. `pop()`은 제거된 컬럼 데이터를 반환하므로, 나중에 다시 필요할 때를 대비해 저장해 둘 수 있습니다.
*   **특정 행 제거**: 데이터 클리닝 과정에서 특정 ID를 가진 불량 샘플 데이터(`index`로 특정)를 제거하거나, 초기 로드된 데이터의 상위 몇 개 행이 테스트 데이터로 사용되어 불필요하다고 판단될 때 `drop(index=...)`를 사용할 수 있습니다.
*   **조건부 행 제거**: "데이터분석 입문" 강의에서 흔히 다루는 이상치(Outlier) 제거에 활용될 수 있습니다. 예를 들어, 특정 변수에서 통계적으로 너무 높거나 낮은 값을 가지는 데이터 포인트들을 제거하여 분석의 정확도를 높일 때, 조건식을 활용한 행 삭제가 매우 유용합니다. 또는 오래된 로그 데이터를 특정 기준(`Year` < 1920)과 함께 사용 빈도가 매우 낮은(`Count` < 5) 경우에만 일괄 삭제하는 시나리오에 적용할 수 있습니다.

---

### **시험 포인트**

*   ⭐ `pandas.DataFrame.pop()` 메서드는 컬럼을 **제거함과 동시에 해당 컬럼의 데이터를 Series로 반환**하며, 원본 DataFrame을 직접 변경합니다.
*   ⭐ `pandas.DataFrame.drop()` 메서드는 기본적으로 **새로운 DataFrame을 반환**하며, `index` 인자를 통해 특정 행 레이블들을, `columns` 인자를 통해 특정 컬럼 레이블들을 삭제할 수 있습니다. 원본을 직접 변경하려면 `inplace=True` 옵션을 명시적으로 지정해야 합니다.
*   ⭐ 불리언 마스킹(`DataFrame[조건식]`)을 사용하여 **특정 조건을 만족하는 행들을 선택**하는 방법을 숙지하고, 이를 `drop()`과 연계하여 조건부 행 삭제를 수행하는 과정을 이해해야 합니다. 특히, 복합 조건을 사용할 때는 각 조건식을 괄호로 묶고 `&`(AND) 또는 `|`(OR) 연산자를 사용해야 합니다.
*   제거할 컬럼을 아는 경우 `pop()` 또는 `drop(columns=[...])`를 사용할 수 있고, 제거할 행의 인덱스 레이블을 아는 경우 `drop(index=[...])`를 사용합니다.

---

## Slide 9

이 슬라이드는 데이터프레임에서 특정 조건을 만족하는 행(row)을 선택하는 'Selection' 연산에 대해 설명합니다. 관계형 대수의 개념과 pandas를 사용한 구현 방법을 함께 다룹니다.

---

### **핵심 개념**

*   **Selection (선택)**: 관계형 대수(Relational Algebra)의 기본 연산 중 하나로, 주어진 조건(predicate)을 만족하는 튜플(행)들만을 추출하여 새로운 관계(테이블 또는 데이터프레임)를 생성하는 연산입니다.
*   **스키마 보존(Schema Preserved)**: Selection 연산은 원본 데이터프레임의 열(column) 구조, 즉 스키마를 그대로 유지하며 행만 필터링합니다.

### **코드/수식 해설**

*   **관계형 대수 표기 (Formal Definition)**
    $$
    \sigma_{\theta}(R) = \{ t \in R \mid \theta(t) \}
    $$
    *   $\sigma$: Selection 연산을 나타내는 기호입니다.
    *   $R$: 원본 관계(Relation) 또는 데이터프레임을 의미합니다.
    *   $\theta$: 선택 조건(Predicate)을 나타냅니다. 예를 들어, `Year=1910 AND Sex startsWith 'F'`와 같은 조건식입니다.
    *   $t$: 관계 $R$의 각 튜플(행)을 의미합니다.
    *   위 수식은 "관계 $R$에 속하는 모든 튜플 $t$ 중에서, 조건 $\theta(t)$를 만족하는 $t$들의 집합"을 의미합니다.

*   **ERA (Query) 예시**
    $$
    \sigma_{\text{Year}=1910 \land \text{Sex startsWith 'F'}}(\text{babynames})
    $$
    *   `babynames`라는 관계(데이터프레임)에서 `Year` 컬럼의 값이 1910이고($\text{Year}=1910$), `Sex` 컬럼의 값이 'F'로 시작하는($\text{Sex startsWith 'F'}$) 모든 행을 선택하라는 의미입니다.
    *   $\land$ (논리곱, AND)는 두 조건이 모두 참일 때만 해당 행을 선택합니다.

*   **pandas 코드**

    ```python
    mask = (babynames["Year"]==1910) & (babynames["Sex"].str.
            startswith("F"))
    sel = babynames.loc[mask]
    ```
    1.  `mask = (babynames["Year"]==1910) & (babynames["Sex"].str.startswith("F"))`:
        *   `babynames["Year"]==1910`: `babynames` 데이터프레임의 'Year' 컬럼에서 값이 1910인 행에 대해 `True`, 아닌 행에 대해 `False`를 가지는 Boolean Series를 생성합니다.
        *   `babynames["Sex"].str.startswith("F")`: 'Sex' 컬럼에 `.str` accessor를 사용하여 문자열 메서드 `startswith("F")`를 적용합니다. 각 문자열이 'F'로 시작하는지 검사하여 `True`/`False` 값을 가지는 Boolean Series를 생성합니다.
        *   `&`: 두 Boolean Series를 논리곱(AND) 연산합니다. 이 연산 결과로 두 조건이 모두 `True`인 경우에만 `True` 값을 가지는 최종 `mask` Boolean Series가 생성됩니다.
    2.  `sel = babynames.loc[mask]`:
        *   `babynames.loc[mask]`: `mask` Series가 `True`인 인덱스(행)들만을 `babynames` 데이터프레임에서 선택하여 `sel`이라는 새로운 데이터프레임에 할당합니다. `.loc` 인덱서는 레이블 기반 인덱싱을 수행합니다.

### **구체적 예시**

`babynames`라는 데이터프레임이 다음과 같다고 가정해봅시다.

| Year | Name    | Sex | Count |
| :--- | :------ | :-- | :---- |
| 1910 | Mary    | F   | 60000 |
| 1910 | John    | M   | 40000 |
| 1910 | Elizabeth | F | 30000 |
| 1911 | William | M   | 50000 |
| 1911 | Florence | F  | 20000 |

위 `pandas` 코드를 실행하면 `mask` Series는 다음과 같이 생성됩니다.

*   `babynames["Year"]==1910`: `[True, True, True, False, False]`
*   `babynames["Sex"].str.startswith("F")`: `[True, False, True, False, True]`
*   최종 `mask` (두 Series를 `&` 연산): `[True, False, True, False, False]`

이 `mask`를 `babynames.loc[mask]`에 적용하면, `sel` 데이터프레임은 다음과 같이 조건('Year'이 1910이고 'Sex'가 'F'로 시작)을 만족하는 행들만 포함하게 됩니다.

| Year | Name      | Sex | Count |
| :--- | :-------- | :-- | :---- |
| 1910 | Mary      | F   | 60000 |
| 1910 | Elizabeth | F   | 30000 |

### **시험 포인트**

*   ⭐ **Selection 연산의 기본 개념과 목적**: 특정 조건을 만족하는 행을 추출하는 데이터 필터링 연산임을 정확히 이해해야 합니다.
*   ⭐ **관계형 대수 표기법($\sigma_{\theta}(R)$)의 각 구성 요소 의미**: $\sigma$, $\theta$, $R$, $t$가 무엇을 나타내는지 명확히 설명할 수 있어야 합니다.
*   ⭐ **pandas에서의 Selection 구현 방법**: `df.loc[boolean_mask]`를 이용한 불리언 마스킹(Boolean Masking)의 원리와 사용법을 숙지해야 합니다. `df.query()` 방법도 있음을 기억하세요.
*   ⭐ **복수 조건 처리**: `&` (AND), `|` (OR), `~` (NOT)와 같은 논리 연산자를 사용하여 여러 조건을 조합하는 방법을 알아야 합니다. 특히 `&`와 `|` 연산 시 각 조건식을 괄호 `()`로 묶어 우선순위를 명확히 하는 것이 중요합니다.
*   ⭐ **문자열 데이터 필터링**: `.str` accessor를 활용한 `startswith()`, `endswith()`, `contains()` 등 문자열 메서드를 이용한 조건 설정 방법을 이해해야 합니다.

---

## Slide 10

**핵심 개념**
*   **일반화된 투영 (Generalized Projection)**: 데이터베이스 및 데이터프레임 연산에서 기존 속성(컬럼)에 함수나 표현식을 적용하여 새로운 속성을 생성하고, 원하는 속성들만 선택하여 새로운 테이블(데이터프레임)을 구성하는 연산입니다. 단순한 컬럼 선택을 넘어, 컬럼의 값을 변형하거나 여러 컬럼의 조합으로 새 컬럼을 만들 수 있습니다. 집계(aggregation) 없이 각 로우(row)별로 연산이 수행됩니다.

**코드/수식 해설**

*   **수식 (ERA Query)**:
    $$ \pi_{\text{Year, Name, SUBSTR(Name,1,1) } \rightarrow \text{ first\_letter, LEN(Name) } \rightarrow \text{ name\_len}}(\text{babynames}) $$
    이 수식은 `babynames`라는 릴레이션(테이블 또는 데이터프레임)에 대해 일반화된 투영 연산을 수행합니다.
    *   `$\pi$`: 투영(Projection) 연산을 의미합니다.
    *   `Year`, `Name`: 기존의 `Year`와 `Name` 속성은 그대로 유지됩니다.
    *   `SUBSTR(Name,1,1) $\rightarrow$ first_letter`: `Name` 속성의 첫 글자를 추출하여 `first_letter`라는 새로운 속성을 생성합니다.
    *   `LEN(Name) $\rightarrow$ name_len`: `Name` 속성의 길이를 계산하여 `name_len`이라는 새로운 속성을 생성합니다.
    *   최종 결과는 `Year`, `Name`, `first_letter`, `name_len` 네 개의 속성으로 구성된 새로운 릴레이션입니다.

*   **코드 (Pandas 구현)**:
    ```python
    proj_easy = (babynames
                    .assign(first_letter=lambda d: d["Name"].str[0],
                            name_len=lambda d: d["Name"].str.len())
                    [["Year", "Name", "first_letter", "name_len"]])
    ```
    이 코드는 `babynames` 데이터프레임에 대해 위 ERA Query와 동일한 일반화된 투영 연산을 pandas로 구현한 것입니다.
    *   `babynames`: 입력 데이터프레임입니다.
    *   `.assign(...)`: 데이터프레임에 새로운 컬럼을 추가하는 메서드입니다.
        *   `first_letter=lambda d: d["Name"].str[0]`: `first_letter`라는 새 컬럼을 생성합니다. 각 로우의 `Name` 컬럼 값(`d["Name"]`)에 `.str[0]` (pandas Series의 문자열 메서드)를 적용하여 첫 글자를 추출합니다.
        *   `name_len=lambda d: d["Name"].str.len()`: `name_len`이라는 새 컬럼을 생성합니다. 각 로우의 `Name` 컬럼 값에 `.str.len()`를 적용하여 문자열 길이를 계산합니다.
    *   `[["Year", "Name", "first_letter", "name_len"]]`: `.assign()`으로 새로운 컬럼이 추가된 데이터프레임에서 최종적으로 원하는 컬럼들(`Year`, `Name`, `first_letter`, `name_len`)만 선택하고, 이중 대괄호를 사용하여 컬럼 순서를 지정합니다.

**구체적 예시**
`babynames` 데이터프레임이 다음과 같다고 가정해 봅시다:

| Year | Name    | Count |
| :--- | :------ | :---- |
| 2020 | Alice   | 100   |
| 2020 | Bob     | 90    |
| 2021 | Charlie | 110   |

위 pandas 코드를 실행하면 `proj_easy` 데이터프레임은 다음과 같이 생성됩니다:

| Year | Name    | first\_letter | name\_len |
| :--- | :------ | :------------ | :-------- |
| 2020 | Alice   | A             | 5         |
| 2020 | Bob     | B             | 3         |
| 2021 | Charlie | C             | 7         |

이 예시를 통해 `Name` 컬럼으로부터 `first_letter`와 `name_len`이라는 새로운 파생 컬럼이 성공적으로 생성되고, 원하는 컬럼만 선택하여 새로운 데이터프레임이 구성된 것을 확인할 수 있습니다.

**시험 포인트**
*   ⭐ **일반화된 투영의 개념과 단순 투영(컬럼 선택)과의 차이점을 명확히 이해해야 합니다.** 일반화된 투영은 기존 컬럼을 기반으로 *새로운 컬럼을 생성*할 수 있다는 점에서 차이가 있습니다.
*   ⭐ **ERA(관계 대수) 표현식과 pandas 코드를 매칭하여 해석할 수 있어야 합니다.** 특히 `assign()` 메서드를 사용하여 새로운 컬럼을 만드는 방법과 `lambda` 함수를 활용한 표현식 작성법, 그리고 최종 컬럼 선택(`[[...]]`)의 역할을 알아야 합니다.
*   ⭐ **`pandas.Series.str` accessor의 활용법 (예: `.str[0]`, `.str.len()`)을 익혀두어야 합니다.** 이는 문자열 데이터에 대한 일반화된 투영 연산에서 매우 유용하게 사용됩니다.
*   ⭐ **`.assign()` 메서드는 원본 데이터프레임을 변경하지 않고 새로운 데이터프레임을 반환한다는 특징을 기억해야 합니다.** (immutable operation)

---

## Slide 11

**핵심 개념**
데이터프레임(또는 관계형 데이터 모델의 릴레이션)에서 특정 **속성(attribute) 또는 컬럼(column)의 이름을 변경**하는 연산입니다. 이 연산은 컬럼의 이름만 바꾸고, 해당 컬럼에 저장된 실제 데이터(값)는 전혀 변경되지 않습니다. 이는 데이터의 가독성을 높이거나, 다른 데이터셋과의 병합(merge) 또는 특정 라이브러리/함수의 요구사항에 맞추기 위해 자주 사용됩니다.

**코드/수식 해설**

*   **수식**:
    관계형 대수(Relational Algebra)에서 속성 이름 변경은 그리스 문자 람다(rho, $\rho$)를 사용하여 다음과 같이 표현됩니다.
    $$
    \rho_{A \to A'}(R)
    $$
    여기서,
    *   $R$: 원본 릴레이션(데이터프레임)
    *   $A$: 원본 릴레이션 $R$의 속성(컬럼) 이름
    *   $A'$: $A$ 속성을 변경하고자 하는 새로운 이름
    슬라이드의 예시에서는 `babynames` 릴레이션의 `Count` 속성을 `freq`로 변경하는 것을 나타냅니다.
    $$
    \rho_{Count \to freq}(babynames)
    $$

*   **코드**:
    pandas 라이브러리에서는 `DataFrame.rename()` 메서드를 사용하여 컬럼 이름을 변경할 수 있습니다.
    ```python
    df.rename(columns={"old_column_name": "new_column_name"})
    ```
    *   `columns`: 컬럼 이름을 변경할 때 사용하는 키워드 인자입니다. 딕셔너리 형태로 `{"원본 컬럼 이름": "새로운 컬럼 이름"}`을 전달합니다. 여러 컬럼을 동시에 변경할 수도 있습니다 (예: `{"col_a": "new_col_a", "col_b": "new_col_b"}`).
    *   `inplace=True` 인자를 사용하면 원본 데이터프레임을 직접 수정할 수 있지만, 일반적으로는 새로운 데이터프레임을 반환받아 사용하는 것이 권장됩니다. (예: `df = df.rename(...)` 또는 `new_df = df.rename(...)`)

    슬라이드의 예시 코드:
    ```python
    ren = babynames.rename(columns={"Count": "freq"})
    ```
    이 코드는 `babynames` 데이터프레임의 `Count`라는 컬럼 이름을 `freq`로 변경한 새로운 데이터프레임을 생성하여 `ren` 변수에 할당합니다. `babynames` 자체는 변경되지 않습니다.

**구체적 예시**

아기 이름 데이터셋이 있다고 가정해봅시다. 이 데이터셋에는 'Name', 'Year', 'Count' 컬럼이 있습니다. 'Count'는 해당 연도에 태어난 아기들의 이름 빈도를 나타냅니다. 이 'Count' 컬럼의 의미를 더 명확하게 'Frequency' 또는 'freq'로 변경하고 싶습니다.

```python
import pandas as pd

# 예시 데이터프레임 생성
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
    'Year': [2020, 2020, 2021, 2021],
    'Count': [150, 120, 100, 180]
}
babynames = pd.DataFrame(data)

print("--- 원본 babynames 데이터프레임 ---")
print(babynames)
print("\n원본 컬럼:", babynames.columns.tolist())

# 'Count' 컬럼 이름을 'freq'로 변경
renamed_babynames = babynames.rename(columns={"Count": "freq"})

print("\n--- 이름 변경 후 renamed_babynames 데이터프레임 ---")
print(renamed_babynames)
print("\n변경된 컬럼:", renamed_babynames.columns.tolist())

print("\n--- 원본 babynames 데이터프레임은 변경되지 않음 ---")
print(babynames.columns.tolist())
```

**실행 결과:**
```
--- 원본 babynames 데이터프레임 ---
      Name  Year  Count
0    Alice  2020    150
1      Bob  2020    120
2  Charlie  2021    100
3    Alice  2021    180

원본 컬럼: ['Name', 'Year', 'Count']

--- 이름 변경 후 renamed_babynames 데이터프레임 ---
      Name  Year  freq
0    Alice  2020   150
1      Bob  2020   120
2  Charlie  2021   100
3    Alice  2021   180

변경된 컬럼: ['Name', 'Year', 'freq']

--- 원본 babynames 데이터프레임은 변경되지 않음 ---
['Name', 'Year', 'Count']
```

**시험 포인트**

*   ⭐ **컬럼 이름 변경의 목적과 효과**: 왜 컬럼 이름을 변경하는지 (가독성, 일관성) 그리고 이름만 변경되고 데이터 값은 유지된다는 점을 이해하고 설명할 수 있어야 합니다.
*   ⭐ **pandas `DataFrame.rename()` 메서드 사용법**: `columns` 인자에 딕셔너리를 사용하여 `{"기존 이름": "새로운 이름"}` 형태로 전달하는 방법을 정확히 알고 있어야 합니다.
*   **`inplace` 인자의 이해**: `inplace=True` 사용 시 원본 데이터프레임이 직접 수정되며, 기본적으로는 새로운 데이터프레임이 반환된다는 점을 알아두세요. (⭐ 시험에서는 이 두 방식의 차이점을 묻는 문제가 자주 출제됩니다.)
*   **관계형 대수 표기**: $\rho_{A \to A'}(R)$ 와 같은 관계형 대수 표기가 컬럼 이름 변경 연산을 의미한다는 것을 알아두세요.

---

## Slide 12

### **핵심 개념**:
*   **중복 제거 (Duplicate Elimination)**: 데이터셋 내에서 완전히 동일한 레코드(튜플)를 식별하고 제거하여 유일한(unique) 데이터만 남기는 과정입니다. 이는 데이터의 정확성과 일관성을 유지하고, 불필요한 연산 및 저장 공간 낭비를 줄이며, 통계적 분석 결과의 신뢰도를 높이는 데 필수적인 데이터 전처리 단계입니다. 관계형 데이터베이스 이론에서는 '집합 의미론(set semantics)'을 따르므로, 릴레이션(테이블)은 본질적으로 중복 튜플을 허용하지 않습니다.
*   **관계 대수 (Relational Algebra)**: 데이터베이스 시스템에서 데이터를 질의하고 조작하는 데 사용되는 공식적인 연산 집합입니다. 슬라이드에서는 특정 컬럼들을 선택(프로젝션)한 후 중복을 제거하는 연산 흐름을 관계 대수 표현식으로 나타냈습니다.

### **코드/수식 해설**:
*   **관계 대수 수식**:
    $$ \delta(\pi_{\text{Year, Name}}(\text{babynames})) $$
    *   $\pi_{\text{Year, Name}}(\text{babynames})$: `babynames`라는 릴레이션(테이블)에서 `Year`와 `Name` 속성(컬럼)만을 선택(프로젝션)하는 연산입니다. 이 연산의 결과는 `(Year, Name)` 쌍으로 이루어진 새로운 릴레이션이 됩니다. 이 단계에서는 동일한 `(Year, Name)` 쌍이 여러 번 나타날 수 있습니다.
    *   $\delta(...)$: 앞서 프로젝션된 결과 릴레이션에 대해 중복 제거 연산 $\delta$를 적용합니다. 이 연산은 `(Year, Name)` 쌍 중에서 내용이 완전히 동일한 튜플들을 모두 제거하고, 각 유일한 튜플만 하나씩 남깁니다.

*   **pandas 코드**:
    ```python
    unique_year_name = babynames[["Year", "Name"]].drop_duplicates()
    ```
    *   `babynames[["Year", "Name"]]`: `babynames`라는 pandas DataFrame에서 `Year`와 `Name`이라는 두 개의 컬럼만을 선택하여 새로운 DataFrame을 생성합니다. 이는 관계 대수의 프로젝션($\pi$) 연산에 해당합니다.
    *   `.drop_duplicates()`: 새로 생성된 `Year`와 `Name` 컬럼으로 구성된 DataFrame에 대해 중복되는 행(row)을 제거합니다. 이 메서드는 기본적으로 모든 컬럼의 값이 동일한 행들을 중복으로 간주하여 하나만 남깁니다. 여기서 `babynames[["Year", "Name"]]`의 결과 DataFrame에는 `Year`와 `Name` 두 컬럼만 있으므로, `(Year, Name)` 쌍이 완전히 동일한 행들을 제거하게 됩니다. 이는 관계 대수의 중복 제거($\delta$) 연산에 해당합니다.

### **구체적 예시**:
`babynames` DataFrame이 다음과 같다고 가정해 봅시다.

| Year | Name | Gender | Count |
|:----:|:----:|:------:|:-----:|
| 2000 | Emma | F      | 15000 |
| 2001 | Liam | M      | 18000 |
| 2000 | Emma | F      | 14900 |
| 2002 | Olivia | F      | 17000 |
| 2001 | Liam | M      | 18200 |
| 2000 | Noah | M      | 16000 |

위 데이터프레임에 다음 코드를 적용하면:
```python
unique_year_name = babynames[["Year", "Name"]].drop_duplicates()
```
1.  `babynames[["Year", "Name"]]` 연산을 먼저 수행하면 다음과 같은 DataFrame이 생성됩니다.
    | Year | Name |
    |:----:|:----:|
    | 2000 | Emma |
    | 2001 | Liam |
    | 2000 | Emma |
    | 2002 | Olivia |
    | 2001 | Liam |
    | 2000 | Noah |

2.  이 중간 결과에 `.drop_duplicates()`를 적용합니다. 이 메서드는 `(Year, Name)` 쌍이 완전히 동일한 행들을 찾아 제거합니다. 여기서는 `(2000, Emma)` 쌍과 `(2001, Liam)` 쌍이 각각 두 번씩 나타나므로, 중복된 하나씩을 제거합니다.

    최종 `unique_year_name` DataFrame의 내용은 다음과 같습니다:
    | Year | Name |
    |:----:|:----:|
    | 2000 | Emma |
    | 2001 | Liam |
    | 2002 | Olivia |
    | 2000 | Noah |

이 결과는 각 `(Year, Name)` 조합이 유일하게 한 번씩만 나타나는 것을 보장합니다.

### **시험 포인트**:
*   ⭐ **중복 제거의 필요성 및 효과**: 데이터 분석 및 머신러닝 모델 학습 과정에서 중복 데이터가 미치는 부정적인 영향(편향된 결과, 과적합, 자원 낭비 등)과 중복 제거를 통해 얻을 수 있는 이점(데이터 품질 향상, 분석 효율 증대 등)을 설명할 수 있어야 합니다.
*   ⭐ **관계 대수와 pandas 연산 매핑**: $\delta$ (중복 제거) 연산이 pandas의 `.drop_duplicates()` 메서드에, $\pi$ (프로젝션) 연산이 `df[[]]`를 이용한 컬럼 선택에 대응된다는 것을 정확히 이해하고 코드를 작성하거나 해석할 수 있어야 합니다.
*   ⭐ **`df.drop_duplicates()` 메서드의 활용**:
    *   기본 동작: 모든 컬럼을 기준으로 중복을 판단하여 제거합니다.
    *   `subset` 인자: 특정 컬럼(들)을 기준으로만 중복을 판단하고 싶을 때 사용합니다. 예: `df.drop_duplicates(subset=['컬럼1', '컬럼2'])`. (슬라이드 예시는 먼저 컬럼을 선택하여 `subset` 인자 없이 사용하는 것과 동일한 효과를 냅니다.)
    *   `keep` 인자: 중복된 값들 중 어떤 것을 남길지 지정합니다 (`'first'`, `'last'`, `False` 등). 기본값은 `'first'`입니다.
*   **`Series.unique()`와 `DataFrame.drop_duplicates()`의 차이**: 특정 Series(단일 컬럼)의 유일한 값들을 알고 싶을 때는 `.unique()`를 사용하고, DataFrame에서 행 또는 여러 컬럼 조합의 유일성을 확보할 때는 `.drop_duplicates()`를 사용한다는 차이점을 명확히 이해해야 합니다.
*   **데이터 처리 파이프라인**: 여러 pandas 연산(컬럼 선택, 중복 제거 등)을 순차적으로 연결하여 데이터를 가공하는 방식을 이해하고 적용할 수 있어야 합니다.

---

## Slide 13

**핵심 개념**:
이 슬라이드는 `pandas` 데이터프레임에서 여러 개의 컬럼을 기준으로 데이터를 정렬하는 방법을 설명합니다. 특히, 각 정렬 기준 컬럼에 대해 오름차순(ascending) 또는 내림차순(descending)을 다르게 지정하여 복합적인 정렬을 수행하는 것이 핵심입니다. 이는 관계형 대수(Relational Algebra, RA)의 확장된 정렬 연산자($\tau$) 표기를 통해 개념적으로 설명되며, `pandas` 라이브러리의 `sort_values()` 메서드를 사용하여 실제 구현됩니다.

**코드/수식 해설**:
*   **관계형 대수 (Relational Algebra) 수식**:
    정렬 연산은 다음과 같이 표현됩니다:
    $$\tau_{A_1 \uparrow, A_2 \downarrow}(R)$$
    이는 릴레이션 $R$을 먼저 속성 $A_1$을 기준으로 오름차순($\uparrow$)으로 정렬하고, 그 다음 $A_1$ 값이 동일한 튜플들 내에서 속성 $A_2$를 기준으로 내림차순($\downarrow$)으로 정렬하라는 의미입니다. 슬라이드의 예시에서는 $R$이 `babynames` 데이터프레임이며, $A_1$은 `Year`, $A_2$는 `Count`입니다.

*   **Pandas 코드**:
    ```python
    sorted_df = babynames.sort_values(["Year", "Count"], ascending=[True, False])
    ```
    이 코드는 `babynames` 데이터프레임을 정렬하는 `pandas`의 `sort_values()` 메서드 사용법을 보여줍니다.
    *   첫 번째 인자인 `["Year", "Count"]`는 정렬에 사용할 컬럼 이름들의 리스트입니다. 리스트에 명시된 컬럼의 순서가 정렬의 우선순위를 결정합니다. 즉, `Year`가 1차 정렬 기준이 되고, `Count`가 2차 정렬 기준이 됩니다.
    *   두 번째 인자인 `ascending=[True, False]`는 `by` 인자에 명시된 각 컬럼에 대한 정렬 방식을 지정합니다. 이 리스트의 `True`/`False` 값은 `by` 인자의 컬럼 순서와 정확히 일치해야 합니다. `Year`에 해당하는 `True`는 오름차순(ascending)을, `Count`에 해당하는 `False`는 내림차순(descending)을 의미합니다.
    *   `sort_values()` 메서드는 정렬된 새로운 데이터프레임을 반환하며, 원본 `babynames` 데이터프레임은 변경되지 않습니다. 반환된 데이터프레임은 `sorted_df` 변수에 저장됩니다.

**구체적 예시**:
다음과 같은 `babynames` 데이터프레임이 있다고 가정해 봅시다:

| Year | Name  | Count |
| :--- | :---- | :---- |
| 2000 | Alice | 100   |
| 2001 | Bob   | 120   |
| 2000 | Carol | 150   |
| 2001 | Alice | 110   |
| 2000 | David | 90    |
| 2002 | Eve   | 80    |

위의 `pandas` 코드를 적용하면 `Year`는 오름차순(`True`), `Count`는 내림차순(`False`)으로 정렬됩니다.

1.  **1차 정렬 (Year 오름차순)**: 먼저 `Year` 컬럼을 기준으로 데이터를 오름차순으로 정렬합니다.

    | Year | Name  | Count |
    | :--- | :---- | :---- |
    | 2000 | Alice | 100   |
    | 2000 | Carol | 150   |
    | 2000 | David | 90    |
    | 2001 | Bob   | 120   |
    | 2001 | Alice | 110   |
    | 2002 | Eve   | 80    |

2.  **2차 정렬 (Year가 같은 경우 Count 내림차순)**: `Year` 값이 동일한 행들 내에서 `Count` 컬럼을 내림차순으로 다시 정렬합니다. 예를 들어, `Year`가 2000인 세 개의 행 (`Alice`, `Carol`, `David`) 중에서 `Count` 값을 기준으로 (150, 100, 90 순으로) 내림차순 정렬됩니다.

    | Year | Name  | Count |
    | :--- | :---- | :---- |
    | 2000 | Carol | 150   |
    | 2000 | Alice | 100   |
    | 2000 | David | 90    |
    | 2001 | Bob   | 120   |
    | 2001 | Alice | 110   |
    | 2002 | Eve   | 80    |

이것이 최종 `sorted_df`의 내용이 됩니다.

**시험 포인트**:
*   ⭐ `pandas.DataFrame.sort_values()` 메서드의 구문과 각 인자(`by`, `ascending`)의 역할을 정확히 이해하고 있어야 합니다.
*   ⭐ 여러 컬럼으로 정렬할 때, `by` 인자에 컬럼 리스트를, `ascending` 인자에 각 컬럼에 해당하는 `True`/`False` 부울 값 리스트를 전달해야 하며, 이 두 리스트의 순서가 서로 대응되어야 한다는 점이 중요합니다.
*   ⭐ 관계형 대수의 정렬 연산($\tau$) 표기법($\uparrow$ 오름차순, $\downarrow$ 내림차순)과 그 의미를 해석할 수 있어야 합니다.
*   ⭐ `sort_values()` 메서드는 기본적으로 원본 DataFrame을 변경하지 않고(immutable) 정렬된 새로운 DataFrame을 반환한다는 점을 기억하세요. (원본 변경을 원한다면 `inplace=True` 옵션을 사용할 수 있지만, 일반적으로는 새로운 DataFrame을 사용하는 것이 권장됩니다.)

---

## Slide 14

---
### **핵심 개념**

관계형 데이터베이스(RDB) 또는 데이터프레임에서 두 집합 간의 관계 연산을 수행하는 세 가지 주요 개념은 **합집합(Union)**, **교집합(Intersection)**, **차집합(Difference)**입니다. 이 연산들은 기본적으로 **집합론(Set Theory)**의 개념을 따르며, 중복을 허용하지 않는 **관계(Relation)** 또는 **데이터프레임(DataFrame)**을 대상으로 합니다.

1.  **합집합 ($R \cup S$)**: 두 관계 $R$과 $S$에 속하는 모든 튜플(행)을 모은 집합입니다. 이때 중복되는 튜플은 한 번만 포함됩니다.
2.  **교집합 ($R \cap S$)**: 두 관계 $R$과 $S$ 모두에 공통적으로 속하는 튜플들을 모은 집합입니다.
3.  **차집합 ($R - S$)**: 관계 $R$에는 속하지만 관계 $S$에는 속하지 않는 튜플들을 모은 집합입니다.

이 연산들을 수행하기 위해서는 두 관계가 **합집합-호환(Union-compatible)**이어야 합니다. 이는 두 관계가 동일한 스키마(즉, 같은 수의 속성(컬럼)을 가지고 각 속성의 도메인(데이터 타입)이 같아야 함)를 가져야 한다는 의미입니다. pandas에서는 `drop_duplicates()`를 사용하여 'bag'(중복 허용) 개념의 결과에서 'set'(중복 제거) 개념의 결과를 얻을 수 있습니다.

---
### **코드/수식 해설**

**관계 대수 표기법:**

슬라이드에서는 `babynames` 데이터로부터 `Year`, `Name` 속성을 투영($\pi$)하여 얻은 관계와 주어진 집합 $S$ 간의 연산을 보여줍니다.

*   합집합: $\pi_{\text{Year, Name}}(\text{babynames}) \cup S$
*   교집합: $\pi_{\text{Year, Name}}(\text{babynames}) \cap S$
*   차집합: $\pi_{\text{Year, Name}}(\text{babynames}) - S$

**Python (pandas) 코드 해설:**

먼저 연산에 사용할 두 데이터프레임 `R`과 `S`를 준비합니다.

```python
# R: babynames 데이터에서 'Year'와 'Name' 컬럼을 추출하여 중복을 제거한 관계
# drop_duplicates()를 사용하여 R이 집합(set) 의미를 갖도록 함
R = babynames[["Year", "Name"]].drop_duplicates()

# S: Year와 Name을 가진 DataFrame으로, 연산의 대상이 될 다른 집합
S = pd.DataFrame({"Year": [1910, 1910], "Name": ["Mary", "Alice"]})
```

1.  **합집합 (UNION)**

    ```python
    # UNION (중복 제거를 통한 집합 합집합)
    # pd.concat을 사용하여 R과 S를 세로로 결합하고, ignore_index=True로 인덱스를 재설정
    # 최종적으로 .drop_duplicates()를 적용하여 중복 행을 제거함으로써 집합 합집합의 의미 구현
    union_set = pd.concat([R, S], ignore_index=True).drop_duplicates()
    ```
    *   `pd.concat([R, S], ignore_index=True)`: 두 DataFrame `R`과 `S`를 수직으로 결합합니다. 이때 `ignore_index=True`는 결합된 DataFrame의 인덱스를 0부터 새로 부여하여 인덱스 충돌을 방지합니다. 이 단계까지는 중복이 허용된 'bag' 형태입니다.
    *   `.drop_duplicates()`: 결합된 결과에서 중복되는 모든 행을 제거하여 'set' 의미의 합집합을 완성합니다.

2.  **교집합 (INTERSECTION)**

    ```python
    # INTERSECTION (집합 교집합)
    # inner merge (내부 조인)를 사용하여 R과 S의 공통 컬럼(여기서는 'Year', 'Name')을 기반으로
    # 양쪽에 모두 존재하는 튜플(행)만 유지하여 교집합을 계산
    inter = R.merge(S, how="inner")
    ```
    *   `R.merge(S, how="inner")`: `R`과 `S` 데이터프레임 간에 내부 조인(inner join)을 수행합니다. `how="inner"`는 양쪽 DataFrame에 모두 일치하는 키(여기서는 공통 컬럼인 'Year', 'Name' 쌍)를 가진 행만 결과에 포함시킵니다. 이는 집합의 교집합과 동일한 결과를 가져옵니다.

3.  **차집합 (DIFFERENCE $R - S$)**

    ```python
    # DIFFERENCE (R - S)
    # left merge (왼쪽 조인)를 사용하고 indicator=True로 병합된 행의 출처를 표시
    # 'left_only'로 표시된 행만 필터링하여 R에는 존재하지만 S에는 없는 행을 추출
    # 마지막으로 _merge 헬퍼 컬럼을 제거
    diff = R.merge(S, how="left", indicator=True) \
           .query("_merge == 'left_only'") \
           .drop(columns=["_merge"])
    ```
    *   `R.merge(S, how="left", indicator=True)`: `R`과 `S` 간에 왼쪽 조인(left join)을 수행합니다. `R`의 모든 행을 유지하고 `S`에서 일치하는 행을 추가합니다. 만약 `S`에 일치하는 행이 없으면 `NaN`으로 채워집니다. `indicator=True`는 병합된 각 행이 어디에서 왔는지(`left_only`, `right_only`, `both`)를 나타내는 `_merge`라는 특수 컬럼을 추가합니다.
    *   `.query("_merge == 'left_only'")`: `_merge` 컬럼의 값이 `'left_only'`인 행만 필터링합니다. 이는 `R`에는 존재하지만 `S`에는 존재하지 않는 행들을 의미하므로, 정확히 $R - S$의 결과를 얻습니다.
    *   `.drop(columns=["_merge"])`: 연산에 사용된 `_merge` 헬퍼 컬럼을 최종 결과에서 제거합니다.

---
### **구체적 예시**

`babynames` 데이터프레임에서 `R`이 1910년에 태어난 아이들의 이름과 연도 목록(중복 제거)이라고 가정해 봅시다.
예를 들어 `R`이 다음과 같다고 합시다:
```
R = pd.DataFrame({'Year': [1910, 1910, 1910], 'Name': ['John', 'Mary', 'Peter']})
```
`S`는 슬라이드에 주어진 대로 다음과 같습니다:
```
S = pd.DataFrame({'Year': [1910, 1910], 'Name': ['Mary', 'Alice']})
```

1.  **합집합 ($R \cup S$)**
    `R`과 `S`의 모든 행을 합치고 중복을 제거합니다.
    결과: `(1910, John)`, `(1910, Mary)`, `(1910, Peter)`, `(1910, Alice)`
    (1910, Mary)는 양쪽에 있으므로 한 번만 포함됩니다.

2.  **교집합 ($R \cap S$)**
    `R`과 `S`에 공통으로 존재하는 행을 찾습니다.
    결과: `(1910, Mary)`
    `'Mary'`는 1910년에 `R`과 `S` 양쪽에 모두 존재합니다.

3.  **차집합 ($R - S$)**
    `R`에는 있지만 `S`에는 없는 행을 찾습니다.
    결과: `(1910, John)`, `(1910, Peter)`
    `'John'`과 `'Peter'`는 1910년에 `R`에만 존재하고 `S`에는 없습니다.

---
### **시험 포인트**

*   **⭐ 합집합, 교집합, 차집합의 개념과 관계 대수 표기법을 정확히 이해해야 합니다.** 특히 두 관계가 합집합-호환(Union-compatible)해야 한다는 조건은 기본입니다.
*   **⭐ pandas에서 `pd.concat`과 `merge` 메서드를 사용하여 이러한 집합 연산을 구현하는 방법을 반드시 숙지해야 합니다.** 각 연산에 어떤 `how` 파라미터가 사용되는지 (예: 합집합은 `concat` 후 `drop_duplicates`, 교집합은 `inner` merge, 차집합은 `left` merge 후 `indicator=True`와 `query` 활용)를 정확히 알아야 합니다.
*   **⭐ `drop_duplicates()`의 역할**: pandas는 기본적으로 'bag' 의미를 가지므로, 'set' 의미의 연산을 위해서는 `drop_duplicates()`를 사용해야 함을 기억해야 합니다. 합집합에서 특히 중요하게 사용됩니다.
*   **⭐ `indicator=True` 파라미터의 기능**: `merge` 시 `_merge` 컬럼을 생성하여 병합된 행의 출처를 파악할 수 있게 해주는 유용한 기능임을 알아두세요. 특히 차집합 구현에 핵심적으로 활용됩니다.
*   주어진 코드를 보고 어떤 집합 연산을 수행하는지 설명하거나, 특정 집합 연산을 수행하는 코드를 작성하는 문제가 출제될 수 있습니다.

---

## Slide 15

---
### 핵심 개념

*   **카티션 곱 (Cartesian Product, $R \times S$)**: 두 릴레이션(테이블) R과 S의 모든 가능한 튜플(행) 조합을 생성합니다. R의 각 튜플과 S의 각 튜플을 결합하여 새로운 튜플을 만듭니다. 결과 릴레이션의 행 수는 R의 행 수와 S의 행 수를 곱한 값과 같습니다.
*   **세타 조인 (Theta Join, $R \bowtie_\theta S$)**: 카티션 곱의 결과에 특정 조건($\theta$)을 적용하여 필터링하는 조인입니다. $\theta$는 일반적인 비교 연산자(>, <, =, >=, <=, !=)를 포함하는 조건식입니다.
*   **동등 조인 (Equi-Join, $R \bowtie_{A=B} S$)**: 세타 조인의 특별한 형태로, 조인 조건($\theta$)이 오직 등호($=$)로만 이루어진 조인입니다. 일반적으로 두 릴레이션의 공통 속성(컬럼) 값이 일치하는 튜플들을 결합합니다.
*   **자연 조인 (Natural Join)**: 동등 조인의 한 형태로, 두 릴레이션에 이름이 같고 도메인도 같은 속성(컬럼)이 있을 때, 이 속성들을 기준으로 동등 조인을 수행한 후, 조인에 참여한 공통 속성은 한 번만 나타나도록 중복된 컬럼을 제거합니다. (슬라이드에는 명시적 예시가 없지만, 동등 조인의 특수한 형태임을 이해해야 합니다.)

### 코드/수식 해설

*   **카티션 곱의 형식 정의**
    $$R \times S = \{t \circ u \mid t \in R, u \in S\}$$
    이는 릴레이션 $R$의 모든 튜플 $t$와 릴레이션 $S$의 모든 튜플 $u$를 결합($\circ$)하여 새로운 튜플을 생성하는 집합을 의미합니다.

*   **세타 조인의 형식 정의**
    세타 조인 $R \bowtie_\theta S$는 $R \times S$의 결과에 Predicate $\theta$ (조건식)를 적용하여 필터링하는 연산입니다.

*   **동등 조인의 ERA Query 예시**
    $$R \bowtie_{\text{Year}=\text{Year}} S$$
    이는 릴레이션 $R$과 $S$의 'Year' 속성 값이 동일한 튜플들을 결합하는 동등 조인을 나타냅니다.

*   **Pandas 코드 예시**
    ```python
    # 1. 카티션 곱 (Product Join)
    # R과 S 두 DataFrame의 모든 행 조합을 생성합니다.
    cross = pd.merge(R, S, how="cross")

    # 2. 동등 조인을 위한 데이터 준비
    # 'babynames' DataFrame에서 'Year' 컬럼을 기준으로 그룹화하고,
    # 각 그룹의 'Count' 컬럼 합계를 계산합니다.
    # 그 결과를 'year_total'이라는 이름으로 바꾸고, 인덱스를 재설정하여
    # 'Year'와 'year_total' 컬럼을 가진 새로운 DataFrame을 만듭니다.
    yr_total = (babynames.groupby("Year")["Count"]
                         .sum()
                         .rename("year_total")
                         .reset_index())

    # 3. 동등 조인 (Equi-Join)
    # 'babynames' DataFrame과 위에서 생성한 'yr_total' DataFrame을
    # 'Year' 컬럼을 기준으로 내부 조인(inner join)합니다.
    # 'inner' 조인은 두 DataFrame 모두에 일치하는 'Year' 값이 있는 행만 결합합니다.
    eq_join = pd.merge(babynames, yr_total, on="Year", how="inner")
    ```

### 구체적 예시

*   **카티션 곱 (`how="cross"`)**:
    학생 명단 DataFrame `R` (컬럼: `Name`)에 `[철수, 영희]`가 있고, 과목 명단 DataFrame `S` (컬럼: `Course`)에 `[수학, 영어]`가 있다고 가정해 봅시다.
    `pd.merge(R, S, how="cross")`를 실행하면 다음과 같은 결과가 나옵니다:
    | Name | Course |
    | :--- | :----- |
    | 철수 | 수학   |
    | 철수 | 영어   |
    | 영희 | 수학   |
    | 영희 | 영어   |
    모든 학생이 모든 과목에 대해 한 쌍씩 조합된 형태로, 발생 가능한 모든 조합을 보여줍니다.

*   **동등 조인 (`on="Year", how="inner"`)**:
    `babynames` DataFrame이 각 해(Year)에 특정 이름(Name)이 사용된 횟수(Count)를 기록하고 있고, `yr_total` DataFrame이 각 해(Year)의 총 이름 사용 횟수(year_total)를 기록하고 있다고 가정해 봅시다.
    `babynames` (일부):
    | Year | Name  | Count |
    | :--- | :---- | :---- |
    | 1990 | John  | 100   |
    | 1990 | Mary  | 80    |
    | 1991 | Tom   | 120   |
    `yr_total` (일부):
    | Year | year_total |
    | :--- | :--------- |
    | 1990 | 100000     |
    | 1991 | 105000     |
    `pd.merge(babynames, yr_total, on="Year", how="inner")`를 실행하면 `Year` 컬럼의 값이 일치하는 행들이 병합됩니다. 예를 들어, 1990년의 'John' 데이터는 1990년의 총 이름 사용 횟수와 결합됩니다.
    결과 (일부):
    | Year | Name  | Count | year_total |
    | :--- | :---- | :---- | :--------- |
    | 1990 | John  | 100   | 100000     |
    | 1990 | Mary  | 80    | 100000     |
    | 1991 | Tom   | 120   | 105000     |
    이를 통해 각 이름의 사용 횟수를 해당 연도의 전체 사용 횟수와 비교하는 등의 분석이 가능해집니다.

### 시험 포인트

*   ⭐ **카티션 곱, 세타 조인, 동등 조인, 자연 조인의 개념적 정의와 차이점을 명확히 이해해야 합니다.** 특히 조인 조건($\theta$)의 일반성/특수성 (일반 조건 vs. 등호 조건)을 중심으로 구분할 수 있어야 합니다.
*   ⭐ **Pandas에서 `pd.merge()` 함수를 사용하여 카티션 곱(`how="cross"`)과 동등 조인(`on="..."`, `how="inner"`)을 구현하는 방법을 코드로 작성하고 설명할 수 있어야 합니다.** `on` 인자를 통한 조인 키 지정도 중요합니다.
*   ⭐ **주어진 관계 대수 표현식($R \times S$, $R \bowtie_\theta S$)이 무엇을 의미하는지 해석하고, 이를 Pandas 코드로 어떻게 구현할지 연결하여 이해하는 것이 중요합니다.**
*   데이터를 준비하는 과정에서 사용된 `groupby()`, `sum()`, `rename()`, `reset_index()` 등 Pandas 데이터 처리 메서드들의 역할과 조합 사용법도 숙지해야 합니다.

---

## Slide 16

**핵심 개념**:
*   `pandas.DataFrame.merge()` 함수는 두 개의 pandas DataFrame을 하나 이상의 공통 컬럼(key)을 기준으로 결합하는 관계형 데이터베이스의 조인(Join) 연산을 수행합니다.
*   이를 통해 분리된 데이터셋들을 통합하여 더 풍부한 정보를 가진 하나의 데이터셋을 생성할 수 있습니다.
*   `on` 파라미터는 조인의 기준이 되는 컬럼을 지정하며, 이 컬럼의 값이 일치하는 행끼리 결합됩니다.
*   `how` 파라미터는 조인 방식을 결정하며, `'inner'`, `'left'`, `'right'`, `'outer'` 네 가지 주요 방식이 있습니다.

**코드/수식 해설**:
`df`와 `df1` 두 DataFrame을 `on='name'` 컬럼을 기준으로 결합하는 예시입니다.

*   **기본 `merge` (Inner Join)**:
    *   양쪽 DataFrame에 모두 존재하는 `on` 키에 해당하는 행만 결합합니다. 기본 `how` 값입니다.
    ```python
    df.merge(df1, on='name')
    # 명시적 표현: df.merge(df1, on='name', how='inner')
    ```
*   **Left Outer Join**:
    *   `df` (왼쪽 DataFrame)의 모든 행을 유지하고, `df1` (오른쪽 DataFrame)에서 매칭되는 행을 결합합니다. `df1`에 매칭되는 키가 없는 경우, `df1`에서 오는 컬럼의 값은 `NaN`으로 채워집니다.
    ```python
    df.merge(df1, on='name', how='left')
    ```
*   **Right Outer Join**:
    *   `df1` (오른쪽 DataFrame)의 모든 행을 유지하고, `df` (왼쪽 DataFrame)에서 매칭되는 행을 결합합니다. `df`에 매칭되는 키가 없는 경우, `df`에서 오는 컬럼의 값은 `NaN`으로 채워집니다.
    ```python
    df.merge(df1, on='name', how='right')
    ```
*   **Full Outer Join**:
    *   양쪽 DataFrame의 모든 행을 포함하여 결합합니다. 한쪽 DataFrame에만 존재하는 키에 대해서는 다른 쪽 DataFrame의 컬럼 값이 `NaN`으로 채워집니다.
    ```python
    df.merge(df1, on='name', how='outer')
    ```
*   수식은 해당 슬라이드에 명시된 바가 없습니다.

**구체적 예시**:
도시의 인구 정보(`df`)와 면적 정보(`df1`)를 결합하는 상황을 예시로 듭니다.

`df` (인구 정보):
| name   | population |
| :----- | :--------- |
| Oslo   | 698660     |
| Vienna | 1911191    |

`df1` (면적 정보):
| name   | area  |
| :----- | :---- |
| Vienna | 414.8 |
| Tokyo  | 2194.1|

1.  **Inner Join (`how='inner'`)**:
    *   `df.merge(df1, on='name')`
    *   `name`이 'Vienna'인 행만 양쪽에 모두 존재하므로, 이 행만 결합됩니다. 'Oslo'와 'Tokyo'는 결과에 포함되지 않습니다.
    *   결과:
        | name   | population | area  |
        | :----- | :--------- | :---- |
        | Vienna | 1911191    | 414.8 |

2.  **Left Outer Join (`how='left'`)**:
    *   `df.merge(df1, on='name', how='left')`
    *   `df` (왼쪽)의 모든 도시('Oslo', 'Vienna')가 포함됩니다.
    *   'Vienna'는 `df1`에도 있으므로 면적 정보가 추가됩니다.
    *   'Oslo'는 `df1`에 없으므로 'area' 컬럼이 `NaN`으로 채워집니다.
    *   결과:
        | name   | population | area  |
        | :----- | :--------- | :---- |
        | Oslo   | 698660.0   | NaN   |
        | Vienna | 1911191.0  | 414.8 |

3.  **Right Outer Join (`how='right'`)**:
    *   `df.merge(df1, on='name', how='right')`
    *   `df1` (오른쪽)의 모든 도시('Vienna', 'Tokyo')가 포함됩니다.
    *   'Vienna'는 `df`에도 있으므로 인구 정보가 추가됩니다.
    *   'Tokyo'는 `df`에 없으므로 'population' 컬럼이 `NaN`으로 채워집니다.
    *   결과:
        | name   | population | area  |
        | :----- | :--------- | :---- |
        | Vienna | 1911191.0  | 414.8 |
        | Tokyo  | NaN        | 2194.1|

4.  **Full Outer Join (`how='outer'`)**:
    *   `df.merge(df1, on='name', how='outer')`
    *   양쪽 DataFrame의 모든 고유한 도시('Oslo', 'Vienna', 'Tokyo')가 포함됩니다.
    *   각 도시에 대해 존재하는 정보는 결합되고, 없는 정보는 `NaN`으로 채워집니다.
    *   결과:
        | name   | population | area  |
        | :----- | :--------- | :---- |
        | Oslo   | 698660.0   | NaN   |
        | Vienna | 1911191.0  | 414.8 |
        | Tokyo  | NaN        | 2194.1|

**시험 포인트**:
*   ⭐ `df.merge()` 함수의 기본적인 사용법(특히 `on`과 `how` 파라미터)을 정확히 이해하고 있어야 합니다.
*   ⭐ `how` 파라미터의 네 가지 조인 방식(`'inner'`, `'left'`, `'right'`, `'outer'`) 각각이 어떤 결과를 반환하는지, 그리고 언제 `NaN` 값이 발생하는지 명확히 구분할 수 있어야 합니다.
*   ⭐ 실제 데이터 통합 시나리오에서 어떤 조인 방식을 선택해야 하는지 그 이유와 함께 설명할 수 있어야 합니다.
*   ⭐ 조인 키에 중복 값이 있을 경우, `merge` 연산은 카티션 곱(Cartesian product, many-to-many match)을 생성할 수 있다는 점을 인지하고 있어야 합니다. 예를 들어, 왼쪽 DF에 키 'A'가 2개, 오른쪽 DF에 키 'A'가 3개 있다면 결과는 'A'가 $2 \times 3 = 6$개 조합으로 나타납니다.

---

## Slide 17

### DataFrame.join: 인덱스 기반 결합 (Index-Aligned Join)

**핵심 개념**:
`DataFrame.join()` 메서드는 두 개의 DataFrame을 인덱스를 기준으로 병합(결합)하는 데 사용됩니다. 이는 SQL의 JOIN 연산과 유사하지만, 기본적으로 공통된 열(column)이 아닌 행의 인덱스를 키(key)로 사용하여 데이터를 연결합니다. `how` 파라미터를 통해 다양한 결합 방식을 지정할 수 있습니다.

**코드/수식 해설**:

`DataFrame.join()`의 기본 문법은 다음과 같습니다.
```python
df.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False)
```
여기서 핵심은 `other` (결합할 다른 DataFrame)와 `how` (결합 방식) 파라미터입니다.

`how` 파라미터는 다음 4가지 값을 가질 수 있습니다:

*   `'left'` (기본값): 왼쪽 DataFrame (`df`)의 모든 인덱스를 유지하고, 오른쪽 DataFrame (`other`)에서 일치하는 인덱스의 데이터를 결합합니다. 오른쪽 DataFrame에 해당 인덱스가 없으면 `NaN`으로 채워집니다.
*   `'inner'`: 두 DataFrame 모두에 존재하는 공통 인덱스만을 기준으로 데이터를 결합합니다.
*   `'outer'`: 두 DataFrame의 모든 인덱스를 포함하여 데이터를 결합합니다. 어느 한쪽 DataFrame에만 존재하는 인덱스는 다른 쪽 DataFrame의 데이터가 `NaN`으로 채워집니다.
*   `'right'`: 오른쪽 DataFrame (`other`)의 모든 인덱스를 유지하고, 왼쪽 DataFrame (`df`)에서 일치하는 인덱스의 데이터를 결합합니다. 왼쪽 DataFrame에 해당 인덱스가 없으면 `NaN`으로 채워집니다.

`df.join()`은 또한 `pd.concat([df, df1], axis=1)`과 유사하게 동작할 수 있지만 중요한 차이점이 있습니다. `join`은 인덱스 기반의 키 로직을 사용하여 데이터를 정렬하고 일치시키지만, `pd.concat(axis=1)`은 단순히 열을 쌓는 방식으로, 인덱스 정렬이 보장되지 않으면 의도치 않은 결과를 초래할 수 있습니다 (물론 `concat`도 인덱스를 맞춰서 병합하는 기능이 있지만, 단순히 `axis=1`로만 사용할 경우 `join`과 같은 키 로직이 없는 경우가 일반적입니다).

**구체적 예시**:

다음과 같은 두 개의 DataFrame을 가정합니다.

```python
import pandas as pd
import numpy as np

# df: 도시별 인구 데이터
data_df = {'population': [698660, 1911191]}
df = pd.DataFrame(data_df, index=['Oslo', 'Vienna'])

# df1: 도시별 면적 데이터
data_df1 = {'area': [414.8, 2194.1]}
df1 = pd.DataFrame(data_df1, index=['Vienna', 'Tokyo'])

print("DataFrame df:")
print(df)
print("\nDataFrame df1:")
print(df1)
```

출력:
```
DataFrame df:
          population
Oslo          698660
Vienna       1911191

DataFrame df1:
          area
Vienna   414.8
Tokyo   2194.1
```

1.  **Inner Join**: `df.join(df1, how='inner')`
    *   두 DataFrame에 공통으로 존재하는 인덱스인 'Vienna'만 남습니다.
    ```python
    df_inner = df.join(df1, how='inner')
    print("\nInner Join:")
    print(df_inner)
    ```
    출력:
    ```
    Inner Join:
            population   area
    Vienna     1911191  414.8
    ```

2.  **Left Join** (기본값): `df.join(df1, how='left')` 또는 `df.join(df1)`
    *   왼쪽 DataFrame `df`의 모든 인덱스('Oslo', 'Vienna')를 유지합니다. `df1`에 'Oslo'가 없으므로 `area`는 `NaN`이 됩니다.
    ```python
    df_left = df.join(df1, how='left')
    print("\nLeft Join:")
    print(df_left)
    ```
    출력:
    ```
    Left Join:
            population   area
    Oslo        698660    NaN
    Vienna     1911191  414.8
    ```

3.  **Right Join**: `df.join(df1, how='right')`
    *   오른쪽 DataFrame `df1`의 모든 인덱스('Vienna', 'Tokyo')를 유지합니다. `df`에 'Tokyo'가 없으므로 `population`은 `NaN`이 됩니다.
    ```python
    df_right = df.join(df1, how='right')
    print("\nRight Join:")
    print(df_right)
    ```
    출력:
    ```
    Right Join:
            population   area
    Vienna     1911191  414.8
    Tokyo          NaN  2194.1
    ```

4.  **Outer Join**: `df.join(df1, how='outer')`
    *   두 DataFrame의 모든 고유한 인덱스('Oslo', 'Vienna', 'Tokyo')를 포함합니다. 데이터가 없는 부분은 `NaN`으로 채워집니다.
    ```python
    df_outer = df.join(df1, how='outer')
    print("\nOuter Join:")
    print(df_outer)
    ```
    출력:
    ```
    Outer Join:
            population   area
    Oslo      698660.0    NaN
    Tokyo          NaN  2194.1
    Vienna   1911191.0  414.8
    ```

**시험 포인트**:

*   ⭐ `DataFrame.join()` 메서드는 기본적으로 **인덱스를 기준**으로 두 DataFrame을 결합합니다. (컬럼 기준 결합은 `on` 파라미터를 사용하거나 `pd.merge()`를 활용할 수 있습니다.)
*   ⭐ `how` 파라미터의 4가지 유형 (`'left'`, `'inner'`, `'outer'`, `'right'`)과 각 유형이 결과를 어떻게 변화시키는지 정확히 이해해야 합니다. 특히 `'left'`가 기본값이라는 것을 기억하세요.
*   ⭐ `df.join()`은 인덱스 기반의 '키' 로직을 사용하지만, `pd.concat([df, df1], axis=1)`은 인덱스 정렬에 대한 명시적인 지시가 없으면 단순히 열을 옆으로 쌓는 방식으로 동작하여 `join`과는 다른 결과를 줄 수 있다는 차이점을 알고 있어야 합니다.

---

## Slide 18

**핵심 개념**
이 슬라이드는 두 개의 데이터프레임을 서로 다른 키(key) 컬럼 이름을 사용하여 병합(merge)하는 방법과, 병합 후 결과 데이터프레임에서 원하는 컬럼만 선택(filter)하는 방법을 설명합니다. 특히, 병합 과정에서 키 컬럼의 이름이 다를 때 `left_on`과 `right_on` 인자를 활용하는 방법과, 컬럼 이름 충돌(clashes)이 발생할 경우 이를 해결하는 `suffixes` 인자에 대한 힌트를 제공합니다.

**코드/수식 해설**

1.  **데이터프레임 병합 (`pandas.merge`)**
    `cities` 데이터프레임과 `states` 데이터프레임을 병합합니다.
    ```python
    df = cities.merge(states, left_on='state_code', right_on='code')
    ```
    *   `cities.merge(states, ...)`: `cities` 데이터프레임을 기준으로 `states` 데이터프레임을 병합합니다.
    *   `left_on='state_code'`: 왼쪽(left) 데이터프레임인 `cities`에서 병합의 기준으로 사용할 컬럼을 `'state_code'`로 지정합니다.
    *   `right_on='code'`: 오른쪽(right) 데이터프레임인 `states`에서 병합의 기준으로 사용할 컬럼을 `'code'`로 지정합니다.
    *   두 컬럼의 값이 일치하는 행들만 병합되어 새로운 데이터프레임 `df`를 생성합니다 (기본적으로 `inner` 조인).
    *   이 예시에서는 `cities`의 'DC'는 `states`에 없으므로, Washington 행은 결과에서 제외됩니다.
    *   결과 `df`에는 `cities`의 모든 컬럼(`city`, `state_code`)과 `states`의 모든 컬럼(`code`, `state`)이 포함됩니다. `state_code`와 `code`는 다른 이름을 가지고 있으므로 모두 유지됩니다.

2.  **컬럼 선택 (`df.filter`)**
    병합된 데이터프레임 `df`에서 특정 컬럼들만 선택합니다.
    ```python
    df.filter(['city', 'state'])
    ```
    *   `df.filter(...)`: `df` 데이터프레임에서 지정된 조건에 따라 행 또는 컬럼을 필터링합니다.
    *   `['city', 'state']`: 리스트 안에 지정된 컬럼 이름인 'city'와 'state'만 선택하여 새로운 데이터프레임을 반환합니다.

3.  **컬럼 이름 충돌 해결 힌트 (`suffixes`)**
    병합하는 두 데이터프레임에 동일한 이름의 컬럼이 존재할 경우, `pandas`는 기본적으로 충돌하는 컬럼에 `_x`와 `_y` 접미사(suffix)를 붙여 이름을 변경합니다.
    ```python
    # 예시: cities와 states에 모두 'population' 컬럼이 있었다면
    # df = cities.merge(states, on='state_code', suffixes=('_city', '_state'))
    ```
    *   `suffixes=('_city', '_state')`: 이 인자를 사용하여 충돌하는 컬럼에 사용자 정의 접미사를 지정할 수 있습니다. 예를 들어, `cities`의 'population'은 'population_city'가 되고, `states`의 'population'은 'population_state'가 됩니다. `pandas.join` 메서드에서는 `lsuffix`와 `rsuffix` 인자를 사용합니다.

**구체적 예시**

`cities` 데이터프레임은 도시 이름과 해당 주 코드를 가지고 있습니다:
```
    city          state_code
0   San Francisco   CA
1   Miami           FL
2   Washington      DC
3   Los Angeles     CA
```

`states` 데이터프레임은 주 코드와 해당 주 이름을 가지고 있습니다:
```
    code    state
0   CA      California
1   FL      Florida
2   TX      Texas
```

두 데이터프레임을 `cities`의 `state_code`와 `states`의 `code`를 기준으로 병합합니다. `cities`의 `state_code='CA'`는 `states`의 `code='CA'`와 매칭되고, `cities`의 `state_code='FL'`은 `states`의 `code='FL'`과 매칭됩니다.
`cities`의 `state_code='DC'`는 `states`에 해당 `code`가 없으므로 병합 결과에서 제외됩니다.

```python
df = cities.merge(states, left_on='state_code', right_on='code')
```
병합 결과 `df`:
```
    city            state_code  code    state
0   Los Angeles     CA          CA      California
1   San Francisco   CA          CA      California
2   Miami           FL          FL      Florida
```
`Los Angeles`와 `San Francisco`는 모두 `CA` 주에 속하며 `California` 주로 연결됩니다. `Miami`는 `FL` 주에 속하며 `Florida` 주로 연결됩니다.

이제 이 `df`에서 `city`와 `state` 컬럼만 보고 싶다면:
```python
df.filter(['city', 'state'])
```
결과:
```
    city            state
0   San Francisco   California
1   Los Angeles     California
2   Miami           Florida
```

**시험 포인트**

*   ⭐ `pandas.merge` 사용 시 두 데이터프레임의 조인 키(join key) 컬럼 이름이 다를 때 `left_on`과 `right_on` 인자를 올바르게 사용하는 방법을 숙지해야 합니다.
*   ⭐ `merge` 또는 `join` 연산 시 컬럼 이름이 충돌할 경우 (`city`와 `states` 모두 `population` 컬럼이 있을 경우 등) `suffixes` (또는 `lsuffix`/`rsuffix`) 인자를 사용하여 충돌을 해결하는 방법을 이해해야 합니다.
*   `df.filter()` 메서드를 사용하여 특정 컬럼을 선택하는 방법도 알아두면 좋습니다.
*   `merge`의 기본 조인 방식은 `inner` 조인이며, 매칭되지 않는 행은 결과에서 제외된다는 점을 기억하세요.

---

## Slide 19

### 핵심 개념

*   **Outer Join**: 두 데이터셋(테이블)의 모든 행을 유지하며 합치는 연산입니다. 한쪽에만 존재하는 키에 대해서는 다른 쪽의 해당 필드를 `null` (pandas에서는 `NaN`) 값으로 채웁니다.
*   **Semijoin ($R \ltimes S$)**: 왼쪽 데이터셋 ($R$)의 튜플 중 오른쪽 데이터셋 ($S$)에 적어도 하나 이상의 일치하는 키가 있는 튜플만을 반환하는 연산입니다. 결과는 왼쪽 데이터셋 ($R$)의 컬럼만 포함합니다. 즉, $R$의 튜플이 $S$에 존재하는지 여부를 확인하는 필터 역할을 합니다.
*   **Antijoin ($R \setminus (R \ltimes S)$)**: 왼쪽 데이터셋 ($R$)의 튜플 중 오른쪽 데이터셋 ($S$)에 일치하는 키가 *없는* 튜플만을 반환하는 연산입니다. 결과는 왼쪽 데이터셋 ($R$)의 컬럼만 포함합니다. 즉, $R$의 튜플이 $S$에 존재하지 않는지 여부를 확인하는 필터 역할을 합니다.

이 세 가지 연산은 특정 조건(다른 데이터셋에 매칭되는 키의 존재 여부)에 따라 데이터프레임 ($R$)의 튜플을 **유지하거나 제외**하는 데 사용됩니다.

### 코드/수식 해설

*   **ERA (Query) Notation**:
    *   Semijoin: $R \ltimes_{Name} S$
        *   $R$의 튜플 중 $S$에 `Name` 속성이 일치하는 것이 있는 경우 $R$의 튜플을 반환.
    *   Antijoin: $R \setminus (R \ltimes_{Name} S)$
        *   $R$의 튜플 중 $S$에 `Name` 속성이 일치하는 것이 *없는* 경우 $R$의 튜플을 반환.

*   **Pandas Code Examples**:

    ```python
    # Outer join (illustrative)
    outer = pd.merge(babynames, yr_total, on="Year", how="outer")
    ```
    *   `pd.merge(df1, df2, on="key", how="outer")`: `df1` (`babynames`)과 `df2` (`yr_total`)를 `Year` 컬럼을 기준으로 외부 조인합니다. 두 DataFrame 중 어느 한쪽에만 있는 `Year` 값에 대해서는 다른 DataFrame의 해당 컬럼이 `NaN`으로 채워집니다.

    ```python
    # Semijoin (key = Name)
    keys = pd.DataFrame({"Name":["Mary","Alice"]})
    semi = babynames[babynames["Name"].isin(keys["Name"])]
    ```
    *   `keys = pd.DataFrame({"Name":["Mary","Alice"]})`: `S` 역할을 할 `keys` DataFrame을 생성합니다. 여기서는 `Name`이 'Mary' 또는 'Alice'인 경우를 찾습니다.
    *   `babynames["Name"].isin(keys["Name"])`: `babynames` DataFrame의 `Name` 컬럼 값이 `keys` DataFrame의 `Name` 컬럼 값들 중 하나에 포함되는지 여부를 나타내는 불리언 Series를 반환합니다.
    *   `babynames[...]`: 이 불리언 Series를 사용하여 `babynames` DataFrame을 필터링합니다. 결과적으로 `keys`에 있는 `Name`을 가진 `babynames`의 행들만 남게 되며, 이는 semijoin의 구현 방식입니다.

    ```python
    # Antijoin
    anti = (babynames.merge(keys, on="Name", how="left", indicator=True)
                    .query("_merge=='left_only'")
                    .drop(columns=["_merge"]))
    ```
    *   `babynames.merge(keys, on="Name", how="left", indicator=True)`: `babynames`와 `keys`를 `Name` 컬럼을 기준으로 **왼쪽 조인**합니다. `indicator=True` 인자를 통해 조인 결과에 `_merge`라는 특수 컬럼을 추가합니다. 이 컬럼은 각 행이 왼쪽 DataFrame에만 있었는지(`'left_only'`), 오른쪽 DataFrame에만 있었는지(`'right_only'`), 또는 양쪽에 모두 있었는지(`'both'`)를 나타냅니다.
    *   `.query("_merge=='left_only'")`: `_merge` 컬럼 값이 `'left_only'`인 행들만 선택합니다. 이들은 `babynames`에는 존재하지만 `keys`에는 매칭되는 `Name`이 없는 행들입니다.
    *   `.drop(columns=["_merge"])`: 최종 결과에서 `_merge` 보조 컬럼을 제거하여 순수한 antijoin 결과를 얻습니다.

### 구체적 예시

*   **Outer Join**: 두 반의 학생 명단(이름, 학번)과 수강 과목 명단(학번, 과목명)을 합친다고 가정해 봅시다. `outer` 조인을 사용하면 모든 학생의 정보와 모든 과목 정보를 볼 수 있습니다. 만약 특정 학생이 과목을 수강하지 않았다면 해당 학생의 과목명은 `NaN`이 되고, 특정 과목을 수강하는 학생이 없다면 해당 과목의 학생 정보는 `NaN`이 됩니다.
*   **Semijoin**: 전체 학생 명단(`babynames`)에서 '데이터 분석' 수업을 수강하는 학생 명단(`keys`에 있는 학생 이름)을 찾고 싶을 때 사용합니다. 결과는 '데이터 분석' 수업을 수강하는 학생들만으로 구성된 전체 학생 명단의 일부가 됩니다. (`babynames`의 모든 컬럼 유지).
*   **Antijoin**: 전체 학생 명단(`babynames`)에서 '데이터 분석' 수업을 *수강하지 않는* 학생 명단(`keys`에 있는 학생 이름이 없는)을 찾고 싶을 때 사용합니다. 결과는 '데이터 분석' 수업을 수강하지 않는 학생들만으로 구성된 전체 학생 명단의 일부가 됩니다. (`babynames`의 모든 컬럼 유지).

### 시험 포인트

*   ⭐ **Outer Join, Semijoin, Antijoin의 정의와 각 연산의 결과가 어떻게 다른지 명확하게 이해하는 것이 중요합니다.** 특히 Semijoin과 Antijoin은 결과에 왼쪽 데이터프레임($R$)의 컬럼만 포함한다는 점을 기억하세요.
*   ⭐ **ERA (Query) Notation**으로 Semijoin ($R \ltimes S$)과 Antijoin ($R \setminus (R \ltimes S)$)을 정확하게 표현할 수 있어야 합니다.
*   ⭐ **Pandas에서 Semijoin과 Antijoin을 구현하는 코드 패턴을 숙지해야 합니다.** 특히 Antijoin을 구현하기 위한 `pd.merge`의 `how='left'`, `indicator=True` 인자 사용법과 `_merge` 컬럼을 활용한 `.query()` 필터링 방식은 시험에서 중요하게 다뤄질 수 있습니다.
*   ⭐ `.isin()`을 이용한 Semijoin과 `merge` + `indicator` + `query`를 이용한 Antijoin의 **장단점과 적절한 사용 상황**을 이해하고 있으면 좋습니다. (`.isin()`은 비교 대상이 Series나 list일 때 간단하고 효율적이며, `merge` 방식은 여러 컬럼을 기준으로 하거나 더 복잡한 조건이 필요할 때 유용할 수 있습니다.)

---

## Slide 20

**핵심 개념**
Grouping/Aggregation은 데이터를 특정 기준(그룹핑 속성)에 따라 분할하고, 각 그룹에 대해 하나 이상의 집계 함수(평균, 합계, 최댓값 등)를 적용하여 요약된 결과를 얻는 과정입니다. 관계형 대수(Relational Algebra)에서는 $\gamma$ (감마) 연산으로 표현됩니다.

**코드/수식 해설**

**수식:**
슬라이드 상단의 수식은 관계형 대수에서 Grouping/Aggregation을 나타냅니다.
$$ \gamma_G, f_1(A_1) \to B_1, \ldots (R) $$
*   $G$: 데이터를 그룹화할 기준이 되는 속성(컬럼)들의 집합입니다. (예: `Sex`, `decade`)
*   $f_i(A_i)$: 각 그룹에 적용될 집계 함수($f_i$)와 해당 함수가 적용될 속성($A_i$)을 나타냅니다. (예: `mean(Count)`, `max(Count)`)
*   $\to B_i$: 집계 함수의 결과가 저장될 새로운 속성(컬럼) 이름($B_i$)을 지정합니다. (예: `mean`, `max`, `total`)
*   $R$: 그룹핑 및 집계가 수행될 릴레이션(테이블 또는 DataFrame)입니다. (예: `babynames`)

**코드:**
```python
1 babynames["decade"] = (babynames["Year"] // 10) * 10
2 stats = (babynames.groupby(["Sex", "decade"])["Count"]
3                  .agg(mean="mean", max="max", total="sum")
4                  .reset_index())
```
1.  `babynames["decade"] = (babynames["Year"] // 10) * 10`: `babynames` DataFrame에 'decade'라는 새로운 컬럼을 추가합니다. 'Year' 컬럼의 값을 10으로 나눈 정수 부분에 다시 10을 곱하여 각 연도를 해당 10년의 시작 연도(예: 2005년 -> 2000년)로 변환합니다. 이는 데이터를 10년 단위로 그룹화하기 위한 전처리 과정입니다.
2.  `babynames.groupby(["Sex", "decade"])`: `babynames` DataFrame을 'Sex'와 'decade' 컬럼을 기준으로 그룹화합니다.
3.  `["Count"]`: 그룹화된 각 그룹에 대해 'Count' 컬럼에 대해서만 집계 연산을 수행하도록 지정합니다.
4.  `.agg(mean="mean", max="max", total="sum")`: 'Count' 컬럼에 대해 여러 집계 함수를 동시에 적용합니다.
    *   `mean="mean"`: 'Count'의 평균을 계산하고 결과를 'mean'이라는 새 컬럼에 저장합니다.
    *   `max="max"`: 'Count'의 최댓값을 계산하고 결과를 'max'라는 새 컬럼에 저장합니다.
    *   `total="sum"`: 'Count'의 합계를 계산하고 결과를 'total'이라는 새 컬럼에 저장합니다.
5.  `.reset_index()`: `groupby` 결과는 기본적으로 그룹핑 키(여기서는 'Sex', 'decade')를 DataFrame의 인덱스(MultiIndex)로 설정합니다. `reset_index()`는 이 인덱스를 일반 컬럼으로 변환하여, 'Sex'와 'decade'가 다시 데이터 컬럼으로 돌아오게 합니다.

**구체적 예시**
'babynames' 데이터셋에 아기 이름, 성별, 출생 연도, 해당 이름의 출생아 수가 있다고 가정해 봅시다.
위 코드는 다음과 같은 과정을 수행합니다:
1.  **'decade' 컬럼 생성**: 예를 들어, 'Year'가 1995면 'decade'는 1990이 되고, 2008년이면 2000이 됩니다.
2.  **그룹화**: 'Sex'(성별)와 'decade'(10년 단위)의 모든 가능한 조합(예: 'F', 1990), ('M', 2000) 등으로 데이터를 나눕니다.
3.  **집계**: 각 그룹에 대해 'Count' 컬럼의 평균, 최댓값, 총합을 계산합니다.
    *   예를 들어, 'F'(여성), 1990년대 그룹에 속하는 모든 아기 이름들의 'Count'를 모아서 평균 출생아 수, 가장 많았던 이름의 출생아 수, 그리고 해당 그룹의 총 출생아 수를 계산합니다.
4.  **결과 DataFrame ('stats') 생성**: 'Sex', 'decade', 'mean', 'max', 'total' 컬럼을 가진 새로운 DataFrame이 생성되어 각 성별-10년 그룹의 통계를 보여줍니다.

**`reset_index()`를 사용하는 이유:**
*   **그룹 키를 컬럼으로 변환**: `groupby`의 기본 동작은 그룹 키를 인덱스(MultiIndex)로 만듭니다. `reset_index()`를 사용하면 이 인덱스 레벨이 일반 데이터 컬럼으로 다시 들어와, 데이터프레임을 다루기 더 편리하게 만듭니다.
*   **쉬운 병합/조인**: 다른 DataFrame과 병합(merge) 또는 조인(join)을 수행할 때, 그룹 키가 일반 컬럼으로 존재해야 `on=['Sex', 'decade']`와 같이 직접 컬럼 이름을 지정하여 쉽게 병합할 수 있습니다. `right_index=True`와 같은 복잡한 옵션 없이 작업이 가능해집니다.

**시험 포인트**
*   ⭐ `groupby()`의 개념과 사용법 (그룹화 기준 컬럼 지정).
*   ⭐ `agg()`를 이용한 다중 집계 함수 적용 및 컬럼 이름 변경 방법.
*   ⭐ `reset_index()`의 역할과 필요성 (왜 `groupby` 후 `reset_index()`를 사용하는지, MultiIndex와의 관계).
*   ⭐ 관계형 대수의 $\gamma$ 연산이 `pandas.groupby().agg()`와 어떻게 매핑되는지 이해.
*   ⭐ 특정 기간(예: 10년 단위)으로 데이터를 그룹화하기 위한 컬럼(`decade`) 생성 방식 (`//` 연산자 활용).

---

## Slide 21

**핵심 개념**:
*   **GroupBy의 본질**: pandas의 `groupby` 연산은 원본 `DataFrame` 또는 `Series`를 특정 기준(key)에 따라 논리적인 부분(sub-DataFrame 또는 sub-Series)으로 분할(partitioning)하는 개념입니다. 이는 실제 데이터 복사본을 만드는 것이 아니라, 키 값과 해당 부분 데이터 간의 **매핑(mapping)**을 생성하는 '지연(lazy)' 연산입니다.
*   **DataFrameGroupBy와 SeriesGroupBy**:
    *   `DataFrameGroupBy`: 하나 이상의 열(column)을 기준으로 그룹화하여 `key`를 `sub-DataFrame`에 매핑합니다.
    *   `SeriesGroupBy`: Series를 기준으로 그룹화하여 `key`를 `sub-Series`에 매핑합니다.
*   **메모리 효율성**: `groupby` 연산 시에는 즉시 데이터 복사본을 생성하지 않습니다. 부분 데이터(subframe/subseries)는 `iter()`, `get_group()`, `apply()`, `agg()` 등의 접근 또는 연산이 일어날 때 **실체화(materialized)**됩니다. ⭐이는 대용량 데이터 처리 시 메모리 효율성을 높이는 중요한 특징입니다.

**코드/수식 해설**:

```python
import pandas as pd

# 1. DataFrame 생성
df = pd.DataFrame({
    "store": ["A", "A", "B", "B", "B"],
    "prod": ["x", "y", "x", "y", "y"],
    "qty": [2, 1, 3, 2, 5],
    "price": [10, 12, 10, 11, 12]
})
print("Original DataFrame:")
print(df)
```
초기 데이터를 담고 있는 `DataFrame`을 생성합니다. 'store', 'prod'(상품), 'qty'(수량), 'price'(가격) 컬럼으로 구성됩니다.

```python
# 2. DataFrameGroupBy 객체 생성
# 'store'와 'prod' 컬럼을 기준으로 그룹화
g = df.groupby(["store", "prod"])
print("\nDataFrameGroupBy object 'g':")
print(g)
```
`df.groupby(["store", "prod"])`는 'store'와 'prod'를 복합 키로 사용하여 `DataFrameGroupBy` 객체 `g`를 생성합니다. 이때 실제 sub-DataFrame이 생성되는 것이 아니라, 매핑 규칙만 정의됩니다.

```python
# 3. DataFrameGroupBy 객체 순회 및 특정 그룹 접근
# 첫 번째 그룹의 키와 sub-DataFrame 추출
first_key, first_subdf = next(iter(g))
print(f"\nFirst group key: {first_key}") # ('A', 'x')
print("First sub-DataFrame:")
print(first_subdf)

# 특정 그룹의 sub-DataFrame 직접 접근
only_Ax = g.get_group(("A", "x"))
print("\nSub-DataFrame for group ('A', 'x') using get_group():")
print(only_Ax)
```
`next(iter(g))`를 통해 `DataFrameGroupBy` 객체를 순회하며 첫 번째 그룹의 키와 해당 `sub-DataFrame`을 얻을 수 있습니다. `g.get_group(("A", "x"))`는 특정 그룹 키 `("A", "x")`에 해당하는 `sub-DataFrame`을 직접 반환합니다. 이 시점에서 데이터가 실체화됩니다.

```python
# 4. SeriesGroupBy 객체 생성
# 'qty' Series를 'store' 컬럼을 기준으로 그룹화
s = df["qty"].groupby(df["store"])
print("\nSeriesGroupBy object 's':")
print(s)
```
`df["qty"].groupby(df["store"])`는 'qty' Series를 'store' 컬럼을 기준으로 그룹화하여 `SeriesGroupBy` 객체 `s`를 생성합니다.

```python
# 5. SeriesGroupBy 객체 순회 및 집계
print("\nIterating through SeriesGroupBy 's' and summing each sub-Series:")
for key, subseries in s:
    print(f"Store: {key}, Sum of qty: {subseries.sum()}")
```
`SeriesGroupBy` 객체 `s`를 순회하면서 각 상점(`key`)의 'qty' `sub-Series`(`subseries`)를 얻고, `subseries.sum()`으로 각 그룹의 합계를 계산합니다.

```python
# 6. apply()를 이용한 그룹별 복합 연산 (가중 평균 계산)
# 각 그룹(store, prod) 내에서 'qty'와 'price'를 사용하여 가중 평균 가격 계산
wmean_price = g.apply(lambda sub: (sub["qty"] * sub["price"]).sum() / sub["qty"].sum())
print("\nWeighted mean price per (store, prod) group using apply():")
print(wmean_price)
```
`g.apply()`는 각 `sub-DataFrame`에 사용자 정의 함수(여기서는 `lambda` 함수)를 적용합니다. 이 예시에서는 각 그룹의 `qty`와 `price`를 이용하여 가중 평균 가격을 계산합니다. 각 `sub`는 해당 그룹의 `sub-DataFrame`입니다.
가중 평균 공식은 다음과 같습니다.
$$ \text{Weighted Mean Price} = \frac{\sum (\text{qty} \times \text{price})}{\sum \text{qty}} $$

```python
# 7. transform()을 이용한 그룹 내 비율 계산 (원본 DataFrame/Series의 shape 유지)
# 각 상점 내에서 'qty'의 비율 계산
share_in_store = s.transform(lambda x: x / x.sum())
print("\nShare of 'qty' within each store using transform():")
print(share_in_store)
```
`s.transform()`은 `apply()`와 유사하게 각 `sub-Series`에 함수를 적용하지만, **결과의 shape가 원본 `Series`와 동일하게 유지**됩니다. 즉, 각 원본 행에 대해 그룹 내에서의 변환된 값을 반환합니다. 이 예시에서는 각 상점 내에서 'qty'가 차지하는 비율을 계산합니다.

**구체적 예시**:

당신이 대형마트의 데이터 분석가라고 가정해 봅시다. 매일 수많은 상품들이 다양한 매장(store)에서 판매(prod, qty, price)됩니다.
*   **`df.groupby(["store", "prod"])`**: 이 연산은 "각 매장별로, 각 상품에 대해" 판매 데이터를 분리하는 것과 같습니다. 예를 들어 "강남점의 사과", "강남점의 바나나", "분당점의 사과" 등으로 데이터를 묶는 것이죠.
*   **`next(iter(g))` 또는 `g.get_group(("A", "x"))`**: 이 매핑을 통해 "A 매장의 x 상품"에 해당하는 모든 판매 기록만을 정확히 조회할 수 있습니다. 마치 특정 매대(그룹)에 가서 특정 상품(키)의 재고 목록(sub-DataFrame)을 확인하는 것과 같습니다.
*   **`g.apply(lambda sub: ...)` (가중 평균 계산)**: "강남점의 사과" 그룹에 대해 팔린 사과의 '평균 가격'을 계산하고 싶을 때, 단순히 가격을 평균내는 것이 아니라, 많이 팔린 사과의 가격에 더 비중을 둬서 '가중 평균'을 계산할 수 있습니다. 이는 실제 매출에 더 가까운 평균 가격을 보여줄 것입니다. 예를 들어, 'A' 매장 'x' 상품이 2개 10원, 1개 12원에 팔렸다면 $(2 \times 10 + 1 \times 12) / (2+1) = 32/3 \approx 10.67$원이 됩니다.
*   **`s.transform(lambda x: x / x.sum())` (그룹 내 비율 계산)**: 특정 매장 내에서 각 상품의 판매 수량이 전체 매장 판매 수량 중 몇 %를 차지하는지 알고 싶을 때 `transform`을 사용합니다. 예를 들어, 'A' 매장에서 'x' 상품이 2개, 'y' 상품이 1개 팔렸다면, 'x' 상품은 'A' 매장 전체 판매량의 2/3을, 'y' 상품은 1/3을 차지한다고 계산할 수 있습니다. 결과가 원본 `Series`의 길이와 같기 때문에, 이 비율 데이터를 원본 `DataFrame`의 새로운 컬럼으로 바로 추가하여 활용하기 좋습니다.

**시험 포인트**:
*   ⭐**`groupby` 연산의 '지연(lazy)' 특성**: `groupby` 객체 생성 시 데이터 복사가 일어나지 않고, 실제 연산(iterate, get_group, apply, agg 등)이 수행될 때 데이터가 실체화된다는 점을 이해해야 합니다. 이는 메모리 효율성과 직결됩니다.
*   ⭐**`apply()`와 `transform()`의 차이점**:
    *   **`apply()`**: 각 그룹에 함수를 적용한 후, 그룹별로 집계된 결과를 반환합니다. 결과의 형태가 원본과 다를 수 있으며, `Series`, `DataFrame`, 스칼라 등 다양한 형태가 될 수 있습니다. (예: 그룹별 가중 평균)
    *   **`transform()`**: 각 그룹에 함수를 적용하지만, 결과의 **shape가 원본 DataFrame/Series의 shape와 동일하게 유지**됩니다. 각 그룹의 원본 행 수만큼의 결과를 반환하며, 주로 그룹 내의 개별 항목을 변환하거나 표준화할 때 사용됩니다. (예: 그룹 내 비율, 그룹 내 스케일링)
    *   두 메서드의 차이점은 시험에서 자주 질문될 수 있습니다. 특히 결과의 'shape' 유지 여부에 주목하세요.
*   `DataFrameGroupBy`와 `SeriesGroupBy` 객체에서 `get_group()` 또는 `iter()`를 사용하여 특정 그룹 데이터에 접근하는 방법.
*   `groupby` 연산이 `partitioning`과 `mapping`이라는 개념으로 설명된다는 점.

---

## Slide 22

**핵심 개념**:
*   **데이터 그룹화 (Grouping Data)**: Pandas의 `groupby()` 메서드는 DataFrame의 데이터를 하나 이상의 컬럼 값을 기준으로 그룹으로 나눕니다.
*   **집계 (Aggregation)**: 그룹으로 나뉜 각 데이터 셋에 대해 `sum()`, `mean()`, `count()`, `max()`, `min()` 등과 같은 집계 함수를 적용하여 요약된 통계치를 계산합니다. 본 슬라이드에서는 `sum()` 함수를 통해 각 그룹의 숫자형 데이터를 합산하는 방법을 다룹니다.
*   **인덱스 처리 (Index Handling)**: `groupby()` 연산의 결과는 기본적으로 그룹화에 사용된 키(컬럼)를 결과 DataFrame의 인덱스로 설정합니다. 이를 변경하기 위해 `reset_index()` 메서드를 사용하거나 `groupby()` 호출 시 `as_index=False` 파라미터를 설정할 수 있습니다.
*   **숫자형 컬럼만 집계**: `sum()`과 같은 숫자형 집계 함수는 기본적으로 DataFrame 내의 숫자형(numeric) 컬럼에만 적용되며, 문자열과 같은 비(非)숫자형 컬럼은 자동으로 제외됩니다.

**코드/수식 해설**:

```python
import pandas as pd

# 원본 DataFrame 생성 예시
data = {
    'client': ['John', 'Silvia', 'Andrew'],
    'product': ['bananas', 'oranges', 'bananas'],
    'quantity': [5, 3, 4]
}
df = pd.DataFrame(data)

print("원본 DataFrame df:")
print(df)
print("-" * 30)

# 1. 'product' 컬럼을 기준으로 그룹화하고 'quantity' 컬럼을 합산
# 결과 DataFrame의 인덱스가 그룹화 키('product')로 설정됩니다.
result_1 = df.groupby('product').sum()
print("df.groupby('product').sum():")
print(result_1)
print("-" * 30)

# 2. 위 결과에 .reset_index()를 적용하여 인덱스를 재설정하고 'product'를 일반 컬럼으로 변환
result_2 = df.groupby('product').sum().reset_index()
print("df.groupby('product').sum().reset_index():")
print(result_2)
print("-" * 30)

# 3. 'product' 컬럼으로 그룹화할 때, 처음부터 'product'를 인덱스로 만들지 않고 일반 컬럼으로 유지
# 'as_index=False' 파라미터를 사용합니다.
result_3 = df.groupby('product', as_index=False).sum()
print("df.groupby('product', as_index=False).sum():")
print(result_3)
print("-" * 30)
```
본 슬라이드에서 다루는 내용은 데이터 집계 및 변환에 중점을 두며, 직접적인 수학적 수식은 포함되지 않습니다. Pandas의 `groupby` 및 `sum` 연산은 내부적으로 각 그룹의 원소들을 합하는 연산을 수행합니다. 예를 들어, 특정 그룹 $G_k$에 속하는 값들의 집합이 $\{x_1, x_2, \ldots, x_n\}$일 때, `sum()` 연산은 $\sum_{i=1}^n x_i$를 계산합니다.

**구체적 예시**:
어떤 온라인 쇼핑몰의 일일 주문 데이터를 `df` DataFrame으로 가지고 있다고 상상해 봅시다.
*   `client`: 주문한 고객의 이름
*   `product`: 주문된 상품의 종류
*   `quantity`: 주문된 상품의 수량

`df.groupby('product').sum()`을 사용하면 각 상품 종류별로 총 몇 개의 상품이 판매되었는지 쉽게 파악할 수 있습니다. 예를 들어, 'bananas' 상품은 'John'이 5개, 'Andrew'가 4개 주문하여 총 9개가 판매되었고, 'oranges' 상품은 'Silvia'가 3개 주문하여 총 3개가 판매된 것을 확인할 수 있습니다.

이때 첫 번째 결과처럼 'product'가 인덱스로 되어 있으면 데이터를 추가로 분석하거나 다른 DataFrame과 병합할 때 불편할 수 있습니다. 이때 `.reset_index()`를 사용하거나 `as_index=False` 옵션을 주어 상품명('product')을 일반 데이터 컬럼으로 만들면 다른 컬럼들과 동일하게 취급하며 유연하게 활용할 수 있습니다.

**시험 포인트**:
*   ⭐ `groupby()` 메서드의 기본 사용법과 데이터 집계(aggregation)에서의 역할(특히 `sum()`)을 정확히 이해하고 있어야 합니다.
*   ⭐ `groupby()` 연산 후 그룹화 키(key)가 결과 DataFrame의 인덱스로 설정되는 기본 동작을 숙지해야 합니다.
*   ⭐ 그룹화 키를 인덱스가 아닌 일반 컬럼으로 유지하는 두 가지 핵심 방법: `df.groupby(...).sum().reset_index()` 와 `df.groupby(..., as_index=False).sum()`의 차이점과 각각의 사용 시나리오를 명확히 구분할 수 있어야 합니다.
*   ⭐ `sum()`과 같은 집계 함수가 숫자형 컬럼에만 적용되며, 다른 타입의 컬럼은 자동으로 제외된다는 점을 기억해야 합니다.

---

## Slide 23

### 핵심 개념
`pandas`의 `groupby()` 연산은 데이터를 특정 기준으로 그룹화한 후, 각 그룹에 대해 집계(aggregation) 함수를 적용할 때 사용됩니다. 이때, 그룹화된 데이터에서 특정 컬럼(들)만 선택하여 집계하는 방법과 그 결과물의 형태(Series 또는 DataFrame)를 이해하는 것이 중요합니다.

1.  **모든 숫자형 컬럼 집계**: `groupby()` 후 별도의 컬럼 선택 없이 집계 함수(예: `sum()`)를 적용하면, 그룹화 키를 제외한 모든 숫자형 컬럼에 대해 집계가 수행됩니다. 결과는 `DataFrame`입니다.
2.  **단일 컬럼 선택 및 집계 (Attribute Access / Single-bracket)**: `groupby()` 결과에 대해 `.컬럼명` (Attribute Access) 또는 `['컬럼명']` (Single-bracket indexing)을 사용하여 단일 컬럼을 선택하고 집계 함수를 적용하면, 해당 컬럼에 대해서만 집계가 수행되며 결과는 `pandas.Series` 객체가 됩니다.
3.  **여러 컬럼 선택 및 집계 (Double-bracket)**: `groupby()` 결과에 대해 `[['컬럼1', '컬럼2']]` (Double-bracket indexing)를 사용하여 여러 컬럼을 리스트 형태로 선택하고 집계 함수를 적용하면, 선택된 컬럼들에 대해서만 집계가 수행되며 결과는 항상 `pandas.DataFrame` 객체가 됩니다.

### 코드/수식 해설

초기 데이터프레임 `df` 예시:

```python
import pandas as pd

data = {
    'client': ['John', 'Silvia', 'Andrew'],
    'product': ['bananas', 'oranges', 'bananas'],
    'quantity': [5, 3, 4],
    'price': [2, 5, 3],
    'total': [10, 15, 12]
}
df = pd.DataFrame(data)
print("Original DataFrame df:\n", df)
```

1.  **모든 숫자형 컬럼 집계:**
    `df.groupby('product').sum()`
    -   `df.groupby('product')`: 'product' 컬럼을 기준으로 데이터를 그룹화합니다.
    -   `.sum()`: 각 그룹에 대해 모든 숫자형 컬럼(`quantity`, `price`, `total`)의 합계를 계산합니다.
    -   **결과 타입**: `pandas.DataFrame`

    ```python
    result_all_numeric = df.groupby('product').sum()
    print("\n1. All numeric columns aggregated (DataFrame):\n", result_all_numeric)
    ```

2.  **단일 컬럼 선택 및 집계 (Attribute Access):**
    `df.groupby('product').quantity.sum()`
    -   `df.groupby('product')`: 'product' 컬럼을 기준으로 그룹화합니다.
    -   `.quantity`: 그룹화된 객체에서 'quantity' 컬럼을 선택합니다 (Attribute Access).
    -   `.sum()`: 선택된 'quantity' 컬럼의 각 그룹별 합계를 계산합니다.
    -   **결과 타입**: `pandas.Series`

    ```python
    result_single_column_series = df.groupby('product').quantity.sum()
    print("\n2. Single column 'quantity' aggregated (Series):\n", result_single_column_series)
    print("Type of result_single_column_series:", type(result_single_column_series))
    ```

3.  **여러 컬럼 선택 및 집계 (Double-bracket indexing):**
    `df.groupby('product')[['quantity', 'total']].sum()`
    -   `df.groupby('product')`: 'product' 컬럼을 기준으로 그룹화합니다.
    -   `[['quantity', 'total']]`: 그룹화된 객체에서 'quantity'와 'total' 두 컬럼을 선택합니다 (Double-bracket indexing).
    -   `.sum()`: 선택된 두 컬럼의 각 그룹별 합계를 계산합니다.
    -   **결과 타입**: `pandas.DataFrame`

    ```python
    result_multi_column_dataframe = df.groupby('product')[['quantity', 'total']].sum()
    print("\n3. Multiple columns 'quantity', 'total' aggregated (DataFrame):\n", result_multi_column_dataframe)
    print("Type of result_multi_column_dataframe:", type(result_multi_column_dataframe))
    ```

### 구체적 예시
여러분들이 편의점에서 물건을 구매한다고 상상해 봅시다.

*   `df`: 오늘 하루 동안 편의점에서 팔린 모든 물건의 판매 기록 (어떤 고객이, 어떤 상품을, 몇 개, 개당 얼마, 총 얼마에 샀는지)
*   **`df.groupby('product').sum()`**:
    "오늘 팔린 상품들을 종류별로 묶어서, 각 상품 종류별로 총 몇 개가 팔렸고(quantity), 개당 가격의 총합은 얼마이며(price), 총 매출액은 얼마인지(total) 한눈에 보고 싶다!"
    -> 모든 숫자형 정보를 합산하여 보여줍니다.
*   **`df.groupby('product').quantity.sum()`**:
    "오늘 팔린 상품들을 종류별로 묶어서, 특히 **몇 개**가 팔렸는지만 알고 싶다!"
    -> 'quantity' 컬럼만 딱 뽑아서 그 합계를 보여줍니다. 결과는 상품 종류와 수량의 짝으로 이루어진 리스트(Series) 형태입니다.
*   **`df.groupby('product')[['quantity', 'total']].sum()`**:
    "오늘 팔린 상품들을 종류별로 묶어서, **몇 개**가 팔렸는지와 **총 매출액**이 얼마인지 알고 싶다!"
    -> 'quantity'와 'total' 컬럼만 뽑아서 그 합계를 보여줍니다. 결과는 여러 개의 컬럼을 가진 표(DataFrame) 형태입니다.

### 시험 포인트

*   ⭐ `groupby()` 연산 후 컬럼 선택 방식에 따라 결과물의 타입(`pandas.Series` vs. `pandas.DataFrame`)이 달라진다는 점을 정확히 이해하고 있어야 합니다.
    *   **단일 컬럼 선택 (`.col` 또는 `['col']`)** → `Series`
    *   **다중 컬럼 선택 (`[['col1', 'col2']]`)** → `DataFrame`
    *   **컬럼 선택 없음** → `DataFrame` (모든 숫자형 컬럼 집계)
*   ⭐ Attribute Access (`.quantity`)와 List of column names (`[['quantity']]`)를 통한 단일 컬럼 선택의 차이점을 묻는 문제가 출제될 수 있습니다. 전자는 Series를 반환하고, 후자는 (단일 컬럼을 선택했더라도) DataFrame을 반환합니다. 이 슬라이드에서는 단일 컬럼 선택에 Attribute Access (`.quantity`)만 다루고 있지만, `df.groupby('product')['quantity'].sum()` 역시 Series를 반환한다는 점을 함께 기억하세요.
*   주어진 시나리오에서 특정 정보를 추출하기 위해 어떤 `groupby()` 및 컬럼 선택 조합을 사용해야 하는지 코드로 작성하는 문제가 나올 수 있습니다.

---

## Slide 24

**핵심 개념**
`pandas`의 `groupby()`와 `agg()` 메서드를 조합하여 데이터프레임을 그룹화하고, 각 그룹에 대해 여러 컬럼에 다양한 집계(aggregation) 함수를 적용하는 기법입니다. "Named Aggregations"는 특히 `agg()` 메서드에 딕셔너리 형태의 인자를 전달하여 특정 컬럼에 특정 집계 함수를 명시적으로 적용하고, 결과 컬럼에 의미 있는 이름을 부여하는 방식을 의미합니다. 이를 통해 한 번의 연산으로 여러 컬럼에 대한 복합적인 통계 요약을 수행할 수 있습니다.

**코드/수식 해설**
주어진 코드는 `df` 데이터프레임을 `product` 컬럼을 기준으로 그룹화한 후, 각 그룹에 대해 `quantity` 컬럼은 합계('sum')를, `price` 컬럼은 평균('mean')을 계산하도록 지시합니다.

```python
df.groupby('product').agg({'quantity': 'sum', 'price': 'mean'})
```

*   `df.groupby('product')`: 데이터프레임 `df`를 `product` 컬럼의 고유 값(예: 'bananas', 'oranges')을 기준으로 여러 그룹으로 나눕니다.
*   `.agg({'quantity': 'sum', 'price': 'mean'})`: 그룹화된 각 서브 데이터프레임에 대해 집계 함수를 적용합니다.
    *   `'quantity': 'sum'`: `quantity` 컬럼의 모든 값을 합산합니다.
        *   수식으로 표현하자면, 특정 그룹 내 `quantity` 값 $q_1, q_2, \ldots, q_n$ 에 대해 합계는 다음과 같습니다:
            $$ \text{Sum}(q) = \sum_{i=1}^{n} q_i $$
    *   `'price': 'mean'`: `price` 컬럼의 모든 값에 대한 평균을 계산합니다.
        *   수식으로 표현하자면, 특정 그룹 내 `price` 값 $p_1, p_2, \ldots, p_m$ 에 대해 평균은 다음과 같습니다:
            $$ \text{Mean}(p) = \frac{1}{m} \sum_{j=1}^{m} p_j $$
이 방식은 `agg()`에 딕셔너리를 전달하여 어떤 원본 컬럼에 어떤 집계 함수를 적용할지 명확히 지정할 수 있게 해줍니다.

**구체적 예시**
원본 `df` 데이터프레임은 다음과 같습니다:

| client  | product | quantity | price | total |
| :------ | :------ | :------- | :---- | :---- |
| John    | bananas | 5        | 2     | 10    |
| Silvia  | oranges | 3        | 5     | 15    |
| Andrew  | bananas | 4        | 3     | 12    |

1.  **`df.groupby('product')`**: `product` 컬럼을 기준으로 'bananas' 그룹과 'oranges' 그룹으로 나눕니다.
    *   **'bananas' 그룹**:
        *   `quantity`: \[5, 4]
        *   `price`: \[2, 3]
    *   **'oranges' 그룹**:
        *   `quantity`: \[3]
        *   `price`: \[5]

2.  **`.agg({'quantity': 'sum', 'price': 'mean'})`**: 각 그룹에 집계 함수를 적용합니다.
    *   **'bananas' 그룹**:
        *   `quantity`의 합계: $5 + 4 = 9$
        *   `price`의 평균: $(2 + 3) / 2 = 2.5$
    *   **'oranges' 그룹**:
        *   `quantity`의 합계: $3 = 3$
        *   `price`의 평균: $5 = 5.0$

최종 결과는 다음과 같은 데이터프레임이 됩니다:

| product | quantity | price |
| :------ | :------- | :---- |
| bananas | 9        | 2.5   |
| oranges | 3        | 5.0   |

이를 통해 각 제품별 총 판매량과 평균 가격을 한눈에 파악할 수 있습니다.

**시험 포인트**
*   ⭐ `groupby()`와 `agg()` 메서드의 연쇄 사용법은 `pandas`를 이용한 데이터 분석에서 매우 중요합니다.
*   ⭐ `agg()`에 딕셔너리를 전달하여 **여러 컬럼에 대해 서로 다른 집계 함수를 동시에 적용**하는 방법을 정확히 이해하고 있어야 합니다.
*   ⭐ `groupby()`의 인자로 지정된 컬럼은 결과 데이터프레임의 **인덱스**가 됩니다.
*   ⭐ `sum`, `mean`, `count`, `min`, `max`, `std` 등 자주 사용되는 집계 함수의 종류와 그 역할은 필수적으로 암기해야 합니다.

---

## Slide 25

### 핵심 개념

Pandas 라이브러리에서 `groupby()`와 `agg()` 메서드를 조합하여 데이터프레임의 특정 컬럼들을 기준으로 그룹을 나누고, 각 그룹에 대해 **여러 가지 집계 함수를 동시에 적용**하는 방법을 설명합니다. 특히, **하나의 컬럼에 대해 여러 개의 집계 함수를 한 번에 적용**할 수 있는 강력한 기능에 초점을 맞춥니다.

### 코드/수식 해설

`df.groupby('product').agg({'quantity': 'sum', 'price': ['mean', 'max']})`

이 코드는 다음과 같은 단계를 거쳐 데이터를 집계합니다:

1.  **`df.groupby('product')`**: `df` 데이터프레임을 `'product'` 컬럼의 고유한 값(예: 'bananas', 'oranges')을 기준으로 그룹화합니다.
2.  **`.agg({...})`**: 그룹화된 각 서브 데이터프레임에 대해 딕셔너리에 명시된 집계 연산을 수행합니다.
    *   `'quantity': 'sum'`: `'quantity'` 컬럼에 대해 각 그룹의 합계(sum)를 계산합니다.
    *   `'price': ['mean', 'max']`: `'price'` 컬럼에 대해 각 그룹의 평균(mean)과 최댓값(max)을 동시에 계산합니다. 여러 집계 함수를 적용할 때는 함수의 이름을 리스트 형태로 제공합니다.

이 연산의 결과는 컬럼에 `MultiIndex` (계층적 인덱스)가 적용된 새로운 데이터프레임입니다. 예를 들어, `'price'` 컬럼 아래에 `'mean'`과 `'max'`가 하위 인덱스로 생성됩니다. 필요에 따라 `map`이나 리스트 컴프리헨션 등을 사용하여 이 `MultiIndex`를 단일 레벨의 컬럼명으로 평탄화(flatten)할 수 있습니다.

### 구체적 예시

다음은 실제 데이터를 사용하여 위 코드가 어떻게 동작하는지 보여주는 예시입니다.

```python
import pandas as pd

# 원본 DataFrame 생성
data = {
    'product': ['bananas', 'oranges', 'bananas', 'bananas', 'oranges'],
    'quantity': [5, 2, 2, 2, 1],
    'price': [2.0, 5.0, 3.0, 2.5, 5.0]
}
df = pd.DataFrame(data)

print("원본 DataFrame:")
print(df)
print("-" * 30)

# 'product'별로 'quantity'는 합계, 'price'는 평균과 최댓값 집계
aggregated_df = df.groupby('product').agg({'quantity': 'sum', 'price': ['mean', 'max']})

print("집계 결과 DataFrame (MultiIndex 컬럼):")
print(aggregated_df)
print("-" * 30)

# MultiIndex 컬럼 평탄화 예시 (선택 사항)
# 각 레벨의 컬럼 이름을 조합하여 새로운 컬럼 이름 생성
aggregated_df.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in aggregated_df.columns.values]
# 또는 다음과 같이 명시적으로 rename할 수도 있습니다.
# aggregated_df.columns = ['quantity_sum', 'price_mean', 'price_max'] # 예시 출력에 맞춰 수동 명명

print("컬럼 평탄화 후 DataFrame:")
print(aggregated_df)
```

**실행 결과:**

```
원본 DataFrame:
   product  quantity  price
0  bananas         5    2.0
1  oranges         2    5.0
2  bananas         2    3.0
3  bananas         2    2.5
4  oranges         1    5.0
------------------------------
집계 결과 DataFrame (MultiIndex 컬럼):
          quantity  price      
               sum   mean  max
product                        
bananas          9   2.50  3.0
oranges          3   5.00  5.0
------------------------------
컬럼 평탄화 후 DataFrame:
         quantity_sum  price_mean  price_max
product                                     
bananas             9        2.50        3.0
oranges             3        5.00        5.0
```

*   'bananas' 그룹: quantity = 5+2+2=9, price mean = (2.0+3.0+2.5)/3 = 2.5, price max = 3.0
*   'oranges' 그룹: quantity = 2+1=3, price mean = (5.0+5.0)/2 = 5.0, price max = 5.0

### 시험 포인트

*   ⭐ **`groupby()`와 `agg()`의 역할**: 데이터 분석에서 특정 기준에 따른 그룹별 통계 계산은 매우 중요하며, `groupby()`로 그룹을 나누고 `agg()`로 집계하는 패턴은 필수적입니다.
*   ⭐ **`agg()` 메서드의 딕셔너리 사용법**: `{컬럼명: 함수명}` 또는 `{컬럼명: [함수명1, 함수명2, ...]}` 형태를 사용하여 여러 컬럼에 대해 다른 집계 함수를 적용하거나, 한 컬럼에 대해 여러 집계 함수를 동시에 적용하는 방법을 정확히 이해해야 합니다.
*   ⭐ **결과 DataFrame의 MultiIndex 컬럼**: `agg()`로 여러 집계 함수를 적용하면 결과 데이터프레임의 컬럼이 `MultiIndex` 구조가 된다는 점을 기억하고, 필요시 이를 평탄화(flatten)하는 방법을 알아야 합니다.

---

## Slide 26

**핵심 개념**

Pandas `groupby().agg()`의 **Named Aggregations**는 그룹별 집계(aggregation)를 수행할 때 출력 컬럼의 이름을 직접 지정하여 `MultiIndex` (계층적 컬럼)를 피하고 "평평한(flat)" 단일 레벨 컬럼 구조를 얻는 방법입니다. 이는 집계된 결과를 더 깔끔하고 다루기 쉽게 만들어줍니다.

**코드/수식 해설**

첨부된 슬라이드의 코드는 `DataFrame` `df`를 'product' 컬럼을 기준으로 그룹화한 후, 각 그룹에 대해 여러 가지 집계 연산을 수행하는 방법을 보여줍니다.

```python
df.groupby('product').agg(
    quantity=('quantity', 'sum'),
    min_price=('price', 'min'),
    max_price=('price', 'max')
)
```

1.  `df.groupby('product')`: `DataFrame` `df`를 'product' 컬럼의 고유한 값(예: 'bananas', 'oranges')을 기준으로 그룹으로 나눕니다.
2.  `.agg(...)`: 그룹화된 객체에 대해 집계(aggregation) 연산을 적용합니다. 여기서는 `named-agg` 문법을 사용합니다.
    *   `새_컬럼_이름=('원본_컬럼_이름', '집계_함수_이름')` 형식으로 작성합니다.
    *   `quantity=('quantity', 'sum')`: 'quantity'라는 새 컬럼을 만듭니다. 이 컬럼의 값은 각 그룹의 'quantity' 컬럼 값들의 합계($\sum$)입니다.
    *   `min_price=('price', 'min')`: 'min_price'라는 새 컬럼을 만듭니다. 이 컬럼의 값은 각 그룹의 'price' 컬럼 값들 중 최솟값($\min$)입니다.
    *   `max_price=('price', 'max')`: 'max_price'라는 새 컬럼을 만듭니다. 이 컬럼의 값은 각 그룹의 'price' 컬럼 값들 중 최댓값($\max$)입니다.

**구체적 예시**

다음과 같은 가상의 쇼핑 데이터 `DataFrame`이 있다고 가정해 봅시다.

```python
import pandas as pd

data = {
    'product': ['bananas', 'oranges', 'bananas', 'oranges', 'bananas'],
    'quantity': [5, 2, 4, 1, 0],
    'price': [3, 5, 2, 5, 1]
}
df = pd.DataFrame(data)
print("원본 DataFrame:")
print(df)
```

```
원본 DataFrame:
   product  quantity  price
0  bananas         5      3
1  oranges         2      5
2  bananas         4      2
3  oranges         1      5
4  bananas         0      1
```

이제 슬라이드의 `named-agg` 코드를 적용해 봅시다.

```python
aggregated_df = df.groupby('product').agg(
    quantity=('quantity', 'sum'),
    min_price=('price', 'min'),
    max_price=('price', 'max')
)
print("\nNamed Aggregations 결과 DataFrame:")
print(aggregated_df)
```

```
Named Aggregations 결과 DataFrame:
         quantity  min_price  max_price
product                              
bananas         9          1          3
oranges         3          5          5
```

*   `bananas` 그룹:
    *   quantity: 5 + 4 + 0 = 9
    *   price: min(3, 2, 1) = 1
    *   price: max(3, 2, 1) = 3
*   `oranges` 그룹:
    *   quantity: 2 + 1 = 3
    *   price: min(5, 5) = 5
    *   price: max(5, 5) = 5

결과 `DataFrame`의 컬럼 이름('quantity', 'min_price', 'max_price')이 우리가 지정한 이름으로 '평평하게' 구성되었음을 확인할 수 있습니다.

**시험 포인트**

*   ⭐ **Named Aggregations의 목적**: `groupby().agg()` 사용 시 `MultiIndex` 컬럼이 생성되는 것을 방지하고, 출력 컬럼 이름을 사용자가 직접 명시하여 **깔끔하고 평평한(flat) 컬럼 구조**를 얻기 위함입니다.
*   ⭐ **Named Aggregations 문법**: `새_컬럼_이름=('원본_컬럼_이름', '집계_함수_이름')` 형식을 정확히 이해하고 사용할 수 있어야 합니다. (예: `total_sales=('sales', 'sum')`)
*   여러 컬럼에 대해 동시에 다른 집계 함수를 적용하고, 각 결과에 고유한 이름을 부여하는 방법을 알고 있어야 합니다.
*   `'sum'`, `'min'`, `'max'`, `'mean'`, `'std'`, `'count'` 등 자주 사용되는 집계 함수들을 숙지하고 있어야 합니다.

---

## Slide 27

**핵심 개념**:
*   `groupby().apply()`는 pandas에서 데이터프레임을 특정 컬럼으로 그룹화한 후, 각 그룹에 **사용자 정의 함수(custom function)**를 적용하여 복잡한 집계(aggregation) 또는 변환(transformation)을 수행할 때 사용되는 메서드입니다.
*   `apply()` 메서드는 특히 `agg()` 메서드에서 제공하는 내장 집계 함수(예: `mean`, `sum`, `count`)만으로는 표현하기 어려운, 그룹별로 특별한 계산 로직이 필요할 때 유용합니다.
*   `apply()`에 전달되는 함수는 각 그룹의 하위 DataFrame을 입력(`x`)으로 받아 처리하며, 그 결과는 그룹 키(group key)를 인덱스로 하는 Series 형태로 반환됩니다.

**코드/수식 해설**:

주어진 코드는 `product`별로 **가중 평균 가격(weighted mean price)**을 계산합니다.

```python
df.groupby('product').apply(lambda x: x.total.sum()/x.quantity.sum())
```

*   `df.groupby('product')`: `df` DataFrame을 'product' 컬럼을 기준으로 그룹화합니다. 이 과정에서 'bananas' 그룹과 'oranges' 그룹이 생성됩니다.
*   `.apply(lambda x: ...)`: 그룹화된 각 부분 DataFrame (`x`)에 람다 함수를 적용합니다. 이 `x`는 'bananas' 또는 'oranges' 그룹에 해당하는 데이터프레임의 일부가 됩니다.
*   `x.total.sum()`: 현재 그룹 (`x`) 내에서 'total' 컬럼의 합계를 계산합니다. 'total' 컬럼은 `quantity * price`이므로, 이는 해당 그룹의 총 판매액을 의미합니다.
*   `x.quantity.sum()`: 현재 그룹 (`x`) 내에서 'quantity' 컬럼의 합계를 계산합니다. 이는 해당 그룹의 총 판매 수량을 의미합니다.
*   `x.total.sum()/x.quantity.sum()`: 총 판매액을 총 판매 수량으로 나누어 해당 그룹(제품)의 가중 평균 가격을 계산합니다.

수식으로 표현하면, 특정 제품 $P$에 대한 가중 평균 가격은 다음과 같습니다.
$$ \text{Weighted Mean Price}_P = \frac{\sum_{i \in P} (\text{quantity}_i \times \text{price}_i)}{\sum_{i \in P} \text{quantity}_i} = \frac{\sum_{i \in P} \text{total}_i}{\sum_{i \in P} \text{quantity}_i} $$
여기서 $i$는 제품 $P$에 속하는 각 개별 판매 기록을 나타냅니다.

**구체적 예시**:

원본 DataFrame `df`가 다음과 같다고 가정합니다.

| client | product | quantity | price | total |
| :----- | :------ | :------- | :---- | :---- |
| John   | bananas | 5        | 2     | 10    |
| Silvia | oranges | 3        | 5     | 15    |
| Andrew | bananas | 4        | 3     | 12    |

1.  **`df.groupby('product')`**:
    *   'bananas' 그룹:
        | client | product | quantity | price | total |
        | :----- | :------ | :------- | :---- | :---- |
        | John   | bananas | 5        | 2     | 10    |
        | Andrew | bananas | 4        | 3     | 12    |
    *   'oranges' 그룹:
        | client | product | quantity | price | total |
        | :----- | :------ | :------- | :---- | :---- |
        | Silvia | oranges | 3        | 5     | 15    |

2.  **`apply(lambda x: x.total.sum()/x.quantity.sum())`**:
    *   **'bananas' 그룹**:
        *   총 판매액 (`x.total.sum()`) = $10 + 12 = 22$
        *   총 수량 (`x.quantity.sum()`) = $5 + 4 = 9$
        *   가중 평균 가격 = $22 / 9 \approx 2.4444...$
    *   **'oranges' 그룹**:
        *   총 판매액 (`x.total.sum()`) = $15$
        *   총 수량 (`x.quantity.sum()`) = $3$
        *   가중 평균 가격 = $15 / 3 = 5.0$

최종 결과는 다음과 같은 Series로 반환됩니다.

| product |      |
| :------ | :--- |
| bananas | 2.44 |
| oranges | 5.0  |

**시험 포인트**:

*   ⭐ `groupby().apply()`는 `groupby().agg()`로 표현하기 어려운 **사용자 정의된 복잡한 집계 또는 변환 로직**을 구현할 때 사용합니다.
*   ⭐ `apply()` 메서드에 전달되는 람다 함수의 인자 `x`는 각 그룹의 **부분 DataFrame**을 의미하며, 이 `x`를 통해 그룹 내의 모든 컬럼에 접근하여 연산을 수행할 수 있습니다.
*   ⭐ `apply()`의 결과는 기본적으로 그룹 키(이 예시에서는 'product')로 인덱싱된 **Series**로 반환됩니다.
*   ⭐ **성능 주의**: 만약 계산하려는 집계가 `agg()`에서 제공하는 내장 함수(예: `mean`, `sum`, `std`)나 간단한 컬럼 연산으로 표현 가능하다면, `apply()`보다 `agg()`를 사용하는 것이 **성능 면에서 더 효율적**입니다. `apply()`는 유연성이 높지만, 내부적으로 파이썬 루프를 사용하기 때문에 대규모 데이터 처리 시 속도 저하가 발생할 수 있습니다.
*   ⭐ **가중 평균의 개념**: 총 판매액의 합을 총 판매 수량의 합으로 나누는 방식으로 가중 평균을 계산하는 원리를 이해해야 합니다.

---

## Slide 28

## Groupby: 내장 함수와 람다 혼용

### 핵심 개념

*   **`groupby().agg()` 활용**: `pandas`의 `groupby` 연산 후 `agg` 메서드를 사용하여 여러 집계(aggregation) 함수를 동시에 적용할 수 있습니다. 이는 데이터프레임의 특정 컬럼에 대해 여러 통계량(예: 합계, 평균, 최대값 등)을 한 번에 계산할 때 유용합니다.
*   **내장 함수와 람다 함수 혼용**: `agg` 메서드 내에서 `sum`, `mean`과 같은 pandas/numpy의 **내장 집계 함수**와 사용자가 직접 정의하는 **람다(lambda) 함수**를 함께 사용할 수 있습니다. 이를 통해 표준적인 집계뿐만 아니라 특정 조건에 따른 맞춤형 집계 로직을 구현할 수 있습니다.
*   **람다 함수 내 그룹 키 접근**: `groupby` 후 `agg`에 전달되는 람다 함수 `x`는 각 그룹의 `Series` 또는 `DataFrame` 객체입니다. 이 `x` 객체의 `.name` 속성을 통해 현재 처리 중인 그룹의 키(label)에 접근할 수 있습니다. 이는 조건부 로직을 작성할 때 매우 중요합니다.

### 코드/수식 해설

슬라이드의 코드는 `product`별로 그룹화한 후 `total` 열에 대해 두 가지 다른 집계 연산을 수행합니다.

```python
df.set_index('product').groupby('product').agg(total=('total', 'sum'),
                                             fixed_total=('total', lambda x: x.sum()/2 if x.index[0]=='bananas' else x.sum()))
```
1.  `df.set_index('product')`: `product` 열을 데이터프레임의 인덱스로 설정합니다. (이 슬라이드에서는 `groupby('product')`와 함께 사용되었으므로 이 `set_index` 부분은 기능적으로 반드시 필요한 것은 아닙니다. `groupby('product')`만으로도 동일하게 그룹화됩니다.)
2.  `groupby('product')`: 'product' 열의 고유한 값('bananas', 'oranges')을 기준으로 데이터를 그룹으로 나눕니다.
3.  `.agg(...)`: 그룹별로 여러 집계 연산을 수행합니다.
    *   `total=('total', 'sum')`: 'total'이라는 새로운 열을 생성하고, 각 그룹의 원본 'total' 열에 대해 `sum` (합계) 연산을 적용합니다.
    *   `fixed_total=('total', lambda x: x.sum()/2 if x.index[0]=='bananas' else x.sum())`: 'fixed_total'이라는 새로운 열을 생성하고, 각 그룹의 원본 'total' 열에 대해 사용자 정의 람다 함수를 적용합니다.
        *   `lambda x`: 각 그룹의 'total' 열에 해당하는 `Series` 객체가 `x`로 전달됩니다.
        *   `x.sum()/2 if x.index[0]=='bananas' else x.sum()`: 이 조건문은 `x`가 속한 그룹의 첫 번째 인덱스(여기서는 그룹 키와 일치)가 'bananas'이면 해당 그룹의 합계를 2로 나누고, 그렇지 않으면 원래 합계를 그대로 사용합니다.

```python
df.groupby('product').agg(total=('total', 'sum'),
                         fixed_total=('total', lambda x: x.sum()/2 if x.name=='bananas' else x.sum()))
```
이 코드는 첫 번째 코드와 거의 동일하지만, `set_index`를 사용하지 않아도 됩니다. 가장 중요한 차이점은 람다 함수 내에서 그룹 키를 참조하는 방식입니다:
*   `x.name=='bananas'`: `lambda` 함수에 전달되는 `Series` `x`의 `.name` 속성은 해당 `Series`가 속한 그룹의 **그룹 키(label)**를 나타냅니다. 예를 들어, 'bananas' 그룹의 경우 `x.name`은 'bananas'가 됩니다. 이 방식은 `x.index[0]`을 사용하는 것보다 더 명확하고 유연하며 "덜 취약(less brittle)"합니다.

### 구체적 예시

주어진 `df` 데이터프레임이 다음과 같다고 가정해 봅시다:

| client | product | quantity | price | total |
| :----- | :------ | :------- | :---- | :---- |
| John   | bananas | 5        | 2     | 10    |
| Silvia | oranges | 3        | 5     | 15    |
| Andrew | bananas | 4        | 3     | 12    |

1.  `groupby('product')`를 수행하면 데이터는 'bananas' 그룹과 'oranges' 그룹으로 나뉩니다.
    *   **'bananas' 그룹**:
        *   total: [10, 12]
    *   **'oranges' 그룹**:
        *   total: [15]
2.  `agg` 함수가 적용됩니다:
    *   **`total=('total', 'sum')`**:
        *   'bananas' 그룹: 10 + 12 = 22
        *   'oranges' 그룹: 15
    *   **`fixed_total=('total', lambda x: x.sum()/2 if x.name=='bananas' else x.sum())`**:
        *   'bananas' 그룹 (`x.name`이 'bananas'이므로 조건 만족): (10 + 12) / 2 = 11.0
        *   'oranges' 그룹 (`x.name`이 'bananas'가 아니므로 조건 불만족): 15

최종 결과 데이터프레임:

| product | total | fixed_total |
| :------ | :---- | :---------- |
| bananas | 22    | 11.0        |
| oranges | 15    | 15.0        |

### 시험 포인트

*   ⭐ **`groupby().agg()`의 다중 집계 기능**: `agg` 메서드를 사용하여 여러 컬럼에 대해 동시에 다른 집계 함수를 적용하거나, 같은 컬럼에 대해 여러 집계 함수를 적용하는 방법을 이해하고 코드로 작성할 수 있어야 합니다. (예: `df.groupby('A').agg(B_sum=('B', 'sum'), C_mean=('C', 'mean'))`)
*   ⭐ **람다 함수를 이용한 커스텀 집계**: `agg` 내에서 `lambda` 함수를 사용하여 특정 조건에 따라 다르게 동작하는 사용자 정의 집계 로직을 구현하는 원리를 숙지해야 합니다. 이는 데이터 분석에서 유연한 집계가 필요할 때 핵심적인 기법입니다.
*   ⭐ **`lambda` 함수 내 그룹 키 접근 (`x.name`)**: 람다 함수에 전달되는 `Series` 또는 `DataFrame` 객체 `x`에서 현재 그룹의 키(label)에 접근하는 방법으로 `x.name`을 사용하는 것을 알고, `x.index[0]`과 같은 다른 방식보다 선호되는 이유(더 견고함)를 설명할 수 있어야 합니다.

---

## Slide 29

**핵심 개념**
데이터를 표현하는 두 가지 주요 형식인 **Wide format (넓은 형식)**과 **Long format (긴 형식)**, 그리고 이 두 형식 간에 데이터를 변환하는 **Pivoting (피벗팅)**에 대한 개념입니다.

*   **Wide Format (넓은 형식)**:
    *   값들이 여러 컬럼에 걸쳐 분산되어 있는 형태입니다.
    *   각 행은 고유한 관측치(observation)의 일부를 나타내며, 다른 변수 값들은 별도의 컬럼으로 표현됩니다.
    *   예시 이미지에서는 `i`가 행 인덱스, `j`의 값들(0, 1, 2)이 각각 별도의 컬럼 헤더가 되고, `a_ij` 값들이 해당 셀에 들어갑니다.
    *   컬럼의 수가 많고 행의 수가 적어지는 경향이 있습니다. 때로는 "short format"이라고도 불립니다.

*   **Long Format (긴 형식)**:
    *   각 관측치가 고유한 한 행을 차지하는 형태입니다.
    *   '키 컬럼(key columns)' (예: `i`, `j`)들이 관측치를 식별하고, 해당 관측치의 '값 컬럼(value column)' (예: `a`)이 별도로 존재합니다.
    *   예시 이미지에서는 `i`, `j`, `a`가 각각 별도의 컬럼으로 존재하며, 각 행은 `(i, j)` 조합에 해당하는 `a` 값을 가집니다.
    *   행의 수가 많고 컬럼의 수가 적어지는 경향이 있습니다.

*   **Pivoting (피벗팅)**:
    *   Wide format과 Long format 간에 데이터를 변환하는 과정을 통칭합니다.
    *   데이터 분석이나 시각화 라이브러리는 특정 형식의 데이터를 더 선호하는 경우가 많으므로, 필요에 따라 형식을 변환하는 것이 중요합니다.

**코드/수식 해설**

데이터 형식을 변환하는 pandas 함수는 다음과 같습니다.

1.  **Wide Format $\rightarrow$ Long Format 변환**:
    *   주로 `pandas.DataFrame.stack()` 또는 `pandas.melt()` 함수를 사용합니다.
    *   `melt()` 함수는 하나 이상의 식별자(identifier) 컬럼을 고정하고, 나머지 컬럼들을 새로운 '변수' 컬럼과 '값' 컬럼으로 변환합니다.

    ```python
    import pandas as pd

    # Wide format DataFrame 예시
    data_wide = {
        'i': [0, 1],
        '0': ['a_00', 'a_10'],
        '1': ['a_01', 'a_11'],
        '2': ['a_02', 'a_12']
    }
    df_wide = pd.DataFrame(data_wide).set_index('i')
    print("--- Wide Format ---")
    print(df_wide)

    # Wide -> Long 변환 (melt 사용)
    # 'i' 컬럼을 식별자로 고정하고, 나머지 컬럼('0', '1', '2')을 'j'라는 새로운 컬럼으로,
    # 그 값들을 'a'라는 새로운 컬럼으로 변환
    df_long_melt = df_wide.reset_index().melt(id_vars=['i'], var_name='j', value_name='a')
    print("\n--- Long Format (melt 결과) ---")
    print(df_long_melt)
    ```

2.  **Long Format $\rightarrow$ Wide Format 변환**:
    *   주로 `pandas.DataFrame.unstack()` 또는 `pandas.DataFrame.pivot()` 함수를 사용합니다.
    *   `pivot()` 함수는 데이터프레임의 특정 컬럼을 새 인덱스, 다른 컬럼을 새 컬럼으로 사용하고, 나머지 컬럼의 값을 채워서 Wide format으로 만듭니다.

    ```python
    import pandas as pd

    # Long format DataFrame 예시 (melt 결과와 유사)
    data_long = {
        'i': [0, 0, 0, 1, 1, 1],
        'j': ['0', '1', '2', '0', '1', '2'],
        'a': ['a_00', 'a_01', 'a_02', 'a_10', 'a_11', 'a_12']
    }
    df_long = pd.DataFrame(data_long)
    print("--- Long Format ---")
    print(df_long)

    # Long -> Wide 변환 (pivot 사용)
    # 'i' 컬럼을 새 인덱스로, 'j' 컬럼을 새 컬럼으로, 'a' 컬럼의 값을 채움
    df_wide_pivot = df_long.pivot(index='i', columns='j', values='a')
    print("\n--- Wide Format (pivot 결과) ---")
    print(df_wide_pivot)
    ```

**구체적 예시**

어떤 학생들의 과목별 점수 데이터가 있다고 가정해 봅시다.

*   **Wide Format (성적표)**:
    각 행은 학생을 나타내고, 각 과목은 별도의 컬럼입니다.
    ```
    학생ID | 국어 | 영어 | 수학
    -------|------|------|------
    101    | 90   | 85   | 92
    102    | 78   | 88   | 95
    ```
    이 형식은 한눈에 학생별 총체적인 성적을 파악하기 좋습니다.

*   **Long Format (데이터베이스 테이블)**:
    각 행은 특정 학생의 특정 과목 점수 하나를 나타냅니다.
    ```
    학생ID | 과목 | 점수
    -------|------|------
    101    | 국어 | 90
    101    | 영어 | 85
    101    | 수학 | 92
    102    | 국어 | 78
    102    | 영어 | 88
    102    | 수학 | 95
    ```
    이 형식은 데이터베이스에 저장하거나, 과목별 평균 점수와 같은 통계량을 계산하거나, 시각화 라이브러리(예: seaborn)에서 특정 과목의 분포를 그릴 때 더 효율적입니다.

**시험 포인트**

*   ⭐**Wide format과 Long format의 정의와 각각의 특징 (장단점)을 명확히 설명할 수 있어야 합니다.** 특히, 컬럼 수와 행 수의 상대적 경향을 이해하는 것이 중요합니다.
*   ⭐**`pandas.melt()`와 `pandas.pivot()` (또는 `stack()`, `unstack()`) 함수를 사용하여 Wide $\leftrightarrow$ Long 변환을 수행하는 방법을 알아야 합니다.** 각 함수의 주요 인자(`id_vars`, `var_name`, `value_name` for `melt`; `index`, `columns`, `values` for `pivot`)의 역할과 사용법을 이해하고 예시 코드 작성이 가능해야 합니다.
*   ⭐**어떤 데이터 분석 또는 시각화 작업에 어떤 형식의 데이터가 더 적합한지 판단할 수 있어야 합니다.** (예: 시계열 분석, 다변량 통계, 특정 라이브러리 요구사항 등)

---

## Slide 30

**핵심 개념**
`pivot` 함수는 데이터를 'long' 형식에서 'wide' 형식으로 재구성하는 데 사용됩니다. 특정 열의 고유 값들을 새로운 열(columns)로 만들고, 다른 열의 값을 이 새로운 열들에 해당하는 데이터로 채워 넣어 DataFrame의 모양을 변환합니다. 이는 데이터 요약을 위한 중요한 전처리 과정 중 하나입니다.

**코드/수식 해설**

```python
df.pivot(index='client', columns='product', values='quantity')
```

*   **`df`**: 피벗할 원본 DataFrame입니다.
*   **`index='client'`**: `client` 열의 고유 값들이 새로운 DataFrame의 행 인덱스(row index)가 됩니다. 즉, 각 클라이언트가 한 행을 차지하게 됩니다.
*   **`columns='product'`**: `product` 열의 고유 값들이 새로운 DataFrame의 열 이름(column names)이 됩니다. 즉, 'bananas'와 'oranges'가 새로운 열로 생성됩니다.
*   **`values='quantity'`**: 새로운 DataFrame의 각 셀을 채울 값으로 `quantity` 열의 값이 사용됩니다. 예를 들어, 'John'이 'bananas'를 구매한 수량인 5가 해당 셀에 들어갑니다.

**구체적 예시**

원본 DataFrame `df`는 다음과 같습니다.

|   | client | product | quantity | price |
|---|--------|---------|----------|-------|
| 0 | John   | bananas | 5        | 1.5   |
| 1 | John   | oranges | 3        | 3.0   |
| 2 | Silvia | bananas | 4        | 2.5   |
| 3 | Silvia | oranges | 2        | 4.0   |

이 `df`에 `df.pivot(index='client', columns='product', values='quantity')`를 적용하면, 다음과 같은 "wide" 형식의 DataFrame이 생성됩니다.

| client | bananas | oranges |
|--------|---------|---------|
| John   | 5       | 3       |
| Silvia | 4       | 2       |

예를 들어, 'John'이 구매한 'bananas'의 수량(5)이 새로운 DataFrame에서 'John' 행과 'bananas' 열이 만나는 지점에 위치하게 됩니다. 이는 각 클라이언트가 어떤 상품을 얼마나 구매했는지를 한눈에 파악하기 쉽게 해줍니다.

**시험 포인트**

*   ⭐ `pivot` 함수는 `long` 형식의 데이터를 `wide` 형식으로 변환하는 데 사용됩니다.
*   ⭐ `index`, `columns`, `values` 파라미터의 역할과 이것이 결과 DataFrame의 구조에 어떻게 반영되는지 정확히 이해해야 합니다.
*   ⭐ `pivot` 함수는 `(index, columns)` 쌍별로 **단 하나의 값만 허용**합니다. 만약 동일한 `(index, columns)` 쌍에 해당하는 데이터가 여러 개(중복) 있다면 `ValueError`를 발생시킵니다. 이런 경우 데이터 집계를 위해서는 `pivot_table` 함수를 사용해야 합니다.

---

## Slide 31

안녕하세요, POSTECH 컴퓨터공학과 전공 튜터입니다.
데이터분석 입문 (CSED226) 강의 자료 중 "Pivoting III: stack (wide → long)" 슬라이드에 대한 마크다운 노트를 작성해 드립니다.

---

### **핵심 개념**

*   **`stack()` 메서드 (Wide to Long)**
    *   `stack()`은 pandas DataFrame의 컬럼(열)들을 새로운 인덱스 레벨(행)로 이동시켜 데이터를 'wide' 형식에서 'long' 형식으로 변환하는 강력한 메서드입니다.
    *   이 작업은 일반적으로 MultiIndex(다중 인덱스)를 가진 `pandas.Series` 객체를 반환합니다.
    *   데이터가 'wide' 형식일 때 특정 컬럼들을 기준으로 그룹화하여 분석하기 어렵거나 시각화에 적합하지 않을 때 `stack()`을 사용하여 'long' 형식으로 변환합니다.

*   **`reset_index()` 메서드 (MultiIndex Series to Tidy DataFrame)**
    *   `stack()`으로 인해 생성된 MultiIndex `Series`를 보다 사용하기 편리한 `pandas.DataFrame` 형태로 복원하는 데 사용됩니다.
    *   인덱스 레벨들을 일반 컬럼으로 변환하고, `Series`의 값을 새로운 컬럼으로 지정하여 깔끔한('tidy') DataFrame을 생성합니다.
    *   `name` 인자를 사용하여 `Series`의 값들이 저장될 새로운 컬럼의 이름을 지정할 수 있습니다.

### **코드/수식 해설**

이 슬라이드에서는 DataFrame의 `stack()` 메서드와 `Series`의 `reset_index()` 메서드를 사용하여 데이터를 변환하는 과정을 보여줍니다.

1.  **초기 Wide 형식 DataFrame (`df`)**:
    초기 데이터는 다음과 같이 'client'를 인덱스로, 'product'를 컬럼으로 가지는 형태입니다.
    ```python
    import pandas as pd

    data = {
        'bananas': [5, 4],
        'oranges': [3, 2]
    }
    df = pd.DataFrame(data, index=['John', 'Silvia'])
    df.index.name = 'client'
    print("Original DataFrame (df):")
    print(df)
    ```
    출력 예시:
    ```
                  bananas  oranges
    client
    John                  5        3
    Silvia                4        2
    ```

2.  **`stack()` 메서드 적용**:
    `df.stack()`은 `df`의 컬럼(`bananas`, `oranges`)을 새로운 인덱스 레벨로 이동시켜 MultiIndex를 가진 `Series` 객체 `s`를 반환합니다.
    ```python
    s = df.stack()
    print("\nResult of df.stack() (Series s):")
    print(s)
    ```
    출력 예시:
    ```
    client  product
    John    bananas    5
            oranges    3
    Silvia  bananas    4
            oranges    2
    dtype: int64
    ```
    여기서 'client'와 'product'가 새로운 인덱스 레벨이 됩니다.

3.  **`reset_index()` 메서드 적용**:
    `s.reset_index(name='quantity')`는 MultiIndex `Series` `s`의 인덱스 레벨('client', 'product')을 일반 컬럼으로 변환하고, `Series`의 값들을 'quantity'라는 이름의 새로운 컬럼으로 지정하여 최종 'long' 형식의 DataFrame을 생성합니다.
    ```python
    df_long = s.reset_index(name='quantity')
    print("\nResult of s.reset_index(name='quantity') (DataFrame df_long):")
    print(df_long)
    ```
    출력 예시:
    ```
      client  product  quantity
    0   John  bananas         5
    1   John  oranges         3
    2  Silvia  bananas         4
    3  Silvia  oranges         2
    ```

### **구체적 예시**

슬라이드의 예시는 **고객별 과일 구매 수량** 데이터를 다루고 있습니다.

*   **초기 'wide' 형식 (`df`)**: 'John'과 'Silvia'라는 고객이 각각 구매한 'bananas'와 'oranges'의 수량이 각 컬럼에 나열되어 있습니다. 이 형식은 특정 고객의 총 구매액을 보거나, 한 번에 두 과일 종류를 비교할 때는 직관적일 수 있습니다.
    *   예: John은 바나나 5개, 오렌지 3개를 구매했습니다.

*   **`stack()` 적용 후 `Series` (`s`)**: 이 데이터를 `stack()` 하면, 각 고객-과일 조합이 하나의 인덱스 엔트리로 바뀌고 해당 구매 수량이 값으로 들어갑니다.
    *   예: `(John, bananas): 5`, `(John, oranges): 3`

*   **`reset_index()` 적용 후 'long' 형식 (`df_long`)**: 마지막으로 `reset_index()`를 통해 고객('client'), 과일('product'), 수량('quantity') 세 개의 컬럼을 가진 깔끔한 'long' 형식의 DataFrame을 얻게 됩니다. 이 'long' 형식은 다음과 같은 분석 작업에 매우 유리합니다.
    *   **특정 과일의 총 판매량 계산**: `df_long.groupby('product')['quantity'].sum()`
    *   **가장 많이 구매한 과일 찾기**: `df_long.groupby('product')['quantity'].sum().idxmax()`
    *   **Pandas나 Matplotlib, Seaborn 등을 이용한 시각화**: 'product' 컬럼을 x축으로, 'quantity' 컬럼을 y축으로 사용하여 막대 그래프를 그릴 때 등.

이처럼 'wide' 데이터를 'long' 데이터로 변환함으로써, 데이터 분석 및 시각화 라이브러리와의 호환성이 높아지고, 다양한 통계적 분석을 수행하기 더 편리해집니다.

### **시험 포인트**

*   ⭐ **`df.stack()`의 역할과 결과 형태를 정확히 이해해야 합니다.** 'wide' 형식의 DataFrame 컬럼이 MultiIndex를 가진 `Series`로 변환되는 과정과 그 목적(분석 용이성)을 설명할 수 있어야 합니다.
*   ⭐ **`s.reset_index(name='value_column_name')`의 사용법과 목적을 알아야 합니다.** `stack()`으로 생성된 `Series`를 어떻게 다시 'tidy'한 DataFrame으로 복원하는지, 그리고 `name` 인자의 역할을 이해해야 합니다.
*   ⭐ **'wide' 형식과 'long' 형식 데이터의 차이점 및 각각의 장단점, 그리고 언제 `stack()`과 같은 변환이 필요한지 설명할 수 있어야 합니다.** 특히 머신러닝 모델 학습이나 통계 분석 라이브러리(예: `scikit-learn`)는 종종 'long' 형식 데이터를 선호한다는 점을 기억하세요.
*   ⭐ **`stack()`은 컬럼을 인덱스로, `unstack()`은 인덱스를 컬럼으로 변환하는 서로 반대되는 작업임을 인지하고 있어야 합니다.** (이 슬라이드에서는 `stack`만 다루지만, 관련 개념으로 함께 이해해두면 좋습니다.)

---

## Slide 32

---
**핵심 개념**

*   **melt**: pandas 라이브러리의 `melt` 함수는 데이터프레임을 "wide(넓은)" 형식에서 "long(긴)" 형식으로 변환하는 데 사용됩니다. 이는 여러 열에 걸쳐 분포된 값들을 단일 열로 모으고, 원래의 열 이름은 새로운 식별자 열의 값으로 변환합니다. 데이터 분석 및 머신러닝에서 특정 형식의 데이터 처리에 유용하며, 특히 관계형 데이터베이스의 정규화된 형태와 유사하게 만듭니다.

**코드/수식 해설**

*   **`df.reset_index()`**:
    *   데이터프레임 `df`의 인덱스를 일반 열로 변환하고, 새로운 기본(0부터 시작하는 정수) 인덱스를 생성합니다. `melt` 함수는 보통 식별자(id) 열이 인덱스가 아닌 일반 열로 존재할 때 더 직관적으로 사용될 수 있습니다.

    ```python
    # 초기 df (client가 인덱스인 상태)
    #           bananas  oranges
    # client
    # John            5        3
    # Silvia          4        2

    # df.reset_index() 적용 후 df1
    #    client  bananas  oranges
    # 0    John        5        3
    # 1  Silvia        4        2
    ```

*   **`df1.melt(id_vars='client', value_vars=['bananas', 'oranges'], value_name='quantity')`**:
    *   `id_vars`: 고정으로 유지할 식별자 열(identifier variables)을 지정합니다. 이 예시에서는 'client' 열이 각 행의 고유 식별자로 유지됩니다.
    *   `value_vars`: "wide" 형식에서 "long" 형식으로 변환될 값(value variables)을 포함하는 열들을 리스트로 지정합니다. 이 예시에서는 'bananas'와 'oranges' 열의 값들이 변환 대상입니다.
    *   `value_name`: `value_vars`에서 추출된 값들이 저장될 새로운 열의 이름을 지정합니다. 여기서는 'quantity'로 지정되었습니다.
    *   `var_name` (선택 사항): `value_vars`에 지정된 원래 열 이름들(예: 'bananas', 'oranges')이 저장될 새로운 열의 이름을 지정합니다. 슬라이드에서는 기본값(‘variable’)이 사용되거나 자동 추론되어 'product'로 표시되었습니다.

**구체적 예시**

처음 `df`는 각 고객(John, Silvia)이 구매한 바나나와 오렌지 수량을 각각의 열로 나타냅니다 (Wide 형식).

```
          bananas  oranges
client
John            5        3
Silvia          4        2
```

`df.reset_index()`를 통해 `client`를 일반 열로 만들면 `df1`이 됩니다.

```python
   client  bananas  oranges
0    John        5        3
1  Silvia        4        2
```

`df1.melt(id_vars='client', value_vars=['bananas', 'oranges'], value_name='quantity')`를 실행하면, 'bananas'와 'oranges' 열의 데이터가 'quantity'라는 새 열로 모이고, 원래의 열 이름('bananas', 'oranges')은 'product' (혹은 'variable'이라는 기본 이름)라는 새로운 열의 값으로 들어갑니다.

```python
   client   product  quantity
0    John   bananas         5
1  Silvia   bananas         4
2    John   oranges         3
3  Silvia   oranges         2
```

이 "long" 형식은 각 행이 `(고객, 상품, 수량)`이라는 하나의 관측치를 나타내어 데이터베이스에서 더 일반적인 형태이며, 통계 분석이나 시각화 라이브러리(예: seaborn)에서 사용하기에 편리합니다.

**시험 포인트**

*   **`melt` 함수의 역할**: ⭐ `melt`가 "wide" 데이터를 "long" 데이터로 변환하는 기능을 정확히 이해하고 설명할 수 있어야 합니다. (Pivoting의 반대 개념)
*   **주요 파라미터**: ⭐ `id_vars`, `value_vars`, `value_name`의 각 역할과 사용법을 숙지해야 합니다. 각 파라미터가 최종 결과 데이터프레임의 열 구성에 어떻게 영향을 미치는지 파악하는 것이 중요합니다.
*   **`reset_index()`와의 연관성**: `melt`를 사용하기 전에 인덱스를 열로 변환해야 하는 상황을 이해해야 합니다.
*   **사용 시점**: ⭐ 언제 `melt`를 사용해야 하는지 (명시적으로 id/value 열을 제어하고 싶을 때) 예시와 함께 설명할 수 있어야 합니다. (예: 특정 라이브러리가 long 형식 데이터를 요구할 때)

---

## Slide 33

**핵심 개념**
*   **관계 대수(Relational Algebra)의 나눗셈(Division, $R \div S$) 연산**: 특정 조건을 '모든(for all)' 경우에 만족하는 튜플을 찾는 연산입니다. 예를 들어, $R(\text{Name, Year})$ 테이블과 $S(\text{Year})$ 테이블이 있을 때, $R \div S$는 $S$에 있는 *모든* 연도에 나타나는 이름(Name)을 반환합니다.
    *   $R$ 테이블은 이름과 해당 이름이 등장한 연도 정보를 포함하고, $S$ 테이블은 특정 연도들의 집합을 포함합니다.
    *   $R \div S$의 결과는 $S$에 있는 모든 연도에 대해 $R$에 등장한 이름을 반환합니다.

**코드/수식 해설**

**수식:**
관계 대수의 나눗셈 연산은 다음과 같이 정의될 수 있습니다.
$R \div S = \{t_A \mid \forall t_B \in S, \exists t_R \in R \text{ such that } t_R[A] = t_A \text{ and } t_R[B] = t_B\}$
여기서 $A$는 $R$의 속성 집합 중 $S$의 속성(들)을 제외한 속성 집합이고, $B$는 $S$의 속성 집합입니다. 슬라이드의 예시에서는 $A = \{\text{Name}\}$ 이고 $B = \{\text{Year}\}$ 입니다.

**코드:**
```python
import pandas as pd

# Toy tables from the slide
# R = babynames[["Name", "Year"]].drop_duplicates()
# 실제 데이터셋 'babynames' 대신 예시 데이터로 R 생성
R = pd.DataFrame({
    "Name": ["Alice", "Alice", "Bob", "Bob", "Carol"],
    "Year": [1910, 1911, 1910, 1911, 1910]
})

S = pd.DataFrame({"Year": [1910, 1911]})

# S 테이블에 있는 고유한 연도의 개수를 계산합니다. (|S| 값)
need = S["Year"].nunique() # 여기서는 need = 2

# 1. R과 S를 'Year' 기준으로 내부 조인(Inner Join)합니다.
#    이는 R에서 S에 없는 연도와 관련된 행을 필터링하는 효과를 가집니다.
merged_df = R.merge(S, on="Year")
# merged_df (예시):
#      Name  Year
# 0   Alice  1910
# 1     Bob  1910
# 2   Carol  1910
# 3   Alice  1911
# 4     Bob  1911

# 2. 'Name'별로 그룹화하여, 각 이름이 등장한 고유한 'Year'의 개수를 셉니다.
#    (이때 Year는 이미 S에 있는 Year로 필터링된 상태)
grouped_counts = merged_df.groupby("Name")["Year"].nunique()
# grouped_counts (예시):
# Name
# Alice    2
# Bob      2
# Carol    1
# Name: Year, dtype: int64

# 3. 그룹화된 결과를 데이터프레임으로 변환하고, 'Year' 컬럼의 이름을 'cnt'로 변경합니다.
named_counts_df = grouped_counts.reset_index(name="cnt")
# named_counts_df (예시):
#     Name  cnt
# 0  Alice    2
# 1    Bob    2
# 2  Carol    1

# 4. 'cnt'가 'need'와 같은 이름만 필터링하고, 'Name' 컬럼만 선택합니다.
#    이는 S의 모든 연도에 등장한 이름만을 찾는 과정입니다.
div_result = named_counts_df.query("cnt == @need")["Name"]

print(div_result.tolist()) # 출력: ['Alice', 'Bob']
```
*   **`need = S["Year"].nunique()`**: $S$ 테이블에 포함된 고유한 `Year` 값의 개수를 계산합니다. 이 값이 나눗셈의 기준이 됩니다.
*   **`R.merge(S, on="Year")`**: $R$ 데이터프레임과 $S$ 데이터프레임을 `Year` 컬럼을 기준으로 내부 조인합니다. 이 단계는 $R$에서 $S$에 포함되지 않은 `Year`를 가진 행들을 제거하여, 계산에 필요한 데이터만 남기는 역할을 합니다.
*   **`.groupby("Name")["Year"].nunique()`**: 조인된 결과에서 `Name`별로 그룹화한 후, 각 `Name`이 몇 개의 *고유한* `Year`에 등장했는지 계산합니다. 이 `Year`들은 이미 $S$에 있는 `Year`들로 필터링된 상태입니다.
*   **`.reset_index(name="cnt")`**: `groupby`의 결과인 Series를 `Name`과 `cnt` (고유 연도 개수) 컬럼을 가진 DataFrame으로 변환합니다.
*   **`.query("cnt == @need")["Name"]`**: 마지막으로, `cnt` (각 이름이 등장한 고유 연도 개수)가 `need` (S의 고유 연도 총 개수)와 같은 행들만 필터링하고, 그 중 `Name` 컬럼만을 추출하여 최종 결과를 얻습니다.

**구체적 예시**
대학 수강생 데이터 `R(학생ID, 수강과목ID)`와 필수 이수 과목 데이터 `S(과목ID)`가 있다고 가정해 봅시다. `R ÷ S` 연산은 $S$에 있는 *모든* 필수 이수 과목을 수강한 학생들의 `학생ID`를 반환합니다.

*   `R` 테이블 (학생ID, 과목ID):
    *   (101, CSED201)
    *   (101, CSED202)
    *   (102, CSED201)
    *   (103, CSED201)
*   `S` 테이블 (과목ID):
    *   (CSED201)
    *   (CSED202)

이 경우 `need = S["과목ID"].nunique()`는 2가 됩니다.
1.  `R.merge(S, on="과목ID")`: $R$의 모든 행이 $S$의 과목에 해당하므로 그대로 남습니다. (만약 S에 없는 과목이 R에 있었다면 해당 행은 제거됨)
2.  `groupby("학생ID")["과목ID"].nunique()`:
    *   학생 101: CSED201, CSED202 (2개)
    *   학생 102: CSED201 (1개)
    *   학생 103: CSED201 (1개)
3.  `query("cnt == @need")`: `cnt == 2`를 만족하는 학생은 학생 101뿐입니다.
따라서 $R \div S$의 결과는 {101}이 됩니다. 학생 101은 CSED201과 CSED202 두 과목을 모두 이수했기 때문입니다.

**시험 포인트**
*   ⭐ **관계 대수 나눗셈($R \div S$)의 개념**: 특정 조건을 '모든' 경우에 만족하는 튜플을 찾는 연산임을 이해해야 합니다. (예: 특정 집합의 모든 원소와 관련된 엔티티 찾기).
*   ⭐ **pandas를 이용한 나눗셈 구현 방식**:
    1.  `S`의 고유 원소 개수(`nunique()`)를 구하여 기준(`need`)으로 설정합니다.
    2.  $R$과 $S$를 공통 속성으로 **내부 조인(Inner Join)**하여, $R$에서 $S$에 없는 관련 데이터를 필터링합니다.
    3.  조인된 결과를 나눗셈 대상 속성(`Name`)으로 **그룹화(`groupby()`)**하고, 그룹 내에서 $S$의 공통 속성(`Year`)의 **고유 개수(`nunique()`)**를 셉니다.
    4.  이 개수가 `need`와 **일치하는(`query("cnt == @need")`)** 그룹을 최종 결과로 선택합니다.
*   ⭐ **'for all' 조건의 중요성**: 왜 `groupby().nunique()` 결과와 $S$의 `nunique()`를 비교하는지 그 의미를 정확히 이해해야 합니다. 이는 '모든' 조건을 만족하는지를 확인하는 핵심 단계입니다.
*   **`@need` 사용법**: `query()` 함수 내에서 외부 변수를 참조할 때 `@` 기호를 사용하는 방법을 알아두세요.

---

## Slide 34

**핵심 개념**:
*   **Pivot (피벗) / Cross-Tab (교차 테이블)**: 원본 데이터를 특정 기준(행, 열)에 따라 재구성하고, 각 교차점에 대한 요약 통계(예: 개수, 합계, 평균)를 계산하여 새로운 테이블을 생성하는 데이터 변환 기법입니다. 주로 넓은(wide) 형식의 데이터를 만들거나, 두 범주형 변수 간의 관계를 요약하는 데 사용됩니다.
*   **관계 대수(Relational Algebra) 관점**: 주어진 릴레이션 $R$을 행($rows$)과 열($cols$)로 인덱싱된 매트릭스 형태로 재구성하며, 각 셀의 값은 특정 속성 $A$에 적용된 집계 함수 $f(A)$의 결과가 됩니다.
*   **pandas에서의 구현**: `pd.crosstab` 함수는 주로 두 개 이상의 범주형 변수 간의 빈도수를 계산하여 교차 테이블을 생성하며, `df.pivot_table`은 더 유연하게 여러 컬럼을 `index`, `columns`, `values`로 지정하고 다양한 집계 함수(`aggfunc`)를 적용할 수 있습니다.

**코드/수식 해설**:
가상의 `babynames` 데이터프레임이 `Year`, `Name`, `Sex`, `Count` 등의 컬럼을 포함한다고 가정합니다.

**1. 관계 대수 표기법**:
주어진 관계 대수 쿼리는 다음과 같습니다.
$$PIVOT_{rows=Year, cols=Name, f=count(*)}(\pi_{Year,Name}(babynames))$$
*   $\pi_{Year,Name}(babynames)$: `babynames` 데이터프레임에서 `Year`와 `Name` 컬럼만 선택(투영)합니다.
*   $PIVOT_{rows=Year, cols=Name, f=count(*)}$: 투영된 결과에 대해 `Year`를 행으로, `Name`을 열로 하여 피벗하고, 각 셀의 값은 해당 `Year`와 `Name` 조합의 발생 횟수($count(*)$)로 채웁니다. 이는 `Year`와 `Name` 컬럼을 기준으로 그룹화한 후 각 그룹의 데이터 수를 세는 것과 유사합니다.

**2. `pd.crosstab` 예시**:
```python
# 각 연도(Year)별 이름(Name)의 발생 횟수를 계산하는 피벗 테이블
# 행: Year, 열: Name
pivot1 = pd.crosstab(index=babynames["Year"], columns=babynames["Name"])
```
*   `index=babynames["Year"]`: 결과 테이블의 행(row) 인덱스를 `babynames` 데이터프레임의 `Year` 컬럼 값으로 설정합니다.
*   `columns=babynames["Name"]`: 결과 테이블의 열(column) 이름을 `babynames` 데이터프레임의 `Name` 컬럼 값으로 설정합니다.
*   `pd.crosstab`은 기본적으로 `index`와 `columns`로 지정된 두 범주형 변수 조합의 **빈도수(frequency count)**를 계산하여 각 셀에 채워 넣습니다.

**3. `df.pivot_table` 예시**:
```python
# 각 연도(Year) 및 성별(Sex)에 따른 아기 이름의 총 Count를 계산
# 행: Year, 열: Sex, 집계 대상: Count, 집계 함수: sum
pivot2 = babynames.pivot_table(index="Year", columns="Sex", values="Count", aggfunc="sum", fill_value=0, margins=True)
```
*   `index="Year"`: `Year` 컬럼을 행 인덱스로 사용합니다.
*   `columns="Sex"`: `Sex` 컬럼을 열 이름으로 사용합니다.
*   `values="Count"`: 집계 대상이 되는 컬럼을 `Count`로 지정합니다. 이 컬럼의 값들이 각 셀에 집계됩니다.
*   `aggfunc="sum"`: `values`로 지정된 `Count` 컬럼의 값들을 합계($sum$)합니다. `mean`, `count`, `min`, `max` 등 다양한 집계 함수를 지정할 수 있습니다.
*   `fill_value=0`: 피벗 테이블 생성 후 데이터가 없는 빈 셀(NaN 값)을 0으로 채웁니다.
*   `margins=True`: 결과 테이블에 행과 열의 총합(`All`)을 추가하여 전체 합계를 보여줍니다.

**구체적 예시**:
`babynames` 데이터프레임이 아래와 같다고 가정합니다.

| Year | Name | Sex | Count |
| :--- | :--- | :-- | :---- |
| 2000 | John | M   | 100   |
| 2000 | Mary | F   | 80    |
| 2000 | Jane | F   | 5     |
| 2001 | John | M   | 110   |
| 2001 | Mary | F   | 90    |
| 2001 | John | F   | 7     |

*   **`pivot1` 결과 (Year별 Name 빈도)**:
    `pd.crosstab(index=babynames["Year"], columns=babynames["Name"])`

    | Name | Jane | John | Mary |
    | :--- | :--- | :--- | :--- |
    | **Year** |      |      |      |
    | 2000 | 1    | 1    | 1    |
    | 2001 | 0    | 2    | 1    |
    *   `2000`년에는 `Jane` 1명, `John` 1명, `Mary` 1명이 존재합니다.
    *   `2001`년에는 `Jane`이 없으므로 0, `John`은 2명(M, F), `Mary`는 1명이 존재합니다.

*   **`pivot2` 결과 (Year별 Sex별 Count 합계, margins 포함)**:
    `babynames.pivot_table(index="Year", columns="Sex", values="Count", aggfunc="sum", fill_value=0, margins=True)`

    | Sex | F   | M   | All |
    | :-- | :-- | :-- | :-- |
    | **Year** |     |     |     |
    | 2000 | 85  | 100 | 185 |
    | 2001 | 97  | 110 | 207 |
    | **All** | 182 | 210 | 392 |
    *   `2000`년 `F` 성별의 `Count` 합계: `Mary` (80) + `Jane` (5) = 85
    *   `2000`년 `M` 성별의 `Count` 합계: `John` (100) = 100
    *   `2001`년 `F` 성별의 `Count` 합계: `Mary` (90) + `John` (7) = 97
    *   `All` 행과 열은 각각 전체 `Count`의 합계를 보여줍니다.

**시험 포인트**:
*   ⭐ **`pd.crosstab`과 `df.pivot_table`의 차이점**:
    *   `pd.crosstab`: 주로 두 범주형 변수 간의 빈도수(frequency count)를 계산할 때 사용됩니다. `values` 인자가 없으며, 기본 `aggfunc`는 `count`입니다.
    *   `df.pivot_table`: `values` 인자를 사용하여 집계할 컬럼을 명시하고, `aggfunc`를 통해 `sum`, `mean`, `count`, `min`, `max` 등 다양한 집계 함수를 지정할 수 있어 더 유연하고 강력합니다.
*   ⭐ **주요 인자의 역할**: `index`, `columns`, `values`, `aggfunc`, `fill_value`, `margins` 각 인자가 피벗 테이블의 어떤 부분을 결정하는지 정확히 이해하고 있어야 합니다. 예를 들어, `values`는 어떤 컬럼의 값을 집계할지, `aggfunc`는 어떻게 집계할지를 결정합니다.
*   ⭐ **피벗(Pivot) 연산의 목적**: 평평한(flat) 데이터를 여러 차원의 요약 테이블로 변환하여 데이터의 패턴이나 관계를 쉽게 파악할 수 있도록 돕는다는 점을 기억하세요. 이는 데이터 분석 과정에서 인사이트를 도출하는 데 매우 중요합니다.

---

## Slide 35

**핵심 개념**:
*   **ERA (Extended Relational Algebra) 쿼리**: 관계형 데이터베이스에서 데이터를 조작하고 검색하는 데 사용되는 관계형 대수(Relational Algebra)를 확장한 개념입니다. 일반적인 필터링($\sigma$), 프로젝션($\pi$), 집계($\gamma$) 외에도, 계산된 컬럼 생성(generalized projection)이나 그룹별 상위/하위 레코드 선택(generalized aggregation)과 같은 복잡한 연산을 표현할 수 있습니다.
*   **pandas 파이프라인 (메서드 체이닝)**: `pandas` DataFrame 객체의 메서드들을 연속적으로 호출하여 데이터 처리 과정을 단계적으로 표현하는 방식입니다. 각 메서드가 DataFrame을 반환하므로 다음 메서드를 바로 이어서 사용할 수 있어, 코드를 간결하고 가독성 있게 작성할 수 있습니다.
*   **`groupby().transform()`**: `groupby()`와 함께 `transform()` 메서드를 사용하면 그룹별 집계 값을 계산하되, 그 결과를 원래 DataFrame의 모든 행에 맞춰 브로드캐스트하여 새로운 컬럼을 생성할 수 있습니다. 이는 그룹별 통계를 계산하여 개별 행에 적용해야 할 때 매우 유용합니다.

**코드/수식 해설**:

**ERA Query (확장된 관계형 대수 쿼리)**:
$$
\gamma_{\text{Year, Sex; top1\_by(share)}} \pi_{\text{Year, Sex, Name, Count, Count/SUM}_{\text{y}}(\text{Count})\to\text{share}} \sigma_{\text{Year}\geq 1910}(\text{babynames})
$$
*   $\sigma_{\text{Year}\geq 1910}(\text{babynames})$: `babynames` 테이블에서 `Year` 컬럼 값이 1910 이상인 모든 행을 선택합니다 (연도 필터링).
*   $\pi_{\text{Year, Sex, Name, Count, Count/SUM}_{\text{y}}(\text{Count})\to\text{share}}$: 앞선 필터링 결과에서 `Year`, `Sex`, `Name`, `Count` 컬럼을 선택합니다. 이때 `Count/SUM_y(Count)`라는 새로운 값을 계산하여 `share`라는 컬럼으로 추가합니다. 여기서 `SUM_y(Count)`는 각 `Year`별 `Count`의 총합을 의미합니다 (확장된 프로젝션).
*   $\gamma_{\text{Year, Sex; top1\_by(share)}}$: 앞선 결과에서 `Year`와 `Sex`로 데이터를 그룹화한 후, 각 그룹 내에서 `share` 컬럼 값이 가장 큰 (top-1) 하나의 행만 선택합니다 (확장된 집계).

**pandas 코드**:
```python
result = (babynames
    .query("Year >= 1910") # 1. Year가 1910 이상인 행 필터링 (ERA의 sigma)
    .assign( # 2. 새로운 컬럼 year_total과 share 계산 (ERA의 generalized projection)
        year_total=lambda d: d.groupby("Year")["Count"].transform("sum"),
        # 각 연도별 전체 Count 합계를 계산하여 모든 행에 추가
        share=lambda d: d["Count"]/d["year_total"]
        # 각 이름의 Count를 해당 연도의 총 Count로 나누어 share 계산
    )
    [["Year", "Sex", "Name", "Count", "share"]] # 3. 필요한 컬럼만 선택 및 순서 지정 (ERA의 pi)
    .sort_values(["Year", "Sex", "share"], ascending=[True, True, False]) # 4. Year, Sex 오름차순, share 내림차순 정렬
    .groupby(["Year", "Sex"]).head(1) # 5. Year, Sex 그룹별로 share가 가장 큰 상위 1개 행 선택 (ERA의 generalized aggregation)
    .reset_index(drop=True) # 6. 불필요한 인덱스 제거 및 재설정
)
```
*   `.query("Year >= 1910")`: `DataFrame.query()`는 SQL의 `WHERE` 절과 유사하게 조건을 만족하는 행을 필터링합니다. ERA의 $\sigma$ 연산에 해당합니다.
*   `.assign(...)`: `DataFrame.assign()`은 하나 이상의 새로운 컬럼을 생성하거나 기존 컬럼을 덮어씁니다. `lambda d: ...` 구문을 사용하여 현재 DataFrame `d`에 접근하여 계산을 수행합니다.
    *   `d.groupby("Year")["Count"].transform("sum")`: `Year` 컬럼을 기준으로 그룹화하고, 각 그룹의 `Count` 컬럼 합계를 구한 후, `transform("sum")`을 사용하여 이 합계 값을 원래 DataFrame의 모든 해당 행에 `year_total` 컬럼으로 추가합니다.
    *   `d["Count"]/d["year_total"]`: 각 행의 `Count`를 해당 연도의 `year_total`로 나누어 `share` 컬럼을 계산합니다. 이 두 `assign` 작업은 ERA의 확장된 프로젝션($\pi_{\dots \to\text{share}}$)에 해당합니다.
*   `[["Year", "Sex", "Name", "Count", "share"]]`: 컬럼 선택(`DataFrame[...]`)은 ERA의 $\pi$ 연산에 해당합니다.
*   `.sort_values(["Year", "Sex", "share"], ascending=[True, True, False])`: `Year`와 `Sex`는 오름차순(`True`)으로 정렬하고, `share`는 내림차순(`False`)으로 정렬하여, 이후 그룹별 `top-1` 선택을 위한 준비를 합니다.
*   `.groupby(["Year", "Sex"]).head(1)`: `Year`와 `Sex`를 기준으로 그룹화한 다음, 각 그룹에서 가장 첫 번째 행(`head(1)`)을 선택합니다. `share`가 내림차순으로 정렬되어 있으므로, 각 그룹에서 `share`가 가장 높은 이름이 선택됩니다. 이는 ERA의 확장된 집계($\gamma_{\text{Year, Sex; top1\_by(share)}}$)에 해당합니다.
*   `.reset_index(drop=True)`: `groupby` 연산 후 인덱스가 재구성될 수 있는데, 이를 초기화하여 깔끔한 정수형 인덱스를 얻습니다. `drop=True`는 기존 인덱스를 컬럼으로 유지하지 않고 버립니다.

**구체적 예시**:
만약 2000년에 `Sex='F'`인 이름 `Mary`가 `Count=100`, `Anna`가 `Count=80`, `Julia`가 `Count=120`을 가지고 있고, 2000년 `Sex='F'`의 총 `Count`가 300이었다고 가정해봅시다.
1.  `.query("Year >= 1910")` 이후, 2000년 데이터는 유지됩니다.
2.  `.assign(...)` 단계에서 `year_total`은 2000년의 전체 `Count` 합으로 채워지고, `share`는 다음과 같이 계산됩니다:
    *   Mary: `Count` 100 / `year_total` 300 = `share` 0.333
    *   Anna: `Count` 80 / `year_total` 300 = `share` 0.267
    *   Julia: `Count` 120 / `year_total` 300 = `share` 0.400
3.  `.sort_values(["Year", "Sex", "share"], ascending=[True, True, False])` 단계에서 2000년 `Sex='F'` 그룹은 `share`가 높은 순서대로 `Julia`, `Mary`, `Anna`로 정렬됩니다.
4.  `.groupby(["Year", "Sex"]).head(1)` 단계에서 `(Year=2000, Sex=F)` 그룹에서 가장 첫 번째 행인 `Julia` 데이터만 최종 결과로 선택됩니다. 이처럼 각 연도 및 성별에서 가장 인기 있는 이름을 찾을 수 있습니다.

**시험 포인트**:
*   ⭐ **ERA 연산 ($\sigma$, $\pi$, $\gamma$)이 pandas 메서드(`query`, `assign`, `groupby`, `sort_values`, `head`)로 어떻게 변환되는지 정확히 매핑하여 설명할 수 있어야 합니다.** 특히 `generalized projection`과 `generalized aggregation`을 pandas로 구현하는 방식이 중요합니다.
*   ⭐ **`transform()`과 `apply()`의 차이점을 명확히 이해하고, `groupby().transform()`이 어떤 상황에서 유용하게 사용되는지 설명할 수 있어야 합니다.** (예: 그룹별 통계를 각 개별 행에 브로드캐스트하여 새로운 컬럼을 생성하는 경우)
*   ⭐ **`sort_values()`와 `head(N)` (또는 `tail(N)`)를 조합하여 그룹별 상위/하위 N개 항목을 선택하는 기법을 이해하고, `ascending` 파라미터의 역할에 대해 설명할 수 있어야 합니다.**
*   **pandas에서 메서드 체이닝(파이프라인)을 사용하는 장점** (코드의 가독성, 효율적인 데이터 흐름, 중간 변수 생성 불필요)을 설명할 수 있어야 합니다.

---

## Slide 36

## Query Best Practices (ERA ↔ pandas)

데이터프레임을 효율적이고 정확하게 쿼리하기 위한 모범 사례들을 다룹니다. 이는 관계형 대수(ERA)의 개념을 pandas 라이브러리에 적용하는 관점으로 이해할 수 있습니다.

---

### **핵심 개념**

*   **Selection (선택)**: 특정 조건에 맞는 행을 필터링하는 작업입니다. 복잡한 조건식의 가독성을 높이는 방법을 강조합니다.
*   **Generalized Projection (일반화된 투영)**: 기존 컬럼을 기반으로 새로운 컬럼을 생성하고, 원하는 컬럼만 선택하여 데이터를 재구성하는 작업입니다.
*   **Set Semantics (집합 의미론)**: 데이터 처리 시 중복을 허용하는 "가방(bag)"이 아닌, 중복을 제거한 "집합(set)"처럼 데이터를 다루는 경우를 의미합니다.
*   **Joins (조인)**: 두 개 이상의 데이터프레임을 특정 키(key)를 기준으로 결합하는 작업입니다. 키의 명시와 데이터 증가(row blow-up) 방지가 중요합니다.
*   **Grouping (그룹화)**: 특정 컬럼의 값을 기준으로 데이터를 그룹으로 나누고, 각 그룹에 대해 집계(aggregation) 함수를 적용하는 작업입니다.
*   **Pivot (피벗)**: 데이터프레임의 구조를 재구성하여, 특정 컬럼의 고유 값들을 새로운 컬럼으로 만들고 다른 컬럼의 값을 해당 셀에 채워 넣는 작업입니다.

---

### **코드/수식 해설**

1.  **Selection**:
    *   **가독성 향상**: 불리언 마스크를 사용할 때 괄호로 조건을 명확히 구분하거나, `.query()` 메서드를 사용하여 SQL과 유사한 구문으로 조건을 지정합니다.
    ```python
    # Bad practice (potential ambiguity without parentheses)
    # df[df['col1'] > 10 & df['col2'] < 20] # Might evaluate (10 & df['col2']) first

    # Good practice: Parenthesize masks for clarity
    df[(df['col1'] > 10) & (df['col2'] < 20)]

    # Alternative: Use .query() for even better readability, especially with multiple conditions
    df.query('col1 > 10 and col2 < 20')
    ```

2.  **Generalized projection**:
    *   `.assign()`을 사용하여 임시 또는 새로운 컬럼을 계산한 후, 명시적으로 필요한 컬럼만 선택합니다.
    ```python
    import pandas as pd
    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    df = pd.DataFrame(data)

    # Calculate 'Sum_AB' and then select 'A' and 'Sum_AB'
    result = df.assign(Sum_AB=df['A'] + df['B'])[['A', 'Sum_AB']]
    print(result)
    ```

3.  **Set semantics**:
    *   데이터프레임이나 시리즈에서 중복된 행/값을 제거하여 유일한 값들만 남기고자 할 때 `.drop_duplicates()`를 사용합니다.
    ```python
    # Example for Set semantics: remove duplicate rows
    data = {'ID': [1, 2, 1, 3], 'Value': ['A', 'B', 'A', 'C']}
    df_bag = pd.DataFrame(data)
    print("Original DataFrame (bag):\n", df_bag)

    df_set = df_bag.drop_duplicates()
    print("\nDataFrame after drop_duplicates (set):\n", df_set)

    # For a specific column
    unique_ids = df_bag['ID'].drop_duplicates()
    print("\nUnique IDs (set semantics for column):\n", unique_ids)
    ```

4.  **Joins**:
    *   두 데이터프레임을 병합할 때 `on` 인자를 통해 반드시 조인 키(key)를 명시해야 합니다. `how` 인자를 통해 조인 방식(inner, left, right, outer)을 지정합니다.
    *   **Key Multiplicity (키의 다중성) 확인**: 조인 전에 각 데이터프레임의 키 컬럼에서 중복이 있는지 확인하여, 예상치 못한 행 수 증가("row blow-up")를 방지합니다.
    ```python
    # Example of Join with explicit key
    df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
    df2 = pd.DataFrame({'ID': [1, 2, 4], 'Score': [90, 85, 95]})

    # Specify 'ID' as the join key
    merged_df = pd.merge(df1, df2, on='ID', how='inner')
    print("Merged DataFrame:\n", merged_df)

    # Verifying key multiplicities
    # print(df1['ID'].value_counts())
    # print(df2['ID'].value_counts())
    ```

5.  **Grouping**:
    *   `.groupby()`를 사용하여 그룹화한 후, `sum()`, `mean()`, `size()` 등 내장된 집계 함수를 우선적으로 사용합니다.
    *   `agg()` 메서드를 사용하여 여러 집계 함수를 동시에 적용하고, 결과를 명시적으로 이름 붙여 출력할 수 있습니다.
    ```python
    # Example of Grouping with built-in functions
    data = {'Category': ['A', 'B', 'A', 'B', 'A'], 'Value': [10, 20, 15, 25, 12]}
    df = pd.DataFrame(data)

    # Group by 'Category' and calculate sum of 'Value'
    grouped_sum = df.groupby('Category')['Value'].sum()
    print("Grouped Sum:\n", grouped_sum)

    # Using .agg() with named outputs
    grouped_agg = df.groupby('Category').agg(
        Total_Value=('Value', 'sum'),
        Mean_Value=('Value', 'mean'),
        Count=('Value', 'size')
    )
    print("\nGrouped Aggregation with named outputs:\n", grouped_agg)
    ```

6.  **Pivot**:
    *   `pivot_table()`을 사용하여 데이터를 재구조화할 때, `index`, `columns`, `values`를 지정합니다.
    *   만약 `index`와 `columns` 조합에 해당하는 `values`가 여러 개 존재할 수 있는 경우, 반드시 `aggfunc` (예: `'mean'`, `'sum'`, `len`)을 지정해야 합니다. 그렇지 않으면 에러가 발생합니다.
    ```python
    # Example of Pivot
    data = {'Date': ['2023-01-01', '2023-01-01', '2023-01-02'],
            'City': ['Seoul', 'Busan', 'Seoul'],
            'Temp': [5, 10, 7]}
    df = pd.DataFrame(data)

    # Pivot: index=Date, columns=City, values=Temp
    # Assuming each Date-City pair has only one temperature
    pivoted_df = df.pivot_table(index='Date', columns='City', values='Temp')
    print("Pivoted DataFrame (unique values):\n", pivoted_df)

    # What if there are multiple temperatures for a Date-City pair?
    data_multi = {'Date': ['2023-01-01', '2023-01-01', '2023-01-01'],
                  'City': ['Seoul', 'Seoul', 'Busan'],
                  'Temp': [5, 8, 10]}
    df_multi = pd.DataFrame(data_multi)
    # This would raise an error without aggfunc:
    # df_multi.pivot_table(index='Date', columns='City', values='Temp')

    # Must provide aggfunc if multiple values exist for (index, columns) pair
    pivoted_agg = df_multi.pivot_table(index='Date', columns='City', values='Temp', aggfunc='mean')
    print("\nPivoted DataFrame (with aggfunc for multiple values):\n", pivoted_agg)
    ```

---

### **구체적 예시**

*   **Selection**: 우리 학과 학생 데이터(`students_df`)에서 학점이 3.5 이상이고 전공이 '컴퓨터공학과'인 학생들만 보고 싶을 때, `students_df.query("GPA >= 3.5 and Major == '컴퓨터공학과'")`를 사용하여 명확하게 쿼리할 수 있습니다.
*   **Generalized Projection**: 기말고사 점수와 중간고사 점수를 합산한 '총점' 컬럼을 새로 만들고, 학생 이름과 총점만 보고 싶을 때 `.assign()`을 활용합니다.
    ```python
    students_df.assign(Total_Score = students_df['Midterm'] + students_df['Final'])[['Student_Name', 'Total_Score']]
    ```
*   **Set Semantics**: 수강 신청 내역(`enrollments_df`)에 한 학생이 같은 과목을 두 번 신청한 기록이 있을 때, 실제로 이 학생이 수강하는 '과목명'의 고유 목록만 얻으려면 `enrollments_df['Course_Name'].drop_duplicates()`를 사용합니다.
*   **Joins**: 각 학생의 기본 정보(`students_df`)와 해당 학생이 수강한 과목 성적 정보(`grades_df`)를 학생 ID를 기준으로 합칠 때, `pd.merge(students_df, grades_df, on='StudentID', how='left')`를 사용합니다. 이때 `StudentID`가 `students_df`에서는 유일하지만 `grades_df`에서는 한 학생이 여러 과목을 수강하여 중복될 수 있으므로, `how='left'`를 사용하여 학생 정보가 중복되지 않도록 주의해야 합니다.
*   **Grouping**: 전국 지점별 월별 판매 데이터에서 각 지점의 총 판매량과 평균 판매량을 알고 싶을 때, `sales_df.groupby('Branch_ID').agg(Total_Sales=('Sales_Amount', 'sum'), Avg_Sales=('Sales_Amount', 'mean'))`와 같이 그룹화 및 집계를 수행합니다.
*   **Pivot**: 학생들의 과목별 점수가 `Student`, `Course`, `Score` 컬럼으로 있을 때, 학생 이름을 행(index)으로, 과목명을 열(columns)로, 점수를 값(values)으로 하는 형태로 데이터를 변환하여 각 학생이 어떤 과목에서 몇 점을 받았는지 한눈에 보고 싶을 때 `df.pivot_table(index='Student', columns='Course', values='Score')`를 사용합니다. 만약 한 학생이 같은 과목을 여러 번 수강하여 점수가 여러 개라면 `aggfunc='mean'` 등을 추가해야 합니다.

---

### **시험 포인트**

*   **⭐ `.query()` 메서드의 사용 목적과 장점**를 설명할 수 있어야 합니다. 특히 복잡한 조건식을 다룰 때의 가독성 측면을 강조하세요.
*   **⭐ `.assign()`을 이용한 새로운 컬럼 생성과 `.drop_duplicates()`를 이용한 중복 제거의 중요성**을 이해하고 실제 코드에 적용할 수 있어야 합니다.
*   **⭐ `pd.merge()` 시 `on` 인자의 역할과 `how` (inner, left, right, outer) 옵션의 차이점**을 정확히 설명하고, **키의 다중성(multiplicity)이 조인 결과에 미치는 영향** (예: row blow-up)을 인지하는 것이 중요합니다.
*   **⭐ `groupby()`와 함께 내장 집계 함수(sum, mean, size 등)를 사용하는 방법**을 숙지하고, **`agg()` 메서드로 여러 집계 함수를 적용하고 출력 컬럼 이름을 지정하는 방법**을 알아야 합니다.
*   **⭐ `pivot_table()` 사용 시 `aggfunc` 인자가 필요한 경우와 그 이유**를 명확히 설명할 수 있어야 합니다. 이는 데이터 재구조화 시 발생할 수 있는 데이터 충돌 문제를 해결하는 핵심 개념입니다.

---

## Slide 37

**핵심 개념**: 누락된 데이터(Missing Data)는 데이터 분석의 정확성을 저해할 수 있으므로, 이를 효율적으로 탐지하고 처리하는 기법이 중요합니다. 이 슬라이드에서는 누락 값을 감지하고 플래그를 지정하는 방법, 그룹별로 누락 값을 보간하는 방법, 그리고 시간 순서를 고려하여 누락 값을 채우는 방법을 다룹니다.

---

### Detect & flag (누락 값 감지 및 플래그 지정)

*   **핵심 개념**: 데이터프레임의 각 행에 누락 값이 존재하는지 여부를 식별하고, 해당 정보를 새로운 열(플래그)로 저장하는 기법입니다. 이는 특정 행이 불완전하다는 사실을 기록하여, 나중에 해당 행들을 쉽게 필터링하거나, 품질 관리(QC) 목적으로 사용하거나, 모델 학습에서 제외할 때 활용합니다.
*   **코드 해설**:
    ```python
    na_rows = df.isna().any(axis=1)
    df["has_na"] = na_rows
    ```
    1.  `df.isna()`: 데이터프레임 `df`의 모든 원소를 순회하며 누락 값(NaN)인 경우 `True`, 그렇지 않은 경우 `False`를 반환하는 불리언(Boolean) 데이터프레임을 생성합니다.
    2.  `.any(axis=1)`: `df.isna()` 결과에 대해 각 행(row, `axis=1`)에 하나라도 `True`가 있는지 확인합니다. 즉, 해당 행에 단 하나의 누락 값이라도 있으면 `True`를, 모든 값이 유효하면 `False`를 반환하는 Series `na_rows`를 생성합니다.
    3.  `df["has_na"] = na_rows`: `df`에 "has_na"라는 새로운 열을 추가하고, `na_rows`의 값(각 행에 누락 값이 있는지 여부)으로 채웁니다. 이 열은 각 행의 누락 값 존재 여부를 나타내는 플래그 역할을 합니다.
*   **구체적 예시**: 설문조사 데이터에서 한 응답자의 인구통계학적 정보(나이, 직업, 소득 등) 중 일부가 누락된 경우, `has_na` 열에 `True`로 플래그를 지정할 수 있습니다. 이렇게 하면 나중에 특정 분석에서 이 불완전한 응답자를 제외하거나, 추가적인 데이터 보강을 시도할 대상을 쉽게 식별할 수 있습니다.
*   **시험 포인트**:
    *   ⭐`df.isna().any(axis=1)` 코드의 의미와 결과가 무엇인지 정확히 설명할 수 있어야 합니다. (어떤 행에라도 결측치가 있는지 True/False로 판단)
    *   ⭐`"has_na"`와 같은 플래그를 생성하는 주요 목적 (빠른 필터링, 품질 관리, 모델 제외)을 이해해야 합니다.
    *   Tip: `df.isna().sum()`을 사용하여 각 열별 누락 값의 개수를 파악할 수 있다는 것도 기억해두세요.

---

### Group-wise impute (그룹별 누락 값 보간)

*   **핵심 개념**: 전체 데이터셋의 통계량으로 누락 값을 채우는 대신, 특정 기준(예: "group" 열)에 따라 데이터를 동질적인 그룹으로 나눈 후, 각 그룹 내에서만 계산된 통계량(중앙값, 평균 등)으로 해당 그룹의 누락 값을 채우는 방법입니다. 이는 그룹 간의 데이터 누수(leakage)를 방지하고, 각 그룹의 고유한 특성을 유지하면서 더 정확한 보간을 가능하게 합니다.
*   **코드 해설**:
    ```python
    df["x_imp"] = (df.groupby("group")["x"]
                    .transform(lambda s: s.fillna(s.median())))
    ```
    1.  `df.groupby("group")`: 데이터프레임 `df`를 "group" 열의 고유 값들을 기준으로 그룹화합니다.
    2.  `["x"]`: 그룹화된 결과에서 "x" 열만을 선택합니다. 이 "x" 열에 대해 누락 값 보간을 수행할 것입니다.
    3.  `.transform(lambda s: s.fillna(s.median()))`: 각 그룹별 "x" 열(Series `s`)에 대해 람다 함수를 적용합니다.
        *   `s.median()`: 현재 그룹의 "x" 열에 대한 중앙값을 계산합니다.
        *   `s.fillna(s.median())`: 현재 그룹의 "x" 열 내에서 누락 값(NaN)을 해당 그룹의 중앙값으로 채웁니다.
        *   `transform()`은 그룹별 연산 결과를 원본 데이터프레임의 인덱스에 맞게 확장하여 반환하므로, `df["x_imp"]`라는 새로운 열로 할당될 수 있습니다.
*   **구체적 예시**: 병원 데이터를 분석할 때, 여러 병원(group)에서 환자들의 혈압(x)을 측정했는데 일부 기록이 누락되었습니다. 이 경우, 모든 병원 환자의 평균 혈압으로 누락 값을 채우기보다는, 각 병원별 평균 혈압으로 해당 병원의 누락 값을 채우는 것이 더 합리적입니다. 특정 병원의 환자 특성(예: 전문병원)이 다른 병원과 다를 수 있기 때문입니다.
*   **시험 포인트**:
    *   ⭐Group-wise imputation의 필요성 (그룹 간 누수 방지, 동질적 코호트의 특성 반영)을 설명할 수 있어야 합니다.
    *   ⭐`groupby().transform()` 패턴이 어떻게 그룹별 연산을 수행하고 결과를 원본 구조에 맞게 반환하는지 이해해야 합니다.
    *   ⭐중앙값(median)이 이상치에 강인하며(robustness), 평균(mean)은 데이터 분포가 대칭적일 때 주로 사용된다는 선택 기준을 기억하세요. `ffill`은 패널 데이터(panel data)에 유용합니다.
    *   Gotcha: ⭐각 그룹에 누락되지 않은 값이 없는 경우(예: 모든 값이 NaN이라서 `s.median()`도 NaN이 되는 경우)에는 `fillna(global_median)`과 같은 추가적인 대체 방안을 고려해야 합니다.

---

### Time-aware fill (시간을 고려한 누락 값 채우기)

*   **핵심 개념**: 시계열 데이터나 패널 데이터와 같이 시간 순서가 중요한 데이터에서 누락 값을 처리할 때, 이전 시점의 값(forward fill) 또는 이후 시점의 값(backward fill)을 사용하여 채우는 기법입니다. 이는 데이터의 시간적 인과성(temporal causality)을 보존하며, 센서 데이터, 로그 데이터 등 시간에 따라 변화하는 데이터에 특히 적합합니다.
*   **코드 해설**:
    ```python
    df = df.sort_values(["id", "ts"])
    df["y_filled"] = df.groupby("id")["y"].ffill().bfill()
    ```
    1.  `df = df.sort_values(["id", "ts"])`: 누락 값을 채우기 전에 데이터프레임을 "id" (개체 식별자)와 "ts" (타임스탬프) 열을 기준으로 오름차순으로 정렬합니다. ⭐**시간 기반 채우기를 위해서는 반드시 이 정렬 과정이 선행되어야 합니다.**
    2.  `df.groupby("id")`: "id" 열을 기준으로 데이터를 그룹화합니다. 이는 각 개체(예: 특정 고객, 특정 센서)의 시계열 내에서만 채우기 작업을 수행하기 위함입니다.
    3.  `["y"]`: 그룹화된 결과에서 "y" 열(누락 값이 있는 대상 열)을 선택합니다.
    4.  `.ffill()`: 각 그룹 내에서 누락 값(NaN)을 바로 이전(forward)의 유효한 값으로 채웁니다.
    5.  `.bfill()`: `.ffill()`을 적용한 후에도 여전히 남아있는 누락 값(주로 시계열의 시작 부분에 있던 NaN)을 바로 이후(backward)의 유효한 값으로 채웁니다. `ffill()`과 `bfill()`을 함께 사용하면 시계열 중간의 모든 누락 값을 효과적으로 채울 수 있습니다.
*   **구체적 예시**: 주식 시장 데이터를 분석할 때, 특정 기업(id)의 특정 날짜(ts) 주가(y) 데이터가 누락될 수 있습니다. 이 경우, 직전 거래일의 주가로 누락 값을 채우거나 (`ffill`), 이후 거래일의 주가로 채우는 (`bfill`) 것이 전체 시장의 평균 주가로 채우는 것보다 더 현실적입니다. 예를 들어, 전날 종가로 현재 시점의 누락된 주가를 채우는 것이 일반적입니다.
*   **시험 포인트**:
    *   ⭐Time-aware fill의 목적 (시간적 인과성 보존, 시계열/패널 데이터에 적합)을 이해해야 합니다.
    *   ⭐`ffill()` (forward fill)과 `bfill()` (backward fill)의 동작 방식과, 두 메서드를 함께 사용하는 이유를 설명할 수 있어야 합니다.
    *   ⭐`sort_values(["id", "ts"])`와 같이 정렬이 시간 기반 채우기 전에 **필수적인 이유**를 강조하세요. (정확한 시간 순서대로 채우기 위함)
    *   Gotcha: `max_gap` 인자를 고려하여 너무 오래된 값으로 누락 값을 채우는 것을 방지해야 합니다. 오래된 데이터로 채우면 'stale propagation' 문제가 발생할 수 있습니다.

---

## Slide 38

## 데이터 타입 및 카테고리 효율적 처리 (Patterns II — Types & Categories)

---

### **1. 숫자형 데이터 안전하게 변환 (Coerce numerics safely)**

-   **핵심 개념**: 다양한 형식으로 저장된 문자열 데이터를 안전하게 숫자형으로 변환하는 방법입니다. 특히, 숫자로 변환할 수 없는 값들을 `NaN` (Not a Number)으로 처리하여 데이터 처리 중 오류를 방지하고, 이후 통계 계산이나 머신러닝 모델링이 가능하도록 합니다.

-   **코드/수식 해설**:
    ```python
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    ```
    이 코드는 `df` DataFrame의 "price" 열을 `pandas.to_numeric` 함수를 사용하여 숫자형으로 변환합니다.
    -   `errors="coerce"`: 이 인자는 숫자로 변환할 수 없는 문자열(예: '1,000원', 'N/A', '데이터없음')이 있을 경우, 해당 값을 `np.nan`으로 자동 변환하여 오류 없이 전체 열을 처리할 수 있도록 합니다. 이 과정이 없으면, 변환 불가능한 값 하나 때문에 전체 작업이 중단될 수 있습니다.

-   **구체적 예시**:
    온라인 쇼핑몰에서 상품 가격 데이터를 수집했을 때, 일부 가격 정보가 '10,000원', '무료', '가격협상' 등으로 입력될 수 있습니다.
    -   원본: `['1000', '2,500', '무료', '500', 'N/A']`
    -   `pd.to_numeric(..., errors="coerce")` 적용 후: `[1000.0, 2500.0, nan, 500.0, nan]`
    이렇게 변환되면 숫자로 연산이 가능한 값들은 유지되고, 그렇지 않은 값들은 `NaN`으로 명시되어 처리됩니다. 이후 `NaN` 값들은 평균 계산에서 제외되거나, 특정 전략에 따라 보간(imputation)될 수 있습니다.

-   **시험 포인트**: ⭐ `pd.to_numeric` 함수의 역할과 `errors="coerce"` 인자가 왜 중요한지 설명할 수 있어야 합니다. (데이터 클리닝, 오류 방지, 통계 및 모델링 준비)

---

### **2. 카테고리형 데이터 사용 (Use categoricals for keys)**

-   **핵심 개념**: 반복되는 고유값이 적거나 중간 정도인 문자열 데이터를 `category` 타입으로 변환하여 메모리 사용량을 줄이고, 데이터 처리 속도(특히 `groupby`, `join` 연산)를 향상시키는 방법입니다. 문자열 레이블을 내부적으로 효율적인 정수 코드로 인코딩하여 저장합니다.

-   **코드/수식 해설**:
    ```python
    df["city"] = df["city"].astype("category")
    ```
    이 코드는 `df` DataFrame의 "city" 열을 `category` 데이터 타입으로 변환합니다. `astype("category")` 메서드를 사용합니다.

-   **구체적 예시**:
    전국 지점별 판매 실적 데이터에서 'city' (도시) 컬럼이 있다고 가정합니다. '서울', '부산', '대구', '인천' 등의 도시 이름이 데이터셋에 수십만 번 반복될 수 있습니다.
    -   일반 `object` (문자열) 타입: 각 도시 이름 문자열이 개별적으로 저장되므로, 데이터가 많아질수록 메모리 소모가 커집니다.
    -   `category` 타입: '서울', '부산', '대구', '인천'이라는 고유 문자열은 한 번만 저장되고, 실제 'city' 열에는 이 고유 문자열에 매핑된 정수 코드(예: 서울=0, 부산=1, 대구=2, 인천=3)가 저장됩니다.
    이러한 방식은 고유값이 적거나 중간 정도인 경우(예: 성별, 지역, 상품 카테고리) 메모리를 크게 절약하고, `groupby('city')`와 같은 연산의 속도를 향상시킵니다.
    -   `Gotcha`: 여러 DataFrame 간 병합(merge) 시, 카테고리 집합(categories set)이 일치하지 않으면 병합이 실패할 수 있습니다. 예를 들어, 한 DataFrame에는 '서울', '부산'만 카테고리로 있고, 다른 DataFrame에는 '서울', '제주'만 있다면 문제가 발생할 수 있습니다.

-   **시험 포인트**: ⭐ 'category' 데이터 타입의 주요 장점(메모리 절약, 연산 속도 향상)과 어떤 종류의 데이터(낮거나 중간 정도의 카디널리티를 가진 차원 데이터)에 적합한지 설명할 수 있어야 합니다. ⭐ `df.astype("category")` 사용법과 카테고리 타입 병합 시 발생할 수 있는 문제점을 함께 이해해야 합니다.

---

### **3. 견고한 날짜/시간 데이터 파싱 (Datetime parsing (robust))**

-   **핵심 개념**: 다양한 형식으로 입력될 수 있는 날짜 및 시간 문자열을 표준화된 `datetime` 객체로 변환하는 방법입니다. 특히, `utc=True` 옵션을 사용하여 모든 시간을 UTC (협정 세계시) 기준으로 통일함으로써, 시간대(timezone) 관련 오류나 일광 절약 시간제(DST)로 인한 문제를 방지하여 시계열 분석의 신뢰성을 높입니다.

-   **코드/수식 해설**:
    ```python
    df["ts"] = pd.to_datetime(df["ts"], errors="coerce", utc=True)
    ```
    이 코드는 `df` DataFrame의 "ts" (timestamp) 열을 `pandas.to_datetime` 함수를 사용하여 `datetime` 객체로 변환합니다.
    -   `errors="coerce"`: 날짜/시간 형식으로 변환할 수 없는 문자열이 있을 경우, 해당 값을 `NaT` (Not a Time)으로 변환합니다.
    -   `utc=True`: 이 인자는 변환된 모든 `datetime` 객체를 시간대 인지(timezone-aware) UTC 시간으로 만듭니다. 이는 다양한 지역에서 수집된 시간 데이터를 일관된 기준으로 비교하고 처리하는 데 필수적입니다.

-   **구체적 예시**:
    사용자 활동 로그 데이터에 '2023-01-01 10:00:00 KST', '2023/02/15 13:30 PDT', '03/10/2023 15:00 GMT' 등 다양한 형식과 시간대의 타임스탬프가 섞여 있을 수 있습니다.
    -   `pd.to_datetime(..., utc=True)` 적용 후: 모든 타임스탬프가 UTC 기준으로 통일됩니다. 예를 들어, '2023-01-01 10:00:00 KST' (UTC+9)는 '2023-01-01 01:00:00 UTC'로 변환됩니다. '잘못된 시간'은 `NaT`로 변환됩니다.
    이렇게 표준화된 `datetime` 객체는 시계열 리샘플링(resampling)이나 롤링(rolling) 연산을 신뢰성 있게 수행하는 데 도움을 줍니다. 또한, 일광 절약 시간제 변경 시 발생할 수 있는 시간 중복이나 누락 문제도 방지할 수 있습니다.

-   **시험 포인트**: ⭐ `pd.to_datetime` 함수의 역할과 `utc=True` 인자를 사용하여 시간대 문제를 해결하고 DST 버그를 피하는 방법의 중요성을 설명하는 문제. 데이터 분석에서 시간대 표준화가 왜 중요한지 이유를 들어 설명할 수 있어야 합니다. ⭐ 원본 시간대(TZ)를 아는 경우 `dt.tz_localize()`를 사용하여 로컬라이즈한 후 UTC로 변환하는 팁도 중요합니다.

---

## Slide 39

**핵심 개념**:
이 슬라이드는 데이터 전처리 과정에서 중요한 세 가지 패턴을 다룹니다: 정확한 중복 제거 (Exact deduplication), 텍스트 정규화를 통한 유사 중복 제거 (Near-duplicate by normalized text), 그리고 분위수 기반 이상치 제한 (Winsorization via quantile clipping). 이 기법들은 데이터의 품질을 높이고, 분석의 정확성과 머신러닝 모델의 견고성을 향상시키는 데 필수적입니다.

---

### **1. Exact / subset-based dedup (정확/부분집합 기반 중복 제거)**

*   **핵심 개념**:
    특정 컬럼(들)의 조합이 완전히 동일한 행들을 중복으로 간주하고, 이들 중 하나만 남기고 나머지를 제거하는 과정입니다. 이는 데이터셋 내에서 불필요하게 반복되는 정보를 없애 데이터의 정확성과 효율성을 높입니다.
    *   **목적**: 핵심 성과 지표(KPI)의 이중 계산을 방지하고, 머신러닝 모델 학습 시 데이터 누수(label leakage)를 막아 모델의 일반화 성능을 저해하는 것을 방지합니다.

*   **코드/수식 해설**:
    ```python
    df = df.drop_duplicates(subset=["user_id", "ts"])
    ```
    *   `df.drop_duplicates()`: pandas DataFrame의 메서드로, 중복된 행을 제거합니다.
    *   `subset=["user_id", "ts"]`: 중복을 판단할 기준이 되는 컬럼(들)을 지정합니다. 여기서는 'user_id'와 'ts'(timestamp) 컬럼의 값이 모두 동일한 경우를 중복으로 간주합니다. 이 인자가 없으면 모든 컬럼의 값이 동일한 경우에만 중복으로 판단합니다.
    *   `keep` 인자 (생략 시 기본값 'first'): 중복된 행들 중 어떤 것을 남길지 지정합니다.
        *   `'first'`: 첫 번째 나타난 행을 남기고 나머지를 제거합니다.
        *   `'last'`: 마지막으로 나타난 행을 남기고 나머지를 제거합니다.
        *   `False`: 모든 중복된 행을 제거합니다 (즉, 유일한 행만 남깁니다).
    *   **팁**: 특정 기준으로 중복 행 중 하나를 선택해야 할 경우, `sort_values()`로 먼저 정렬한 후 `drop_duplicates(keep="first" 또는 "last")`를 사용하면 유연하게 처리할 수 있습니다.

*   **구체적 예시**:
    온라인 쇼핑몰의 사용자 행동 로그 데이터에 `user_id`, `event_type`, `timestamp` 컬럼이 있다고 가정해 봅시다. 만약 시스템 오류로 인해 한 사용자가 동일한 시간에 동일한 이벤트를 두 번 기록한 중복된 로그가 발생했다면, `df.drop_duplicates(subset=["user_id", "event_type", "timestamp"])`를 사용하여 이러한 중복을 제거할 수 있습니다. 이는 특정 이벤트의 발생 횟수를 정확하게 집계하는 데 중요합니다.

*   **시험 포인트**:
    *   ⭐ `df.drop_duplicates()` 메서드의 기능과 `subset` 인자의 역할을 정확히 설명할 수 있어야 합니다.
    *   ⭐ 왜 중복 제거가 필요한지 (KPI 정확성, ML 데이터 누수 방지) 그 중요성을 이해하고 설명할 수 있어야 합니다.
    *   `keep` 인자를 활용하여 중복 행 중 특정 기준에 따라 보존하는 방법을 아는 것이 좋습니다.

---

### **2. Near-dup by normalized text (텍스트 정규화를 통한 유사 중복 제거)**

*   **핵심 개념**:
    텍스트 데이터는 대소문자, 공백, 특수 문자, 악센트 등의 사소한 차이로 인해 컴퓨터는 다른 값으로 인식하지만, 실제로는 동일한 의미를 가질 수 있습니다. "유사 중복" 제거는 이러한 텍스트 데이터를 표준화(normalization)하여 의미상 동일한 엔티티를 하나의 대표 값으로 통일하고, 이를 기준으로 중복을 처리하는 기법입니다.

*   **코드/수식 해설**:
    ```python
    key = df["name"].str.strip().str.lower()
    df = df.loc[~key.duplicated()]
    ```
    *   `df["name"].str.strip()`: 'name' 컬럼의 각 문자열 양 끝에 있는 공백(whitespace)을 제거합니다. (`.str` 접근자는 Series의 문자열 메서드를 사용할 수 있게 합니다.)
    *   `.str.lower()`: 공백 제거 후, 모든 문자를 소문자로 변환합니다.
    *   `key = ...`: 이렇게 공백 제거 및 소문자 변환을 거쳐 정규화된 텍스트 값을 `key`라는 새로운 pandas Series로 만듭니다. 이 `key` Series가 유사 중복을 판단하는 기준이 됩니다.
    *   `key.duplicated()`: `key` Series에서 중복된 값을 `True`로 표시하는 Boolean Series를 반환합니다. 이 메서드는 기본적으로 첫 번째 나타난 값은 `False`로, 이후 동일한 값들은 `True`로 처리합니다.
    *   `~key.duplicated()`: `~` 연산자는 Boolean Series의 값을 반전시킵니다. 즉, `key` Series에서 중복이 아닌 (첫 번째 나타난) 값들만 `True`가 됩니다.
    *   `df.loc[...]`: 이 Boolean Series를 사용하여 원본 DataFrame `df`에서 `True`에 해당하는 행들만 선택하여, 유사 중복이 제거된 새로운 DataFrame을 만듭니다.

*   **구체적 예시**:
    고객 설문 응답 데이터에서 '회사명'을 입력받았을 때, "Google Inc.", "google inc.", " GOOGLE Inc" 와 같이 다양한 형태로 입력될 수 있습니다. `str.strip().str.lower()`를 적용하면 이 모든 값들이 "google inc."와 같이 표준화됩니다. 이 표준화된 '회사명'을 기준으로 `duplicated()`를 적용하면, 실제로는 같은 회사임에도 불구하고 텍스트 차이로 인해 다르게 취급되던 데이터들을 하나의 회사로 묶어 정확한 통계나 분석을 수행할 수 있습니다.

*   **시험 포인트**:
    *   ⭐ 텍스트 데이터의 유사 중복이 발생하는 이유와 이를 처리하기 위한 정규화의 중요성을 설명할 수 있어야 합니다.
    *   ⭐ `str.strip()`, `str.lower()`와 같은 기본적인 텍스트 정규화 메서드의 사용법을 알고, 이를 `duplicated()`와 결합하여 유사 중복을 제거하는 로직을 이해해야 합니다.
    *   더 나아가, 악센트 제거 (`str.normalize("NFKD")`)나 정규 표현식을 사용한 문자열 교체 (`str.replace(r"\s+", "")`)와 같은 고급 정규화 기법의 필요성도 인지해야 합니다.

---

### **3. Winsorize via quantile clipping (분위수 기반 값 제한을 통한 윈저라이징)**

*   **핵심 개념**:
    윈저라이징(Winsorization)은 데이터의 극단적인 이상치(outliers)를 제거하는 대신, 특정 분위수(quantile) 값으로 대체하여 처리하는 통계 기법입니다. 이는 데이터 손실 없이 이상치의 영향을 완화하여, 평균이나 분산 같은 통계량의 안정성을 높이고 머신러닝 모델의 견고성(robustness)을 향상시키는 데 사용됩니다.

*   **코드/수식 해설**:
    ```python
    lo, hi = df["x"].quantile([0.01, 0.99])
    df["x_clip"] = df["x"].clip(lo, hi)
    ```
    *   `df["x"].quantile([0.01, 0.99])`: 'x' 컬럼의 값들을 기준으로 1% 분위수(하한 `lo`)와 99% 분위수(상한 `hi`)를 계산합니다. 이는 데이터의 하위 1%와 상위 1%에 해당하는 극단적인 값을 찾아내는 기준이 됩니다.
    *   `df["x"].clip(lo, hi)`: 'x' 컬럼의 각 값에 대해 다음 규칙을 적용합니다.
        *   값이 `lo`보다 작으면 `lo`로 대체합니다.
        *   값이 `hi`보다 크면 `hi`로 대체합니다.
        *   값이 `lo`와 `hi` 사이에 있으면 원래 값을 유지합니다.
    *   `df["x_clip"] = ...`: 윈저라이징 처리된 결과를 `x_clip`이라는 새로운 컬럼에 저장합니다. 이는 원본 데이터(`df["x"]`)를 보존하면서 이상치가 제한된 버전을 활용할 수 있게 해줍니다.

*   **구체적 예시**:
    가계 소득 데이터에서 소수의 매우 높은 소득자와 매우 낮은 소득자가 있을 경우, 이들이 전체 소득 평균이나 분산에 큰 영향을 미쳐 통계치를 왜곡할 수 있습니다. 예를 들어, 1% 분위수 소득이 100만원이고 99% 분위수 소득이 1억원이라면, 100만원 미만 소득자는 100만원으로, 1억원 초과 소득자는 1억원으로 값을 제한하는 것입니다. 이렇게 하면 이상치로 인한 통계적 왜곡을 줄이고, 소득 수준을 예측하는 머신러닝 모델이 더욱 안정적으로 학습될 수 있습니다.

*   **시험 포인트**:
    *   ⭐ 윈저라이징(Winsorization)의 개념과 이상치를 제거하는 방식(예: 단순 삭제)과의 차이점을 명확히 설명할 수 있어야 합니다. (데이터 손실 없이 이상치 영향 완화)
    *   ⭐ `quantile()` 메서드를 이용한 분위수 계산과 `clip()` 메서드를 이용한 값 제한 파이썬 코드를 이해하고 활용할 수 있어야 합니다.
    *   ⭐ 윈저라이징을 사용하는 주된 이유 (통계량 안정화, 모델 견고성 향상)와 그 실제 적용 사례를 설명할 수 있어야 합니다.
    *   원본 데이터를 보존하는 것(`x_raw` 언급)의 중요성도 함께 알아두세요.

---

## Slide 40

## 데이터 리셰이핑 (Long $\leftrightarrow$ Wide)

이 슬라이드는 데이터프레임의 형태를 변경하는 주요 기법인 `melt`, `pivot_table`, 그리고 `explode`에 대해 다룹니다. 데이터 분석 및 시각화를 위해 'tidy'한 형태로 데이터를 정리하거나, 특정 분석 목적에 맞게 데이터를 재구성할 때 사용됩니다.

---

### **1. Wide $\rightarrow$ Long (tidy) 변환: `df.melt()`**

*   **핵심 개념**: `melt` 함수는 여러 열에 퍼져 있는 값들을 하나의 '변수' 열과 하나의 '값' 열로 묶어 길고 깔끔한(long, tidy) 형태로 데이터를 변환합니다. 이는 데이터 시각화 라이브러리(예: `seaborn`)에서 각 변수를 개별적으로 다루기 용이하게 만들거나, 특정 변수(column)들을 기준으로 그룹화(groupby) 작업을 수행할 때 유용합니다.
*   **코드/수식 해설**:
    ```python
    long = df.melt(id_vars=["id"], var_name="k", value_name="v")
    ```
    *   `id_vars`: 고유 식별자로 유지할 열(들)을 지정합니다. 이 열들은 melt 과정에서 행을 식별하는 역할을 합니다.
    *   `var_name`: 원래 DataFrame의 열 이름(여기서는 'key' 역할을 하는 값)이 저장될 새로운 열의 이름을 지정합니다.
    *   `value_name`: 원래 DataFrame의 각 셀의 값(여기서는 'value' 역할을 하는 값)이 저장될 새로운 열의 이름을 지정합니다.
    *   **Tip**: `value_vars` 인자를 추가하여 특정 열들만 `melt` 작업에 포함시킬 수 있습니다.
*   **구체적 예시**:
    원본 `df` (Wide format):
    ```
       id  score_A  score_B
    0   1       90       85
    1   2       70       95
    ```
    `df.melt(id_vars=["id"], var_name="test", value_name="score")` 결과 (Long format):
    ```
       id     test  score
    0   1  score_A     90
    1   2  score_A     70
    2   1  score_B     85
    3   2  score_B     95
    ```
*   **시험 포인트**: ⭐ `melt`는 Wide 형식을 Tidy(Long) 형식으로 변환하는 기본 도구입니다. `id_vars`, `var_name`, `value_name`의 역할과 각 인자가 결과 DataFrame의 어떤 열을 만드는지 정확히 이해해야 합니다.

---

### **2. Long $\rightarrow$ Wide 변환: `long.pivot_table()`**

*   **핵심 개념**: `pivot_table` 함수는 Long 형식의 데이터를 다시 Wide 형식의 매트릭스 형태로 재구성합니다. 특정 열의 고유 값을 새로운 열(columns)로 만들고, 다른 열의 값을 채워 넣는 방식으로 동작합니다. 이는 통계적 요약이나 교차 분석에 유용합니다.
*   **코드/수식 해설**:
    ```python
    wide = (long.pivot_table(index="id", columns="k", values="v", aggfunc="first")
                 .reset_index())
    ```
    *   `index`: 새로운 DataFrame의 인덱스(행)가 될 열을 지정합니다.
    *   `columns`: 새로운 DataFrame의 열 이름이 될 열을 지정합니다. `k` 열의 고유 값들이 각각 새로운 열이 됩니다.
    *   `values`: 새로운 DataFrame의 셀을 채울 값이 있는 열을 지정합니다.
    *   `aggfunc`: `index`와 `columns` 조합에 해당하는 값이 여러 개일 경우, 이 값들을 어떻게 집계할지 지정하는 함수입니다. `'first'`, `'mean'`, `'sum'`, `'max'` 등이 될 수 있습니다.
    *   `.reset_index()`: `pivot_table`은 기본적으로 `index`로 지정된 열을 인덱스로 만드는데, 이를 일반 열로 되돌립니다.
    *   **Gotcha**: `aggfunc`를 지정하지 않고 중복된 `index`/`columns` 조합이 발생하면 오류가 발생합니다. 이 경우 `first`, `max` 또는 사용자 정의 함수와 같은 집계 함수를 반드시 사용해야 합니다.
*   **구체적 예시**:
    `long` (위의 melt 예시에서 생성된 Long format 데이터):
    ```
       id     test  score
    0   1  score_A     90
    1   2  score_A     70
    2   1  score_B     85
    3   2  score_B     95
    ```
    `long.pivot_table(index="id", columns="test", values="score", aggfunc="first")` 결과 (Wide format):
    ```
    test  score_A  score_B
    id                    
    1          90       85
    2          70       95
    ```
    `.reset_index()` 적용 후:
    ```
    test  id  score_A  score_B
    0      1       90       85
    1      2       70       95
    ```
*   **시험 포인트**: ⭐ `pivot_table`의 `index`, `columns`, `values`, `aggfunc` 각 인자의 역할과 `aggfunc`가 왜 필요한지(특히 중복 값이 있을 때)를 명확히 설명할 수 있어야 합니다. `reset_index()`의 사용 목적도 중요합니다.

---

### **3. 리스트와 같은 데이터 확장: `df.explode()`**

*   **핵심 개념**: `explode` 함수는 DataFrame의 특정 열에 리스트(또는 유사 iterable) 형태의 데이터가 있을 때, 리스트의 각 요소를 개별 행으로 확장합니다. 이는 다중 레이블(multi-label) 텍스트 데이터나 태그(tags)와 같은 데이터를 다룰 때 각 레이블/태그를 독립적인 행으로 분리하여 분석하기 용이하게 만듭니다.
*   **코드/수식 해설**:
    ```python
    expl = df.explode("tags", ignore_index=True)
    ```
    *   첫 번째 인자: 리스트 또는 iterable을 포함하는 열의 이름입니다.
    *   `ignore_index=True`: 폭발(explode) 후 생성된 새로운 DataFrame의 인덱스를 재설정하여 기본 정수 인덱스로 만듭니다. `False`인 경우, 원본 행의 인덱스를 유지합니다 (중복 발생).
*   **구체적 예시**:
    원본 `df` (tags 열에 리스트 데이터 포함):
    ```
       id             tags
    0   A      ['apple', 'banana']
    1   B               ['orange']
    2   C  ['apple', 'grape', 'kiwi']
    ```
    `df.explode("tags")` 결과:
    ```
       id    tags
    0   A   apple
    0   A  banana
    1   B  orange
    2   C   apple
    2   C   grape
    2   C    kiwi
    ```
*   **시험 포인트**: ⭐ `explode`가 어떤 상황에서 사용되는지 (예: 다중 레이블, 태그) 이해하고, 리스트 내 각 요소가 어떻게 독립적인 행으로 확장되는지 설명할 수 있어야 합니다. `ignore_index`의 역할도 중요합니다. `explode` 후에는 일반적으로 조회 테이블(lookup tables)과의 조인(join)을 통해 태그 수준의 특징(features)을 엔지니어링하는 데 활용될 수 있습니다.

---

## Slide 41

POSTECH 컴퓨터공학과 전공 튜터로서 데이터분석 입문 강의 슬라이드에 대한 노트를 작성합니다.

---

### **핵심 개념**
이 슬라이드는 데이터 전처리 과정에서 자주 발생하는 세 가지 핵심적인 문제를 다룹니다:
1.  **Join Hygiene**: 데이터프레임 병합(merge) 시 발생할 수 있는 데이터 중복(fanout)이나 누락 문제를 사전에 검증하고 감사(audit)하는 방법입니다.
2.  **Text Cleanup**: 텍스트 데이터의 일관성을 확보하기 위해 유니코드 정규화, 공백 제거, 대소문자 통일 등을 수행하는 방법입니다.
3.  **Datetime Gotchas**: 다양한 형식의 날짜/시간 데이터를 표준화된 datetime 객체로 변환하고, 오류를 안전하게 처리하며, UTC로 시간대를 통일하는 방법입니다.

### **코드/수식 해설**

**1. Join hygiene: validate & audit**
```python
merged = pd.merge(A, B, on="key", how="left", validate="one_to_one", indicator=True)
anti = merged.loc[merged["_merge"]=="left_only", "key"]
```
*   `pd.merge(A, B, on="key", how="left", ...)`: `A`와 `B` 두 데이터프레임을 `key` 컬럼을 기준으로 `left` 조인합니다.
*   `validate="one_to_one"`: ⭐가장 중요한 파라미터 중 하나로, 조인 키 `key`가 `A`와 `B` 양쪽에 모두 유일해야 함을 강제합니다. 만약 이 조건이 만족되지 않으면(`A` 또는 `B`에 `key`가 중복되는 경우), `pd.merge`는 `MergeError`를 발생시켜 예상치 못한 데이터 복제(fanout)를 방지합니다. 다른 옵션으로는 `one_to_many`, `many_to_one`, `many_to_many`가 있습니다.
*   `indicator=True`: 병합 결과에 `_merge`라는 새로운 컬럼을 추가합니다. 이 컬럼은 각 행이 어디에서 왔는지(`'left_only'`, `'right_only'`, `'both'`)를 나타냅니다. `how` 인자에 따라 `right_only`는 나타나지 않을 수 있습니다 (예: `how="left"`인 경우).
*   `anti = merged.loc[merged["_merge"]=="left_only", "key"]`: `indicator=True`로 생성된 `_merge` 컬럼을 활용하여, 왼쪽 데이터프레임(`A`)에는 존재하지만 오른쪽 데이터프레임(`B`)에는 매칭되는 `key`가 없었던 행들의 `key` 값을 추출합니다. 이는 매칭되지 않은 데이터를 감사하는 데 유용합니다.

**2. Text cleanup**
```python
s = (df["title"]
     .str.normalize("NFKC")
     .str.strip()
     .str.lower())
```
*   `df["title"].str`: `df` 데이터프레임의 "title" 컬럼(Series)에 대해 문자열(string) 관련 메서드를 적용하기 위한 접근자입니다.
*   `.str.normalize("NFKC")`: 유니코드 문자열을 정규화합니다. "NFKC" (Normalization Form Compatibility Composition)는 호환성 문자를 표준 문자로 변환하여 비교 시 일관성을 확보합니다 (예: '½'를 '1/2'로, 'ﬁ'를 'fi'로).
*   `.str.strip()`: 문자열 양 끝의 공백(whitespace)을 제거합니다.
*   `.str.lower()`: 문자열의 모든 대문자를 소문자로 변환하여 대소문자로 인한 불일치를 제거합니다.

**3. Datetime gotchas**
```python
df["ts"] = pd.to_datetime(df["ts"], errors="coerce", utc=True)
```
*   `pd.to_datetime(df["ts"], ...)`: `df`의 "ts" 컬럼에 있는 문자열이나 다른 형식의 데이터를 Pandas `datetime` 객체로 변환합니다.
*   `errors="coerce"`: ⭐날짜/시간 변환 시 오류가 발생하면, 해당 값을 `NaT` (Not a Time)로 강제 변환합니다. 이는 잘못된 형식의 데이터 때문에 전체 파싱 작업이 중단되는 것을 방지하여 대규모 데이터셋 처리 시 유용합니다. 기본값은 `raise`로 오류 발생 시 예외를 발생시킵니다.
*   `utc=True`: ⭐파싱된 `datetime` 객체를 협정 세계시(UTC)로 변환합니다. 이는 다양한 시간대에서 수집된 데이터를 일관된 기준으로 비교하고 분석할 수 있게 해줍니다.

### **구체적 예시**

**1. Join hygiene**
회원 정보 (`df_members`: `id`, `name`)와 구매 기록 (`df_purchases`: `id`, `item`, `price`)이 있다고 가정합시다.
`pd.merge(df_members, df_purchases, on='id', how='left', validate='one_to_many', indicator=True)`
*   `validate='one_to_many'`: 한 회원이 여러 번 구매할 수 있으므로, `df_members`의 `id`는 유일하지만 `df_purchases`의 `id`는 중복될 수 있음을 명시합니다. 만약 `df_members`에 `id`가 중복되어 있다면 오류가 발생하여 잘못된 회원 데이터 입력을 즉시 알 수 있습니다.
*   `indicator=True`: 병합 후 `_merge` 컬럼을 통해 `left_only`인 행을 찾아 `df_members`에는 있지만 구매 기록이 없는 회원을 쉽게 식별할 수 있습니다.

**2. Text cleanup**
상품 이름 데이터가 `["  Apple Inc. ", "apple inc", "Apple Inc.", "Äpple Inc."]`와 같다고 가정합니다.
```python
product_names = pd.Series(["  Apple Inc. ", "apple inc", "Apple Inc.", "Äpple Inc."])
cleaned_names = (product_names
                 .str.normalize("NFKC")  # "Äpple" -> "Apple" (유니코드 호환성 문자 정규화)
                 .str.strip()           # "  Apple Inc. " -> "Apple Inc."
                 .str.lower())          # "Apple Inc." -> "apple inc."
print(cleaned_names)
# 결과:
# 0    apple inc.
# 1    apple inc
# 2    apple inc.
# 3    apple inc.
# dtype: object
```
이 과정을 통해 모든 이름이 `apple inc.` 또는 `apple inc`와 유사한 형태로 통일되어, 동일한 상품을 정확하게 매칭하거나 집계할 수 있습니다.

**3. Datetime gotchas**
웹 서버 로그의 `timestamp` 컬럼이 `["2023-10-26 14:30:00", "October 27, 2023", "Invalid Log Entry", "2023-10-28 10:00:00 PST"]`와 같다고 가정합니다.
```python
log_timestamps = pd.Series(["2023-10-26 14:30:00", "October 27, 2023", "Invalid Log Entry", "2023-10-28 10:00:00 PST"])
parsed_timestamps = pd.to_datetime(log_timestamps, errors="coerce", utc=True)
print(parsed_timestamps)
# 결과:
# 0   2023-10-26 14:30:00+00:00
# 1   2023-10-27 00:00:00+00:00
# 2                         NaT
# 3   2023-10-28 18:00:00+00:00  (PST는 UTC-8이므로 10시 PST는 18시 UTC)
# dtype: datetime64[ns, UTC]
```
`errors="coerce"` 덕분에 "Invalid Log Entry"는 `NaT`로 변환되어 오류 없이 진행됩니다. `utc=True`로 모든 시간이 UTC 기준으로 통일되어 시간대 차이로 인한 분석 오류를 방지할 수 있습니다. 변환 후 `parsed_timestamps.dt.hour` 등으로 시간 정보를 쉽게 추출할 수 있습니다.

### **시험 포인트**

*   ⭐`pd.merge` 사용 시 `validate` 파라미터가 데이터 무결성 검증 및 'fanout' 방지에 어떻게 기여하는지 설명할 수 있어야 합니다. 특히 `one_to_one`, `one_to_many` 등의 의미를 이해해야 합니다.
*   ⭐`indicator=True` 옵션이 추가하는 `_merge` 컬럼의 역할과 `left_only`, `both` 등의 값의 의미를 알고 있어야 합니다. 이를 활용하여 매칭되지 않은 데이터를 식별하는 방법을 설명할 수 있어야 합니다.
*   ⭐텍스트 클리닝에서 `Series.str` 접근자를 활용하여 `normalize("NFKC")`, `strip()`, `lower()`와 같은 메서드를 적용하는 방법을 코드로 작성하고 각 메서드의 역할을 설명할 수 있어야 합니다.
*   ⭐`pd.to_datetime` 함수에서 `errors="coerce"` 파라미터가 유효하지 않은 날짜/시간 데이터를 어떻게 처리하는지(`NaT`로 변환) 설명하고, 이것이 데이터 클리닝에 왜 중요한지 설명할 수 있어야 합니다.
*   ⭐`pd.to_datetime` 함수에서 `utc=True` 파라미터의 역할(시간대 표준화)과 데이터 분석 시 그 중요성을 설명할 수 있어야 합니다.
*   ⭐파싱된 `datetime` Series에서 `.dt` 접근자를 사용하여 연도, 월, 일, 시간 등 세부 시간 정보를 추출하는 방법을 알아야 합니다.

---

## Slide 42

**핵심 개념**
*   **그룹별 특성 공학 (Group-aware Feature Engineering)**: 데이터 내 특정 그룹(예: 'store' 별)의 통계적 특성(평균, 표준편차, 순위, 이동 평균 등)을 활용하여 새로운 특성(feature)을 생성하는 기법입니다. 이는 개별 엔티티를 더 공정하게 비교하고, 추세(momentum)나 계절성(seasonality)을 포착하는 데 중요합니다.
*   **멱등성 체이닝 (Idempotent Chaining)**: 데이터 처리 단계를 여러 메소드를 연속적으로 연결하여(메소드 체이닝) 하나의 파이프라인으로 구성하는 기법입니다. 각 연산이 원본 데이터를 직접 수정하지 않고 새로운 데이터프레임을 반환하도록 설계하여, 동일한 연산을 여러 번 수행해도 항상 같은 결과를 보장하는 멱등성(Idempotent)을 유지합니다. 이는 코드의 가독성, 디버깅 용이성, 재현성(reproducibility)을 크게 향상시킵니다.

**코드/수식 해설**

**1. 그룹별 Z-score, 순위, 이동 평균 계산**

```python
# g = df.groupby("store")["sales"] # 미리 그룹 객체 생성
# Z-score 계산: 각 매장(store)별 sales의 평균과 표준편차를 사용하여 표준화
df["z"] = (df["sales"] - g.transform("mean")) / g.transform("std")

# 순위 계산: 각 매장(store)별 sales 값을 기준으로 내림차순 순위 부여 (동일 값은 연속 순위)
df["rank"] = g.rank(ascending=False, method="dense")

# 이동 평균(Rolling Mean) 계산:
# 1. 롤링 연산을 위해 'store'와 'ts'(시계열) 기준으로 데이터 정렬
df = df.sort_values([["store", "ts"]])
# 2. 각 매장별 sales에 대해 7일 이동 평균 계산 (최소 1개의 데이터로도 계산 허용)
df["roll7"] = (df.groupby("store")["sales"]
               .rolling(7, min_periods=1)
               .mean()
               .reset_index(level=0, drop=True))
```

*   **Z-score 수식**:
    각 그룹 내 데이터 포인트 $x$에 대한 Z-score는 다음과 같이 계산됩니다.
    $$ z = \frac{x - \mu}{\sigma} $$
    여기서 $\mu$는 해당 그룹의 평균이고, $\sigma$는 해당 그룹의 표준편차입니다. `transform("mean")`과 `transform("std")`는 그룹별 평균과 표준편차를 계산하여 원본 DataFrame의 인덱스와 동일하게 브로드캐스팅(broadcasting)합니다.
*   `g.rank(ascending=False, method="dense")`: `ascending=False`는 값이 클수록 1위가 되도록, `method="dense"`는 동일한 값이 있을 경우 순위가 끊어지지 않고 연속적으로 부여되도록 합니다 (예: 1, 2, 2, 3).
*   `rolling(7, min_periods=1)`: 윈도우 크기를 7로 설정하고, 윈도우 내 최소 데이터가 1개만 있어도 연산을 수행합니다.
*   `reset_index(level=0, drop=True)`: `groupby`와 `rolling` 연산은 MultiIndex를 생성할 수 있는데, `level=0` 인덱스(여기서는 'store' 인덱스)를 해제하고 데이터프레임에서 제거(`drop=True`)하여 원래 DataFrame에 쉽게 병합할 수 있도록 합니다.

**2. 멱등성 체이닝 (Idempotent Chaining) with assign/pipe**

```python
tidy = (df
        .pipe(lambda d: d.dropna(subset=["y"])) # 'y' 컬럼에 결측치가 있는 행 제거
        .assign(x=lambda d: d["x"].fillna(d["x"].median())) # 'x' 컬럼의 결측치를 중앙값으로 채우기
        .sort_values([["id", "ts"]])) # 'id'와 'ts' 기준으로 정렬
```

*   `pipe(lambda d: d.dropna(subset=["y"]))`: `pipe()`는 DataFrame을 인자로 받아 DataFrame을 반환하는 함수를 메소드 체이닝 중간에 적용할 수 있게 합니다. `lambda d:`는 이전 단계의 DataFrame을 `d`로 받아 처리합니다. 여기서는 `y` 컬럼에 결측치가 있는 행을 제거합니다.
*   `assign(x=lambda d: d["x"].fillna(d["x"].median()))`: `assign()`은 새로운 컬럼을 생성하거나 기존 컬럼을 갱신할 때 사용합니다. 원본 DataFrame을 변경하지 않고 새로운 DataFrame을 반환하므로 체이닝에 적합합니다. 여기서는 `x` 컬럼의 결측치를 해당 컬럼의 중앙값으로 채웁니다. `lambda d:`를 사용하여 현재까지 처리된 DataFrame `d`의 `x` 컬럼 중앙값을 계산합니다.
*   `sort_values([["id", "ts"]])`: 최종적으로 `id`와 `ts` 컬럼을 기준으로 정렬합니다.

**구체적 예시**

*   **그룹별 Z-score**: 전국 각지에 체인점을 둔 패스트푸드점에서 특정 지점의 일일 매출이 다른 지점들과 비교했을 때 어느 정도인지 알고 싶을 때 사용합니다. 예를 들어, A 지점의 매출이 100만 원인데 다른 지점들의 평균 매출이 80만 원이고 표준편차가 10만 원이라면, A 지점은 평균보다 훨씬 높은 성과를 낸 것입니다. Z-score는 이러한 상대적인 위치를 수치화하여 공정한 비교를 가능하게 합니다.
*   **그룹별 이동 평균**: 백화점의 요일별 고객 방문 데이터가 있을 때, 주말과 평일의 방문객 수가 크게 다를 수 있습니다. 이럴 때 '백화점 지점별'로 '지난 7일간의 이동 평균 고객 수'를 계산하면, 일시적인 요일별 변동보다는 실제 고객 방문 추세(momentum)를 더 잘 파악할 수 있습니다.
*   **멱등성 체이닝**: 원본 고객 데이터에서
    1.  먼저 `배송 주소`가 비어있는 고객 정보는 삭제하고 (`dropna` via `pipe`),
    2.  이후 `구매 금액`이 비어있는 고객은 해당 고객 그룹의 `평균 구매 금액`으로 대체하며 (`assign` + `fillna`),
    3.  마지막으로 `고객 ID`와 `가입일` 순서로 정렬하여 (`sort_values`) 깔끔하게 정리된 고객 목록 `tidy`를 얻는 일련의 과정을 하나의 코드 블록으로 작성하는 것입니다. 각 단계가 독립적으로 작동하고, 어떤 단계에서 문제가 발생해도 디버깅이 용이하며, 전체 과정을 재실행해도 항상 동일한 결과를 얻을 수 있습니다.

**시험 포인트**

*   ⭐ `groupby().transform()`과 `groupby().apply()`의 차이점: `transform()`은 브로드캐스팅을 통해 원래 DataFrame의 크기에 맞는 Series를 반환하여 새로운 컬럼 추가에 용이하고, `apply()`는 그룹별로 연산을 적용한 결과를 반환합니다.
*   ⭐ 그룹별 Z-score 계산식 ($z = \frac{x - \mu}{\sigma}$)과 이를 pandas 코드로 구현하는 방식.
*   ⭐ `rolling()` 연산 시 `df.sort_values()`로 정렬하는 이유와 `min_periods` 인자의 역할.
*   ⭐ `pandas.pipe()`와 `pandas.assign()` 메소드의 역할 및 이들이 메소드 체이닝과 멱등성에 기여하는 방식. 특히 `lambda` 함수를 활용하는 구문.
*   ⭐ "멱등성(Idempotency)"이 데이터 파이프라인 설계에서 왜 중요한 개념인지 (재현성, 디버깅, 안정성 측면).

---

