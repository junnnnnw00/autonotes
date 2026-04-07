# PPT 상세 해설 노트

## Slide 1

이번 슬라이드의 핵심 개념은 **Pandas 라이브러리의 `DataFrame`을 활용한 데이터의 기본적인 조작(CRUD)과 특정 조건에 맞는 데이터 검색(Query)**입니다.

---

### 1. Pandas DataFrame 개요 (간략)

`DataFrame`은 Pandas에서 데이터를 다루는 핵심 구조로, 엑셀 스프레드시트나 SQL 테이블처럼 행과 열로 이루어진 2차원 테이블 형태의 데이터를 저장하고 관리합니다. 각 열은 특정 데이터 타입을 가지며, 다양한 통계 분석 및 데이터 처리 작업을 수행할 수 있도록 해줍니다.

### 2. CRUD (Create, Read, Update, Delete) with DataFrames

CRUD는 데이터베이스 시스템의 기본적인 네 가지 작업을 의미하며, Pandas `DataFrame`에서도 이와 유사한 방식으로 데이터를 생성, 조회, 수정, 삭제할 수 있습니다.

#### 예시 시나리오: 온라인 쇼핑몰의 '주문 목록' 데이터

온라인 쇼핑몰에서 고객의 주문 내역을 `DataFrame`으로 관리한다고 가정해 봅시다. 데이터는 다음과 같은 형태일 수 있습니다:

| 주문ID | 고객ID | 상품명 | 수량 | 가격 | 주문일자 | 상태 |
|---|---|---|---|---|---|---|
| 1001 | A001 | 노트북 | 1 | 1200000 | 2023-10-26 | 배송 완료 |
| 1002 | B002 | 스마트폰 | 2 | 800000 | 2023-10-27 | 배송 중 |
| 1003 | A001 | 마우스 | 1 | 30000 | 2023-10-27 | 배송 중 |

```python
import pandas as pd

# 초기 DataFrame 생성 (Read의 일부)
data = {
    '주문ID': [1001, 1002, 1003],
    '고객ID': ['A001', 'B002', 'A001'],
    '상품명': ['노트북', '스마트폰', '마우스'],
    '수량': [1, 2, 1],
    '가격': [1200000, 800000, 30000],
    '주문일자': ['2023-10-26', '2023-10-27', '2023-10-27'],
    '상태': ['배송 완료', '배송 중', '배송 중']
}
df_orders = pd.DataFrame(data)
print("--- 초기 주문 목록 DataFrame ---")
print(df_orders)
print("\n")
```

#### 2.1. Create (생성)

새로운 데이터를 `DataFrame`에 추가하는 작업입니다.

*   **새로운 행 추가:** 새로운 주문이 들어왔을 때 `DataFrame`에 새로운 레코드를 추가합니다.
*   **새로운 열 추가:** 예를 들어, '총 결제 금액'과 같은 새로운 파생 정보를 계산하여 열로 추가할 수 있습니다.

```python
# 1) 새로운 주문(행) 추가
new_order = pd.DataFrame([
    {'주문ID': 1004, '고객ID': 'C003', '상품명': '키보드', '수량': 1, '가격': 50000, '주문일자': '2023-10-28', '상태': '주문 접수'}
])
df_orders = pd.concat([df_orders, new_order], ignore_index=True)
print("--- 1) 새로운 주문 추가 후 DataFrame ---")
print(df_orders)
print("\n")

# 2) 새로운 열 추가: '총 결제 금액' (수량 * 가격)
df_orders['총 결제 금액'] = df_orders['수량'] * df_orders['가격']
print("--- 2) '총 결제 금액' 열 추가 후 DataFrame ---")
print(df_orders)
print("\n")
```

#### 2.2. Read (조회)

`DataFrame`에서 데이터를 확인하는 작업입니다. 전체 데이터를 보거나, 특정 행/열만 선택하여 볼 수 있습니다. (이 부분은 Query와 밀접하게 관련됩니다.)

```python
# 1) 특정 열(예: 상품명, 가격)만 조회
print("--- 1) '상품명'과 '가격' 열 조회 ---")
print(df_orders[['상품명', '가격']])
print("\n")

# 2) 상위 2개의 행만 조회 (head() 메서드)
print("--- 2) 상위 2개 주문 조회 ---")
print(df_orders.head(2))
print("\n")
```

#### 2.3. Update (수정)

기존 `DataFrame`의 데이터를 변경하는 작업입니다.

*   **특정 값 변경:** 예를 들어, '주문ID 1002'의 '상태'를 '배송 중'에서 '배송 완료'로 변경할 수 있습니다.
*   **여러 값 일괄 변경:** 특정 조건에 맞는 모든 상품의 가격을 일괄 인상할 수도 있습니다.

```python
# 1) 특정 주문의 상태 업데이트 (예: 주문ID 1002의 상태를 '배송 완료'로 변경)
df_orders.loc[df_orders['주문ID'] == 1002, '상태'] = '배송 완료'
print("--- 1) 주문ID 1002 상태 업데이트 후 DataFrame ---")
print(df_orders)
print("\n")

# 2) 특정 조건의 여러 값 일괄 업데이트 (예: '키보드' 가격을 55000으로 인상)
df_orders.loc[df_orders['상품명'] == '키보드', '가격'] = 55000
df_orders['총 결제 금액'] = df_orders['수량'] * df_orders['가격'] # 총 결제 금액 재계산
print("--- 2) '키보드' 가격 인상 후 DataFrame ---")
print(df_orders)
print("\n")
```

#### 2.4. Delete (삭제)

`DataFrame`에서 특정 데이터(행 또는 열)를 제거하는 작업입니다.

*   **행 삭제:** 특정 '주문ID'에 해당하는 주문을 취소하여 삭제할 수 있습니다.
*   **열 삭제:** 더 이상 필요 없는 '고객ID'와 같은 열을 삭제할 수 있습니다.

```python
# 1) 특정 주문(행) 삭제 (예: 주문ID 1003 삭제)
df_orders = df_orders[df_orders['주문ID'] != 1003]
print("--- 1) 주문ID 1003 삭제 후 DataFrame ---")
print(df_orders)
print("\n")

# 2) 특정 열 삭제 (예: '주문일자' 열 삭제)
df_orders = df_orders.drop(columns=['주문일자'])
print("--- 2) '주문일자' 열 삭제 후 DataFrame ---")
print(df_orders)
print("\n")
```

---

### 3. Query over DataFrames (데이터 질의)

`Query`는 `DataFrame`에서 특정 조건을 만족하는 데이터를 필터링하여 찾아내는 과정입니다. SQL의 `WHERE` 절과 유사하게 작동하며, 데이터 분석에서 가장 중요하고 자주 사용되는 기능 중 하나입니다.

#### 예시 시나리오: (위에서 업데이트된) 온라인 쇼핑몰의 '주문 목록' 데이터에서 특정 조건의 주문 찾기

```python
# 현재 df_orders 상태
#    주문ID 고객ID   상품명  수량     가격    상태   총 결제 금액
# 0  1001  A001  노트북   1  1200000  배송 완료     1200000
# 1  1002  B002 스마트폰   2   800000  배송 완료     1600000
# 3  1004  C003  키보드   1    55000  주문 접수       55000
```

```python
# 1) '배송 완료' 상태인 주문만 조회
delivered_orders = df_orders[df_orders['상태'] == '배송 완료']
print("--- 1) '배송 완료' 상태인 주문 ---")
print(delivered_orders)
print("\n")

# 2) '가격'이 100000원 이상인 주문만 조회
expensive_orders = df_orders[df_orders['가격'] >= 100000]
print("--- 2) '가격'이 10만원 이상인 주문 ---")
print(expensive_orders)
print("\n")

# 3) 여러 조건 결합: '고객ID'가 'A001'이고 '총 결제 금액'이 100만원 이상인 주문
specific_customer_expensive_orders = df_orders[(df_orders['고객ID'] == 'A001') & (df_orders['총 결제 금액'] >= 1000000)]
print("--- 3) 고객 A001의 100만원 이상 주문 ---")
print(specific_customer_expensive_orders)
print("\n")

# 4) 특정 단어가 포함된 상품명 찾기 (예: '스마트'가 들어간 상품)
# Python의 .str.contains() 메서드를 활용합니다.
smartphone_related_orders = df_orders[df_orders['상품명'].str.contains('스마트', na=False)]
print("--- 4) '스마트'가 포함된 상품명의 주문 ---")
print(smartphone_related_orders)
print("\n")
```

**요약:**
*   `DataFrame`은 데이터를 테이블 형태로 관리하는 Pandas의 핵심 구조입니다.
*   **CRUD**는 `DataFrame` 내에서 데이터를 **생성(Create)**, **조회(Read)**, **수정(Update)**, **삭제(Delete)**하는 기본적인 연산을 의미합니다.
*   **Query**는 특정 조건(들)을 사용하여 `DataFrame`에서 원하는 데이터의 부분집합을 **선택(Select)**하는 강력한 기능입니다. 이는 `Read` 작업의 핵심적인 부분이며, 실제 데이터 분석에서 데이터 탐색과 전처리에 필수적으로 활용됩니다.

이러한 CRUD 및 Query 기능들을 숙달하면 어떤 형태의 테이블 데이터라도 효율적으로 다루고 분석할 수 있게 될 것입니다.

---

## Slide 2

다음은 슬라이드의 학습 목표에 대한 핵심 개념과 구체적인 실생활 예시입니다.

---

### **1. CRUD for pandas: Create, Update, Delete, Query**

*   **핵심 개념:** CRUD는 대부분의 데이터 관리 시스템에서 데이터를 다루는 기본적인 네 가지 작업(생성, 읽기, 업데이트, 삭제)의 약자입니다. Pandas DataFrame에서도 이와 유사하게 데이터를 추가하고, 조회하고, 수정하고, 제거하는 기능을 수행할 수 있습니다.

*   **실생활 예시:** 학교의 **도서관 장서 관리 시스템**을 상상해 봅시다.
    *   **Create (생성):** 새로 구매한 책(`도서명`, `저자`, `출판사`, `ISBN`)을 시스템에 **추가**합니다.
    *   **Query (조회):** 특정 저자의 책을 **검색**하거나, '컴퓨터 공학' 카테고리의 모든 책을 **목록으로 확인**합니다.
    *   **Update (수정):** 어떤 책의 보관 장소가 바뀌거나, 대출 가능 여부(`대출_가능_여부`)가 변경될 때 해당 책의 정보를 **업데이트**합니다.
    *   **Delete (삭제):** 너무 낡아서 폐기된 책이나 분실된 책의 정보를 시스템에서 **제거**합니다.

### **2. ERA Operators: Formal definitions + pandas counterparts**

*   **핵심 개념:** ERA는 '확장 관계 대수(Extended Relational Algebra)'의 약자로, 데이터를 수학적이고 논리적인 연산을 통해 조작하는 공식적인 방법을 제공합니다. Pandas는 이러한 이론적인 관계 대수 연산에 해당하는 실제적인 프로그래밍 함수나 메서드를 제공하여 데이터를 처리할 수 있게 합니다. 이 목표는 이론적인 연산의 의미와 그에 대응하는 pandas 코드를 연결하는 것입니다.

*   **실생활 예시:** 온라인 **음악 스트리밍 서비스의 사용자 데이터**를 분석한다고 가정해 봅시다.
    *   **Formal Definition (이론적 정의):**
        *   **선택 (Selection, $\sigma$):** 특정 조건을 만족하는 행(튜플)을 필터링하는 연산입니다. 예를 들어, '장르가 팝'인 곡만 선택합니다.
        *   **투영 (Projection, $\pi$):** 특정 열(속성)만 추출하여 새로운 테이블을 만드는 연산입니다. 예를 들어, '곡명'과 '아티스트' 열만 추출합니다.
    *   **Pandas Counterparts (판다스 대응):**
        *   **선택 (Selection):** `df[df['장르'] == 'POP']` 또는 `df.loc[df['재생_횟수'] > 1000]` 과 같이 조건부 인덱싱을 사용하여 특정 조건을 만족하는 행을 선택합니다.
        *   **투영 (Projection):** `df[['곡명', '아티스트']]` 와 같이 열 이름 리스트를 사용하여 원하는 열만 추출합니다.
    *   이론적인 관계 대수 연산의 '의도'를 pandas의 메서드를 통해 '구현'하는 방법을 배우는 것이 핵심입니다.

### **3. Grouping/Pivoting: ERA $\gamma$ (grouping/aggregation) and pivot tables**

*   **핵심 개념:**
    *   **Grouping ($\gamma$, 그룹화/집계):** 특정 기준에 따라 데이터를 여러 그룹으로 나눈 후, 각 그룹에 대해 합계, 평균, 개수 등과 같은 집계 함수를 적용하여 요약된 결과를 얻는 연산입니다. 관계 대수에서는 $\gamma$ (감마) 연산으로 표현됩니다.
    *   **Pivoting (피벗 테이블):** 데이터를 재구성하고 요약하여, 특정 열의 고유 값을 새로운 열로 변환하고 다른 열을 기준으로 집계 값을 계산하여 표 형태로 보여주는 기술입니다. 여러 변수 간의 관계를 한눈에 파악하기 용이합니다.

*   **실생활 예시:** 한 **온라인 쇼핑몰의 판매 데이터**를 분석한다고 생각해 봅시다.
    *   **Grouping (그룹화/집계):**
        *   **시나리오:** "우리 쇼핑몰에서 **카테고리별**로 팔린 상품의 **총 판매액**은 얼마일까?"
        *   **설명:** 이 질문에 답하기 위해 판매 데이터를 '의류', '가전', '식품' 등의 '카테고리'로 **그룹화**합니다. 각 그룹 안에서 해당 카테고리에 속한 모든 상품의 '판매액'을 **합산(SUM)**하여 각 카테고리별 총 판매액을 구합니다.
        *   **Pandas:** `df.groupby('카테고리')['판매액'].sum()`
    *   **Pivoting (피벗 테이블):**
        *   **시나리오:** "지난 3개월간 **월별**로 각 **카테고리**의 **평균 판매 단가**는 어떻게 변동했을까?"
        *   **설명:** 이 질문에는 피벗 테이블이 유용합니다. 행(index)에는 '월'을, 열(columns)에는 '카테고리'를 놓고, 각 셀에는 해당 월과 카테고리의 '판매 단가'의 '평균'을 나타내도록 데이터를 재구성합니다. 이를 통해 월별-카테고리별 패턴을 쉽게 파악할 수 있습니다.
        *   **Pandas:** `df.pivot_table(index='월', columns='카테고리', values='판매_단가', aggfunc='mean')`

### **4. Semantics: State the ERA query and describe its meaning before code.**

*   **핵심 개념:** 이 목표는 코드를 작성하기 전에, 해결하려는 문제나 분석 목표를 명확하게 이해하고, 이를 관계 대수 쿼리(ERA query)와 같은 공식적인 언어로 명시하며, 그 의미를 정확히 설명하는 것의 중요성을 강조합니다. 즉, "무엇을 얻고자 하는가?"에 대한 명확한 논리적 사고가 "어떻게 코드를 작성할 것인가?"보다 선행되어야 함을 의미합니다.

*   **실생활 예시:** 한 **대학의 학생 성적 데이터베이스**에서 특정 정보를 추출하려 합니다.
    *   **시나리오:** "우리 학과에서 **평균 학점이 3.5 이상**이고, **3학년인 학생들의 이름과 전공만** 알고 싶다."
    *   **의미 정의 (Semantics) - 코딩 전 사고 과정:**
        1.  **어떤 데이터를 볼 것인가?** 전체 학생들의 성적 데이터.
        2.  **어떤 학생들을 선택할 것인가?**
            *   '학과'가 우리 학과인 학생.
            *   그중에서 '평균 학점'이 3.5 이상인 학생.
            *   그리고 '학년'이 3학년인 학생.
        3.  **선택된 학생들 중 무엇을 볼 것인가?** 그 학생들의 '이름'과 '전공' 정보.
    *   **ERA Query (가상):** $\pi_{\text{이름, 전공}}(\sigma_{\text{학과='우리 학과'} \land \text{평균 학점} \ge 3.5 \land \text{학년=3}}(\text{학생_성적_데이터}))$
    *   **설명:** 이 ERA 쿼리는 '학생_성적_데이터' 테이블에서 먼저 '학과가 우리 학과이고 평균 학점이 3.5 이상이며 학년이 3인' 모든 행(학생)을 선택한 다음, 그 결과에서 '이름'과 '전공' 열만을 추출하여 보여준다는 의미입니다.
    *   **이점:** 이렇게 의미를 명확히 정의하고 이론적 쿼리 형태로 구체화하면, `df[(df['학과'] == '우리 학과') & (df['평균 학점'] >= 3.5) & (df['학년'] == 3)][['이름', '전공']]`와 같은 pandas 코드를 훨씬 정확하고 논리적으로 작성할 수 있으며, 코드의 의도 또한 명확해집니다.

---

## Slide 3

## Pandas DataFrame 생성 및 기본 구조 이해

이 슬라이드는 **Pandas 라이브러리를 사용하여 기본적인 DataFrame을 생성하고 그 구조를 확인하는 방법**을 보여줍니다.

### 1. Pandas 및 NumPy 라이브러리 임포트

```python
import pandas as pd
import numpy as np
```

*   **핵심 개념:** `import` 문은 파이썬 외부 라이브러리를 현재 코드에서 사용할 수 있도록 불러오는 역할을 합니다. `as pd`와 `as np`는 각각 `pandas`와 `numpy` 라이브러리에 `pd`, `np`라는 짧은 별명을 붙여 코드를 더 간결하게 작성할 수 있게 합니다.
*   **구체적인 예시:** 마치 요리사가 특정한 요리를 만들기 위해 '오븐'이나 '믹서' 같은 전문 도구를 주방에 가져다 놓는 것과 같습니다. `import pandas as pd`는 우리가 데이터를 요리(분석)하기 위해 'Pandas 데이터 분석 도구'를 준비하고, 앞으로는 간단히 'pd'라고 부르겠다는 의미입니다. 여기서는 NumPy가 직접 사용되지는 않지만, Pandas와 함께 데이터 분석에 자주 쓰이는 수학 및 배열 연산 라이브러리입니다.

### 2. Python 딕셔너리를 활용한 데이터 준비

```python
data = {'State': ['CA']*4, 'Sex': ['F']*4, 'Year': [1910]*4,
        'Name': ['Mary', 'Helen', 'Dorothy', 'Margaret'],
        'Count': [295, 239, 220, 163]}
```

*   **핵심 개념:** 데이터를 **딕셔너리(Dictionary)** 형태로 준비합니다. 딕셔너리의 **키(Key)**는 생성될 DataFrame의 **컬럼(열) 이름**이 되고, **값(Value)**은 해당 컬럼에 들어갈 **데이터 리스트(List)**가 됩니다. 이때, 모든 리스트의 길이는 동일해야 합니다.
    *   `['CA']*4`와 같이 리스트에 단일 값을 곱하면 해당 값을 여러 번 반복하는 리스트를 쉽게 생성할 수 있습니다. (예: `['CA', 'CA', 'CA', 'CA']`)
*   **구체적인 예시:** 학교에서 학생들의 정보를 관리한다고 가정해 봅시다.
    *   `'State': ['CA']*4`는 "주(State)"라는 항목(컬럼)에 모든 학생이 "CA" 주 출신이라고 기록하는 것과 같습니다. 4명의 학생 모두 같은 주에 살고 있으므로, 4번 반복해서 입력합니다.
    *   `'Name': ['Mary', 'Helen', 'Dorothy', 'Margaret']`는 "이름"이라는 항목(컬럼)에 각 학생의 이름을 순서대로 기록하는 것과 같습니다.
    *   이 딕셔너리는 마치 "주", "성별", "출생연도", "이름", "인구수"라는 제목의 서랍(컬럼)에 각 서랍에 들어갈 내용물(데이터 리스트)을 미리 준비해 둔 상태와 같습니다.

### 3. DataFrame 생성

```python
babynames = pd.DataFrame(data)
```

*   **핵심 개념:** `pd.DataFrame()` 함수는 준비된 딕셔너리 `data`를 Pandas의 핵심 자료구조인 **DataFrame**으로 변환합니다. DataFrame은 행(row)과 열(column)로 이루어진 테이블 형태의 데이터 구조로, 엑셀 스프레드시트나 데이터베이스 테이블과 유사합니다.
*   **구체적인 예시:** 위에서 준비한 서랍별 내용물(딕셔너리)을 가지고, 이제 실제 **테이블**을 만드는 과정입니다. `pd.DataFrame(data)`는 마치 엑셀을 열고, "State", "Sex" 등의 컬럼 헤더를 만든 다음, 그 아래에 해당하는 데이터들을 각 행에 맞춰 깔끔하게 입력하는 것과 같습니다. 이 과정을 통해 `babynames`라는 이름의 정돈된 데이터 테이블이 생성됩니다.

### 4. DataFrame의 형태(Shape) 확인

```python
print(babynames.shape)
```

*   **핵심 개념:** `.shape` 속성은 DataFrame의 **차원**을 나타내는 튜플(tuple)을 반환합니다. `(행의 개수, 열의 개수)` 형식으로 구성됩니다.
*   **구체적인 예시:** 방금 만든 `babynames` 테이블의 크기를 확인하는 것입니다. 만약 `(4, 5)`가 출력된다면, 이는 테이블에 **4개의 행(row)**과 **5개의 열(column)**이 있다는 의미입니다. 실제 데이터의 '덩치'가 어느 정도인지 파악하는 데 유용합니다. 마치 책의 페이지 수와 장의 수를 세어보는 것과 같다고 볼 수 있습니다.

---

**결론적으로, 이 슬라이드는 파이썬 딕셔너리를 활용하여 Pandas DataFrame을 만들고, 그 기본적인 크기를 확인하는 과정을 보여주는 '아주 작은 데이터셋' 예시입니다.**

---

## Slide 4

*오류 발생으로 해설을 생성하지 못했습니다.*

---

## Slide 5

## Pandas 쿼리 API 핵심 개념 및 실생활 예시

다음은 판다스(pandas)에서 데이터프레임(DataFrame)을 쿼리하고 조작하는 주요 API와 각각의 기능, 그리고 학생들이 완벽하게 이해할 수 있도록 구체적인 실생활 예시입니다.

---

### 1. `df.loc[mask]`
*   **개념**: 불리언(Boolean) 마스크를 사용하여 조건에 맞는 행을 선택하거나, 특정 열만 선택하여 데이터를 필터링합니다. (관계형 대수: selection $\sigma$)
*   **실생활 예시**:
    *   **상황**: 한 온라인 쇼핑몰의 고객 주문 데이터(`orders_df`)가 있습니다. 이 데이터에는 '상품명', '가격', '수량', '구매자_지역' 등의 정보가 포함되어 있습니다.
    *   **적용**: '서울' 지역 고객이 주문한 상품 중 '가격'이 50,000원 이상인 모든 주문을 확인하고 싶을 때.
    ```python
    import pandas as pd
    data = {
        '상품명': ['노트북', '마우스', '키보드', '모니터', '웹캠', '노트북'],
        '가격': [1200000, 25000, 70000, 300000, 40000, 1500000],
        '수량': [1, 2, 1, 1, 3, 1],
        '구매자_지역': ['서울', '부산', '서울', '인천', '경기', '서울']
    }
    orders_df = pd.DataFrame(data)

    # 서울 지역에서 50,000원 이상인 주문 필터링
    expensive_orders_in_seoul = orders_df.loc[
        (orders_df['구매자_지역'] == '서울') & (orders_df['가격'] >= 50000)
    ]
    print(expensive_orders_in_seoul)
    ```

### 2. `df.query("expr")`
*   **개념**: SQL과 유사한 문자열 표현식을 사용하여 데이터프레임의 행을 필터링합니다. `df.loc`과 유사하지만, 문자열 쿼리 방식을 제공하여 가독성이 높을 수 있습니다. (관계형 대수: selection $\sigma$)
*   **실생활 예시**:
    *   **상황**: 위와 동일한 온라인 쇼핑몰 주문 데이터(`orders_df`)를 사용합니다.
    *   **적용**: '서울' 또는 '인천' 지역의 고객 중 '가격'이 100,000원 미만이면서 '수량'이 1개 초과인 주문을 찾고 싶을 때.
    ```python
    # query() 메서드를 사용하여 필터링
    specific_low_price_orders = orders_df.query(
        "(구매자_지역 == '서울' or 구매자_지역 == '인천') and 가격 < 100000 and 수량 > 1"
    )
    print(specific_low_price_orders)
    ```

### 3. `pd.merge(L, R, on=..., how=...)`
*   **개념**: 두 개의 데이터프레임을 특정 키(key)를 기준으로 결합합니다. 내부 조인(inner), 왼쪽 조인(left), 오른쪽 조인(right), 외부 조인(outer) 등 다양한 조인 방식을 지원합니다. (관계형 대수: equi-join $\bowtie_{\theta}$, cross join $\times$)
*   **실생활 예시**:
    *   **상황**: 고객 정보가 담긴 데이터프레임(`customers_df`)과 고객별 주문 내역이 담긴 데이터프레임(`orders_df`)이 따로 있습니다. 두 데이터에 공통으로 '고객ID'가 있습니다.
    *   **적용**: 각 주문에 해당 고객의 이름과 이메일 정보를 추가하여 통합된 주문 내역을 만들고 싶을 때.
    ```python
    customers_data = {
        '고객ID': ['C001', 'C002', 'C003', 'C004'],
        '이름': ['김철수', '박영희', '이민지', '최현우'],
        '이메일': ['kim@example.com', 'park@example.com', 'lee@example.com', 'choi@example.com']
    }
    customers_df = pd.DataFrame(customers_data)

    orders_data = {
        '주문ID': ['ORD001', 'ORD002', 'ORD003', 'ORD004', 'ORD005'],
        '고객ID': ['C001', 'C002', 'C001', 'C005', 'C003'], # C005는 고객 정보에 없음
        '상품': ['티셔츠', '바지', '신발', '모자', '가방']
    }
    orders_df = pd.DataFrame(orders_data)

    # 고객ID를 기준으로 orders_df에 customers_df를 병합 (left join)
    # 모든 주문을 유지하고, 고객 정보가 있는 경우에만 추가
    merged_orders = pd.merge(orders_df, customers_df, on='고객ID', how='left')
    print(merged_orders)
    ```

### 4. `df.groupby(keys).agg(...)`
*   **개념**: 하나 이상의 열을 기준으로 데이터를 그룹화한 후, 각 그룹에 대해 합계, 평균, 개수 등 다양한 집계 함수를 적용합니다. (관계형 대수: γ$_{G;f(\cdot)}$)
*   **실생활 예시**:
    *   **상황**: 한 회사의 판매 실적 데이터(`sales_df`)가 있습니다. '지점', '상품_카테고리', '판매액' 등의 정보가 있습니다.
    *   **적용**: 각 '지점'별 총 판매액과 평균 판매액을 계산하고 싶을 때. 또는 각 '지점'과 '상품_카테고리'별로 가장 많이 팔린 상품의 판매액을 알고 싶을 때.
    ```python
    sales_data = {
        '지점': ['강남', '강남', '종로', '종로', '강남', '종로'],
        '상품_카테고리': ['전자제품', '의류', '전자제품', '식품', '식품', '의류'],
        '판매액': [150000, 50000, 200000, 30000, 20000, 80000]
    }
    sales_df = pd.DataFrame(sales_data)

    # 지점별 총 판매액 및 평균 판매액
    branch_sales_summary = sales_df.groupby('지점')['판매액'].agg(['sum', 'mean'])
    print("지점별 판매 요약:\n", branch_sales_summary)

    # 지점과 상품_카테고리별 최대 판매액
    category_sales_summary = sales_df.groupby(['지점', '상품_카테고리'])['판매액'].max()
    print("\n지점 및 카테고리별 최대 판매액:\n", category_sales_summary)
    ```

### 5. `df.drop_duplicates(subset)`
*   **개념**: 데이터프레임에서 중복된 행을 제거합니다. 특정 열(subset)을 기준으로 중복을 판단할 수 있으며, 첫 번째 또는 마지막으로 나타나는 중복 값을 유지할 수 있습니다. (관계형 대수: duplicate elimination $\delta$)
*   **실생활 예시**:
    *   **상황**: 고객 가입 이벤트에 참여한 명단(`event_participants_df`)이 있습니다. 실수로 같은 사람이 여러 번 참여했을 수 있습니다.
    *   **적용**: '이메일'을 기준으로 중복되는 참가자를 제거하여 유일한 참가자 명단을 만들고 싶을 때.
    ```python
    participants_data = {
        '이름': ['김하나', '이두나', '김하나', '박세진', '이두나'],
        '이메일': ['hana@example.com', 'duna@example.com', 'hana@example.com', 'sejin@example.com', 'duna@example.com'],
        '참여일': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']
    }
    event_participants_df = pd.DataFrame(participants_data)

    # '이메일'을 기준으로 중복 제거 (첫 번째 값 유지)
    unique_participants = event_participants_df.drop_duplicates(subset=['이메일'])
    print(unique_participants)
    ```

### 6. `df.sort_values(by)`
*   **개념**: 하나 이상의 열(by)을 기준으로 데이터프레임의 행을 오름차순 또는 내림차순으로 정렬합니다. (관계형 대수 확장: sorting $\tau$)
*   **실생활 예시**:
    *   **상황**: 학생들의 시험 점수 데이터(`scores_df`)가 있습니다.
    *   **적용**: '총점'이 높은 순서대로 학생들을 정렬하여 성적 우수자를 확인하고 싶을 때. 만약 총점이 같다면 '이름' 순서로 정렬하고 싶을 때.
    ```python
    student_scores_data = {
        '이름': ['철수', '영희', '민수', '수지', '지혜'],
        '수학': [85, 92, 78, 92, 88],
        '영어': [90, 88, 85, 90, 75],
        '총점': [175, 180, 163, 182, 163]
    }
    scores_df = pd.DataFrame(student_scores_data)

    # '총점'을 내림차순으로, '총점'이 같으면 '이름'을 오름차순으로 정렬
    sorted_students = scores_df.sort_values(by=['총점', '이름'], ascending=[False, True])
    print(sorted_students)
    ```

### 7. `pd.concat([...], axis=0)`
*   **개념**: 여러 데이터프레임이나 시리즈를 특정 축(axis)을 따라 이어 붙입니다. `axis=0`은 행을 따라, `axis=1`은 열을 따라 이어 붙입니다. (관계형 대수: union $\cup$)
*   **실생활 예시**:
    *   **상황**: 각 분기별 판매 보고서가 별도의 데이터프레임(`q1_sales_df`, `q2_sales_df`)으로 저장되어 있습니다.
    *   **적용**: 상반기 전체 판매 실적을 분석하기 위해 두 분기의 데이터를 하나의 데이터프레임으로 합치고 싶을 때.
    ```python
    q1_sales_data = {'상품': ['A', 'B'], '판매량': [100, 150]}
    q1_sales_df = pd.DataFrame(q1_sales_data)

    q2_sales_data = {'상품': ['C', 'A'], '판매량': [80, 120]}
    q2_sales_df = pd.DataFrame(q2_sales_data)

    # 두 데이터프레임을 행(axis=0)을 따라 이어 붙이기
    half_year_sales = pd.concat([q1_sales_df, q2_sales_df], axis=0)
    print(half_year_sales)
    ```

### 8. `pd.crosstab(idx, cols)`
*   **개념**: 두 개 이상의 인자(factor)에 대한 교차 빈도표(contingency table)를 계산합니다. 이는 두 변수 간의 관계를 요약하여 보여줍니다. 기본적으로 개수(count)를 집계합니다. (관계형 대수: PIVOT with count(*))
*   **실생활 예시**:
    *   **상황**: 영화 관람객 설문조사 데이터(`survey_df`)가 있습니다. 이 데이터에는 '성별', '선호_장르' 등의 정보가 포함되어 있습니다.
    *   **적용**: 성별에 따른 선호하는 영화 장르의 분포를 파악하여, 어떤 성별이 어떤 장르를 더 선호하는지 알고 싶을 때.
    ```python
    survey_data = {
        '성별': ['남', '여', '남', '여', '남', '여', '남'],
        '선호_장르': ['액션', '로맨스', '액션', '스릴러', '코미디', '로맨스', '액션']
    }
    survey_df = pd.DataFrame(survey_data)

    # 성별과 선호_장르 간의 교차 빈도표 생성
    genre_by_gender = pd.crosstab(survey_df['성별'], survey_df['선호_장르'])
    print(genre_by_gender)
    ```

### 9. `df.pivot_table(index, columns, values, aggfunc)`
*   **개념**: 스프레드시트의 피벗 테이블처럼 데이터를 재구성하고 집계합니다. `index`와 `columns`를 기준으로 `values`를 `aggfunc`으로 집계하여 새로운 테이블을 만듭니다. (관계형 대수: PIVOT with aggregation $f$)
*   **실생활 예시**:
    *   **상황**: 여러 지역에서 여러 상품을 판매한 내역 데이터(`detailed_sales_df`)가 있습니다. '지역', '상품_종류', '판매일', '판매량' 등의 정보가 있습니다.
    *   **적용**: 각 '지역'별로 '상품_종류'마다 총 '판매량'이 어떻게 되는지 한눈에 비교하고 싶을 때.
    ```python
    detailed_sales_data = {
        '지역': ['서울', '부산', '서울', '부산', '인천', '서울', '인천'],
        '상품_종류': ['전자제품', '의류', '전자제품', '식품', '전자제품', '의류', '식품'],
        '판매일': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-07'],
        '판매량': [10, 5, 12, 8, 7, 3, 6]
    }
    detailed_sales_df = pd.DataFrame(detailed_sales_data)

    # 지역별 상품 종류별 총 판매량을 보여주는 피벗 테이블 생성
    sales_pivot = detailed_sales_df.pivot_table(
        index='지역',        # 행 인덱스
        columns='상품_종류',   # 열 인덱스
        values='판매량',      # 집계할 값
        aggfunc='sum'        # 집계 함수 (합계)
    )
    print(sales_pivot)
    ```

---

## Slide 6

핵심 개념: DataFrame 데이터 생성 및 변경 (Create)

이 슬라이드는 Pandas DataFrame에 새로운 행(row)과 열(column)을 추가하는 다양한 방법을 보여줍니다. 여기서 "Create mutates the relation instance"라는 Note는 이러한 작업들이 대부분 원본 DataFrame 객체 자체를 변경(수정)한다는 의미입니다. 관계형 데이터베이스의 "관계 인스턴스"는 Pandas DataFrame과 유사하게 데이터의 테이블을 의미합니다.

---

### 1. 단일 행 추가 (Appending a Single Row)

**개념:**
DataFrame의 `.loc` 인덱서를 사용하여 다음 사용 가능한 인덱스 위치에 새로운 행 데이터를 직접 할당하는 방식입니다. `len(babynames)`는 현재 DataFrame의 마지막 인덱스 바로 다음 위치를 가리키므로, 새로운 행을 추가하는 데 사용됩니다.

**코드:**
```python
# babynames라는 DataFrame에 하나의 행을 추가
babynames.loc[len(babynames)] = ["CA", "F", 2023, "Nova", 12]
```

**구체적인 실생활 예시:**
당신이 학생들의 성적을 관리하는 `grade_book` DataFrame을 가지고 있다고 가정해 봅시다.
| 이름 | 과목 | 점수 |
|---|---|---|
| 김철수 | 수학 | 90 |
| 이영희 | 영어 | 85 |

여기에 새로운 학생 '박민수'의 성적을 추가하려면 다음과 같이 할 수 있습니다:
```python
import pandas as pd
grade_book = pd.DataFrame([
    ['김철수', '수학', 90],
    ['이영희', '영어', 85]
], columns=['이름', '과목', '점수'])

# 새로운 학생 '박민수'의 성적 추가
grade_book.loc[len(grade_book)] = ['박민수', '과학', 92]
print(grade_book)
```
**결과:**
| 이름 | 과목 | 점수 |
|---|---|---|
| 김철수 | 수학 | 90 |
| 이영희 | 영어 | 85 |
| 박민수 | 과학 | 92 |

---

### 2. 여러 행 일괄 추가 (Batch Appending Multiple Rows - 권장 방식)

**개념:**
하나의 행을 추가하는 것보다 여러 행을 동시에 추가할 때 더 효율적인 방법입니다. 추가할 데이터를 리스트 형태로 준비한 다음, 이를 바탕으로 새로운 임시 DataFrame을 만들고, 기존 DataFrame과 `pd.concat()` 함수를 사용하여 결합합니다. `ignore_index=True` 옵션은 병합 후 인덱스가 재설정되도록 하여 중복을 방지합니다.

**코드:**
```python
# 여러 개의 행 데이터를 리스트에 담기
rows = [["CA", "M", 2023, "Atlas", 9], ("CA", "F", 2024, "Mira", 7)]
# 기존 DataFrame과 새로 만든 DataFrame을 연결
babynames = pd.concat(
    [babynames, pd.DataFrame(rows, columns=babynames.columns)],
    ignore_index=True
)
```

**구체적인 실생활 예시:**
당신이 특정 달의 웹사이트 방문자 데이터를 `website_visitors` DataFrame으로 가지고 있습니다.
| 날짜 | 방문자수 | 페이지뷰 |
|---|---|---|
| 2023-01-01 | 1500 | 5000 |
| 2023-01-02 | 1600 | 5200 |

다음 달(2월)의 첫 며칠치 방문자 데이터가 여러 건 한꺼번에 도착했다고 해봅시다.
```python
# 기존 DataFrame (예시를 위해 초기화)
website_visitors = pd.DataFrame([
    ['2023-01-01', 1500, 5000],
    ['2023-01-02', 1600, 5200]
], columns=['날짜', '방문자수', '페이지뷰'])

# 2월 첫 며칠치 데이터 (여러 행)
new_month_data = [
    ['2023-02-01', 1700, 5500],
    ['2023-02-02', 1800, 5800],
    ['2023-02-03', 1750, 5600]
]

# 새로운 데이터를 DataFrame으로 만들고 기존 DataFrame에 추가
website_visitors = pd.concat(
    [website_visitors, pd.DataFrame(new_month_data, columns=website_visitors.columns)],
    ignore_index=True
)
print(website_visitors)
```
**결과:**
| 날짜 | 방문자수 | 페이지뷰 |
|---|---|---|
| 2023-01-01 | 1500 | 5000 |
| 2023-01-02 | 1600 | 5200 |
| 2023-02-01 | 1700 | 5500 |
| 2023-02-02 | 1800 | 5800 |
| 2023-02-03 | 1750 | 5600 |

---

### 3. 새로운 열 파생 및 추가 (Derive and Insert Columns)

**개념:**
기존 열의 데이터를 기반으로 새로운 계산된 열을 만들거나, 두 개 이상의 기존 열을 결합하여 새로운 열을 추가하는 방법입니다.

#### 3.1. 기존 열로부터 새로운 열 파생 (Adding a new column by derivation)

**개념:**
하나 이상의 기존 열에 연산을 적용하여 새로운 열의 값을 생성합니다. 단순히 새 열 이름을 할당하고 `=` 연산자를 사용하여 값을 지정하면 DataFrame의 가장 오른쪽에 새 열이 추가됩니다.

**코드:**
```python
# 'Year' 열을 이용하여 'decade' 열을 파생
babynames["decade"] = (babynames["Year"] // 10) * 10
```

**구체적인 실생활 예시:**
쇼핑몰의 `sales_data` DataFrame에 '가격'과 '수량' 열이 있습니다. '총 판매액' 열을 새로 만들고 싶다면:
| 상품명 | 가격 | 수량 |
|---|---|---|
| 셔츠 | 25000 | 2 |
| 바지 | 40000 | 1 |

```python
sales_data = pd.DataFrame([
    ['셔츠', 25000, 2],
    ['바지', 40000, 1]
], columns=['상품명', '가격', '수량'])

# '총 판매액' 열 파생
sales_data['총 판매액'] = sales_data['가격'] * sales_data['수량']
print(sales_data)
```
**결과:**
| 상품명 | 가격 | 수량 | 총 판매액 |
|---|---|---|---|
| 셔츠 | 25000 | 2 | 50000 |
| 바지 | 40000 | 1 | 40000 |

#### 3.2. 특정 위치에 새로운 열 삽입 (Inserting a new column at a specific position)

**개념:**
`.insert()` 메서드를 사용하여 새 열을 원하는 위치(인덱스)에 삽입할 수 있습니다. `DataFrame.insert(loc, column, value)` 형태로 사용하며, `loc`는 삽입할 위치의 정수 인덱스, `column`은 새 열의 이름, `value`는 새 열의 데이터를 지정합니다.

**코드:**
```python
# 'State'와 'Sex' 열을 결합하여 'state_sex' 열을 만들고 가장 왼쪽에 삽입 (인덱스 0)
babynames.insert(0, "state_sex", babynames["State"].str.cat(babynames["Sex"], sep="-"))
```
이 코드에서는 `.str.cat()`을 사용하여 두 문자열 Series를 하이픈으로 연결합니다.

**구체적인 실생활 예시:**
고객 정보 `customer_data` DataFrame이 있다고 합시다.
| 이름 | 도시 | 주소 |
|---|---|---|
| 홍길동 | 서울 | 강남구 |
| 김영희 | 부산 | 해운대구 |

여기에 '전화번호' 열을 추가했는데, '이름' 바로 뒤에 보이게 하고 싶다면:
```python
customer_data = pd.DataFrame([
    ['홍길동', '서울', '강남구'],
    ['김영희', '부산', '해운대구']
], columns=['이름', '도시', '주소'])

# '전화번호' 데이터 (Series)
phone_numbers = pd.Series(['010-1111-2222', '010-3333-4444'])

# '이름' (인덱스 0) 바로 뒤인 인덱스 1에 '전화번호' 열 삽입
customer_data.insert(1, '전화번호', phone_numbers)
print(customer_data)
```
**결과:**
| 이름 | 전화번호 | 도시 | 주소 |
|---|---|---|---|
| 홍길동 | 010-1111-2222 | 서울 | 강남구 |
| 김영희 | 010-3333-4444 | 부산 | 해운대구 |

---

## Slide 7

핵심 개념: 데이터 업데이트 (Data Update)

'업데이트'는 데이터베이스나 데이터프레임 내의 기존 데이터를 수정하는 작업을 의미합니다. 슬라이드에서 언급된 'ERA 쿼리'가 아니라는 점은, 업데이트가 단순히 정보를 조회하는(쿼리하는) 것을 넘어 실제 '튜플/속성'(데이터 행/열)의 내용을 변경한다는 본질적인 차이를 강조합니다. 여기서는 데이터프레임에서 데이터를 업데이트하는 네 가지 주요 방법에 대해 알아봅니다.

---

### 1. Point Update (지점 업데이트)

**설명:** 특정 조건을 정확히 만족하는 *단일* 또는 *소수의* 데이터 지점(셀)의 값을 수정하는 방법입니다. 데이터프레임 내에서 매우 구체적인 위치를 지정하여 데이터를 변경할 때 사용됩니다.

**구체적이고 실생활에 가까운 예시:**

> 당신이 한 대학교의 학사관리팀 직원이라고 상상해 보세요. "2023년 가을학기"에 "김민준" 학생이 "데이터베이스 시스템" 과목에서 "A+" 학점을 받았습니다. 그런데 교수님의 재평가 결과, 이 학생의 최종 학점이 "A0"로 정정되어야 합니다.
>
> 이 경우, 학사관리 데이터프레임(`student_grades_df`)에서 `Name`이 '김민준'이고 `Course`가 '데이터베이스 시스템'이며 `Semester`가 '2023 Fall'인 *특정 행*을 찾아, 해당 행의 `Grade` 열 값만을 "A0"로 정확히 업데이트하는 것이 바로 'Point Update'입니다. 다른 학생의 성적이나 다른 과목의 성적에는 전혀 영향을 주지 않습니다.

---

### 2. Conditional Update (조건부 업데이트)

**설명:** 특정 조건을 만족하는 *모든* 데이터 지점(여러 셀 또는 행)의 값을 한 번에 수정하는 방법입니다. 어떤 기준에 따라 여러 데이터에 동일한 변경을 적용해야 할 때 유용합니다.

**구체적이고 실생활에 가까운 예시:**

> 당신은 온라인 쇼핑몰의 재고 관리 담당자입니다. `product_inventory_df`라는 데이터프레임에 모든 상품의 `재고수량` 정보가 있습니다. 이번 달 판매량이 저조하여, `재고수량`이 5개 미만인 모든 상품에 대해 `주문상태`를 "긴급 재주문 필요"로 일괄 변경해야 합니다.
>
> 이 경우, `재고수량 < 5`라는 *조건*을 만족하는 *모든 상품*의 `주문상태` 열 값을 "긴급 재주문 필요"로 업데이트하는 것이 'Conditional Update'입니다. 수백, 수천 개의 상품 중 해당 조건에 맞는 모든 상품의 상태가 한 번에 변경됩니다.

---

### 3. Map / Replace (매핑/치환)

**설명:** 한 열에 있는 특정 값들을 미리 정의된 규칙(매핑)에 따라 다른 값으로 일괄적으로 변환하는 방법입니다. 데이터의 형식이나 가독성을 개선하거나 표준화할 때 주로 사용됩니다.

**구체적이고 실생활에 가까운 예시:**

> 당신은 고객 만족도 설문조사 데이터를 분석하고 있습니다. 설문조사 시 응답자들이 만족도를 'VS' (매우 만족), 'S' (만족), 'N' (보통), 'D' (불만족), 'VD' (매우 불만족)와 같이 약어로 입력했습니다. 보고서 작성을 위해 이 약어들을 "매우 만족", "만족", "보통", "불만족", "매우 불만족"과 같은 전체 한글 표현으로 바꾸고 싶습니다.
>
> 이 경우, `satisfaction_survey_df`의 `Satisfaction_Level` 열에서 'VS'는 "매우 만족"으로, 'S'는 "만족"으로... 이런 식으로 *미리 정해진 매핑 규칙*에 따라 모든 약어를 전체 문구로 *치환*하는 것이 'Map / Replace'입니다.

---

### 4. Where/Mask Idiom (조건 마스크 활용 - `np.where` 등)

**설명:** 특정 조건을 기반으로 새로운 열을 생성하거나 기존 열의 값을 업데이트할 때 사용되는 강력한 방법입니다. 조건에 따라 두 가지 이상의 다른 값을 할당할 수 있게 해주는 'if-else' 로직과 유사하게 작동합니다.

**구체적이고 실생활에 가까운 예시:**

> 당신은 신용카드 회사에서 고객 등급을 분류하는 업무를 맡고 있습니다. `customer_data_df`라는 데이터프레임에 고객들의 `월평균_사용금액` 정보가 있습니다. 회사의 정책상, `월평균_사용금액`이 100만원 이상인 고객은 "VIP"로, 그렇지 않은 고객은 "일반"으로 `고객등급` 열을 새로 만들어 분류하고 싶습니다.
>
> 이 경우, `월평균_사용금액 >= 1,000,000`이라는 *조건*을 기준으로, 조건이 참(True)일 때는 "VIP"를, 거짓(False)일 때는 "일반"을 새로운 `고객등급` 열에 할당하여 생성하거나 기존 열을 업데이트하는 것이 'Where/Mask Idiom'입니다. 이는 `np.where(조건, 참일 때 값, 거짓일 때 값)`과 같은 형태로 구현됩니다.

---

## Slide 8

# 핵심 개념: Pandas DataFrame에서 데이터 삭제

이 슬라이드는 Pandas DataFrame에서 열(Column)과 행(Row)을 삭제하는 다양한 방법을 보여줍니다. 여기서 중요한 점은 `Delete` 작업은 데이터프레임 자체의 `튜플(행)`이나 `속성(열)`을 직접 제거하는 것으로, 단순히 특정 조건을 조회하는(ERA query) 것이 아니라 데이터 구조를 영구적으로 변경한다는 것입니다.

---

## 1. 열(Column) 제거 (값을 반환하며)

*   **개념**: `DataFrame.pop('컬럼_이름')` 메서드는 지정된 열을 데이터프레임에서 제거하고, 제거된 열의 데이터를 Pandas Series 형태로 반환합니다. 이는 특정 열을 잠시 분리하여 다른 작업에 사용하거나, 분석에서 제외했다가 필요할 때 다시 추가하고 싶을 때 유용합니다.

*   **예시 코드**:
    ```python
    cnt = babynames.pop("Count") # "Count" 열을 babynames에서 제거하고 그 내용을 cnt에 저장
    # babynames DataFrame에는 더 이상 "Count" 열이 없습니다.
    # babynames["Count"] = cnt   # 필요하다면 나중에 다시 "Count" 열을 추가할 수 있습니다.
    ```

*   **구체적이고 실생활에 가까운 예시**:
    당신이 한 카페의 `주문 내역(orders)` DataFrame을 관리하고 있다고 가정해 봅시다. 이 데이터프레임에는 `['주문ID', '메뉴', '가격', '수량', '고객ID']`와 같은 열이 있습니다.
    어느 날, 고객ID 정보를 다른 팀에 보안상의 이유로 잠시 분리하여 전달해야 할 필요가 생겼습니다. 이때 `pop()`을 사용할 수 있습니다.
    ```python
    # orders = pd.DataFrame({'주문ID': [1,2,3], '메뉴': ['아메리카노', '라떼', '샌드위치'], '가격': [4000, 4500, 6000], '수량': [1,1,2], '고객ID': ['A1', 'B2', 'A1']})

    고객ID_데이터 = orders.pop('고객ID')
    # 이제 'orders' DataFrame에는 '고객ID' 열이 없습니다.
    # '고객ID_데이터'는 ['A1', 'B2', 'A1']와 같은 Series 형태의 고객ID 정보만 담고 있습니다.
    ```
    이렇게 하면 원본 `orders` DataFrame에서 `고객ID` 열이 제거되어 다른 작업에 활용할 수 있고, `고객ID_데이터`는 필요한 팀에 별도로 전달하여 개인 정보 보호를 강화하거나 특정 분석에만 활용할 수 있습니다.

---

## 2. 행(Row) 제거 (레이블/인덱스 기반)

*   **개념**: `DataFrame.drop(index=삭제할_인덱스_리스트)` 메서드는 지정된 인덱스(레이블)에 해당하는 행들을 데이터프레임에서 제거합니다. 특정 위치의 행이나, 이미 알고 있는 인덱스 레이블을 가진 행들을 삭제할 때 사용됩니다.

*   **예시 코드**:
    ```python
    to_remove = babynames.index[:2] # 첫 두 행의 인덱스를 추출
    babynames = babynames.drop(index=to_remove) # 해당 인덱스에 해당하는 행들을 제거
    ```

*   **구체적이고 실생활에 가까운 예시**:
    당신이 `온라인 쇼핑몰 상품 목록(products)` DataFrame을 가지고 있으며, 인덱스는 상품의 고유한 `SKU (재고 관리 코드)`라고 가정해 봅시다. `products` DataFrame에는 `['상품명', '가격', '재고수량']`과 같은 열이 있습니다.
    만약 특정 SKU를 가진 상품 두 개(예: 'SKU001', 'SKU002')가 단종되어 목록에서 완전히 삭제해야 한다면:
    ```python
    # products = pd.DataFrame({'상품명': ['티셔츠', '바지', '모자'], '가격': [20000, 35000, 15000], '재고수량': [100, 50, 20]}, index=['SKU001', 'SKU002', 'SKU003'])

    단종될_상품_SKU = ['SKU001', 'SKU002']
    products = products.drop(index=단종될_상품_SKU)
    # 이제 'products' DataFrame에는 'SKU001'과 'SKU002' 상품이 제거되었습니다.
    # 'SKU003' 상품만 남아있습니다.
    ```
    이렇게 하면 특정 인덱스(SKU)를 가진 상품 정보를 정확하게 제거하여 재고 목록을 최신 상태로 유지할 수 있습니다.

---

## 3. 행(Row) 제거 (조건 기반)

*   **개념**: 이 방법은 먼저 특정 조건을 만족하는 행들을 식별하고, 해당 행들의 인덱스를 추출한 다음, 그 인덱스를 `drop()` 메서드에 전달하여 제거합니다. 이는 복잡한 비즈니스 로직이나 데이터 정제 규칙에 따라 데이터를 삭제할 때 매우 유용합니다.

*   **예시 코드**:
    ```python
    old_rare = (babynames["Year"] < 1920) & (babynames["Count"] < 5) # 1920년 이전이면서 이름 사용 횟수가 5회 미만인 조건을 만족하는 행들을 True로 표시하는 Series 생성
    babynames = babynames.drop(index=babynames[old_rare].index) # 해당 조건을 만족하는 행들의 인덱스를 추출하여 제거
    ```

*   **구체적이고 실생활에 가까운 예시**:
    당신이 한 앱의 `사용자 피드백(feedback)` DataFrame을 분석하고 있다고 가정해 봅시다. 이 데이터프레임에는 `['사용자ID', '제출일', '평점', '댓글']`과 같은 열이 있습니다.
    오래되고 낮은 평점의 피드백은 현재 서비스 개선에 큰 도움이 되지 않는다고 판단하여, 2020년 이전에 제출되었으며 평점이 2점 이하인 피드백을 모두 삭제하고 싶을 때:
    ```python
    # feedback = pd.DataFrame({
    #     '사용자ID': ['U1', 'U2', 'U3', 'U4', 'U5'],
    #     '제출일': pd.to_datetime(['2019-01-15', '2021-03-20', '2018-07-01', '2022-05-10', '2019-11-20']),
    #     '평점': [1, 4, 2, 5, 1],
    #     '댓글': ['불편해요', '좋아요', '개선필요', '최고', '별로예요']
    # })

    오래된_낮은_평점_조건 = (feedback['제출일'].dt.year < 2020) & (feedback['평점'] <= 2)
    # 이 조건은 '제출일'이 2020년 이전이고 '평점'이 2점 이하인 행들에 대해 True를 반환하는 불리언 Series를 생성합니다.
    # 예시에서는 'U1'과 'U3', 'U5'가 이 조건에 해당됩니다.

    feedback = feedback.drop(index=feedback[오래된_낮은_평점_조건].index)
    # 이제 'feedback' DataFrame에서 'U1', 'U3', 'U5' 사용자의 피드백이 제거되었습니다.
    # 최신이거나 평점이 높은 피드백만 남게 됩니다.
    ```
    이 방법을 통해 특정 기준을 만족하지 않거나 더 이상 필요 없는 데이터를 대량으로 정리하여 분석의 효율성과 정확도를 높일 수 있습니다.

---

## Slide 9

*오류 발생으로 해설을 생성하지 못했습니다.*

---

## Slide 10

## 핵심 개념: 일반화된 프로젝션 (Generalized Projection)

일반화된 프로젝션은 데이터베이스나 데이터프레임에서 특정 속성(컬럼)을 선택하는 것을 넘어, **기존 속성들을 사용하여 새로운 속성(컬럼)을 생성하고, 이를 결과에 포함**시키는 강력한 데이터 조작 기법입니다.

*   **정의:** 슬라이드의 `π_e1→B1,...,ek→Bk (R)` 형식처럼, 관계 `R`의 기존 속성들에 `e_i`와 같은 표현식(함수, 연산 등)을 적용하여 `B_i`라는 이름의 새로운 속성을 계산하고, 이들을 포함한 결과를 반환합니다.
*   **"일반화된"의 의미:** 일반적인 프로젝션은 단순히 기존 컬럼들을 선택하는 것입니다. 하지만 '일반화된' 프로젝션은 여기에 **'파생된(derived)' 컬럼을 생성하는 기능**이 추가됩니다. 즉, 원본 데이터에는 없던 새로운 정보를 기존 데이터를 기반으로 만들어냅니다.
*   **활용 목적:** 데이터를 분석하거나 보고서를 작성할 때 필요한 형태로 데이터를 가공하거나, 기존 정보에서 새로운 유의미한 특징(feature)을 추출할 때 주로 사용됩니다.

## 슬라이드 예시 상세 설명

슬라이드에서는 `babynames` 데이터셋을 예로 들어 일반화된 프로젝션을 설명합니다.

*   **ERA (Query) 표현:** `π_Year, Name, SUBSTR(Name,1,1) → first_letter, LEN(Name) → name_len (babynames)`
    *   이는 `babynames` 테이블에서 `Year`와 `Name` 컬럼을 그대로 가져오고, `Name` 컬럼의 첫 글자를 추출하여 `first_letter`라는 새 컬럼으로, `Name` 컬럼의 길이를 계산하여 `name_len`이라는 새 컬럼으로 추가하라는 의미입니다.
*   **Pandas 구현:** `babynames.assign(...) [...]`
    *   `assign()` 메서드를 사용하여 새로운 컬럼을 생성합니다.
        *   `first_letter=lambda d: d["Name"].str[0]`: `Name` 컬럼의 각 값(문자열)에서 첫 번째 문자(`[0]`)를 추출하여 `first_letter` 컬럼을 만듭니다.
        *   `name_len=lambda d: d["Name"].str.len()`: `Name` 컬럼의 각 값(문자열)의 길이(`len()`)를 계산하여 `name_len` 컬럼을 만듭니다.
    *   마지막 `[["Year", "Name", "first_letter", "name_len"]]` 부분은 `assign`으로 생성된 새 데이터프레임에서 최종적으로 포함시킬 컬럼들을 지정하는 것입니다. 이렇게 하면 `Year`와 `Name` 외에 새로 생성된 `first_letter`와 `name_len` 컬럼이 함께 결과로 반환됩니다.

## 구체적인 실생활 예시: 온라인 쇼핑몰 주문 데이터 분석

**시나리오:** 여러분이 온라인 쇼핑몰의 데이터 분석가라고 가정해 봅시다. `orders`라는 데이터프레임이 있으며, 여기에는 고객의 주문 정보가 담겨 있습니다.

**원본 `orders` 데이터프레임 (가상):**

| OrderID | CustomerID | ItemName    | Price | Quantity | OrderDate  |
| :------ | :--------- | :---------- | :---- | :------- | :--------- |
| 1001    | C001       | Laptop      | 1200  | 1        | 2023-01-15 |
| 1002    | C002       | Mouse       | 25    | 2        | 2023-01-15 |
| 1003    | C001       | Keyboard    | 75    | 1        | 2023-02-20 |
| 1004    | C003       | Monitor     | 300   | 1        | 2023-02-28 |

**일반화된 프로젝션 목표:**

우리는 단순히 기존 컬럼을 보는 것을 넘어, 다음과 같은 새로운 정보를 추가하여 분석에 활용하고 싶습니다.

1.  **총 주문 금액 (`TotalPrice`)**: `Price`와 `Quantity`를 곱하여 각 주문 건의 총 금액을 계산합니다.
2.  **주문 요일 (`OrderDayOfWeek`)**: `OrderDate`를 바탕으로 주문이 들어온 요일을 파악합니다. (예: 월요일, 화요일 등)
3.  **상품 카테고리 약어 (`ItemCategoryAbbr`)**: `ItemName`의 첫 세 글자를 추출하여 간략한 카테고리 약어를 만듭니다. (예: 'Lap' for 'Laptop', 'Mou' for 'Mouse')

**적용 및 결과 (`pandas` 코드 가정):**

```python
import pandas as pd

# 가정의 orders 데이터프레임 생성
data = {
    'OrderID': [1001, 1002, 1003, 1004],
    'CustomerID': ['C001', 'C002', 'C001', 'C003'],
    'ItemName': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Price': [1200, 25, 75, 300],
    'Quantity': [1, 2, 1, 1],
    'OrderDate': ['2023-01-15', '2023-01-15', '2023-02-20', '2023-02-28']
}
orders = pd.DataFrame(data)
orders['OrderDate'] = pd.to_datetime(orders['OrderDate'])

# 일반화된 프로젝션 적용
# 기존 컬럼 유지: OrderID, CustomerID, ItemName
# 새 컬럼 생성: TotalPrice, OrderDayOfWeek, ItemCategoryAbbr
analyzed_orders = orders.assign(
    TotalPrice=lambda df: df['Price'] * df['Quantity'],
    OrderDayOfWeek=lambda df: df['OrderDate'].dt.day_name(),
    ItemCategoryAbbr=lambda df: df['ItemName'].str[:3]
)[['OrderID', 'CustomerID', 'ItemName', 'TotalPrice', 'OrderDayOfWeek', 'ItemCategoryAbbr']]

print(analyzed_orders)
```

**결과 `analyzed_orders` 데이터프레임:**

| OrderID | CustomerID | ItemName    | TotalPrice | OrderDayOfWeek | ItemCategoryAbbr |
| :------ | :--------- | :---------- | :--------- | :------------- | :--------------- |
| 1001    | C001       | Laptop      | 1200       | Sunday         | Lap              |
| 1002    | C002       | Mouse       | 50         | Sunday         | Mou              |
| 1003    | C001       | Keyboard    | 75         | Monday         | Key              |
| 1004    | C003       | Monitor     | 300        | Tuesday        | Mon              |

**이 예시가 일반화된 프로젝션인 이유:**

*   **기존 속성 선택:** `OrderID`, `CustomerID`, `ItemName`과 같은 원본 컬럼들을 그대로 유지했습니다.
*   **새로운 속성 파생:**
    *   `TotalPrice`는 `Price`와 `Quantity`라는 두 기존 컬럼을 곱하여 생성된 새로운 컬럼입니다.
    *   `OrderDayOfWeek`는 `OrderDate` 컬럼의 정보를 가공하여(날짜에서 요일 추출) 만들어진 새로운 컬럼입니다.
    *   `ItemCategoryAbbr`는 `ItemName` 컬럼의 문자열을 가공하여(첫 세 글자 추출) 만들어진 새로운 컬럼입니다.

이처럼 일반화된 프로젝션은 원본 데이터를 손상시키지 않고, 기존 데이터에 기반한 새로운 시각이나 정보를 추가하여 분석의 깊이를 더하고 유연성을 높이는 데 매우 유용합니다.

---

## Slide 11

## 핵심 개념: 속성(컬럼) 이름 변경 (Rename Operation)

슬라이드에서 다루는 핵심 개념은 **데이터셋의 특정 속성(Attribute) 또는 컬럼(Column)의 이름을 변경하는 작업**입니다. 이 작업은 데이터의 내용(값)을 변경하지 않고 오직 이름만을 바꾸는 것이 특징입니다. 데이터 분석 및 관리에서 컬럼 이름을 더 명확하게 하거나, 특정 시스템의 명명 규칙에 맞추기 위해 자주 사용됩니다.

### 1. 형식적 정의 (Formal Definition)

*   **정의**: 관계형 대수(Relational Algebra)에서 'Rename' 연산(`ρ`)은 릴레이션(Relation, 즉 테이블이나 데이터프레임)의 속성 이름을 변경하는 데 사용됩니다.
*   **특징**: 이 연산은 릴레이션에 저장된 실제 데이터 값에는 어떤 영향도 주지 않고, 오직 해당 속성의 메타데이터(이름)만을 수정합니다.

### 2. 관계형 대수 (ERA Query) 표기

*   **일반 형식**: `ρ_A→A'(R)`
    *   `R`: 원본 릴레이션(데이터셋)
    *   `A`: 변경하고자 하는 원본 속성 이름
    *   `A'`: 새롭게 부여할 속성 이름
*   **슬라이드 예시**: `ρ_Count→freq(babynames)`
    *   `babynames`라는 릴레이션에서
    *   `Count`라는 속성 이름을
    *   `freq`로 변경하겠다는 의미입니다.

### 3. Pandas에서의 구현 (Python)

데이터 분석 라이브러리인 Pandas에서는 `DataFrame.rename()` 메서드를 사용하여 컬럼 이름을 변경합니다.

*   **일반 형식**: `df.rename(columns={"OldName": "NewName"})`
    *   `df`: Pandas DataFrame 객체
    *   `columns`: 딕셔너리 형태로 `{"원본_컬럼_이름": "새로운_컬럼_이름"}`을 전달하여 여러 컬럼을 한 번에 변경할 수 있습니다.
*   **슬라이드 예시**: `ren = babynames.rename(columns={"Count": "freq"})`
    *   `babynames`라는 DataFrame에서
    *   `Count`라는 컬럼 이름을
    *   `freq`로 변경한 후, 그 결과를 `ren`이라는 새로운 DataFrame 변수에 할당합니다. (원본 DataFrame은 변경되지 않고 새로운 DataFrame이 반환됩니다. 만약 원본을 직접 변경하고 싶다면 `inplace=True` 옵션을 사용할 수 있습니다.)

---

### 구체적인 실생활 예시: 온라인 쇼핑몰 주문 데이터 관리

당신이 온라인 쇼핑몰의 데이터 분석가라고 가정해 봅시다. 매일 수많은 주문 데이터가 생성되며, 이 데이터를 분석하여 매출 트렌드나 고객 행동을 파악해야 합니다. 초기 시스템에서 내보낸 주문 데이터는 다음과 같은 컬럼을 가지고 있습니다.

**원본 `orders` DataFrame:**

| OrderID | CustID | ItemName   | Price | Qty | OrderDate  |
| :------ | :----- | :--------- | :---- | :-- | :--------- |
| 1001    | C001   | Laptop     | 1200  | 1   | 2023-10-26 |
| 1002    | C002   | Mouse      | 30    | 2   | 2023-10-26 |
| 1003    | C001   | Keyboard   | 80    | 1   | 2023-10-27 |

여기서 몇 가지 컬럼 이름이 모호하거나, 다른 부서의 표준 명명 규칙과 맞지 않아 변경이 필요하다고 느꼈습니다.

1.  `CustID`는 고객 ID를 의미하지만, 데이터베이스 팀에서는 `CustomerID`를 표준으로 사용합니다.
2.  `Qty`는 수량을 의미하지만, 마케팅 팀에서는 분석 보고서에 `QuantityPurchased`라고 표기하는 것을 선호합니다.

이 경우, `rename` 연산을 사용하여 컬럼 이름을 변경할 수 있습니다.

**Pandas 코드:**

```python
import pandas as pd

# 원본 DataFrame 생성 (가정)
data = {
    'OrderID': [1001, 1002, 1003],
    'CustID': ['C001', 'C002', 'C001'],
    'ItemName': ['Laptop', 'Mouse', 'Keyboard'],
    'Price': [1200, 30, 80],
    'Qty': [1, 2, 1],
    'OrderDate': ['2023-10-26', '2023-10-26', '2023-10-27']
}
orders = pd.DataFrame(data)

print("--- 원본 DataFrame ---")
print(orders.head())

# 컬럼 이름 변경
# CustID를 CustomerID로, Qty를 QuantityPurchased로 변경
renamed_orders = orders.rename(columns={
    "CustID": "CustomerID",
    "Qty": "QuantityPurchased"
})

print("\n--- 이름 변경 후 DataFrame ---")
print(renamed_orders.head())
```

**결과 `renamed_orders` DataFrame:**

| OrderID | CustomerID | ItemName   | Price | QuantityPurchased | OrderDate  |
| :------ | :--------- | :--------- | :---- | :---------------- | :--------- |
| 1001    | C001       | Laptop     | 1200  | 1                 | 2023-10-26 |
| 1002    | C002       | Mouse      | 30    | 2                 | 2023-10-26 |
| 1003    | C001       | Keyboard   | 80    | 1                 | 2023-10-27 |

이 예시에서 볼 수 있듯이, `OrderID`, `ItemName`, `Price`, `OrderDate` 컬럼의 이름과 모든 데이터 값은 그대로 유지되면서, `CustID`는 `CustomerID`로, `Qty`는 `QuantityPurchased`로 이름만 변경되었습니다. 이렇게 컬럼 이름을 명확하게 변경함으로써 다른 팀원들이 데이터를 쉽게 이해하고 활용할 수 있도록 돕거나, 향후 데이터 통합 시 발생할 수 있는 혼란을 방지할 수 있습니다.

---

## Slide 12

# 중복 제거 (Duplicate Elimination - δ(R))

## 핵심 개념

슬라이드는 데이터베이스에서 '중복 제거(Duplicate Elimination)'라는 핵심 연산을 다룹니다. 이는 특정 데이터를 집합(set)으로 취급하여, 완전히 동일한 행(tuple)이 여러 개 존재하는 경우 하나의 행만 남기고 나머지를 제거하는 작업입니다. 관계형 대수(Relational Algebra)에서는 그리스 문자 델타(δ)로 표현됩니다.

**주요 내용:**

1.  **목적:** 데이터 셋에서 중복된 행(tuples)을 제거하여 고유한(unique) 값들만 남깁니다. 데이터의 무결성을 유지하고, 통계 분석의 정확성을 높이며, 불필요한 데이터 저장을 막는 데 필수적입니다.
2.  **관계형 대수 표현:** `δ(R)` 형태로 사용되며, 특정 속성(컬럼)에 대한 중복 제거는 먼저 해당 속성들을 프로젝션(`π`)한 후에 δ 연산을 적용합니다.
    *   슬라이드 예시: `δ(π_Year,Name(babynames))`
        *   `π_Year,Name(babynames)`: `babynames` 테이블에서 'Year'와 'Name' 컬럼만을 선택(투영)합니다. 이 단계에서는 여전히 중복된 (Year, Name) 쌍이 존재할 수 있습니다.
        *   `δ(...)`: 투영된 결과에서 완전히 동일한 (Year, Name) 쌍을 가진 행들을 제거하고, 고유한 (Year, Name) 쌍만 남깁니다.
    *   **의미:** `babynames` 데이터에서 발견되는 모든 고유한 '연도(Year)'와 '이름(Name)' 조합을 나열합니다.
3.  **Pandas 구현:** Python의 데이터 분석 라이브러리인 Pandas에서는 `DataFrame.drop_duplicates()` 메서드를 사용하여 중복을 제거합니다.
    *   슬라이드 예시: `unique_year_name = babynames[["Year", "Name"]].drop_duplicates()`
        *   `babynames[["Year", "Name"]]`: `babynames` DataFrame에서 'Year'와 'Name' 컬럼만을 선택합니다.
        *   `.drop_duplicates()`: 선택된 'Year'와 'Name' 컬럼을 기준으로, 완전히 동일한 조합을 가진 행들을 제거하고 고유한 행들만 `unique_year_name` 변수에 저장합니다.

## 구체적이고 실생활에 가까운 예시

### 예시 1: 이메일 구독자 목록 관리

당신이 온라인 뉴스레터를 발행하는 회사에서 마케팅 담당자라고 가정해 봅시다. 고객들이 뉴스레터 구독을 신청하는데, 어떤 고객은 실수로 여러 번 같은 이메일 주소를 입력했을 수도 있고, 시스템 오류로 인해 중복된 이메일이 저장될 수도 있습니다.

*   **원본 데이터 (중복 포함):**
    | ID | Email                | Subscription Date |
    |----|----------------------|-------------------|
    | 1  | alice@example.com    | 2023-01-01        |
    | 2  | bob@example.com      | 2023-01-05        |
    | 3  | alice@example.com    | 2023-01-10        |
    | 4  | charlie@example.com  | 2023-01-12        |
    | 5  | bob@example.com      | 2023-01-15        |

*   **문제점:** 만약 이 목록 그대로 뉴스레터를 발송하면, 'alice@example.com'과 'bob@example.com'은 뉴스레터를 두 번씩 받게 됩니다. 이는 비효율적이고 고객에게 스팸처럼 느껴질 수 있습니다.

*   **중복 제거 적용:**
    당신은 'Email' 컬럼을 기준으로 중복을 제거하여 고유한 이메일 주소 목록을 얻고 싶습니다.
    *   **관계형 대수적 사고:** `δ(π_Email(SubscriptionList))`
    *   **Pandas 코드 예시:**
        ```python
        import pandas as pd

        data = {
            'ID': [1, 2, 3, 4, 5],
            'Email': ['alice@example.com', 'bob@example.com', 'alice@example.com', 'charlie@example.com', 'bob@example.com'],
            'Subscription Date': ['2023-01-01', '2023-01-05', '2023-01-10', '2023-01-12', '2023-01-15']
        }
        df = pd.DataFrame(data)

        # 'Email' 컬럼만을 선택한 후 중복 제거
        unique_emails_df = df[['Email']].drop_duplicates()
        ```

*   **결과 (고유한 이메일 목록):**
    | Email               |
    |---------------------|
    | alice@example.com   |
    | bob@example.com     |
    | charlie@example.com |

이처럼 중복 제거를 통해 뉴스레터를 각 고객에게 단 한 번만 보낼 수 있게 되어 효율성을 높이고 고객 경험을 개선할 수 있습니다.

### 예시 2: 영화 데이터베이스에서 특정 배우와 출연 연도의 고유한 조합 찾기

당신이 영화 데이터베이스를 분석하는 연구원이라고 가정해 봅시다. 특정 배우가 여러 해에 걸쳐 다양한 영화에 출연했을 때, 각 배우가 *어떤 연도에 한 번이라도 출연했는지*의 고유한 조합을 알고 싶습니다. 즉, (배우 이름, 출연 연도)의 고유한 쌍을 얻는 것입니다.

*   **원본 데이터 (일부):**
    | Film ID | Title           | Actor Name | Release Year | Genre   |
    |---------|-----------------|------------|--------------|---------|
    | 101     | The Matrix      | Keanu      | 1999         | Sci-Fi  |
    | 102     | Speed           | Keanu      | 1994         | Action  |
    | 103     | Point Break     | Keanu      | 1991         | Action  |
    | 104     | Matrix Reloaded | Keanu      | 2003         | Sci-Fi  |
    | 105     | Matrix Revolut. | Keanu      | 2003         | Sci-Fi  |
    | 106     | John Wick       | Keanu      | 2014         | Action  |
    | 201     | Titanic         | Leonardo   | 1997         | Romance |
    | 202     | Inception       | Leonardo   | 2010         | Sci-Fi  |
    | 203     | The Revenant    | Leonardo   | 2015         | Drama   |
    | 204     | Django Unchained| Leonardo   | 2012         | Western |
    | 205     | Wolf of Wall St.| Leonardo   | 2013         | Bio     |

*   **문제점:** 'Keanu'는 2003년에 두 편의 영화('Matrix Reloaded', 'Matrix Revolutions')에 출연했습니다. 만약 단순히 모든 행을 나열하면 'Keanu, 2003'이라는 쌍이 두 번 나타나게 됩니다. 우리는 'Keanu'가 '2003'년에 *출연했다*는 사실만을 한 번 알고 싶습니다.

*   **중복 제거 적용:**
    'Actor Name'과 'Release Year' 컬럼을 기준으로 중복을 제거합니다.
    *   **관계형 대수적 사고:** `δ(π_ActorName,ReleaseYear(Movies))`
    *   **Pandas 코드 예시:**
        ```python
        import pandas as pd

        data = {
            'Film ID': [101, 102, 103, 104, 105, 106, 201, 202, 203, 204, 205],
            'Title': ['The Matrix', 'Speed', 'Point Break', 'Matrix Reloaded', 'Matrix Revolut.', 'John Wick', 'Titanic', 'Inception', 'The Revenant', 'Django Unchained', 'Wolf of Wall St.'],
            'Actor Name': ['Keanu', 'Keanu', 'Keanu', 'Keanu', 'Keanu', 'Keanu', 'Leonardo', 'Leonardo', 'Leonardo', 'Leonardo', 'Leonardo'],
            'Release Year': [1999, 1994, 1991, 2003, 2003, 2014, 1997, 2010, 2015, 2012, 2013],
            'Genre': ['Sci-Fi', 'Action', 'Action', 'Sci-Fi', 'Sci-Fi', 'Action', 'Romance', 'Sci-Fi', 'Drama', 'Western', 'Bio']
        }
        df_movies = pd.DataFrame(data)

        # 'Actor Name'과 'Release Year' 컬럼만을 선택한 후 중복 제거
        unique_actor_year = df_movies[['Actor Name', 'Release Year']].drop_duplicates()
        ```

*   **결과 (고유한 배우-출연 연도 조합):**
    | Actor Name | Release Year |
    |------------|--------------|
    | Keanu      | 1999         |
    | Keanu      | 1994         |
    | Keanu      | 1991         |
    | Keanu      | 2003         |
    | Keanu      | 2014         |
    | Leonardo   | 1997         |
    | Leonardo   | 2010         |
    | Leonardo   | 2015         |
    | Leonardo   | 2012         |
    | Leonardo   | 2013         |

이 결과로 우리는 각 배우가 어떤 연도에 출연했는지에 대한 고유한 정보만을 깔끔하게 얻을 수 있습니다. 예를 들어, 'Keanu'는 2003년에 두 편의 영화에 출연했지만, 결과에서는 'Keanu, 2003' 조합이 한 번만 나타납니다.

이처럼 중복 제거는 데이터의 본질적인 고유성을 파악하고, 불필요한 반복을 제거하여 데이터를 더욱 의미 있게 만드는 데 핵심적인 역할을 합니다.

---

## Slide 13

핵심 개념은 **다중 키를 활용한 데이터 정렬(Multi-key Data Sorting)**입니다. 이는 하나 이상의 기준으로 데이터를 정렬하는 방법을 의미하며, 각 기준에는 정렬 우선순위와 오름차순/내림차순 정렬 방향이 부여됩니다.

### 1. 개념 설명

데이터 정렬은 정보를 특정 기준에 따라 재배열하여 이해하거나 분석하기 쉽게 만드는 기본적인 데이터 처리 작업입니다. 일반적으로 하나의 열(column)을 기준으로 정렬하지만, 실제 데이터에서는 여러 기준을 동시에 적용해야 하는 경우가 많습니다.

**다중 키 정렬의 원리:**
1.  **첫 번째 기준 (Primary Key):** 데이터는 가장 먼저 지정된 키(열)를 기준으로 정렬됩니다. 이 키에 대한 오름차순(ascending) 또는 내림차순(descending)이 적용됩니다.
2.  **두 번째 기준 (Secondary Key):** 첫 번째 키의 값이 **동일한** 레코드(행)들 사이에서만 두 번째 지정된 키를 기준으로 정렬됩니다. 이 키에 대해서도 마찬가지로 오름차순 또는 내림차순이 적용됩니다.
3.  **그 이후의 기준:** 필요한 경우 세 번째, 네 번째 등 추가 키를 지정하여 동일한 값이 나오는 경우에만 다음 키를 기준으로 정렬합니다.

슬라이드의 예시는 `Year`를 첫 번째 키로 오름차순 정렬하고, 그 다음 `Count`를 두 번째 키로 내림차순 정렬하는 것을 보여줍니다.

### 2. Pandas `sort_values()` 함수

데이터 분석 라이브러리인 Pandas에서는 `DataFrame.sort_values()` 함수를 사용하여 다중 키 정렬을 쉽게 구현할 수 있습니다.

*   `df.sort_values(by=[컬럼1, 컬럼2, ...], ascending=[컬럼1_방향, 컬럼2_방향, ...])`
    *   `by`: 정렬 기준으로 사용할 컬럼 이름들의 리스트입니다. 리스트에 나열된 순서대로 정렬 우선순위가 결정됩니다 (왼쪽이 가장 높은 우선순위).
    *   `ascending`: 각 컬럼에 대한 정렬 방향을 지정하는 불리언(True/False) 값들의 리스트입니다. `True`는 오름차순(작은 값부터 큰 값), `False`는 내림차순(큰 값부터 작은 값)을 의미합니다. `by` 리스트의 컬럼 순서와 `ascending` 리스트의 불리언 순서가 일치해야 합니다.

**슬라이드 예시 코드 분석:**
```python
sorted_df = babynames.sort_values(["Year", "Count"], ascending=[True, False])
```
이 코드는 `babynames`라는 DataFrame을 다음 규칙에 따라 정렬합니다:
1.  먼저 `Year` 컬럼의 값을 **오름차순(True)**으로 정렬합니다. (예: 2000년 데이터가 2001년 데이터보다 먼저 나옴)
2.  `Year` 값이 동일한 레코드들(예: 모든 2005년 데이터) 내에서는 `Count` 컬럼의 값을 **내림차순(False)**으로 정렬합니다. (예: 2005년도 이름 중 가장 많이 사용된 이름이 먼저 나옴)

### 3. 구체적인 실생활 예시: 대학교 수강 신청 목록 정렬

당신이 다음 학기 수강 신청을 위해 대학교의 **전체 개설 강좌 목록**을 보고 있다고 상상해 보세요. 강좌 목록 DataFrame은 `Department`(학과), `CourseName`(강좌명), `Credits`(학점), `AvailableSeats`(잔여 좌석 수)와 같은 컬럼들을 포함하고 있습니다.

당신은 목록을 다음과 같은 기준으로 보고 싶습니다:
1.  **먼저, 학과(Department)별로 정렬하여 관심 있는 학과의 강좌들을 모아서 보고 싶습니다.** (예: "컴퓨터공학과" 강좌들이 "수학과" 강좌들보다 먼저 나오도록).
2.  **그 다음, 동일한 학과 내에서는 잔여 좌석이 많은 강좌부터 보고 싶습니다.** (인기 많아서 잔여 좌석이 적은 강좌들보다, 아직 여유 있는 강좌들을 먼저 확인하고 싶기 때문입니다).

이러한 요구사항을 Pandas의 `sort_values()`로 구현하면 다음과 같습니다:

```python
import pandas as pd

# 가상의 대학교 강좌 데이터프레임 생성
data = {
    'Department': ['Computer Science', 'Mathematics', 'Computer Science', 'English', 'Mathematics', 'English'],
    'CourseName': ['Data Structures', 'Calculus I', 'Algorithms', 'Introduction to Poetry', 'Linear Algebra', 'Creative Writing'],
    'Credits': [3, 3, 3, 3, 3, 3],
    'AvailableSeats': [15, 20, 5, 25, 10, 8]
}
courses_df = pd.DataFrame(data)

print("--- 원본 강좌 목록 ---")
print(courses_df)
print("\n")

# 학과(오름차순), 잔여 좌석(내림차순) 기준으로 정렬
sorted_courses = courses_df.sort_values(
    by=['Department', 'AvailableSeats'],
    ascending=[True, False]
)

print("--- 정렬된 강좌 목록 ---")
print(sorted_courses)
```

**예시 결과 설명:**

`sorted_courses` DataFrame을 출력해보면 다음과 같은 순서로 강좌들이 나타날 것입니다:

1.  `Department`가 'Computer Science'인 강좌들이 가장 먼저 나타납니다.
    *   그 안에서 `AvailableSeats`가 많은 'Data Structures' (15석)가 'Algorithms' (5석)보다 먼저 정렬됩니다.
2.  그 다음 `Department`가 'English'인 강좌들이 나타납니다.
    *   'Introduction to Poetry' (25석)가 'Creative Writing' (8석)보다 먼저 정렬됩니다.
3.  마지막으로 `Department`가 'Mathematics'인 강좌들이 나타납니다.
    *   'Calculus I' (20석)가 'Linear Algebra' (10석)보다 먼저 정렬됩니다.

이처럼 다중 키 정렬을 사용하면 복잡한 데이터도 원하는 우선순위에 따라 논리적으로 정리하여 효율적으로 정보를 탐색하고 의사결정을 내릴 수 있게 됩니다.

---

## Slide 14

## 핵심 개념 설명: 합집합, 교집합, 차집합 (관계형 대수 및 Pandas 구현)

첨부된 슬라이드는 관계형 대수(Relational Algebra)의 기본 연산인 합집합(Union), 교집합(Intersection), 차집합(Difference)을 설명하고, 이를 Python Pandas 라이브러리로 구현하는 방법을 보여줍니다. 이 연산들은 두 개의 '스키마가 동일한' (즉, 열 이름과 데이터 타입이 같은) 데이터셋을 비교하고 결합하는 데 사용됩니다.

---

### 1. 합집합 (Union) $R \cup S$

*   **개념**: 두 개의 데이터셋 R과 S에 있는 모든 고유한 행(레코드)을 포함하는 새로운 데이터셋을 만듭니다. R에 있거나 S에 있거나 둘 다에 있는 모든 항목을 포함하되, 중복되는 항목은 한 번만 나타냅니다. (집합의 개념과 동일하게 중복을 제거합니다.)
*   **구체적이고 실생활에 가까운 예시**:
    어떤 대학교에서 `수학 과목 수강생 목록`(`R`)과 `과학 과목 수강생 목록`(`S`)을 가지고 있다고 가정해 봅시다. 두 목록 모두 학생의 학번(`StudentID`)과 이름(`StudentName`) 정보를 포함합니다. 학교는 이번 학기에 *적어도 하나의 STEM(수학, 과학, 공학) 과목을 수강하는 모든 학생*에게 환영 이메일을 보내고 싶습니다.
    *   `수학 과목 수강생 목록 (R)`: `[(101, '김민준'), (102, '이서연'), (103, '박준서')]`
    *   `과학 과목 수강생 목록 (S)`: `[(102, '이서연'), (104, '최아린'), (105, '정우진')]`
    *   **합집합 결과**: `[(101, '김민준'), (102, '이서연'), (103, '박준서'), (104, '최아린'), (105, '정우진')]`
        *   `이서연(102)`은 수학과 과학을 모두 수강했지만, 합집합에서는 한 번만 나타납니다.
*   **Pandas 구현 원리**: `pd.concat([R, S], ignore_index=True)`를 사용하여 두 데이터프레임을 위아래로 단순히 붙인 다음, `.drop_duplicates()`를 호출하여 중복되는 행을 제거함으로써 고유한 학생 목록을 만듭니다.

---

### 2. 교집합 (Intersection) $R \cap S$

*   **개념**: 두 개의 데이터셋 R과 S에 *모두 존재하는* 고유한 행만을 포함하는 새로운 데이터셋을 만듭니다.
*   **구체적이고 실생활에 가까운 예시**:
    위의 예시와 동일하게 `수학 과목 수강생 목록`(`R`)과 `과학 과목 수강생 목록`(`S`)이 있습니다. 학교는 `수학과 과학을 모두 수강하는 학생들`만을 대상으로 하는 '통합 STEM 심화 과정'을 홍보하고 싶습니다.
    *   `수학 과목 수강생 목록 (R)`: `[(101, '김민준'), (102, '이서연'), (103, '박준서')]`
    *   `과학 과목 수강생 목록 (S)`: `[(102, '이서연'), (104, '최아린'), (105, '정우진')]`
    *   **교집합 결과**: `[(102, '이서연')]`
        *   `이서연(102)`만이 수학과 과학을 모두 수강하는 학생입니다.
*   **Pandas 구현 원리**: `R.merge(S, how="inner")`를 사용합니다. `inner` 조인은 두 데이터프레임 모두에 키(여기서는 `StudentID`와 `StudentName` 같은 모든 컬럼)가 일치하는 행만 반환하므로 교집합과 동일한 결과를 얻습니다.

---

### 3. 차집합 (Difference) $R - S$

*   **개념**: 데이터셋 R에는 존재하지만, 데이터셋 S에는 존재하지 않는 모든 고유한 행만을 포함하는 새로운 데이터셋을 만듭니다. 순서가 중요하며, $R - S$는 $S - R$과 다릅니다.
*   **구체적이고 실생활에 가까운 예시**:
    다시 `수학 과목 수강생 목록`(`R`)과 `과학 과목 수강생 목록`(`S`)을 사용합니다. 학교는 이번 학기에 `수학만 수강하고, 과학은 수강하지 않는 학생들`을 대상으로 '과학 기초 학습 자료'를 배포하고 싶습니다.
    *   `수학 과목 수강생 목록 (R)`: `[(101, '김민준'), (102, '이서연'), (103, '박준서')]`
    *   `과학 과목 수강생 목록 (S)`: `[(102, '이서연'), (104, '최아린'), (105, '정우진')]`
    *   **차집합 결과 ($R - S$)**: `[(101, '김민준'), (103, '박준서')]`
        *   `김민준(101)`과 `박준서(103)`는 수학을 수강하지만, 과학은 수강하지 않습니다. `이서연(102)`은 수학을 수강하지만 과학도 수강하므로 이 목록에 포함되지 않습니다.
*   **Pandas 구현 원리**: `R.merge(S, how="left", indicator=True)`를 사용합니다.
    *   `how="left"`는 R의 모든 행을 유지하고 S에서 일치하는 행을 찾습니다.
    *   `indicator=True`는 `_merge`라는 새로운 열을 추가하여 각 행이 어디에서 왔는지(`left_only`, `right_only`, `both`) 알려줍니다.
    *   `.query("_merge == 'left_only'")`를 사용하여 R에만 있는 행(즉, S에는 없는 R의 행)만을 필터링합니다.
    *   마지막으로 `.drop(columns=['_merge'])`를 통해 임시로 생성된 `_merge` 열을 제거하여 최종 결과를 얻습니다.

---

## Slide 15

### 핵심 개념 및 설명

1.  **카테시안 곱 (Cartesian Product 또는 Product $R \times S$)**
    *   **정의:** 두 릴레이션(테이블) R과 S의 모든 가능한 튜플(행) 조합을 생성합니다. 릴레이션 R의 모든 행이 릴레이션 S의 모든 행과 한 번씩 짝지어져 새로운 튜플을 만듭니다. 결과 릴레이션의 행 수는 R의 행 수와 S의 행 수를 곱한 것과 같고, 열 수는 두 릴레이션의 열 수를 합한 것과 같습니다.
    *   **형식:** `R × S = {t ∘ u | t ∈ R, u ∈ S}` (R의 각 튜플 `t`와 S의 각 튜플 `u`를 결합)
    *   **Pandas 구현:** `pd.merge(R, S, how="cross")`
    *   **실생활 예시:**
        당신이 점심 식당을 운영하고 있고, `메인 메뉴` 목록과 `사이드 메뉴` 목록이 있다고 가정해 봅시다.
        *   **메인 메뉴 (R):**
            | MainDish | Price |
            |----------|-------|
            | 파스타   | 15000 |
            | 스테이크 | 25000 |
        *   **사이드 메뉴 (S):**
            | SideDish | Calories |
            |----------|----------|
            | 샐러드   | 100      |
            | 수프     | 150      |
            | 빵       | 80       |
        이 두 테이블의 카테시안 곱은 고객에게 제공할 수 있는 모든 메인 메뉴와 사이드 메뉴 조합을 생성합니다.
        *   **결과 (R × S):**
            | MainDish | Price | SideDish | Calories |
            |----------|-------|----------|----------|
            | 파스타   | 15000 | 샐러드   | 100      |
            | 파스타   | 15000 | 수프     | 150      |
            | 파스타   | 15000 | 빵       | 80       |
            | 스테이크 | 25000 | 샐러드   | 100      |
            | 스테이크 | 25000 | 수프     | 150      |
            | 스테이크 | 25000 | 빵       | 80       |

2.  **세타 조인 (Theta Join)**
    *   **정의:** 카테시안 곱을 수행한 결과에 특정 조건(술어 $\theta$)을 적용하여 필터링하는 조인입니다. 이 조건은 동등(`=`)뿐만 아니라 크다(`>`), 작다(`<`), 같지 않다(`!=`) 등 다양한 비교 연산자를 포함할 수 있습니다.
    *   **형식:** `R × S`에 `θ` 필터 적용
    *   **실생활 예시:**
        위의 `메인 메뉴`와 `사이드 메뉴` 카테시안 곱 결과에서, '메인 메뉴의 가격이 사이드 메뉴의 칼로리의 100배를 초과하는 조합'이라는 조건($\theta$: `Price > Calories * 100`)을 적용하는 것이 세타 조인입니다.
        *   **조건:** `Price > Calories * 100`
        *   **결과:**
            | MainDish | Price | SideDish | Calories |
            |----------|-------|----------|----------|
            | 파스타   | 15000 | 샐러드   | 100      | (15000 > 100 * 100 = 10000)
            | 스테이크 | 25000 | 샐러드   | 100      | (25000 > 100 * 100 = 10000)
            | 스테이크 | 25000 | 수프     | 150      | (25000 > 150 * 100 = 15000)
            | 스테이크 | 25000 | 빵       | 80       | (25000 > 80 * 100 = 8000)

3.  **동등 조인 (Equi-Join)**
    *   **정의:** 세타 조인의 특별한 형태로, 조인 조건이 오직 동등(`=`) 비교만으로 이루어집니다. 두 릴레이션이 하나 이상의 공통 속성(컬럼)을 가지고 있을 때, 그 속성들의 값이 같은 행들만 결합합니다. 일반적으로 가장 많이 사용되는 조인 형태입니다.
    *   **형식:** `R ⋈Year=Year S` (Year 속성이 같은 경우 결합)
    *   **Pandas 구현:** `pd.merge(df1, df2, on="공통컬럼", how="inner")`
    *   **실생활 예시:**
        슬라이드에서 제시된 `babynames` (아기 이름 데이터)와 `yr_total` (연도별 전체 아기 수 데이터)를 `Year`라는 공통 컬럼을 기준으로 동등 조인하는 예시입니다.
        *   **babynames (예시):**
            | Year | Name  | Count |
            |------|-------|-------|
            | 2010 | James | 14781 |
            | 2010 | Mary  | 13627 |
            | 2011 | John  | 15000 |
        *   **yr_total (연도별 전체 아기 수, `babynames`에서 `Year`별 `Count`를 합산하여 생성):**
            | Year | year_total |
            |------|------------|
            | 2010 | 28408      |
            | 2011 | 15000      |
        *   **동등 조인 (`on="Year"`, `how="inner"`) 결과:** `pd.merge(babynames, yr_total, on="Year", how="inner")`
            `babynames`의 각 행에 해당 `Year`의 전체 아기 수(`year_total`)가 추가됩니다.
            | Year | Name  | Count | year_total |
            |------|-------|-------|------------|
            | 2010 | James | 14781 | 28408      |
            | 2010 | Mary  | 13627 | 28408      |
            | 2011 | John  | 15000 | 15000      |
        이 조인을 통해 우리는 특정 아기 이름의 출생 수(`Count`)와 해당 연도의 전체 출생 수(`year_total`)를 한눈에 비교할 수 있게 됩니다.

4.  **자연 조인 (Natural Join)**
    *   **정의:** 동등 조인의 한 종류로, 두 릴레이션에 이름과 도메인이 같은 공통 속성이 있을 때, 그 속성들을 기준으로 동등 조인을 수행하며, 결과에서 중복되는 조인 속성(컬럼)을 제거합니다. 즉, 공통 컬럼이 한 번만 나타납니다. (슬라이드에 명시적인 pandas 예시는 없지만, 개념적으로 알아두면 좋습니다.)
    *   **실생활 예시:**
        *   **직원 (R):**
            | EmployeeID | Name  | DepartmentID |
            |------------|-------|--------------|
            | 1          | Alice | 101          |
            | 2          | Bob   | 102          |
        *   **부서 (S):**
            | DepartmentID | DepartmentName | Location |
            |--------------|----------------|----------|
            | 101          | Sales          | Seoul    |
            | 102          | Marketing      | Busan    |
        *   **자연 조인 결과:** `DepartmentID`를 기준으로 동등 조인하며, 결과에서 `DepartmentID` 컬럼은 한 번만 나타납니다.
            | EmployeeID | Name  | DepartmentID | DepartmentName | Location |
            |------------|-------|--------------|----------------|----------|
            | 1          | Alice | 101          | Sales          | Seoul    |
            | 2          | Bob   | 102          | Marketing      | Busan    |

---

## Slide 16

주어진 슬라이드는 Pandas 라이브러리에서 두 개의 DataFrame을 특정 컬럼(column keys)을 기준으로 결합하는 `merge` 함수와 다양한 조인(Join) 방식에 대해 설명하고 있습니다.

---

### **핵심 개념: Pandas `merge`를 이용한 데이터프레임 결합**

Pandas의 `df.merge()` 함수는 SQL의 JOIN과 유사하게 두 개의 데이터프레임(DataFrame)을 하나 이상의 공통 컬럼(column keys)을 기준으로 결합합니다. 이를 통해 서로 다른 정보가 담긴 데이터프레임을 하나로 합쳐서 더 풍부한 정보를 얻을 수 있습니다.

#### **1. `merge` 함수의 기본 사용법 (`inner` join이 기본)**

*   **문법**: `df.merge(other_df, on='key_column')`
*   **설명**: `df`에 `other_df`를 `key_column`을 기준으로 병합합니다. 기본적으로 `how='inner'` 방식으로 동작합니다.
*   **`on` 파라미터**: 두 데이터프레임에서 공통으로 존재하는 컬럼의 이름을 지정하여, 해당 컬럼의 값이 일치하는 행들끼리 결합하도록 합니다.

#### **2. 다양한 조인(Join) 방식 (`how` 파라미터)**

`how` 파라미터를 사용하여 데이터를 결합하는 방식을 지정할 수 있습니다.

*   **`how='inner'` (내부 조인)**
    *   `on`으로 지정된 `key_column`의 값이 **두 데이터프레임 모두에 존재하는 행만** 결합하여 결과로 반환합니다.
    *   어느 한쪽에라도 일치하는 키가 없는 행은 결과에서 제외됩니다.
    *   슬라이드의 예시에서는 `df`와 `df1` 모두에 'Vienna'만 존재하므로, 'Vienna'에 대한 정보만 결합됩니다.

*   **`how='left'` (좌측 외부 조인)**
    *   `df` (왼쪽 데이터프레임)의 **모든 행을 유지**합니다.
    *   `on`으로 지정된 `key_column`의 값이 `other_df` (오른쪽 데이터프레임)에 일치하는 행이 있으면 해당 정보를 결합합니다.
    *   만약 `other_df`에 일치하는 키가 없으면, `other_df`에서 가져올 컬럼의 값은 `NaN` (Not a Number, 결측치)으로 채워집니다.
    *   슬라이드 예시에서 'Oslo'는 `df`에만 있고 `df1`에는 없으므로, 'area' 컬럼이 `NaN`으로 채워집니다.

*   **`how='right'` (우측 외부 조인)**
    *   `other_df` (오른쪽 데이터프레임)의 **모든 행을 유지**합니다.
    *   `on`으로 지정된 `key_column`의 값이 `df` (왼쪽 데이터프레임)에 일치하는 행이 있으면 해당 정보를 결합합니다.
    *   만약 `df`에 일치하는 키가 없으면, `df`에서 가져올 컬럼의 값은 `NaN`으로 채워집니다.
    *   슬라이드 예시에서 'Tokyo'는 `df1`에만 있고 `df`에는 없으므로, 'population' 컬럼이 `NaN`으로 채워집니다.

*   **`how='outer'` (전체 외부 조인 또는 완전 외부 조인)**
    *   `df`와 `other_df`의 **모든 행을 유지**합니다.
    *   `on`으로 지정된 `key_column`의 값이 어느 한쪽에만 존재하더라도 결과에 포함됩니다.
    *   일치하는 키가 없는 쪽의 컬럼 값은 `NaN`으로 채워집니다.
    *   슬라이드 예시에서 'Oslo', 'Vienna', 'Tokyo' 모두 결과에 포함되며, 일치하지 않는 정보는 `NaN`으로 표시됩니다.

#### **3. 중복 키 처리 (Many-to-Many Match)**

*   **설명**: 만약 `on`으로 지정된 `key_column`에 **두 데이터프레임 모두에서 중복된 값(key)이 존재**한다면, `merge` 함수는 해당 키를 가진 모든 조합의 행들을 만들어냅니다 (데카르트 곱, Cartesian product). 이는 원치 않는 결과 행의 증가를 초래할 수 있으므로, 중복 키가 예상될 때는 주의해서 사용하거나 전처리해야 합니다.

---

### **구체적인 실생활 예시: 온라인 쇼핑몰의 주문 및 고객 정보 결합**

우리가 온라인 쇼핑몰을 운영한다고 가정해봅시다. 두 개의 데이터프레임을 가지고 있습니다.

1.  **`df_customers` (고객 정보)**:
    *   `customer_id`: 고객 ID
    *   `name`: 고객 이름
    *   `city`: 거주 도시

2.  **`df_orders` (주문 정보)**:
    *   `order_id`: 주문 ID
    *   `customer_id`: 주문한 고객 ID
    *   `product`: 주문 상품
    *   `amount`: 주문 금액

이 두 데이터프레임을 `customer_id`를 기준으로 병합하여, 특정 고객의 주문 내역이나 특정 주문의 고객 정보를 알고 싶을 때 `merge`를 사용할 수 있습니다.

```python
import pandas as pd
import numpy as np

# 고객 정보 데이터프레임
df_customers = pd.DataFrame({
    'customer_id': [101, 102, 103, 104],
    'name': ['김철수', '이영희', '박지민', '최수빈'],
    'city': ['서울', '부산', '대구', '인천']
})

# 주문 정보 데이터프레임
df_orders = pd.DataFrame({
    'order_id': ['A001', 'A002', 'A003', 'A004', 'A005'],
    'customer_id': [101, 103, 101, 105, 103], # 105번 고객은 아직 df_customers에 없음
    'product': ['노트북', '마우스', '키보드', '모니터', '헤드셋'],
    'amount': [1200000, 30000, 70000, 250000, 80000]
})

print("--- df_customers ---")
print(df_customers)
print("\n--- df_orders ---")
print(df_orders)
```

**결과:**
```
--- df_customers ---
   customer_id   name city
0          101  김철수   서울
1          102  이영희   부산
2          103  박지민   대구
3          104  최수빈   인천

--- df_orders ---
   order_id  customer_id product    amount
0     A001          101    노트북   1200000
1     A002          103    마우스     30000
2     A003          101    키보드     70000
3     A004          105    모니터    250000
4     A005          103    헤드셋     80000
```

#### **예시 1: `how='inner'` (내부 조인)**

*   **목표**: **주문 내역이 있는 고객 정보만** 확인하고 싶을 때
*   `df_customers`와 `df_orders` 모두에 존재하는 `customer_id` (101, 103)에 해당하는 정보만 결합됩니다.
*   102, 104번 고객은 주문이 없고, 105번 고객의 주문은 고객 정보에 없으므로 모두 제외됩니다.

```python
inner_join_df = df_customers.merge(df_orders, on='customer_id', how='inner')
print("\n--- Inner Join (주문이 있는 고객 정보) ---")
print(inner_join_df)
```

**결과:**
```
--- Inner Join (주문이 있는 고객 정보) ---
   customer_id   name city order_id product    amount
0          101  김철수   서울     A001    노트북   1200000
1          101  김철수   서울     A003    키보드     70000
2          103  박지민   대구     A002    마우스     30000
3          103  박지민   대구     A005    헤드셋     80000
```
*설명: 101번 고객은 2개의 주문을 했기 때문에 '김철수' 정보가 두 번 나타납니다. 102, 104번 고객 정보나 105번 고객의 주문 정보는 결과에 없습니다.*

#### **예시 2: `how='left'` (좌측 외부 조인)**

*   **목표**: **모든 고객의 정보는 유지하되, 있다면 주문 내역도 함께** 보고 싶을 때
*   `df_customers` (왼쪽)의 모든 행이 유지됩니다.
*   주문이 없는 고객(102, 104)의 경우, 주문 관련 컬럼(`order_id`, `product`, `amount`)은 `NaN`으로 채워집니다.

```python
left_join_df = df_customers.merge(df_orders, on='customer_id', how='left')
print("\n--- Left Join (모든 고객의 정보 + 주문 내역) ---")
print(left_join_df)
```

**결과:**
```
--- Left Join (모든 고객의 정보 + 주문 내역) ---
   customer_id   name city order_id product     amount
0          101  김철수   서울     A001    노트북  1200000.0
1          101  김철수   서울     A003    키보드    70000.0
2          102  이영희   부산      NaN     NaN        NaN
3          103  박지민   대구     A002    마우스    30000.0
4          103  박지민   대구     A005    헤드셋    80000.0
5          104  최수빈   인천      NaN     NaN        NaN
```
*설명: 102, 104번 고객은 주문 내역이 없으므로 주문 관련 정보는 NaN으로 표시됩니다.*

#### **예시 3: `how='right'` (우측 외부 조인)**

*   **목표**: **모든 주문 내역은 유지하되, 있다면 고객 정보도 함께** 보고 싶을 때
*   `df_orders` (오른쪽)의 모든 행이 유지됩니다.
*   고객 정보에 없는 주문(105번 고객의 주문)의 경우, 고객 관련 컬럼(`name`, `city`)은 `NaN`으로 채워집니다.

```python
right_join_df = df_customers.merge(df_orders, on='customer_id', how='right')
print("\n--- Right Join (모든 주문 내역 + 고객 정보) ---")
print(right_join_df)
```

**결과:**
```
--- Right Join (모든 주문 내역 + 고객 정보) ---
   customer_id   name  city order_id product    amount
0          101  김철수    서울     A001    노트북   1200000
1          103  박지민    대구     A002    마우스     30000
2          101  김철수    서울     A003    키보드     70000
3          105    NaN   NaN     A004    모니터    250000
4          103  박지민    대구     A005    헤드셋     80000
```
*설명: 105번 고객은 아직 `df_customers`에 등록되지 않은 가상의 고객이라고 가정하면, 해당 고객의 주문은 유지되지만 고객 이름과 도시는 NaN으로 표시됩니다.*

#### **예시 4: `how='outer'` (전체 외부 조인)**

*   **목표**: **모든 고객 정보와 모든 주문 내역을 한눈에** 보고 싶을 때
*   `df_customers`와 `df_orders`의 모든 `customer_id`가 결과에 포함됩니다.
*   어느 한쪽에만 있는 정보는 `NaN`으로 채워집니다.

```python
outer_join_df = df_customers.merge(df_orders, on='customer_id', how='outer')
print("\n--- Outer Join (모든 고객 + 모든 주문) ---")
print(outer_join_df)
```

**결과:**
```
--- Outer Join (모든 고객 + 모든 주문) ---
   customer_id   name  city order_id product     amount
0          101  김철수    서울     A001    노트북  1200000.0
1          101  김철수    서울     A003    키보드    70000.0
2          102  이영희    부산      NaN     NaN        NaN
3          103  박지민    대구     A002    마우스    30000.0
4          103  박지민    대구     A005    헤드셋    80000.0
5          104  최수빈    인천      NaN     NaN        NaN
6          105    NaN   NaN     A004    모니터   250000.0
```
*설명: 주문이 없는 102, 104번 고객의 주문 정보는 NaN, 고객 정보에 없는 105번 고객의 이름/도시는 NaN으로 표시되어 모든 정보가 하나의 표에 나타납니다.*

---

이 예시를 통해 `merge` 함수의 동작 방식과 각 `how` 옵션이 실제 데이터 분석에서 어떻게 다른 결과를 가져오는지 명확히 이해하셨기를 바랍니다. 데이터프레임을 결합할 때는 원하는 결과에 따라 적절한 조인 방식을 선택하는 것이 중요합니다.

---

## Slide 17

`DataFrame.join`: 인덱스 기반 데이터 결합

`DataFrame.join` 메서드는 두 개의 DataFrame을 인덱스를 기준으로 결합(merge)하는 강력한 방법입니다. 관계형 데이터베이스의 조인(JOIN)과 유사하지만, 기본적으로는 DataFrame의 인덱스를 '키'로 사용하여 데이터를 정렬하고 합칩니다.

---

### 핵심 개념

1.  **인덱스 정렬 결합 (Index-Aligned Join)**
    `df.join(df1)`은 `df` (왼쪽 DataFrame)와 `df1` (오른쪽 DataFrame)의 인덱스 값을 비교하여 일치하는 행을 연결합니다. 만약 인덱스가 다르면, `on` 파라미터를 사용하여 특정 컬럼을 키로 지정할 수도 있지만, 기본 동작은 인덱스를 사용합니다.

2.  **결합 유형 (`how` 파라미터)**
    `how` 파라미터는 어떤 방식으로 DataFrame들을 결합할지 지정하며, 다음 네 가지 유형이 있습니다:

    *   **`'inner'`**: 양쪽 DataFrame에 모두 존재하는 인덱스만 결과에 포함합니다. (교집합)
    *   **`'left'` (기본값)**: 왼쪽 DataFrame의 모든 인덱스를 유지하고, 오른쪽 DataFrame에서 일치하는 인덱스의 데이터를 가져옵니다. 오른쪽 DataFrame에 해당 인덱스가 없으면 `NaN`으로 채웁니다.
    *   **`'right'`**: 오른쪽 DataFrame의 모든 인덱스를 유지하고, 왼쪽 DataFrame에서 일치하는 인덱스의 데이터를 가져옵니다. 왼쪽 DataFrame에 해당 인덱스가 없으면 `NaN`으로 채웁니다.
    *   **`'outer'`**: 양쪽 DataFrame에 존재하는 모든 고유한 인덱스를 결과에 포함합니다. 일치하는 데이터가 없는 곳은 `NaN`으로 채웁니다. (합집합)

3.  **`pd.concat`과의 차이**:
    `df.join`은 인덱스(또는 지정된 키 컬럼)를 기반으로 **논리적인 매칭**을 통해 데이터를 결합합니다. 반면 `pd.concat([df, df1], axis=1)`은 기본적으로 인덱스를 따라 열을 합치지만, 슬라이드에서 언급하듯이 "key logic 없이 단순히 열을 쌓는 경우"와는 다릅니다. `join`은 데이터 간의 관계를 기반으로 필터링하고 매칭하는 데 초점을 맞춥니다.

---

### 실생활 예시: 학생 정보 및 성적 데이터 결합

**시나리오:** 대학교에서 학생들의 기본 정보와 수강 과목 성적을 두 개의 다른 데이터베이스에 관리하고 있다고 가정해봅시다. 각 학생은 고유한 학번(student_id)을 가지고 있으며, 이 학번을 인덱스로 사용하겠습니다.

**1. 학생 기본 정보 DataFrame (`df_info`) - 왼쪽 DataFrame**
| `student_id` (인덱스) | `name` | `major` |
| :-------------------- | :----- | :------ |
| `101`                 | Alice  | CS      |
| `102`                 | Bob    | EE      |
| `103`                 | Carol  | Math    |

**2. 학생 성적 정보 DataFrame (`df_grades`) - 오른쪽 DataFrame**
| `student_id` (인덱스) | `course` | `grade` |
| :-------------------- | :------- | :------ |
| `102`                 | Physics  | B+      |
| `103`                 | Calculus | A-      |
| `104`                 | David    | C       |
*(주의: 학생 `104`는 성적 정보는 있지만, `df_info`에는 없는 가상의 학생입니다. 학생 `101`은 정보는 있지만 성적 정보는 없습니다.)*

#### 1) `'inner'` join: 양쪽 모두 존재하는 학생만 보기

```python
# df_info.join(df_grades, how='inner')
```
**결과:** `student_id`가 `df_info`와 `df_grades` 모두에 있는 학생만 나옵니다.
| `student_id` | `name` | `major` | `course` | `grade` |
| :----------- | :----- | :------ | :------- | :------ |
| `102`        | Bob    | EE      | Physics  | B+      |
| `103`        | Carol  | Math    | Calculus | A-      |
*설명: Alice(101)는 성적 정보가 없고, David(104)는 기본 정보가 없으므로 제외됩니다. Bob과 Carol만 양쪽에 모두 존재합니다.*

#### 2) `'left'` join (기본값): 왼쪽(기본 정보)의 모든 학생을 보기

```python
# df_info.join(df_grades, how='left')
# 또는 df_info.join(df_grades)
```
**결과:** `df_info`의 모든 학생이 포함되고, `df_grades`에서 일치하는 정보가 없는 경우 `NaN`으로 채워집니다.
| `student_id` | `name` | `major` | `course`   | `grade` |
| :----------- | :----- | :------ | :--------- | :------ |
| `101`        | Alice  | CS      | `NaN`      | `NaN`   |
| `102`        | Bob    | EE      | Physics    | B+      |
| `103`        | Carol  | Math    | Calculus   | A-      |
*설명: Alice(101)는 성적 정보가 없으므로 `course`와 `grade`가 `NaN`으로 표시됩니다. `df_info`에 없는 David(104)는 결과에 포함되지 않습니다.*

#### 3) `'right'` join: 오른쪽(성적 정보)의 모든 학생을 보기

```python
# df_info.join(df_grades, how='right')
```
**결과:** `df_grades`의 모든 학생이 포함되고, `df_info`에서 일치하는 정보가 없는 경우 `NaN`으로 채워집니다.
| `student_id` | `name` | `major` | `course`   | `grade` |
| :----------- | :----- | :------ | :--------- | :------ |
| `102`        | Bob    | EE      | Physics    | B+      |
| `103`        | Carol  | Math    | Calculus   | A-      |
| `104`        | `NaN`  | `NaN`   | Chemistry | C       |
*설명: David(104)는 기본 정보가 없으므로 `name`과 `major`가 `NaN`으로 표시됩니다. `df_grades`에 없는 Alice(101)는 결과에 포함되지 않습니다.*

#### 4) `'outer'` join: 양쪽의 모든 학생을 보기

```python
# df_info.join(df_grades, how='outer')
```
**결과:** `df_info`와 `df_grades`에 있는 모든 고유한 `student_id`가 포함되고, 데이터가 없는 곳은 `NaN`으로 채워집니다.
| `student_id` | `name` | `major` | `course`   | `grade` |
| :----------- | :----- | :------ | :--------- | :------ |
| `101`        | Alice  | CS      | `NaN`      | `NaN`   |
| `102`        | Bob    | EE      | Physics    | B+      |
| `103`        | Carol  | Math    | Calculus   | A-      |
| `104`        | `NaN`  | `NaN`   | Chemistry | C       |
*설명: Alice(101)는 성적 정보가 없어 `NaN`이, David(104)는 기본 정보가 없어 `NaN`이 채워집니다. 양쪽 모두의 모든 학생 데이터가 하나로 합쳐집니다.*

이 예시를 통해 `DataFrame.join`이 데이터 분석에서 서로 다른 정보 소스를 통합하는 데 얼마나 유용하고 유연한지 이해하는 데 도움이 되었기를 바랍니다.

---

## Slide 18

데이터프레임(DataFrame) 병합 및 컬럼 관리 방법에 대한 핵심 개념을 자세히 살펴보겠습니다.

### 1. 다른 이름의 키(Key) 컬럼으로 병합하기 (`left_on`, `right_on`)

데이터프레임을 병합할 때, 각 테이블에서 공통으로 참조해야 하는 컬럼의 이름이 다를 수 있습니다. 이럴 때 `left_on`과 `right_on` 인자를 사용하여 왼쪽(첫 번째) 데이터프레임의 어떤 컬럼과 오른쪽(두 번째) 데이터프레임의 어떤 컬럼을 기준으로 병합할지 명시할 수 있습니다.

**예시:**
당신이 두 개의 다른 부서에서 관리하는 학생 정보와 성적 정보를 통합해야 한다고 가정해 봅시다.

*   **학생 정보 데이터프레임 (`students_info`):**
    | student_id | name | major |
    | :--------- | :--- | :---- |
    | S101       | 김철수 | 컴퓨터공학 |
    | S102       | 이영희 | 경영학 |
    | S103       | 박민준 | 통계학 |

*   **성적 정보 데이터프레임 (`grades`):**
    | student_number | course | grade |
    | :------------- | :----- | :---- |
    | S101           | 자료구조 | A+    |
    | S102           | 회계원리 | B     |
    | S104           | 미적분학 | C+    |

여기서 `students_info`의 `student_id`와 `grades`의 `student_number`는 같은 의미를 가지지만 이름이 다릅니다. 이 두 데이터프레임을 합치려면 다음과 같이 병합할 수 있습니다:

```python
merged_df = students_info.merge(grades, left_on='student_id', right_on='student_number')
```

이 코드를 실행하면 `student_id`와 `student_number` 컬럼을 기준으로 데이터를 병합하여, 각 학생의 이름, 전공, 수강 과목, 성적 정보를 한눈에 볼 수 있는 새로운 데이터프레임이 생성됩니다.

### 2. 병합 후 중복 및 불필요한 컬럼 정리하기

병합 작업을 수행하고 나면, 때때로 원본 데이터프레임에 있던 컬럼들이 모두 결과 데이터프레임에 포함될 수 있습니다. 특히 `left_on`과 `right_on`으로 다른 이름의 키 컬럼을 사용한 경우, 두 키 컬럼이 모두 남아서 중복된 정보를 보여주게 됩니다. 또한, 최종적으로 필요한 정보만 선택적으로 남기고 싶을 수 있습니다. 이럴 때는 원하는 컬럼만 선택하여 새로운 데이터프레임을 만들거나 기존 데이터프레임을 수정합니다.

**예시:**
위의 `merged_df` 결과를 보면 `student_id`와 `student_number` 컬럼이 모두 남아있을 것입니다. 이 두 컬럼은 같은 정보를 나타내므로 하나만 있어도 충분하고, 어떤 보고서에서는 특정 정보(예: 학과와 성적)만 필요할 수 있습니다.

```python
# merged_df 결과 예시:
#    student_id  name    major student_number course grade
# 0        S101  김철수  컴퓨터공학           S101   자료구조    A+
# 1        S102  이영희   경영학           S102   회계원리     B
# (S103은 grades에 없으므로 merge에서 제외됨. S104는 students_info에 없으므로 제외됨.)

# 불필요한 student_number 컬럼 제거 및 필요한 컬럼만 선택
final_report_df = merged_df[['name', 'major', 'course', 'grade']]
```

이렇게 하면 `student_id`와 `student_number`의 중복을 제거하고, 보고서에 필요한 학생 이름, 전공, 과목, 성적 정보만 담긴 깔끔한 데이터프레임을 얻을 수 있습니다. 슬라이드에서는 `df.filter(['city', 'state'])`를 사용하여 이와 같은 컬럼 선택 및 정리를 수행하는 것을 보여줍니다.

### 3. 컬럼 이름 충돌 해결하기 (`suffixes` 또는 `lsuffix`/`rsuffix`)

병합하는 두 데이터프레임에 **키(Key) 컬럼이 아닌 다른 컬럼들의 이름이 동일한 경우**가 있을 수 있습니다. 예를 들어, `sales` 데이터프레임과 `marketing` 데이터프레임 모두에 `budget`이라는 컬럼이 있다고 생각해 봅시다. 이때 Pandas는 기본적으로 컬럼 이름 뒤에 `_x`와 `_y`를 붙여서 구분합니다 (`budget_x`, `budget_y`). 하지만 `suffixes` 인자를 사용하면 더 의미 있는 접미사를 지정하여 컬럼들을 명확하게 구분할 수 있습니다.

**예시:**
당신이 두 개의 다른 온라인 쇼핑몰(A, B)에서 판매하는 상품 데이터를 통합한다고 가정해 봅시다.

*   **쇼핑몰 A 상품 데이터 (`shop_A`):**
    | product_id | name | price | category |
    | :--------- | :--- | :---- | :------- |
    | P001       | 셔츠   | 25000 | 의류     |
    | P002       | 청바지  | 40000 | 의류     |

*   **쇼핑몰 B 상품 데이터 (`shop_B`)::**
    | item_id | name | price | stock_quantity |
    | :------ | :--- | :---- | :------------- |
    | P001    | 셔츠   | 27000 | 100            |
    | P003    | 스커트  | 35000 | 50             |

이 두 데이터프레임을 `product_id` (쇼핑몰 A)와 `item_id` (쇼핑몰 B)를 기준으로 병합하려고 합니다. 여기서 `name`과 `price` 컬럼은 양쪽에 모두 존재합니다.

```python
merged_products = shop_A.merge(shop_B, left_on='product_id', right_on='item_id',
                              suffixes=('_A', '_B'))
```

이 코드를 실행하면 다음과 같은 결과가 나타날 것입니다:

| product_id | name_A | price_A | category | item_id | name_B | price_B | stock_quantity |
| :--------- | :----- | :------ | :------- | :------ | :----- | :------ | :------------- |
| P001       | 셔츠     | 25000   | 의류     | P001    | 셔츠     | 27000   | 100            |

`name` 컬럼은 `name_A`와 `name_B`로, `price` 컬럼은 `price_A`와 `price_B`로 이름이 변경되어, 각 컬럼이 어느 쇼핑몰에서 왔는지 명확히 알 수 있습니다. 이처럼 `suffixes`를 사용하면 병합 시 발생하는 컬럼 이름 충돌을 의미론적으로 해결할 수 있어 데이터 분석의 명확성을 높일 수 있습니다. (참고로 `join` 메소드에서는 `lsuffix`와 `rsuffix` 인자를 사용합니다.)

---

## Slide 19

데이터 분석에서 두 개 이상의 데이터셋(테이블 또는 데이터프레임)을 특정 기준에 따라 결합하고 필터링하는 데 사용되는 핵심 연산인 **Outer Joins, Semijoin, Antijoin**에 대해 자세히 설명해 드릴게요. 이 연산들은 데이터의 관계를 이해하고 필요한 정보만 효율적으로 추출하는 데 매우 중요합니다.

---

### 1. Outer Join (외부 조인)

**핵심 개념:**
Outer Join은 두 테이블을 결합할 때, **매칭되는 레코드뿐만 아니라 매칭되지 않는 레코드도 모두 포함**시키는 방식입니다. 매칭되지 않는 레코드의 경우, 다른 테이블의 해당 컬럼 값은 `null` (Pandas에서는 `NaN`)로 채워집니다.

**구체적인 실생활 예시:**
당신이 대학교에서 **학생 명단**(`students` 테이블)과 **수강 신청 내역**(`enrollments` 테이블)을 가지고 있다고 상상해 보세요.

*   `students` 테이블: (학번, 이름, 학과) - `[(101, '김민수', '컴퓨터'), (102, '이유진', '경영'), (103, '박서준', '디자인')]`
*   `enrollments` 테이블: (수강번호, 학번, 과목명) - `[(S1, 101, '자료구조'), (S2, 101, '알고리즘'), (S3, 102, '회계원리')]`

여기서 `students` 테이블의 '박서준'(학번 103) 학생은 아직 수강 신청을 하지 않았고, `enrollments` 테이블에는 학번 104인 가상의 '최지우' 학생이 실수로 등록된 과목이 있다고 가정해 봅시다.

`학번`을 기준으로 Outer Join을 수행하면:
*   매칭되는 김민수, 이유진 학생의 정보와 수강 내역이 모두 나옵니다.
*   수강 신청을 하지 않은 박서준 학생의 이름과 학과는 나오지만, 수강번호, 과목명 컬럼은 `null`로 채워집니다.
*   가상의 최지우 학생이 등록된 과목 정보(수강번호, 과목명)는 나오지만, 이름, 학과 컬럼은 `null`로 채워집니다.

**목적:** 두 데이터셋의 모든 정보를 확인하고 싶을 때, 특히 어느 한쪽에만 존재하는 데이터를 놓치고 싶지 않을 때 사용합니다. 매칭 여부와 관계없이 전체적인 현황을 파악하는 데 유용합니다.

**Pandas 코드:**
```python
outer = pd.merge(babynames, yr_total, on="Year", how="outer")
```
`babynames`와 `yr_total` 데이터프레임을 `Year` 컬럼을 기준으로 외부 조인합니다. 이는 `babynames`에만 있는 연도, `yr_total`에만 있는 연도, 그리고 양쪽에 모두 있는 연도의 모든 레코드를 포함하며, 매칭되지 않는 부분은 `NaN`으로 채워집니다.

### 2. Semijoin (세미 조인)

**핵심 개념:**
Semijoin ($R \ltimes S$)은 두 테이블 R과 S를 조인하되, **테이블 R의 레코드 중 테이블 S에 매칭되는 것이 있는 레코드만 반환**합니다. 결과에는 **테이블 R의 컬럼만 포함**되며, S의 컬럼은 포함되지 않습니다. 이는 R을 S의 매칭 조건을 기반으로 필터링하는 것과 같습니다.

**구체적인 실생활 예시:**
당신이 쇼핑몰 운영자이고, **전체 상품 목록**(`all_products` 테이블)과 **현재 재고가 있는 상품 목록**(`in_stock` 테이블)을 가지고 있다고 가정해 봅시다.

*   `all_products` 테이블: (상품ID, 상품명, 가격) - `[(P001, '노트북', 120만원), (P002, '스마트폰', 80만원), (P003, '태블릿', 50만원), (P004, '헤드셋', 10만원)]`
*   `in_stock` 테이블: (상품ID, 재고수량) - `[(P001, 10), (P003, 5)]`

`상품ID`를 기준으로 `all_products`와 `in_stock`을 Semijoin 하면:
*   `all_products`에서 `in_stock`에 `상품ID`가 존재하는 상품들만 필터링됩니다.
*   결과로 `[(P001, '노트북', 120만원), (P003, '태블릿', 50만원)]` 이 반환됩니다. `in_stock` 테이블의 `재고수량` 컬럼은 결과에 포함되지 않습니다.

**목적:** 한 테이블의 데이터를 다른 테이블의 조건을 기준으로 필터링하되, 필터링 기준이 된 다른 테이블의 정보는 결과에 필요 없을 때 사용합니다. 예를 들어, "주문 이력이 있는 고객 목록"을 얻고 싶지만, 주문의 상세 내용은 필요 없을 때 유용합니다.

**Pandas 코드:**
```python
keys = pd.DataFrame({"Name":["Mary","Alice"]})
semi = babynames[babynames["Name"].isin(keys["Name"])]
```
`babynames` 데이터프레임에서 `Name` 컬럼의 값이 `keys` 데이터프레임의 `Name` 컬럼에 존재하는 레코드만 필터링하여 반환합니다. 결과는 `babynames`의 모든 컬럼을 포함하며, `keys`의 정보는 추가되지 않습니다.

### 3. Antijoin (안티 조인)

**핵심 개념:**
Antijoin ($R \setminus (R \ltimes S)$)은 Semijoin의 반대 개념입니다. 테이블 R의 레코드 중 **테이블 S에 매칭되는 것이 없는 레코드만 반환**합니다. 결과에는 Semijoin과 마찬가지로 **테이블 R의 컬럼만 포함**됩니다.

**구체적인 실생활 예시:**
다시 쇼핑몰 예시로 돌아가서, **전체 상품 목록**(`all_products` 테이블)과 **현재 재고가 있는 상품 목록**(`in_stock` 테이블)을 사용합니다.

*   `all_products` 테이블: (상품ID, 상품명, 가격) - `[(P001, '노트북', 120만원), (P002, '스마트폰', 80만원), (P003, '태블릿', 50만원), (P004, '헤드셋', 10만원)]`
*   `in_stock` 테이블: (상품ID, 재고수량) - `[(P001, 10), (P003, 5)]`

`상품ID`를 기준으로 `all_products`에서 `in_stock`을 Antijoin 하면:
*   `all_products`에서 `in_stock`에 `상품ID`가 존재하지 않는 상품들만 필터링됩니다.
*   결과로 `[(P002, '스마트폰', 80만원), (P004, '헤드셋', 10만원)]` 이 반환됩니다. 이는 현재 재고가 없는 상품 목록입니다.

**목적:** 한 테이블의 데이터 중 다른 테이블에는 없는 데이터를 찾을 때 사용합니다. 예를 들어, "주문 이력이 없는 고객 목록", "아직 이수하지 않은 과목 목록" 등을 찾을 때 유용합니다.

**Pandas 코드:**
```python
anti = (babynames.merge(keys, on="Name", how="left", indicator=True)
        .query("_merge=='left_only'")
        .drop(columns=["_merge"]))
```
이 코드는 Pandas에서 Antijoin을 구현하는 일반적인 방식입니다.
1.  `babynames.merge(keys, on="Name", how="left", indicator=True)`: `babynames`를 기준으로 `keys`와 `Name` 컬럼을 이용해 Left Join을 수행합니다. `indicator=True` 옵션은 `_merge`라는 특수 컬럼을 생성하여 각 레코드가 어느 테이블에 존재했는지(`left_only`, `right_only`, `both`)를 표시합니다.
2.  `.query("_merge=='left_only'")`: 생성된 `_merge` 컬럼에서 값이 `'left_only'`인 레코드만 필터링합니다. 이는 `babynames`에는 존재하지만 `keys`에는 매칭되는 레코드가 없는 경우를 의미합니다.
3.  `.drop(columns=["_merge"])`: 임시로 생성된 `_merge` 컬럼을 제거하여 최종적으로 `babynames`의 컬럼만 남깁니다.

---

이 세 가지 연산은 데이터 처리 및 분석에서 특정 조건을 가진 데이터 집합을 효율적으로 추출하는 데 필수적인 도구입니다. 각 연산의 목적과 반환하는 데이터의 형태를 명확히 이해하시면 실제 프로젝트에서 데이터를 훨씬 유연하게 다룰 수 있을 겁니다.

---

## Slide 20

## 데이터 그룹핑 및 집계 (Grouping/Aggregation)

데이터 그룹핑 및 집계는 방대한 데이터를 특정 기준(그룹)으로 나누고, 각 그룹별로 요약 통계(집계)를 계산하여 데이터의 패턴이나 특성을 파악하는 강력한 방법입니다. 마치 설문조사 결과를 성별이나 연령대별로 나눠서 분석하는 것과 같다고 볼 수 있습니다.

### 1. 핵심 개념: 그룹 나누기와 집계 계산

*   **그룹 속성 (G)**: 데이터를 나누는 기준이 되는 컬럼(들)입니다. 슬라이드에서는 `Sex`와 `decade`를 기준으로 사용합니다. 예를 들어, '남성 1980년대', '여성 1990년대' 등과 같이 그룹이 생성됩니다.
*   **집계 함수 (f)**: 각 그룹별로 수행할 계산(요약 통계)입니다. 슬라이드에서는 `Count` 컬럼에 대해 `평균(mean)`, `최댓값(max)`, `합계(sum)`를 계산합니다. 이는 각 그룹 내의 `Count` 데이터들을 대상으로 하는 연산입니다.

**예시: 온라인 쇼핑몰 판매 데이터 분석**

당신이 온라인 의류 쇼핑몰의 데이터 분석가라고 가정해 봅시다. 당신은 `orders`라는 데이터프레임에 각 주문에 대한 정보(예: `Category` (상의, 하의, 신발 등), `Region` (서울, 경기 등), `Price` (판매 금액), `Quantity` (판매 수량))를 가지고 있습니다.

여기서 "각 지역별로 카테고리별 총 판매 금액과 평균 판매 수량을 알고 싶다"는 목표가 있다고 해봅시다.

*   **그룹 속성 (G)**: `Region`, `Category`
*   **집계 함수 (f)**: `Price` 컬럼에 대한 `합계(sum)`, `Quantity` 컬럼에 대한 `평균(mean)`

이를 통해 서울 지역의 '상의' 총 판매 금액, 평균 판매 수량, 경기 지역의 '하의' 총 판매 금액, 평균 판매 수량 등을 각각 얻을 수 있습니다.

### 2. Pandas에서의 구현 (`groupby()` 및 `agg()`)

슬라이드의 Pandas 코드는 다음과 같은 과정을 거칩니다.

1.  **새로운 컬럼 생성 (`decade`)**:
    ```python
    babynames["decade"] = (babynames["Year"] // 10) * 10
    ```
    `babynames` 데이터프레임에 `Year` 컬럼이 있다면, 이를 10으로 나눈 몫에 다시 10을 곱하여 `decade` (1980년대, 1990년대 등) 컬럼을 만듭니다. 이는 기존 데이터를 기반으로 새로운 그룹핑 기준을 만드는 과정입니다.

2.  **그룹핑 및 집계**:
    ```python
    stats = (babynames.groupby(["Sex", "decade"])["Count"]
                     .agg(mean="mean", max="max", total="sum")
                     .reset_index())
    ```
    *   `babynames.groupby(["Sex", "decade"])`: `babynames` 데이터프레임을 `Sex`와 `decade` 두 컬럼을 기준으로 그룹핑합니다. 이제 데이터는 '남성 1980', '여성 1990' 등의 그룹으로 나뉘게 됩니다.
    *   `["Count"]`: 각 그룹 내에서 `Count` 컬럼의 값들을 대상으로 집계 연산을 수행하겠다는 의미입니다.
    *   `.agg(mean="mean", max="max", total="sum")`: `Count` 컬럼에 대해 여러 집계 함수를 동시에 적용합니다.
        *   `mean="mean"`: `Count`의 평균을 계산하고, 결과 컬럼의 이름을 `mean`으로 지정합니다.
        *   `max="max"`: `Count`의 최댓값을 계산하고, 결과 컬럼의 이름을 `max`로 지정합니다.
        *   `total="sum"`: `Count`의 합계를 계산하고, 결과 컬럼의 이름을 `total`으로 지정합니다.

**온라인 쇼핑몰 예시 코드:**

```python
import pandas as pd

# 예시 데이터 생성
data = {
    'OrderID': range(1, 11),
    'Category': ['상의', '하의', '신발', '상의', '하의', '신발', '상의', '하의', '신발', '상의'],
    'Region': ['서울', '경기', '서울', '경기', '서울', '경기', '서울', '경기', '서울', '경기'],
    'Price': [50000, 30000, 70000, 60000, 40000, 80000, 55000, 35000, 75000, 65000],
    'Quantity': [2, 1, 1, 3, 2, 1, 2, 1, 1, 3]
}
orders = pd.DataFrame(data)

print("원본 orders 데이터프레임:")
print(orders)
print("-" * 30)

# 지역별, 카테고리별 판매 분석
sales_stats = orders.groupby(["Region", "Category"]).agg(
    total_price=("Price", "sum"),      # 각 그룹의 Price 합계 (컬럼명 total_price)
    avg_quantity=("Quantity", "mean")  # 각 그룹의 Quantity 평균 (컬럼명 avg_quantity)
)
print("그룹핑 및 집계 결과 (reset_index() 적용 전):")
print(sales_stats)
print("-" * 30)

# reset_index() 적용 후
sales_stats_reset = sales_stats.reset_index()
print("그룹핑 및 집계 결과 (reset_index() 적용 후):")
print(sales_stats_reset)
```

**코드 실행 결과:**

```
원본 orders 데이터프레임:
   OrderID Category Region  Price  Quantity
0        1       상의     서울  50000         2
1        2       하의     경기  30000         1
2        3       신발     서울  70000         1
3        4       상의     경기  60000         3
4        5       하의     서울  40000         2
5        6       신발     경기  80000         1
6        7       상의     서울  55000         2
7        8       하의     경기  35000         1
8        9       신발     서울  75000         1
9       10       상의     경기  65000         3
------------------------------
그룹핑 및 집계 결과 (reset_index() 적용 전):
                     total_price  avg_quantity
Region Category                             
경기     신발                  80000           1.0
       상의                 125000           3.0
       하의                  65000           1.0
서울     신발                 145000           1.0
       상의                 105000           2.0
       하의                  40000           2.0
------------------------------
그룹핑 및 집계 결과 (reset_index() 적용 후):
  Region Category  total_price  avg_quantity
0     경기       신발        80000           1.0
1     경기       상의       125000           3.0
2     경기       하의        65000           1.0
3     서울       신발       145000           1.0
4     서울       상의       105000           2.0
5     서울       하의        40000           2.0
```

### 3. `reset_index()`를 사용하는 이유

`reset_index()`는 `groupby()` 이후의 결과물을 다루기 훨씬 편리하게 만들어주는 필수적인 메서드입니다.

*   **그룹 키(컬럼)를 일반 컬럼으로 전환**: `groupby()`를 수행하면 기본적으로 그룹을 나누는 기준이 되었던 컬럼들(`Sex`, `decade` 또는 `Region`, `Category`)이 결과 데이터프레임의 **인덱스(MultiIndex)**가 됩니다. 위 예시의 `reset_index()` 적용 전 결과를 보면 `Region`과 `Category`가 일반적인 데이터 컬럼이 아닌, 옆으로 튀어나와 있는 인덱스처럼 보입니다. `reset_index()`는 이 인덱스를 다시 일반 컬럼으로 되돌려 놓습니다.
    *   **실생활 예시**: 회사에서 부서별 직원 평균 급여를 계산했다고 가정해 봅시다. `groupby('부서명')`을 하면 '부서명'이 결과 테이블의 행 인덱스가 됩니다. 이 테이블을 다른 팀에 전달하거나 보고서에 포함할 때, '부서명'이 일반 컬럼으로 존재해야 보기에도 좋고 다루기도 쉽겠죠? `reset_index()`는 이 '부서명'을 다시 평범한 컬럼으로 만들어 줍니다.

*   **병합(merge/join) 작업 용이성**: 많은 데이터프레임 병합 작업은 특정 '키' 컬럼을 기반으로 이루어집니다. `reset_index()`를 통해 그룹 키가 일반 컬럼으로 존재하면, `merge(on=["Region", "Category"])`와 같이 명확하게 키 컬럼을 지정하여 다른 데이터프레임과 쉽게 병합할 수 있습니다. 인덱스로 남아있을 경우, 병합 옵션을 더 복잡하게 설정해야 할 수 있습니다 (예: `right_index=True`).
    *   **실생활 예시**: 위에서 만든 `sales_stats_reset` 데이터에 각 카테고리별 마진율 정보가 있는 `category_margin` 데이터프레임을 합치고 싶다고 해봅시다. `sales_stats_reset`에 `Category` 컬럼이 명확하게 존재해야 `orders_stats_reset.merge(category_margin, on="Category")` 와 같이 깔끔하게 병합할 수 있습니다. 인덱스로 남아있다면 `Category`를 직접 `on`에 지정하기 어렵겠죠.

결론적으로, `reset_index()`는 `groupby()`의 결과를 더 직관적이고 활용하기 쉬운 형태로 만들어 주기 때문에, 대부분의 경우 집계 작업 후에 함께 사용되는 중요한 단계입니다.

---

## Slide 21

`pandas GroupBy`는 데이터 분석에서 매우 강력한 도구이며, 핵심적으로는 데이터를 **논리적으로 분할하고 각 그룹에 대한 하위 데이터(sub-DataFrame 또는 sub-Series)를 매핑하는 방식**으로 작동합니다.

### 핵심 개념

1.  **`GroupBy`는 '키'를 '하위 DataFrame/Series'에 매핑합니다.**
    *   `DataFrameGroupBy` 객체는 원본 DataFrame을 지정된 '그룹 키' 기준으로 여러 개의 하위 DataFrame으로 **분할(partitioning)**한 것을 나타냅니다. 각 그룹 키는 해당 그룹에 속하는 모든 행을 포함하는 논리적인 하위 DataFrame에 연결(매핑)됩니다.
    *   `SeriesGroupBy`도 마찬가지로 그룹 키를 해당 하위 Series에 매핑합니다.
    *   **예시:** 당신이 대형 온라인 쇼핑몰의 데이터 분석가라고 가정해 봅시다. 당신은 여러 상품(`product`)이 다양한 지점(`store`)에서 판매된 데이터를 가지고 있습니다.
        ```python
        import pandas as pd

        data = {
            'store': ['강남점', '강남점', '홍대점', '강남점', '홍대점', '종로점'],
            'product': ['노트북', '마우스', '키보드', '모니터', '노트북', '마우스'],
            'quantity': [2, 1, 3, 2, 5, 1],
            'price_per_unit': [100, 20, 50, 150, 100, 20]
        }
        df = pd.DataFrame(data)

        # store를 기준으로 그룹화
        store_groups = df.groupby('store')
        ```
        여기서 `store_groups`는 `강남점`이라는 키를 강남점의 모든 판매 데이터(노트북, 마우스, 모니터)에 대한 하위 DataFrame에 매핑하고, `홍대점` 키를 홍대점 판매 데이터에 매핑하는 식입니다.

2.  **'게으른(Lazy)', '뷰(View-like)' 처리 방식입니다 (복사본 생성 안 함).**
    *   `groupby()`를 호출하는 순간 실제 데이터의 복사본이 만들어지거나 별도의 하위 DataFrame들이 생성되는 것이 아닙니다. 대신, 어떤 그룹에 어떤 행들이 속하는지에 대한 '메타데이터' 또는 '설명서'만 만들어집니다.
    *   **예시:** 위 예시에서 `store_groups = df.groupby('store')`를 실행해도, Pandas는 즉시 '강남점', '홍대점', '종로점'에 해당하는 데이터를 각각 복사하여 3개의 별도 DataFrame을 만들지 않습니다. 대신, "강남점 데이터는 원본 DataFrame의 0, 1, 3번 행에 있고, 홍대점 데이터는 2, 4번 행에 있다"는 정보를 내부적으로 기억하고 있습니다. 이는 마치 어떤 영화가 어떤 배우들을 포함하고 있는지의 '목록'만 가지고 있고, 실제로 영화를 볼 때만 해당 배우들의 연기를 '보는' 것과 같습니다.

3.  **데이터의 '구체화(Materialization)'는 접근 시점에 이루어집니다.**
    *   실제로 그룹별 데이터를 사용하거나 집계(aggregation) 연산을 수행할 때 비로소 해당 그룹의 하위 DataFrame/Series가 생성되고 필요한 연산이 이루어집니다.
    *   **예시:** 각 지점의 총 판매 수량을 알고 싶어서 `store_groups['quantity'].sum()`을 호출할 때, Pandas는 비로소 '강남점'에 해당하는 행들만 모아와서 `quantity` 컬럼의 값을 합산하고, '홍대점'에 대해서도 같은 작업을 수행합니다. 이처럼 필요한 시점에만 데이터를 처리하므로 효율적입니다.

### 탐색 API (매핑 확인 및 활용)

`GroupBy` 객체는 단순히 데이터를 묶는 것을 넘어, 각 그룹에 접근하고 다양한 작업을 수행할 수 있는 편리한 API를 제공합니다.

1.  **`for key, subdf in g:` (그룹 반복 순회):**
    *   `GroupBy` 객체를 반복문으로 순회하여 각 그룹의 키(key)와 해당 그룹의 하위 DataFrame(subdf) 또는 Series(subseries)를 얻을 수 있습니다. 이때 `subdf`가 그때그때 구체화됩니다.
    *   **예시:** 각 지점별로 어떤 상품들이 판매되었는지 확인하고 싶을 때:
        ```python
        for store_name, store_df in store_groups:
            print(f"\n--- {store_name} ---")
            print(f"판매된 상품: {store_df['product'].unique()}")
            print(f"총 판매 수량: {store_df['quantity'].sum()}")
        ```
        이 코드는 '강남점'의 `store_df`를 구체화하여 출력하고, 그 다음 '홍대점', '종로점'에 대해 같은 작업을 반복합니다.

2.  **`g.get_group(key)` (특정 그룹 직접 접근):**
    *   특정 그룹 키에 해당하는 하위 DataFrame/Series를 직접 가져올 수 있습니다.
    *   **예시:** '홍대점'의 판매 데이터만 따로 자세히 분석하고 싶을 때:
        ```python
        hongdae_sales = store_groups.get_group('홍대점')
        print("\n--- 홍대점의 판매 데이터 ---")
        print(hongdae_sales)
        ```
        이렇게 하면 '홍대점' 그룹에 해당하는 데이터만 즉시 하나의 DataFrame으로 반환됩니다.

### 실용적인 활용 (매핑을 통한 결과 계산)

`GroupBy` 객체는 `apply()`, `transform()`, `agg()`와 같은 메서드를 통해 각 그룹에 대한 복잡한 연산을 효율적으로 수행할 수 있게 합니다.

1.  **`apply()` (그룹별 복합 연산):**
    *   각 하위 DataFrame/Series에 사용자가 정의한 복잡한 함수를 적용하고 그 결과를 결합합니다. 결과는 각 그룹을 하나의 값으로 축소하거나, 새로운 DataFrame 또는 Series를 반환할 수 있습니다.
    *   **예시:** 각 지점별로 총 수익(`quantity * price_per_unit`)을 계산하고 싶을 때:
        ```python
        store_revenue = store_groups.apply(lambda df_group: (df_group['quantity'] * df_group['price_per_unit']).sum())
        print("\n--- 지점별 총 수익 (apply) ---")
        print(store_revenue)
        ```
        `apply`는 각 지점의 `df_group`에 대해 수익을 계산하고 합산하여, 지점별 총 수익을 담은 Series를 반환합니다.

2.  **`transform()` (원본 DataFrame의 모양 유지):**
    *   각 그룹 내에서 계산된 값을 원본 DataFrame의 인덱스에 맞춰 다시 정렬하여 반환합니다. 결과 Series/DataFrame의 길이는 원본과 동일하게 유지됩니다. 이는 그룹 내에서의 비율, 순위 등을 계산하여 원본 데이터에 추가할 때 유용합니다.
    *   **예시:** 각 상품 판매가 해당 'store' 내 전체 판매 수량에서 차지하는 '비율'을 계산하여 원본 DataFrame에 추가하고 싶을 때:
        ```python
        df['share_in_store_quantity'] = df.groupby('store')['quantity'].transform(lambda x: x / x.sum())
        print("\n--- 지점 내 판매 수량 비율 (transform) ---")
        print(df)
        ```
        `transform`은 각 지점 그룹(`x`)에 대해 총 판매 수량(`x.sum()`)을 계산하고, 그 값으로 각 행의 `quantity`를 나누어 원본 DataFrame의 각 행에 해당하는 위치에 결과를 반환합니다. 이는 각 판매 건이 속한 지점 내에서 얼마나 비중을 차지하는지 알려줍니다.

이처럼 `pandas GroupBy`는 데이터를 유연하게 분할하고, 필요할 때만 연산을 수행하며, 다양한 방식으로 그룹별 분석을 가능하게 하는 강력한 도구입니다.

---

## Slide 22

## Pandas `groupby` 핵심 개념 및 실생활 예시

첨부된 슬라이드는 Pandas DataFrame에서 `groupby` 연산을 통해 데이터를 집계(aggregation)하고, 그 결과로 생성되는 인덱스를 다루는 방법을 설명합니다.

### 핵심 개념

1.  **데이터 그룹화 (`groupby`)**: 특정 열(column)의 고유한 값들을 기준으로 DataFrame의 행들을 여러 그룹으로 나눕니다. 마치 여러 종류의 과일을 바구니에 담는 것과 같습니다. 각 과일 종류가 하나의 그룹이 되는 거죠.
2.  **그룹별 집계 (`.sum()`)**: 그룹화된 각 그룹에 대해 통계 연산(예: 합계, 평균, 개수 등)을 수행합니다. 슬라이드에서는 `.sum()`을 사용하여 각 그룹의 `quantity`를 합산합니다.
3.  **인덱스 처리**: `groupby` 연산 후 결과 DataFrame의 인덱스가 어떻게 되는지를 이해하는 것이 중요합니다.
    *   **기본 동작**: `groupby`에 사용된 열(예: `'product'`)이 결과 DataFrame의 새로운 인덱스가 됩니다.
    *   **`.reset_index()`**: 인덱스로 설정된 열을 다시 일반적인 데이터 열로 되돌리고, 새로운 기본 숫자 인덱스(0부터 시작)를 생성합니다.
    *   **`as_index=False`**: `groupby` 연산을 수행할 때 처음부터 그룹화 기준이 되는 열을 인덱스로 만들지 않고, 일반적인 데이터 열로 유지하며 새로운 기본 숫자 인덱스를 생성하도록 지정합니다. 이는 `.reset_index()`를 나중에 호출하는 것과 동일한 최종 결과를 한 번에 얻을 수 있는 방법입니다.
4.  **숫자형 열만 집계**: `sum()`과 같은 집계 함수는 기본적으로 숫자형 데이터가 있는 열에만 적용됩니다. 숫자형이 아닌 열은 결과에서 제외되거나, 명시적으로 선택하지 않으면 무시됩니다.

---

### 실생활 예시: 온라인 쇼핑몰 판매 데이터 분석

당신이 작은 온라인 쇼핑몰을 운영하고 있다고 가정해 봅시다. 매일 다음과 같은 주문 데이터(DataFrame `df_sales`)가 쌓입니다.

```
df_sales
| order_id | product_category | item_name  | price | quantity |
|----------|------------------|------------|-------|----------|
| 1001     | Electronics      | Laptop     | 1200  | 1        |
| 1002     | Books            | Novel      | 20    | 2        |
| 1003     | Electronics      | Mouse      | 30    | 1        |
| 1004     | Books            | Textbook   | 50    | 1        |
| 1005     | Electronics      | Keyboard   | 80    | 1        |
| 1006     | Books            | Comic Book | 15    | 3        |
```

당신은 오늘 어떤 카테고리의 상품이 총 몇 개 판매되었는지 궁금합니다.

#### 1. 기본 그룹화 및 합계 (Default Index)

가장 먼저 떠올릴 수 있는 방법은 `product_category`별로 그룹을 나누고 각 그룹의 `quantity`를 합산하는 것입니다.

```python
category_sales = df_sales.groupby('product_category').sum()
print(category_sales)
```

**결과:**
```
                    order_id  price  quantity
product_category                             
Books                   3023     85         6
Electronics             3089   1310         3
```

**설명:**
*   `product_category` 열의 고유 값('Books', 'Electronics')을 기준으로 데이터가 두 개의 그룹으로 나뉩니다.
*   각 그룹 내에서 `quantity` (및 다른 숫자 열인 `order_id`, `price`)가 합산됩니다.
*   **여기서 중요한 점은 `product_category`가 결과 DataFrame의 새로운 인덱스(Index)가 되었다는 것입니다.** 슬라이드의 첫 번째 `groupby().sum()` 결과와 동일합니다.
*   `order_id`나 `price`의 합계는 이 분석에서는 의미가 없을 수 있습니다. `groupby()`는 기본적으로 모든 숫자형 열에 `sum()`을 적용하기 때문입니다. 특정 열만 합계하고 싶다면 `df_sales.groupby('product_category')['quantity'].sum()`처럼 명시적으로 열을 선택해야 합니다.

#### 2. 인덱스를 일반 열로 되돌리기 (`.reset_index()`)

만약 `product_category`를 인덱스가 아닌 일반적인 데이터 열로 사용하고 싶다면, `reset_index()` 메서드를 사용합니다.

```python
category_sales_reset = df_sales.groupby('product_category').sum().reset_index()
print(category_sales_reset)
```

**결과:**
```
  product_category  order_id  price  quantity
0            Books      3023     85         6
1      Electronics      3089   1310         3
```

**설명:**
*   `product_category`가 인덱스에서 다시 일반 열로 돌아왔고, 새로운 기본 숫자 인덱스(0, 1)가 자동으로 생성되었습니다.
*   이 결과는 데이터베이스에서 쿼리한 테이블과 유사하여, 다른 데이터와 병합하거나 시각화할 때 편리할 수 있습니다. 슬라이드의 `.reset_index()` 이후 결과와 동일합니다.

#### 3. 처음부터 인덱스 생성을 방지 (`as_index=False`)

`groupby` 연산을 할 때부터 `product_category`를 인덱스로 만들고 싶지 않다면, `groupby` 메서드에 `as_index=False` 옵션을 추가할 수 있습니다.

```python
category_sales_no_index = df_sales.groupby('product_category', as_index=False).sum()
print(category_sales_no_index)
```

**결과:**
```
  product_category  order_id  price  quantity
0            Books      3023     85         6
1      Electronics      3089   1310         3
```

**설명:**
*   `product_category`는 처음부터 일반 데이터 열로 유지되고, 기본 숫자 인덱스(0, 1)가 자동으로 생성됩니다.
*   이 방식은 `.reset_index()`를 나중에 호출하는 것과 동일한 결과를 주지만, 코드를 더 간결하게 만들 수 있습니다. 슬라이드의 `as_index=False` 옵션 사용 결과와 동일합니다.

이 예시를 통해 `groupby`의 동작 방식과 인덱스 처리의 중요성을 완벽하게 이해하셨기를 바랍니다!

---

## Slide 23

첨부된 슬라이드는 Pandas의 `groupby()` 함수를 사용하여 데이터를 그룹화한 후, 어떤 컬럼들을 집계(aggregation)할지 선택하는 세 가지 주요 방법을 보여줍니다. 각 방법의 핵심 개념과 구체적인 예시는 다음과 같습니다.

---

### 핵심 개념: Pandas `groupby()` 후 컬럼 선택 및 집계

`groupby()`는 특정 컬럼의 고유 값들을 기준으로 데이터를 그룹으로 나눈 후, 각 그룹에 대해 통계 함수(예: `sum()`, `mean()`, `count()`)를 적용할 때 사용합니다. 이때 어떤 컬럼에 통계 함수를 적용할지에 따라 다른 구문을 사용하게 됩니다.

실생활 예시를 위해 가상의 **온라인 서점 판매 데이터**를 사용해 보겠습니다.
`books_sales`라는 DataFrame은 고객들이 구매한 도서 정보를 담고 있습니다.

| customer | category  | quantity | rating | total_price |
|:---------|:----------|:---------|:-------|:------------|
| Alice    | 소설      | 2        | 8      | 20000       |
| Bob      | 비문학    | 1        | 7      | 15000       |
| Charlie  | 소설      | 3        | 9      | 30000       |
| Alice    | 비문학    | 1        | 6      | 12000       |

-   `customer`: 구매 고객 이름
-   `category`: 도서 카테고리 (예: 소설, 비문학, 만화)
-   `quantity`: 구매 수량
-   `rating`: 고객이 도서에 매긴 점수 (가상의 숫자 데이터)
-   `total_price`: 해당 도서 구매로 발생한 총 매출액

---

#### 1. 모든 숫자형 컬럼 집계하기

-   **구문:** `df.groupby('그룹화_기준_컬럼').sum()`
-   **개념:** `groupby()`를 수행한 후, 명시적으로 컬럼을 선택하지 않고 바로 `.sum()`과 같은 집계 함수를 호출하면, 그룹 내의 **모든 숫자형(numeric) 컬럼**에 대해 집계 함수를 적용합니다. 결과는 DataFrame 형태로 반환됩니다.
-   **예시:** "우리 서점에서 각 **도서 카테고리**별로 총 몇 권이 팔렸고, 고객들이 매긴 총점은 얼마이며, 총 매출은 얼마인지 알고 싶어요."
    ```python
    books_sales.groupby('category').sum()
    ```
    **결과 예측:**
    | category | quantity | rating | total_price |
    |:---------|:---------|:-------|:------------|
    | 비문학   | 2        | 13     | 27000       |
    | 소설     | 5        | 17     | 50000       |
    
    *   '비문학' 카테고리: `quantity` (1+1=2), `rating` (7+6=13), `total_price` (15000+12000=27000)
    *   '소설' 카테고리: `quantity` (2+3=5), `rating` (8+9=17), `total_price` (20000+30000=50000)

---

#### 2. 특정 단일 컬럼만 집계하기 (Attribute Access)

-   **구문:** `df.groupby('그룹화_기준_컬럼').선택_컬럼_이름.sum()`
-   **개념:** `groupby()`를 수행한 후, 점(`.`)을 사용하여 **특정 단일 컬럼**에만 접근하여 집계 함수를 적용합니다. 결과는 Pandas Series 형태로 반환됩니다. 이는 하나의 특정 지표에만 관심이 있을 때 유용합니다.
-   **예시:** "각 **도서 카테고리**별로 총 '판매 수량'만 알고 싶어요."
    ```python
    books_sales.groupby('category').quantity.sum()
    ```
    **결과 예측:**
    ```
    category
    비문학    2
    소설      5
    Name: quantity, dtype: int64
    ```
    **설명:** '비문학' 카테고리는 총 2권, '소설' 카테고리는 총 5권이 팔렸다는 것을 Series 형태로 보여줍니다.

---

#### 3. 특정 여러 컬럼만 집계하기 (List of Columns Selection)

-   **구문:** `df.groupby('그룹화_기준_컬럼')[['선택_컬럼1', '선택_컬럼2']].sum()`
-   **개념:** `groupby()`를 수행한 후, 대괄호 `[]` 안에 **컬럼 이름들을 리스트 형태로** 넣어 여러 특정 컬럼을 선택하고 집계 함수를 적용합니다. 결과는 DataFrame 형태로 반환됩니다.
-   **예시:** "각 **도서 카테고리**별로 '판매 수량'과 '총 매출액'만 알고 싶어요."
    ```python
    books_sales.groupby('category')[['quantity', 'total_price']].sum()
    ```
    **결과 예측:**
    | category | quantity | total_price |
    |:---------|:---------|:------------|
    | 비문학    | 2        | 27000       |
    | 소설     | 5        | 50000       |
    
    **설명:** '비문학' 카테고리의 총 판매 수량과 총 매출액, 그리고 '소설' 카테고리의 총 판매 수량과 총 매출액을 DataFrame 형태로 보여줍니다.

---

이 세 가지 방법은 `groupby()`를 통해 원하는 정보를 정확하게 추출하고 분석하는 데 필수적인 기술입니다. 데이터의 목적과 필요한 결과 형태에 따라 적절한 방법을 선택하여 사용하면 됩니다.

---

## Slide 24

첨부된 슬라이드의 핵심 개념은 Pandas의 `groupby()`와 `agg()` 메서드를 활용하여 데이터를 그룹화하고, 각 그룹 내에서 특정 열에 대해 여러 가지 통계적 집계(aggregation) 함수를 동시에 적용하는 방법입니다. 특히, 이 방법은 어떤 열에 어떤 집계 함수를 적용할지 명시적으로 지정하여 "이름 있는 집계(Named Aggregations)"를 수행할 수 있게 해줍니다.

---

### 핵심 개념: Pandas `groupby().agg()`를 이용한 이름 있는 집계

슬라이드에서 제시된 `df.groupby('product').agg({'quantity': 'sum', 'price': 'mean'})` 코드는 다음 두 가지 중요한 단계를 통해 데이터를 요약합니다.

1.  **데이터 그룹화 (`groupby()`):**
    `df.groupby('product')`는 원본 데이터프레임 `df`를 'product' 열의 고유한 값(예: 'bananas', 'oranges')을 기준으로 여러 개의 하위 그룹으로 나눕니다. 각 그룹은 동일한 'product'를 가진 모든 행을 포함하게 됩니다.

2.  **그룹별 집계 (`agg()`):**
    `agg()` 메서드는 그룹화된 각 하위 그룹에 대해 하나 이상의 집계 함수를 적용합니다. 이때 딕셔너리(`{ '컬럼명': '집계함수' }`) 형태로 어떤 컬럼에 어떤 집계 함수를 적용할지 명시적으로 지정할 수 있습니다.
    *   `'quantity': 'sum'`: 각 그룹에서 'quantity' 열의 모든 값을 합산합니다.
    *   `'price': 'mean'`: 각 그룹에서 'price' 열의 모든 값의 평균을 계산합니다.

이렇게 하면 'product'별로 'quantity'의 총합과 'price'의 평균을 동시에 얻을 수 있으며, 결과 데이터프레임의 컬럼 이름은 원본 컬럼 이름을 유지하여 의미를 쉽게 파악할 수 있습니다.

---

### 구체적이고 실생활에 가까운 예시: 온라인 의류 쇼핑몰 판매 분석

당신이 한 온라인 의류 쇼핑몰의 데이터 분석가라고 가정해 봅시다. 매일 수많은 고객이 다양한 카테고리(예: '상의', '하의', '액세서리')의 옷을 구매하고 리뷰를 남깁니다. 당신은 주간 판매 데이터를 분석하여 각 카테고리의 판매 현황과 고객 만족도를 파악하려고 합니다.

**원본 데이터 (`sales_df`):**

| order_id | category | item_name | quantity_sold | unit_price | customer_rating |
| :------- | :------- | :-------- | :------------ | :--------- | :-------------- |
| 101      | 상의     | 티셔츠    | 2             | 15000      | 4.5             |
| 102      | 하의     | 청바지    | 1             | 35000      | 3.8             |
| 103      | 상의     | 스웨터    | 1             | 25000      | 4.9             |
| 104      | 액세서리 | 목걸이    | 1             | 10000      | 4.2             |
| 105      | 상의     | 티셔츠    | 3             | 15000      | 4.1             |
| 106      | 하의     | 치마      | 1             | 28000      | 4.0             |

**분석 목표:**
*   각 의류 **카테고리(`category`)**별로 **총 판매된 수량(`quantity_sold`)**이 얼마인지 알고 싶습니다.
*   각 카테고리별 **고객 평균 만족도(`customer_rating`)**가 어떻게 되는지 알고 싶습니다.

**Pandas 코드 적용:**

```python
import pandas as pd

# 예시 데이터프레임 생성
data = {
    'order_id': [101, 102, 103, 104, 105, 106],
    'category': ['상의', '하의', '상의', '액세서리', '상의', '하의'],
    'item_name': ['티셔츠', '청바지', '스웨터', '목걸이', '티셔츠', '치마'],
    'quantity_sold': [2, 1, 1, 1, 3, 1],
    'unit_price': [15000, 35000, 25000, 10000, 15000, 28000],
    'customer_rating': [4.5, 3.8, 4.9, 4.2, 4.1, 4.0]
}
sales_df = pd.DataFrame(data)

# 'category'를 기준으로 그룹화하고, 'quantity_sold'는 합계, 'customer_rating'은 평균을 계산
category_summary = sales_df.groupby('category').agg({
    'quantity_sold': 'sum',
    'customer_rating': 'mean'
})

print(category_summary)
```

**결과 (`category_summary`):**

| category | quantity_sold | customer_rating |
| :------- | :------------ | :-------------- |
| 상의     | 6             | 4.5             |
| 액세서리 | 1             | 4.2             |
| 하의     | 2             | 3.9             |

**설명:**

1.  **`sales_df.groupby('category')`**: 이 부분이 데이터프레임을 '상의', '하의', '액세서리' 세 가지 그룹으로 나눕니다.
    *   '상의' 그룹: order_id 101, 103, 105
    *   '하의' 그룹: order_id 102, 106
    *   '액세서리' 그룹: order_id 104

2.  **`.agg({'quantity_sold': 'sum', 'customer_rating': 'mean'})`**:
    *   **'상의' 그룹:**
        *   `quantity_sold`의 합계: 2 (티셔츠) + 1 (스웨터) + 3 (티셔츠) = 6
        *   `customer_rating`의 평균: (4.5 + 4.9 + 4.1) / 3 = 4.5
    *   **'액세서리' 그룹:**
        *   `quantity_sold`의 합계: 1 (목걸이) = 1
        *   `customer_rating`의 평균: 4.2 / 1 = 4.2
    *   **'하의' 그룹:**
        *   `quantity_sold`의 합계: 1 (청바지) + 1 (치마) = 2
        *   `customer_rating`의 평균: (3.8 + 4.0) / 2 = 3.9

이 예시처럼, `groupby().agg()`를 사용하면 복잡한 데이터에서 특정 기준에 따라 필요한 정보를 여러 가지 방식으로 동시에 요약하고 추출할 수 있습니다. 각 집계 결과가 원본 컬럼 이름을 유지하므로, 'quantity_sold'는 총 판매 수량을, 'customer_rating'은 평균 고객 만족도를 직관적으로 보여주어 데이터 분석에 매우 유용합니다.

---

## Slide 25

## 컬럼별 다중 집계 (Multiple Aggregations per Column)

이 개념은 Pandas에서 데이터를 그룹화(grouping)한 후, **특정 컬럼에 대해 여러 가지 통계 함수를 동시에 적용**하는 방법을 설명합니다. 특히, 하나의 컬럼에 대해 평균, 최댓값, 최솟값 등 여러 집계 연산을 한 번에 수행할 때 유용합니다.

### 핵심 개념

1.  **`df.groupby('기준_컬럼')`**: 데이터를 지정된 '기준_컬럼'의 고유한 값들을 기준으로 그룹으로 나눕니다.
2.  **`.agg({'컬럼1': '집계함수1', '컬럼2': ['집계함수2', '집계함수3']})`**: 그룹화된 각 그룹에 대해 집계 함수를 적용합니다.
    *   `'컬럼1': '집계함수1'`: '컬럼1'에는 하나의 집계 함수(`sum`, `mean`, `max` 등)만 적용합니다.
    *   `'컬럼2': ['집계함수2', '집계함수3']`: **'컬럼2'에는 여러 개의 집계 함수를 리스트 형태로 지정하여 동시에 적용**합니다. 이것이 바로 '컬럼별 다중 집계'의 핵심입니다.
3.  **결과 형태 (MultiIndex)**: 이처럼 여러 집계 함수를 한 컬럼에 적용하면, 결과 데이터프레임의 컬럼 인덱스가 계층적(Hierarchical)인 **MultiIndex** 형태로 생성됩니다. 최상위 인덱스는 원본 컬럼 이름('quantity', 'price'), 그 하위 인덱스는 적용된 집계 함수 이름('sum', 'mean', 'max')이 됩니다. 필요에 따라 `map`이나 리스트 컴프리헨션을 사용하여 이 MultiIndex를 단일 레벨로 평탄화(flatten)할 수 있습니다.

### 구체적인 실생활 예시: 온라인 쇼핑몰 판매 데이터 분석

**상황:** 당신은 온라인 전자제품 쇼핑몰의 데이터 분석가입니다. 매일 수많은 상품 판매 기록이 쌓이고 있습니다. 각 상품 카테고리(예: "스마트폰", "노트북", "악세사리")별로 다음과 같은 정보를 빠르게 파악하고 싶습니다.

*   각 카테고리에서 팔린 **총 수량(quantity_sold)의 합계**.
*   각 카테고리에 속한 상품들의 **평균 단가(unit_price)**와 **가장 높은 단가(unit_price)**.

**원본 데이터 (`sales_df`) 예시:**

```python
import pandas as pd

data = {
    'category': ['스마트폰', '노트북', '스마트폰', '악세사리', '노트북', '스마트폰', '악세사리'],
    'item_name': ['갤럭시 S23', '맥북 에어', '아이폰 15', '무선 이어폰', 'LG 그램', '아이폰 15 프로', '고속 충전기'],
    'quantity_sold': [2, 1, 3, 5, 1, 2, 4],
    'unit_price': [120, 150, 130, 30, 140, 160, 20]
}
sales_df = pd.DataFrame(data)
print("--- 원본 판매 데이터 ---")
print(sales_df)
print("\n")
```

**문제 해결을 위한 Pandas 코드:**

우리의 목표(카테고리별 총 수량 합계, 평균 단가, 최고 단가)를 달성하기 위해 `groupby()`와 `agg()`를 다음과 같이 사용합니다.

```python
# 'category'를 기준으로 그룹화하고, 'quantity_sold'는 총합을, 'unit_price'는 평균과 최댓값을 구합니다.
category_summary = sales_df.groupby('category').agg({
    'quantity_sold': 'sum',
    'unit_price': ['mean', 'max']
})

print("--- 카테고리별 판매 요약 (MultiIndex) ---")
print(category_summary)
print("\n")
```

**코드 상세 설명:**

*   `sales_df.groupby('category')`: `sales_df`를 'category' 컬럼의 값(예: '스마트폰', '노트북', '악세사리')을 기준으로 그룹화합니다.
*   `.agg({...})`: 각 그룹에 대해 지정된 집계 연산을 수행합니다.
    *   `'quantity_sold': 'sum'`: 'quantity_sold' 컬럼에 대해서는 해당 카테고리 내 모든 상품의 '판매 수량'을 합산(sum)합니다.
    *   `'unit_price': ['mean', 'max']`: **'unit_price' 컬럼에 대해서는 해당 카테고리 내 모든 상품의 '평균 단가(mean)'와 '최고 단가(max)'를 동시에 계산**합니다. 이 부분이 바로 '컬럼별 다중 집계'의 핵심입니다.

**결과 해석:**

위 코드를 실행하면 다음과 같은 결과가 나옵니다.

```
--- 원본 판매 데이터 ---
  category    item_name  quantity_sold  unit_price
0   스마트폰   갤럭시 S23              2         120
1     노트북     맥북 에어              1         150
2   스마트폰    아이폰 15              3         130
3   악세사리   무선 이어폰              5          30
4     노트북      LG 그램              1         140
5   스마트폰  아이폰 15 프로              2         160
6   악세사리    고속 충전기              4          20


--- 카테고리별 판매 요약 (MultiIndex) ---
           quantity_sold unit_price      
                     sum       mean max
category                               
노트북                  2      145.0 150
스마트폰                  7      136.666667 160
악세사리                  9       25.0  30
```

*   **인덱스:** 왼쪽의 'category'는 `groupby`의 기준이 된 컬럼입니다.
*   **컬럼 MultiIndex (계층적 컬럼):**
    *   `quantity_sold` 아래에 `sum`이 있습니다. 이는 각 카테고리별 `quantity_sold`의 합계입니다.
    *   `unit_price` 아래에 `mean`과 `max`가 있습니다. 이는 각 카테고리별 `unit_price`의 평균과 최댓값을 나타냅니다.
        *   예를 들어, '스마트폰' 카테고리의 `quantity_sold` 총합은 7개이며, 이 카테고리 내 상품들의 평균 단가는 약 136.67, 최고 단가는 160이라는 것을 한눈에 알 수 있습니다.
*   이렇게 MultiIndex 형태로 출력된 컬럼들을 필요에 따라 `category_summary.columns = ['_'.join(col).strip() for col in category_summary.columns.values]` 와 같은 리스트 컴프리헨션을 사용하여 'quantity_sold_sum', 'unit_price_mean', 'unit_price_max'처럼 단일 레벨 컬럼 이름으로 평탄화할 수도 있습니다.

이처럼 `groupby()`와 `agg()`를 조합하여 컬럼별로 단일 또는 다중의 집계 함수를 적용하면, 복잡한 데이터를 효율적으로 요약하고 분석하여 의사결정에 필요한 통찰력을 얻을 수 있습니다.

---

## Slide 26

### Pandas Groupby: Named Aggregations (Flat Columns)

제시된 슬라이드의 핵심 개념은 Pandas의 `groupby()`와 `agg()` 메서드를 함께 사용하여 데이터를 그룹화하고 여러 집계 함수를 적용할 때, 출력 컬럼의 이름을 직접 지정하여 'MultiIndex' 형태가 아닌 '단일 레벨(flat)'의 깔끔한 컬럼 구조를 얻는 방법입니다.

#### 1. 핵심 개념: 명명된 집계 (Named Aggregations)
일반적으로 Pandas에서 `df.groupby(...).agg(...)`를 사용하여 여러 컬럼에 여러 집계 함수를 적용하면, 결과 데이터프레임의 컬럼 이름이 MultiIndex(다중 인덱스) 형태로 생성될 수 있습니다. 예를 들어, `'price'` 컬럼에 `'min'`과 `'max'`를 모두 적용하면 `('price', 'min')`, `('price', 'max')`와 같은 계층적 컬럼이 생길 수 있습니다.

**명명된 집계(named aggregations)는 이러한 MultiIndex를 피하고, 사용자가 원하는 이름으로 출력 컬럼을 직접 지정할 수 있게 해주는 특별한 `agg` 구문입니다.**

**사용 방법:**
`df.groupby('그룹화_기준_컬럼').agg(새로운_출력_컬럼명=('원본_데이터_컬럼', '집계_함수'))`

*   `새로운_출력_컬럼명`: 결과 데이터프레임에 나타날 컬럼의 이름입니다.
*   `원본_데이터_컬럼`: 실제로 집계 함수를 적용할 원본 데이터프레임의 컬럼 이름입니다.
*   `집계_함수`: `'sum'`, `'min'`, `'max'`, `'mean'`, `'count'` 등 문자열 형태의 집계 함수입니다.

**장점:**
*   **MultiIndex 회피**: 출력 데이터프레임의 컬럼이 단일 레벨로 유지되어 데이터를 다루기 훨씬 쉽고 직관적입니다.
*   **명확한 컬럼 이름**: 원하는 대로 컬럼 이름을 지정할 수 있어 결과의 가독성이 높습니다. 슬라이드에서 `quantity`, `min_price`, `max_price`와 같이 지정된 이름 그대로 출력됩니다.

---

#### 실생활 예시: 온라인 강의 플랫폼 수강생 학습 현황 분석

당신이 온라인 강의 플랫폼의 데이터 관리자라고 가정해 봅시다. 여러 강의를 수강하는 학생들의 학습 데이터를 기반으로, 각 강의별로 수강생들이 얼마나 학습을 했고, 학습 시간은 어떻게 되는지 요약하고 싶습니다.

**원본 데이터 (`course_logs_df`):**
```
   course_id  student_id  lecture_count  watch_time_minutes
0      CS101           A              5                  60
1      CS101           B              3                  45
2      DS201           A              8                 120
3      CS101           C              7                  90
4      DS201           C              4                  50
5      DS201           B              6                  80
```

여기서 우리는 각 `course_id` (강의) 별로 다음 정보를 추출하고자 합니다:
1.  **`total_lectures`**: 해당 강의의 모든 수강생이 수강한 총 강의 수 (sum of `lecture_count`)
2.  **`min_watch_time`**: 해당 강의의 수강생별 최소 시청 시간 (min of `watch_time_minutes`)
3.  **`max_watch_time`**: 해당 강의의 수강생별 최대 시청 시간 (max of `watch_time_minutes`)

**Named Aggregation 적용 코드:**
```python
import pandas as pd

# 예시 데이터프레임 생성
data = {
    'course_id': ['CS101', 'CS101', 'DS201', 'CS101', 'DS201', 'DS201'],
    'student_id': ['A', 'B', 'A', 'C', 'C', 'B'],
    'lecture_count': [5, 3, 8, 7, 4, 6],
    'watch_time_minutes': [60, 45, 120, 90, 50, 80]
}
course_logs_df = pd.DataFrame(data)

# Named Aggregation 적용
course_summary = course_logs_df.groupby('course_id').agg(
    total_lectures=('lecture_count', 'sum'),
    min_watch_time=('watch_time_minutes', 'min'),
    max_watch_time=('watch_time_minutes', 'max')
)

print(course_summary)
```

**결과 (`course_summary`):**
```
           total_lectures  min_watch_time  max_watch_time
course_id                                                
CS101                  15              45              90
DS201                  18              50             120
```

**결과 분석:**
*   **`course_id`**: 각 강의 ID가 인덱스로 그룹화되었습니다.
*   **`total_lectures`**: 'CS101' 강의 수강생들은 총 15회(5+3+7)의 강의를 수강했고, 'DS201' 강의 수강생들은 총 18회(8+4+6)의 강의를 수강했음을 알 수 있습니다.
*   **`min_watch_time`**: 'CS101' 강의 수강생 중 최소 시청 시간은 45분, 'DS201' 강의 수강생 중 최소 시청 시간은 50분임을 알 수 있습니다.
*   **`max_watch_time`**: 'CS101' 강의 수강생 중 최대 시청 시간은 90분, 'DS201' 강의 수강생 중 최대 시청 시간은 120분임을 알 수 있습니다.

이처럼 Named Aggregation을 사용하면 복잡한 MultiIndex 없이 원하는 이름으로 깔끔하게 집계 결과를 얻어, 각 강의의 전반적인 학습 참여도를 효율적으로 파악할 수 있습니다.

---

## Slide 27

해당 슬라이드의 핵심 개념은 **Pandas `groupby()`와 `apply()` 메서드를 활용하여 그룹별로 사용자 정의된 복합 통계량(Custom Metric)을 계산하는 방법**입니다. 특히, 여러 컬럼을 사용하여 직접적인 내장 함수로는 표현하기 어려운 '가중 평균(weighted mean)'과 같은 계산에 유용합니다.

---

### 핵심 개념: `groupby`와 `apply`를 이용한 사용자 정의 통계량 계산

1.  **`df.groupby('product')`**: 데이터프레임 `df`를 'product' 컬럼의 고유한 값(예: 'bananas', 'oranges')을 기준으로 여러 개의 하위 그룹으로 나눕니다. 각 그룹은 원본 데이터프레임의 일부를 포함하는 독립적인 데이터프레임처럼 취급됩니다.
2.  **`.apply(lambda x: ...)`**: `groupby`에 의해 생성된 각 그룹(`x`)에 대해 사용자 정의 함수를 적용합니다. 여기서 `x`는 각 그룹에 해당하는 DataFrame 객체입니다.
    *   **`lambda x: x.total.sum() / x.quantity.sum()`**: 이 람다 함수는 각 그룹(`x`) 내에서 `total` 컬럼의 합계를 `quantity` 컬럼의 합계로 나눕니다. 이는 각 상품의 총 판매액을 총 판매량으로 나누어 **상품별 가중 평균 가격**을 계산하는 방식입니다. 단순 평균이 아닌, 판매량(quantity)에 따라 각 가격에 가중치를 부여한 평균입니다.

### 실생활 예시: 배달 앱의 메뉴별 '평균 주문 단가' 계산

당신이 인기 있는 배달 앱의 데이터 분석가라고 상상해 보세요. 특정 기간 동안 다양한 메뉴가 여러 번 주문되었고, 각 주문마다 수량과 개당 가격, 그리고 총 주문 금액이 기록되어 있습니다. 이때, 각 메뉴의 **'평균 주문 단가'**를 계산하고 싶습니다. 하지만 단순하게 모든 주문의 개당 가격을 평균 내는 것이 아니라, **총 판매액을 총 판매 수량으로 나누어 실제 판매량에 가중치를 부여한 평균 단가**를 알고 싶습니다.

*   **원본 데이터프레임 (`df_orders`) 예시:**

    | order_id | menu_item | quantity | price_per_item | total_price |
    | :------- | :-------- | :------- | :------------- | :---------- |
    | 101      | 불고기버거  | 2        | 5000           | 10000       |
    | 102      | 콜라      | 3        | 2000           | 6000        |
    | 103      | 불고기버거  | 1        | 5500           | 5500        |
    | 104      | 프렌치프라이 | 2        | 3000           | 6000        |
    | 105      | 콜라      | 4        | 1900           | 7600        |

*   **목표:** 각 `menu_item` (불고기버거, 콜라, 프렌치프라이)별로 **가중 평균 주문 단가**를 계산합니다.

*   **Pandas 코드:**

    ```python
    import pandas as pd

    data = {
        'order_id': [101, 102, 103, 104, 105],
        'menu_item': ['불고기버거', '콜라', '불고기버거', '프렌치프라이', '콜라'],
        'quantity': [2, 3, 1, 2, 4],
        'price_per_item': [5000, 2000, 5500, 3000, 1900],
        'total_price': [10000, 6000, 5500, 6000, 7600]
    }
    df_orders = pd.DataFrame(data)

    # 메뉴별 가중 평균 주문 단가 계산
    weighted_avg_price = df_orders.groupby('menu_item').apply(
        lambda x: x['total_price'].sum() / x['quantity'].sum()
    )

    print(weighted_avg_price)
    ```

*   **결과 예상:**

    ```
    menu_item
    콜라          1942.857143  (총 판매액 13600 / 총 수량 7)
    불고기버거       5166.666667  (총 판매액 15500 / 총 수량 3)
    프렌치프라이      3000.000000  (총 판매액 6000 / 총 수량 2)
    dtype: float64
    ```

이 예시에서 `groupby('menu_item')`은 주문 데이터를 메뉴 종류별로 묶습니다. 그리고 `.apply(lambda x: x['total_price'].sum() / x['quantity'].sum())`는 각 메뉴 그룹(`x`)에 대해 총 판매액을 총 수량으로 나누어 해당 메뉴의 '가중 평균 주문 단가'를 계산합니다. 슬라이드의 `df.total.sum() / df.quantity.sum()`과 정확히 동일한 논리로, 각 그룹(`x`로 표현됨) 내부에서 필요한 컬럼들을 활용해 복잡한 계산을 수행할 수 있음을 보여줍니다.

**요약:** `groupby`는 데이터를 의미 있는 단위로 분할하고, `apply`는 분할된 각 단위(그룹)에 대해 우리가 원하는 어떤 복잡한 계산이든 적용할 수 있는 강력한 유연성을 제공합니다. 이는 단순한 합계, 평균을 넘어선 심층적인 분석을 가능하게 합니다.

---

## Slide 28

## 핵심 개념 설명: Pandas `groupby().agg()`를 활용한 복합 집계

이 슬라이드는 Pandas DataFrame에서 `groupby()`와 `agg()` 메서드를 사용하여 여러 종류의 집계(aggregation)를 동시에 수행하는 방법을 보여줍니다. 특히, 내장된 집계 함수(`'sum'`, `'mean'` 등)와 조건부 로직을 포함하는 사용자 정의 `lambda` 함수를 혼합하여 사용하는 고급 기법과, 이 과정에서 그룹 키(group key)에 안전하게 접근하는 방법을 강조합니다.

### 1. `groupby().agg()`로 다양한 집계 함수 동시에 적용하기

`groupby()`는 데이터를 특정 컬럼의 값에 따라 여러 그룹으로 나누는 역할을 합니다. `agg()`는 이렇게 나눠진 각 그룹에 대해 여러 집계 연산을 동시에 적용할 때 사용됩니다. 각 집계 연산은 `새로운_컬럼_이름=('원본_컬럼_이름', '집계_함수_또는_람다')` 형식으로 정의합니다.

**슬라이드 예시 해석:**
*   `total=('total', 'sum')`: 각 `product` 그룹 내에서 'total' 컬럼의 값들을 단순히 합산(sum)하여 'total'이라는 새 컬럼을 만듭니다. 이는 `groupby`의 가장 일반적인 활용법 중 하나입니다.

### 2. 람다(Lambda) 함수를 이용한 조건부/커스텀 집계

`agg()` 메서드는 단순히 `'sum'`, `'mean'`과 같은 문자열 형식의 내장 함수뿐만 아니라, `lambda` 함수를 사용하여 복잡하거나 조건부적인 사용자 정의 집계 로직을 적용할 수 있습니다. `lambda x: ...`에서 `x`는 현재 처리되고 있는 그룹의 특정 컬럼에 해당하는 `Series` 객체를 나타냅니다.

**슬라이드 예시 해석:**
*   `fixed_total=('total', lambda x: x.sum()/2 if x.index[0]=='bananas' else x.sum())`:
    *   'total' 컬럼에 대해 집계하되, `lambda` 함수를 사용합니다.
    *   이 람다 함수는 현재 그룹이 'bananas'인 경우, 해당 그룹의 'total' 값 합계를 2로 나누고, 그렇지 않으면 그냥 합계를 그대로 사용합니다.
    *   `x.index[0]`는 현재 그룹의 `Series` (여기서는 'total' 컬럼)의 첫 번째 인덱스 값을 참조합니다. `df.set_index('product').groupby('product')`로 인해 이 인덱스에는 그룹 키인 'bananas' 또는 'oranges'가 들어가게 됩니다.

### 3. 그룹 키(Group Key) 참조: `x.name` 사용의 중요성 (Less Brittle)

람다 함수 내에서 현재 그룹의 키(예: 'bananas', 'oranges')를 참조할 때, 슬라이드는 `x.index[0]` 대신 `x.name`을 사용할 것을 권장합니다.

*   `x.index[0]` 방식은 그룹화된 `Series`의 첫 번째 인덱스 값이 항상 그룹 키와 일치한다는 가정에 의존합니다. 이는 `set_index`를 하거나 특정 상황에서는 동작할 수 있지만, 데이터의 인덱스가 변경되거나 복잡해질 경우 오류가 발생할 수 있는 "취약(brittle)"한 방법입니다.
*   **`x.name`은 훨씬 견고(robust)한 방법입니다.** `groupby().agg()`에서 `lambda x:`에 전달되는 `x` (각 그룹의 `Series`)는 그 `Series`의 `name` 속성에 해당 그룹의 키 값을 자동으로 가집니다. 따라서 `x.name`을 사용하면 그룹 키를 명확하고 안전하게 참조할 수 있습니다.

---

### 구체적이고 실생활에 가까운 예시: 온라인 쇼핑몰 주문 분석

당신은 온라인 쇼핑몰 분석가입니다. 각 상품 카테고리별로 총 판매액을 집계하고 싶습니다. 그런데 '전자제품' 카테고리는 마진율이 낮아서 특별히 '순 판매액'을 계산할 때 10% 할인을 적용해야 합니다.

**초기 데이터 (DataFrame `orders_df`):**

| order_id | category     | product_name | price | quantity | total_price |
| :------- | :----------- | :----------- | :---- | :------- | :---------- |
| 101      | 의류         | 티셔츠       | 20000 | 2        | 40000       |
| 102      | 전자제품     | 스마트폰     | 800000| 1        | 800000      |
| 103      | 의류         | 바지         | 30000 | 1        | 30000       |
| 104      | 도서         | 소설책       | 15000 | 3        | 45000       |
| 105      | 전자제품     | 무선 이어폰  | 150000| 1        | 150000      |

**목표:**
1.  각 `category`별로 `total_price`의 총합(`total_sales`)을 구합니다.
2.  `category`가 '전자제품'인 경우에만 `total_price` 총합에 0.9 (10% 할인)를 곱한 값을 `net_sales`로 구하고, 그 외 카테고리는 `total_price` 총합을 그대로 `net_sales`로 사용합니다.

```python
import pandas as pd

# 1. 초기 데이터 생성
data = {
    'order_id': [101, 102, 103, 104, 105],
    'category': ['의류', '전자제품', '의류', '도서', '전자제품'],
    'product_name': ['티셔츠', '스마트폰', '바지', '소설책', '무선 이어폰'],
    'price': [20000, 800000, 30000, 15000, 150000],
    'quantity': [2, 1, 1, 3, 1]
}
orders_df = pd.DataFrame(data)
orders_df['total_price'] = orders_df['price'] * orders_df['quantity']

print("--- 원본 주문 데이터 ---")
print(orders_df)
print("\n")

# 2. groupby().agg()를 사용하여 두 가지 집계 동시에 수행
#    - total_sales: 각 카테고리별 총 판매액 (built-in 'sum')
#    - net_sales: '전자제품' 카테고리에 10% 할인을 적용한 순 판매액 (lambda와 x.name 사용)
aggregated_sales = orders_df.groupby('category').agg(
    total_sales=('total_price', 'sum'),
    net_sales=('total_price', lambda x: x.sum() * 0.9 if x.name == '전자제품' else x.sum())
)

print("--- 카테고리별 집계 결과 ---")
print(aggregated_sales)
```

**예시 결과:**

```
--- 원본 주문 데이터 ---
   order_id  category product_name   price  quantity  total_price
0       101        의류         티셔츠   20000         2        40000
1       102      전자제품        스마트폰  800000         1       800000
2       103        의류          바지   30000         1        30000
3       104        도서         소설책   15000         3        45000
4       105      전자제품       무선 이어폰  150000         1       150000


--- 카테고리별 집계 결과 ---
          total_sales  net_sales
category                        
도서              45000    45000.0
전자제품         950000   855000.0
의류              70000    70000.0
```

**설명:**

1.  **`groupby('category')`**: `orders_df`는 'category' 컬럼('의류', '전자제품', '도서')을 기준으로 그룹화됩니다.
2.  **`total_sales=('total_price', 'sum')`**:
    *   '도서' 그룹의 `total_price` 합계: 45000
    *   '전자제품' 그룹의 `total_price` 합계: 800000 + 150000 = 950000
    *   '의류' 그룹의 `total_price` 합계: 40000 + 30000 = 70000
3.  **`net_sales=('total_price', lambda x: x.sum() * 0.9 if x.name == '전자제품' else x.sum())`**:
    *   'total_price' 컬럼에 대해 람다 함수가 적용됩니다.
    *   `lambda x:`에서 `x`는 각 카테고리 그룹에 해당하는 'total_price' 값들의 `Series`입니다.
    *   `x.name == '전자제품'` 부분에서, `x.name`은 현재 처리 중인 그룹의 키인 'category'의 값을 의미합니다.
        *   '도서' 그룹일 때 `x.name`은 '도서'이므로 `x.name == '전자제품'`은 `False`가 되어 `x.sum()` (45000)이 `net_sales`가 됩니다.
        *   '전자제품' 그룹일 때 `x.name`은 '전자제품'이므로 `x.name == '전자제품'`은 `True`가 되어 `x.sum() * 0.9` (950000 * 0.9 = 855000)가 `net_sales`가 됩니다.
        *   '의류' 그룹일 때 `x.name`은 '의류'이므로 `x.name == '전자제품'`은 `False`가 되어 `x.sum()` (70000)이 `net_sales`가 됩니다.

이 예시를 통해 내장 함수와 `lambda` 함수를 결합하여 조건부 로직을 포함한 복합적인 집계 연산을 수행하는 방법을 완벽하게 이해할 수 있을 것입니다. 특히 `x.name`을 사용하여 그룹 키를 안전하게 참조하는 모범 사례를 기억하는 것이 중요합니다.

---

## Slide 29

### 핵심 개념: Wide Format(광범위 형식)과 Long Format(세로 형식)

데이터를 저장하고 분석하는 방식에는 크게 두 가지 일반적인 형식이 있습니다. 슬라이드에서는 이를 'Wide'와 'Long'으로 구분하며, 각 형식의 특징과 변환 방법에 대해 설명하고 있습니다.

1.  **Wide Format (광범위 형식)**
    *   **정의:** 특정 관측치(observation)에 대한 여러 값이 여러 개의 열(columns)에 퍼져 있는 형식입니다. 각 행은 고유한 하나의 독립적인 단위를 나타내며, 해당 단위와 관련된 속성들이 각각의 열에 배치됩니다.
    *   **특징:**
        *   데이터가 가로로 길어지는 형태를 띱니다.
        *   사람이 직관적으로 이해하기 쉽고, 스프레드시트와 같은 형태로 자주 사용됩니다.
        *   새로운 속성이 추가될 때마다 새로운 열을 추가해야 합니다.
    *   **슬라이드 설명:** "values spread across columns" (값들이 열에 걸쳐 퍼져 있음)

2.  **Long Format (세로 형식)**
    *   **정의:** 각 관측치의 모든 값을 행으로 펼쳐 놓은 형식입니다. 즉, 하나의 독립적인 관측치에 대한 특정 속성의 '값' 하나가 한 행을 구성합니다. 이때, 그 값이 어떤 속성에 대한 것인지를 나타내는 '키(key) 열'이 추가됩니다.
    *   **특징:**
        *   데이터가 세로로 길어지는 형태를 띱니다.
        *   데이터베이스나 통계 분석(특히 시계열 데이터나 반복 측정 데이터)에 훨씬 더 적합한 구조입니다.
        *   새로운 속성이 추가되어도 열을 추가하는 대신 행을 추가하는 방식으로 유연하게 대응할 수 있습니다.
    *   **슬라이드 설명:** "one row per observation with key columns" (각 관측치마다 하나의 행을 가지며, 키 열을 포함함)

---

### 실생활 예시: 지역별 제품 판매 데이터

어떤 회사가 '동부'와 '서부' 두 지역에서 '제품 A', '제품 B', '제품 C' 세 가지 제품의 월별 판매량을 기록하고 있다고 가정해 봅시다.

#### 1. Wide Format (광범위 형식)으로 표현

이 경우, 각 '지역'을 고유한 관측치(행)로 보고, 각 '제품'의 판매량을 별도의 열로 나열할 수 있습니다.

| Region (지역) | Sales_ProductA (제품 A 판매량) | Sales_ProductB (제품 B 판매량) | Sales_ProductC (제품 C 판매량) |
| :------------ | :----------------------------- | :----------------------------- | :----------------------------- |
| East (동부)   | 100                            | 150                            | 200                            |
| West (서부)   | 120                            | 180                            | 210                            |

*   **설명:** 위 표에서 각 행은 하나의 '지역'에 대한 정보를 담고 있습니다. '제품 A', '제품 B', '제품 C'의 판매량이라는 값들이 `Sales_ProductA`, `Sales_ProductB`, `Sales_ProductC` 세 개의 개별적인 열에 걸쳐 퍼져 있습니다. 이렇게 보면 각 지역별로 어떤 제품이 얼마나 팔렸는지 한눈에 파악하기 쉽습니다.

#### 2. Long Format (세로 형식)으로 표현

이제 이 데이터를 Long Format으로 바꿔보면, 각 '지역-제품' 조합의 '판매량' 하나하나가 독립적인 관측치(행)가 됩니다.

| Region (지역) | Product (제품) | Sales (판매량) |
| :------------ | :------------- | :------------- |
| East (동부)   | Product A      | 100            |
| East (동부)   | Product B      | 150            |
| East (동부)   | Product C      | 200            |
| West (서부)   | Product A      | 120            |
| West (서부)   | Product B      | 180            |
| West (서부)   | Product C      | 210            |

*   **설명:** 위 표에서 각 행은 '어떤 지역'의 '어떤 제품'이 '얼마나 팔렸는지'라는 하나의 개별적인 판매 관측치를 나타냅니다. 'Region'과 'Product' 열이 이 관측치를 식별하는 '키(key) 열'이 되고, 실제 값은 'Sales' 열에 모여 있습니다.
*   **활용 예시:**
    *   **통계 분석:** 모든 제품의 평균 판매량을 계산하거나, 각 제품별 판매량 추이를 분석하는 등, 'Sales' 열의 값을 기반으로 다양한 통계 분석을 수행하기에 용이합니다. 예를 들어, `Product` 열을 기준으로 그룹화하여 각 제품의 총 판매량을 쉽게 계산할 수 있습니다.
    *   **데이터베이스 저장:** 관계형 데이터베이스에서 데이터를 저장하고 쿼리(query)하기에 효율적인 구조입니다.
    *   **유연성:** 만약 새로운 '제품 D'가 추가된다면, Wide Format에서는 새로운 열을 추가해야 하지만, Long Format에서는 단순히 'Region', 'Product D', '판매량'으로 이루어진 새 행만 추가하면 됩니다.

---

### 형식 변환 (Pivoting)

슬라이드에서 언급된 것처럼, 이 두 형식 간의 변환은 데이터 분석에서 매우 중요합니다.

*   **Wide -> Long 변환:** `stack` 또는 `melt` 연산을 통해 수행됩니다.
    *   예시 데이터에서 Wide Format을 Long Format으로 바꾸는 것을 'melt'라고 생각할 수 있습니다. 여러 열에 퍼져있던 제품 판매량을 'Product'라는 새로운 키 열 아래로 '녹여(melt)' 내리는 과정입니다.
    *   주로 Pandas 라이브러리의 `pd.melt()` 함수가 사용됩니다.
*   **Long -> Wide 변환:** `unstack` 또는 `pivot` 연산을 통해 수행됩니다.
    *   Long Format을 Wide Format으로 바꾸는 것을 'pivot'이라고 생각할 수 있습니다. 'Product' 키 열의 값들(Product A, Product B, Product C)을 새로운 열로 '회전(pivot)'시키고, 해당하는 판매량을 채워 넣는 과정입니다.
    *   주로 Pandas 라이브러리의 `pd.pivot()` 또는 `pd.pivot_table()` 함수가 사용됩니다.

이러한 변환은 데이터의 구조를 분석 목적에 맞게 변경하여 효율적인 탐색, 분석, 시각화를 가능하게 합니다.

---

## Slide 30

### 핵심 개념: `DataFrame.pivot()` 메서드를 이용한 데이터 형태 변경 (Long to Wide)

`DataFrame.pivot()` 메서드는 데이터프레임의 형태를 '긴(long)' 형식에서 '넓은(wide)' 형식으로 변환할 때 사용됩니다. 이는 특정 컬럼의 고유 값들을 새로운 컬럼 헤더로 만들고, 다른 컬럼의 값을 해당 교차점에 배치하여 데이터를 재구성합니다.

**작동 방식:**

1.  **`index` 인자:** 새로운 데이터프레임의 행(row) 인덱스로 사용할 컬럼을 지정합니다. 슬라이드에서는 `client` 컬럼이 인덱스로 사용되었습니다.
2.  **`columns` 인자:** 새로운 데이터프레임의 열(column) 헤더로 사용할 컬럼을 지정합니다. 슬라이드에서는 `product` 컬럼의 고유 값들('bananas', 'oranges')이 새로운 컬럼이 됩니다.
3.  **`values` 인자:** 새로운 데이터프레임의 각 셀을 채울 값을 가져올 컬럼을 지정합니다. 슬라이드에서는 `quantity` 값이 각 클라이언트와 제품의 교차점에 채워졌습니다.

**핵심 제약 사항:**

*   `pivot()` 메서드는 지정된 `index`와 `columns`의 각 고유 조합에 대해 **하나의 `values`만 존재**해야 합니다. 만약 동일한 `(index, columns)` 쌍에 해당하는 값이 두 개 이상이라면 (`'John', 'bananas'`에 대한 `quantity`가 두 개 이상인 경우처럼), `pivot()` 메서드는 에러를 발생시킵니다. 이런 경우에는 `pivot_table()`과 같이 집계(aggregation) 기능을 포함하는 메서드를 사용해야 합니다.

---

### 구체적인 실생활 예시: 지역별 월간 매출액 분석

당신이 여러 지역에서 특정 상품들의 월별 매출액을 기록하는 회사의 데이터 분석가라고 가정해 봅시다.

**1. '긴' 형식의 데이터프레임 (원본):**

| 지역 | 월 | 상품 | 매출액 (단위: 억 원) |
| :--- | :--- | :--- | :---: |
| 서울 | 1월 | A상품 | 10 |
| 서울 | 1월 | B상품 | 12 |
| 부산 | 1월 | A상품 | 8 |
| 부산 | 1월 | B상품 | 9 |
| 서울 | 2월 | A상품 | 11 |
| 서울 | 2월 | B상품 | 13 |
| 부산 | 2월 | A상품 | 7 |
| 부산 | 2월 | B상품 | 10 |

이 데이터는 각 행이 특정 지역, 월, 상품에 대한 매출액을 나타내는 '긴' 형식입니다. 서울의 1월 A상품 매출액을 확인하려면 특정 행을 찾아야 합니다.

**2. `pivot()` 메서드 적용:**

만약 각 지역별로 월별 A상품과 B상품의 매출액을 한눈에 비교하고 싶다면, `pivot()` 메서드를 사용하여 데이터를 '넓은' 형식으로 바꿀 수 있습니다.

먼저, '상품' 컬럼으로 피벗하여 각 지역과 월별로 'A상품'과 'B상품'의 매출액을 나란히 보고 싶습니다.

`df.pivot(index=['지역', '월'], columns='상품', values='매출액')`

*   `index=['지역', '월']`: '지역'과 '월'의 조합이 새로운 데이터프레임의 복합 행 인덱스가 됩니다.
*   `columns='상품'`: 'A상품', 'B상품'이 새로운 컬럼 헤더가 됩니다.
*   `values='매출액'`: 각 지역/월에 해당하는 A상품 및 B상품의 매출액이 셀에 채워집니다.

**3. '넓은' 형식의 결과 데이터프레임:**

| 지역 | 월 | A상품 | B상품 |
| :--- | :-: | :---: | :---: |
| 서울 | 1월 | 10 | 12 |
| 서울 | 2월 | 11 | 13 |
| 부산 | 1월 | 8 | 9 |
| 부산 | 2월 | 7 | 10 |

이제 각 지역의 월별 A상품 및 B상품 매출액이 한눈에 비교 가능하며, 데이터 분석이 훨씬 직관적으로 변환되었습니다. 예를 들어, 서울의 1월 A상품 매출액과 B상품 매출액을 바로 확인할 수 있습니다.

**4. 제약 사항 예시 (중복 데이터 발생 시):**

만약 원본 데이터에 어떤 이유로 "서울, 1월, A상품"에 대한 매출액이 두 번 기록되어 있다면 (예: 실수로 10억, 11억 두 번 입력), `pivot()`은 에러를 발생시킵니다. 왜냐하면 '(서울, 1월)'이라는 인덱스에 'A상품' 컬럼에 해당하는 값이 10억과 11억 두 개가 되기 때문에, `pivot()`은 어떤 값을 넣어야 할지 결정할 수 없기 때문입니다. 이럴 때는 `pivot_table()`을 사용하여 중복된 값들의 평균, 합계 등을 계산하도록 지정해야 합니다.

---

## Slide 31

*오류 발생으로 해설을 생성하지 못했습니다.*

---

## Slide 32

## Pandas `melt()` 함수를 이용한 데이터 재구성 (Wide → Long 형식)

이 슬라이드의 핵심 개념은 Pandas 라이브러리의 `melt()` 함수를 사용하여 데이터를 **'넓은(wide) 형식'에서 '긴(long) 형식'으로 재구성(unpivot 또는 reshape)하는 방법**입니다. 이는 데이터 분석에서 매우 흔하게 필요한 변환으로, 특정 컬럼들을 행으로 '녹여내어' 데이터의 구조를 변경합니다.

---

### 상세 설명

`melt()` 함수는 여러 컬럼에 걸쳐 분산되어 있는 값들을 하나의 컬럼으로 모으고, 원래 컬럼의 이름들을 또 다른 새로운 컬럼으로 생성할 때 사용됩니다. 이를 통해 데이터를 특정 기준(예: 시간, 카테고리 등)으로 그룹화하거나 시각화하기에 더 적합한 형태로 만들 수 있습니다.

슬라이드의 예시를 통해 과정을 단계별로 살펴보겠습니다.

1.  **원본 데이터 (`df`): 넓은 형식**
    ```
    client  product (columns)
           bananas   oranges
    John       5         3
    Silvia     4         2
    ```
    이 데이터는 `client`가 인덱스이고, `bananas`와 `oranges`라는 두 가지 `product` 컬럼에 각 클라이언트의 `quantity`가 넓게 퍼져있는 형태입니다.

2.  **인덱스 리셋 (`df1 = df.reset_index()`):**
    `melt()` 함수를 적용하기 전에, `client` 인덱스를 일반 컬럼으로 변환합니다.
    ```
      client  bananas  oranges
    0   John        5        3
    1 Silvia        4        2
    ```
    이제 `client`가 독립적인 컬럼이 되어 `melt()`의 `id_vars`로 쉽게 지정할 수 있습니다.

3.  **`melt()` 함수 적용:**
    ```python
    df1.melt(id_vars='client', value_vars=['bananas', 'oranges'], value_name='quantity')
    ```
    *   **`id_vars='client'`**: 'client' 컬럼은 고유 식별자(ID) 역할을 하므로, `melt` 과정에서 그대로 유지되어야 하는 컬럼으로 지정합니다. 이는 '녹여내지 않을' 컬럼입니다.
    *   **`value_vars=['bananas', 'oranges']`**: '바나나'와 '오렌지' 컬럼의 데이터가 행으로 '녹아내릴' 대상이 됩니다. 이 컬럼들의 이름(`bananas`, `oranges`)은 새로운 컬럼의 값이 되고, 이 컬럼들의 원래 값들(5, 3, 4, 2)은 또 다른 새로운 컬럼의 값이 됩니다.
    *   **`value_name='quantity'`**: `value_vars`에 지정된 컬럼들에서 추출된 실제 값들(5, 3, 4, 2)이 들어갈 새로운 컬럼의 이름을 'quantity'로 지정합니다. (참고: `bananas`, `oranges`와 같은 변수 이름이 들어갈 새로운 컬럼의 이름은 `var_name` 파라미터로 지정할 수 있으며, 슬라이드 예시에서는 자동으로 `product`로 추론되거나 명시적으로 `var_name='product'`가 사용되었을 것으로 보입니다.)

4.  **결과: 긴 형식 (Long Format)**
    ```
      client    product  quantity
    0   John    bananas         5
    1 Silvia    bananas         4
    2   John    oranges         3
    3 Silvia    oranges         2
    ```
    이제 데이터는 `client`, `product`, `quantity` 세 개의 컬럼으로 재구성되었습니다. 각 행은 특정 `client`가 특정 `product`를 `quantity`만큼 구매했다는 하나의 사실을 나타냅니다.

**결론적으로, `melt()`는 ID/값 컬럼에 대한 명시적인 제어가 필요할 때, 즉 여러 컬럼에 퍼져있는 측정값을 하나의 "측정값" 컬럼으로 모으고, 해당 측정값의 "유형"을 나타내는 새로운 컬럼을 만들고자 할 때 선택해야 하는 강력한 도구입니다.**

---

### 구체적이고 실생활에 가까운 예시: 학생 시험 점수 기록

대학에서 수강생들의 과목별 시험 점수를 기록한 데이터가 있다고 가정해 봅시다. 이 데이터는 보통 각 과목이 하나의 컬럼으로 되어 있는 '넓은' 형식으로 저장됩니다.

**1. 원본 데이터 (넓은 형식): `df_grades_wide`**

| 학생ID | 중간고사_국어 | 중간고사_영어 | 기말고사_국어 | 기말고사_영어 |
| :----- | :------------ | :------------ | :------------ | :------------ |
| 101    | 85            | 90            | 92            | 88            |
| 102    | 78            | 85            | 80            | 91            |
| 103    | 90            | 88            | 95            | 87            |

이 형식은 한눈에 각 학생의 모든 점수를 볼 수 있지만, '국어' 점수만을 모아서 평균을 내거나, '중간고사' 점수만 비교하는 등의 분석을 하기에는 다소 불편합니다.

**2. `melt()` 함수 적용:**

우리의 목표는 이 데이터를 각 행이 '어떤 학생이', '어떤 과목의', '어떤 시험에서', '몇 점을 받았는지'를 명확하게 보여주는 '긴' 형식으로 바꾸는 것입니다.

```python
import pandas as pd

data = {
    '학생ID': [101, 102, 103],
    '중간고사_국어': [85, 78, 90],
    '중간고사_영어': [90, 85, 88],
    '기말고사_국어': [92, 80, 95],
    '기말고사_영어': [88, 91, 87]
}
df_grades_wide = pd.DataFrame(data)

# melt() 함수 적용
df_grades_long = df_grades_wide.melt(
    id_vars=['학생ID'],
    value_vars=['중간고사_국어', '중간고사_영어', '기말고사_국어', '기말고사_영어'],
    var_name='시험_과목',  # 새로운 변수 컬럼의 이름
    value_name='점수'     # 새로운 값 컬럼의 이름
)
```

*   `id_vars=['학생ID']`: '학생ID'는 각 학생을 식별하는 고유한 값으로, '녹여내지 않고' 그대로 유지합니다.
*   `value_vars=['중간고사_국어', ..., '기말고사_영어']`: 이 컬럼들의 이름(예: '중간고사_국어')은 새로운 컬럼인 `시험_과목`의 값이 되고, 이 컬럼들이 원래 가지고 있던 숫자 값(예: 85)은 새로운 컬럼인 `점수`의 값이 됩니다.
*   `var_name='시험_과목'`: `value_vars`에 지정된 원래 컬럼 이름들이 들어갈 새로운 컬럼의 이름을 '시험_과목'으로 지정합니다.
*   `value_name='점수'`: 원래 컬럼에 있던 점수 값들이 들어갈 새로운 컬럼의 이름을 '점수'로 지정합니다.

**3. 결과 데이터 (긴 형식): `df_grades_long`**

| 학생ID | 시험_과목   | 점수 |
| :----- | :---------- | :--- |
| 101    | 중간고사_국어 | 85   |
| 102    | 중간고사_국어 | 78   |
| 103    | 중간고사_국어 | 90   |
| 101    | 중간고사_영어 | 90   |
| 102    | 중간고사_영어 | 85   |
| 103    | 중간고사_영어 | 88   |
| 101    | 기말고사_국어 | 92   |
| 102    | 기말고사_국어 | 80   |
| 103    | 기말고사_국어 | 95   |
| 101    | 기말고사_영어 | 88   |
| 102    | 기말고사_영어 | 91   |
| 103    | 기말고사_영어 | 87   |

이제 '긴' 형식의 데이터를 얻었습니다. 이 데이터는 다음과 같은 분석에 매우 유용합니다:
*   **과목별 평균 점수 계산:** `df_grades_long.groupby('시험_과목')['점수'].mean()`
*   **특정 시험(예: 중간고사)의 모든 점수 선택:** `df_grades_long[df_grades_long['시험_과목'].str.contains('중간고사')]`
*   **각 학생의 모든 점수 추적 및 시각화**
*   **데이터베이스 저장 시 효율성:** 일반적으로 '긴' 형식이 관계형 데이터베이스에 저장하기 더 적합합니다.

이처럼 `melt()` 함수는 복잡한 데이터 분석과 시각화 작업을 위해 데이터를 준비하는 데 필수적인 도구입니다.

---

## Slide 33

## 관계형 나눗셈 (Relational Division) $R \div S$ ("for all" 조건)

### 1. 핵심 개념

관계형 나눗셈($R \div S$)은 특정 조건을 *모두* 만족하는 엔티티를 찾는 데 사용되는 고급 관계형 대수 연산입니다. 주어진 슬라이드에서는 $R(\text{Name, Year})$ 테이블과 $S(\text{Year})$ 테이블을 사용하여, $S$에 있는 *모든* 연도에 등장한 `Name`을 찾아내는 과정을 보여줍니다.

*   **R (Name, Year):** 어떤 `Name`이 어떤 `Year`에 등장했는지 기록한 테이블.
*   **S (Year):** 우리가 찾고자 하는 기준이 되는 `Year` 목록을 담은 테이블.
*   **$R \div S$의 결과:** $S$에 포함된 *모든* `Year`에 대해 $R$에 기록된 `Name`들의 집합.

**슬라이드 예시:**
*   $R$: (Alice, 1910), (Alice, 1911), (Bob, 1910), (Bob, 1911), (Carol, 1910)
*   $S$: (1910), (1911)
*   $R \div S$: {Alice, Bob}
    *   `Alice`는 1910년과 1911년 *모두* 등장했으므로 결과에 포함됩니다.
    *   `Bob`도 1910년과 1911년 *모두* 등장했으므로 결과에 포함됩니다.
    *   `Carol`은 1910년에만 등장하고 1911년에는 등장하지 않았으므로 (즉, $S$의 *모든* 연도에 등장하지 않았으므로) 결과에서 제외됩니다.

이처럼 "for all" 조건, 즉 $S$의 모든 요소와 일치하는 것을 찾는 것이 나눗셈의 핵심입니다.

### 2. 구체적이고 실생활에 가까운 예시: "올인원 구독자 찾기"

한 스트리밍 서비스가 있다고 가정해 봅시다. 이 서비스는 "프리미엄 패키지"라는 특별한 콘텐츠 묶음을 제공합니다. 이 패키지에 포함된 *모든* 콘텐츠를 시청한 사용자에게만 "올인원 구독자"라는 특별한 혜택을 주려고 합니다.

**테이블 정의:**

1.  **`시청_기록` 테이블 ($R$):**
    *   `사용자ID`: 콘텐츠를 시청한 사용자의 고유 ID.
    *   `콘텐츠ID`: 시청한 콘텐츠의 고유 ID.

    | 사용자ID | 콘텐츠ID |
    | :------ | :------- |
    | userA   | Movie_X  |
    | userA   | Movie_Y  |
    | userA   | Movie_Z  |
    | userB   | Movie_X  |
    | userB   | Movie_Y  |
    | userC   | Movie_X  |
    | userD   | Movie_Z  |

2.  **`프리미엄_패키지` 테이블 ($S$):**
    *   `콘텐츠ID`: 프리미엄 패키지에 포함된 콘텐츠의 고유 ID. (여기서는 `Movie_X`, `Movie_Y`, `Movie_Z` 세 가지라고 가정)

    | 콘텐츠ID |
    | :------- |
    | Movie_X  |
    | Movie_Y  |
    | Movie_Z  |

**문제:** `프리미엄_패키지`에 있는 *모든* 콘텐츠를 시청한 `사용자ID`는 누구인가요? 즉, "올인원 구독자"는 누구인가요?

**관계형 나눗셈 적용:** `시청_기록` $\div$ `프리미엄_패키지`

결과는 다음과 같습니다:

*   **userA:** `Movie_X`, `Movie_Y`, `Movie_Z` *모두* 시청했습니다. -> **포함**
*   **userB:** `Movie_X`, `Movie_Y`를 시청했지만, `Movie_Z`는 시청하지 않았습니다. (즉, `프리미엄_패키지`의 모든 콘텐츠를 시청하지 않았습니다.) -> **제외**
*   **userC:** `Movie_X`만 시청했습니다. -> **제외**
*   **userD:** `Movie_Z`만 시청했습니다. -> **제외**

따라서, `시청_기록` $\div$ `프리미엄_패키지`의 결과는 **{userA}** 입니다.

이 예시를 통해 관계형 나눗셈이 특정 집합($S$)의 *모든* 요소를 만족하는지 확인해야 할 때 얼마나 유용하게 사용될 수 있는지 이해할 수 있을 것입니다. 슬라이드의 판다스 코드도 이와 동일한 논리로 작동하며, `S`의 고유한 `Year` 개수(`need`)를 구한 뒤, 각 `Name`별로 `Year` 개수가 `need`와 일치하는지를 확인하여 "for all" 조건을 만족하는 `Name`을 찾아냅니다.

---

## Slide 34

## 핵심 개념: Pivot (Cross-Tab)

`Pivot` 또는 `Cross-Tab`은 평평한(flat) 형태의 데이터를 행(rows)과 열(columns)을 기준으로 재구성하여, 각 교차점에 특정 기준에 따라 집계된 값을 요약하여 보여주는 강력한 데이터 분석 기법입니다. 이는 마치 스프레드시트의 피벗 테이블과 같은 역할을 합니다.

### 1. 정의 및 목적

*   **재구성 (Reshape):** 원본 데이터 `R`을 행과 열로 색인된(indexed) 행렬 형태로 변환합니다.
*   **집계 (Aggregation):** 새롭게 만들어진 행렬의 각 셀(Cell)은 해당 행과 열의 교차점에 해당하는 원본 데이터 조각(slice)에 대해 특정 함수 `f(A)` (예: 개수, 합계, 평균)가 적용된 결과값을 가집니다.
*   **목적:** 복잡한 데이터를 단순화하고, 두 개 이상의 변수 간의 관계나 패턴, 빈도 등을 한눈에 파악하기 쉽게 만듭니다.

### 2. Pandas에서의 구현

Pandas 라이브러리에서는 주로 두 가지 함수를 사용하여 피벗 테이블을 생성합니다.

*   `pd.crosstab`: 주로 두 개 이상의 인자(factor) 간의 빈도수(frequency)를 계산할 때 사용됩니다. 기본적으로 각 조합의 개수를 세는(`count`) 역할을 합니다.
*   `df.pivot_table`: `pd.crosstab`보다 더 일반적이고 유연합니다. 집계할 값(`values`)과 집계 함수(`aggfunc`)를 명시적으로 지정할 수 있어, 빈도수 외에 합계, 평균 등 다양한 통계량을 계산할 수 있습니다.

    *   `index`: 피벗 테이블의 행(row)이 될 컬럼(들).
    *   `columns`: 피벗 테이블의 열(column)이 될 컬럼(들).
    *   `values`: 집계할 데이터가 있는 컬럼. 이 컬럼의 값들을 `aggfunc`으로 집계합니다.
    *   `aggfunc`: `values` 컬럼에 적용할 집계 함수 (예: `'sum'`, `'mean'`, `'count'`, `np.sum`).
    *   `fill_value`: 누락된(NaN) 값에 채울 값.
    *   `margins=True`: 행과 열의 총합(Grand Total)을 추가할지 여부.

### 3. 구체적이고 실생활에 가까운 예시: 온라인 쇼핑몰 판매 분석

당신이 온라인 쇼핑몰의 데이터 분석가라고 가정해 봅시다. 당신은 다음과 같은 판매 데이터(`sales_df`)를 가지고 있습니다.

| Order ID | Product Category | Region | Customer Segment | Sales Amount | Quantity Sold |
| :------- | :--------------- | :----- | :--------------- | :----------- | :------------ |
| 1        | Electronics      | North  | VIP              | 1200         | 1             |
| 2        | Books            | South  | Regular          | 50           | 2             |
| 3        | Electronics      | East   | Regular          | 800          | 1             |
| 4        | Clothing         | North  | VIP              | 200          | 3             |
| 5        | Books            | West   | Regular          | 75           | 1             |
| 6        | Electronics      | North  | Regular          | 1500         | 1             |
| 7        | Clothing         | South  | VIP              | 300          | 2             |

이 데이터를 가지고 **각 `Region` (지역)별로 `Customer Segment` (고객 분류)에 따른 총 `Sales Amount` (판매 금액)가 어떻게 되는지** 분석하고 싶습니다.

#### 1. 목표 설정 및 피벗 설계

*   **궁금한 점:** "어떤 지역의 어떤 고객 분류가 우리 쇼핑몰에 가장 많은 매출을 가져다주는가?"
*   **피벗 설계:**
    *   **행 (index):** `Region` (지역)
    *   **열 (columns):** `Customer Segment` (고객 분류)
    *   **집계할 값 (values):** `Sales Amount` (판매 금액)
    *   **집계 함수 (aggfunc):** `sum` (총 판매 금액)
    *   **누락 값 처리 (fill_value):** 0 (해당 조합의 판매가 없으면 0으로 표시)
    *   **총합 추가 (margins):** True (각 지역별 총합과 고객 분류별 총합을 보고 싶음)

#### 2. 코드 (가상)

`sales_df.pivot_table(index="Region", columns="Customer Segment", values="Sales Amount", aggfunc="sum", fill_value=0, margins=True)`

#### 3. 결과 (예상)

다음과 같은 피벗 테이블이 생성될 것입니다:

| Customer Segment | Regular | VIP  | All   |
| :--------------- | :------ | :--- | :---- |
| **Region**       |         |      |       |
| East             | 800     | 0    | 800   |
| North            | 1500    | 1400 | 2900  |
| South            | 50      | 300  | 350   |
| West             | 75      | 0    | 75    |
| **All**          | 2425    | 1700 | 4125  |

#### 4. 결과 해석

*   **한눈에 파악:** 이 테이블을 통해 우리는 "North" 지역의 "Regular" 고객이 1500달러, "VIP" 고객이 1400달러의 매출을 발생시켜 가장 큰 매출(총 2900달러)을 기록했음을 즉시 알 수 있습니다.
*   "East"와 "West" 지역에는 "VIP" 고객의 판매가 없었으며, "South" 지역에서는 "VIP" 고객이 "Regular" 고객보다 더 많은 판매를 기여했음을 볼 수 있습니다.
*   가장 하단과 오른쪽의 `All` 열/행은 각각 전체 고객 분류에 대한 지역별 총합, 그리고 전체 지역에 대한 고객 분류별 총합을 보여줍니다. 예를 들어, 전체 "Regular" 고객은 총 2425달러의 매출을, "VIP" 고객은 1700달러의 매출을 발생시켰다는 것을 알 수 있습니다.

이처럼 피벗 테이블을 활용하면, 원본 데이터를 일일이 필터링하거나 여러 번 집계할 필요 없이, 복잡한 비즈니스 질문에 대한 답을 빠르고 명확하게 얻을 수 있습니다.

---

## Slide 35

## ERA 쿼리 및 Pandas 파이프라인으로 '연도별/성별 최고 인기 아기 이름' 찾기

이 슬라이드는 복잡한 데이터 분석 요구사항을 관계형 대수(ERA) 쿼리로 표현하고, 이를 Pandas 파이프라인으로 구현하는 과정을 보여줍니다. 핵심 목표는 주어진 '아기 이름' 데이터셋에서 **각 연도와 성별에 대해 가장 높은 '점유율'을 가진 아기 이름을 찾아내는 것**입니다.

### 1. 핵심 개념: 관계형 대수(ERA Query) 이해

제시된 관계형 대수 쿼리는 다음과 같습니다.
`γYear,Sex; top1_by(share) πYear, Sex, Name, Count, Count/SUM_Y(Count)→share σYear≥1910(babynames)`

이는 다음 세 가지 주요 단계로 분해될 수 있습니다.

1.  **선택 (Selection, `σ`)**: `σYear≥1910(babynames)`
    *   `babynames` 데이터셋에서 `Year` (연도)가 1910년 이상인 모든 레코드(행)를 선택합니다. 즉, 1910년 이전의 데이터는 분석에서 제외됩니다.
2.  **일반화된 투영 (Generalized Projection, `π`)**: `πYear, Sex, Name, Count, Count/SUM_Y(Count)→share`
    *   선택된 레코드에서 `Year`, `Sex`, `Name`, `Count` 컬럼을 추출합니다.
    *   동시에 `Count` 컬럼을 해당 연도의 전체 아기 이름 수(`SUM_Y(Count)`)로 나누어 `share`라는 새로운 컬럼을 계산합니다. 이 `share`는 특정 아기 이름이 해당 연도 전체에서 차지하는 비율을 의미합니다. 단순히 컬럼을 선택하는 것이 아니라 계산을 포함하므로 '일반화된 투영'입니다.
3.  **그룹화 및 집계 (Grouping and Aggregation, `γ`)**: `γYear,Sex; top1_by(share)`
    *   위에서 계산된 결과를 `Year`와 `Sex`를 기준으로 그룹화합니다.
    *   각 `(Year, Sex)` 그룹 내에서 `share` 값이 가장 높은(top 1) 아기 이름 레코드를 선택합니다.

### 2. 핵심 개념: Pandas 파이프라인 구현

위의 관계형 대수 쿼리를 Pandas 코드로 구현한 파이프라인은 다음과 같습니다.

```python
result = (babynames
    .query("Year >= 1910")                                  # 1단계: 연도 필터링 (Selection)
    .assign(year_total=lambda d: d.groupby("Year")["Count"].transform("sum"),
            share=lambda d: d["Count"]/d["year_total"])     # 2단계: 'year_total' 및 'share' 계산 (Generalized Projection)
    [["Year", "Sex", "Name", "Count", "share"]]             # 3단계: 필요한 컬럼만 선택 (Projection)
    .sort_values(["Year", "Sex", "share"], ascending=[True, True, False]) # 4단계: 정렬
    .groupby(["Year", "Sex"]).head(1)                       # 5단계: 그룹별 상위 1개 선택 (Grouping & Aggregation)
    .reset_index(drop=True)
)
```

각 라인의 의미는 다음과 같습니다.

*   **`.query("Year >= 1910")`**:
    *   `babynames` DataFrame에서 `Year` 컬럼의 값이 1910 이상인 행들만 필터링합니다. 이는 관계형 대수의 `σYear≥1910`에 해당합니다.
*   **`.assign(...)`**:
    *   새로운 컬럼을 생성하거나 기존 컬럼을 수정합니다.
    *   `year_total=lambda d: d.groupby("Year")["Count"].transform("sum")`: `Year`를 기준으로 그룹화한 후 각 연도의 `Count` (아기 이름 수)의 총합을 계산합니다. 여기서 `transform("sum")`이 중요합니다. `transform`은 그룹별 집계 결과를 원본 DataFrame의 행 수에 맞게 다시 확장하여, 각 행에 해당 연도의 총합을 붙여줍니다. (예: 2000년의 모든 아기 이름 행에는 2000년의 총 아기 이름 수가 `year_total`로 할당됩니다.)
    *   `share=lambda d: d["Count"]/d["year_total"]`: 각 아기 이름의 `Count`를 해당 연도의 `year_total`로 나누어 `share` (점유율) 컬럼을 계산합니다. 이 두 `assign` 작업은 관계형 대수의 일반화된 투영 `π...Count/SUM_Y(Count)→share`에 해당합니다.
*   **`[["Year", "Sex", "Name", "Count", "share"]]`**:
    *   계산된 DataFrame에서 `Year`, `Sex`, `Name`, `Count`, `share` 컬럼만 선택합니다. 이는 최종적인 투영(Projection)입니다.
*   **`.sort_values(["Year", "Sex", "share"], ascending=[True, True, False])`**:
    *   데이터를 정렬합니다. `Year`와 `Sex`는 오름차순(`True`)으로, `share`는 내림차순(`False`)으로 정렬합니다. 이 정렬은 다음 단계에서 각 그룹의 "가장 높은 점유율"을 쉽게 찾기 위해 필수적입니다.
*   **`.groupby(["Year", "Sex"]).head(1)`**:
    *   정렬된 데이터를 `Year`와 `Sex`를 기준으로 다시 그룹화합니다.
    *   각 그룹에서 `head(1)`을 호출하여 첫 번째 행만 가져옵니다. `share`가 내림차순으로 정렬되어 있었기 때문에, 각 `(Year, Sex)` 그룹에서 `share`가 가장 높은(즉, 가장 인기 있는) 아기 이름이 선택됩니다. 이는 관계형 대수의 `γYear,Sex; top1_by(share)`에 해당합니다.
*   **`.reset_index(drop=True)`**:
    *   `groupby` 작업 후 생기는 그룹 인덱스를 제거하고 새로운 기본 정수 인덱스를 생성합니다. `drop=True`는 이전 인덱스를 컬럼으로 유지하지 않고 완전히 버린다는 의미입니다.

### 3. 구체적이고 실생활에 가까운 예시: "최고 인기 스트리밍 콘텐츠" 찾기

우리는 "아기 이름" 대신 "스트리밍 서비스 콘텐츠 시청 기록" 데이터를 분석한다고 가정해봅시다. 목표는 **각 연도와 콘텐츠 카테고리(영화, 드라마 등)별로 가장 많은 시청 시간을 기록한 콘텐츠**를 찾는 것입니다.

**가상 데이터셋 (`streaming_data` DataFrame):**

| Year | Category | ContentTitle | WatchTime_Hours |
| :--- | :------- | :----------- | :-------------- |
| 2021 | Movie    | 영화 A       | 150             |
| 2021 | Movie    | 영화 B       | 200             |
| 2021 | Drama    | 드라마 X     | 300             |
| 2021 | Drama    | 드라마 Y     | 180             |
| 2022 | Movie    | 영화 C       | 250             |
| 2022 | Movie    | 영화 D       | 120             |
| 2022 | Drama    | 드라마 Z     | 400             |
| 2022 | Drama    | 드라마 W     | 220             |

**분석 파이프라인 적용:**

1.  **필터링**: 최근 2년간의 데이터만 보고 싶다고 가정하여, `Year >= 2021`인 데이터만 선택합니다. (슬라이드의 `.query("Year >= 1910")`와 동일)
    ```python
    filtered_data = streaming_data.query("Year >= 2021")
    ```
2.  **'카테고리별_연간_총시청시간' 및 '점유율' 계산**:
    *   먼저, 각 `Year`와 `Category` 조합별로 총 시청 시간을 계산해야 합니다. 예를 들어, 2021년 'Movie' 카테고리의 모든 콘텐츠 시청 시간을 합산합니다. `groupby(["Year", "Category"])["WatchTime_Hours"].transform("sum")`을 사용하여 이 값을 각 콘텐츠에 할당합니다.
    *   그다음, 각 콘텐츠의 `WatchTime_Hours`를 해당 `(Year, Category)`의 `total_category_year_watchtime`으로 나누어 `share` (점유율)를 계산합니다.
    ```python
    calculated_data = filtered_data.assign(
        total_category_year_watchtime=lambda d: d.groupby(["Year", "Category"])["WatchTime_Hours"].transform("sum"),
        share=lambda d: d["WatchTime_Hours"] / d["total_category_year_watchtime"]
    )
    ```
3.  **컬럼 선택**: `Year`, `Category`, `ContentTitle`, `WatchTime_Hours`, `share` 컬럼만 남깁니다. (슬라이드의 `[[]]` 부분과 동일)
    ```python
    projected_data = calculated_data[["Year", "Category", "ContentTitle", "WatchTime_Hours", "share"]]
    ```
4.  **정렬**: `Year` (오름차순), `Category` (오름차순), `share` (내림차순) 순으로 데이터를 정렬합니다. 이렇게 하면 각 `(Year, Category)` 그룹 내에서 가장 높은 `share`를 가진 콘텐츠가 맨 위로 오게 됩니다. (슬라이드의 `.sort_values()`와 동일)
    ```python
    sorted_data = projected_data.sort_values(
        ["Year", "Category", "share"], ascending=[True, True, False]
    )
    ```
5.  **그룹별 상위 1개 선택**: `Year`와 `Category`를 기준으로 그룹화한 후, 각 그룹의 첫 번째 행(`head(1)`)을 선택합니다. 이는 정렬 덕분에 각 그룹에서 가장 높은 `share`를 가진 콘텐츠가 됩니다. (슬라이드의 `.groupby().head(1)`과 동일)
    ```python
    top_content_per_category_year = sorted_data.groupby(["Year", "Category"]).head(1)
    ```
6.  **인덱스 초기화**: 최종 결과의 인덱스를 깔끔하게 정리합니다. (슬라이드의 `.reset_index(drop=True)`와 동일)
    ```python
    final_result = top_content_per_category_year.reset_index(drop=True)
    ```

**최종 결과 예시:**

| Year | Category | ContentTitle | WatchTime_Hours | share |
| :--- | :------- | :----------- | :-------------- | :---- |
| 2021 | Drama    | 드라마 X     | 300             | 0.625 |
| 2021 | Movie    | 영화 B       | 200             | 0.571 |
| 2022 | Drama    | 드라마 Z     | 400             | 0.645 |
| 2022 | Movie    | 영화 C       | 250             | 0.676 |

이 예시를 통해 우리는 각 연도와 카테고리별로 시청 점유율이 가장 높은 단 하나의 콘텐츠를 정확하게 식별할 수 있습니다. 슬라이드의 아기 이름 예시와 동일한 논리적 흐름과 Pandas 함수들이 어떻게 실제 데이터 분석에 활용되는지 명확히 보여줍니다. 특히 `groupby().transform()`을 사용하여 그룹별 통계를 계산하고 이를 개별 행에 다시 매핑하는 강력한 기법을 이해하는 것이 중요합니다.

---

## Slide 36

다음은 첨부된 슬라이드의 핵심 개념과 각 개념에 대한 구체적인 실생활 예시입니다.

---

### Query Best Practices (ERA $\leftrightarrow$ pandas)

`pandas`에서 데이터 쿼리(Query)를 효율적이고 명확하게 수행하기 위한 모범 사례들입니다.

#### 1. Selection (선택)
*   **개념**: 조건(마스크)을 사용하여 데이터프레임의 특정 행을 선택할 때, 복잡한 조건은 괄호로 명확히 묶어 가독성을 높이고, SQL과 유사한 `.query()` 메소드를 고려하여 코드를 더 직관적으로 만듭니다.
*   **실생활 예시**: 온라인 쇼핑몰에서 `가격이 5만원 이상`이면서 `재고가 10개 미만`인 상품을 찾고 싶을 때.
    ```python
    import pandas as pd
    data = {'상품명': ['노트북', '마우스', '키보드', '모니터', '웹캠'],
            '가격': [1200000, 30000, 70000, 300000, 45000],
            '재고': [5, 20, 8, 3, 15]}
    df = pd.DataFrame(data)

    # 괄호를 사용하여 조건 명확화 (가장 일반적인 pandas 필터링 방식)
    filtered_products_mask = df[(df['가격'] >= 50000) & (df['재고'] < 10)]
    print("괄호를 사용한 선택:\n", filtered_products_mask)

    # .query() 메소드 사용 (SQL과 유사하여 가독성이 더 높을 수 있음)
    filtered_products_query = df.query("가격 >= 50000 and 재고 < 10")
    print("\n.query()를 사용한 선택:\n", filtered_products_query)
    ```

#### 2. Generalized projection (일반화된 프로젝션)
*   **개념**: 기존 열을 바탕으로 새로운 계산된 열을 만들 때 `.assign()` 메소드를 사용하여 원본 데이터프레임을 변경하지 않고, 이후 명시적으로 필요한 열만 선택하여 최종 결과를 만듭니다. 이는 중간 계산 과정을 명확히 하고 코드 체인에 유용합니다.
*   **실생활 예시**: 전자상거래 주문 데이터에서 `판매가`와 `수량`을 곱하여 `총 매출` 열을 새로 만들고, `상품명`과 `총 매출` 정보만 확인하고 싶을 때.
    ```python
    import pandas as pd
    order_data = {'상품명': ['A상품', 'B상품', 'C상품', 'D상품'],
                  '판매가': [10000, 5000, 15000, 8000],
                  '수량': [3, 5, 2, 7]}
    df_orders = pd.DataFrame(order_data)

    # .assign()으로 '총_매출' 열을 계산하고, 필요한 열만 선택
    result_projection = df_orders.assign(총_매출=df_orders['판매가'] * df_orders['수량'])[
        ['상품명', '총_매출']
    ]
    print(result_projection)
    ```

#### 3. Set semantics (집합 의미론)
*   **개념**: 중복을 허용하는 '가방(bag)'이 아닌, 중복되지 않는 고유한 요소들의 모임인 '집합(set)'처럼 데이터를 다루고 싶을 때 `.drop_duplicates()` 메소드를 사용하여 중복 행을 제거합니다.
*   **실생활 예시**: 웹사이트 접속 로그에서 한 사용자가 여러 번 접속한 기록이 있을 때, 실제로 사이트에 접속한 `고유 사용자 수`를 알고 싶을 때.
    ```python
    import pandas as pd
    access_log = {'사용자_ID': ['user001', 'user002', 'user001', 'user003', 'user002'],
                  '접속_시간': ['10:00', '10:05', '10:15', '10:20', '10:25']}
    df_log = pd.DataFrame(access_log)

    print("원본 접속 로그 (중복 포함):\n", df_log)

    # '사용자_ID' 기준으로 중복 제거하여 고유 사용자 목록 생성
    unique_users_df = df_log.drop_duplicates(subset=['사용자_ID'])
    print("\n고유 사용자 목록:\n", unique_users_df)
    print("\n고유 사용자 수:", len(unique_users_df))
    ```

#### 4. Joins (조인)
*   **개념**: 두 데이터프레임을 결합(조인)할 때, 조인 키(기준 열)를 항상 명시하고, 키의 다중성(multiplicity)을 검증하여 의도치 않은 행 폭증(row blow-up)을 방지해야 합니다. `pandas.merge`의 `validate` 인자를 활용하면 좋습니다.
*   **실생활 예시**: `직원 정보`와 `부서 정보`를 합치려는데, 만약 `부서 정보` 데이터에 같은 `부서_ID`를 가진 부서가 여러 개 정의되어 있다면 (예: 부서_ID 101이 '영업1팀', '영업2팀'으로 두 번 존재), 한 직원이 예상치 않게 여러 부서에 할당된 것처럼 행이 복제될 수 있습니다.
    ```python
    import pandas as pd
    employees = pd.DataFrame({
        '직원_ID': [1, 2, 3], '이름': ['김철수', '박영희', '이지혜'], '부서_ID': [101, 102, 101]
    })
    departments_good = pd.DataFrame({
        '부서_ID': [101, 102], '부서명': ['영업팀', '마케팅팀']
    })
    departments_bad = pd.DataFrame({ # 부서_ID 101이 중복되어 정의된 경우
        '부서_ID': [101, 102, 101], '부서명': ['영업1팀', '마케팅팀', '영업2팀']
    })

    print("직원 정보:\n", employees)
    print("\n정상 부서 정보:\n", departments_good)
    print("\n중복 포함 부서 정보:\n", departments_bad)

    # 정상적인 조인 (key multiplicity 문제 없음)
    merged_good = pd.merge(employees, departments_good, on='부서_ID', how='left')
    print("\n정상 조인 결과:\n", merged_good)

    # row blow-up이 발생하는 조인 (부서_ID 101이 departments_bad에 중복되어 김철수 행이 복제됨)
    merged_blow_up = pd.merge(employees, departments_bad, on='부서_ID', how='left')
    print("\nRow blow-up 조인 결과 (김철수 행이 2개):\n", merged_blow_up)

    # validate='many_to_one' 사용 시 에러 발생 (right 데이터프레임의 키가 고유하지 않으므로)
    # try:
    #     pd.merge(employees, departments_bad, on='부서_ID', how='left', validate='many_to_one')
    # except ValueError as e:
    #     print(f"\nvalidate 에러: {e}")
    ```

#### 5. Grouping (그룹화)
*   **개념**: 데이터를 특정 기준(열)으로 그룹화하여 집계할 때, `sum`, `mean`, `size`와 같은 내장 함수를 사용하는 것을 선호하고, 결과로 생성되는 집계 열의 이름을 명확하게 지정하여 데이터의 의미를 쉽게 파악할 수 있도록 합니다.
*   **실생활 예시**: 회사에서 각 `부서`별로 `평균 급여`, `총 급여`, `직원 수`를 알고 싶을 때.
    ```python
    import pandas as pd
    employee_salary = {'직원명': ['A', 'B', 'C', 'D', 'E'],
                       '부서': ['영업', '마케팅', '영업', '개발', '마케팅'],
                       '급여': [5000, 6000, 5500, 7000, 6200]}
    df_salary = pd.DataFrame(employee_salary)

    print("원본 직원 급여 데이터:\n", df_salary)

    # 부서별로 그룹화하고 여러 집계 함수를 적용하며 결과 열 이름 지정
    grouped_stats = df_salary.groupby('부서').agg(
        평균_급여=('급여', 'mean'),
        총_급여=('급여', 'sum'),
        직원_수=('직원명', 'size') # 'size'는 그룹 내 원소 개수를 반환
    )
    print("\n부서별 통계:\n", grouped_stats)
    ```

#### 6. Pivot (피벗)
*   **개념**: 데이터를 재구성하여 특정 열을 행 인덱스로, 다른 열을 컬럼으로 만들고 값을 채울 때, 각 `(행, 열)` 조합에 단 하나의 값만 존재해야 합니다. 만약 여러 값이 존재할 경우, 반드시 `aggfunc` (집계 함수: `sum`, `mean`, `first` 등)를 지정하여 이 값들을 어떻게 요약할지 명시해야 합니다.
*   **실생활 예시**: 월별 `상품별 매출` 데이터가 있을 때, `월`을 행으로, `상품_카테고리`를 열로 하여 각 카테고리의 `총 판매량`을 보고 싶을 때. 이때, 한 달에 동일 카테고리 상품이 여러 번 팔릴 수 있으므로 `aggfunc`를 사용해야 합니다.
    ```python
    import pandas as pd
    sales_data = {'월': ['1월', '1월', '2월', '2월', '1월'],
                  '상품_카테고리': ['전자제품', '의류', '전자제품', '의류', '전자제품'],
                  '상품명': ['노트북', '티셔츠', '마우스', '바지', '웹캠'],
                  '판매량': [10, 20, 15, 25, 12]}
    df_sales = pd.DataFrame(sales_data)

    print("원본 판매 데이터:\n", df_sales)

    # '월'과 '상품_카테고리' 조합에 여러 '판매량' 값이 있을 수 있으므로 aggfunc='sum' 사용
    pivot_monthly_category_sales = df_sales.pivot_table(
        index='월',
        columns='상품_카테고리',
        values='판매량',
        aggfunc='sum' # 1월 전자제품: 노트북(10) + 웹캠(12) = 22
    ).fillna(0) # 값이 없는 셀은 0으로 채움
    print("\n월별 상품 카테고리별 총 판매량 (aggfunc='sum' 사용):\n", pivot_monthly_category_sales)
    ```

---

## Slide 37

*오류 발생으로 해설을 생성하지 못했습니다.*

---

## Slide 38

### 1. 숫자 데이터 안전하게 변환하기 (Coerce numerics safely)

**핵심 개념:**
데이터 분석 과정에서 '가격', '수량' 등 숫자여야 할 데이터가 불필요한 문자(예: 쉼표, 통화 기호, '원', '개')나 의미 없는 텍스트('N/A', '알 수 없음')와 섞여 문자열 형태로 저장되는 경우가 많습니다. `pd.to_numeric` 함수를 `errors="coerce"` 옵션과 함께 사용하면, 이러한 '더러운' 문자열을 자동으로 숫자로 변환합니다. 변환할 수 없는 값은 `NaN`(Not a Number)으로 처리하여 분석 가능한 형태로 정제합니다.

**왜 중요한가요?**
*   **수학적 연산 활성화:** 숫자로 변환해야만 합계, 평균, 사칙연산 등 기본적인 통계 계산은 물론, 편차, 표준화 등 고급 수학적 분석을 수행할 수 있습니다.
*   **데이터 정제 및 스케일링:** 이상치 처리(예: winsorization)나 머신러닝 모델을 위한 데이터 스케일링 등 전처리 작업의 필수적인 전 단계입니다.
*   **문제 데이터 명시:** 잘못된 입력값을 `NaN`으로 명확히 표시하여, 어떤 데이터가 숫자로 변환하는 데 실패했는지 쉽게 식별하고 추후 처리할 수 있도록 돕습니다.

**실생활 예시:**
당신이 중고차 판매 데이터를 분석하는 데이터 과학자라고 가정해 봅시다. `price` 컬럼에는 판매가 정보가 들어있지만, 사람들이 직접 입력한 데이터라 다음과 같이 다양한 형식의 문자열이 섞여 있을 수 있습니다.
*   `"1,500만원"`
*   `"2300"`
*   `"3500만"`
*   `"가격협의"`
*   `"$18,000"`

이대로는 평균 판매가를 계산하거나 가격 분포를 분석할 수 없습니다. 이때 `df["price"] = pd.to_numeric(df["price"], errors="coerce")`를 적용하면:
*   `"2300"`은 `2300`으로,
*   `"1,500만원"`은 `NaN`으로 (숫자 외 '만원' 문자 때문에),
*   `"가격협의"`도 `NaN`으로 변환됩니다.
*   **Tip:** `errors="coerce"`만으로는 모든 이질적인 형식을 처리하기 어렵습니다. 더 높은 변환 성공률을 위해서는 `df["price"].str.replace('[만원,$ ]', '', regex=True).str.replace(',', '')`와 같이 정규 표현식을 사용해 통화 기호, 쉼표, 단위('만원') 등을 미리 제거하는 전처리 과정을 거친 후 `pd.to_numeric`을 적용하는 것이 좋습니다. 이렇게 하면 `1,500만원`이나 `$18,000` 같은 값도 성공적으로 `1500`이나 `18000`으로 숫자로 변환할 수 있습니다.

### 2. 범주형 데이터 활용하기 (Use categoricals for keys)

**핵심 개념:**
`category` 데이터 타입은 고정된 몇 가지 고유한 값(범주)을 반복적으로 가지는 데이터를 효율적으로 저장하고 처리하기 위한 Pandas의 특수 데이터 타입입니다. 문자열 값을 직접 저장하는 대신, 내부적으로 이러한 문자열을 고유한 정수 코드에 매핑하고, 실제 데이터에는 이 정수 코드만을 저장함으로써 메모리 사용량을 획기적으로 줄이고 특정 연산 속도를 향상시킵니다.

**왜 중요한가요?**
*   **메모리 절약:** '서울', '부산', '대구'와 같이 반복되는 문자열이 데이터셋에 수십만 번 나타날 경우, 각 문자열을 개별적으로 저장하는 것보다 '서울'을 0, '부산'을 1 등으로 인코딩하고 숫자 코드만 저장하는 것이 훨씬 적은 메모리를 사용합니다. 이는 대규모 데이터셋 처리 시 특히 중요합니다.
*   **연산 속도 향상:** `groupby()`, `join()` 등의 그룹화/병합 연산에서 긴 문자열을 비교하는 대신 짧은 정수 코드를 비교하므로 훨씬 빠르게 처리됩니다. 이는 복잡한 데이터 분석 작업의 효율성을 높입니다.
*   **의미 전달:** 데이터의 '차원(Dimension)' 특성을 명확히 하여 분석 의도를 표현하기 좋습니다. 예를 들어, `성별`, `지역`, `상품 카테고리`와 같이 고정된 선택지가 있는 컬럼에 적합합니다.

**실생활 예시:**
당신이 전국에서 수집된 고객 주문 데이터를 분석한다고 가정해 봅시다. `city` 컬럼에는 수백만 개의 주문 기록이 있지만, 실제 도시의 종류는 '서울', '부산', '대구', '인천', '광주' 등 몇십 개 정도로 한정되어 있습니다.
만약 `city` 컬럼이 일반 `object`(문자열) 타입이라면, "서울"이라는 2글자 문자열이 주문 수만큼 반복적으로 메모리에 저장될 것입니다. 이는 매우 비효율적입니다.

이것을 `df["city"] = df["city"].astype("category")`로 변환하면:
Pandas는 내부적으로 다음과 같은 매핑 테이블을 만듭니다.
`{'서울': 0, '부산': 1, '대구': 2, '인천': 3, ...}`
그리고 실제 `city` 컬럼에는 이 숫자 코드(`0, 0, 1, 0, 2, 1, ...`)만 저장합니다.
*   **메모리 절약 효과:** '서울'이라는 문자열 자체는 한 번만 저장하고, 실제 데이터에는 해당 '서울'에 해당하는 숫자 코드만 저장되므로, 메모리 사용량이 크게 줄어듭니다.
*   **`groupby` 속도 향상:** `df.groupby('city')['total_sales'].sum()`과 같은 연산을 할 때, 문자열 비교 대신 정수 비교를 수행하여 계산 속도가 현저히 빨라집니다.
*   **주의 사항 (Gotcha):** 서로 다른 두 DataFrame을 병합(merge)할 때, `category` 타입의 키 컬럼이 가지고 있는 범주(categories) 집합이 서로 다르면 병합이 제대로 되지 않거나 예상치 못한 결과를 줄 수 있습니다. 예를 들어, `df1`의 `city` 범주가 `{'서울', '부산'}`이고, `df2`의 `city` 범주가 `{'서울', '인천'}`이라면 직접적인 병합이 어려울 수 있습니다. 이럴 때는 두 컬럼의 범주 집합을 일치시키거나, 잠시 `object` 타입으로 변경한 후 병합하는 등의 추가 작업이 필요합니다.

### 3. 견고한 날짜/시간 파싱 (Datetime parsing (robust))

**핵심 개념:**
데이터 분석에서 날짜와 시간 정보는 매우 중요하지만, `2023-10-27`, `10/27/2023`, `27-Oct-2023 14:30:00`, `2023-10-27T05:30:00Z` 등 다양한 형식과 타임존으로 제공되는 경우가 많습니다. `pd.to_datetime` 함수는 이러한 이질적인 타임스탬프 문자열을 Pandas의 `datetime` 객체로 변환하고, `utc=True` 옵션을 통해 모든 시간을 표준 시간대인 UTC(협정 세계시)로 통일하여 처리할 수 있도록 돕습니다.

**왜 중요한가요?**
*   **신뢰할 수 있는 시계열 분석:** 모든 시간을 UTC로 통일함으로써 일광 절약 시간제(DST) 변경으로 인한 혼란이나 시간대 차이로 발생하는 오류를 방지하고, 정확한 시계열 분석(예: 리샘플링, 이동 평균 계산, 특정 이벤트 발생 시간 비교)을 가능하게 합니다.
*   **시간대 독립적인 비교:** 서로 다른 지역에서 수집된 데이터를 비교하거나 병합할 때, 각 데이터의 원본 시간대가 달라도 UTC 기준으로 비교하여 정확한 순서와 시간 간격을 보장합니다.

**실생활 예시:**
당신이 전 세계에 설치된 IoT 센서에서 실시간으로 온도 데이터를 수집하고 있다고 가정해 봅시다. `ts` (timestamp) 컬럼에는 각 센서가 데이터를 기록한 시간이 문자열 형태로 저장되어 있습니다.
*   미국 캘리포니아의 센서: `2023-10-26 14:00:00 PST`
*   대한민국 서울의 센서: `2023-10-27 06:00:00 KST`
*   영국 런던의 센서: `2023-10-26 22:00:00 BST`
*   어떤 센서는 타임존 정보 없이 `2023/10/26 18:00:00`과 같은 형식으로 데이터를 보낼 수도 있습니다.

이대로는 정확한 시간에 따른 온도 변화 추이를 분석하거나, 특정 시점에 전 세계 모든 센서의 평균 온도를 계산하기 어렵습니다.
`df["ts"] = pd.to_datetime(df["ts"], errors="coerce", utc=True)`를 사용하면:
1.  모든 문자열 타임스탬프가 Pandas의 `datetime` 객체로 변환됩니다.
2.  `utc=True` 옵션 덕분에, Pandas는 가능한 경우 명시된 타임존을 고려하여 모든 시간을 UTC 기준으로 변환합니다.
    *   `2023-10-26 14:00:00 PST` (UTC-8)는 `2023-10-26 22:00:00+00:00`으로,
    *   `2023-10-27 06:00:00 KST` (UTC+9)는 `2023-10-26 21:00:00+00:00`으로,
    *   `2023-10-26 22:00:00 BST` (UTC+1)는 `2023-10-26 21:00:00+00:00`으로 변환됩니다.
*   **결과:** 모든 `ts` 컬럼의 값이 `+00:00` (UTC) 타임존이 붙은 `datetime` 객체로 통일되어, 이제 어떤 센서의 데이터든 시간대 혼란 없이 정확한 시간 순서로 정렬하고 분석할 수 있게 됩니다.
*   **Tip:** 만약 원본 데이터에 타임존 정보가 없는 경우 (`2023/10/26 18:00:00`처럼), `pd.to_datetime`은 이를 '타임존 정보가 없는' 시간으로 처리합니다. 이 경우, 먼저 `df["ts"].dt.tz_localize('Asia/Seoul')`와 같이 원본 시간대를 지정하여 '지역화'한 다음, `df["ts"].dt.tz_convert('UTC')`를 사용하여 UTC로 명확히 변환하는 것이 가장 정확하고 안전합니다.

---

## Slide 39

## 핵심 개념 및 실생활 예시

### 1. Exact / Subset-based 중복 제거 (Dedup)

*   **핵심 개념:** 데이터프레임에서 특정 열(들)의 조합이 완전히 동일한 행이 여러 개 있을 때, 이 중 하나의 행만 남기고 나머지 중복된 행을 제거하는 기법입니다. 이는 특정 기준(예: 사용자 ID와 타임스탬프)에 따라 각 고유한 '키' 조합에 대해 단 하나의 레코드만 존재하도록 강제합니다.
*   **적용 이유:**
    *   KPI (핵심 성과 지표) 계산 시 이중 계산을 방지하여 정확한 통계를 얻을 수 있습니다. 예를 들어, 특정 이벤트 발생 횟수를 셀 때 중복된 기록이 있다면 실제보다 과장된 수치를 얻게 됩니다.
    *   머신러닝 모델 학습 시 '레이블 누출(label leakage)'을 방지합니다. 중복된 데이터가 훈련 세트와 테스트 세트에 분산되면 모델이 실제 데이터의 패턴을 학습하기보다는 단순히 중복된 정보를 기억하게 될 수 있습니다.
*   **팁:** `drop_duplicates` 함수는 기본적으로 첫 번째 중복 행을 남기지만, `keep='last'`를 사용하여 마지막 중복 행을 남기거나, 사전에 `sort_values()`를 사용하여 원하는 기준(예: 최신 데이터)으로 정렬한 후 중복 제거를 수행하여 어떤 행을 남길지 명확하게 제어할 수 있습니다.

*   **실생활 예시:**
    여러분은 온라인 쇼핑몰의 데이터 분석가입니다. 고객이 상품을 구매할 때마다 주문 데이터가 `orders` 테이블에 기록됩니다. 그런데 가끔 인터넷 연결이 불안정하거나 사용자가 구매 버튼을 여러 번 클릭하는 바람에 동일한 `user_id`와 `order_timestamp`를 가진 주문 기록이 여러 개 생성되는 경우가 있습니다. 만약 이 중복된 데이터들을 제거하지 않고 '일별 총 주문 건수'나 '총 매출액'을 계산한다면, 실제보다 훨씬 부풀려진 수치가 나올 것입니다.

    이때 `df.drop_duplicates(subset=["user_id", "order_timestamp"])`와 같은 방식으로 `user_id`와 `order_timestamp`가 동일한 모든 행 중에서 하나만 남겨 정확한 주문 건수를 집계할 수 있습니다. 이렇게 하면 한 고객이 특정 시간에 한 번의 구매 행위를 통해 생성된 주문은 단일 레코드로 처리되어, 정확한 판매 지표를 얻고 향후 고객 행동 분석이나 마케팅 전략 수립에 오차가 생기는 것을 방지합니다.

### 2. 정규화된 텍스트를 통한 유사 중복 제거 (Near-dup by normalized text)

*   **핵심 개념:** 텍스트 데이터의 표기상 차이(대소문자, 공백, 특수문자 등)로 인해 실제로는 같은 의미인데 다르게 보이는 '유사 중복'을 처리하는 기법입니다. 텍스트를 일관된 형식(정규화된 형태)으로 변환한 후 중복을 제거합니다.
*   **적용 이유:**
    *   서로 다른 시스템에서 입력되거나 수동 입력 과정에서 발생하는 오타, 표기법 차이(예: "삼성전자", "삼성 전자", "SAMSUNG 전자")로 인해 발생하는 데이터 불일치를 해소합니다.
    *   '퍼지 매칭(Fuzzy Matching)'과 같은 복잡하고 느린 기법 대신, 간단한 텍스트 정규화만으로도 효율적으로 유사 중복을 제거할 수 있습니다.
*   **주의사항 (Gotcha):** 악센트가 있는 문자(`café` vs `cafe`)나 정식 명칭과 약어(`International Business Machines` vs `IBM`) 등 더욱 복잡한 유사 중복의 경우, 단순히 대소문자 변환이나 공백 제거를 넘어 `unicodedata.normalize("NFKD")`와 같은 방법을 사용하거나 추가적인 텍스트 대체 규칙을 적용해야 할 수 있습니다.

*   **실생활 예시:**
    여러분은 회사 CRM(고객 관계 관리) 시스템의 데이터를 관리하고 있습니다. 고객 정보에는 '회사명' 필드가 있는데, 여러 영업사원이 각자의 방식대로 회사명을 입력하여 "ABC Corporation", "ABC corp.", "abc corporation", "A.B.C. Corporation" 등 다양한 형태로 동일한 회사를 지칭하는 기록들이 존재합니다. 이 상태로는 특정 회사에 대한 모든 고객 기록을 통합하거나, 해당 회사의 총 구매액을 정확하게 집계하기 어렵습니다.

    이때, `key = df["name"].str.strip().str.lower().str.replace(r'[.,]', '', regex=True)`와 같이 회사명 컬럼의 문자열에서 앞뒤 공백을 제거하고, 모든 문자를 소문자로 변환하며, 마침표(.)나 쉼표(,) 같은 불필요한 특수문자를 제거하는 정규화 과정을 거칩니다. 이렇게 하면 위 예시의 모든 회사명은 `abc corporation`이라는 하나의 '정규화된 키'로 통일됩니다. 이제 이 정규화된 키를 사용하여 중복된 회사 기록을 찾아 제거하면, 실제로는 하나의 회사에 대한 정보를 여러 개로 분리하여 관리하는 문제를 해결하고, 각 회사에 대한 통합적인 뷰를 얻을 수 있습니다.

### 3. Winsorize를 통한 이상치 처리 (Winsorize via Quantile Clipping)

*   **핵심 개념:** 데이터 분포의 극단적인 값(이상치, Outlier)을 삭제하는 대신, 특정 분위수(quantile)에 해당하는 값으로 대체하여 데이터의 범위(variance)를 안정화시키는 기법입니다. 예를 들어, 하위 1% 값은 1% 분위수 값으로, 상위 1% 값은 99% 분위수 값으로 바꾸는 방식입니다.
*   **적용 이유:**
    *   이상치는 평균, 표준편차와 같은 통계량이나 선형 모델의 결과에 큰 영향을 미쳐 왜곡을 발생시킬 수 있습니다. 윈서라이징은 이러한 극단값의 영향을 줄여 모델과 통계의 '견고성(Robustness)'을 높여줍니다.
    *   데이터를 삭제하는 것과 달리, 모든 행을 유지하여 데이터 손실 없이 이상치의 영향을 완화할 수 있습니다.
*   **팁:** 원본 데이터를 보존하여 (`x_raw`와 같이) 윈서라이징 전후의 변화를 비교하거나, 모델의 설명력(explainability)을 높이는 데 활용하는 것이 좋습니다.

*   **실생활 예시:**
    여러분은 한 회사의 인사 담당자로서 직원들의 월급 데이터를 분석하고 있습니다. 대부분의 직원은 합리적인 범위 내에서 월급을 받지만, CEO나 임원진 중 몇몇은 일반 직원의 월급과는 비교할 수 없을 정도로 매우 높은 보너스나 성과급을 받아 전체 월급 분포의 '꼬리'를 길게 늘어뜨리는 이상치로 존재합니다. 만약 이 이상치들을 그대로 두고 '전 직원의 평균 월급'을 계산하면, 소수의 고액 연봉자들 때문에 실제 대다수 직원이 받는 월급보다 훨씬 높은 평균치가 산출되어 현실을 왜곡할 수 있습니다.

    이때 `df["x"].quantile(0.01)` (하위 1% 값)과 `df["x"].quantile(0.99)` (상위 99% 값)을 사용하여 임계값을 정하고, `df["x"].clip(lo, hi)`를 적용하여 윈서라이징을 수행합니다. 예를 들어, 월급이 하위 1%보다 낮은 직원은 하위 1% 월급으로, 상위 99%보다 높은 직원은 상위 99% 월급으로 값을 대체하는 것입니다. 이렇게 하면 이상치로 인한 평균값의 왜곡을 줄여, 전체 직원 월급 분포를 더 현실적으로 파악하고, 이를 기반으로 한 HR 정책 수립이나 예산 책정 시 오류를 최소화할 수 있습니다. 데이터를 삭제하지 않으므로 모든 직원의 정보는 유지됩니다.

---

## Slide 40

## 데이터 형태 변경: Wide ↔ Long & Explode

이번 슬라이드는 데이터를 분석하고 시각화하기 쉬운 형태로 변환하는 세 가지 핵심 기법을 다룹니다. 특히 Pandas 라이브러리에서 매우 유용하게 사용되는 `melt()`, `pivot_table()`, `explode()` 함수에 대해 자세히 알아보겠습니다.

---

### 1. Wide 데이터프레임을 Long 데이터프레임으로 (df.melt())

**핵심 개념:**
`df.melt()` 함수는 "Wide" 형식의 데이터를 "Long" 형식으로 변환합니다. 여러 개의 컬럼에 걸쳐 분산되어 있는 값들을 하나의 컬럼으로 모으고, 원래 컬럼의 이름을 담는 새로운 컬럼을 만듭니다. 이는 데이터를 'tidy'하게 만들어 분석, 시각화, 그룹화 작업에 용이하게 합니다.

**구체적인 실생활 예시:**
당신이 온라인 상점에서 월별 판매 데이터를 관리하는 사람이라고 상상해 보세요. 각 상품 (`item_id`)에 대해 1월, 2월, 3월의 판매량이 다음과 같이 Wide 형식으로 저장되어 있습니다.

**Wide 형식 데이터 (원래 데이터프레임 `df_sales`):**

| item_id | sales_jan | sales_feb | sales_mar |
| :------ | :-------- | :-------- | :-------- |
| A       | 100       | 120       | 110       |
| B       | 50        | 60        | 70        |
| C       | 200       | 180       | 220       |

만약 "가장 많이 팔린 월은 언제였을까?" 또는 "각 월별 총 판매량은 얼마일까?"와 같은 질문에 답하려면, 이 데이터를 Long 형식으로 바꾸는 것이 훨씬 편리합니다.

**`df.melt()` 적용:**
`df_sales.melt(id_vars=["item_id"], var_name="month", value_name="sales_amount")`

*   `id_vars=["item_id"]`: `item_id` 컬럼은 고유 식별자로 유지하고 싶은 컬럼입니다.
*   `var_name="month"`: `sales_jan`, `sales_feb` 등의 원래 컬럼 이름들이 새로운 `month`라는 컬럼에 담깁니다.
*   `value_name="sales_amount"`: `sales_jan`, `sales_feb` 컬럼의 실제 값들이 새로운 `sales_amount`라는 컬럼에 담깁니다.

**Long 형식 데이터 (변환 후):**

| item_id | month     | sales_amount |
| :------ | :-------- | :----------- |
| A       | sales_jan | 100          |
| B       | sales_jan | 50           |
| C       | sales_jan | 200          |
| A       | sales_feb | 120          |
| B       | sales_feb | 60           |
| C       | sales_feb | 180          |
| A       | sales_mar | 110          |
| B       | sales_mar | 70           |
| C       | sales_mar | 220          |

이제 이 Long 형식 데이터로 "월별 총 판매량"을 `df_long.groupby('month')['sales_amount'].sum()`처럼 쉽게 계산할 수 있습니다.

**Tip:** `value_vars` 인수를 사용하면 특정 컬럼만 선택하여 melt 할 수 있습니다. 예를 들어, `sales_feb`와 `sales_mar`만 보고 싶다면 `value_vars=["sales_feb", "sales_mar"]`를 추가하면 됩니다.

---

### 2. Long 데이터프레임을 Wide 데이터프레임으로 (df.pivot_table())

**핵심 개념:**
`df.pivot_table()` 함수는 Long 형식의 데이터를 다시 Wide 형식의 매트릭스로 변환합니다. 특정 컬럼의 고유 값들을 새로운 컬럼으로 만들고, 다른 컬럼의 값들을 그 새로운 컬럼의 셀에 채워 넣습니다. 이 과정에서 한 셀에 여러 값이 들어가게 될 경우, `aggfunc` (집계 함수)를 사용하여 충돌을 해결해야 합니다.

**구체적인 실생활 예시:**
위에서 `melt`를 통해 얻은 월별 판매량 데이터 (`df_long`)를 다시 `item_id`를 기준으로 월별 판매량이 컬럼으로 나타나는 Wide 형식으로 되돌리고 싶다고 가정해 봅시다.

**Long 형식 데이터 (원래 데이터프레임 `df_long`):**

| item_id | month     | sales_amount |
| :------ | :-------- | :----------- |
| A       | sales_jan | 100          |
| A       | sales_feb | 120          |
| A       | sales_mar | 110          |
| B       | sales_jan | 50           |
| ...     | ...       | ...          |

**`df.pivot_table()` 적용:**
`df_long.pivot_table(index="item_id", columns="month", values="sales_amount", aggfunc="first").reset_index()`

*   `index="item_id"`: `item_id` 컬럼의 고유 값들이 새로운 데이터프레임의 인덱스(행)가 됩니다.
*   `columns="month"`: `month` 컬럼의 고유 값들(`sales_jan`, `sales_feb`, `sales_mar`)이 새로운 데이터프레임의 컬럼이 됩니다.
*   `values="sales_amount"`: `sales_amount` 컬럼의 값들이 새로운 컬럼(`sales_jan`, `sales_feb`, `sales_mar`)의 셀에 채워집니다.
*   `aggfunc="first"`: 만약 특정 `item_id`와 `month` 조합에 해당하는 `sales_amount` 값이 여러 개 있을 경우, 그 중 첫 번째 값을 선택하라는 의미입니다. 여기서는 각 조합이 고유하므로 큰 문제는 없지만, 중복이 발생할 경우 이 인수가 중요해집니다.
*   `.reset_index()`: `pivot_table`의 결과는 `item_id`가 인덱스로 설정되는데, 이를 일반 컬럼으로 되돌립니다.

**Wide 형식 데이터 (변환 후):**

| item_id | sales_jan | sales_feb | sales_mar |
| :------ | :-------- | :-------- | :-------- |
| A       | 100       | 120       | 110       |
| B       | 50        | 60        | 70        |
| C       | 200       | 180       | 220       |

**Gotcha (주의사항):**
만약 `item_id` A가 `sales_jan`에 대한 `sales_amount`를 두 번 가지고 있다면 (예: `item_id` A, `month` `sales_jan`, `sales_amount` 100; `item_id` A, `month` `sales_jan`, `sales_amount` 105), `aggfunc`를 지정하지 않으면 오류가 발생합니다. 이 경우 `aggfunc="first"`, `aggfunc="max"`, `aggfunc="mean"` 또는 사용자 정의 함수를 사용하여 어떻게 여러 값을 하나의 셀로 집계할지 명시해야 합니다.

---

### 3. 리스트와 같은 요소를 개별 행으로 확장 (df.explode())

**핵심 개념:**
`df.explode()` 함수는 데이터프레임의 특정 컬럼에 리스트(또는 배열) 형태의 값을 포함하는 경우, 각 리스트 요소를 개별 행으로 확장하여 새로운 행들을 생성합니다. 다른 컬럼의 값들은 복제됩니다.

**구체적인 실생활 예시:**
당신이 영화 추천 서비스를 개발하고 있다고 가정해 봅시다. 각 영화는 여러 장르 태그를 가질 수 있으며, 이 정보가 다음과 같이 저장되어 있습니다.

**원래 데이터프레임 `df_movies`:**

| movie_id | title         | genres                      | rating |
| :------- | :------------ | :-------------------------- | :----- |
| 1        | The Matrix    | ['Action', 'Sci-Fi']        | 8.7    |
| 2        | Inception     | ['Sci-Fi', 'Thriller']      | 8.8    |
| 3        | Forest Gump   | ['Drama', 'Romance', 'War'] | 8.8    |
| 4        | Interstellar  | ['Sci-Fi', 'Drama']         | 8.6    |

만약 "어떤 장르가 가장 인기가 많을까?" 또는 "각 장르별 평균 평점은 얼마일까?"와 같은 질문에 답하고 싶다면, 현재의 `genres` 컬럼은 분석하기 어렵습니다. 하나의 셀에 여러 장르가 있기 때문입니다. 이럴 때 `explode()`가 유용합니다.

**`df.explode()` 적용:**
`df_movies.explode("genres", ignore_index=True)`

*   `"genres"`: 리스트를 포함하는 `genres` 컬럼을 지정합니다.
*   `ignore_index=True`: 확장된 데이터프레임의 인덱스를 재설정하여 새로운 고유 인덱스를 부여합니다.

**변환 후 데이터:**

| movie_id | title         | genres   | rating |
| :------- | :------------ | :------- | :----- |
| 1        | The Matrix    | Action   | 8.7    |
| 1        | The Matrix    | Sci-Fi   | 8.7    |
| 2        | Inception     | Sci-Fi   | 8.8    |
| 2        | Inception     | Thriller | 8.8    |
| 3        | Forest Gump   | Drama    | 8.8    |
| 3        | Forest Gump   | Romance  | 8.8    |
| 3        | Forest Gump   | War      | 8.8    |
| 4        | Interstellar  | Sci-Fi   | 8.6    |
| 4        | Interstellar  | Drama    | 8.6    |

이제 이 데이터를 가지고 `df_exploded.groupby('genres')['rating'].mean()`처럼 각 장르별 평균 평점을 쉽게 계산할 수 있습니다.

**Tip:** `explode()` 후에는 `genres`와 같은 태그 컬럼을 기준으로 다른 조회 테이블(lookup table)과 조인하여 장르의 상세 정보(예: 장르별 인기 배우, 제작사 등)를 추가하고, 이를 바탕으로 더 복잡한 특성(feature)을 생성할 수 있습니다. 예를 들어, 각 영화가 속한 장르들의 평균 평점을 합산하거나, 특정 장르가 포함된 영화의 수를 세는 등의 작업이 가능해집니다.

---

---

## Slide 41

## 핵심 개념 상세 설명: 데이터 위생, 텍스트 전처리, 날짜/시간 처리

이번 슬라이드에서는 데이터 분석의 정확성과 효율성을 높이는 세 가지 중요한 데이터 처리 기법에 대해 알아봅니다. 바로 `pd.merge`를 활용한 조인 데이터의 무결성 유지, 텍스트 데이터의 표준화, 그리고 날짜/시간 데이터의 올바른 파싱 및 활용입니다.

---

### 1. 조인 데이터 위생: 유효성 검사 및 감사 (`Join Hygiene: Validate & Audit`)

**핵심 개념:** 데이터를 병합(Join)할 때 예상치 못한 중복이나 누락이 발생하지 않도록 사전에 관계를 검증하고, 병합 결과를 감사하여 데이터 무결성을 확보하는 것입니다.

**무엇인가요? (What?)**
Pandas의 `pd.merge` 함수에서 `validate`와 `indicator` 옵션을 사용하는 것을 말합니다.
*   `validate`: 두 데이터프레임의 키(key) 간 예상되는 관계(카디널리티, cardinality)를 명시하여, 해당 관계가 지켜지지 않으면 에러를 발생시킵니다.
    *   `'one_to_one'`: 왼쪽(A)의 각 키가 오른쪽(B)의 최대 한 키와 매칭되고, 그 반대도 마찬가지일 때.
    *   `'one_to_many'`: 왼쪽(A)의 각 키가 오른쪽(B)의 최대 한 키와 매칭되지만, 오른쪽(B)의 키는 여러 왼쪽(A) 키와 매칭될 수 있을 때. (가장 흔한 시나리오)
    *   `'many_to_one'`: 위와 반대.
    *   `'many_to_many'`: 양쪽 키가 여러 번 매칭될 수 있을 때.
*   `indicator=True`: 병합된 결과에 `_merge`라는 새로운 열을 추가하여 각 행이 어느 데이터프레임에서 왔는지 (`left_only`, `right_only`, `both`) 알려줍니다.

**왜 중요한가요? (Why?)**
`validate`는 예상치 못한 **행 증식(fanout)**이나 **데이터 손실**을 미연에 방지합니다. 예를 들어, `one_to_one` 관계여야 할 데이터에 중복 키가 있으면 `validate`가 에러를 띄워 문제를 발견할 수 있게 합니다. `indicator`는 병합 후 어떤 데이터가 매칭되지 않았는지 쉽게 파악하여 데이터의 누락 여부를 감사(audit)하는 데 도움을 줍니다.

**구체적인 실생활 예시:**
당신이 온라인 쇼핑몰의 데이터 분석가라고 가정해 봅시다.
1.  **`고객_정보` 데이터프레임 (df_customers):** `customer_id` (고유값), `이름`, `주소`
2.  **`주문_내역` 데이터프레임 (df_orders):** `order_id` (고유값), `customer_id`, `주문_날짜`, `총_금액`

이제 각 고객의 주문 내역을 합쳐서 보려고 합니다.
*   **시나리오 1: `validate='one_to_many'` 사용하기**
    *   한 명의 고객(`customer_id`)은 여러 개의 주문을 할 수 있지만, `df_customers`에는 각 `customer_id`가 단 하나만 존재해야 합니다. 반대로 `df_orders`에는 동일한 `customer_id`가 여러 번 나타날 수 있습니다.
    *   따라서 `df_customers` (왼쪽)와 `df_orders` (오른쪽)를 `customer_id`를 기준으로 병합할 때, 올바른 관계는 `one_to_many`입니다.
    *   만약 `df_customers`에 실수로 동일한 `customer_id`가 두 번 입력된 행이 있다고 해봅시다. 이때 `validate='one_to_many'`를 사용하면, Pandas는 `df_customers`에서 `customer_id`가 고유하지 않다는 것을 감지하고 에러를 발생시킵니다. 덕분에 잘못된 데이터가 조용히 병합되어 `customer_id`당 주문 내역이 두 배로 뻥튀기되는 **"숨겨진 행 증식" (silent row multiplication)**을 방지할 수 있습니다.
    ```python
    # df_customers (가정): customer_id가 중복된 행이 있다고 가정
    # df_orders

    try:
        merged_df = pd.merge(df_customers, df_orders, on='customer_id', how='left', validate='one_to_many')
        print("성공적으로 병합되었습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")
        print("df_customers에 customer_id 중복이 있을 수 있습니다. 확인해주세요.")
    ```

*   **시나리오 2: `indicator=True`를 이용한 '안티 조인' (Anti-join)으로 미매칭 데이터 찾기**
    *   새로 가입했지만 아직 한 번도 주문하지 않은 고객을 찾아 마케팅 캠페인을 진행하고 싶다고 가정합시다.
    *   `df_customers` (왼쪽)와 `df_orders` (오른쪽)를 `how='left'`로 병합하고 `indicator=True`를 사용합니다.
    ```python
    merged_with_indicator = pd.merge(df_customers, df_orders, on='customer_id', how='left', indicator=True)

    # _merge 컬럼이 'left_only'인 경우: 고객 정보는 있지만 주문 내역이 없는 경우
    new_customers_no_orders = merged_with_indicator[merged_with_indicator['_merge'] == 'left_only']

    print("\n아직 주문하지 않은 신규 고객 목록:")
    print(new_customers_no_orders[['customer_id', '이름']].drop_duplicates())
    ```
    이처럼 `_merge == 'left_only'` 조건으로 필터링하면, 왼쪽 데이터프레임(`df_customers`)에는 존재하지만 오른쪽 데이터프레임(`df_orders`)에는 매칭되는 키가 없는 행들을 쉽게 찾아낼 수 있습니다. 이를 **안티 조인(Anti-join)**이라고 부르며, 데이터 누락을 확인하거나 특정 조건에 맞지 않는 데이터를 식별하는 데 매우 유용합니다.

---

### 2. 텍스트 데이터 정리 (`Text Cleanup`)

**핵심 개념:** 텍스트 데이터를 분석에 적합하도록 일관된 형태로 표준화하는 과정입니다.

**무엇인가요? (What?)**
슬라이드에 제시된 세 가지 주요 단계는 다음과 같습니다.
1.  `df["title"].str.normalize('NFKC')`: 유니코드 문자열을 표준화합니다. 특히 'NFKC'는 시각적으로 비슷하지만 내부적으로 다르게 인코딩될 수 있는 문자(예: 반각/전각 문자, 결합 문자)를 통일하는 데 효과적입니다.
2.  `.str.strip()`: 문자열의 양 끝에 있는 공백(띄어쓰기, 탭, 개행 문자 등)을 제거합니다.
3.  `.str.lower()`: 문자열의 모든 대문자를 소문자로 변환하여 대소문자 구분을 없앱니다.

**왜 중요한가요? (Why?)**
텍스트 데이터는 다양한 형식과 오타, 불규칙한 입력으로 인해 지저분한 경우가 많습니다. 이러한 전처리 과정을 거치면:
*   **매칭률 증가:** 서로 다른 표기 방식 때문에 같은 단어가 다르게 인식되는 것을 막아, 조인(join)이나 중복 제거(deduplication) 시 매칭 성공률을 높입니다.
*   **벡터화 안정화:** 머신러닝 모델의 텍스트 벡터화(Text Vectorization) 단계에서 일관된 입력을 제공하여 모델의 성능을 향상시킵니다.
*   **검색 및 필터링 정확도 향상:** 사용자가 검색하는 쿼리와 데이터의 형식이 통일되어 검색 정확도를 높입니다.

**구체적인 실생활 예시:**
당신이 도서 판매 플랫폼의 데이터베이스 관리자라고 가정해 봅시다. `도서_제목` 컬럼에 다음과 같은 다양한 형태의 입력이 있다고 상상해 보세요.

| `raw_title`              |
| :----------------------- |
| ` 　파이썬 기초  `         |
| ` 파이썬 기초 `          |
| `python 기초`            |
| `Python 기초`            |
| `파이썬-기초`            |
| `파이썬—기초`            |
| `카페`                     |
| `ㅋㅏ페`                   |

이제 이 제목들을 표준화하여 정확하게 검색하고 분석할 수 있도록 전처리해 봅시다.
```python
import pandas as pd

data = {'raw_title': [
    ' 　파이썬 기초  ', # 전각 공백 포함, 후행 공백
    ' 파이썬 기초 ',  # 선행/후행 공백
    'python 기초',   # 소문자
    'Python 기초',   # 대문자
    '파이썬-기초',    # 하이픈
    '파이썬—기초',    # 전각 하이픈
    '카페',          # 일반 한글
    'ㅋㅏ페',        # 분리된 한글
    'Hello World!',  # 구두점
    'Hello  World'   # 중간에 여러 공백
]}
df_books = pd.DataFrame(data)

# 텍스트 정리 과정
df_books['cleaned_title'] = (
    df_books['raw_title']
    .str.normalize('NFKC')  # 유니코드 표준화 (전각 공백, 하이픈, 분리 한글 등)
    .str.strip()           # 양 끝 공백 제거
    .str.lower()           # 소문자 변환
    .str.replace(r'[!?]', '', regex=True) # Tip: 구두점 제거
    .str.replace(r'\s+', ' ', regex=True) # Tip: 중간에 여러 공백을 하나로
)

print(df_books[['raw_title', 'cleaned_title']])
```

**결과:**

| `raw_title`              | `cleaned_title`      |
| :----------------------- | :------------------- |
| ` 　파이썬 기초  `         | `파이썬 기초`        |
| ` 파이썬 기초 `          | `파이썬 기초`        |
| `python 기초`            | `python 기초`        |
| `Python 기초`            | `python 기초`        |
| `파이썬-기초`            | `파이썬-기초`        |
| `파이썬—기초`            | `파이썬-기초`        |
| `카페`                     | `카페`               |
| `ㅋㅏ페`                   | `카페`               |
| `Hello World!`           | `hello world`        |
| `Hello  World`           | `hello world`        |

*   `normalize('NFKC')`: ' 　파이썬 기초 '의 전각 공백이 일반 공백으로, '파이썬—기초'의 전각 하이픈이 일반 하이픈으로, 'ㅋㅏ페'가 '카페'로 표준화됩니다.
*   `strip()`: 양 끝의 공백들이 제거됩니다.
*   `lower()`: 'Python 기초'가 'python 기초'로, 'Hello World!'가 'hello world!'로 소문자화됩니다.
*   **팁 (슬라이드에 추가된 부분):** `str.replace(r'[!?]', '', regex=True)`를 사용하여 제목의 구두점(`!`, `?`)을 제거하고, `str.replace(r'\s+', ' ', regex=True)`를 사용하여 중간에 불필요하게 여러 개 있는 공백을 하나의 공백으로 줄였습니다.
이 과정을 통해 ' 　파이썬 기초  ', ' 파이썬 기초 ', 'Python 기초' 등 서로 다른 원본들이 모두 '파이썬 기초' 또는 'python 기초'로 통일되어, 사용자가 어떤 방식으로 검색해도 해당 도서를 정확히 찾을 수 있게 됩니다.

---

### 3. 날짜/시간 데이터의 문제점 (`Datetime Gotchas`)

**핵심 개념:** 다양한 형태로 저장된 날짜/시간 데이터를 안전하게 파싱하고, 시간대(Time Zone)를 고려하여 국제 표준시(UTC)로 표준화하는 것입니다.

**무엇인가요? (What?)**
*   `pd.to_datetime()`: 문자열, 숫자 등 다양한 형식의 데이터를 Pandas의 datetime 객체로 변환하는 함수입니다.
*   `errors="coerce"`: 파싱에 실패한 데이터는 에러를 발생시키는 대신 `NaT` (Not a Time, 즉 유효하지 않은 시간)로 변환합니다. 이는 전체 데이터 처리 흐름을 중단하지 않고 문제성 데이터를 식별할 수 있게 합니다.
*   `utc=True`: 모든 날짜/시간 데이터를 협정 세계시(Coordinated Universal Time, UTC)로 변환합니다. 이는 전 세계적으로 통용되는 시간 표준이며, 일광 절약 시간(Daylight Saving Time) 등 지역 시간대 변화로 인한 혼란을 방지합니다.

**왜 중요한가요? (Why?)**
날짜/시간 데이터는 `2023-10-26`, `10/26/2023`, `Oct 26, 2023 14:30 EST`, `2023-10-26T19:30:00Z` 등 매우 다양한 형식으로 저장될 수 있습니다. 또한, 시간대가 명시되지 않거나 혼재되어 있으면 정확한 시간 비교나 시계열 분석이 불가능합니다. `pd.to_datetime`을 `errors="coerce"`와 `utc=True`와 함께 사용하면, 이러한 복잡성을 효율적으로 관리하고 데이터의 일관성과 정확성을 보장할 수 있습니다.

**구체적인 실생활 예시:**
당신이 글로벌 서비스의 사용자 활동 로그를 분석하는 데이터 과학자라고 가정해 봅시다. 전 세계 여러 서버에서 수집된 로그 데이터에는 `timestamp` 컬럼이 다음과 같은 다양한 형식으로 존재합니다.

| `raw_timestamp`                  |
| :------------------------------- |
| `2023-10-26 14:30:00 EST`        |
| `10/26/23 11:30 AM PST`          |
| `2023-10-26T19:30:00Z`           |
| `2023-13-01 00:00:00` (잘못된 월) |
| `invalid_time_string`            |

이 데이터를 분석하기 위해 먼저 표준화된 datetime 객체로 변환해 봅시다.
```python
import pandas as pd

data = {'raw_timestamp': [
    '2023-10-26 14:30:00 EST',  # 미국 동부 표준시
    '10/26/23 11:30 AM PST',    # 미국 태평양 표준시
    '2023-10-26T19:30:00Z',     # UTC
    '2023-13-01 00:00:00',      # 잘못된 날짜 형식
    'invalid_time_string'       # 유효하지 않은 문자열
]}
df_logs = pd.DataFrame(data)

# 날짜/시간 데이터 파싱 및 UTC 표준화
df_logs['standardized_ts'] = pd.to_datetime(
    df_logs['raw_timestamp'],
    errors='coerce', # 파싱 실패 시 NaT로 변환
    utc=True         # 모든 시간을 UTC로 변환
)

print("원시 타임스탬프와 표준화된 타임스탬프:")
print(df_logs[['raw_timestamp', 'standardized_ts']])

# Gotcha: NaT 값 감사하기
# df_logs['standardized_ts'].isna()는 NaT인 경우 True, 아닌 경우 False
# .mean()은 True 비율을 계산, 즉 NaT의 비율
missing_ts_percentage = df_logs['standardized_ts'].isna().mean() * 100
print(f"\n파싱에 실패한 타임스탬프의 비율: {missing_ts_percentage:.2f}%")

# Tip: 파싱된 datetime 객체에서 연, 주, 시 같은 특징 추출하기
# .dt accessor를 사용하여 다양한 시간 관련 속성 접근 가능
df_logs['year'] = df_logs['standardized_ts'].dt.year
df_logs['week_of_year'] = df_logs['standardized_ts'].dt.isocalendar().week # ISO 주차
df_logs['hour'] = df_logs['standardized_ts'].dt.hour
df_logs['day_of_week'] = df_logs['standardized_ts'].dt.day_name() # 요일 이름

print("\n추출된 날짜/시간 특징:")
print(df_logs[['raw_timestamp', 'standardized_ts', 'year', 'week_of_year', 'hour', 'day_of_week']])
```

**결과:**

*   `2023-10-26 14:30:00 EST` (UTC-5)는 `2023-10-26 19:30:00+00:00` (UTC)로 변환됩니다.
*   `10/26/23 11:30 AM PST` (UTC-7)는 `2023-10-26 18:30:00+00:00` (UTC)로 변환됩니다.
*   `2023-10-26T19:30:00Z` (이미 UTC)는 동일하게 `2023-10-26 19:30:00+00:00` (UTC)로 변환됩니다.
*   `2023-13-01 00:00:00` (유효하지 않은 월)과 `invalid_time_string`은 모두 `NaT`로 변환됩니다.

이제 모든 유효한 시간 데이터는 UTC로 통일되어 시간대 차이 없이 정확한 비교 및 분석이 가능해집니다. `NaT` 비율을 확인하여 데이터 품질을 감사할 수 있으며, `dt` 접근자를 통해 연, 주차, 시간, 요일 등 다양한 정보를 쉽게 추출하여 시간 기반 패턴을 분석하는 데 활용할 수 있습니다. 예를 들어, 특정 시간대나 요일에 사용자 활동이 급증하는지 등을 파악할 수 있습니다.

---

## Slide 42

## 핵심 개념 설명

### 1. 그룹별 특징 (Group-aware features: z-score, ranks, rolling)

이 섹션은 데이터를 특정 '그룹'으로 나눈 뒤, 각 그룹 내에서 데이터를 표준화하거나 순위를 매기거나 시간 경과에 따른 평균을 계산하여 새로운 특징(feature)을 생성하는 방법을 설명합니다. 이는 전체 데이터셋을 일괄적으로 처리하는 것보다 더 미묘하고 의미 있는 통찰을 제공합니다.

#### 1.1. 그룹 내 표준화 (Z-score)

*   **무엇인가요?** 데이터를 특정 그룹의 평균과 표준 편차를 사용하여 표준화하는 기법입니다. 이를 통해 각 데이터 포인트가 해당 그룹의 평균에서 얼마나 떨어져 있는지(표준 편차 단위로) 알 수 있습니다.
*   **왜 사용하나요?** 그룹별로 특성이 다른 경우, 단순히 절대적인 값을 비교하는 것은 공정하지 않을 수 있습니다. 그룹 내 표준화를 통해 서로 다른 그룹에 속한 항목들을 공정하게 비교할 수 있게 됩니다. 또한, 이상치(outlier)를 식별하는 데도 유용합니다.

*   **구체적이고 실생활에 가까운 예시:**
    *   **시나리오:** 전국에 수백 개의 매장을 가진 대형 슈퍼마켓 체인이 있다고 가정해 봅시다. 이 매장들은 도시 중심가, 교외, 소도시 등 다양한 지역에 위치해 있어 매장 규모와 잠재 고객 수가 크게 다릅니다. 특정 주에 각 매장의 '주간 매출'이 기록됩니다.
    *   **문제점:** '매장 A'가 1억 원의 매출을 올렸고, '매장 B'가 5천만 원의 매출을 올렸다면, 단순히 매장 A가 매장 B보다 "더 잘했다"고 말하기는 어렵습니다. 매장 A는 뉴욕 타임스퀘어에 있는 초대형 매장이고, 매장 B는 작은 교외 마을의 매장일 수 있기 때문입니다.
    *   **해결책 (그룹 내 Z-score):**
        1.  각 매장의 **과거 평균 매출**과 **표준 편차**를 계산합니다. (여기서 각 '매장'이 하나의 그룹이 됩니다.)
        2.  이번 주의 각 매장 매출에 대해 해당 매장의 과거 데이터(평균, 표준 편차)를 사용하여 Z-score를 계산합니다.
        3.  예시:
            *   **매장 A (뉴욕):** 과거 평균 매출 9천만 원, 표준 편차 1천만 원. 이번 주 매출 1억 원.
                Z-score = (1억 - 9천만) / 1천만 = **1.0**
            *   **매장 B (교외):** 과거 평균 매출 4천만 원, 표준 편차 5백만 원. 이번 주 매출 5천만 원.
                Z-score = (5천만 - 4천만) / 5백만 = **2.0**
        4.  **결과 해석:** 매장 B의 Z-score(2.0)가 매장 A(1.0)보다 높습니다. 이는 매장 B가 자신의 평소 실적에 비해 훨씬 더 뛰어난 성과를 냈다는 것을 의미합니다. 반면 매장 A는 평소보다 약간 더 나은 정도입니다. 이처럼 Z-score를 통해 매장 규모나 위치에 관계없이 '상대적인' 성과를 공정하게 비교할 수 있습니다.

#### 1.2. 그룹 내 순위 (Ranks)

*   **무엇인가요?** 특정 그룹 내에서 데이터 포인트를 특정 기준에 따라 정렬하고 순위를 부여하는 기법입니다.
*   **왜 사용하나요?** 그룹 내에서의 상대적인 위치를 파악하고, 최상위 또는 최하위 항목을 쉽게 식별하는 데 도움을 줍니다.

*   **구체적이고 실생활에 가까운 예시:**
    *   **시나리오:** 한 대학교에 여러 학과(그룹)가 있고, 각 학과마다 학생들이 치른 시험 점수가 있습니다.
    *   **문제점:** 경제학과에서 90점을 받은 학생과 체육학과에서 90점을 받은 학생의 상대적 학업 성취도를 직접 비교하기는 어렵습니다. 학과별로 시험의 난이도나 학생들의 전반적인 학업 수준이 다를 수 있기 때문입니다.
    *   **해결책 (그룹 내 순위):**
        1.  각 '학과'를 하나의 그룹으로 설정합니다.
        2.  각 학과 내에서 학생들의 시험 점수를 기준으로 순위를 매깁니다.
        3.  예시:
            *   **경제학과:** 학생 A (95점, 1위), 학생 B (90점, 2위), 학생 C (88점, 3위)...
            *   **체육학과:** 학생 D (92점, 1위), 학생 E (89점, 2위), 학생 F (85점, 3위)...
        4.  **결과 해석:** 이제 우리는 각 학과 내에서 누가 가장 높은 성적을 받았는지 명확하게 알 수 있습니다. 학생 A는 경제학과에서 1위이고, 학생 D는 체육학과에서 1위입니다. 이를 통해 학과 특성을 고려한 장학금 지급, 학업 우수자 선정 등 의사결정을 내릴 수 있습니다.

#### 1.3. 이동 평균 (Rolling averages)

*   **무엇인가요?** 시계열 데이터에서 특정 기간(윈도우) 동안의 평균을 계산하여 데이터의 단기적인 변동성을 완화하고 장기적인 추세나 패턴을 파악하는 기법입니다.
*   **왜 사용하나요?** 일별/주별 등 단기적인 노이즈가 심한 데이터에서 추세와 계절성(momentum and seasonality)을 파악하여 예측이나 의사결정에 더 안정적인 기준을 제공합니다.
*   **Tip:** `rolling` 연산을 수행하기 전에는 반드시 `df.sort_values`를 사용하여 `store`와 `ts` (시간) 기준으로 데이터를 올바르게 정렬해야 합니다. 또한, `min_periods`를 설정하여 초기 데이터 부족으로 인한 편향(warm-up bias)을 제어할 수 있습니다. 예를 들어, 7일 이동 평균을 계산할 때 `min_periods=1`로 설정하면 첫 6일 동안은 가용한 데이터만으로 평균을 계산하여 초반에도 값을 얻을 수 있습니다.

*   **구체적이고 실생활에 가까운 예시:**
    *   **시나리오:** 한 온라인 쇼핑몰이 매일 특정 상품의 '일일 판매량' 데이터를 가지고 있습니다.
    *   **문제점:** 일일 판매량은 특정 요일(주말), 프로모션, 날씨, 사회적 이벤트 등 다양한 요인에 따라 크게 변동합니다. 특정 하루의 판매량만 보고 상품의 인기를 판단하기 어렵습니다. 예를 들어, 어제 갑자기 판매량이 폭증했다고 해서 상품이 폭발적으로 인기 있다고 단정하기는 이릅니다.
    *   **해결책 (7일 이동 평균):**
        1.  각 상품에 대해 '일일 판매량' 데이터를 날짜 순서로 정렬합니다.
        2.  7일 이동 평균(rolling(7).mean())을 계산하여 새로운 '7일 평균 판매량' 특징을 만듭니다. 이 값은 오늘을 포함한 지난 7일간의 평균 판매량을 나타냅니다.
        3.  예시:
            *   1월 1일: 100개
            *   1월 2일: 110개
            *   ...
            *   1월 7일: 150개 (1/1~1/7 평균: 120개) -> 1/7의 7일 이동 평균 = 120개
            *   1월 8일: 90개 (1/2~1/8 평균: 115개) -> 1/8의 7일 이동 평균 = 115개
        4.  **결과 해석:** 이 7일 이동 평균은 매일의 급격한 판매량 변동을 완화하여 상품의 장기적인 판매 추세(예: 점차 판매량이 늘고 있는지, 줄고 있는지)나 주간 계절성(예: 주말에 판매량이 오르는 경향)을 명확하게 보여줍니다. 이를 통해 쇼핑몰 관리자는 상품의 재고 수준을 조절하거나, 마케팅 캠페인의 효과를 더 안정적으로 평가할 수 있습니다.

---

### 2. Idempotent Chaining with assign/pipe (멱등성 체이닝과 파이프라인)

이 섹션은 데이터 처리 과정을 여러 단계로 나누어 순차적으로 연결하는 '체이닝' 기법과, 그 과정이 '멱등성(idempotent)'을 가지도록 만드는 방법을 설명합니다.

#### 2.1. 멱등성 체이닝 (Idempotent Chaining)

*   **무엇인가요?** 데이터프레임(DataFrame)에 대한 여러 데이터 변환(transformation) 작업을 `.pipe()`와 `.assign()` 같은 메서드를 사용하여 연결하는 방식입니다. 여기서 '멱등성'이란, 동일한 연산을 여러 번 적용해도 결과가 항상 같다는 것을 의미합니다. Pandas의 `assign` 메서드는 원본 데이터프레임을 변경하지 않고 항상 새로운 데이터프레임을 반환하기 때문에 멱등성을 보장하기 좋습니다.
*   **왜 사용하나요?**
    *   **선언적이고 재실행 가능(Declarative, Re-runnable):** 코드만 보면 어떤 작업들이 어떤 순서로 이루어지는지 명확하게 알 수 있으며, 언제든지 전체 파이프라인을 처음부터 다시 실행해도 동일한 최종 결과를 얻을 수 있습니다.
    *   **디버깅 및 재현성 용이(Easier Debugging, Reproducibility):** 각 단계가 독립적으로 작동하므로, 특정 단계에서 문제가 발생하면 그 부분을 쉽게 격리하고 디버깅할 수 있습니다. 또한, 데이터 처리 과정을 명확하게 문서화하므로 다른 사람이나 미래의 나 자신도 쉽게 작업을 재현할 수 있습니다.
    *   **테스트 용이(Testable):** 각 단계를 단위 테스트하기 용이하여 데이터 파이프라인의 신뢰성을 높일 수 있습니다.
*   **Tip:** `pipe`를 사용할 때는 작고 순수한(pure function) 헬퍼 함수들을 활용하여 체인을 더 읽기 쉽게 만드는 것이 좋습니다.

*   **구체적이고 실생활에 가까운 예시:**
    *   **시나리오:** 한 회사의 인사팀에서 직원 성과 평가를 위해 여러 데이터를 취합하고 정제하는 작업을 한다고 가정해 봅시다. 데이터는 `df`라는 이름의 데이터프레임에 담겨 있으며, 여기에는 `id` (직원 ID), `ts` (평가 날짜), `y` (성과 점수), `x` (부가 정보) 등의 컬럼이 있습니다.
    *   **문제점 (일반적인 순차 처리 방식):**
        ```python
        # 1. 'y' 컬럼에 결측치가 있는 행 제거
        df_step1 = df.dropna(subset=['y'])

        # 2. 'x' 컬럼의 결측치를 중앙값으로 채우기
        median_x = df_step1['x'].median()
        df_step2 = df_step1.fillna({'x': median_x})

        # 3. 'id'와 'ts' 기준으로 정렬
        final_df = df_step2.sort_values(by=['id', 'ts'])
        ```
        이 방식은 여러 개의 중간 변수(`df_step1`, `df_step2`)를 생성하여 메모리 효율이 떨어질 수 있고, 전체 흐름을 한눈에 파악하기 어렵습니다. 만약 데이터가 커지면 중간 변수들이 쌓여 관리가 복잡해집니다.

    *   **해결책 (Idempotent Chaining with assign/pipe):**
        ```python
        tidy_df = (
            df # 원본 데이터프레임에서 시작
            .pipe(lambda d: d.dropna(subset=['y'])) # 1. 'y'에 결측치 있는 행 제거 (새 데이터프레임 반환)
            .assign(x=lambda d: d['x'].fillna(d['x'].median())) # 2. 'x' 결측치 중앙값으로 채우기 (새 데이터프레임에 'x' 컬럼 업데이트)
            .sort_values(by=['id', 'ts']) # 3. 'id'와 'ts' 기준으로 정렬 (새 데이터프레임 반환)
        )
        ```
    *   **결과 해석:**
        1.  **가독성:** 전체 데이터 처리 흐름이 `.`으로 연결된 하나의 블록으로 표현되어, 각 단계가 무엇을 하는지 시각적으로 명확합니다. 마치 레시피처럼 순서대로 읽을 수 있습니다.
        2.  **재현성 및 멱등성:** `tidy_df`를 생성하는 이 코드는 언제 실행하더라도 항상 동일한 `tidy_df`를 생성합니다. 중간에 원본 `df`를 변경하는 작업이 없기 때문에 (모든 메서드가 새로운 데이터프레임을 반환) 다른 코드에 의해 `df`가 수정되더라도 이 파이프라인은 항상 `df`의 초기 상태를 기준으로 일관된 결과를 만들어냅니다.
        3.  **디버깅:** 만약 `.assign` 단계에서 에러가 발생하면, 파이썬 트레이스백은 에러가 발생한 정확한 라인을 가리킬 것이고, 우리는 해당 단계만 집중해서 문제를 해결할 수 있습니다.
        4.  **유지보수:** 새로운 데이터 정제 단계를 추가하거나 기존 단계를 수정하기가 훨씬 용이합니다. 예를 들어, `assign` 앞에 새로운 `pipe` 단계를 추가하여 특정 문자열을 소문자로 바꾸는 작업을 넣을 수 있습니다.

이처럼 멱등성 체이닝은 데이터 전처리 코드를 더 깔끔하고, 안정적이며, 유지보수하기 쉽게 만들어줍니다.

---

