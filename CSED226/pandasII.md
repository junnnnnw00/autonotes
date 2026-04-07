# PPT 상세 해설 노트

## Slide 1

이 슬라이드의 핵심 개념은 **Pandas 라이브러리의 Dataframe을 활용한 데이터 관리 및 조회 방법**입니다. 구체적으로는 데이터의 **생성(Create), 조회(Read), 수정(Update), 삭제(Delete)**, 그리고 **조건에 따른 데이터 질의(Query)**에 대해 다룹니다.

---

### 1. Pandas와 Dataframe 개요

*   **Pandas**: Python에서 데이터를 효율적으로 다루고 분석하기 위한 강력한 라이브러리입니다. 특히 대량의 정형 데이터를 처리하는 데 매우 유용합니다.
*   **Dataframe**: Pandas의 핵심 데이터 구조로, 엑셀 스프레드시트나 관계형 데이터베이스의 테이블과 유사합니다. 행(row)과 열(column)로 이루어져 있으며, 각 열은 다른 데이터 타입을 가질 수 있습니다.

### 2. CRUD (Create, Read, Update, Delete)

CRUD는 데이터베이스나 데이터 관리 시스템에서 데이터를 다루는 기본적인 네 가지 작업을 의미하며, Pandas Dataframe에서도 이 원칙이 동일하게 적용됩니다.

*   **Create (생성)**: 새로운 Dataframe을 만들거나, 기존 Dataframe에 새로운 행이나 열을 추가하는 작업입니다.
*   **Read (조회)**: Dataframe의 데이터를 확인하고, 특정 조건에 맞는 데이터를 선택하여 불러오는 작업입니다. 이는 'Query'와 밀접하게 관련됩니다.
*   **Update (수정)**: Dataframe 내의 기존 데이터를 변경하는 작업입니다.
*   **Delete (삭제)**: Dataframe에서 특정 행이나 열을 제거하는 작업입니다.

### 3. Query over Dataframes (Dataframe 질의)

Dataframe 질의는 'Read' 작업의 핵심으로, Dataframe에서 원하는 조건에 맞는 데이터를 효율적으로 찾아내는 과정입니다. 특정 열의 값, 여러 열의 조합, 불리언 인덱싱 등 다양한 방법으로 데이터를 필터링하고 선택할 수 있습니다.

---

### 실생활 예시: 온라인 쇼핑몰 상품 관리 시스템

당신이 온라인 쇼핑몰의 상품 관리 담당자라고 가정해봅시다. 매일 수많은 상품을 등록하고, 가격을 변경하며, 품절된 상품을 확인하고, 판매가 부진한 상품을 삭제하는 등의 작업을 합니다. 이러한 작업을 Pandas Dataframe으로 효율적으로 처리할 수 있습니다.

#### 시나리오 설정:
우리는 `상품 ID`, `상품명`, `카테고리`, `가격`, `재고 수량` 정보를 담는 Dataframe을 관리할 것입니다.

```python
import pandas as pd

# 1. Create (생성): 초기 상품 Dataframe 생성
# 쇼핑몰에 등록된 초기 상품 목록
data = {
    '상품ID': [101, 102, 103, 104, 105],
    '상품명': ['스마트폰 X', '블루투스 이어폰', '노트북 Pro', '무선 충전기', '스마트 워치'],
    '카테고리': ['전자제품', '전자제품', '전자제품', '액세서리', '전자제품'],
    '가격': [1200000, 150000, 2500000, 30000, 300000],
    '재고': [50, 120, 30, 200, 75]
}
products_df = pd.DataFrame(data)
print("--- 1. 초기 상품 Dataframe ---")
print(products_df)
print("\n")

# 새로운 상품 추가 (새로운 행 생성)
new_product = pd.DataFrame([{'상품ID': 106, '상품명': '고속 충전 케이블', '카테고리': '액세서리', '가격': 15000, '재고': 300}])
products_df = pd.concat([products_df, new_product], ignore_index=True)
print("--- 1-1. 새로운 상품 추가 후 Dataframe ---")
print(products_df)
print("\n")

# 2. Read (조회) & Query (질의):
# 2-1. 모든 상품 정보 조회 (Read)
print("--- 2-1. 모든 상품 정보 ---")
print(products_df)
print("\n")

# 2-2. 특정 카테고리의 상품만 조회 (Query: '카테고리'가 '전자제품'인 상품)
print("--- 2-2. '전자제품' 카테고리 상품만 조회 ---")
electronics = products_df[products_df['카테고리'] == '전자제품']
print(electronics)
print("\n")

# 2-3. 재고가 100개 미만인 상품 조회 (Query: '재고'가 100 미만)
print("--- 2-3. 재고 부족 상품 (100개 미만) ---")
low_stock_products = products_df[products_df['재고'] < 100]
print(low_stock_products)
print("\n")

# 2-4. 특정 상품명의 상품 조회 (Query: '스마트폰 X' 상품)
print("--- 2-4. '스마트폰 X' 상품 정보 ---")
smartphone_x = products_df[products_df['상품명'] == '스마트폰 X']
print(smartphone_x)
print("\n")

# 2-5. 가격이 5만원 이상 50만원 이하인 상품 조회 (Query: 복합 조건)
print("--- 2-5. 가격대가 5만원~50만원인 상품 ---")
mid_price_products = products_df[(products_df['가격'] >= 50000) & (products_df['가격'] <= 500000)]
print(mid_price_products)
print("\n")

# 3. Update (수정):
# 3-1. '스마트폰 X'의 가격을 115만원으로 인하
products_df.loc[products_df['상품명'] == '스마트폰 X', '가격'] = 1150000
print("--- 3-1. '스마트폰 X' 가격 인하 후 ---")
print(products_df[products_df['상품명'] == '스마트폰 X'])
print("\n")

# 3-2. '블루투스 이어폰'의 재고를 10개 판매 후 110개로 업데이트
products_df.loc[products_df['상품명'] == '블루투스 이어폰', '재고'] -= 10
print("--- 3-2. '블루투스 이어폰' 재고 업데이트 후 ---")
print(products_df[products_df['상품명'] == '블루투스 이어폰'])
print("\n")

# 4. Delete (삭제):
# 4-1. 상품 ID가 104인 '무선 충전기' 상품을 단종하여 삭제
products_df = products_df[products_df['상품ID'] != 104].reset_index(drop=True)
print("--- 4-1. '무선 충전기'(ID:104) 삭제 후 Dataframe ---")
print(products_df)
print("\n")

# 4-2. 재고가 0인 상품 삭제 (만약 있다면)
# (이 예시에서는 재고가 0인 상품이 없으므로, 직접 만들어서 보여줌)
products_df.loc[products_df['상품ID'] == 106, '재고'] = 0 # 임시로 '고속 충전 케이블' 재고를 0으로 설정
print("--- 4-2. '고속 충전 케이블' 재고 0으로 설정 (삭제 예시를 위해) ---")
print(products_df[products_df['상품ID'] == 106])
print("\n")

products_df = products_df[products_df['재고'] > 0].reset_index(drop=True)
print("--- 4-2. 재고가 0인 상품 삭제 후 Dataframe ---")
print(products_df)
```

이 예시를 통해 Dataframe을 만들고, 조건에 따라 데이터를 찾아내며, 값을 바꾸고, 필요 없는 데이터를 제거하는 과정이 얼마나 직관적이고 효율적인지 이해할 수 있을 것입니다. Pandas는 이처럼 복잡한 데이터 관리 작업을 몇 줄의 코드로 간결하게 처리할 수 있도록 도와줍니다.

---

## Slide 2

## 학습 목표 핵심 개념 설명

### 1. CRUD for pandas: Create, Update, Delete, Query

*   **개념**: CRUD는 데이터를 다루는 데 있어 가장 기본이 되는 네 가지 연산을 의미합니다.
    *   **Create (생성)**: 새로운 데이터를 추가합니다.
    *   **Read (읽기/조회)**: 기존 데이터를 검색하고 가져옵니다. 'Query'와 동일한 의미로 사용됩니다.
    *   **Update (수정)**: 기존 데이터의 내용을 변경합니다.
    *   **Delete (삭제)**: 기존 데이터를 제거합니다.
*   **실생활 예시**: 친구들과 함께하는 동아리 명부를 `pandas` DataFrame으로 관리한다고 생각해 봅시다.
    *   **Create (생성)**: 새로운 신입 부원이 들어와 이름, 학번, 전공 등의 정보를 명부에 추가합니다.
        *   `df.loc[새로운_인덱스] = [값1, 값2, 값3]` 또는 새로운 DataFrame을 만들어 `pd.concat()`으로 합칩니다.
    *   **Read (조회)**: 특정 학과 친구들만 보고 싶거나, 전체 부원들의 목록을 확인합니다.
        *   `df[df['전공'] == '컴퓨터공학']` 또는 `df.head()`, `df.tail()` 등.
    *   **Update (수정)**: 한 친구가 전공을 바꿨거나, 연락처가 변경되어 명부의 해당 정보를 수정합니다.
        *   `df.loc[해당_인덱스, '전공'] = '새로운 전공'`
    *   **Delete (삭제)**: 졸업하거나 휴학하는 친구가 생겨 명부에서 해당 정보를 삭제합니다.
        *   `df.drop(삭제할_인덱스)`

### 2. ERA Operators: Formal definitions + pandas counterparts

*   **개념**: ERA는 '확장 관계 대수(Extended Relational Algebra)'를 의미하며, 관계형 데이터베이스에서 데이터를 조작하고 질의하는 데 사용되는 수학적이고 형식적인 연산 집합입니다. 이 목표는 이러한 연산들의 공식적인 정의를 이해하고, `pandas`에서 해당 연산들이 어떻게 구현되는지 (어떤 함수나 메서드에 대응되는지) 아는 것입니다.
*   **실생활 예시**: 학교의 학생 성적 데이터를 분석하는 상황을 가정해 봅시다.
    *   **선택 (Selection, σ)**: 특정 조건을 만족하는 행(레코드)을 선택하는 연산.
        *   **공식 정의**: "수강 과목이 '데이터베이스'이고 점수가 90점 이상인 모든 학생 레코드를 선택하라."
        *   **pandas 대응**: `grades_df[ (grades_df['과목'] == '데이터베이스') & (grades_df['점수'] >= 90) ]`
    *   **투영 (Projection, π)**: 특정 열(속성)만 선택하여 새로운 테이블을 만드는 연산.
        *   **공식 정의**: "모든 학생의 '이름'과 '학과' 정보만 보여라."
        *   **pandas 대응**: `grades_df[['이름', '학과']]`
    *   **결합 (Join, ⋈)**: 두 테이블을 특정 기준(공통 열)에 따라 합치는 연산.
        *   **공식 정의**: "학생 정보 테이블과 수강 과목 테이블을 '학번'을 기준으로 결합하여 각 학생이 수강하는 과목 정보를 함께 보여라."
        *   **pandas 대응**: `pd.merge(students_df, courses_df, on='학번')`
    *   이 외에도 합집합(Union), 차집합(Difference) 등 다양한 ERA 연산들이 `pandas`의 `concat`, `isin`, `drop_duplicates` 등의 메서드와 대응될 수 있습니다.

### 3. Grouping/Pivoting: ERA γ (grouping/aggregation) and pivot tables

*   **개념**: 데이터 분석에서 데이터를 특정 기준에 따라 묶고(Grouping), 묶인 그룹별로 요약 통계(Aggregation)를 내는 것은 매우 중요합니다. ERA γ (감마)는 이러한 그룹화 및 집계 연산을 나타냅니다. 피벗 테이블은 이처럼 그룹화되고 집계된 데이터를 행과 열의 교차 형태로 시각화하여 보여주는 강력한 도구입니다.
*   **실생활 예시**: 온라인 쇼핑몰의 월별 판매 데이터를 분석한다고 상상해 봅시다.
    *   **Grouping/Aggregation (ERA γ)**: 각 '카테고리'별로 '총 매출'과 '평균 판매 가격'을 알고 싶을 때.
        *   먼저 판매 데이터를 '상품 카테고리'별로 **그룹화**합니다.
        *   각 그룹에 대해 '매출액'을 **합계(sum)**하고, '가격'을 **평균(mean)** 냅니다.
        *   **pandas 대응**: `sales_df.groupby('상품 카테고리').agg(총_매출=('매출액', 'sum'), 평균_가격=('가격', 'mean'))`
    *   **Pivot Tables**: 각 '지역'별 '주요 상품 카테고리'의 '평균 만족도 점수'를 한눈에 비교하고 싶을 때.
        *   '지역'을 행(index)으로, '상품 카테고리'를 열(columns)으로, '만족도 점수'를 값(values)으로 사용하여 평균을 계산하는 피벗 테이블을 만듭니다.
        *   **pandas 대응**: `sales_df.pivot_table(values='만족도 점수', index='지역', columns='상품 카테고리', aggfunc='mean')`
        *   이를 통해 "서울 지역의 전자기기 만족도는 3.5점, 의류는 4.2점"과 같이 데이터를 직관적으로 비교할 수 있습니다.

### 4. Semantics: State the ERA query and describe its meaning before code

*   **개념**: 이 목표는 코드를 작성하기 전에 '무엇을 할 것인가?' (의미론, Semantics)에 대해 명확하게 정의하는 것의 중요성을 강조합니다. 즉, 해결하고자 하는 데이터 문제에 대해 ERA 연산과 같은 형식적인 언어나 구체적인 한글 설명을 통해 논리적인 질의를 먼저 구상하고, 그 의미를 정확히 파악한 후에 비로소 코드를 작성하라는 의미입니다. 이는 코드의 오류를 줄이고, 복잡한 문제도 체계적으로 해결할 수 있게 돕습니다.
*   **실생활 예시**: 한 스포츠 브랜드의 마케팅 담당자로서, '가장 많이 팔린 신발 종류 TOP 3'를 찾아 다음 시즌 전략에 활용해야 한다고 해봅시다.
    *   **코드 작성 전 (의미론적 질의/ERA 사고방식)**:
        1.  "먼저, 모든 판매 기록 중에서 '신발' 카테고리만 골라내야 해." (선택, Selection)
        2.  "그 다음, 이 신발 판매 기록들을 '신발 종류'별로 묶어서 각 종류의 '총 판매량'을 계산해야겠어." (그룹화 및 집계, Grouping/Aggregation - ERA γ)
        3.  "계산된 총 판매량이 높은 순서대로 신발 종류들을 정렬해야 해." (정렬, Ordering)
        4.  "마지막으로, 정렬된 결과 중에서 상위 3개만 선택하고, 그들의 '신발 종류'와 '총 판매량' 정보만 보여주면 돼." (투영 및 제한, Projection and Limiting)
    *   **코드 작성 후 (pandas 구현)**:
        ```python
        # 판매 데이터프레임 'sales_data'에 '카테고리', '상품명', '판매량' 컬럼이 있다고 가정
        
        # 1. 신발 카테고리만 선택
        shoes_sales = sales_data[sales_data['카테고리'] == '신발']
        
        # 2. 신발 종류별 총 판매량 계산 (그룹화 및 집계)
        shoes_sales_by_type = shoes_sales.groupby('상품명')['판매량'].sum()
        
        # 3. 판매량이 높은 순서대로 정렬
        sorted_shoes = shoes_sales_by_type.sort_values(ascending=False)
        
        # 4. 상위 3개 선택 및 정보 확인 (투영 및 제한)
        top_3_shoes = sorted_shoes.head(3)
        print(top_3_shoes)
        ```
    *   이렇게 코드를 작성하기 전에 문제를 논리적으로 분해하고 단계별 의미를 파악하는 것이 'Semantics' 목표의 핵심입니다.

---

## Slide 3

이 슬라이드에서는 Python의 Pandas 라이브러리를 사용하여 간단한 '장난감(Toy) 데이터셋'을 생성하고 그 구조를 확인하는 방법을 보여줍니다.

### 1. Pandas 및 NumPy 라이브러리 불러오기

*   **`import pandas as pd`**: 데이터 조작 및 분석을 위한 강력한 라이브러리인 Pandas를 불러옵니다. `pd`라는 별칭을 사용하여 코드를 더 짧고 읽기 쉽게 만듭니다.
*   **`import numpy as np`**: 과학 계산을 위한 핵심 라이브러리인 NumPy를 불러옵니다. Pandas는 내부적으로 NumPy의 배열 객체를 많이 사용하므로, Pandas를 사용할 때 함께 불러오는 경우가 많습니다.

**실생활 예시**:
만약 당신이 레시피 앱을 개발한다면, `pandas`는 다양한 요리 데이터(재료, 조리 시간, 난이도 등)를 효율적으로 관리하고 분석하는 '고성능 주방 도구 세트'와 같습니다. `numpy`는 그 도구 세트 중 '칼'이나 '저울'처럼 숫자 기반의 정밀한 계산을 처리하는 데 특화된 기본 도구라고 할 수 있습니다. 이 둘을 함께 사용하면 복잡한 요리 과정도 체계적으로 처리할 수 있습니다.

### 2. 파이썬 딕셔너리로 데이터 생성

*   **`data = {...}`**: Pandas DataFrame의 원천이 될 파이썬 딕셔너리를 정의합니다. 이 딕셔너리의 각 '키(key)'는 최종 DataFrame의 '열(column) 이름'이 되고, 각 '값(value)'은 해당 열에 들어갈 '데이터 리스트'가 됩니다.
    *   `'State': ['CA']*4`는 `'CA'` 문자열이 4번 반복되는 리스트 `['CA', 'CA', 'CA', 'CA']`를 생성합니다.
    *   `'Sex': ['F']*4`는 `'F'` 문자열이 4번 반복되는 리스트 `['F', 'F', 'F', 'F']`를 생성합니다.
    *   `'Year': [1910]*4`는 숫자 `1910`이 4번 반복되는 리스트 `[1910, 1910, 1910, 1910]`를 생성합니다.
    *   `'Name': ['Mary', 'Helen', 'Dorothy', 'Margaret']`는 네 개의 고유한 이름으로 구성된 리스트입니다.
    *   `'Count': [295, 239, 220, 163]`는 네 개의 숫자로 구성된 리스트입니다.
*   **중요**: 딕셔너리의 모든 값(리스트)은 동일한 길이를 가져야 합니다. 여기서는 모두 길이가 4입니다.

**실생활 예시**:
당신이 반 친구들의 시험 점수를 기록한다고 생각해 봅시다. 다음과 같은 딕셔너리를 만들 수 있습니다:
`score_data = {`
`    'Name': ['김철수', '이영희', '박지민'],`
`    'Math': [90, 85, 92],`
`    'English': [78, 95, 88]`
`}`
여기서 'Name', 'Math', 'English'가 데이터의 '카테고리'(열 이름)가 되고, 각 리스트는 해당 카테고리에 속하는 실제 값들이 됩니다. 모든 리스트의 길이가 3으로 같죠? 이는 세 명의 학생에 대한 정보를 담고 있기 때문입니다.

### 3. Pandas DataFrame 생성

*   **`babynames = pd.DataFrame(data)`**: 위에서 정의한 `data` 딕셔너리를 사용하여 Pandas DataFrame 객체를 생성합니다. Pandas는 이 딕셔너리를 '테이블' 형태로 변환하여 `babynames` 변수에 저장합니다. 각 키는 열 이름이 되고, 해당 값 리스트는 그 열의 데이터가 됩니다.

**실생활 예시**:
앞서 만든 `score_data` 딕셔너리(`score_data = {'Name': ['김철수', ...], 'Math': [...], 'English': [...]}`)를 `pd.DataFrame(score_data)`로 변환하는 것은 마치 당신이 손으로 쓴 친구들의 점수 목록을 깔끔한 '엑셀 스프레드시트'로 옮겨 정리하는 것과 같습니다. 이제 이 스프레드시트는 각 학생의 정보를 행으로, 각 과목의 점수를 열로 가지는 정돈된 테이블이 됩니다.

### 4. DataFrame의 형태(Shape) 확인

*   **`print(babynames.shape)`**: 생성된 `babynames` DataFrame의 차원(dimension)을 확인합니다. 결과는 `(행의 개수, 열의 개수)` 형태의 튜플로 반환됩니다.
    *   이 코드의 경우, 4개의 항목(Mary, Helen, Dorothy, Margaret)이 있으므로 행은 4개입니다.
    *   'State', 'Sex', 'Year', 'Name', 'Count'의 총 5개 열이 있으므로 열은 5개입니다.
    *   따라서 출력 결과는 `(4, 5)`가 됩니다.

**실생활 예시**:
당신이 서점에서 책을 정리하고 있다고 가정해 봅시다. `babynames.shape`를 확인하는 것은 "서점에 총 몇 권의 책이 있고, 각 책마다 제목, 저자, 출판일, 가격 등의 정보가 몇 가지씩 기록되어 있는가?"를 파악하는 것과 같습니다. 만약 책이 100권이고 각 책마다 4가지 정보가 있다면, `.shape`는 `(100, 4)`라고 알려줄 것입니다. 이는 데이터셋의 '크기'를 한눈에 파악하는 데 매우 유용합니다.

---

## Slide 4

## Pandas DataFrame CRUD (Create, Update, Delete) 핵심 API와 활용

Pandas DataFrame에서 데이터를 생성하고, 수정하며, 삭제하는 기본 작업(CRUD)은 데이터 분석의 핵심입니다. 여기서는 각 작업 유형별로 주요 API와 그 동작 방식, 그리고 실생활 예시를 통해 자세히 살펴보겠습니다.

### 1. Create (데이터 생성 및 추가)

| API | 설명 |
| :------------------------------- | :------------------------------------------------------------------------------------------------ |
| `pd.concat([df1, df2], axis=0)` | 여러 DataFrame의 행(row)을 위아래로 쌓아 병합합니다. (Bag append, 관계 대수 `U` + `δ`) |
| `pd.concat([df1, df2], axis=1)` | 여러 DataFrame의 열(column)을 인덱스를 기준으로 옆으로 연결하여 병합합니다. (Reshape / Attribute extension) |
| `df.assign(new=expr, ...)` | 기존 DataFrame의 사본에 새로운 열을 추가하거나, 기존 열을 계산하여 업데이트한 새 DataFrame을 반환합니다. 원본은 변경되지 않습니다. (Generalized projection `π*`) |
| `df.loc[new_idx] = row` | 레이블(인덱스)을 사용하여 새 행을 삽입하거나 기존 행을 덮어씁니다. DataFrame을 직접 변경(mutate)합니다. (관계 대수와는 다소 다름) |
| `df.insert(pos, "col", values)` | 특정 위치(position)에 새 열을 삽입합니다. DataFrame을 직접 변경(mutate)합니다. (관계 대수 `π*`) |
| `df.reindex(new_index, columns)` | 지정된 새 인덱스(행)나 열에 맞춰 DataFrame을 재구성합니다. 없는 행/열은 `NaN`으로 채워집니다. (Reshape) |

**예시 설명:**

*   **`pd.concat([df1, df2], axis=0)` (행 병합)**
    *   **설명**: 서로 다른 기간(예: 2023년 상반기, 2023년 하반기)의 판매 데이터를 담고 있는 두 개의 DataFrame을 하나의 통합된 연간 판매 보고서 DataFrame으로 만들 때 사용합니다. 두 DataFrame의 열 구조가 같을 때 유용하며, 중복된 행을 포함할 수 있습니다.
    *   **실생활 예시**:
        *   `df_sales_h1` (상반기 판매)과 `df_sales_h2` (하반기 판매)를 합쳐 `df_sales_annual = pd.concat([df_sales_h1, df_sales_h2], axis=0)`와 같이 2023년 전체 판매 데이터를 만듭니다.

*   **`pd.concat([df1, df2], axis=1)` (열 병합)**
    *   **설명**: 고객의 기본 정보(이름, 주소)를 담은 DataFrame과 해당 고객의 구매 이력(구매 금액, 구매 일자)을 담은 다른 DataFrame을, 공통된 고객 ID를 기준으로 옆으로 연결하여 하나의 완전한 고객 데이터 DataFrame을 만들 때 사용합니다. 두 DataFrame의 인덱스가 잘 정렬되어 있어야 합니다.
    *   **실생활 예시**:
        *   `df_customer_info` (고객 ID, 이름, 주소)와 `df_purchase_history` (고객 ID, 구매액, 구매일)를 `df_full_customer_data = pd.concat([df_customer_info, df_purchase_history], axis=1)` (단, 두 df의 인덱스가 고객 ID로 정렬되어 있다고 가정)와 같이 연결하여 고객 정보를 풍부하게 합니다.

*   **`df.assign(new_column = lambda df: ...)` (새 열 추가)**
    *   **설명**: 온라인 쇼핑몰에서 상품의 '단가'와 '수량'이 있는 DataFrame이 있을 때, 이 정보를 바탕으로 '총 금액'이라는 새로운 열을 계산하여 추가하고 싶을 때 사용합니다. `assign`은 원본 DataFrame을 변경하지 않고 새 DataFrame을 반환하므로, 기존 데이터를 안전하게 유지할 수 있습니다.
    *   **실생활 예시**:
        *   `df_orders`에 'price'와 'quantity' 열이 있다면, `df_orders_with_total = df_orders.assign(total_price = lambda x: x['price'] * x['quantity'])`를 사용하여 각 주문의 총 금액을 계산한 `total_price` 열을 추가합니다.

*   **`df.loc[new_idx] = row` (새 행 삽입)**
    *   **설명**: 회사 직원 목록 DataFrame에 새로운 직원의 정보를 행으로 추가할 때 사용합니다. 특정 인덱스 레이블을 지정하여 해당 위치에 새 데이터를 삽입하며, 이는 원본 DataFrame을 직접 변경(mutation)하는 작업입니다.
    *   **실생활 예시**:
        *   `df_employees`에 새로운 직원 '김민수'의 정보(사번 'E005', 이름 '김민수', 부서 '인사팀')를 추가하려면 `df_employees.loc['E005'] = ['김민수', '인사팀']`와 같이 할 수 있습니다.

*   **`df.insert(pos, "col", values)` (새 열 삽입)**
    *   **설명**: 학생 성적표 DataFrame에서 '이름'과 '수학' 점수 사이에 '영어' 점수 열을 추가하고 싶을 때 사용합니다. 특정 위치(`pos`)를 지정하여 열을 삽입할 수 있으며, 이것 또한 원본 DataFrame을 직접 변경합니다.
    *   **실생활 예시**:
        *   `df_grades`에 'Name' 열 다음(인덱스 1)에 'English' 열을 추가하려면 `df_grades.insert(1, 'English', [85, 90, 78, 92])`와 같이 사용합니다.

### 2. Update (데이터 수정)

| API | 설명 |
| :-------------------------- | :--------------------------------------------------------------------------------------------------- |
| `df.loc[keys, cols] = values` | 레이블(keys)과 열 이름(cols)을 사용하여 여러 셀의 값을 벡터화된 방식으로 수정합니다. DataFrame을 직접 변경(mutate)합니다. |
| `df.at[row, col] = scalar` | 단일 셀의 값을 레이블을 통해 빠르게 수정합니다. DataFrame을 직접 변경(mutate)합니다. |
| `df.where(cond, other)` | `cond` 조건이 True인 곳은 값을 유지하고, False인 곳은 `other` 값으로 대체합니다. (관계 대수: 선택(selection) `σ`와 유사) |
| `df.mask(cond, other)` | `cond` 조건이 True인 곳은 `other` 값으로 대체하고, False인 곳은 값을 유지합니다. (`where`의 반대) |
| `df.replace(old, new)` | 특정 값을 다른 값으로 바꿉니다. 사전(dict)이나 리스트, 정규 표현식을 사용하여 여러 값을 한 번에 바꿀 수도 있습니다. |
| `df.assign(col=f(df))` | 함수를 적용하여 기존 열을 계산하고 업데이트한 새 DataFrame을 반환합니다. 원본은 변경되지 않습니다. (관계 대수 `π*`) |

**예시 설명:**

*   **`df.loc[keys, cols] = values` (여러 값 수정)**
    *   **설명**: 재고 관리 시스템에서 특정 상품들(keys)의 재고 수량(cols)을 일괄적으로 업데이트해야 할 때 사용합니다. 예를 들어, 특정 상품들의 재고를 100개로 변경하거나, 기존 재고에 50개를 더하는 등 벡터화된 연산을 적용할 수 있습니다. 이 작업은 원본 DataFrame을 직접 변경합니다.
    *   **실생활 예시**:
        *   `df_inventory`에서 'product_A', 'product_C'의 'stock_quantity'를 100으로 업데이트하려면 `df_inventory.loc[['product_A', 'product_C'], 'stock_quantity'] = 100`과 같이 사용합니다.

*   **`df.at[row, col] = scalar` (단일 값 수정)**
    *   **설명**: 고객 지원 시스템에서 특정 고객('customer_id_101')의 전화번호('phone_number')가 변경되었을 때, 해당 고객의 단일 정보를 빠르고 정확하게 업데이트할 때 사용합니다. `loc`보다 단일 값 접근에 더 최적화되어 있으며, 원본 DataFrame을 직접 변경합니다.
    *   **실생활 예시**:
        *   `df_customers`에서 'C101' 고객의 'Phone' 번호를 '010-1234-5678'로 바꾸려면 `df_customers.at['C101', 'Phone'] = '010-1234-5678'`와 같이 사용합니다.

*   **`df.where(cond, other)` (조건에 따른 값 유지/대체)**
    *   **설명**: 학생 성적 DataFrame에서 시험에 결시하여 점수가 0점인 학생들의 점수를 '결시'로 표시하되, 실제로 시험을 본 학생들의 점수는 그대로 유지하고 싶을 때 사용합니다. 조건에 부합하는(True) 행/셀의 값만 유지하고 나머지를 변경합니다.
    *   **실생활 예시**:
        *   `df_scores`에서 'Exam' 점수가 0점인 경우 'Absent'로 표시하고 싶다면, `df_scores['Exam'] = df_scores['Exam'].where(df_scores['Exam'] > 0, 'Absent')`와 같이 사용할 수 있습니다.

*   **`df.mask(cond, other)` (조건에 따른 값 대체/유지)**
    *   **설명**: 설문조사 데이터에서 '나이' 응답이 비어있거나(NaN) 0으로 잘못 기입된 경우, 이 값들을 설문조사에 참여한 전체 응답자의 '평균 나이'로 대체하고 싶을 때 사용합니다. `where`와 반대로, 조건이 True인 경우 값을 `other`로 대체합니다.
    *   **실생활 예시**:
        *   `df_survey`의 'Age' 열에서 `NaN` 값을 평균 나이로 채우려면 `mean_age = df_survey['Age'].mean()`, `df_survey['Age'] = df_survey['Age'].mask(df_survey['Age'].isna(), mean_age)`와 같이 사용합니다.

*   **`df.replace(old, new)` (값 재매핑)**
    *   **설명**: 인구 통계 데이터에서 '성별' 열의 값이 'M', 'F'로 되어 있는데, 이를 'Male', 'Female'로 통일하고 싶을 때 사용합니다. 단일 값, 리스트, 사전(dictionary) 또는 정규 표현식을 사용하여 여러 값을 동시에 변경할 수 있습니다.
    *   **실생활 예시**:
        *   `df_population`의 'Gender' 열에서 `df_population['Gender'].replace({'M': 'Male', 'F': 'Female'}, inplace=True)`와 같이 값을 변경할 수 있습니다. (`inplace=True`는 원본 DataFrame을 직접 수정한다는 의미입니다.)

### 3. Delete (데이터 삭제)

| API | 설명 |
| :---------------------------- | :-------------------------------------------------------------------------------------------- |
| `df.drop(labels, axis=0)` | 지정된 레이블(인덱스)에 해당하는 행을 삭제합니다. 새 DataFrame을 반환하며, 원본을 변경하려면 `inplace=True`를 사용해야 합니다. |
| `df.drop(labels, axis=1)` | 지정된 레이블(열 이름)에 해당하는 열을 삭제합니다. 새 DataFrame을 반환하며, 원본을 변경하려면 `inplace=True`를 사용해야 합니다. |
| `df.dropna(subset=[...])` | 특정 열(subset)에 `NaN`(결측치)이 있는 행을 삭제합니다. (관계 대수: `is_not_null`에 대한 선택 `σ`와 유사) |
| `df.pop("col")` | 특정 열을 삭제하고, 삭제된 열을 Series 형태로 반환합니다. 원본 DataFrame은 변경됩니다. |
| `del df["col"]` | 특정 열을 삭제합니다. `pop`과 달리 삭제된 열을 반환하지 않으며, 원본 DataFrame을 변경합니다. |

**예시 설명:**

*   **`df.drop(labels, axis=0)` (행 삭제)**
    *   **설명**: 회원 명단 DataFrame에서 더 이상 활동하지 않는 특정 회원의 정보를 삭제하고 싶을 때 사용합니다. 해당 회원의 ID(인덱스 레이블)를 지정하여 행을 제거합니다. 원본을 유지하려면 새 DataFrame으로 결과를 할당하고, 원본을 변경하려면 `inplace=True`를 사용합니다.
    *   **실생활 예시**:
        *   `df_members`에서 'member_id_101', 'member_id_103'에 해당하는 회원을 삭제하려면 `df_members_cleaned = df_members.drop(['member_id_101', 'member_id_103'], axis=0)`와 같이 새 DataFrame을 만들거나, `df_members.drop(['member_id_101', 'member_id_103'], axis=0, inplace=True)`로 원본을 수정합니다.

*   **`df.drop(labels, axis=1)` (열 삭제)**
    *   **설명**: 설문조사 데이터에서 분석에 필요 없는 '응답자 IP 주소'나 '타임스탬프'와 같은 열을 영구적으로 제거하고 싶을 때 사용합니다. `axis=1`을 사용하여 열을 지정하며, `inplace=True`를 통해 원본을 직접 수정할 수 있습니다.
    *   **실생활 예시**:
        *   `df_survey_data`에서 'IP_Address'와 'Timestamp' 열을 삭제하려면 `df_survey_data_cleaned = df_survey_data.drop(['IP_Address', 'Timestamp'], axis=1)`와 같이 사용합니다.

*   **`df.dropna(subset=[...])` (결측치 포함 행 삭제)**
    *   **설명**: 고객 주문 데이터에서 '상품 코드'나 '결제 금액' 등 핵심 정보가 누락(NaN)된 주문은 유효하지 않다고 판단하고 해당 주문 기록을 통째로 삭제하여 데이터의 품질을 높일 때 사용합니다. `subset` 인자를 사용하여 특정 열에만 결측치가 있는지 확인하고 삭제할 수 있습니다.
    *   **실생활 예시**:
        *   `df_orders`에서 'product_code' 또는 'payment_amount' 열에 `NaN`이 있는 행을 삭제하려면 `df_orders_valid = df_orders.dropna(subset=['product_code', 'payment_amount'])`와 같이 사용합니다.

*   **`df.pop("col")` (열 삭제 및 반환)**
    *   **설명**: 대규모 고객 데이터에서 '이메일 주소' 열만 따로 추출하여 마케팅 캠페인에 활용하고 싶지만, 원본 DataFrame에서는 이메일 주소 열을 제거하여 개인 정보 보호 목적을 달성하고 싶을 때 사용합니다. 이 메서드는 삭제된 열을 Series 형태로 반환하며, 원본 DataFrame을 직접 변경합니다.
    *   **실생활 예시**:
        *   `customer_emails = df_customer_full.pop('email_address')`와 같이 사용하면 `customer_emails` 변수에 이메일 주소 Series가 저장되고, `df_customer_full`에서는 해당 열이 삭제됩니다.

*   **`del df["col"]` (열 삭제)**
    *   **설명**: 데이터 분석 과정에서 임시로 생성했던 '평균값_차이'와 같은 중간 계산 열이 더 이상 필요 없을 때, 메모리 효율을 위해 즉시 삭제하고 싶을 때 사용합니다. `pop`과 달리 삭제된 열의 데이터를 반환하지 않으며, 원본 DataFrame을 직접 변경합니다.
    *   **실생활 예시**:
        *   `df_analysis`에서 'temp_calculation'이라는 임시 열을 완전히 제거하려면 `del df_analysis['temp_calculation']`과 같이 사용합니다.

---

## Slide 5

## Pandas API 쿼리 및 동작 매핑

제공된 슬라이드는 Pandas 라이브러리에서 데이터를 쿼리하고 조작하는 다양한 핵심 API 함수들을 소개하고, 각 함수가 어떤 동작을 수행하며 데이터베이스의 관계형 대수(ERA: Extended Relational Algebra) 개념에 어떻게 매핑되는지를 보여줍니다. 각 개념을 상세히 설명하고 실생활 예시를 들어보겠습니다.

---

### 1. 조건에 따른 행 필터링 (`df.loc[mask]`, `df.query("expr")`)

*   **핵심 개념:** 특정 조건을 만족하는 데이터 행(row)을 선택하는 기능입니다.
*   **자세한 설명:**
    *   `df.loc[mask]`는 불리언 마스크(True/False 배열)를 사용하여 행을 필터링합니다. 예를 들어, `df[df['컬럼명'] > 값]`과 같은 형태로 조건을 직접 지정하여 원하는 행만 선택할 수 있습니다. 특정 열만 선택할 수도 있습니다. 관계형 대수의 '선택(selection, $\sigma$)' 연산에 해당합니다.
    *   `df.query("expr")`는 SQL의 `WHERE` 절처럼 문자열 표현식을 사용하여 행을 필터링하는 편리한 방법입니다. 조건을 더 직관적으로 작성할 수 있습니다.
*   **실생활 예시:**
    *   **`df.loc[mask]`:** 온라인 쇼핑몰에서 지난 한 달간 구매 금액이 5만 원을 초과하는 고객들의 목록을 추출하고 싶을 때, `customers_df[customers_df['구매금액'] > 50000]`와 같이 사용하여 해당 조건을 만족하는 고객 데이터만 필터링합니다.
    *   **`df.query("expr")`:** 자동차 판매 대리점에서 "2022년 이후 생산된 차량 중, 가격이 3천만 원 이상이고 연료 타입이 '전기' 또는 '하이브리드'인 차량"을 찾고 싶을 때, `cars_df.query("생산년도 >= 2022 and 가격 >= 30000000 and (연료타입 == '전기' or 연료타입 == '하이브리드')")`와 같이 SQL과 유사한 쿼리 문자열로 쉽게 조회할 수 있습니다.

---

### 2. 데이터프레임 병합 (`pd.merge(L,R,on=...,how=...)`)

*   **핵심 개념:** 두 개 이상의 데이터프레임을 특정 기준(열 또는 인덱스)에 따라 결합하는 기능입니다.
*   **자세한 설명:** `pd.merge()`는 관계형 데이터베이스의 `JOIN` 연산과 유사하며, `how` 인자를 통해 `inner`, `left`, `right`, `outer`, `cross` 등의 다양한 조인 방식을 지정할 수 있습니다. `on` 인자를 사용하여 공통 열을 기준으로 병합할 수 있습니다. 이는 관계형 대수의 '조인($\bowtie_\theta$)' 또는 '카테시안 곱($\times$)' 연산에 해당합니다.
*   **실생활 예시:**
    *   학교에서 '학생 정보' 데이터프레임(학생 ID, 이름, 학과 등)과 '수강 과목' 데이터프레임(학생 ID, 과목명, 성적 등)이 분리되어 있다고 가정해 봅시다. 각 학생의 이름과 그 학생이 수강한 과목 정보를 함께 보고 싶을 때, `pd.merge(학생정보_df, 수강과목_df, on='학생ID', how='inner')`와 같이 `학생ID`를 기준으로 두 데이터프레임을 병합하여, 어떤 학생이 어떤 과목을 듣고 어떤 성적을 받았는지 한눈에 파악할 수 있습니다.

---

### 3. 데이터 그룹화 및 집계 (`df.groupby(keys).agg(...)`)

*   **핵심 개념:** 특정 열(키)의 값을 기준으로 데이터를 그룹으로 나눈 후, 각 그룹에 대해 합계, 평균, 개수 등과 같은 집계 함수를 적용하는 기능입니다.
*   **자세한 설명:** `groupby()`는 관계형 대수의 '그룹화($\gamma_G,f(.)$)' 연산에 해당하며, 데이터를 의미 있는 묶음으로 분리하여 각 묶음의 특성을 요약할 때 사용됩니다. `agg()` 메서드와 함께 사용하여 다양한 집계 연산을 수행할 수 있습니다.
*   **실생활 예시:**
    *   회사에서 전국 지점별 매출 데이터가 있다고 가정해 봅시다(지점명, 판매품목, 매출액). 각 지점의 총 매출액을 계산하고 싶을 때, `sales_df.groupby('지점명')['매출액'].sum()`과 같이 사용하여 '지점명'으로 데이터를 그룹화한 후, 각 지점의 '매출액' 합계를 계산할 수 있습니다. 이를 통해 어떤 지점이 가장 높은 매출을 올렸는지 쉽게 알 수 있습니다.

---

### 4. 중복 행 제거 (`df.drop_duplicates(subset)`)

*   **핵심 개념:** 데이터프레임 내에서 완전히 동일하거나 특정 열(subset)을 기준으로 중복되는 행들을 제거하는 기능입니다.
*   **자세한 설명:** 데이터 클리닝 과정에서 매우 중요하며, 데이터의 정확성과 분석의 신뢰성을 높여줍니다. `subset` 인자를 지정하면 특정 열을 기준으로만 중복을 판단할 수 있습니다. 관계형 대수의 '중복 제거(duplicate elimination, $\delta$)' 연산에 해당합니다.
*   **실생활 예시:**
    *   이벤트 참여자 명단을 받았는데, 시스템 오류나 사용자 실수로 인해 동일한 이메일 주소를 가진 참가자가 여러 번 등록되었을 수 있습니다. 이때 `participants_df.drop_duplicates(subset=['이메일주소'])`를 사용하여 '이메일주소' 열을 기준으로 중복되는 참가자를 제거하고, 각 이메일 주소당 한 명의 참가자만 남겨 이벤트 당첨자 선정 시 혼란을 방지할 수 있습니다.

---

### 5. 값에 따른 행 정렬 (`df.sort_values(by)`)

*   **핵심 개념:** 데이터프레임의 행들을 하나 또는 여러 개의 특정 열(by)의 값을 기준으로 오름차순 또는 내림차순으로 재배열하는 기능입니다.
*   **자세한 설명:** `ascending` 인자를 통해 오름차순(기본값) 또는 내림차순 정렬을 선택할 수 있습니다. 이는 관계형 대수 확장 연산 중 '정렬(sorting, $\tau$)'에 해당합니다.
*   **실생활 예시:**
    *   학생들의 시험 점수 데이터가 있을 때, 최고 점수를 받은 학생부터 최저 점수를 받은 학생 순으로 정렬하여 성적 순위를 매기고 싶을 수 있습니다. 이때 `exam_scores_df.sort_values(by='총점', ascending=False)`를 사용하여 '총점'을 기준으로 내림차순 정렬하여 쉽게 순위를 파악할 수 있습니다.

---

### 6. 데이터프레임 연결/합치기 (`pd.concat([...], axis=0)`)

*   **핵심 개념:** 여러 개의 데이터프레임을 특정 축(axis)을 따라 이어 붙이는 기능입니다. `axis=0`은 행 방향으로 위아래로 쌓는 것을 의미하며, SQL의 `UNION ALL`과 유사합니다.
*   **자세한 설명:** 데이터프레임들이 동일한 열 구조를 가질 때 주로 사용되며, 여러 조각으로 나뉜 데이터를 하나로 모을 때 유용합니다. `axis=0`은 행을 추가하고, `axis=1`은 열을 추가합니다. 관계형 대수의 '합집합($\cup$)'과 비슷하지만, 중복 행을 제거하지 않는다는 점에서 '멀티셋(bag) 합집합'에 가깝습니다. 중복 제거를 원하면 이후 `drop_duplicates()`를 사용해야 합니다.
*   **실생활 예시:**
    *   한 회사의 각 부서가 월별 매출 보고서를 각각 다른 데이터프레임으로 만들었다고 가정해 봅시다. 1분기 전체 매출을 분석하기 위해 1월, 2월, 3월의 매출 데이터프레임들을 하나로 합쳐야 할 때, `pd.concat([jan_sales_df, feb_sales_df, mar_sales_df], axis=0)`를 사용하여 세 개의 월별 매출 데이터를 하나의 분기별 통합 매출 데이터프레임으로 만들 수 있습니다.

---

### 7. 교차표 생성 (`pd.crosstab(idx, cols)`)

*   **핵심 개념:** 두 개 이상의 범주형 변수 간의 빈도 분포를 보여주는 교차표(contingency table)를 생성하는 기능입니다.
*   **자세한 설명:** 주로 특정 범주 조합의 개수를 세는 데 사용되며, 데이터의 분포나 관계를 탐색할 때 유용합니다. 관계형 대수의 '피벗(PIVOT)' 연산 중 `COUNT(*)` 집계를 사용한 경우에 해당합니다.
*   **실생활 예시:**
    *   어떤 제품에 대한 고객 만족도 설문조사 결과가 있습니다(성별, 연령대, 만족도 등). '성별'과 '제품 만족도' 간의 관계를 파악하고 싶을 때, `pd.crosstab(survey_df['성별'], survey_df['만족도'])`를 사용하면 각 성별(행)에 따른 '만족도' 수준(열)별 응답자 수를 표 형태로 볼 수 있습니다. 예를 들어, 남성 중 '매우 만족'한 사람의 수, 여성 중 '불만족'한 사람의 수 등을 알 수 있습니다.

---

### 8. 피벗 테이블 생성 (`df.pivot_table(index, columns, values, aggfunc)`)

*   **핵심 개념:** 데이터프레임을 재구성하고 요약하는 강력한 도구로, 특정 열을 인덱스, 다른 열을 컬럼으로 사용하여 새로운 테이블을 만들고, 지정된 값(values)에 대해 집계 함수(aggfunc)를 적용합니다.
*   **자세한 설명:** `pivot_table()`은 `groupby()`와 `unstack()`의 기능을 통합하여 더욱 유연하고 강력한 데이터 요약 기능을 제공합니다. `index`, `columns`, `values` 인자를 사용하여 테이블의 행, 열, 그리고 채워질 값을 지정하며, `aggfunc` 인자로 평균, 합계, 개수 등 다양한 집계 함수를 적용할 수 있습니다. 이는 관계형 대수의 '집계 함수 f'를 사용한 '일반적인 피벗(PIVOT)' 연산에 해당합니다.
*   **실생활 예시:**
    *   전국 백화점 지점별(지점명), 분기별(분기), 판매된 제품 카테고리(카테고리)별 총 판매액(판매액) 데이터가 있다고 가정해 봅시다. 각 지점의 분기별 제품 카테고리 판매 동향을 한눈에 보고 싶을 때, `sales_df.pivot_table(index='지점명', columns='분기', values='판매액', aggfunc='sum')`을 사용하면, 행은 '지점명', 열은 '분기'로 구성되고 각 셀에는 해당 지점의 분기별 총 판매액이 요약된 표를 얻을 수 있습니다. 이를 통해 특정 지점의 분기별 매출 변화나, 특정 분기에 매출이 급증한 지점을 쉽게 파악할 수 있습니다.

---

## Slide 6

핵심 개념 1: 관계형 인스턴스(DataFrame)의 변이(Mutate)

*   **설명:** 슬라이드의 `Note: Create mutates the relation instance...`는 Pandas DataFrame에서 새로운 데이터를 '생성(Create)'하는 작업이 기존의 DataFrame 객체 자체를 직접 변경(변이)한다는 것을 의미합니다. 즉, 새로운 DataFrame을 반환하는 것이 아니라, 현재 작업 중인 DataFrame에 직접적으로 변화를 가하는 방식입니다. 이는 데이터베이스 관리 시스템(DBMS)의 ERA(Entity-Relationship-Attribute) 쿼리 연산자와 유사하게, 데이터 구조의 상태를 직접 변경하는 조작임을 강조합니다.
*   **구체적 실생활 예시:** 여러분이 학교의 '학생 명단'을 관리하는 엑셀 파일을 가지고 있다고 가정해 봅시다.
    *   '새로운 학생 추가' 버튼을 눌러 명단에 새 이름을 입력하거나, '봉사활동 시간'이라는 새로운 열을 추가하는 것은 *바로 그 엑셀 파일 자체*를 수정하는 것입니다. 새로운 엑셀 파일이 만들어지는 것이 아니라, 기존의 파일에 변경 사항이 즉시 반영되어 저장됩니다. 이처럼 Pandas의 `Create` 작업도 `babynames`라는 DataFrame을 직접 수정하는 방식으로 동작합니다.

핵심 개념 2: 행 추가 (Appending Rows)

*   **설명:** DataFrame에 새로운 데이터 레코드(행)를 추가하는 방법입니다.
    *   **단일 행 추가:** `babynames.loc[len(babynames)] = [...]` 코드는 `loc` 인덱서를 사용하여 DataFrame의 현재 마지막 인덱스 다음 위치(즉, `len(babynames)` 값)에 새로운 단일 행 데이터를 삽입합니다. 이는 DataFrame의 끝에 한 줄을 추가하는 것과 같습니다.
    *   **여러 행 동시 추가 (Batch Append):** 슬라이드의 예시처럼 여러 개의 새로운 행 데이터를 리스트 형태의 튜플로 준비하고, 이를 `pd.DataFrame`으로 변환한 뒤, `pd.concat([기존 DataFrame, 새 행들 DataFrame], ignore_index=True)` 함수를 사용하여 기존 DataFrame에 효율적으로 합치는 방법입니다. `ignore_index=True`는 기존 인덱스를 무시하고 새로운 연속적인 인덱스를 부여하도록 합니다. 이 방식은 단일 행을 여러 번 반복해서 추가하는 것보다 대량의 데이터를 추가할 때 훨씬 빠르고 효율적입니다.
*   **구체적 실생활 예시:** 온라인 서점의 '신간 도서 목록' DataFrame이 있다고 생각해 봅시다.
    *   **단일 행 추가:** 어느 날, '오늘의 베스트셀러'로 한 권의 책이 선정되어 급히 목록에 추가해야 합니다. 이 책의 정보(제목, 저자, 출판일 등)를 '신간 도서 목록'의 *가장 마지막 줄*에 한 줄로 추가합니다. (`book_list.loc[len(book_list)] = ["책 제목", "저자", "2024-03-01", ...])`
    *   **여러 행 동시 추가:** 매달 초에는 수십 권의 새로운 도서가 대량으로 입고됩니다. 이 모든 신간 도서들을 하나씩 추가하는 대신, 출판사로부터 받은 신간 도서 목록(엑셀 파일 등)을 바탕으로 새 도서 정보들을 리스트로 만들고, 이를 DataFrame으로 변환하여 기존 '신간 도서 목록' DataFrame에 *한꺼번에 병합*합니다. 이 방법은 수십 번의 개별 추가 작업보다 훨씬 빠르고 효율적으로 목록을 업데이트할 수 있습니다.

핵심 개념 3: 열 파생 및 삽입 (Derive and Insert Columns)

*   **설명:** 기존 데이터를 바탕으로 새로운 열을 만들거나, 새로운 열을 DataFrame의 특정 위치에 추가하는 방법입니다.
    *   **열 파생 (Derive):** `babynames["decade"] = (babynames["Year"] // 10) * 10` 코드는 기존 "Year" 열의 값들을 사용하여 "decade" (연대, 예: 1990년, 2000년)라는 새로운 열을 계산하고 생성합니다. 이는 기존 데이터로부터 새로운 의미 있는 정보를 추출하여 DataFrame에 추가하는 것입니다.
    *   **열 삽입 (Insert):** `babynames.insert(0, "state_sex", babynames["State"].str.cat(babynames["Sex"], sep="-"))` 코드는 "State"와 "Sex" 열의 문자열을 "-"로 연결하여 "state_sex"라는 새로운 열을 생성하고, 이 열을 DataFrame의 *가장 첫 번째(인덱스 0) 위치*에 삽입합니다. `insert` 메서드를 사용하면 단순히 열을 추가하는 것을 넘어, 원하는 정확한 위치에 열을 배치할 수 있습니다.
*   **구체적 실생활 예시:** 한 마케팅 회사의 '고객 정보' DataFrame이 있다고 합시다.
    *   **열 파생:** '고객 정보'에는 '가입일'과 '최근 구매일' 열이 있습니다. 마케팅팀은 이 두 정보를 활용하여 고객의 '활동 기간' (예: `최근 구매일 - 가입일`)이라는 *새로운 열을 파생*시킬 수 있습니다. 이를 통해 고객의 충성도를 분석하는 데 활용할 수 있습니다. (`customers["Activity_Period"] = customers["Latest_Purchase_Date"] - customers["Join_Date"]`)
    *   **열 삽입:** 회사 정책이 변경되어 '고객 ID'와 '회원 등급'을 결합한 '통합 고객 코드'를 가장 중요하게 관리해야 한다고 결정했습니다. 이 '통합 고객 코드'는 다른 어떤 정보보다 먼저 표시되어야 합니다. 마케팅 관리자는 `customers.insert(0, "Combined_Customer_Code", customers["Customer_ID"].str.cat(customers["Membership_Tier"], sep="-"))` 코드를 사용하여 '통합 고객 코드' 열을 생성하고, 이 열을 '고객 정보' DataFrame의 *가장 왼쪽(첫 번째) 열*로 추가합니다. 이렇게 하면 필요한 정보를 한눈에 빠르게 파악할 수 있습니다.

---

## Slide 7

데이터 업데이트는 Pandas DataFrame 내의 기존 데이터를 수정하는 핵심적인 작업입니다. 특정 조건에 따라 데이터를 정정하거나, 표준화하거나, 새로운 파생 변수를 생성하는 데 사용됩니다. 아래에서는 슬라이드에 제시된 네 가지 주요 업데이트 기법을 상세히 설명하고, 각 기법이 언제 유용하게 쓰일 수 있는지 실생활 예시를 통해 알아보겠습니다.

---

### 1. Point Update (포인트 업데이트)

**개념**: DataFrame에서 특정 조건을 만족하는 **단일 레코드 또는 아주 소수의 특정 레코드**에 대해 특정 컬럼의 값을 수정하는 방식입니다. 마치 지도에서 특정 지점(point)을 찾아 정보를 수정하는 것과 같습니다.

**코드 예시**:

```python
ix = (babynames["Name"]=="Mary") & (babynames["Year"]==1910)
babynames.loc[ix, "Count"] = babynames.loc[ix, "Count"] + 1
```

**실생활 예시**:
온라인 쇼핑몰의 `orders` DataFrame이 있다고 가정해 봅시다. 이 DataFrame에는 주문 번호, 고객 이름, 상품명, 수량 등의 정보가 있습니다.
한 고객이 실수로 특정 상품의 수량을 잘못 입력하여 주문했다고 가정해 보세요. 예를 들어, `주문 번호 12345`에 있는 `아이폰15`의 `수량`을 `1`에서 `2`로 수정해야 하는 경우입니다.

```python
# 가상의 orders DataFrame
# orders = pd.DataFrame({
#     'Order_ID': [12345, 12345, 12346],
#     'Customer_Name': ['김철수', '김철수', '이영희'],
#     'Product_Name': ['아이폰15', '에어팟프로', '갤럭시워치'],
#     'Quantity': [1, 1, 1]
# })

# 특정 주문(Order_ID=12345)의 특정 상품(Product_Name='아이폰15')의 수량을 1 증가시키는 경우
specific_order = (orders["Order_ID"] == 12345) & (orders["Product_Name"] == "아이폰15")
orders.loc[specific_order, "Quantity"] = orders.loc[specific_order, "Quantity"] + 1
```
이처럼 `Point update`는 정확한 조건으로 한정되는 데이터를 수정할 때 유용합니다.

---

### 2. Conditional Update (조건부 업데이트)

**개념**: DataFrame에서 **특정 조건을 만족하는 모든 레코드**에 대해 특정 컬럼의 값을 일괄적으로 수정하는 방식입니다. 여러 데이터에 동일한 규칙을 적용하여 변경할 때 사용됩니다.

**코드 예시**:

```python
low = babynames["Count"] < 10
babynames.loc[low, "Count"] = 0
```

**실생활 예시**:
은행에서 `customer_accounts` DataFrame을 관리하고 있다고 가정해 봅시다. 이 DataFrame에는 고객의 계좌 번호, 잔액, 계좌 상태 등의 정보가 있습니다.
은행 정책상 **잔액이 10만원 미만인 모든 계좌**에 대해 `계좌 상태`를 '휴면 계좌 고려'로 변경해야 하는 경우입니다.

```python
# 가상의 customer_accounts DataFrame
# customer_accounts = pd.DataFrame({
#     'Account_ID': [1001, 1002, 1003, 1004],
#     'Balance': [50000, 150000, 80000, 200000],
#     'Account_Status': ['Active', 'Active', 'Active', 'Active']
# })

# 잔액이 100000 미만인 모든 계좌의 'Account_Status'를 'Dormant_Consideration'으로 변경
low_balance = customer_accounts["Balance"] < 100000
customer_accounts.loc[low_balance, "Account_Status"] = "Dormant_Consideration"
```
이처럼 `Conditional update`는 특정 조건에 해당하는 다수의 데이터를 일괄적으로 처리할 때 효율적입니다.

---

### 3. Map / Replace (매핑/교체)

**개념**: 특정 컬럼 내의 값을 다른 값으로 일괄적으로 **대체**하는 방식입니다. 주로 데이터의 표준화를 위해 사용되며, 기존 값을 새로운 값으로 '매핑'하여 변경합니다. `replace()` 메서드는 딕셔너리를 사용하여 여러 값을 동시에 매핑할 수 있습니다.

**코드 예시**:

```python
babynames["Sex"] = babynames["Sex"].replace({"F":"Female", "M":"Male"})
```

**실생활 예시**:
설문조사 데이터를 분석한다고 가정해 봅시다. `survey_data` DataFrame에는 응답자의 `성별` 컬럼이 있는데, 이 컬럼에 'M', 'm' (남자), 'F', 'f' (여자)와 같이 다양한 형태로 입력된 값이 섞여 있을 수 있습니다. 분석의 일관성을 위해 이 값들을 'Male'과 'Female'로 표준화해야 합니다.

```python
# 가상의 survey_data DataFrame
# survey_data = pd.DataFrame({
#     'Respondent_ID': [1, 2, 3, 4, 5],
#     'Gender': ['M', 'f', 'Male', 'F', 'm'],
#     'Age': [25, 30, 35, 28, 40]
# })

# 'Gender' 컬럼의 값을 'M', 'm'은 'Male'로, 'F', 'f'는 'Female'로 일괄 변경
gender_mapping = {"M": "Male", "m": "Male", "F": "Female", "f": "Female"}
survey_data["Gender"] = survey_data["Gender"].replace(gender_mapping)
```
`Map / Replace`는 데이터 입력 오류를 수정하거나, 범주형 데이터를 일관된 형태로 만들 때 매우 유용합니다.

---

### 4. Where/Mask Idiom (조건부 할당 / 마스크 이디엄)

**개념**: NumPy의 `np.where()` 함수를 활용하여, 특정 조건(mask)에 따라 DataFrame의 새로운 컬럼을 생성하거나 기존 컬럼의 값을 조건적으로 할당하는 방식입니다. 조건이 참(True)일 때의 값과 거짓(False)일 때의 값을 명시하여 분기 처리가 가능합니다.

**코드 예시**:

```python
high = babynames["Count"] >= 100
babynames["pop_flag"] = np.where(high, "popular", "normal")
```

**실생활 예시**:
학생들의 성적을 관리하는 `students` DataFrame이 있다고 가정해 봅시다. 이 DataFrame에는 학생 이름, 점수, 그리고 합격 여부를 나타낼 `Pass_Fail` 컬럼이 있습니다.
**점수가 60점 이상이면 'Pass'로, 그렇지 않으면 'Fail'로** `Pass_Fail` 컬럼에 값을 할당해야 합니다.

```python
import numpy as np # np.where를 사용하기 위해 numpy import

# 가상의 students DataFrame
# students = pd.DataFrame({
#     'Student_ID': [100, 101, 102, 103],
#     'Score': [75, 50, 88, 60],
#     'Grade': ['B', 'F', 'A', 'C']
# })

# 점수가 60점 이상인 경우 'Pass', 그렇지 않은 경우 'Fail'로 'Pass_Fail' 컬럼 생성
passing_condition = students["Score"] >= 60
students["Pass_Fail"] = np.where(passing_condition, "Pass", "Fail")
```
`Where/Mask idiom`은 복잡한 조건에 따라 새로운 범주형 컬럼을 만들거나 기존 컬럼의 값을 조건적으로 변환할 때 매우 강력하고 직관적인 방법입니다.

---

## Slide 8

슬라이드에서 다루는 핵심 개념은 Pandas DataFrame에서 데이터(컬럼 또는 행)를 삭제하는 다양한 방법입니다.

---

### **핵심 개념: Pandas DataFrame에서 데이터 삭제하기**

Pandas DataFrame에서 특정 컬럼(속성)이나 행(튜플)을 삭제하는 방법을 예시 코드를 통해 설명하고 있습니다. `Note`에서 언급했듯이, 여기서의 `Delete` 작업은 실제 데이터 구조를 변경하는 구체적인 명령이며, 추상적인 관계 대수(ERA) 쿼리와는 다릅니다.

#### **1. 컬럼 삭제 및 반환 (`.pop()` 사용)**

*   **설명:** `pop()` 메서드는 DataFrame에서 지정된 컬럼을 제거하고, 제거된 컬럼의 데이터를 Pandas Series 형태로 반환합니다. 컬럼을 일시적으로 분리하거나 다른 용도로 사용한 후 주 DataFrame에서 제거할 때 유용합니다.
*   **예시 코드:**
    ```python
    cnt = babynames.pop("Count") # "Count" 컬럼을 삭제하고 그 내용을 cnt에 저장
    # babynames DataFrame에서는 이제 "Count" 컬럼이 없음
    # babynames["Count"] = cnt # 필요하다면 나중에 다시 추가할 수도 있음
    ```
*   **실생활 예시:**
    당신이 한 프로젝트 팀의 팀장이고, 팀원들의 개인별 성과 점수(예: `score_A`, `score_B`, `score_C`)와 최종 종합 점수(`total_score`)를 기록한 스프레드시트(`DataFrame`)를 관리하고 있다고 가정해 봅시다. `total_score`는 다른 점수들의 합계로 계산된 값입니다.
    
    어느 날 상사가 `total_score` 컬럼만 따로 모아 분석한 보고서를 요구했습니다. 이때 당신은 `babynames.pop("Count")`와 유사하게, `team_data.pop("total_score")`를 사용해 `total_score` 컬럼을 메인 스프레드시트에서 **제거하면서 동시에 그 데이터를 `total_scores_for_report`라는 별도의 리스트(Series)로 추출**할 수 있습니다. 메인 스프레드시트는 이제 `total_score` 컬럼 없이 깔끔하게 유지되고, 당신은 추출한 `total_scores_for_report` 데이터로 상사에게 필요한 보고서를 작성할 수 있습니다.

#### **2. 특정 라벨(인덱스)을 기준으로 행 삭제 (`.drop()` 사용)**

*   **설명:** `drop()` 메서드는 특정 라벨(행 인덱스 또는 컬럼 이름)을 지정하여 DataFrame에서 해당 행 또는 컬럼을 제거합니다. `index` 파라미터를 사용하여 제거할 행의 인덱스를 전달합니다.
*   **예시 코드:**
    ```python
    to_remove = babynames.index[:2] # 첫 두 행의 인덱스를 선택
    babynames = babynames.drop(index=to_remove) # 해당 인덱스의 행들을 삭제
    ```
*   **실생활 예시:**
    당신이 온라인 쇼핑몰의 고객 주문 목록(`DataFrame`)을 관리하고 있습니다. 이 목록에는 고객 ID, 주문 상품, 수량, 배송 상태 등 여러 정보가 포함되어 있습니다. 목록의 상위 2개 주문(인덱스 0과 1)은 테스트 목적으로 입력된 가짜 주문 데이터였습니다.
    
    이때 `babynames.index[:2]`와 유사하게 `order_list.index[:2]`를 사용하여 **목록의 첫 두 행(가짜 주문)의 인덱스를 정확히 지정**하고, `order_list = order_list.drop(index=first_two_orders)`를 통해 이 가짜 주문들을 주문 목록에서 **영구적으로 제거**할 수 있습니다. 이렇게 하면 실제 유효한 주문 데이터만 남게 됩니다.

#### **3. 조건에 따라 행 삭제 (`.drop()` + 불리언 인덱싱 사용)**

*   **설명:** 특정 조건을 만족하는 행들을 선택하고, 그 행들의 인덱스를 `drop()` 메서드에 전달하여 제거하는 방법입니다. 이는 대량의 데이터에서 특정 기준에 미달하거나 불필요한 데이터를 일괄적으로 제거할 때 매우 유용합니다.
*   **예시 코드:**
    ```python
    old_rare = (babynames["Year"] < 1920) & (babynames["Count"] < 5) # 1920년 이전 & 등장 횟수 5회 미만 조건
    babynames = babynames.drop(index=babynames[old_rare].index) # 조건을 만족하는 행들을 삭제
    ```
*   **실생활 예시:**
    당신이 도서관의 책 재고 목록(`DataFrame`)을 담당하고 있습니다. 이 목록에는 책 제목, 저자, 출판 연도, 재고 수량 등의 정보가 있습니다. 도서관에서는 오래되고 인기가 없어 거의 대출되지 않는 책들을 정리하려고 합니다.
    
    조건은 다음과 같습니다: **"1990년 이전에 출판되었으면서 동시에 현재 재고 수량이 2권 미만인 책"** 들을 폐기합니다.
    
    `old_rare` 변수와 유사하게, `to_discard = (book_inventory["출판연도"] < 1990) & (book_inventory["재고수량"] < 2)`와 같은 불리언 조건을 만듭니다. 이 조건에 맞는 책들(행들)의 인덱스를 `book_inventory[to_discard].index`로 추출한 다음, `book_inventory = book_inventory.drop(index=book_inventory[to_discard].index)`를 사용하여 해당 책들을 재고 목록에서 **자동으로 삭제**할 수 있습니다. 이는 수많은 책 중에서 폐기 대상을 수동으로 찾는 번거로움을 크게 줄여줍니다.

---

**중요 참고:** `babynames = babynames.drop(...)`와 같이 삭제 후 재할당하는 것을 볼 수 있습니다. Pandas의 `drop()` 메서드는 기본적으로 원본 DataFrame을 직접 수정하는 대신, 변경된 내용을 담은 **새로운 DataFrame을 반환**합니다. 만약 원본 DataFrame을 바로 수정하고 싶다면 `inplace=True` 옵션을 사용할 수 있지만, 데이터를 실수로 잃는 것을 방지하기 위해 새 DataFrame을 반환받아 재할당하는 방식이 더 안전하고 일반적입니다.

---

## Slide 9

### 핵심 개념: 관계형 대수(Relational Algebra)의 '선택' (Selection, $\sigma$) 연산

**설명:**

'선택' 연산은 데이터베이스나 데이터프레임에서 특정 조건을 만족하는 **행(Row/Tuple)**들만을 추출하는 데 사용됩니다. 이 연산은 원본 테이블(Relation)의 **열(Column/Attribute) 구조는 그대로 유지**하면서, 조건에 부합하는 행들만 걸러내는 역할을 합니다.

수학적인 표기법으로는 $\sigma_\theta(R)$ 로 표현되며, 여기서 $R$은 원본 데이터셋(테이블), $\theta$는 필터링할 조건(Predicate)을 의미합니다. 슬라이드의 예시처럼 `Year`가 1910년이고 `Sex`가 'F'로 시작하는 행만 선택하는 것이 대표적인 사용 예시입니다.

**구체적이고 실생활에 가까운 예시: 온라인 쇼핑몰 상품 검색**

당신이 온라인 쇼핑몰에서 특정 조건의 상품을 찾고 있다고 가정해 봅시다. 쇼핑몰에는 수많은 상품이 등록되어 있으며, 이 모든 상품 정보가 하나의 거대한 데이터프레임(`products_df`)에 저장되어 있다고 생각할 수 있습니다. 각 상품은 '상품명', '카테고리', '가격', '브랜드', '평점', '재고' 등의 열을 가지고 있습니다.

1.  **원본 데이터셋 (R):** 쇼핑몰의 `products_df` (모든 상품 정보가 담긴 테이블).
2.  **당신의 검색 조건 ($\theta$):**
    *   "카테고리"가 '가전제품'이어야 하고,
    *   "가격"이 50만 원 이상 100만 원 이하여야 하며,
    *   "평점"이 4.5점 이상인 상품.

3.  **'선택' 연산 적용:** 당신이 검색창에 위 조건을 입력하고 검색 버튼을 누르면, 쇼핑몰 시스템은 '선택' 연산을 사용하여 `products_df`에서 이 모든 조건을 만족하는 상품들만을 찾아 보여줍니다.

4.  **Pandas 코드로 이해하기 (슬라이드 예시와 유사):**
    ```python
    import pandas as pd

    # 예시 데이터프레임 생성
    data = {
        '상품명': ['스마트폰', '노트북', '무선 이어폰', '태블릿', '공기청정기', '스마트워치'],
        '카테고리': ['가전제품', '가전제품', '액세서리', '가전제품', '가전제품', '액세서리'],
        '가격': [800000, 1200000, 150000, 700000, 450000, 300000],
        '브랜드': ['S전자', 'L사', 'A사', 'S전자', 'D사', 'G사'],
        '평점': [4.7, 4.3, 4.8, 4.6, 3.9, 4.1]
    }
    products_df = pd.DataFrame(data)

    print("--- 원본 상품 데이터프레임 ---")
    print(products_df)

    # 검색 조건 (mask) 생성
    # 슬라이드의 mask = (babynames["Year"]==1910) & (babynames["Sex"].str.startswith("F")) 와 동일한 방식
    search_mask = (
        (products_df["카테고리"] == "가전제품") &
        (products_df["가격"] >= 500000) &
        (products_df["가격"] <= 1000000) &
        (products_df["평점"] >= 4.5)
    )

    # 마스크를 사용하여 행 선택 (Selection)
    # 슬라이드의 sel = babynames.loc[mask] 와 동일한 방식
    filtered_products = products_df.loc[search_mask]

    print("\n--- 검색 조건에 맞는 상품 (선택 연산 결과) ---")
    print(filtered_products)
    ```

**결과:**

이 '선택' 연산을 통해 얻은 `filtered_products` 데이터프레임은 원본 `products_df`와 동일한 '상품명', '카테고리', '가격' 등의 열을 가지고 있지만, 당신이 지정한 모든 검색 조건을 만족하는 상품(이 예시에서는 '스마트폰'과 '태블릿')들로만 구성됩니다. 이것이 바로 관계형 대수의 '선택' 연산이 실생활에서 데이터를 필터링하는 방식으로 활용되는 예시입니다.

---

## Slide 10

## 핵심 개념: 일반화된 투영 (Generalized Projection)

일반화된 투영(Generalized Projection)은 관계형 데이터베이스에서 특정 컬럼(속성)을 선택하는 기본적인 '투영(Projection)' 개념을 확장한 것입니다. 단순히 존재하는 컬럼을 선택하는 것을 넘어, 기존 컬럼에 '연산(expressions)'을 적용하여 새로운 컬럼을 만들고, 그 결과를 새로운 이름으로 지정하여(alias) 데이터셋에 포함시키는 작업입니다.

### 주요 구성 요소

*   **`$e_i$` (표현식/Expression):** 기존 컬럼의 데이터를 조작하거나 변형하는 함수 또는 계산식입니다. 예를 들어, 문자열을 자르거나(SUBSTR), 길이를 계산하거나(LEN), 두 숫자 컬럼을 더하거나 곱하는 등의 연산이 포함됩니다.
*   **`$B_i$` (새로운 속성/New Attribute):** `$e_i$` 표현식을 통해 생성된 새로운 컬럼에 부여되는 이름입니다. 이는 원본 컬럼과 다른 새 이름을 가질 수 있습니다.
*   **`R` (원본 관계/테이블):** 연산이 적용될 원본 데이터셋 또는 테이블입니다.
*   **결과:** 원본 컬럼 중 일부와 새로 파생된 컬럼들로 구성된 새로운 테이블(관계)입니다. 각 행에 대해 독립적으로 연산이 수행되며, **집계(aggregation)는 포함하지 않습니다.** 즉, 여러 행을 묶어서 하나의 값을 계산하는 것이 아니라, 각 행의 데이터를 기반으로 새로운 값을 만듭니다.

### 구체적이고 실생활에 가까운 예시

온라인 상점에서 고객의 `주문(Orders)` 데이터를 분석하는 상황을 가정해 봅시다. 원본 데이터에는 `OrderID`, `ProductName`, `UnitPrice`(개별 상품 가격), `Quantity`(주문 수량), `DiscountRate`(할인율) 컬럼이 있습니다. 우리는 이 데이터를 활용하여 각 주문의 `TotalPrice`(할인 전 총 가격)와 `FinalPrice`(할인 후 최종 가격)를 계산하고 싶습니다.

#### 1. 원본 데이터 (예시)

| OrderID | ProductName | UnitPrice | Quantity | DiscountRate |
| :------ | :---------- | :-------- | :------- | :----------- |
| 101     | Laptop      | 1200      | 1        | 0.1          |
| 102     | Mouse       | 25        | 2        | 0.05         |
| 103     | Keyboard    | 75        | 1        | 0.0          |

#### 2. 일반화된 투영 적용

우리는 다음과 같은 연산을 통해 새로운 컬럼을 파생시킬 수 있습니다.

*   **`TotalPrice` 계산:** `UnitPrice` * `Quantity`
*   **`FinalPrice` 계산:** `(UnitPrice` * `Quantity)` * `(1 - DiscountRate)`

**ERA (관계형 대수) 관점:**

$\pi_{\text{OrderID, ProductName, UnitPrice, Quantity, DiscountRate, (UnitPrice * Quantity) } \to \text{TotalPrice, (UnitPrice * Quantity * (1 - DiscountRate)) } \to \text{FinalPrice}}(\text{Orders})$

이 표기법은 `Orders` 테이블에서 `OrderID`, `ProductName`, `UnitPrice`, `Quantity`, `DiscountRate` 컬럼을 유지하고, 추가로 두 개의 파생 컬럼 `TotalPrice`와 `FinalPrice`를 생성하라는 의미입니다.

#### 3. 결과 데이터 (예상)

| OrderID | ProductName | UnitPrice | Quantity | DiscountRate | TotalPrice | FinalPrice |
| :------ | :---------- | :-------- | :------- | :----------- | :--------- | :--------- |
| 101     | Laptop      | 1200      | 1        | 0.1          | 1200       | 1080       |
| 102     | Mouse       | 25        | 2        | 0.05         | 50         | 47.5       |
| 103     | Keyboard    | 75        | 1        | 0.0          | 75         | 75         |

#### 4. Pandas를 이용한 구현

Python의 Pandas 라이브러리에서는 `.assign()` 메서드를 사용하여 일반화된 투영을 쉽게 구현할 수 있습니다.

```python
import pandas as pd

# 1. 원본 데이터프레임 생성
data = {
    'OrderID': [101, 102, 103],
    'ProductName': ['Laptop', 'Mouse', 'Keyboard'],
    'UnitPrice': [1200, 25, 75],
    'Quantity': [1, 2, 1],
    'DiscountRate': [0.1, 0.05, 0.0]
}
df_orders = pd.DataFrame(data)

print("--- 원본 주문 데이터 ---")
print(df_orders)
print("\n" + "="*30 + "\n")

# 2. 일반화된 투영 적용: 새로운 컬럼 'TotalPrice'와 'FinalPrice' 생성
# 그리고 원하는 컬럼만 선택하여 새로운 데이터프레임 생성
df_processed_orders = (df_orders
    .assign(
        # e1: UnitPrice * Quantity --> B1: TotalPrice
        TotalPrice=lambda x: x['UnitPrice'] * x['Quantity'],
        # e2: (UnitPrice * Quantity * (1 - DiscountRate)) --> B2: FinalPrice
        FinalPrice=lambda x: x['UnitPrice'] * x['Quantity'] * (1 - x['DiscountRate'])
    )
    # 마지막으로 원하는 컬럼들만 최종적으로 선택 (투영)
    [['OrderID', 'ProductName', 'TotalPrice', 'FinalPrice']]
)

print("--- 일반화된 투영 적용 후 데이터 ---")
print(df_processed_orders)
```

**설명:**

1.  `df_orders.assign(...)`: `assign` 메서드는 새로운 컬럼을 생성합니다. 여기서는 `TotalPrice`와 `FinalPrice`라는 두 개의 새 컬럼을 정의합니다. `lambda x: ...`는 각 행에 대해 `x` (데이터프레임 자체)를 사용하여 컬럼 값을 계산하는 익명 함수를 정의합니다.
    *   `TotalPrice=lambda x: x['UnitPrice'] * x['Quantity']`: `UnitPrice` 컬럼과 `Quantity` 컬럼의 값을 곱하여 `TotalPrice` 컬럼의 값을 계산합니다. 이것이 `$e_1 \to B_1$`에 해당합니다.
    *   `FinalPrice=lambda x: x['UnitPrice'] * x['Quantity'] * (1 - x['DiscountRate'])`: `TotalPrice` 계산식에 `(1 - DiscountRate)`를 곱하여 `FinalPrice`를 계산합니다. 이것이 `$e_2 \to B_2$`에 해당합니다.
2.  `[['OrderID', 'ProductName', 'TotalPrice', 'FinalPrice']]`: `.assign()`으로 새로운 컬럼들이 추가된 데이터프레임에서 최종적으로 필요한 컬럼들(`OrderID`, `ProductName`, `TotalPrice`, `FinalPrice`)만 선택하여 새로운 데이터프레임을 반환합니다. 이는 일반적인 '투영' 개념으로, 필요한 컬럼만 추출하는 단계입니다.

이처럼 일반화된 투영은 데이터 분석 및 전처리 과정에서 기존 데이터를 기반으로 새로운 통찰력을 제공하는 파생 변수를 생성할 때 매우 유용하게 활용됩니다.

---

## Slide 11

## 핵심 개념: 데이터프레임 컬럼(속성) 이름 변경 (`Rename`)

이 슬라이드의 핵심은 데이터프레임(또는 관계형 데이터 모델의 '관계') 내에서 **컬럼(속성)의 이름을 변경**하는 연산입니다. 중요한 점은 컬럼의 이름만 바뀌고, 그 컬럼이 가지고 있는 실제 데이터 값은 전혀 변경되지 않는다는 것입니다.

### 1. 개념 설명

*   **정의:** 데이터를 담고 있는 테이블이나 데이터프레임에서 특정 컬럼(열)의 식별자를 더 명확하거나 일관된 이름으로 바꾸는 과정입니다.
*   **관계 대수 (Formal/ERA Query):** `ρ_A→A'(R)` 형식으로 표현됩니다. 이는 관계(Relation) `R`에서 속성(Attribute) `A`를 `A'`로 이름을 변경한다는 의미입니다. 슬라이드의 예시에서는 `ρ_Count→freq(babynames)`로, `babynames` 데이터프레임에서 `Count`라는 컬럼의 이름을 `freq`로 변경합니다.
*   **Pandas 구현:** Python의 Pandas 라이브러리에서는 `.rename()` 메서드를 사용하여 컬럼 이름을 변경합니다. 주로 `df.rename(columns={"기존_컬럼명": "새로운_컬럼명"})` 형태로 사용됩니다.

### 2. 구체적인 실생활 예시

데이터 분석이나 개발 과정에서 컬럼 이름을 변경해야 하는 상황은 매우 흔합니다. 몇 가지 예시를 들어보겠습니다.

---

**예시 1: 온라인 쇼핑몰 판매 데이터 분석**

당신이 온라인 쇼핑몰의 판매 데이터를 분석하고 있다고 가정해봅시다. 여러 부서에서 수집된 데이터를 통합해야 하는데, 각 부서마다 동일한 정보를 다른 컬럼 이름으로 사용하고 있습니다.

*   **기존 데이터 (DataFrame: `sales_data`)**
    ```
    상품코드  가격    수량  판매일
    P001   10000  2     2023-01-05
    P002   5000   1     2023-01-05
    ...
    ```
    여기서 '상품코드'는 Product ID를 의미하고, '수량'은 Quantity를 의미합니다. 다른 부서에서 가져온 데이터에는 'prod_id', 'qty_sold' 와 같은 영어 컬럼명이 사용되고 있어 통일이 필요합니다.

*   **문제점:** 컬럼 이름이 한글이거나, 다른 데이터 소스와 통합 시 이름이 일관되지 않아 혼란을 주거나 자동화된 스크립트 실행에 어려움을 줍니다.

*   **컬럼 이름 변경 (Pandas):**
    데이터 분석 표준을 위해 컬럼 이름을 영어로 바꾸고, 더 명확하게 변경합니다.
    ```python
    import pandas as pd

    # 예시 데이터프레임 생성
    sales_data = pd.DataFrame({
        '상품코드': ['P001', 'P002', 'P003'],
        '가격': [10000, 5000, 15000],
        '수량': [2, 1, 3],
        '판매일': ['2023-01-05', '2023-01-05', '2023-01-06']
    })

    print("--- 변경 전 데이터프레임 ---")
    print(sales_data)
    print("\n")

    # '상품코드'를 'ProductID'로, '수량'을 'QuantitySold'로 변경
    sales_data_renamed = sales_data.rename(columns={
        "상품코드": "ProductID",
        "수량": "QuantitySold"
    })

    print("--- 변경 후 데이터프레임 ---")
    print(sales_data_renamed)
    ```

*   **결과:**
    ```
    --- 변경 전 데이터프레임 ---
      상품코드     가격  수량        판매일
    0   P001  10000   2  2023-01-05
    1   P002   5000   1  2023-01-05
    2   P003  15000   3  2023-01-06


    --- 변경 후 데이터프레임 ---
      ProductID     가격  QuantitySold        판매일
    0      P001  10000             2  2023-01-05
    1      P002   5000             1  2023-01-05
    2      P003  15000             3  2023-01-06
    ```
    `상품코드` 컬럼은 `ProductID`로, `수량` 컬럼은 `QuantitySold`로 이름이 변경되었지만, 각 컬럼 내의 숫자나 문자열 값들은 전혀 바뀌지 않고 그대로 유지됩니다. 이처럼 컬럼 이름을 변경하여 데이터의 의미를 명확히 하고, 다른 데이터셋과의 병합을 용이하게 할 수 있습니다.

---

## Slide 12

**핵심 개념: 중복 제거 (Duplicate Elimination, $\delta(R)$)**

**설명:**
중복 제거는 데이터 집합에서 완전히 동일한 항목(튜플 또는 행)들을 단 하나만 남기고 나머지는 모두 제거하여, 각 항목이 유일하게 존재하도록 만드는 연산입니다. 이는 데이터를 '집합(set)'처럼 다루는 것으로, 집합의 원소는 중복될 수 없다는 수학적 개념을 따릅니다.

**1. 핵심 원리:**
*   **Formal (형식적 정의):** `Remove duplicate tuples (set semantics)`
    *   데이터베이스나 데이터 처리에서 '튜플'은 한 레코드 또는 한 행을 의미합니다. 'set semantics'는 결과 데이터가 수학적 집합의 특성을 가지며, 모든 요소가 고유해야 함을 뜻합니다. 즉, 중복된 행을 제거하여 유일한 행들만 남깁니다.

**2. 관계 대수(ERA)에서의 표현:**
*   **ERA (Query):** $\delta(\pi_{Year, Name}(\text{babynames}))$
*   **Meaning (의미):** `Unique pairs of (Year, Name)`
    *   $\pi_{Year, Name}(\text{babynames})$: 'babynames'라는 테이블(또는 데이터프레임)에서 'Year'와 'Name' 두 컬럼만 선택(투영)하는 연산입니다.
    *   $\delta(...)$: 선택된 'Year'와 'Name' 컬럼의 조합들 중에서 중복되는 모든 쌍을 제거하고, 고유한 ('Year', 'Name') 쌍들만 남기라는 의미입니다.

**3. Pandas에서의 구현:**
*   **pandas:** `df.drop_duplicates()`
    *   Pandas 데이터프레임(`df`)에서 중복된 행을 제거하는 편리한 메서드입니다. 기본적으로 모든 컬럼의 값이 동일한 행을 중복으로 간주하여 제거합니다. `subset` 인자를 사용하여 특정 컬럼들의 조합을 기준으로 중복을 제거할 수 있습니다.
    *   `unique_year_name = babynames[["Year", "Name"]].drop_duplicates()`:
        *   `babynames[["Year", "Name"]]`: 'babynames' 데이터프레임에서 'Year'와 'Name' 컬럼만 선택하여 새로운 임시 데이터프레임을 만듭니다.
        *   `.drop_duplicates()`: 이렇게 선택된 ('Year', 'Name') 쌍들 중에서 정확히 일치하는 중복을 제거하여, 고유한 ('Year', 'Name') 조합들만 `unique_year_name` 변수에 저장합니다.

**구체적이고 실생활에 가까운 예시: 온라인 쇼핑몰 주문 데이터**

어떤 온라인 쇼핑몰에서 고객들의 `주문 기록`을 관리하는 `orders` 데이터프레임이 있다고 가정해 봅시다. 이 데이터프레임은 다음과 같은 컬럼을 가질 수 있습니다: `OrderID`, `CustomerID`, `ProductName`, `Quantity`, `OrderDate`, `DeliveryStatus`.
간혹 시스템 오류나 고객의 실수로 동일한 주문 기록이 중복해서 입력될 수 있습니다.

**예시 시나리오:**
다음과 같은 `orders` 데이터프레임이 있습니다.

| OrderID | CustomerID | ProductName | Quantity | OrderDate  | DeliveryStatus |
| :------ | :--------- | :---------- | :------- | :--------- | :------------- |
| ORD001  | CUST001    | 노트북      | 1        | 2023-10-26 | 배송 완료      |
| ORD002  | CUST002    | 스마트폰    | 1        | 2023-10-26 | 배송 중        |
| ORD001  | CUST001    | 노트북      | 1        | 2023-10-26 | 배송 완료      |
| ORD003  | CUST001    | 키보드      | 1        | 2023-10-27 | 배송 준비      |
| ORD002  | CUST002    | 스마트폰    | 1        | 2023-10-26 | 배송 중        |
| ORD004  | CUST003    | 마우스      | 2        | 2023-10-27 | 배송 준비      |

**문제 1: 완전히 중복된 주문 기록을 제거하여 정확한 주문 내역을 파악하고 싶을 때**
*   **목표:** `OrderID`, `CustomerID`, `ProductName`, `Quantity`, `OrderDate`, `DeliveryStatus`의 모든 값이 정확히 일치하는 중복 기록을 제거하여 순수한 유일한 주문 기록만 남기고자 합니다.
*   **Pandas 코드:**
    ```python
    unique_orders = orders.drop_duplicates()
    ```
*   **결과:**
    | OrderID | CustomerID | ProductName | Quantity | OrderDate  | DeliveryStatus |
    | :------ | :--------- | :---------- | :------- | :--------- | :------------- |
    | ORD001  | CUST001    | 노트북      | 1        | 2023-10-26 | 배송 완료      |
    | ORD002  | CUST002    | 스마트폰    | 1        | 2023-10-26 | 배송 중        |
    | ORD003  | CUST001    | 키보드      | 1        | 2023-10-27 | 배송 준비      |
    | ORD004  | CUST003    | 마우스      | 2        | 2023-10-27 | 배송 준비      |
    (원래 데이터에서 `(ORD001, CUST001, 노트북, 1, 2023-10-26, 배송 완료)`와 `(ORD002, CUST002, 스마트폰, 1, 2023-10-26, 배송 중)`이 각각 한 번씩 제거되었습니다.)

**문제 2: 특정 고객이 특정 날짜에 주문한 기록 (OrderID, CustomerID, OrderDate) 중 유일한 조합만 알고 싶을 때**
*   **목표:** 어떤 고객이 특정 날짜에 여러 개의 상품을 주문했거나, 같은 상품을 여러 번 주문했더라도, 그 고객이 그 날짜에 '주문을 했다'는 사실 자체를 유일하게 파악하고 싶을 때 사용합니다. 예를 들어, `(ORD001, CUST001, 2023-10-26)`이라는 조합이 여러 번 나타나더라도 한 번만 세고 싶을 때입니다.
*   **Pandas 코드 (슬라이드 예시와 유사):**
    ```python
    unique_order_info = orders[["OrderID", "CustomerID", "OrderDate"]].drop_duplicates()
    ```
*   **결과:**
    | OrderID | CustomerID | OrderDate  |
    | :------ | :--------- | :--------- |
    | ORD001  | CUST001    | 2023-10-26 |
    | ORD002  | CUST002    | 2023-10-26 |
    | ORD003  | CUST001    | 2023-10-27 |
    | ORD004  | CUST003    | 2023-10-27 |
    (원래 데이터에서 `(ORD001, CUST001, 2023-10-26)`과 `(ORD002, CUST002, 2023-10-26)`이 각각 한 번씩 제거되었습니다. `ProductName`, `Quantity`, `DeliveryStatus` 컬럼은 고려되지 않았으므로, 이 컬럼들이 달랐더라도 `OrderID`, `CustomerID`, `OrderDate` 조합이 같으면 중복으로 처리됩니다.)

이처럼 중복 제거는 데이터의 정확성을 높이고, 필요한 고유한 정보만을 추출하며, 분석 과정에서 중복 데이터로 인한 오류나 비효율성을 방지하는 데 매우 유용하게 사용됩니다.

---

## Slide 13

### 핵심 개념: 다중 열 정렬과 정렬 방향 지정 (Multi-Column Sorting with Specified Directions)

이 슬라이드의 핵심은 데이터를 여러 개의 기준 열(key columns)에 따라 정렬하되, 각 열에 대해 개별적으로 오름차순(ascending) 또는 내림차순(descending) 정렬 방식을 지정하는 방법입니다. 관계형 대수(ERA)에서는 $\tau$ 기호를 사용하여 이러한 정렬 작업을 표현하며, 파이썬의 `pandas` 라이브러리에서는 `sort_values()` 함수를 통해 쉽게 구현할 수 있습니다.

### 상세 설명

데이터를 정렬할 때 하나의 열만으로 충분하지 않은 경우가 많습니다. 예를 들어, 동점자가 있거나, 1차 정렬 기준으로는 같은 값을 가지는 레코드들이 있을 때, 2차, 3차 정렬 기준을 사용하여 데이터를 더 세밀하게 구조화할 필요가 있습니다.

1.  **정렬 기준의 우선순위**: 여러 열을 기준으로 정렬할 때는 정렬 기준이 되는 열들의 순서가 중요합니다. `["Year", "Count"]`와 같이 리스트로 열을 지정하면, 리스트의 첫 번째 열(`Year`)이 1차 정렬 기준이 되고, 그 다음 열(`Count`)이 2차 정렬 기준이 됩니다. 데이터는 먼저 1차 기준에 따라 정렬되고, 1차 기준 값이 동일한 레코드들에 한해 2차 기준에 따라 다시 정렬됩니다. 이 과정은 모든 지정된 열에 대해 반복됩니다.
2.  **각 열의 정렬 방향 지정**: 각 정렬 기준 열에 대해 오름차순(`True`) 또는 내림차순(`False`)을 개별적으로 지정할 수 있습니다. 예를 들어, `ascending=[True, False]`는 첫 번째 열(`Year`)은 오름차순으로, 두 번째 열(`Count`)은 내림차순으로 정렬하라는 의미입니다. 이는 매우 유연하며, 데이터를 분석 목적에 맞게 다양한 방식으로 조합하여 볼 수 있게 해줍니다.

### 구체적이고 실생활에 가까운 예시: 대학교 성적표 정렬

어느 대학교의 학과별 성적표를 정리하는 상황을 상상해 봅시다. 우리는 다음과 같은 기준으로 학생 데이터를 정렬하고 싶습니다.

*   **1차 기준**: 학과(`Major`)별로 정렬하되, 가나다순(오름차순)으로 정렬합니다.
*   **2차 기준**: 같은 학과 내에서는 학점(`GPA`)이 높은 학생을 먼저 보려고 합니다. 즉, 학점은 내림차순으로 정렬합니다.

**가상의 학생 데이터 (정렬 전)**

| 학과 (Major) | 이름 (Name) | 학년 (Year) | 학점 (GPA) |
| :----------- | :---------- | :---------- | :--------- |
| 컴퓨터공학   | 김철수      | 3           | 3.8        |
| 경영학       | 이영희      | 2           | 4.0        |
| 컴퓨터공학   | 박민수      | 4           | 3.9        |
| 경영학       | 최지아      | 3           | 3.5        |
| 디자인학     | 한준호      | 2           | 4.1        |
| 컴퓨터공학   | 정수진      | 3           | 3.8        |
| 디자인학     | 강은서      | 4           | 3.9        |

**적용할 정렬 논리:**
`Major` 열은 오름차순(`True`), `GPA` 열은 내림차순(`False`)으로 정렬합니다.

**정렬 과정 및 결과:**

1.  **1차 정렬 (학과 - 오름차순)**: 먼저 `Major` 열을 기준으로 가나다순으로 정렬합니다.
    *   경영학 그룹
    *   디자인학 그룹
    *   컴퓨터공학 그룹

2.  **2차 정렬 (학점 - 내림차순)**: 각 학과 그룹 내에서 `GPA` 열을 기준으로 높은 학점부터 낮은 학점 순으로 정렬합니다.

**정렬 후 데이터 (pandas `sort_values` 적용 결과)**

```python
import pandas as pd

data = {
    'Major': ['컴퓨터공학', '경영학', '컴퓨터공학', '경영학', '디자인학', '컴퓨터공학', '디자인학'],
    'Name': ['김철수', '이영희', '박민수', '최지아', '한준호', '정수진', '강은서'],
    'Year': [3, 2, 4, 3, 2, 3, 4],
    'GPA': [3.8, 4.0, 3.9, 3.5, 4.1, 3.8, 3.9]
}
df = pd.DataFrame(data)

# 'Major'는 오름차순, 'GPA'는 내림차순으로 정렬
sorted_df = df.sort_values(by=["Major", "GPA"], ascending=[True, False])

print(sorted_df.to_markdown(index=False))
```

| Major      | Name | Year | GPA |
| :--------- | :--- | :--- | :-- |
| 경영학     | 이영희 | 2    | 4.0 |
| 경영학     | 최지아 | 3    | 3.5 |
| 디자인학   | 한준호 | 2    | 4.1 |
| 디자인학   | 강은서 | 4    | 3.9 |
| 컴퓨터공학 | 박민수 | 4    | 3.9 |
| 컴퓨터공학 | 김철수 | 3    | 3.8 |
| 컴퓨터공학 | 정수진 | 3    | 3.8 |

이 예시에서 볼 수 있듯이,
*   가장 먼저 '경영학' 학생들이 나오고, 그 다음 '디자인학', 그리고 '컴퓨터공학' 학생들이 나옵니다 (학과 오름차순).
*   '경영학' 학생들 내에서는 이영희(4.0)가 최지아(3.5)보다 먼저 나옵니다 (GPA 내림차순).
*   '디자인학' 학생들 내에서도 한준호(4.1)가 강은서(3.9)보다 먼저 나옵니다 (GPA 내림차순).
*   '컴퓨터공학' 학생들 내에서는 박민수(3.9)가 가장 먼저 나오고, 김철수(3.8)와 정수진(3.8)은 같은 학점이므로 이들의 상대적인 순서는 원본 데이터에서의 순서나 파이썬의 내부 구현에 따라 달라질 수 있습니다 (여기서는 원본 순서를 유지한 것으로 보입니다).

이처럼 `sort_values()` 함수와 `by`, `ascending` 인수를 활용하면 복잡한 정렬 요구사항도 유연하고 효율적으로 처리할 수 있습니다.

---

## Slide 14

핵심 개념은 데이터프레임(관계) 간의 '집합 연산'입니다. 관계형 데이터베이스에서 두 개 이상의 릴레이션(테이블)을 특정 기준으로 결합하거나 비교할 때 사용되며, 파이썬 Pandas 라이브러리에서도 유사한 연산을 수행할 수 있습니다.

---

### 1. 합집합 (Union: R ∪ S)

*   **개념:** 두 관계 `R`과 `S`에 속하는 모든 고유한 튜플(행)을 포함하는 새로운 관계를 만듭니다. 이때, `R`과 `S`는 동일한 스키마(컬럼명과 데이터 타입)를 가져야 합니다 (Union-compatible). 결과에서는 중복되는 튜플이 제거됩니다.
*   **Pandas 구현:** `pd.concat([R, S], ignore_index=True).drop_duplicates()`를 사용하여 두 데이터프레임을 위아래로 합친 후 중복 행을 제거합니다.
*   **구체적인 실생활 예시:**
    영화 스트리밍 서비스 '스트림픽스(StreamFlix)'와 '무비나우(MovieNow)'가 각각 보유한 영화 목록이 있다고 가정해 봅시다.
    *   **R (스트림픽스 영화):** `[(영화A, 액션), (영화B, 코미디), (영화C, 드라마)]`
    *   **S (무비나우 영화):** `[(영화C, 드라마), (영화D, 스릴러), (영화E, 공포)]`

    이때, 두 플랫폼의 **합집합**은 '스트림픽스' 또는 '무비나우' 중 **어느 한 곳이라도 존재하는 모든 고유한 영화 목록**이 됩니다.
    *   **결과:** `[(영화A, 액션), (영화B, 코미디), (영화C, 드라마), (영화D, 스릴러), (영화E, 공포)]`
    (영화C, 드라마)는 양쪽에 모두 있었지만, 합집합 결과에서는 한 번만 나타납니다.

---

### 2. 교집합 (Intersection: R ∩ S)

*   **개념:** 두 관계 `R`과 `S`에 모두 속하는 고유한 튜플만을 포함하는 새로운 관계를 만듭니다. 즉, 두 관계에 공통적으로 존재하는 튜플들을 찾습니다.
*   **Pandas 구현:** `R.merge(S, how='inner')`를 사용하여 두 데이터프레임에서 공통된 키(여기서는 모든 컬럼)를 기준으로 내부 조인(inner merge)을 수행합니다.
*   **구체적인 실생활 예시:**
    위 '스트림픽스(R)'와 '무비나우(S)' 영화 목록을 다시 사용합니다.
    *   **R (스트림픽스 영화):** `[(영화A, 액션), (영화B, 코미디), (영화C, 드라마)]`
    *   **S (무비나우 영화):** `[(영화C, 드라마), (영화D, 스릴러), (영화E, 공포)]`

    이때, 두 플랫폼의 **교집합**은 '스트림픽스'와 '무비나우' **모두에서 시청 가능한 영화 목록**이 됩니다.
    *   **결과:** `[(영화C, 드라마)]`
    영화C(드라마)만이 두 플랫폼에 공통적으로 존재합니다.

---

### 3. 차집합 (Difference: R - S)

*   **개념:** 관계 `R`에는 속하지만, 관계 `S`에는 속하지 않는 고유한 튜플만을 포함하는 새로운 관계를 만듭니다.
*   **Pandas 구현:** `R.merge(S, how='left', indicator=True).query("_merge == 'left_only'").drop(columns=["_merge"])`를 사용합니다. `how='left'`로 `R`의 모든 행을 유지하면서 `S`와 조인하고, `indicator=True`로 조인 결과를 나타내는 `_merge` 컬럼을 생성합니다. 이후 `_merge == 'left_only'`로 `R`에만 존재하는 행을 필터링하고, `_merge` 컬럼을 제거합니다.
*   **구체적인 실생활 예시:**
    다시 '스트림픽스(R)'와 '무비나우(S)' 영화 목록을 사용합니다.
    *   **R (스트림픽스 영화):** `[(영화A, 액션), (영화B, 코미디), (영화C, 드라마)]`
    *   **S (무비나우 영화):** `[(영화C, 드라마), (영화D, 스릴러), (영화E, 공포)]`

    이때, 두 플랫폼의 **차집합 (R - S)**은 '스트림픽스'에는 있지만 **'무비나우'에는 없는 영화 목록**이 됩니다.
    *   **결과:** `[(영화A, 액션), (영화B, 코미디)]`
    이 영화들은 스트림픽스에서만 독점적으로 제공되며, 무비나우에서는 볼 수 없습니다.

---

## Slide 15

## 데이터베이스 조인 개념 (Product, Theta, Equi, Natural Join)

본 슬라이드에서는 데이터베이스에서 두 개 이상의 릴레이션(테이블)을 결합하는 다양한 조인(Join) 연산의 핵심 개념을 설명하고, 파이썬 Pandas 라이브러리를 사용한 실제 구현 예시를 제시합니다.

---

### 1. Product (카르테시안 곱, Cartesian Product) `R × S`

*   **핵심 개념:** 두 릴레이션 `R`과 `S`의 모든 튜플(행) 조합을 생성합니다. `R`의 각 튜플은 `S`의 모든 튜플과 연결됩니다. 결과 릴레이션의 스키마는 `R`의 모든 속성과 `S`의 모든 속성을 포함하며, 튜플의 수는 `R`의 튜플 수와 `S`의 튜플 수를 곱한 값과 같습니다.
*   **Pandas 구현:** `pd.merge(R, S, how="cross")`
*   **실생활 예시:**
    당신이 의류 쇼핑몰을 운영한다고 가정해 봅시다.
    *   **릴레이션 R (상의):** `[티셔츠(S), 티셔츠(M), 셔츠(L)]`
    *   **릴레이션 S (하의):** `[청바지(28), 청바지(30), 면바지(32)]`
    카르테시안 곱은 가능한 모든 상하의 조합을 만들어냅니다. 예를 들어:
    *   `[티셔츠(S), 청바지(28)]`
    *   `[티셔츠(S), 청바지(30)]`
    *   ...
    *   `[셔츠(L), 면바지(32)]`
    이 결과는 "모든 가능한 옷차림 조합"을 얻을 때 유용할 수 있습니다. 예를 들어, 재고 시스템에서 특정 색상의 상의와 하의를 조합했을 때 어떤 옷차림이 가능한지 모두 파악한 후, 그 위에 특정 조건을 적용하여 팔릴 만한 조합을 찾아낼 때 활용될 수 있습니다.

---

### 2. Theta Join (조건부 조인) `R ⋈_θ S`

*   **핵심 개념:** 카르테시안 곱 `R × S`의 결과에 특정 조건(predicate) `θ`를 적용하여 필터링하는 연산입니다. 여기서 `θ`는 등호(=)뿐만 아니라 부등호(<, >, <=, >=, !=) 등 모든 비교 연산자를 포함할 수 있습니다.
*   **실생활 예시:**
    당신이 고객 관리 시스템을 개발한다고 가정해 봅시다.
    *   **릴레이션 R (고객 정보):** `[고객ID, 이름, 나이, 등급]`
    *   **릴레이션 S (주문 정보):** `[주문ID, 고객ID, 주문금액, 주문일자]`
    `R ⋈_{R.나이 >= 18 AND S.주문금액 < 50000} S`와 같은 Theta Join을 사용하면, "18세 이상이면서 주문금액이 5만원 미만인 고객의 주문 정보"를 추출할 수 있습니다. 이는 단순히 같은 고객ID를 가진 정보를 연결하는 것을 넘어, 비즈니스 규칙에 따른 복잡한 조건을 충족하는 데이터를 찾아낼 때 유용합니다.

---

### 3. Equi-Join (동등 조인) `R ⋈_{A=B} S`

*   **핵심 개념:** Theta Join의 특수한 형태로, 조인 조건 `θ`가 오직 등호(`=`)만을 사용하여 두 릴레이션의 속성 값을 비교할 때 사용됩니다. 일반적으로 두 릴레이션이 공통으로 가지고 있는 키(key) 속성을 기준으로 연결합니다.
*   **Pandas 구현:** `pd.merge(babynames, yr_total, on="Year", how="inner")`
    *   슬라이드 예시에서 `babynames` 데이터프레임과 `yr_total` 데이터프레임을 `Year` 컬럼을 기준으로 `inner` 조인하여, 각 이름 데이터에 해당 연도의 총 아기 수를 연결하는 작업을 보여줍니다. 이는 `Year` 컬럼의 값이 같은 행들을 결합합니다.
*   **실생활 예시:**
    대학교에서 수강 신청 데이터를 관리한다고 가정해 봅시다.
    *   **릴레이션 R (학생):** `[학생ID, 이름, 전공ID]`
    *   **릴레이션 S (전공):** `[전공ID, 전공명, 학과장]`
    `R ⋈_{R.전공ID = S.전공ID} S`와 같은 Equi-Join을 사용하면, `학생` 릴레이션의 `전공ID`와 `전공` 릴레이션의 `전공ID`가 일치하는 행들만을 연결하여 "각 학생의 이름과 그 학생이 속한 전공의 상세 정보(전공명, 학과장 등)"를 함께 볼 수 있습니다. 가장 흔하게 사용되는 조인 방식입니다.

---

### 4. Natural Join (자연 조인)

*   **핵심 개념:** Equi-Join의 또 다른 특수한 형태로, 두 릴레이션이 **동일한 이름을 가진 모든 공통 속성(컬럼)**을 찾아 자동으로 조인 조건을 설정하고, 조인 결과에서 중복되는 공통 속성 컬럼을 제거하여 하나만 남깁니다.
*   **실생활 예시:**
    다시 대학교 수강 신청 예시를 사용해 봅시다.
    *   **릴레이션 R (학생_과목):** `[학생ID, 과목코드, 성적]`
    *   **릴레이션 S (과목_정보):** `[과목코드, 과목명, 학점]`
    두 릴레이션에 `과목코드`라는 동일한 이름의 공통 속성이 있습니다. Natural Join을 사용하면, 시스템이 자동으로 `과목코드`를 조인 키로 인식하고, `R.과목코드 = S.과목코드` 조건으로 Equi-Join을 수행한 뒤, 결과에서 `과목코드` 컬럼을 하나만 남깁니다. 이를 통해 "어떤 학생이 어떤 과목을 수강했고 그 과목의 이름과 학점은 무엇인지"를 간결하게 볼 수 있습니다.

---

---

## Slide 16

## 데이터프레임 병합(Relational Join via merge)의 핵심 개념

슬라이드에서 제시된 `df.merge()` 함수는 두 개의 데이터프레임을 특정 열(키)을 기준으로 결합하는 강력한 기능입니다. 데이터베이스의 조인(JOIN) 연산과 유사하며, Pandas에서는 `merge` 함수를 통해 다양한 방식으로 데이터를 합칠 수 있습니다.

### 1. 기본 사용법 및 매개변수

*   **`df.merge(df1, on='name')`**: `df` 데이터프레임에 `df1` 데이터프레임을 'name'이라는 공통 열을 기준으로 병합합니다.
*   **`on='column_name'`**: 두 데이터프레임에서 공통으로 존재하는 열을 지정하여 이 열의 값을 기준으로 행을 매칭합니다.
*   **`how='inner'` (기본값)**: 데이터를 병합하는 방식을 지정합니다. `inner`가 기본값입니다.

### 2. 병합 유형 (`how` 파라미터)

`how` 파라미터는 총 네 가지 주요 병합 방식을 제공하며, 각 방식에 따라 결과 데이터프레임에 포함되는 행의 범위가 달라집니다.

#### 가. Inner Join (`how='inner'`)
*   **설명**: 양쪽 데이터프레임에 모두 존재하는 `on` 키(열)의 값에 해당하는 행들만 결합합니다. 어느 한쪽에라도 키가 존재하지 않으면 해당 행은 결과에서 제외됩니다.
*   **슬라이드 예시**:
    *   `df` (Oslo, Vienna) 와 `df1` (Vienna, Tokyo) 에서 'name' 열을 기준으로 병합합니다.
    *   'Vienna'만 양쪽 데이터프레임에 모두 존재하므로, 최종 결과에는 'Vienna' 행만 포함됩니다.
    *   `df.merge(df1, on='name', how='inner')`
    ```
       name  population   area
    0  Vienna     1911191  414.8
    ```
*   **실생활 예시**:
    *   **상황**: 한 회사에 `직원_정보` 테이블(직원ID, 이름, 부서)과 `급여_정보` 테이블(직원ID, 급여, 입사일)이 있다고 가정해 봅시다.
    *   **Inner Join 적용**: "현재 직원 중 급여 정보가 모두 등록된 직원"의 정보만 보고 싶을 때 사용합니다. `직원_정보`와 `급여_정보`에 모두 직원ID가 존재하는 경우만 결합하여, 직원ID, 이름, 부서, 급여, 입사일이 모두 포함된 결과를 얻습니다. 급여 정보가 아직 없는 신입 직원이나, 퇴사했지만 급여 정보가 남아있는 직원은 제외됩니다.

#### 나. Left Outer Join (`how='left'`)
*   **설명**: `df.merge()`의 첫 번째 인자(왼쪽)로 지정된 데이터프레임의 모든 행을 포함하고, 두 번째 인자(오른쪽)의 데이터프레임에서 일치하는 키가 있는 경우에만 정보를 결합합니다. 왼쪽 데이터프레임에만 존재하는 키에 대해서는 오른쪽 데이터프레임에서 온 열에 `NaN`(Not a Number, 결측값)이 채워집니다.
*   **슬라이드 예시**:
    *   `df` (왼쪽)의 모든 도시('Oslo', 'Vienna')를 포함합니다.
    *   'Oslo'는 `df1`에 없으므로, `area` 열에 `NaN`이 채워집니다.
    *   'Vienna'는 `df1`에 있으므로, `area` 정보가 올바르게 결합됩니다.
    *   `df.merge(df1, on='name', how='left')`
    ```
       name  population   area
    0  Oslo   698660.0    NaN
    1  Vienna  1911191.0  414.8
    ```
*   **실생활 예시**:
    *   **상황**: "모든 직원의 정보"를 보되, "급여 정보가 있다면 함께 보여주고 싶을 때" 사용합니다.
    *   **Left Join 적용**: `직원_정보` 테이블의 모든 행을 가져오고, `급여_정보` 테이블에서 해당 직원ID가 있는 경우 급여와 입사일을 추가합니다. 만약 아직 급여 정보가 등록되지 않은 신입 직원이 있다면, 해당 직원의 급여와 입사일 열에는 `NaN`이 표시됩니다.

#### 다. Right Outer Join (`how='right'`)
*   **설명**: `df.merge()`의 두 번째 인자(오른쪽)로 지정된 데이터프레임의 모든 행을 포함하고, 첫 번째 인자(왼쪽)의 데이터프레임에서 일치하는 키가 있는 경우에만 정보를 결합합니다. 오른쪽 데이터프레임에만 존재하는 키에 대해서는 왼쪽 데이터프레임에서 온 열에 `NaN`이 채워집니다.
*   **슬라이드 예시**:
    *   `df1` (오른쪽)의 모든 도시('Vienna', 'Tokyo')를 포함합니다.
    *   'Tokyo'는 `df`에 없으므로, `population` 열에 `NaN`이 채워집니다.
    *   'Vienna'는 `df`에 있으므로, `population` 정보가 올바르게 결합됩니다.
    *   `df.merge(df1, on='name', how='right')`
    ```
       name  population   area
    0  Vienna  1911191.0  414.8
    1  Tokyo       NaN  2194.1
    ```
*   **실생활 예시**:
    *   **상황**: "등록된 모든 급여 정보"를 보되, "어떤 직원에게 해당하는 급여인지도 함께 보고 싶을 때" 사용합니다.
    *   **Right Join 적용**: `급여_정보` 테이블의 모든 행을 가져오고, `직원_정보` 테이블에서 해당 직원ID가 있는 경우 이름과 부서를 추가합니다. 만약 어떤 이유로 `직원_정보` 테이블에는 없지만 `급여_정보` 테이블에만 남아있는 직원ID가 있다면, 해당 급여 정보에는 이름과 부서 열에 `NaN`이 표시됩니다.

#### 라. Full Outer Join (`how='outer'`)
*   **설명**: 양쪽 데이터프레임의 모든 행을 포함합니다. 한쪽에만 존재하는 키에 대해서는 다른 쪽 데이터프레임에서 온 열에 `NaN`이 채워집니다. 즉, 왼쪽 데이터프레임에만 있는 행, 오른쪽 데이터프레임에만 있는 행, 그리고 양쪽에 모두 있는 행을 모두 포함합니다.
*   **슬라이드 예시**:
    *   'Oslo', 'Vienna', 'Tokyo' 등 양쪽 데이터프레임에 있는 **모든 도시**를 포함합니다.
    *   'Oslo'는 `df1`에 없으므로 `area`가 `NaN`이고, 'Tokyo'는 `df`에 없으므로 `population`이 `NaN`이 됩니다.
    *   `df.merge(df1, on='name', how='outer')`
    ```
       name  population   area
    0  Oslo   698660.0    NaN
    1  Vienna  1911191.0  414.8
    2  Tokyo       NaN  2194.1
    ```
*   **실생활 예시**:
    *   **상황**: "현재 회사에 대한 모든 정보"(직원 정보, 급여 정보)를 통합하여 보고 싶을 때 사용합니다. 누락된 정보는 `NaN`으로 표시됩니다.
    *   **Full Outer Join 적용**: `직원_정보`와 `급여_정보` 테이블에 존재하는 모든 직원ID에 대한 행을 가져옵니다. 급여 정보가 없는 신입 직원은 급여/입사일 열에 `NaN`이 표시되고, `직원_정보`에 없지만 급여 정보만 남아있는 직원ID가 있다면 이름/부서 열에 `NaN`이 표시됩니다.

### 3. NaN (Not a Number)
`NaN`은 데이터프레임에서 결측값(missing value)을 나타내는 데 사용됩니다. `merge` 연산에서 일치하는 데이터가 없을 경우 자동으로 해당 셀에 `NaN`이 채워집니다.

### 4. 중복 키 처리 (Duplicate keys)
만약 `on`으로 지정된 키 열에 중복된 값이 있다면, `df.merge()`는 'many-to-many' (다대다) 매칭을 수행합니다. 이는 해당 그룹 내에서 가능한 모든 조합으로 행을 생성하는 카테시안 곱(Cartesian product)과 유사하게 작동할 수 있습니다.
*   **예시**: 만약 `직원_정보` 테이블에 한 직원이 실수로 두 번 등록되어 있고, `급여_정보` 테이블에도 해당 직원의 급여가 한 번 등록되어 있다면, 이 직원에 대한 정보는 결과 데이터프레임에 두 번 나타날 수 있습니다. 더 복잡하게, 한 직원이 여러 프로젝트에 배정되어 `프로젝트_정보` 테이블에 여러 행이 있고, `급여_정보` 테이블에도 여러 급여 내역이 있다면, 해당 직원의 모든 프로젝트-급여 조합이 결과로 나올 수 있습니다. 이러한 상황에서는 중복 키가 의도된 것인지, 아니면 데이터 정리가 필요한지 확인해야 합니다.

---

## Slide 17

## DataFrame.join: 인덱스 기반 결합

`DataFrame.join()`은 두 개의 Pandas DataFrame을 결합하는 강력한 메서드입니다. 특히 **인덱스(index)**를 기준으로 데이터를 정렬하고 합치는 데 특화되어 있습니다. `pd.concat`이 단순히 데이터를 옆으로 이어 붙이는 것과 달리, `join`은 키(key) 로직을 사용하여 공통된 인덱스 또는 컬럼 값을 기준으로 행을 매칭합니다.

### 핵심 개념

1.  **인덱스 기반 결합**: `DataFrame.join()`의 가장 기본적이고 핵심적인 기능은 두 DataFrame의 **인덱스 값**을 비교하여 일치하는 행들을 결합하는 것입니다. 즉, 각 DataFrame의 인덱스가 조인의 '키' 역할을 합니다.
    *   만약 인덱스가 아닌 특정 컬럼을 기준으로 결합하고 싶다면, `on` 파라미터에 해당 컬럼 이름을 지정할 수 있습니다. (예: `df.join(df1, on='공통컬럼')`) 하지만 기본 동작은 인덱스를 사용합니다.

2.  **결합 유형 (how 파라미터)**: `how` 파라미터를 사용하여 두 DataFrame을 어떻게 결합할지 지정할 수 있습니다. 각 유형은 매칭되는 인덱스 유무에 따라 최종 결과 DataFrame에 포함되는 행의 범위를 결정합니다.

    *   **`'inner'`**: 두 DataFrame에 모두 존재하는 인덱스에 해당하는 행만 결합합니다. 즉, 양쪽 모두에서 매칭되는 데이터만 보존됩니다.
    *   **`'left'` (기본값)**: `join`을 호출하는 왼쪽 DataFrame(`df`)의 모든 인덱스를 기준으로 합니다. `df1`에 매칭되는 인덱스가 없는 경우, `df1`에서 온 컬럼들은 `NaN` (Not a Number)으로 채워집니다.
    *   **`'right'`**: `join` 메서드에 인수로 전달되는 오른쪽 DataFrame(`df1`)의 모든 인덱스를 기준으로 합니다. `df`에 매칭되는 인덱스가 없는 경우, `df`에서 온 컬럼들은 `NaN`으로 채워집니다.
    *   **`'outer'`**: 두 DataFrame 중 어느 한쪽에라도 존재하는 모든 인덱스를 결합합니다. 매칭되지 않는 인덱스의 경우, 해당 DataFrame에서 온 컬럼들은 `NaN`으로 채워집니다.

3.  **`pd.concat`과의 차이점**: `pd.concat([df, df1], axis=1)`는 단순히 두 DataFrame을 컬럼 기준으로 옆으로 이어 붙이는 것으로, 인덱스 매칭을 통한 데이터 정렬 로직이 없습니다. 반면 `df.join(df1)`은 인덱스(또는 `on`으로 지정된 컬럼)를 기준으로 행을 정렬하고 매칭하여 데이터를 결합합니다.

---

### 실생활 예시: 회사 직원 정보와 프로젝트 역할 데이터

한 소프트웨어 개발 회사의 인사팀에서 직원들의 기본 정보와 현재 참여하고 있는 프로젝트 역할을 관리하는 두 개의 데이터프레임이 있다고 가정해 봅시다.

1.  **`df_employee_details` (직원 상세 정보)**
    *   인덱스: `EmployeeID`
    *   컬럼: `Name`, `Department`

2.  **`df_project_roles` (프로젝트 역할)**
    *   인덱스: `EmployeeID`
    *   컬럼: `ProjectName`, `Role`

이제 이 두 DataFrame을 `join` 메서드를 사용하여 다양한 방식으로 결합해 보겠습니다.

```python
import pandas as pd

# 1. 직원 상세 정보 DataFrame 생성
data_details = {
    'Name': ['Alice', 'Bob', 'Carol', 'David'],
    'Department': ['HR', 'Engineering', 'Marketing', 'Engineering']
}
df_employee_details = pd.DataFrame(data_details, index=['E001', 'E002', 'E003', 'E005'])
print("--- df_employee_details ---")
print(df_employee_details)
#              Name   Department
# EmployeeID
# E001        Alice           HR
# E002          Bob  Engineering
# E003        Carol    Marketing
# E005        David  Engineering

print("\n")

# 2. 프로젝트 역할 DataFrame 생성
data_roles = {
    'ProjectName': ['Project Alpha', 'Project Beta', 'Project Gamma'],
    'Role': ['Lead Dev', 'Tester', 'PM']
}
df_project_roles = pd.DataFrame(data_roles, index=['E002', 'E003', 'E004'])
print("--- df_project_roles ---")
print(df_project_roles)
#              ProjectName      Role
# EmployeeID
# E002       Project Alpha  Lead Dev
# E003        Project Beta    Tester
# E004       Project Gamma        PM
```

두 DataFrame의 인덱스를 비교해 보면:
*   `df_employee_details` 인덱스: `E001`, `E002`, `E003`, `E005`
*   `df_project_roles` 인덱스: `E002`, `E003`, `E004`
*   공통 인덱스: `E002`, `E003`

---

#### 1. `how='inner'` (내부 결합)

**설명**: 양쪽 DataFrame에 모두 존재하는 `EmployeeID` (E002, E003)만 남기고, 해당 직원들의 모든 정보를 결합합니다. 즉, 현재 프로젝트에 참여하고 있는 직원들 중, 회사에도 등록된 직원 정보만 보여줍니다.

```python
inner_join_df = df_employee_details.join(df_project_roles, how='inner')
print("--- Inner Join (df_employee_details와 df_project_roles의 공통 직원) ---")
print(inner_join_df)
#              Name   Department    ProjectName      Role
# EmployeeID
# E002          Bob  Engineering  Project Alpha  Lead Dev
# E003        Carol    Marketing   Project Beta    Tester
```
**결과 해석**: `E001`, `E005`는 프로젝트에 배정되지 않았고, `E004`는 직원 상세 정보에 없으므로 결과에서 제외됩니다.

---

#### 2. `how='left'` (왼쪽 결합)

**설명**: 왼쪽 DataFrame(`df_employee_details`)의 모든 `EmployeeID`를 기준으로 결합합니다. `df_project_roles`에 해당 `EmployeeID`가 없으면, 프로젝트 관련 컬럼에는 `NaN`이 채워집니다. 즉, 모든 직원의 상세 정보를 보여주되, 프로젝트에 참여하고 있다면 프로젝트 정보도 함께 보여줍니다.

```python
left_join_df = df_employee_details.join(df_project_roles, how='left') # how='left'는 기본값이므로 생략 가능
print("--- Left Join (모든 직원의 상세 정보 + 매칭되는 프로젝트 정보) ---")
print(left_join_df)
#              Name   Department    ProjectName      Role
# EmployeeID
# E001        Alice           HR            NaN       NaN
# E002          Bob  Engineering  Project Alpha  Lead Dev
# E003        Carol    Marketing   Project Beta    Tester
# E005        David  Engineering            NaN       NaN
```
**결과 해석**: `E001`과 `E005`는 `df_project_roles`에 없기 때문에 `ProjectName`과 `Role` 컬럼에 `NaN`이 표시됩니다.

---

#### 3. `how='right'` (오른쪽 결합)

**설명**: 오른쪽 DataFrame(`df_project_roles`)의 모든 `EmployeeID`를 기준으로 결합합니다. `df_employee_details`에 해당 `EmployeeID`가 없으면, 직원 상세 정보 컬럼에는 `NaN`이 채워집니다. 즉, 모든 프로젝트 참여 직원들의 역할을 보여주되, 해당 직원의 상세 정보가 있다면 함께 보여줍니다.

```python
right_join_df = df_employee_details.join(df_project_roles, how='right')
print("--- Right Join (모든 프로젝트 참여 직원의 역할 + 매칭되는 상세 정보) ---")
print(right_join_df)
#              Name   Department    ProjectName      Role
# EmployeeID
# E002          Bob  Engineering  Project Alpha  Lead Dev
# E003        Carol    Marketing   Project Beta    Tester
# E004          NaN         NaN  Project Gamma        PM
```
**결과 해석**: `E004`는 `df_project_roles`에는 있지만 `df_employee_details`에는 없기 때문에 `Name`과 `Department` 컬럼에 `NaN`이 표시됩니다. 이는 아직 회사에 정식 등록되지 않았지만 프로젝트에 참여하고 있는 인원일 수 있습니다.

---

#### 4. `how='outer'` (완전 외부 결합)

**설명**: 두 DataFrame에 존재하는 모든 `EmployeeID`를 포함하여 결합합니다. 어느 한쪽에만 있는 `EmployeeID`의 경우, 다른 DataFrame에서 온 컬럼들은 `NaN`으로 채워집니다. 즉, 회사에 등록된 모든 직원과 프로젝트에 참여하는 모든 직원의 정보를 빠짐없이 보여줍니다.

```python
outer_join_df = df_employee_details.join(df_project_roles, how='outer')
print("--- Outer Join (두 DataFrame의 모든 직원의 정보) ---")
print(outer_join_df)
#              Name   Department    ProjectName      Role
# EmployeeID
# E001        Alice           HR            NaN       NaN
# E002          Bob  Engineering  Project Alpha  Lead Dev
# E003        Carol    Marketing   Project Beta    Tester
# E004          NaN         NaN  Project Gamma        PM
# E005        David  Engineering            NaN       NaN
```
**결과 해석**: `E001`과 `E005`는 프로젝트 정보가 없고, `E004`는 직원 상세 정보가 없으므로 해당 컬럼에 `NaN`이 표시됩니다. `E002`와 `E003`은 양쪽에 모두 정보가 있으므로 완벽하게 결합됩니다.

이 예시를 통해 `DataFrame.join`이 인덱스를 어떻게 활용하며, `how` 파라미터가 결과 DataFrame에 어떤 영향을 미치는지 명확하게 이해하셨기를 바랍니다.

---

## Slide 18

이 슬라이드의 핵심 개념은 다음과 같습니다:

### 1. 다른 키 이름을 가진 데이터프레임 병합 (Merging DataFrames with Different Key Names)

*   **설명:** Pandas의 `merge` 함수를 사용하여 두 개의 데이터프레임을 결합할 때, 각 데이터프레임에서 연결 기준으로 사용될 컬럼의 이름이 다를 수 있습니다. `left_on` 인자는 왼쪽(처음 호출하는) 데이터프레임의 키 컬럼을 지정하고, `right_on` 인자는 오른쪽(병합될) 데이터프레임의 키 컬럼을 지정하여, 이름이 다른 두 컬럼을 기준으로 데이터를 연결할 수 있습니다.
*   **실생활 예시:**
    당신이 온라인 쇼핑몰의 데이터베이스 관리자라고 가정해 봅시다.
    1.  **`주문_목록` 데이터프레임:** 각 주문에 대한 정보(`order_id`, `고객_id`, `상품_코드`, `배송지_우편번호`)를 가지고 있습니다.
    2.  **`우편번호_정보` 데이터프레임:** 우편번호에 따른 상세 지역 정보(`postal_code`, `도시`, `시군구`, `도_이름`)를 가지고 있습니다.
    
    여기서 `주문_목록`의 `배송지_우편번호` 컬럼과 `우편번호_정보`의 `postal_code` 컬럼은 같은 의미를 가지지만 이름이 다릅니다. 각 주문의 배송지 상세 정보를 얻기 위해 두 데이터프레임을 병합해야 할 때, 다음과 같이 `left_on`과 `right_on`을 사용합니다.
    
    ```python
    merged_df = 주문_목록.merge(우편번호_정보, left_on='배송지_우편번호', right_on='postal_code')
    ```
    이 코드를 통해 `주문_목록`의 각 주문에 해당하는 `도시`, `시군구`, `도_이름` 정보가 성공적으로 추가됩니다.

### 2. 병합 후 중복 컬럼 이름 처리 (Handling Duplicate Column Names After Merge)

*   **설명:** 두 데이터프레임을 병합했을 때, 키 컬럼이 아닌 다른 컬럼들 중에서 이름이 같은 컬럼이 존재할 수 있습니다. 예를 들어, `item_id`와 `price`를 가진 `products` 테이블과 `order_id`와 `price`를 가진 `orders` 테이블을 병합하는 경우, 두 테이블 모두 `price`라는 컬럼을 가지고 있습니다. Pandas는 기본적으로 이러한 이름 충돌을 해결하기 위해 중복된 컬럼 이름 뒤에 `_x` (왼쪽 데이터프레임에서 옴)와 `_y` (오른쪽 데이터프레임에서 옴) 같은 접미사를 자동으로 추가합니다. 더 명확한 구분을 위해 `suffixes` 인자를 사용하여 사용자 정의 접미사를 지정할 수 있습니다.
*   **실생활 예시:**
    당신이 학교의 학사 시스템을 관리한다고 상상해 봅시다.
    1.  **`학생_정보` 데이터프레임:** 학생 개인 정보(`학생_ID`, `이름`, `주소`, `등록_날짜`, `상태`)를 포함합니다. 여기서 `상태`는 학생의 재학 상태(예: '재학', '휴학')를 나타냅니다.
    2.  **`장학금_정보` 데이터프레임:** 학생별 장학금 내역(`학생_ID`, `장학금_종류`, `금액`, `상태`)을 포함합니다. 여기서 `상태`는 장학금 지급 상태(예: '지급_완료', '심사_중')를 나타냅니다.
    
    두 데이터프레임은 `학생_ID`를 기준으로 연결되지만, 둘 다 `상태`라는 컬럼을 가지고 있습니다. 이 두 `상태` 컬럼은 서로 다른 의미를 가집니다.
    
    ```python
    merged_student_data = 학생_정보.merge(장학금_정보, on='학생_ID')
    # 기본 merge 결과: 상태_x (학생 재학 상태), 상태_y (장학금 지급 상태)
    
    # 더 명확하게 접미사 지정
    merged_student_data_custom = 학생_정보.merge(장학금_정보, on='학생_ID', suffixes=('_재학', '_장학금'))
    # 결과: 상태_재학 (학생 재학 상태), 상태_장학금 (장학금 지급 상태)
    ```
    이처럼 `suffixes`를 사용하면 병합된 데이터프레임에서 어떤 `상태` 컬럼이 학생의 재학 상태를 의미하고, 어떤 `상태` 컬럼이 장학금 지급 상태를 의미하는지 쉽게 구분할 수 있어 데이터 분석의 혼란을 줄일 수 있습니다. 슬라이드의 `df.filter(['city', 'state'])` 부분은 병합 후 필요한 컬럼만 선택하여 최종 데이터프레임을 정리하는 일반적인 후처리 과정으로 이해할 수 있습니다.

---

## Slide 19

### 핵심 개념 설명

슬라이드에서 다루는 주요 개념은 데이터프레임(또는 관계형 데이터베이스 테이블) 간의 관계를 설정하고 데이터를 필터링하는 세 가지 고급 조인(Join) 방식입니다: **아우터 조인(Outer Join)**, **세미조인(Semijoin)**, 그리고 **안티조인(Antijoin)**.

---

### 1. 아우터 조인 (Outer Join)

*   **개념:** 두 데이터프레임을 특정 키(key)를 기준으로 결합하되, 어느 한쪽 데이터프레임에만 존재하는 행(row)도 결과에 포함시키는 조인 방식입니다. 매칭되는 데이터가 없는 경우, 해당 컬럼에는 `NaN` (Not a Number, 또는 SQL의 NULL) 값이 채워집니다. `how="outer"` 옵션을 사용합니다.

*   **구체적이고 실생활에 가까운 예시:**
    *   **상황:** 당신은 온라인 쇼핑몰의 데이터 분석가입니다. 두 개의 데이터프레임을 가지고 있습니다.
        1.  `상품_목록 (products)`: `상품ID`, `상품명`, `재고량`
        2.  `판매_기록 (sales)`: `판매ID`, `상품ID`, `판매수량`, `판매일자`
    *   **목표:** 모든 상품의 정보를 보되, 만약 특정 상품이 한 번도 판매된 적이 없다면 판매 기록 부분은 `NaN`으로 비워두고, 반대로 판매 기록이 있는데 해당 `상품ID`가 `상품_목록`에 없다면 (데이터 오류 가능성) 상품 정보 부분을 `NaN`으로 채운 채로 모든 데이터를 한눈에 보고 싶을 때 사용합니다. 즉, 어느 한쪽에만 있는 데이터도 버리지 않고 모두 확인하려는 경우에 유용합니다.
    *   **Pandas 코드 (슬라이드 예시와 유사):**
        ```python
        import pandas as pd

        # 슬라이드 예시: babynames 데이터와 연도별 총 출생아 수 데이터를 가정
        babynames = pd.DataFrame({
            'Name': ['Mary', 'John', 'Alice', 'Bob'],
            'Year': [2000, 2000, 2001, 2002],
            'Count': [5000, 4000, 3000, 2000]
        })

        yr_total = pd.DataFrame({
            'Year': [2000, 2001, 2003], # 2002년 데이터는 yr_total에 없음, 2003년 데이터는 babynames에 없음
            'TotalBirths': [4000000, 3900000, 3800000]
        })

        # 'Year'를 기준으로 아우터 조인 수행
        outer_join_result = pd.merge(babynames, yr_total, on="Year", how="outer")
        print("--- Outer Join Result ---")
        print(outer_join_result)
        ```
        *   **결과 설명:** `babynames`에 있는 2002년 데이터('Bob')는 `yr_total`에 해당 연도가 없으므로 `TotalBirths` 컬럼이 `NaN`으로 채워집니다. 반대로 `yr_total`에 있는 2003년 데이터는 `babynames`에 해당 연도가 없으므로 `Name`, `Count` 컬럼이 `NaN`으로 채워져 모든 정보를 유지합니다.

---

### 2. 세미조인 (Semijoin, $R \bowtie_{\text{Name}} S$)

*   **개념:** 왼쪽 데이터프레임(R)의 행 중에서 오른쪽 데이터프레임(S)에 **매칭되는 키가 하나라도 존재하는** 행들만을 반환합니다. 결과는 오직 왼쪽 데이터프레임(R)의 컬럼들로만 구성되며, 오른쪽 데이터프레임(S)의 컬럼은 포함되지 않습니다. 특정 조건(오른쪽 테이블에 존재 여부)에 따라 왼쪽 테이블을 필터링할 때 사용합니다. Pandas에서는 주로 `isin()` 함수를 활용하여 구현합니다.

*   **구체적이고 실생활에 가까운 예시:**
    *   **상황:** 당신은 한 대학의 학생 관리팀입니다. 두 개의 데이터프레임을 가지고 있습니다.
        1.  `전체_학생 (all_students)`: `학번`, `이름`, `학과` (전체 학생 정보)
        2.  `수강신청_완료_학번 (enrolled_student_ids)`: `학번` (이번 학기 수강신청을 완료한 학생들의 학번 목록)
    *   **목표:** 이번 학기에 수강신청을 완료한 학생들만 `전체_학생` 데이터프레임에서 모든 정보를 그대로 가져와 보고 싶을 때 사용합니다. `수강신청_완료_학번` 데이터프레임 자체의 다른 정보(예: 신청 과목 수 등)는 필요 없고, 단지 '이 학번이 수강신청을 했는가?'라는 사실 여부만으로 `전체_학생` 정보를 필터링하고 싶을 때 유용합니다.
    *   **Pandas 코드 (슬라이드 예시):**
        ```python
        import pandas as pd

        # 슬라이드 예시: babynames 데이터와 특정 이름 목록을 가정
        babynames = pd.DataFrame({
            'Name': ['Mary', 'John', 'Alice', 'Bob', 'Mary'],
            'Year': [2000, 2000, 2001, 2002, 2003],
            'Count': [5000, 4000, 3000, 2000, 5100]
        })

        # 찾고자 하는 이름들의 목록 (S 역할)
        keys = pd.DataFrame({'Name': ['Mary', 'Alice']})

        # babynames의 'Name' 컬럼이 keys 데이터프레임의 'Name' 컬럼에 존재하는지 확인하여 필터링
        semi_join_result = babynames[babynames["Name"].isin(keys["Name"])]
        print("\n--- Semijoin Result ---")
        print(semi_join_result)
        ```
        *   **결과 설명:** `babynames`에서 'Name' 컬럼 값이 `keys` 데이터프레임의 'Name' 컬럼에 존재하는 모든 행(즉, 'Mary'와 'Alice'의 기록)이 반환됩니다. 'John'이나 'Bob'의 기록은 `keys`에 없으므로 제외됩니다.

---

### 3. 안티조인 (Antijoin, $R \setminus (R \bowtie_{\text{Name}} S)$)

*   **개념:** 왼쪽 데이터프레임(R)의 행 중에서 오른쪽 데이터프레임(S)에 **매칭되는 키가 단 하나도 존재하지 않는** 행들만을 반환합니다. 세미조인과 정확히 반대되는 개념입니다. 결과는 오직 왼쪽 데이터프레임(R)의 컬럼들로만 구성됩니다. 특정 조건(오른쪽 테이블에 존재하지 않음)에 따라 왼쪽 테이블을 필터링할 때 사용합니다. Pandas에서는 `merge`의 `indicator=True` 옵션과 `query`를 조합하거나 `~isin()` 함수를 활용하여 구현할 수 있습니다.

*   **구체적이고 실생활에 가까운 예시:**
    *   **상황:** 위 세미조인 예시와 동일합니다. 당신은 대학의 학생 관리팀입니다.
        1.  `전체_학생 (all_students)`: `학번`, `이름`, `학과`
        2.  `수강신청_완료_학번 (enrolled_student_ids)`: `학번`
    *   **목표:** 이번 학기에 **수강신청을 하지 않은** (즉, `수강신청_완료_학번` 데이터프레임에 학번이 없는) 학생들만 `전체_학생` 데이터프레임에서 모든 정보를 가져와 보고 싶을 때 사용합니다. '누가 아직 수강신청을 안 했는가?'를 파악하여 독려 메일을 보내는 등의 조치를 취할 수 있습니다.
    *   **Pandas 코드 (슬라이드 예시):**
        ```python
        import pandas as pd

        # 슬라이드 예시: babynames 데이터와 특정 이름 목록을 가정 (세미조인과 동일)
        babynames = pd.DataFrame({
            'Name': ['Mary', 'John', 'Alice', 'Bob', 'Mary'],
            'Year': [2000, 2000, 2001, 2002, 2003],
            'Count': [5000, 4000, 3000, 2000, 5100]
        })

        # 찾고자 하는 이름들의 목록 (S 역할)
        keys = pd.DataFrame({'Name': ['Mary', 'Alice']})

        # 슬라이드에서 제시된 안티조인 구현 방식 (Left Join + indicator 활용)
        anti_join_result_slide_method = (
            babynames.merge(keys, on="Name", how="left", indicator=True)
            .query("_merge == 'left_only'") # 왼쪽 테이블에만 존재하는 행 필터링
            .drop(columns=["_merge"])      # _merge 컬럼 제거
        )
        print("\n--- Antijoin Result (using slide method) ---")
        print(anti_join_result_slide_method)

        # 더 간결한 Antijoin 구현 방식 (~isin() 활용)
        anti_join_result_isin_method = babynames[~babynames["Name"].isin(keys["Name"])]
        print("\n--- Antijoin Result (using ~isin() method) ---")
        print(anti_join_result_isin_method)
        ```
        *   **결과 설명:** `babynames`에서 'Name' 컬럼 값이 `keys` 데이터프레임의 'Name' 컬럼에 존재하지 않는 모든 행(즉, 'John'과 'Bob'의 기록)이 반환됩니다. 슬라이드 방식과 `~isin()` 방식 모두 동일한 결과를 반환하며, 실제 사용 시에는 `~isin()` 방식이 더 직관적이고 간결하게 안티조인을 구현하는 방법으로 자주 쓰입니다.

---

## Slide 20

### 핵심 개념: 데이터 그룹화 및 집계 (Grouping/Aggregation)

데이터 그룹화 및 집계는 특정 기준(하나 또는 여러 개의 컬럼)에 따라 데이터를 여러 그룹으로 나눈 다음, 각 그룹 내에서 평균, 합계, 최댓값, 최솟값 등과 같은 통계량을 계산하는 작업입니다. 이를 통해 전체 데이터셋에서는 볼 수 없었던 유의미한 패턴이나 요약을 얻을 수 있습니다.

**실생활 예시:**
대형마트에서 고객들의 구매 데이터를 분석한다고 가정해봅시다. 이 데이터에는 고객 ID, 성별, 연령, 구매 상품 카테고리, 구매 금액 등의 정보가 포함되어 있습니다. 마케팅 팀에서는 특정 그룹의 구매 행태를 파악하여 맞춤형 프로모션을 기획하고 싶어 합니다.

1.  **그룹화 기준 설정**: 마케팅 팀은 고객을 '성별'과 '나이대' 기준으로 나누어 분석하고자 합니다. 예를 들어, '여성 20대', '남성 30대'와 같이 그룹을 나눕니다.
    *   이때 슬라이드의 `babynames["decade"] = (babynames["Year"] // 10) * 10` 코드는 고객 데이터의 '연령' 컬럼을 '나이대'(예: 20, 30, 40) 컬럼으로 변환하는 과정과 유사합니다. (예: 1995년생이면 `1995 // 10 * 10 = 1990`으로 '1990년대생'으로 분류)

2.  **집계 함수 적용**: 각 그룹(예: '여성 20대')에 대해 구매 금액 데이터를 집계합니다.
    *   **평균 구매 금액**: 이 그룹의 고객들이 평균적으로 얼마를 구매하는가? (슬라이드의 `mean="mean"`에 해당)
    *   **최대 구매 금액**: 이 그룹 내에서 가장 많이 구매한 고객의 구매 금액은 얼마인가? (슬라이드의 `max="max"`에 해당)
    *   **총 구매 금액**: 이 그룹의 고객들이 총 얼마를 구매했는가? (슬라이드의 `total="sum"`에 해당)

이 과정을 통해 우리는 '여성 20대 고객은 평균 구매 금액이 X원이고, 주로 Y 카테고리에서 구매하며, 특정 주말에 최대 구매 금액을 기록했다'와 같은 인사이트를 얻을 수 있습니다.

**Pandas 코드 매핑:**

```python
# 1. 'decade' 컬럼 생성 (나이대 또는 연대 정보)
# 예시: babynames 데이터의 "Year" 컬럼을 10으로 나누고 버림하여 연대를 만듭니다.
babynames["decade"] = (babynames["Year"] // 10) * 10

# 2. 'Sex'와 'decade'를 기준으로 그룹화하고 'Count'(여기서는 구매 금액) 컬럼에 대해 집계
stats = (babynames.groupby(["Sex", "decade"])["Count"]
                 .agg(mean="mean", max="max", total="sum") # 각 그룹별 평균, 최댓값, 합계를 계산합니다.
                 .reset_index()) # 최종 결과를 보기 좋게 정리합니다.
```

### `reset_index()`의 필요성

`groupby()` 연산을 수행하면, 기본적으로 그룹화에 사용된 컬럼들(예: 'Sex', 'decade')이 결과 DataFrame의 **인덱스**가 됩니다. 이때 인덱스가 여러 레벨을 가지는 'MultiIndex' 형태가 될 수 있습니다. `reset_index()`는 이러한 인덱스를 일반 컬럼으로 되돌려주는 역할을 합니다.

**실생활 예시 (대형마트 고객 데이터 이어서):**
그룹화 및 집계 결과, '성별'과 '나이대'가 인덱스로 설정된 DataFrame이 나왔다고 가정해봅시다.

| Sex | decade |     | mean | max | total |
| :-- | :----- | :-- | :--- | :-- | :---- |
| Female | 1990 |     | 12000 | 50000 | 1200000 |
|        | 2000 |     | 15000 | 70000 | 1500000 |
| Male   | 1990 |     | 10000 | 40000 | 1000000 |
|        | 2000 |     | 13000 | 60000 | 1300000 |

이 형태는 특정 그룹의 통계치를 확인하기에는 좋지만, 다른 데이터와 결합하거나(merge/join), 결과를 다시 필터링하거나, 특정 컬럼을 기준으로 정렬하는 등의 **후속 작업(downstream tasks)**에서는 다소 불편할 수 있습니다. 마치 보고서의 목차처럼 인덱스로 들어가 있어서 데이터 자체로 활용하기가 번거로운 상황입니다.

`reset_index()`를 적용하면 아래와 같이 'Sex'와 'decade'가 일반 데이터 컬럼으로 돌아옵니다.

|      | Sex | decade | mean | max | total |
| :--- | :-- | :----- | :--- | :-- | :---- |
| 0    | Female | 1990 | 12000 | 50000 | 1200000 |
| 1    | Female | 2000 | 15000 | 70000 | 1500000 |
| 2    | Male   | 1990 | 10000 | 40000 | 1000000 |
| 3    | Male   | 2000 | 13000 | 60000 | 1300000 |

이처럼 일반 컬럼으로 만들면 다음과 같은 이점이 있습니다.

1.  **데이터 접근 용이성**: 'Sex'나 'decade'를 직접 컬럼 이름으로 사용하여 데이터를 필터링하거나 선택하기 훨씬 편리해집니다.
2.  **쉬운 병합/조인 (Easier merges/joins)**: 만약 마케팅 팀이 특정 '성별'과 '나이대' 그룹에 대한 설문조사 데이터(예: 만족도 점수)를 가지고 있고, 이를 집계 결과와 합치고 싶다면, `Sex`와 `decade`가 일반 컬럼으로 존재해야 이 두 컬럼을 기준으로 쉽게 `merge()` 연산을 수행할 수 있습니다. `on=["Sex", "decade"]`와 같이 명시적으로 조인 키를 지정할 수 있으며, 인덱스를 기준으로 조인할 때 필요한 `right_index=True` 같은 추가 옵션 없이도 편리하게 작업할 수 있습니다.

요약하자면, `reset_index()`는 `groupby` 결과의 인덱스를 일반 컬럼으로 변환하여 데이터를 다루기 더 쉬운 표준 DataFrame 형태로 만들어주는 필수적인 단계입니다.

---

## Slide 21

안녕하세요! pandas의 `GroupBy`는 데이터 분석에서 정말 강력하고 중요한 개념입니다. 슬라이드의 핵심 개념들을 '실생활 예시'와 함께 친절하고 명확하게 설명해 드릴게요.

---

### pandas GroupBy: 데이터를 나누고 분석하는 똑똑한 방법

`pandas GroupBy`는 원본 `DataFrame`이나 `Series`를 특정 기준(하나 이상의 컬럼)에 따라 논리적으로 '분할'하고, 각 분할된 그룹에 독립적인 연산을 적용할 수 있게 해주는 기능입니다. 마치 큰 덩어리의 데이터를 여러 작은 덩어리로 쪼개어 개별적으로 살펴본 뒤, 그 결과를 다시 합치는 과정과 유사합니다.

#### 1. 핵심 개념: GroupBy는 '매핑'이자 '지연 평가' 방식의 '파티셔닝'입니다.

*   **DataFrameGroupBy (DataFrame을 그룹화하는 경우):**
    *   `DataFrameGroupBy` 객체는 원본 `DataFrame`을 **파티셔닝(partitioning)**합니다. 여기서 파티셔닝이란 데이터를 물리적으로 여러 개로 복사하여 나누는 것이 아니라, 특정 기준(그룹 키 값)에 따라 논리적으로 '묶음'을 만드는 것을 의미합니다.
    *   이는 **게으른(lazy) 방식의, 뷰(view)-라이크 매핑(view-like mapping)**입니다. `groupby()`를 호출하는 순간 바로 데이터의 복사본을 만들어 분할된 `DataFrame`들을 생성하는 것이 아닙니다. 대신, 각 **그룹 키 값** (예: '서울 지점', '부산 지점')이 해당 그룹에 속하는 **하위 DataFrame (sub-DataFrame)**을 어떻게 찾아야 하는지에 대한 '지도(mapping)'를 만듭니다.
    *   **비유:** 여러분이 대형 마트의 모든 판매 기록(원본 DataFrame)을 가지고 있다고 상상해 보세요. `groupby('상품 카테고리')`를 하면, pandas는 "음료는 1번 선반에, 과자는 2번 선반에, 채소는 3번 선반에 있어!"라고 적힌 목록(GroupBy 객체)을 만드는 것과 같습니다. 이 목록은 실제로 상품들을 물리적으로 분리해서 진열한 것이 아니라, 어떤 상품 카테고리가 어디에 있는지 알려주는 '지도'인 거죠.

*   **SeriesGroupBy (Series를 그룹화하는 경우):**
    *   마찬가지로 `SeriesGroupBy`는 그룹 키 값을 **하위 Series (sub-Series)**에 매핑합니다. 예를 들어, 특정 지점별 '총 판매 금액'만 보려면, 판매 금액 Series를 지점 ID로 그룹화할 수 있습니다.

*   **데이터 복사 없음 (No Copy):**
    *   `groupby()` 메서드를 호출하는 시점에는 데이터의 **복사본이 전혀 만들어지지 않습니다.** 이것은 매우 중요한 성능 최적화입니다. 실제 하위 `DataFrame`이나 `Series`는 여러분이 해당 그룹 데이터에 접근하거나, 특정 연산(예: `for` 루프, `get_group()`, `apply()`, `agg()` 등)을 수행할 때 비로소 '생성(materialized)'됩니다.
    *   **비유:** 마트 목록(GroupBy 객체)만 있을 뿐, 실제 상품(sub-DataFrame)은 여러분이 "과자 코너 좀 보여주세요!"라고 요청할 때까지는 꺼내놓지 않는 것과 같아요. 요청이 있을 때만 필요한 부분만 꺼내 보여주는 거죠.

#### 2. 실생활 예시로 이해하기

우리는 여러 지점을 가진 카페 체인의 일일 판매 데이터를 분석한다고 가정해봅시다.

**원본 데이터:**

```python
import pandas as pd

data = {
    '지점_ID': ['강남점', '강남점', '강남점', '홍대점', '홍대점', '강남점', '종로점', '종로점'],
    '상품_카테고리': ['음료', '빵', '음료', '음료', '빵', '음료', '빵', '음료'],
    '판매수량': [5, 2, 8, 10, 3, 3, 5, 7],
    '개당_가격': [4000, 3000, 4500, 3800, 3500, 4200, 3200, 4100]
}
df = pd.DataFrame(data)
print("--- 원본 판매 데이터 ---")
print(df)
# 예상 출력:
#   지점_ID 상품_카테고리  판매수량  개당_가격
# 0   강남점     음료     5   4000
# 1   강남점      빵     2   3000
# 2   강남점     음료     8   4500
# 3   홍대점     음료    10   3800
# 4   홍대점      빵     3   3500
# 5   강남점     음료     3   4200
# 6   종로점      빵     5   3200
# 7   종로점     음료     7   4100
```

---

#### 3. GroupBy 객체 생성 및 탐색 (Navigation API)

`groupby()`를 호출하여 `DataFrameGroupBy` 객체를 생성합니다. 이 객체는 앞서 설명한 '지도'입니다.

```python
# '지점_ID' 기준으로 그룹화
store_groups = df.groupby('지점_ID')

print(f"\n--- GroupBy 객체 생성 ---")
print(f"df.groupby('지점_ID') 결과의 타입: {type(store_groups)}")
# 예상 출력: <class 'pandas.core.groupby.generic.DataFrameGroupBy'>
# 보시다시피, GroupBy 객체가 생성되었을 뿐 원본 DataFrame이 바뀐 것은 아닙니다.
```

**3.1. 각 그룹을 순회하며 확인 (`for key, subdf in g:`)**

`GroupBy` 객체는 각 그룹에 대해 반복할 수 있습니다. `key`는 그룹의 키 값(여기서는 지점 ID)이고, `subdf`는 해당 그룹에 해당하는 하위 `DataFrame`입니다. 이 때 `subdf`가 비로소 생성됩니다.

```python
print("\n--- 각 지점별 판매 데이터 및 총 매출 확인 (for 루프) ---")
for store_id, store_sales_df in store_groups:
    print(f"\n### {store_id} 지점 판매 데이터:")
    print(store_sales_df)
    total_revenue = (store_sales_df['판매수량'] * store_sales_df['개당_가격']).sum()
    print(f"  > 총 매출: {total_revenue:,}원")

# 예상 출력 (일부 발췌):
# ### 강남점 지점 판매 데이터:
#   지점_ID 상품_카테고리  판매수량  개당_가격
# 0   강남점     음료     5   4000
# 1   강남점      빵     2   3000
# 2   강남점     음료     8   4500
# 5   강남점     음료     3   4200
#   > 총 매출: 77,600원
# ... (다른 지점들도 동일하게 출력)
```

**3.2. 특정 그룹만 선택하여 확인 (`g.get_group(key)`)**

특정 그룹의 하위 `DataFrame`만 직접 얻고 싶을 때 사용합니다.

```python
print("\n--- 홍대점 판매 데이터만 보기 (get_group) ---")
hongdae_sales = store_groups.get_group('홍대점')
print(hongdae_sales)

# 예상 출력:
#   지점_ID 상품_카테고리  판매수량  개당_가격
# 3   홍대점     음료    10   3800
# 4   홍대점      빵     3   3500
```

---

#### 4. 그룹에 함수 적용하기 (가장 강력한 기능)

`GroupBy`의 진정한 힘은 각 그룹에 통계 함수(`sum()`, `mean()`, `count()`, `max()`, `min()`)를 적용하거나, `apply()`, `transform()` 같은 사용자 정의 함수를 적용하는 데 있습니다.

**4.1. `apply()` 예시: 각 지점별 심층 통계 분석**

`apply()`는 각 하위 `DataFrame` (또는 `Series`)에 원하는 함수를 적용하고, 그 결과를 모아 새로운 `DataFrame`이나 `Series`를 만듭니다.

```python
print("\n--- 각 지점별 평균 판매수량 및 총 매출 (apply) ---")
store_stats = store_groups.apply(lambda x: pd.Series({
    '평균_판매수량': x['판매수량'].mean(),
    '총_매출': (x['판매수량'] * x['개당_가격']).sum()
}))
print(store_stats)

# 예상 출력:
#          평균_판매수량    총_매출
# 지점_ID
# 강남점      4.5  77600.0
# 종로점      6.0  46300.0
# 홍대점      6.5  48500.0
```
**설명:** `apply()`는 각 `store_sales_df` (강남점, 홍대점, 종로점의 하위 DataFrame)에 대해 `lambda` 함수를 실행합니다. 이 함수는 각 지점의 평균 판매수량과 총 매출을 계산하여 새로운 Series로 반환하고, `apply()`는 이 Series들을 모아 최종 `DataFrame`을 만들어줍니다.


**4.2. `transform()` 예시: 각 판매 건이 해당 지점 총 판매수량에서 차지하는 비율 계산**

`transform()`은 각 그룹 내에서 연산을 수행하되, 원본 `DataFrame`과 **동일한 인덱스와 크기를 가진 결과**를 반환합니다. 이는 그룹별 계산 결과를 원본 `DataFrame`의 새로운 컬럼으로 쉽게 추가할 때 유용합니다.

```python
print("\n--- 각 판매 건이 해당 지점 총 판매수량에서 차지하는 비율 (transform) ---")
# 각 판매 건별로, 해당 지점의 전체 판매수량 대비 해당 상품의 판매수량이 몇 %인지 알고 싶을 때
df['지점_내_판매수량_비율'] = df.groupby('지점_ID')['판매수량'].transform(lambda x: x / x.sum())
print(df)

# 예상 출력:
#   지점_ID 상품_카테고리  판매수량  개당_가격  지점_내_판매수량_비율
# 0   강남점     음료     5   4000      0.277778  (5 / (5+2+8+3))
# 1   강남점      빵     2   3000      0.111111
# 2   강남점     음료     8   4500      0.444444
# 3   홍대점     음료    10   3800      0.769231  (10 / (10+3))
# 4   홍대점      빵     3   3500      0.230769
# 5   강남점     음료     3   4200      0.166667
# 6   종로점      빵     5   3200      0.416667  (5 / (5+7))
# 7   종로점     음료     7   4100      0.583333
```
**설명:** `transform()`은 각 지점(그룹) 내에서 '판매수량'의 총합을 계산한 뒤, 해당 지점 내의 각 '판매수량'을 이 총합으로 나누어 비율을 구합니다. 중요한 것은 결과 Series의 길이가 원본 `df`의 길이와 같고, 각 행의 `지점_내_판매수량_비율`이 해당 지점의 총 판매수량에 기반하여 계산된다는 점입니다.

---

`pandas GroupBy`는 이처럼 데이터를 유연하게 분할하고 분석하는 데 있어 핵심적인 도구입니다. '복사본 없이' '지연 평가' 방식으로 작동한다는 점과, 다양한 API를 통해 그룹 데이터를 탐색하고 연산할 수 있다는 점을 잘 기억해두세요!

---

## Slide 22

핵심 개념과 실생활 예시를 통해 Pandas DataFrame의 `groupby()`, `sum()`, 그리고 인덱스 처리에 대해 자세히 설명해 드릴게요.

---

### Pandas `groupby()`: 데이터 집계 및 인덱스 처리

`groupby()`는 특정 기준에 따라 데이터를 그룹으로 묶고, 각 그룹에 대해 합계, 평균, 개수 등 다양한 통계 연산(집계)을 수행할 때 사용되는 강력한 함수입니다. 슬라이드에서는 특히 `sum()` 연산과 그 결과로 나타나는 인덱스 처리 방식에 중점을 두고 있습니다.

#### 1. 기본 집계: `df.groupby('기준').sum()`

*   **개념:** `df.groupby('기준')`은 DataFrame을 지정된 '기준' 컬럼의 고유한 값들을 바탕으로 여러 그룹으로 나눕니다. 여기에 `.sum()`을 붙이면, 각 그룹 내의 **숫자형** 컬럼들을 합산합니다.
*   **실생활 예시:**
    여러분은 작은 온라인 상점에서 다양한 상품을 판매하고 있습니다. 일별 주문 데이터를 관리하는 `DataFrame` `df`가 있다고 가정해 봅시다.

    | 주문번호 | 고객ID | 상품명   | 수량 | 단가   |
    | :----- | :----- | :------- | :--- | :----- |
    | 101    | A      | 바나나   | 5    | 2000   |
    | 102    | B      | 오렌지   | 3    | 3000   |
    | 103    | A      | 사과     | 2    | 1500   |
    | 104    | C      | 바나나   | 4    | 2000   |
    | 105    | B      | 사과     | 1    | 1500   |

    이때, **각 상품이 총 몇 개 팔렸는지** 알고 싶다면 `groupby('상품명').sum()`을 사용합니다.

    ```python
    df.groupby('상품명').sum()
    ```

    *   **결과:**
        | 상품명   | 주문번호 | 수량 | 단가   |
        | :------- | :------- | :--- | :----- |
        | 바나나   | 205    | 9    | 4000   |
        | 사과     | 208    | 3    | 3000   |
        | 오렌지   | 102    | 3    | 3000   |

    *   **설명:**
        *   `상품명` 컬럼의 '바나나', '오렌지', '사과'를 기준으로 그룹이 나뉘었습니다.
        *   각 그룹 내에서 '수량' 컬럼이 합산되어 '바나나'는 5 + 4 = 9개, '오렌지'는 3개, '사과'는 2 + 1 = 3개가 팔렸음을 알 수 있습니다.
        *   `주문번호`와 `단가`도 숫자형 컬럼이므로 자동으로 합산되었습니다. 하지만 이 경우에는 `주문번호`를 합산하는 것은 의미가 없으며, `단가`의 합산은 각 주문 라인의 단가를 단순히 더한 것이므로 총 매출액과는 다를 수 있습니다. (만약 정확한 총 매출을 원했다면, `total_price = df['수량'] * df['단가']`와 같은 새 컬럼을 만들고 이를 `groupby`하는 것이 좋습니다.) 슬라이드의 예시처럼 `quantity`만 있다면 직관적입니다.

#### 2. 인덱스 처리 (`.reset_index()` 또는 `as_index=False`)

`groupby().sum()`을 수행하면, 기본적으로 그룹화의 기준이 되었던 컬럼('상품명' 등)이 결과 `DataFrame`의 **인덱스**가 됩니다. 인덱스는 `DataFrame`의 각 행을 식별하는 고유한 레이블입니다. 때로는 이 인덱스를 일반 컬럼으로 다시 사용하고 싶거나, 처음부터 인덱스가 되는 것을 원치 않을 수 있습니다.

*   **`reset_index()`: 인덱스를 일반 컬럼으로 변경**
    *   **개념:** `groupby()`의 결과로 인덱스가 된 컬럼을 일반 데이터 컬럼으로 되돌리고, 자동으로 0부터 시작하는 새로운 정수 인덱스를 부여합니다.
    *   **실생활 예시:**
        위에서 얻은 `groupby()` 결과 `DataFrame`을 가지고, '상품명'을 인덱스가 아닌 일반 컬럼으로 보고 싶을 때 사용합니다.

        ```python
        df.groupby('상품명').sum().reset_index()
        ```

        *   **결과:**
            |    | 상품명   | 주문번호 | 수량 | 단가   |
            |---:| :------- | :------- | :--- | :----- |
            | 0  | 바나나   | 205    | 9    | 4000   |
            | 1  | 사과     | 208    | 3    | 3000   |
            | 2  | 오렌지   | 102    | 3    | 3000   |

        *   **설명:** '상품명'이 일반 컬럼으로 다시 들어왔고, 0, 1, 2의 새로운 인덱스가 생성되었습니다. 이렇게 하면 '상품명' 컬럼에 대한 필터링이나 정렬 같은 추가 분석을 더 쉽게 할 수 있습니다.

*   **`as_index=False`: 처음부터 인덱스 생성을 방지**
    *   **개념:** `groupby()` 함수 내에서 `as_index=False` 옵션을 지정하면, 그룹화 기준이 되는 컬럼이 애초에 인덱스로 설정되지 않고 일반 데이터 컬럼으로 유지됩니다. 이는 `reset_index()`를 한 번 더 호출하는 과정을 생략할 수 있게 해줍니다.
    *   **실생활 예시:**
        처음부터 상품명 컬럼을 인덱스가 아닌 일반 컬럼으로 유지하면서 각 상품의 총 수량을 계산하고 싶을 때.

        ```python
        df.groupby('상품명', as_index=False).sum()
        ```

        *   **결과:** `reset_index()`를 사용했을 때와 동일한 결과를 얻습니다.
            |    | 상품명   | 주문번호 | 수량 | 단가   |
            |---:| :------- | :------- | :--- | :----- |
            | 0  | 바나나   | 205    | 9    | 4000   |
            | 1  | 사과     | 208    | 3    | 3000   |
            | 2  | 오렌지   | 102    | 3    | 3000   |

        *   **설명:** 이 방법은 코드를 더 간결하게 만들어주어 가독성이 높아지고, 불필요한 연산을 줄일 수 있습니다.

#### 3. 숫자형 컬럼만 합산

*   **개념:** `sum()`과 같은 집계 함수는 기본적으로 `DataFrame` 내의 **숫자형(numeric)** 데이터를 가진 컬럼에만 적용됩니다. 문자열(text), 날짜(datetime) 등 비숫자형 컬럼은 자동으로 집계 대상에서 제외됩니다.
*   **실생활 예시:**
    처음의 주문 데이터 `DataFrame` `df`에서 `고객ID` 컬럼은 문자열입니다. `groupby().sum()`을 수행하면 `고객ID` 컬럼은 결과 `DataFrame`에 나타나지 않습니다.

    | 주문번호 | 고객ID | 상품명   | 수량 | 단가   |
    | :----- | :----- | :------- | :--- | :----- |
    | 101    | A      | 바나나   | 5    | 2000   |
    | 102    | B      | 오렌지   | 3    | 3000   |
    | 103    | A      | 사과     | 2    | 1500   |
    | 104    | C      | 바나나   | 4    | 2000   |
    | 105    | B      | 사과     | 1    | 1500   |

    `df.groupby('상품명').sum()`의 결과에서 `고객ID`가 없는 것을 볼 수 있습니다. 고객ID는 숫자가 아니므로 합산하는 것이 의미가 없기 때문에 자동으로 제외됩니다. 만약 특정 비숫자형 컬럼을 포함하고 싶다면, `groupby()` 전에 해당 컬럼을 제외하거나, 다른 방식으로 처리해야 합니다.

---

이 설명이 `groupby()`와 관련된 개념들을 완벽하게 이해하는 데 도움이 되었기를 바랍니다! 궁금한 점이 있다면 언제든지 다시 질문해주세요.

---

## Slide 23

### `groupby()`: 컬럼 선택과 속성 접근

Pandas의 `groupby()` 함수는 데이터를 특정 기준에 따라 그룹화하고 각 그룹에 대해 통계 연산을 수행할 때 사용됩니다. 이때, 어떤 컬럼에 대해 집계(aggregation)를 수행할 것인지 선택하는 방식에 따라 결과의 형태와 내용이 달라지며, 주로 세 가지 방법이 있습니다.

#### 1. 모든 숫자형 컬럼 집계: `df.groupby('기준컬럼').sum()`

*   **설명:** `groupby()` 연산 후 특정 컬럼을 명시적으로 선택하지 않고 바로 `sum()`, `mean()`과 같은 집계 함수를 호출하면, 그룹화 기준이 된 컬럼을 제외한 **모든 숫자형(numeric) 컬럼**에 대해 집계 연산이 수행됩니다. 결과는 Pandas `DataFrame` 형태로 반환됩니다.
*   **실생활 예시:**
    당신이 운영하는 온라인 서점의 오늘 판매 내역 `df`가 다음과 같다고 가정해 봅시다. 각 행은 고객의 한 번의 도서 구매를 나타냅니다.
    ```python
    import pandas as pd

    df = pd.DataFrame({
        '고객': ['Alice', 'Bob', 'Alice'],
        '도서명': ['파이썬 정복', '데이터 과학 입문', '파이썬 정복'],
        '수량': [3, 2, 5],
        '단가': [15000, 20000, 15000], # 이 거래에서 책 1권당 가격
        '총결제금액': [45000, 40000, 75000] # 수량 * 단가
    })
    print(df)
    #       고객         도서명  수량    단가   총결제금액
    # 0   Alice     파이썬 정복   3  15000   45000
    # 1     Bob  데이터 과학 입문   2  20000   40000
    # 2   Alice     파이썬 정복   5  15000   75000
    ```
    이 서점에서 어떤 `도서명`이 얼마나 많이 팔렸는지 (총 `수량`), 해당 도서로 인해 발생한 총 매출(`총결제금액`)을 알고 싶을 때, 다음과 같이 사용할 수 있습니다.
    ```python
    df.groupby('도서명').sum()
    ```
    **결과:**
    ```
                      수량     단가    총결제금액
    도서명
    데이터 과학 입문      2   20000    40000
    파이썬 정복          8   30000   120000
    ```
    *   **설명:**
        *   `'데이터 과학 입문'`은 2권이 팔려 40000원의 매출을 기록했습니다. `단가`는 20000원입니다.
        *   `'파이썬 정복'`은 Alice가 3권, 5권 총 8권이 팔려 120000원의 매출을 기록했습니다. 이때 `단가`는 Alice의 두 번의 구매 시 단가를 합한 15000 + 15000 = 30000원으로 계산되는데, 이는 "모든 숫자형 컬럼을 합계"하는 Pandas의 기본 동작에 의한 것입니다. 이 `단가`의 합계는 실제 비즈니스에서는 큰 의미를 갖지 않을 수 있습니다. 중요한 것은 `수량`과 `총결제금액`의 합계입니다.

#### 2. 단일 컬럼 선택 (속성 접근): `df.groupby('기준컬럼').선택컬럼.sum()`

*   **설명:** `groupby()` 연산 후에 `.`(점)을 사용하여 특정 컬럼 이름으로 접근하면, 해당 **단일 컬럼**에 대해서만 집계 연산이 수행됩니다. 결과는 Pandas `Series` 형태로 반환됩니다. 이는 마치 객체의 속성(attribute)에 접근하는 것과 유사합니다.
*   **실생활 예시:**
    위 서점 예시에서 각 `도서명`별로 팔린 총 `수량`만 알고 싶을 때 다음과 같이 사용할 수 있습니다.
    ```python
    df.groupby('도서명').수량.sum()
    ```
    **결과:**
    ```
    도서명
    데이터 과학 입문    2
    파이썬 정복        8
    Name: 수량, dtype: int64
    ```
    *   **설명:** `'데이터 과학 입문'`은 총 2권, `'파이썬 정복'`은 총 8권이 판매되었음을 Series 형태로 명확하게 보여줍니다.

#### 3. 여러 컬럼 선택 (리스트 활용): `df.groupby('기준컬럼')[['선택컬럼1', '선택컬럼2']].sum()`

*   **설명:** `groupby()` 연산 후에 `[[]]` (대괄호 안에 리스트)를 사용하여 **여러 컬럼 이름**을 명시하면, 해당 컬럼들에 대해서만 집계 연산이 수행됩니다. 결과는 항상 Pandas `DataFrame` 형태로 반환됩니다.
*   **실생활 예시:**
    위 서점 예시에서 각 `도서명`별로 팔린 총 `수량`과 해당 도서로 인한 총 `총결제금액`만 알고 싶을 때 다음과 같이 사용할 수 있습니다.
    ```python
    df.groupby('도서명')[['수량', '총결제금액']].sum()
    ```
    **결과:**
    ```
                      수량    총결제금액
    도서명
    데이터 과학 입문      2    40000
    파이썬 정복          8   120000
    ```
    *   **설명:** `'데이터 과학 입문'`은 2권이 팔려 40000원의 매출을, `'파이썬 정복'`은 8권이 팔려 120000원의 매출을 기록했음을 보여줍니다. `수량`과 `총결제금액` 두 컬럼을 선택했으므로 결과는 DataFrame 형태입니다.

---

**핵심 요약:**

*   **`df.groupby().sum()`**: 모든 숫자형 컬럼 집계, 결과는 DataFrame.
*   **`df.groupby().컬럼명.sum()`**: 단일 컬럼 집계, 결과는 Series.
*   **`df.groupby()[['컬럼1', '컬럼2']].sum()`**: 여러 컬럼 집계, 결과는 DataFrame.

이 세 가지 방법은 데이터 분석 시 필요에 따라 유연하게 컬럼을 선택하고 원하는 형태의 집계 결과를 얻는 데 매우 중요합니다.

---

## Slide 24

## Pandas에서의 이름 지정 집계 (Named Aggregations)

첨부된 슬라이드의 핵심 개념은 Pandas DataFrame에서 `groupby()`와 `agg()` 메서드를 함께 사용하여, **특정 그룹별로 여러 컬럼에 각각 다른 집계 함수를 적용**하는 방법입니다. 이때 `agg()` 메서드에 딕셔너리(`{}`) 형태로 컬럼 이름과 적용할 집계 함수를 지정하여, 결과 DataFrame의 컬럼들이 원본 컬럼 이름으로 의미 있게 유지되도록 하는 것이 특징입니다.

---

### 핵심 개념 설명

1.  **그룹화 (Grouping):** `df.groupby('product')`는 DataFrame `df`를 `'product'` 컬럼의 고유한 값(예: 'bananas', 'oranges')을 기준으로 여러 그룹으로 나눕니다.
2.  **이름 지정 집계 (Named Aggregations):** `agg({'quantity': 'sum', 'price': 'mean'})` 부분에서 이름 지정 집계가 일어납니다.
    *   `agg()` 메서드에 딕셔너리를 전달합니다. 이 딕셔너리의 `키`는 집계를 수행할 원본 컬럼의 이름이고, `값`은 해당 컬럼에 적용할 집계 함수(예: `'sum'`, `'mean'`, `'min'`, `'max'`, `'count'` 등 문자열 또는 함수 객체)입니다.
    *   예시에서는 `'quantity'` 컬럼에는 `sum` 함수를 적용하고, `'price'` 컬럼에는 `mean` 함수를 적용하라고 지시하고 있습니다.
    *   이렇게 하면 각 그룹별로 `'quantity'`는 총합을 계산하고, `'price'`는 평균을 계산하여 새로운 DataFrame을 생성합니다. 결과 DataFrame의 컬럼 이름은 딕셔너리에서 지정한 원본 컬럼 이름 그대로 유지되어 이해하기 쉽습니다.

**슬라이드 예시 해석:**

*   **원본 데이터(`df`):**
    | client | product | quantity | price | total |
    | :----- | :------ | :------- | :---- | :---- |
    | John   | bananas | 5        | 2     | 10    |
    | Silvia | oranges | 3        | 5     | 15    |
    | Andrew | bananas | 4        | 3     | 12    |
*   **코드:** `df.groupby('product').agg({'quantity': 'sum', 'price': 'mean'})`
*   **결과:**
    *   `product`가 `'bananas'`인 그룹:
        *   `quantity`: 5 (John) + 4 (Andrew) = 9 (합계)
        *   `price`: (2 (John) + 3 (Andrew)) / 2 = 2.5 (평균)
    *   `product`가 `'oranges'`인 그룹:
        *   `quantity`: 3 (Silvia) = 3 (합계)
        *   `price`: 5 (Silvia) = 5.0 (평균)

    따라서 결과는 다음과 같습니다.
    | product | quantity | price |
    | :------ | :------- | :---- |
    | bananas | 9        | 2.5   |
    | oranges | 3        | 5.0   |

---

### 구체적이고 실생활에 가까운 예시: 온라인 쇼핑몰 판매 분석

당신이 한 온라인 쇼핑몰의 데이터 분석가라고 상상해 봅시다. 고객 주문 데이터를 가지고 각 **상품 카테고리(category)별로 총 판매량과 평균 단가, 그리고 가장 많이 팔린 상품의 ID**를 분석하고 싶습니다.

**원본 데이터 (`df_sales`):**

| order_id | category     | product_id | quantity | unit_price | customer_rating |
| :------- | :----------- | :--------- | :------- | :--------- | :-------------- |
| 101      | Electronics  | P1001      | 2        | 150.0      | 4.5             |
| 102      | Books        | B2003      | 1        | 25.0       | 4.0             |
| 103      | Electronics  | P1002      | 1        | 300.0      | 4.8             |
| 104      | Books        | B2001      | 3        | 15.0       | 3.9             |
| 105      | Home Goods   | H3005      | 1        | 50.0       | 4.2             |
| 106      | Electronics  | P1001      | 1        | 150.0      | 4.6             |
| 107      | Home Goods   | H3005      | 2        | 50.0       | 4.1             |

**분석 목표:**
*   각 카테고리별 `quantity`의 총합을 알고 싶습니다.
*   각 카테고리별 `unit_price`의 평균을 알고 싶습니다.
*   (추가) 각 카테고리에서 가장 높은 `customer_rating`을 기록한 주문을 알고 싶습니다.

**Pandas 코드:**

```python
import pandas as pd

data = {
    'order_id': [101, 102, 103, 104, 105, 106, 107],
    'category': ['Electronics', 'Books', 'Electronics', 'Books', 'Home Goods', 'Electronics', 'Home Goods'],
    'product_id': ['P1001', 'B2003', 'P1002', 'B2001', 'H3005', 'P1001', 'H3005'],
    'quantity': [2, 1, 1, 3, 1, 1, 2],
    'unit_price': [150.0, 25.0, 300.0, 15.0, 50.0, 150.0, 50.0],
    'customer_rating': [4.5, 4.0, 4.8, 3.9, 4.2, 4.6, 4.1]
}
df_sales = pd.DataFrame(data)

# 이름 지정 집계 적용
category_summary = df_sales.groupby('category').agg({
    'quantity': 'sum',        # 각 카테고리별 총 판매량
    'unit_price': 'mean',     # 각 카테고리별 상품의 평균 단가
    'customer_rating': 'max'  # 각 카테고리에서 가장 높은 고객 평점
})

print(category_summary)
```

**결과 DataFrame (`category_summary`):**

| category    | quantity | unit_price | customer_rating |
| :---------- | :------- | :--------- | :-------------- |
| Books       | 4        | 20.0       | 4.0             |
| Electronics | 4        | 200.0      | 4.8             |
| Home Goods  | 3        | 50.0       | 4.2             |

**결과 해석:**

이 결과를 통해 당신은 다음과 같은 인사이트를 얻을 수 있습니다.

*   **Books 카테고리:** 총 4개의 상품이 판매되었고, 평균 단가는 20.0원이며, 최고 고객 평점은 4.0점입니다.
*   **Electronics 카테고리:** 총 4개의 상품이 판매되었고, 평균 단가는 200.0원이며, 최고 고객 평점은 4.8점입니다. (단가가 높은 상품들이 포함되어 평균 단가도 높습니다.)
*   **Home Goods 카테고리:** 총 3개의 상품이 판매되었고, 평균 단가는 50.0원이며, 최고 고객 평점은 4.2점입니다.

이처럼 `Named Aggregations`는 특정 기준(여기서는 'category')으로 데이터를 묶은 후, 각 그룹에 속한 여러 데이터 항목(`quantity`, `unit_price`, `customer_rating`)에 대해 원하는 통계량(총합, 평균, 최댓값)을 한 번에 효율적으로 계산하고, 그 결과 컬럼들에 의미 있는 이름을 부여하여 분석 결과를 명확하게 보여줄 때 매우 유용합니다.

---

## Slide 25

핵심 개념: 컬럼별 다중 집계 (Multiple Aggregations per Column)

Pandas에서 `groupby()`와 `agg()` 메서드를 함께 사용하여 데이터를 그룹화하고, 각 그룹에 대해 하나 이상의 컬럼에 여러 개의 집계(aggregation) 함수를 동시에 적용하는 방법입니다. 이 과정에서 결과 DataFrame의 컬럼이 계층적 인덱스인 `MultiIndex` 형태로 생성될 수 있습니다.

### 상세 설명

1.  **`groupby()`의 역할**: 데이터프레임을 특정 컬럼(예: 'product')의 고유한 값들을 기준으로 여러 개의 그룹으로 나눕니다. 마치 여러 개의 작은 데이터프레임으로 쪼개는 것과 같습니다.
2.  **`agg()`의 역할**: `groupby()`로 나뉜 각 그룹에 대해 통계적인 집계 함수(예: `sum`, `mean`, `max`, `min`, `count` 등)를 적용하여 데이터를 요약합니다.
3.  **컬럼별 다중 집계**:
    *   `agg()` 메서드에 딕셔너리(`{}`)를 전달하여 어떤 컬럼에 어떤 집계 함수를 적용할지 지정합니다.
    *   **한 컬럼에 하나의 집계 함수**: `'컬럼명': '함수명'` (예: `'quantity': 'sum'`)
    *   **한 컬럼에 여러 개의 집계 함수**: `'컬럼명': ['함수명1', '함수명2', ...]` (예: `'price': ['mean', 'max']`) 형태로 리스트를 사용하여 여러 함수를 지정할 수 있습니다.
4.  **`MultiIndex` 컬럼 생성**: 한 컬럼에 여러 집계 함수를 적용할 경우, 결과 데이터프레임의 컬럼은 최상위 레벨에 원래 컬럼명(예: 'price')이 오고, 그 아래에 적용된 집계 함수명(예: 'mean', 'max')이 오는 계층적 구조(`MultiIndex`)를 가집니다. 이는 데이터를 더욱 구조적으로 보여주는 강력한 기능입니다. 필요에 따라 `map`이나 리스트 컴프리헨션을 사용하여 이 MultiIndex를 단일 레벨 컬럼으로 평탄화(flatten)할 수 있습니다.

### 실생활 예시: 온라인 쇼핑몰 판매 데이터 분석

한 온라인 쇼핑몰에서 발생한 판매 데이터를 분석한다고 가정해 봅시다. `sales_df`라는 데이터프레임에는 `상품명(product)`, `판매량(quantity)`, `단가(price)` 등의 정보가 있습니다.

**원시 데이터 (`sales_df`):**

| 상품명 (product) | 판매량 (quantity) | 단가 (price) |
| :--------------- | :---------------- | :----------- |
| 바나나           | 3                 | 2000         |
| 오렌지           | 5                 | 3000         |
| 바나나           | 2                 | 2500         |
| 사과             | 1                 | 4000         |
| 오렌지           | 3                 | 2800         |
| 바나나           | 4                 | 2300         |

**목표:**
각 `상품명`별로 다음 정보를 얻고 싶습니다.
1.  총 `판매량` (합계)
2.  해당 상품이 판매된 `단가`의 평균
3.  해당 상품이 판매된 `단가` 중 최고가

**Pandas 코드:**

```python
import pandas as pd

# 가상의 판매 데이터프레임 생성
data = {
    'product': ['바나나', '오렌지', '바나나', '사과', '오렌지', '바나나'],
    'quantity': [3, 5, 2, 1, 3, 4],
    'price': [2000, 3000, 2500, 4000, 2800, 2300]
}
sales_df = pd.DataFrame(data)

# 각 상품명별로 총 판매량, 가격의 평균, 가격의 최고가 집계
summary_df = sales_df.groupby('product').agg({
    'quantity': 'sum',           # 'quantity' 컬럼에는 'sum' 함수 적용
    'price': ['mean', 'max']     # 'price' 컬럼에는 'mean'과 'max' 함수 모두 적용
})

print(summary_df)
```

**코드 실행 결과 (`summary_df`):**

```
              quantity         price
                   sum      mean   max
product
사과                   1    4000.0  4000
오렌지                  8    2900.0  3000
바나나                  9  2266.667  2500
```

**결과 해석:**

*   `product` 컬럼은 인덱스가 되어 각 상품별로 데이터가 그룹화되었습니다.
*   `quantity` 컬럼에는 `sum` 함수만 적용되었기 때문에, 'sum'이라는 단일 컬럼명을 가집니다.
*   `price` 컬럼에는 `mean`과 `max` 두 가지 함수가 적용되었기 때문에, `price` 아래에 `mean`과 `max`라는 두 개의 하위 컬럼을 가진 **MultiIndex** 형태로 나타납니다.
    *   예를 들어, '바나나'의 총 판매량은 9개이고, 평균 판매 단가는 약 2266.67원, 최고 판매 단가는 2500원이라는 것을 한눈에 파악할 수 있습니다.

이처럼 `groupby().agg()`를 사용하고 특정 컬럼에 여러 집계 함수를 리스트로 지정함으로써, 복잡한 데이터 분석 요구사항을 간결하고 효율적으로 처리할 수 있습니다.

---

## Slide 26

`Groupby: 명명된 집계 (평평한 열)`

### 핵심 개념: Named Aggregations를 사용한 Groupby 집계

`pandas`에서 `groupby().agg()` 메서드는 데이터를 특정 기준으로 그룹화한 후 각 그룹에 대해 하나 이상의 집계 함수(예: 합계, 평균, 최소값, 최대값)를 적용할 때 사용됩니다. 이때 "명명된 집계(Named Aggregations)"는 출력되는 결과 DataFrame의 열 이름(컬럼명)을 개발자가 직접 지정하여, MultiIndex 형태의 열 구조를 피하고 단일 레벨의 '평평한(flat)' 열을 생성하는 방법입니다.

**주요 특징 및 장점:**

1.  **MultiIndex 회피:** 일반적인 `groupby().agg()`는 여러 함수를 적용할 때 `(원본_열_이름, 집계_함수_이름)` 형태의 MultiIndex 열을 생성할 수 있습니다. 하지만 명명된 집계를 사용하면 `새로운_열_이름`으로 직접 지정하여 단일 레벨의 열을 얻을 수 있어, 결과 DataFrame을 다루기가 훨씬 편리해집니다.
2.  **직관적인 열 이름:** 출력 열의 이름을 'quantity_sum'이나 'price_min'과 같이 함수가 붙는 방식이 아닌, '총_판매_수량', '최소_가격' 등 데이터를 즉각적으로 이해할 수 있는 의미 있는 이름으로 지정할 수 있습니다.
3.  **문법:** `groupby('그룹_기준_열').agg(새로운_열_이름=('원본_열_이름', '집계_함수'))` 형태를 따릅니다.
    *   `새로운_열_이름`: 결과 DataFrame에 나타날 열의 이름입니다.
    *   `('원본_열_이름', '집계_함수')`: 원본 DataFrame에서 집계할 열과 적용할 집계 함수(예: 'sum', 'min', 'max', 'mean', 'count')를 튜플 형태로 지정합니다.

### 구체적인 실생활 예시: 온라인 쇼핑몰 판매 데이터 분석

당신은 온라인 쇼핑몰의 데이터 분석가입니다. 매일 수많은 상품이 판매되며, 각 판매 기록은 `상품명`, `카테고리`, `판매_수량`, `단가` 정보를 포함하고 있습니다.
여기서 각 `카테고리`별로 다음 정보를 알고 싶습니다.

1.  해당 카테고리의 **총 판매 수량**
2.  해당 카테고리 상품들의 **최소 판매 단가**
3.  해당 카테고리 상품들의 **최대 판매 단가**

**원본 데이터 (가상의 `sales_df` DataFrame):**

| 상품명        | 카테고리 | 판매_수량 | 단가  |
| :------------ | :------- | :-------- | :---- |
| 노트북 Pro    | 전자제품 | 50        | 150만원 |
| 스마트폰 A    | 전자제품 | 120       | 80만원 |
| 냉장고 Smart  | 가전제품 | 10        | 200만원 |
| 다이슨 청소기 | 가전제품 | 30        | 70만원 |
| 패딩 점퍼     | 의류     | 80        | 25만원 |
| 운동화 X      | 의류     | 150       | 10만원 |
| 데스크탑 게이밍 | 전자제품 | 20        | 220만원 |
| 세탁기 슬림   | 가전제품 | 15        | 120만원 |

**Python (Pandas) 코드:**

```python
import pandas as pd

# 가상의 판매 데이터 DataFrame 생성
data = {
    '상품명': ['노트북 Pro', '스마트폰 A', '냉장고 Smart', '다이슨 청소기', '패딩 점퍼', '운동화 X', '데스크탑 게이밍', '세탁기 슬림'],
    '카테고리': ['전자제품', '전자제품', '가전제품', '가전제품', '의류', '의류', '전자제품', '가전제품'],
    '판매_수량': [50, 120, 10, 30, 80, 150, 20, 15],
    '단가': [1500000, 800000, 2000000, 700000, 250000, 100000, 2200000, 1200000]
}
sales_df = pd.DataFrame(data)

# '카테고리'별로 총 판매 수량, 최소 단가, 최대 단가를 명명된 집계를 사용하여 계산
category_summary = sales_df.groupby('카테고리').agg(
    총_판매_수량=('판매_수량', 'sum'),
    최소_판매_단가=('단가', 'min'),
    최대_판매_단가=('단가', 'max')
)

print(category_summary)
```

**코드 실행 결과:**

| 카테고리 | 총_판매_수량 | 최소_판매_단가 | 최대_판매_단가 |
| :------- | :----------- | :------------- | :------------- |
| 가전제품 | 55           | 700000         | 2000000        |
| 전자제품 | 190          | 800000         | 2200000        |
| 의류     | 230          | 100000         | 250000         |

**예시 설명:**

위 예시에서 `sales_df.groupby('카테고리')`는 모든 판매 기록을 '전자제품', '가전제품', '의류' 카테고리로 묶습니다.
`agg()` 메서드 내에서 우리는 세 가지 명명된 집계를 사용했습니다:

*   `총_판매_수량=('판매_수량', 'sum')`: 각 카테고리 내의 모든 `판매_수량`을 합산하여 '총_판매_수량'이라는 새 열을 만듭니다.
*   `최소_판매_단가=('단가', 'min')`: 각 카테고리 내의 `단가` 중 가장 작은 값을 찾아 '최소_판매_단가'라는 새 열을 만듭니다.
*   `최대_판매_단가=('단가', 'max')`: 각 카테고리 내의 `단가` 중 가장 큰 값을 찾아 '최대_판매_단가'라는 새 열을 만듭니다.

결과 `category_summary` DataFrame을 보면, '카테고리'를 인덱스로 하여 각 카테고리별로 원하는 세 가지 통계량('총_판매_수량', '최소_판매_단가', '최대_판매_단가')이 **직관적이고 평평한 열 이름**으로 깔끔하게 정리되어 있음을 확인할 수 있습니다. 만약 명명된 집계를 사용하지 않았다면, 예를 들어 `df.groupby('카테고리').agg({'판매_수량': 'sum', '단가': ['min', 'max']})`와 같이 코드를 작성했을 때, `('판매_수량', 'sum')`, `('단가', 'min')`, `('단가', 'max')`와 같은 MultiIndex 열이 생성되어 데이터를 다룰 때 추가적인 처리가 필요했을 것입니다. 명명된 집계는 이러한 번거로움을 줄여줍니다.

---

## Slide 27

## 핵심 개념: `groupby().apply()`를 이용한 사용자 정의 집계 (Custom Aggregation)

제시된 슬라이드는 Pandas DataFrame에서 `groupby()`와 `apply()` 메서드를 함께 사용하여 그룹별로 **사용자 정의된 복잡한 계산(메트릭)**을 수행하는 방법을 보여줍니다. 특히, 단순히 내장된 `sum()`, `mean()` 같은 함수로는 해결하기 어려운 **가중 평균(Weighted Mean)**과 같은 계산에 유용합니다.

1.  **`df.groupby('product')`**: 먼저 DataFrame `df`를 'product' (상품) 컬럼을 기준으로 그룹화합니다. 이는 'bananas' 그룹과 'oranges' 그룹으로 데이터를 논리적으로 분할합니다.
2.  **`.apply(lambda x: ...)`**: `apply()` 메서드는 `groupby()`에 의해 생성된 각 그룹에 대해 지정된 함수를 적용합니다. 여기서 `lambda x: ...`는 익명 함수를 의미하며, `x`는 각 그룹에 해당하는 서브(sub) DataFrame을 나타냅니다.
3.  **`x.total.sum() / x.quantity.sum()`**: `apply()`에 전달된 람다 함수는 각 그룹 `x`에 대해 다음을 수행합니다.
    *   `x.total.sum()`: 해당 그룹 내의 'total' (총액) 컬럼 값들을 모두 더합니다.
    *   `x.quantity.sum()`: 해당 그룹 내의 'quantity' (수량) 컬럼 값들을 모두 더합니다.
    *   이 두 합계를 나누어 **그룹별 가중 평균 가격**을 계산합니다. 여기서 'total'은 'quantity * price'이므로, '총액의 합계 / 수량의 합계'는 곧 '가중 평균 가격'을 의미합니다.

결과적으로, 각 상품('bananas', 'oranges')별로 총 판매액을 총 판매 수량으로 나눈 가중 평균 가격이 계산됩니다. 슬라이드의 예시에서는 'bananas'의 경우 (10+12) / (5+4) = 22 / 9 = 2.44, 'oranges'의 경우 15 / 3 = 5.0이 됩니다.

---

### 실생활 예시: 온라인 강의 플랫폼의 강좌별 평균 수강 평점 계산

당신이 온라인 강의 플랫폼의 데이터 분석가라고 가정해봅시다. 각 강좌에는 여러 수강생이 있고, 각 수강생은 강좌 수료 후 평점을 부여합니다. 단순히 평점의 산술 평균을 내는 것이 아니라, **강의 시간(길이)이 긴 강좌의 평점을 더 중요하게 반영하여 각 강좌의 '가중 평균 평점'을 계산**하고 싶습니다.

| StudentID | Course | Duration_Hours | Rating | Total_Rating_Contribution |
| :-------- | :----- | :------------- | :----- | :------------------------ |
| 101       | Python | 10             | 4.5    | 45                        |
| 102       | Python | 10             | 4.0    | 40                        |
| 103       | SQL    | 5              | 5.0    | 25                        |
| 104       | Python | 10             | 3.8    | 38                        |
| 105       | SQL    | 5              | 4.2    | 21                        |

여기서 `Total_Rating_Contribution`은 `Duration_Hours * Rating`으로 계산된 값입니다.

일반적인 평균(mean)은 각 수강생의 평점을 동등하게 취급하지만, 우리는 강좌의 길이를 가중치로 사용하여 긴 강좌의 평점이 더 많이 반영되도록 하고 싶습니다.

**Pandas 코드:**

```python
import pandas as pd

data = {
    'StudentID': [101, 102, 103, 104, 105],
    'Course': ['Python', 'Python', 'SQL', 'Python', 'SQL'],
    'Duration_Hours': [10, 10, 5, 10, 5],
    'Rating': [4.5, 4.0, 5.0, 3.8, 4.2]
}
df = pd.DataFrame(data)

# 'Total_Rating_Contribution' 컬럼을 추가합니다.
df['Total_Rating_Contribution'] = df['Duration_Hours'] * df['Rating']

# 강좌별 가중 평균 평점 계산
weighted_average_rating = df.groupby('Course').apply(
    lambda x: x['Total_Rating_Contribution'].sum() / x['Duration_Hours'].sum()
)

print(weighted_average_rating)
```

**결과:**

```
Course
Python    4.1
SQL       4.6
dtype: float64
```

**설명:**

1.  **`df.groupby('Course')`**: DataFrame을 'Course' (강좌) 컬럼을 기준으로 'Python' 그룹과 'SQL' 그룹으로 나눕니다.
2.  **`.apply(lambda x: ...)`**: 각 강좌 그룹 `x`에 대해 람다 함수를 적용합니다.
3.  **`x['Total_Rating_Contribution'].sum() / x['Duration_Hours'].sum()`**:
    *   'Python' 그룹의 경우: (45 + 40 + 38) / (10 + 10 + 10) = 123 / 30 = 4.1
    *   'SQL' 그룹의 경우: (25 + 21) / (5 + 5) = 46 / 10 = 4.6
    
이처럼 `groupby().apply()`를 사용하면, 각 그룹(`Course`) 내에서 `Rating`과 `Duration_Hours`를 사용하여 단순 산술 평균이 아닌, 강좌 길이를 고려한 **가중 평균 평점**이라는 사용자 정의 메트릭을 유연하게 계산할 수 있습니다. 슬라이드의 예시와 동일하게, 그룹 내에서 두 컬럼의 합계를 이용해 새로운 비율을 계산하는 방식입니다.

---

**참고:** 슬라이드 하단에 언급된 것처럼, 만약 계산하려는 메트릭이 `sum`, `mean`, `max`, `min` 등 Pandas 내장 집계 함수로 직접 표현 가능하다면, `apply()` 대신 `agg()`를 사용하는 것이 일반적으로 더 효율적이고 권장됩니다. 하지만 위 예시나 슬라이드의 가중 평균처럼 여러 컬럼을 복합적으로 사용하여 계산해야 하는 경우에는 `apply()`가 매우 강력하고 유연한 대안이 됩니다.

---

## Slide 28

핵심 개념은 Pandas DataFrame에서 `groupby()`와 `agg()`를 함께 사용하여 여러 집계 연산을 수행하고, 이 과정에서 내장 함수와 조건부 `lambda` 함수를 유연하게 혼합하는 방법입니다. 특히 그룹별로 다른 계산 로직을 적용할 때 `lambda`를 활용하는 방법과 그룹의 키(key)에 접근하는 올바른 방법을 설명합니다.

---

### Pandas `groupby().agg()`를 활용한 조건부 다중 집계

#### 1. `groupby().agg()`를 사용한 다중 집계
Pandas의 `groupby()`와 `agg()` 메서드를 조합하면 데이터를 특정 기준으로 그룹화한 후, 각 그룹에 대해 여러 가지 통계 및 집계 연산을 한 번의 호출로 수행할 수 있습니다. 각 집계 결과는 새로운 컬럼으로 생성됩니다.

**예시:**
당신이 운영하는 온라인 쇼핑몰에서 다음과 같은 판매 데이터가 있다고 가정해 봅시다:

| 고객명 | 상품명 | 수량 | 단가 | 총액 |
|---|---|---|---|---|
| John | 바나나 | 5 | 2 | 10 |
| Silvia | 오렌지 | 3 | 5 | 15 |
| Andrew | 바나나 | 4 | 3 | 12 |

이 쇼핑몰에서는 각 `상품명`별로 `총액`의 합계를 알고 싶을 뿐만 아니라, 특별 프로모션 대상 상품에 대해서는 `총액`의 절반을 '프로모션 예산'으로 책정하고 싶습니다.

#### 2. `agg()` 내에 내장 함수와 커스텀 람다 함수 혼합 사용
`agg()`는 파이썬/Pandas에서 기본 제공하는 집계 함수(예: `'sum'`, `'mean'`, `'max'`)를 문자열 형태로 사용할 수 있으며, 필요에 따라 복잡한 로직을 수행하는 사용자 정의 `lambda` 함수도 함께 사용할 수 있습니다.

*   **`total=('total', 'sum')`**: `total` 컬럼의 합계를 구하여 `total`이라는 새 컬럼으로 만듭니다. 이는 가장 일반적인 형태의 내장 함수 사용입니다.
*   **`fixed_total=('total', lambda x: ...)`**: `total` 컬럼에 대해 `lambda` 함수로 정의된 복잡한 계산을 수행하여 `fixed_total`이라는 새 컬럼으로 만듭니다. 여기서 `x`는 현재 그룹에 속하는 `total` 컬럼의 `Series` 데이터입니다.

#### 3. 람다 함수 내 조건부 로직 (`if-else`)
`lambda` 함수 내에서 `if-else` 조건을 사용하여 그룹별로 다른 계산을 적용할 수 있습니다. 이는 특정 그룹에만 특별한 규칙을 적용해야 할 때 매우 유용합니다.

**예시 설명:**
온라인 쇼핑몰 예시에서 '바나나'는 특별 프로모션 대상이므로 `총액`의 절반을 '프로모션 예산'으로 책정하고, 그 외 다른 상품들은 `총액` 전체를 '프로모션 예산'으로 간주하려 합니다.
이 로직은 다음과 같은 `lambda` 함수로 표현될 수 있습니다:
`lambda x: x.sum() / 2 if x.name == '바나나' else x.sum()`

*   `x.sum()`: 현재 그룹 (`바나나` 그룹 또는 `오렌지` 그룹)의 `total` 컬럼 값들을 합산합니다.
*   `x.name == '바나나'`: 현재 그룹의 이름(즉, 상품명)이 '바나나'인지 확인하는 조건입니다.
*   만약 `바나나` 그룹이라면 `x.sum() / 2` (총액의 절반)을 반환하고,
*   그렇지 않다면 `x.sum()` (총액 전체)을 반환합니다.

#### 4. 그룹 키(`group key`) 접근: `x.name` vs `x.index[0]`
람다 함수 내에서 현재 처리 중인 그룹의 키(여기서는 `상품명`)를 알아내기 위해 `x.name` 또는 `x.index[0]`을 사용할 수 있습니다.

*   **`x.name` (권장):** `x.name`은 현재 처리 중인 그룹의 키(예: '바나나', '오렌지')를 직접 반환합니다. 이는 `groupby()`의 결과에서 그룹의 이름을 가져오는 가장 표준적이고 견고한 방법입니다.
*   **`x.index[0]` (덜 견고):** `df.set_index('product')`와 같이 `groupby` 전에 특정 컬럼을 인덱스로 설정한 경우에, `x.index[0]`은 해당 그룹의 첫 번째 요소의 인덱스 값을 반환합니다. 이 방법은 DataFrame의 인덱스 구조에 의존하기 때문에, 만약 인덱스가 그룹 키와 다른 상황이 발생하면 의도치 않은 결과를 초래할 수 있어 **덜 견고한(less brittle)** 방법으로 간주됩니다.

**최종 코드 예시 (권장):**
```python
import pandas as pd

# 온라인 쇼핑몰 판매 데이터 생성
data = {
    'client': ['John', 'Silvia', 'Andrew'],
    'product': ['bananas', 'oranges', 'bananas'],
    'quantity': [5, 3, 4],
    'price': [2, 5, 3],
    'total': [10, 15, 12]
}
df = pd.DataFrame(data)

# 'product' 기준으로 그룹화하고, 'total'의 합계와 조건부 'fixed_total'을 계산
# x.name을 사용하여 그룹 키에 접근하는 것이 권장됩니다.
result = df.groupby('product').agg(
    total=('total', 'sum'),
    fixed_total=('total', lambda x: x.sum() / 2 if x.name == 'bananas' else x.sum())
)

print(result)
```

**결과:**
```
         total  fixed_total
product                    
bananas     22         11.0
oranges     15         15.0
```

이 예시를 통해 '바나나' 그룹의 `total`은 22, `fixed_total`은 11 (22의 절반)이 되었고, '오렌지' 그룹의 `total`은 15, `fixed_total`은 15 (조건에 해당하지 않아 전체 값)가 된 것을 확인할 수 있습니다.

---

## Slide 29

이 슬라이드는 데이터 분석에서 매우 중요한 '피벗팅(Pivoting)' 개념 중 'Wide' 형식과 'Long' 형식의 데이터 구조를 비교하고, 이들 간의 변환 방법을 설명합니다.

### 핵심 개념

1.  **데이터 형식 (Data Format):** 데이터를 테이블 형태로 표현하는 방식에는 크게 'Wide' 형식과 'Long' 형식이 있습니다.
    *   **Wide (와이드) 형식:**
        *   **특징:** 여러 관측치(observations)의 값이 여러 컬럼(columns)에 퍼져(spread across) 있는 형태입니다. 즉, 각 행(row)은 고유한 식별자를 가지고, 관련 측정값들이 별도의 컬럼으로 나열됩니다.
        *   **장점:** 사람의 눈으로 데이터를 한눈에 파악하기 쉽고, 특정 개체의 모든 속성을 빠르게 볼 수 있습니다. 엑셀 스프레드시트에서 흔히 볼 수 있는 형태입니다.
    *   **Long (롱) 형식:**
        *   **특징:** 각 행(row)이 하나의 고유한 관측치(observation)를 나타내며, 측정값과 그 측정값의 유형을 설명하는 '키 컬럼(key columns)'을 포함합니다. 즉, 와이드 형식의 여러 컬럼에 퍼져 있던 값들이 하나의 '값 컬럼'으로 모이고, 원래 컬럼의 이름들은 새로운 '변수명 컬럼'의 값으로 들어갑니다.
        *   **장점:** 통계 분석, 시각화(특히 `ggplot2`나 `seaborn` 같은 라이브러리 사용 시), 데이터베이스 저장(정규화된 형태), 그리고 특정 머신러닝 모델의 입력 데이터 형태로 더 적합합니다. 데이터의 유연성이 높아 새로운 유형의 측정값을 추가하기 용이합니다.

2.  **데이터 형식 변환 (Conversion):**
    *   **Wide → Long 변환:** 와이드 형식의 여러 컬럼에 있는 값들을 하나의 컬럼으로 모으고, 원래 컬럼 이름들을 새로운 '변수명' 컬럼의 값으로 만드는 과정입니다. 주로 `stack` 또는 `melt` 함수(Pandas 라이브러리 기준)를 사용합니다.
    *   **Long → Wide 변환:** 롱 형식의 '변수명' 컬럼에 있는 값들을 새로운 컬럼 이름으로 만들고, 해당하는 '값 컬럼'의 값을 채워 넣는 과정입니다. 주로 `unstack` 또는 `pivot` 함수(Pandas 라이브러리 기준)를 사용합니다.

### 구체적인 실생활 예시: 학생 성적 관리

한 고등학교의 학년별, 과목별 학생들의 성적을 관리하는 시나리오를 생각해봅시다.

#### 1. Wide 형식의 데이터: 학생별 과목 점수 스프레드시트

담당 선생님이 학기 말에 학생들의 성적을 입력하는 엑셀 파일이라고 상상해 보세요. 각 학생을 한 줄로 보고, 각 과목의 점수를 별도의 컬럼에 기록하는 것이 일반적일 것입니다.

| 학생 ID | 이름 | 학년 | 수학 점수 | 영어 점수 | 과학 점수 |
| :------ | :--- | :--- | :-------- | :-------- | :-------- |
| 1001    | 김철수 | 1    | 90        | 85        | 92        |
| 1002    | 이영희 | 1    | 78        | 95        | 88        |
| 1003    | 박지민 | 2    | 88        | 90        | 75        |

*   **여기서 'Wide' 형식인 이유:** '수학 점수', '영어 점수', '과학 점수'라는 세 개의 컬럼에 점수 값들이 퍼져 있습니다. 한 학생(`학생 ID`로 구분)에 대한 모든 정보(이름, 학년, 각 과목 점수)가 한 행에 모두 기록됩니다. 각 행은 고유한 학생을 나타냅니다.

#### 2. Long 형식의 데이터: 분석을 위한 데이터베이스 테이블

이제 이 데이터를 가지고 어떤 분석을 하고 싶다고 가정해 봅시다. 예를 들어, 모든 과목의 평균 점수를 구하거나, 특정 과목의 점수 분포를 시각화하거나, 학생별 과목 점수를 데이터베이스에 저장하여 다른 테이블과 연동하고 싶을 수 있습니다. 이때 'Long' 형식이 훨씬 유용합니다.

와이드 형식의 데이터를 롱 형식으로 변환(`stack`/`melt` 수행)하면 다음과 같습니다:

| 학생 ID | 이름 | 학년 | 과목 | 점수 |
| :------ | :--- | :--- | :--- | :--- |
| 1001    | 김철수 | 1    | 수학 | 90   |
| 1001    | 김철수 | 1    | 영어 | 85   |
| 1001    | 김철수 | 1    | 과학 | 92   |
| 1002    | 이영희 | 1    | 수학 | 78   |
| 1002    | 이영희 | 1    | 영어 | 95   |
| 1002    | 이영희 | 1    | 과학 | 88   |
| 1003    | 박지민 | 2    | 수학 | 88   |
| 1003    | 박지민 | 2    | 영어 | 90   |
| 1003    | 박지민 | 2    | 과학 | 75   |

*   **여기서 'Long' 형식인 이유:** '수학 점수', '영어 점수', '과학 점수' 컬럼이 사라지고, 이 컬럼들의 이름이었던 '수학', '영어', '과학'이 '과목'이라는 새로운 컬럼의 값으로 들어갔습니다. 그리고 원래 각 과목에 해당하는 점수들은 모두 '점수'라는 하나의 컬럼에 모였습니다.
*   **관측치(Observation):** 이제 각 행은 '한 학생의 한 과목 점수'라는 하나의 독립적인 관측치를 나타냅니다. 예를 들어, `(1001, 김철수, 1, 수학, 90)`은 '김철수 학생의 수학 점수'라는 하나의 관측치입니다. '학생 ID'와 '과목'이 결합되어 각 행의 고유성을 정의하는 '키 컬럼'이 됩니다.

#### 왜 변환할까요?

*   **Wide → Long (예: `melt`)**:
    *   **분석 용이성:** '수학', '영어', '과학' 각 과목에 대해 일일이 통계를 내는 대신, '과목' 컬럼을 기준으로 그룹화하여 전체 평균 점수, 과목별 평균 점수, 학년별 과목 평균 점수 등을 훨씬 쉽게 계산할 수 있습니다.
    *   **시각화:** 예를 들어, `matplotlib`이나 `seaborn`으로 과목별 점수 분포를 상자 그림(boxplot)으로 그리고 싶다면, '과목' 컬럼을 x축으로, '점수' 컬럼을 y축으로 사용하면 쉽게 그릴 수 있습니다. 와이드 형식에서는 각 과목 컬럼마다 그래프를 따로 그려야 할 수도 있습니다.
    *   **확장성:** 만약 '미술 점수'를 추가해야 한다면, 와이드 형식에서는 새로운 '미술 점수' 컬럼을 추가해야 하지만, 롱 형식에서는 단순히 기존 데이터에 '미술' 과목의 점수 행들을 추가하기만 하면 됩니다.

*   **Long → Wide (예: `pivot`/`unstack`)**:
    *   **보고서 생성:** 최종적으로 학생별 성적표를 만들 때, 각 학생의 모든 과목 점수가 한 줄에 나열된 와이드 형식이 사람들에게 더 익숙하고 보기 편한 보고서 형태일 수 있습니다.
    *   **특정 비교:** 예를 들어, '수학 점수'와 '영어 점수'를 직접적으로 나란히 놓고 비교하거나 연산해야 할 때 와이드 형식이 편리합니다.

이처럼 Wide 형식과 Long 형식은 데이터를 다루는 목적에 따라 서로 변환하며 사용되며, 데이터 분석가에게 매우 중요한 기본적인 데이터 처리 기술입니다.

---

## Slide 30

첨부된 슬라이드는 Pandas DataFrame에서 `pivot()` 메서드를 사용하여 데이터를 'long' 형식에서 'wide' 형식으로 재구성하는 방법을 설명하고 있습니다.

### 핵심 개념: `pivot()` 메서드를 이용한 데이터 Long To Wide 변환

`pivot()` 메서드는 데이터프레임의 특정 열들을 새로운 인덱스(행)와 컬럼(열)으로 사용하여 데이터를 재배열하고, 다른 열의 값을 채워 넣는 기능입니다.

1.  **Long 형식 데이터**: 각 관측치(예: 개별 거래, 학생의 개별 과목 점수)가 여러 행에 걸쳐 기록되어 있는 형태입니다. 동일한 엔티티(고객, 학생)에 대한 정보가 여러 행에 분산되어 있습니다.
2.  **Wide 형식 데이터**: 각 행이 특정 엔티티(예: 고객, 학생)를 나타내고, 그 엔티티에 대한 여러 속성(예: 제품 종류, 과목 점수)이 각각 독립적인 열로 펼쳐져 있는 형태입니다. 이 형식은 특정 엔티티의 모든 정보를 한 눈에 파악하기 용이합니다.

`df.pivot()` 함수는 다음과 같은 주요 인자를 사용합니다:

*   `index`: 새로운 데이터프레임의 행 인덱스가 될 원래 데이터프레임의 열 이름 (예: `client`).
*   `columns`: 새로운 데이터프레임의 열 이름이 될 원래 데이터프레임의 열 이름입니다. 이 열의 고유한 값들이 새로운 열을 생성합니다 (예: `product`).
*   `values`: 새로운 데이터프레임의 셀을 채울 값들을 담고 있는 원래 데이터프레임의 열 이름입니다 (예: `quantity`).

**주의할 점:** `pivot()` 메서드는 `(index, columns)` 쌍별로 반드시 **하나의 고유한 값**만 존재해야 합니다. 만약 동일한 `index`와 `columns` 조합에 해당하는 `values`가 여러 개라면(예: 한 고객이 같은 제품을 여러 번 구매하여 여러 수량 기록이 있는 경우), `ValueError`를 발생시킵니다. 이런 경우 데이터 집계(aggregation)가 필요한 `pivot_table()` 메서드를 사용하는 것이 더 적합합니다.

### 구체적이고 실생활에 가까운 예시: 학생별 과목 성적표 만들기

**시나리오:** 한 학급 학생들의 과목별 점수가 아래와 같이 'Long' 형식으로 기록되어 있습니다. 우리는 각 학생의 모든 과목 점수를 한 줄에 볼 수 있는 'Wide' 형식의 성적표로 만들고 싶습니다.

**1. Long 형식 데이터:**

| 학생 이름 | 과목    | 점수 |
| :-------- | :------ | :--- |
| 김철수    | 수학    | 90   |
| 김철수    | 영어    | 85   |
| 이영희    | 수학    | 78   |
| 이영희    | 영어    | 92   |
| 박민수    | 수학    | 88   |
| 박민수    | 영어    | 75   |

**2. `pivot()` 함수 적용:**

위 데이터프레임이 `grades_df`라고 가정했을 때, 다음 코드를 사용하여 데이터를 변환할 수 있습니다.

```python
import pandas as pd

data = {
    '학생 이름': ['김철수', '김철수', '이영희', '이영희', '박민수', '박민수'],
    '과목': ['수학', '영어', '수학', '영어', '수학', '영어'],
    '점수': [90, 85, 78, 92, 88, 75]
}
grades_df = pd.DataFrame(data)

# pivot() 메서드 적용
# index='학생 이름': 학생 이름이 새로운 행 인덱스가 됩니다.
# columns='과목': 과목(수학, 영어)이 새로운 열 이름이 됩니다.
# values='점수': 각 학생의 과목별 점수가 셀을 채웁니다.
pivoted_grades = grades_df.pivot(index='학생 이름', columns='과목', values='점수')

print(pivoted_grades)
```

**3. Wide 형식 결과:**

```
과목     수학  영어
학생 이름       
김철수    90  85
이영희    78  92
박민수    88  75
```

이 예시에서, 각 학생(`index='학생 이름'`)은 한 행에 위치하고, 각 과목(`columns='과목'`)은 독립적인 열로 펼쳐져 있습니다. 해당 학생의 과목별 점수(`values='점수'`)가 각 셀을 채우고 있어, 각 학생의 모든 과목 점수를 한 눈에 파악하기 훨씬 쉬워집니다. 이는 각 학생이 특정 과목에 대해 하나의 점수만을 가지므로 `pivot()`의 "단일 값" 제약 조건을 만족합니다.

---

## Slide 31

## 핵심 개념: Pandas `stack()`을 이용한 데이터 재구조화 (Wide to Long)

제공된 슬라이드는 Pandas 라이브러리의 `stack()` 메서드를 활용하여 데이터를 '넓은(wide)' 형식에서 '긴(long)' 형식으로 변환하는 방법을 설명합니다. 이는 데이터 분석 및 시각화에 있어 데이터를 더 효율적으로 다룰 수 있게 해주는 중요한 데이터 재구조화(reshaping) 기법입니다.

### 1. `df.stack()`의 역할: 열(Columns)을 새로운 인덱스 레벨로 이동

*   **Wide 형식 데이터**: 슬라이드의 왼쪽 `df` DataFrame처럼, 각 열(column)이 특정 범주나 측정값을 나타내는 형태입니다. 여기서는 `client`가 인덱스이고 `bananas`, `oranges`가 각각의 독립된 열로 존재하며, 그 값은 해당 클라이언트의 제품별 수량을 나타냅니다. 이 형식은 특정 클라이언트의 제품별 구매량을 빠르게 파악하는 데 유용할 수 있습니다.
*   **`df.stack()` 작동 방식**: `stack()` 메서드는 DataFrame의 **열 이름** (여기서는 'bananas', 'oranges')을 가져와서 **새로운 인덱스 레벨**로 이동시킵니다. 이 변환의 결과로 `pd.Series` 객체가 반환되며, 원래의 인덱스(`client`)와 새로 추가된 인덱스 레벨(`product` 또는 원래의 열 이름)으로 구성된 `MultiIndex` (다중 인덱스)를 가집니다. 각 값은 원래 DataFrame의 해당 셀에 있던 데이터(예: 5, 3, 4, 2)가 됩니다.
    *   **예시**: `df.stack()`을 적용하면 `John`의 'bananas' 수량 5는 `(John, bananas)` 인덱스에 매핑되고, `Silvia`의 'oranges' 수량 2는 `(Silvia, oranges)` 인덱스에 매핑되는 식입니다.

### 2. `s.reset_index(name='...')`를 통한 Tidy DataFrame 복원

*   `df.stack()`의 직접적인 결과물은 `MultiIndex`를 가진 `Series` 객체입니다. 대부분의 데이터 분석 작업에서는 `DataFrame` 형태가 더 편리하므로, `reset_index()` 메서드를 사용하여 이를 다시 `DataFrame`으로 변환합니다.
*   **`reset_index()` 작동 방식**: `reset_index()`는 `Series`의 `MultiIndex`를 일반적인 열(column)으로 변환하고, 새로운 기본 숫자 인덱스를 생성하여 `DataFrame`을 반환합니다.
*   **`name` 파라미터**: `name='quantity'`와 같이 `name` 파라미터를 지정하면, `stack()` 과정에서 `Series`의 **값**으로 들어갔던 데이터(여기서는 바나나와 오렌지의 수량)에 새로운 열 이름(`quantity`)을 부여할 수 있습니다. 슬라이드의 최종 결과처럼 `client`, `product`, `quantity`라는 세 개의 열을 가진 깔끔한(tidy) `DataFrame`을 얻게 됩니다.

---

### 실생활 예시: 학교 시험 점수 데이터 관리

당신이 한 학급의 학생들 시험 점수를 관리하는 선생님이라고 가정해 봅시다. 각 학생이 과목별로 받은 점수를 기록한 데이터가 있습니다.

**초기 (Wide) 데이터: `exam_scores_df`**
(각 학생의 과목별 점수를 열로 표현)

| student_id | Math | Science | History |
|:-----------|:-----|:--------|:--------|
| 김철수     | 90   | 85      | 78      |
| 이영희     | 75   | 92      | 88      |
| 박지민     | 88   | 79      | 95      |

이 데이터는 '김철수가 수학에서 90점을 받았다'는 것을 쉽게 알 수 있지만, '모든 학생의 과학 과목 평균 점수'를 구하거나 '가장 점수가 낮은 과목'을 찾기 위해서는 각 과목 열을 개별적으로 처리해야 하거나 복잡한 코드가 필요할 수 있습니다.

**1. `stack()` 적용: 데이터의 '긴' 형식 변환**

`stacked_scores = exam_scores_df.stack()`

`stack()` 메서드를 적용하면 `Math`, `Science`, `History`라는 과목 이름들이 `student_id`와 함께 새로운 인덱스 레벨로 이동하여 `MultiIndex`를 가진 `Series`가 됩니다.

```
student_id  subject
김철수       Math        90
            Science     85
            History     78
이영희       Math        75
            Science     92
            History     88
박지민       Math        88
            Science     79
            History     95
dtype: int64
```
이제 각 데이터 포인트가 `(학생 ID, 과목)`이라는 고유한 조합으로 표현되며, 그 값은 해당 과목의 점수가 됩니다.

**2. `reset_index()` 적용: Tidy DataFrame으로 복원**

`tidy_scores_df = stacked_scores.reset_index(name='score')`

`reset_index()`를 사용하여 `MultiIndex` (즉, `student_id`와 `subject`)를 일반 열로 변환하고, Series의 값(점수)에 `score`라는 열 이름을 부여합니다.

| student_id | subject | score |
|:-----------|:--------|:------|
| 김철수       | Math    | 90    |
| 김철수       | Science | 85    |
| 김철수       | History | 78    |
| 이영희       | Math    | 75    |
| 이영희       | Science | 92    |
| 이영희       | History | 88    |
| 박지민       | Math    | 88    |
| 박지민       | Science | 79    |
| 박지민       | History | 95    |

**왜 이렇게 변환하는가? (핵심 이점)**

이제 이 '긴' 형식의 `tidy_scores_df`를 사용하면 다음과 같은 분석이 훨씬 쉬워집니다:

*   **과목별 평균 점수 계산**: `tidy_scores_df.groupby('subject')['score'].mean()`와 같이 단 한 줄의 코드로 쉽게 계산할 수 있습니다.
*   **특정 학생의 점수 필터링**: `tidy_scores_df[tidy_scores_df['student_id'] == '이영희']`
*   **점수가 80점 미만인 경우 찾기**: `tidy_scores_df[tidy_scores_df['score'] < 80]`
*   **데이터 추가의 유연성**: 새로운 과목(예: `English`)이 추가되어도 새로운 열을 추가하는 대신 단순히 새 과목에 대한 점수 행만 추가하면 됩니다. 이는 데이터베이스나 다른 데이터 처리 시스템과 통합할 때 더 유연하고 자연스러운 형태입니다.

결론적으로, `stack()`과 `reset_index()` 조합은 데이터를 분석 및 시각화하기에 더 적합한 'tidy' 또는 '긴' 형태로 변환하여 데이터 처리의 효율성과 유연성을 크게 높여줍니다.

---

## Slide 32

슬라이드의 핵심 개념은 `pandas.DataFrame.melt` 함수를 사용하여 데이터를 **'넓은(wide)' 형식에서 '긴(long)' 형식으로 변환(unpivot 또는 melt)하는 방법**입니다.

### 핵심 개념: `melt` 함수를 이용한 데이터 형식 변환 (Wide -> Long)

데이터 분석이나 시각화를 하다 보면 데이터의 형태를 바꾸어야 할 때가 많습니다. 특히, 여러 개의 컬럼에 분산되어 있는 값들을 하나의 컬럼으로 모으고, 원래 컬럼의 이름을 담는 새로운 컬럼을 만들고 싶을 때 `melt` 함수가 유용합니다.

**1. '넓은(Wide)' 형식 데이터:**
*   각 고유한 측정 항목이나 범주가 별도의 컬럼으로 나열된 형태입니다.
*   예시: 슬라이드의 `df` 또는 `df1`처럼, 'bananas'와 'oranges'가 각각 독립적인 컬럼으로 존재하여 각 클라이언트의 수량을 표시하는 형태.

**2. '긴(Long)' 형식 데이터:**
*   각 고유한 측정 항목이나 범주가 하나의 컬럼 값으로 통합되고, 해당 값(value)은 또 다른 하나의 컬럼에 모여 있는 형태입니다.
*   예시: 슬라이드의 최종 결과처럼, 'product' 컬럼에 'bananas'와 'oranges'가 모두 들어가고, 그에 해당하는 수량은 'quantity' 컬럼에 모여 있는 형태.

**`melt` 함수 사용 시 주요 인자:**

*   `id_vars`: '고정할' 또는 '식별자로 유지할' 컬럼(들)을 지정합니다. 이 컬럼들은 '녹여지지(melt되지)' 않고 그대로 유지됩니다. (슬라이드 예시에서는 `'client'`)
*   `value_vars`: '녹일' 대상이 되는, 즉 새로운 행으로 변환될 값들이 있는 컬럼(들)을 지정합니다. (슬라이드 예시에서는 `['bananas', 'oranges']`)
*   `var_name`: `value_vars`에 지정된 원래 컬럼 이름들(예: 'bananas', 'oranges')이 들어갈 새로운 컬럼의 이름을 지정합니다. (슬라이드 예시에서는 결과에 'product'로 표시됨)
*   `value_name`: `value_vars`에 해당하는 실제 값들(예: 수량 5, 3, 4, 2)이 들어갈 새로운 컬럼의 이름을 지정합니다. (슬라이드 예시에서는 `'quantity'`)

**`reset_index()`의 역할:**
슬라이드에서 `df.reset_index()`를 먼저 수행한 것을 볼 수 있습니다. 이는 초기 `df`에서 'client'가 DataFrame의 인덱스였기 때문입니다. `melt` 함수는 기본적으로 컬럼을 대상으로 작동하므로, 인덱스를 `id_vars`로 사용하려면 먼저 `reset_index()`를 통해 인덱스를 일반 컬럼으로 만들어주어야 합니다.

### 구체적이고 실생활에 가까운 예시: 시험 점수 데이터 관리

당신이 한 학급의 담임 선생님이라고 가정해봅시다. 학생들의 세 과목(국어, 영어, 수학) 시험 점수를 다음과 같이 기록하고 있습니다.

**1. 초기 데이터 (넓은 형식):**
학생 이름이 인덱스로 설정되어 있고, 각 과목의 점수가 별도의 컬럼으로 되어 있는 형태입니다.

```python
import pandas as pd

# 초기 데이터 (넓은 형식)
data = {
    '국어': [85, 90, 78],
    '영어': [90, 88, 92],
    '수학': [75, 82, 80]
}
df_scores = pd.DataFrame(data, index=['김철수', '이영희', '박민지'])
print("--- 초기 데이터 (df_scores) ---")
print(df_scores)
"""
          국어  영어  수학
김철수     85  90  75
이영희     90  88  82
박민지     78  92  80
"""
```

**문제점:** 이 형태로 데이터를 분석하려고 하면 불편할 때가 많습니다. 예를 들어, 모든 학생의 모든 과목 점수를 한꺼번에 시각화하거나, 특정 과목의 평균 점수를 쉽게 구하고 싶을 때, 각 과목 컬럼을 일일이 지정해야 합니다. 데이터베이스에 저장할 때도 보통 이보다는 '긴' 형태를 선호합니다.

**2. 인덱스 리셋:**
`melt` 함수를 사용하기 전에 인덱스(`학생 이름`)를 일반 컬럼으로 만들어줍니다.

```python
df_scores_reset = df_scores.reset_index()
df_scores_reset.rename(columns={'index': '학생이름'}, inplace=True) # 컬럼 이름 변경
print("\n--- 인덱스 리셋 후 (df_scores_reset) ---")
print(df_scores_reset)
"""
  학생이름  국어  영어  수학
0  김철수  85  90  75
1  이영희  90  88  82
2  박민지  78  92  80
"""
```

**3. `melt` 함수 적용 (긴 형식으로 변환):**
이제 이 데이터를 '긴' 형식으로 변환하여, 각 행이 '어떤 학생'이 '어떤 과목'에서 '몇 점'을 받았는지를 나타내도록 합니다.

*   `id_vars='학생이름'`: '학생이름' 컬럼은 그대로 유지합니다.
*   `value_vars=['국어', '영어', '수학']`: 점수가 들어있는 '국어', '영어', '수학' 컬럼을 녹입니다.
*   `var_name='과목'`: 원래 컬럼 이름인 '국어', '영어', '수학'이 들어갈 새로운 컬럼의 이름을 '과목'으로 지정합니다.
*   `value_name='점수'`: 각 과목의 실제 점수(85, 90 등)가 들어갈 새로운 컬럼의 이름을 '점수'로 지정합니다.

```python
df_long_scores = df_scores_reset.melt(
    id_vars='학생이름',
    value_vars=['국어', '영어', '수학'],
    var_name='과목',
    value_name='점수'
)
print("\n--- melt 적용 후 (df_long_scores) ---")
print(df_long_scores)
"""
  학생이름  과목  점수
0  김철수  국어  85
1  이영희  국어  90
2  박민지  국어  78
3  김철수  영어  90
4  이영희  영어  88
5  박민지  영어  92
6  김철수  수학  75
7  이영희  수학  82
8  박민지  수학  80
"""
```

**결과를 통한 이해:**
이제 데이터는 훨씬 더 분석하기 쉬운 '긴' 형식이 되었습니다.

*   **데이터 분석 용이성:** 예를 들어, 과목별 평균 점수를 구하려면 `df_long_scores.groupby('과목')['점수'].mean()`와 같이 단 한 줄로 쉽게 계산할 수 있습니다.
*   **시각화 용이성:** Matplotlib이나 Seaborn 같은 라이브러리로 점수를 시각화할 때, `x='과목'`, `y='점수'`, `hue='학생이름'` 등으로 지정하여 다양한 그래프를 쉽게 그릴 수 있습니다.
*   **데이터베이스 친화적:** 대부분의 관계형 데이터베이스는 이처럼 '긴' 형태의 데이터를 저장하는 것을 선호합니다.

이처럼 `melt` 함수는 데이터를 구조적으로 재구성하여 특정 유형의 분석이나 처리에 더 적합한 형태로 만들어주는 강력한 도구입니다. 슬라이드 하단의 'Choose melt when you want explicit control over id/value columns.'라는 문구처럼, 어떤 컬럼을 고정하고(id_vars), 어떤 컬럼을 녹여서(value_vars) 새로운 컬럼 이름(var_name)과 값(value_name)으로 만들지 명확하게 제어하고 싶을 때 `melt`를 선택하면 됩니다.

---

## Slide 33

### 핵심 개념: 관계형 대수(Relational Algebra)의 '나눗셈(Division)' 연산

관계형 대수의 '나눗셈(Division)' 연산 ($R \div S$)은 특정 조건(S 집합의 모든 원소)을 *모두* 만족하는 엔티티(R 집합의 첫 번째 속성)를 찾는 데 사용됩니다. 슬라이드에서는 `R(Name, Year)`와 `S(Year)`가 주어졌을 때, $R \div S$는 `S`에 있는 *모든* `Year`에 등장하는 `Name`들을 반환합니다. 즉, "`S`의 모든 연도에 나타난 `Name`은 무엇인가?"라는 질문에 답하는 것입니다.

---

### 실생활 예시: 필수 과목을 모두 수강한 학생 찾기

이 개념을 완벽하게 이해하기 위해 대학교 시나리오를 생각해 봅시다.

**시나리오:** 특정 학과의 졸업 요건에 해당하는 **필수 과목들을 모두 수강한 학생**을 찾고 싶습니다.

1.  **테이블 정의:**
    *   **R (수강 기록 테이블 - `StudentEnrollment`)**: 어떤 학생이 어떤 과목을 수강했는지 기록합니다.
        *   속성: `Student_ID` (학생 고유 번호), `Course_ID` (과목 고유 번호)
        *   예시 데이터:
            | Student_ID | Course_ID |
            | :--------- | :-------- |
            | Alice      | CS101     |
            | Alice      | CS102     |
            | Alice      | CS103     |
            | Bob        | CS101     |
            | Bob        | CS102     |
            | Carol      | CS101     |
            | David      | CS101     |
            | David      | CS102     |
            | David      | CS103     |
            | David      | CS104     |

    *   **S (필수 과목 테이블 - `RequiredCourses`)**: 학과에서 지정한 필수 과목 목록입니다.
        *   속성: `Course_ID`
        *   예시 데이터:
            | Course_ID |
            | :-------- |
            | CS101     |
            | CS102     |
            | CS103     |

2.  **질문:** `RequiredCourses`에 있는 *모든* 과목(CS101, CS102, CS103)을 수강한 `Student_ID`는 누구인가요? 이것이 바로 $R \div S$의 결과가 됩니다.

3.  **결과 도출 과정:**

    *   **Alice:** CS101, CS102, CS103을 수강했습니다. `RequiredCourses`의 모든 과목을 수강했으므로 결과에 포함됩니다.
    *   **Bob:** CS101, CS102만 수강했습니다. CS103을 수강하지 않았으므로 `RequiredCourses`의 모든 과목을 수강하지 못했습니다. 결과에 포함되지 않습니다.
    *   **Carol:** CS101만 수강했습니다. CS102, CS103을 수강하지 않았으므로 결과에 포함되지 않습니다.
    *   **David:** CS101, CS102, CS103, CS104를 수강했습니다. 비록 필수 과목 외에 다른 과목(CS104)도 들었지만, `RequiredCourses`의 모든 과목(CS101, CS102, CS103)을 *모두* 수강했으므로 결과에 포함됩니다.

    따라서, $R \div S = \{Alice, David\}$ 가 됩니다.

---

### Pandas 코드 (count-within-S pattern)로 구현 원리 이해

슬라이드의 Pandas 코드는 위와 같은 "모든 조건을 만족하는 엔티티 찾기" 과정을 효율적으로 구현합니다.

```python
import pandas as pd

# R 테이블 (StudentEnrollment)
R = pd.DataFrame({
    "Student_ID": ["Alice", "Alice", "Alice", "Bob", "Bob", "Carol", "David", "David", "David", "David"],
    "Course_ID": ["CS101", "CS102", "CS103", "CS101", "CS102", "CS101", "CS101", "CS102", "CS103", "CS104"]
}).drop_duplicates()

# S 테이블 (RequiredCourses)
S = pd.DataFrame({"Course_ID": ["CS101", "CS102", "CS103"]})

# 1. 'need' 변수 계산: S 테이블의 고유한 Course_ID 개수
#    -> 필수 과목의 총 개수를 저장합니다. (여기서는 3개)
need = S["Course_ID"].nunique()
# need = 3

# 2. R과 S를 'Course_ID' 기준으로 병합(merge):
#    -> R의 수강 기록 중, S에 있는 필수 과목에 해당하는 기록만 남깁니다.
#       즉, 필수 과목이 아닌 과목 수강 기록은 이 단계에서 제외됩니다.
merged_df = R.merge(S, on="Course_ID")
# merged_df 결과 (필수 과목 수강 기록만):
#   Student_ID Course_ID
# 0      Alice     CS101
# 1      Alice     CS102
# 2      Alice     CS103
# 3        Bob     CS101
# 4        Bob     CS102
# 5      Carol     CS101
# 6      David     CS101
# 7      David     CS102
# 8      David     CS103

# 3. 'Student_ID'별로 그룹화하여, 필수 과목 중 몇 개를 수강했는지 세기:
#    -> 각 학생이 merged_df (즉, 필수 과목만 포함된 기록)에서 몇 개의 고유한 과목을 수강했는지 계산합니다.
grouped_counts = merged_df.groupby("Student_ID")["Course_ID"].nunique().reset_index(name="cnt")
# grouped_counts 결과:
#   Student_ID  cnt
# 0      Alice    3
# 1        Bob    2
# 2      Carol    1
# 3      David    3

# 4. 'cnt'가 'need'와 같은 학생만 필터링:
#    -> 각 학생이 수강한 필수 과목의 개수('cnt')가 전체 필수 과목 개수('need')와 정확히 일치하는 학생만 선택합니다.
div_result = grouped_counts.query("cnt == @need")["Student_ID"]

# 최종 결과:
# 0    Alice
# 3    David
# Name: Student_ID, dtype: object
```

**동작 원리 요약:**

1.  **필요한 조건 개수 파악 (`need`):** `S` 테이블에 있는 고유한 `Year` (예시에서는 `Course_ID`)의 총 개수를 미리 세어둡니다. 이 개수가 우리가 "모두" 만족해야 할 기준이 됩니다.
2.  **관련 데이터만 필터링 (`R.merge(S)`):** `R` 테이블에서 `S` 테이블에 있는 `Year` (또는 `Course_ID`)와 일치하는 기록만 남깁니다. 이 과정은 `R`의 모든 기록을 보는 것이 아니라, 우리가 "모두"라는 조건을 검사할 대상인 `S`의 `Year`에 해당하는 기록만 고려하겠다는 의미입니다.
3.  **엔티티별 조건 만족 개수 세기 (`groupby().nunique()`):** 필터링된 결과에서 `Name` (또는 `Student_ID`)별로 그룹화하여, `S`에 속하는 `Year` (또는 `Course_ID`)를 몇 개나 가지고 있는지(즉, 몇 개의 조건을 만족했는지) 개수를 셉니다.
4.  **최종 필터링 (`query()`):** 개수를 센 결과가 `need` (총 만족해야 할 조건 개수)와 정확히 일치하는 `Name` (또는 `Student_ID`)만 선택합니다. 이렇게 하면 `S`의 *모든* `Year`에 등장하는 `Name`만 얻게 됩니다.

이 과정을 통해 우리는 "모든 (for all)"이라는 조건을 데이터베이스 연산으로 정확하게 구현할 수 있습니다.

---

## Slide 34

핵심 개념은 데이터를 특정 기준(행과 열)에 따라 재구성하고, 각 기준에 해당하는 데이터를 특정 함수로 집계(요약)하여 보여주는 **피벗(Pivot) 또는 교차표(Cross-Tab)** 입니다.

---

### **핵심 개념: 피벗 (Pivot) / 교차표 (Cross-Tab)**

피벗 또는 교차표는 대량의 원본 데이터를 특정 기준에 따라 **행(rows)** 과 **열(columns)** 로 재구성하고, 각 행과 열이 교차하는 지점의 데이터에 대해 **집계 함수(aggregation function)** 를 적용하여 요약된 통계를 제공하는 강력한 데이터 분석 도구입니다.

**주요 구성 요소:**

1.  **행 (Index):** 새롭게 구성될 테이블의 행 레이블이 될 원본 데이터의 열(Column)을 지정합니다.
2.  **열 (Columns):** 새롭게 구성될 테이블의 열 레이블이 될 원본 데이터의 열(Column)을 지정합니다.
3.  **값 (Values):** 각 행과 열의 교차점에서 집계할 실제 데이터가 있는 원본 데이터의 열(Column)을 지정합니다. (선택 사항, 지정하지 않으면 기본적으로 빈도(count)를 계산합니다.)
4.  **집계 함수 (Aggregation Function):** 각 교차점에서 데이터를 어떻게 요약할지 정의합니다. 예를 들어, `sum` (합계), `mean` (평균), `count` (개수), `min` (최소), `max` (최대) 등이 있습니다.

**Pandas에서의 구현:**

*   `pd.crosstab`: 주로 두 개 이상의 범주형 변수의 **빈도(Frequency)** 를 계산하여 교차표를 만들 때 사용됩니다. 각 교차점의 기본값은 개수(count)입니다.
*   `df.pivot_table`: `DataFrame` 객체의 메서드로, 보다 일반적인 피벗팅을 가능하게 합니다. `values` 인자를 통해 어떤 열의 값을 집계할지, `aggfunc` 인자를 통해 어떤 집계 함수를 사용할지 명시적으로 지정할 수 있습니다. `fill_value`, `margins` 등 다양한 옵션을 제공하여 유연하게 사용할 수 있습니다.

---

### **실생활 예시: 온라인 쇼핑몰 판매 데이터 분석**

당신이 온라인 쇼핑몰의 데이터 분석가라고 가정해 봅시다. 당신에게는 다음과 같은 `sales` 데이터프레임이 있습니다.

| OrderID | Region | Product_Category | Sale_Amount | Quantity |
| :------ | :----- | :--------------- | :---------- | :------- |
| 1001    | North  | Electronics      | 500         | 1        |
| 1002    | South  | Clothing         | 120         | 2        |
| 1003    | North  | Books            | 30          | 1        |
| 1004    | East   | Electronics      | 750         | 1        |
| 1005    | North  | Clothing         | 80          | 1        |
| 1006    | South  | Electronics      | 200         | 1        |
| ...     | ...    | ...              | ...         | ...      |

이 데이터를 가지고 다음과 같은 질문에 답하고 싶을 때 피벗/교차표가 유용합니다.

---

#### **예시 1: 각 지역별, 제품 카테고리별 주문 건수 ( `pd.crosstab` 활용)**

*   **질문:** 각 지역에서 어떤 제품 카테고리의 주문이 얼마나 발생했을까요?
*   **목표:** 'Region'을 행으로, 'Product_Category'를 열로 하고, 각 교차점에 해당하는 주문 건수(빈도)를 알고 싶습니다.

**Pandas 코드:**
```python
import pandas as pd

# 예시 데이터프레임 생성
data = {
    'OrderID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    'Region': ['North', 'South', 'North', 'East', 'North', 'South', 'East', 'West', 'North', 'South'],
    'Product_Category': ['Electronics', 'Clothing', 'Books', 'Electronics', 'Clothing', 'Electronics', 'Books', 'Electronics', 'Electronics', 'Clothing'],
    'Sale_Amount': [500, 120, 30, 750, 80, 200, 45, 600, 400, 150],
    'Quantity': [1, 2, 1, 1, 1, 1, 1, 1, 1, 2]
}
sales_df = pd.DataFrame(data)

# pd.crosstab 사용
order_counts_by_region_category = pd.crosstab(index=sales_df["Region"], columns=sales_df["Product_Category"])
print("--- 각 지역별, 제품 카테고리별 주문 건수 (pd.crosstab) ---")
print(order_counts_by_region_category)
```

**결과 (예상):**

```
Product_Category  Books  Clothing  Electronics
Region                                      
East                  1         0            1
North                 1         1            2
South                 0         2            1
West                  0         0            1
```

**해석:** 이 표를 통해 'North' 지역에서는 'Electronics' 주문이 2건, 'Clothing' 주문이 1건, 'Books' 주문이 1건 발생했음을 한눈에 알 수 있습니다. 'East' 지역에서는 'Clothing' 주문이 없었네요.

---

#### **예시 2: 각 지역별, 제품 카테고리별 총 판매액 ( `df.pivot_table` 활용)**

*   **질문:** 각 지역에서 어떤 제품 카테고리가 총 얼마의 판매액을 기록했을까요? 전체 총합도 함께 보고 싶습니다.
*   **목표:** 'Region'을 행으로, 'Product_Category'를 열로 하고, 'Sale_Amount'를 'sum' (합계)하여 각 교차점에 배치합니다. 판매가 없는 경우는 0으로 표시하고, 전체 행/열의 총합을 추가합니다.

**Pandas 코드:**
```python
# df.pivot_table 사용
total_sales_by_region_category = sales_df.pivot_table(
    index="Region",             # 행 (rows)
    columns="Product_Category", # 열 (columns)
    values="Sale_Amount",       # 집계할 값 (values)
    aggfunc="sum",              # 집계 함수 (aggregation function)
    fill_value=0,               # 값이 없는 경우 0으로 채움
    margins=True                # 행과 열의 총합 추가
)
print("\n--- 각 지역별, 제품 카테고리별 총 판매액 (df.pivot_table) ---")
print(total_sales_by_region_category)
```

**결과 (예상):**

```
Product_Category  Books  Clothing  Electronics    All
Region                                             
East                 45         0          750    795
North                30        80         900   1010
South                 0       270          200    470
West                  0         0          600    600
All                  75       350         2450   2875
```

**해석:** 이 표는 훨씬 더 많은 정보를 제공합니다.
*   'North' 지역의 총 판매액은 $1010이며, 그 중 'Electronics'가 $900를 차지합니다.
*   'South' 지역에서는 'Clothing' 판매액($270)이 'Electronics'($200)보다 높습니다.
*   가장 오른쪽의 'All' 열은 각 지역의 총 판매액을 보여줍니다.
*   가장 아래쪽의 'All' 행은 각 제품 카테고리의 전체 판매액을 보여줍니다. 예를 들어, 전체 'Electronics' 판매액은 $2450입니다.
*   오른쪽 하단의 'All' 셀($2875)은 전체 쇼핑몰의 총 판매액입니다.

이처럼 피벗/교차표는 복잡한 원본 데이터를 직관적이고 요약된 형태로 변환하여 데이터 이해와 분석을 돕는 강력한 도구입니다.

---

## Slide 35

이 슬라이드는 특정 조건을 만족하는 아기 이름 데이터에서 각 연도와 성별에 따른 이름의 '점유율(share)'을 계산하고, 그 점유율이 가장 높은 상위 1개 이름을 추출하는 데이터 파이프라인을 설명합니다. ERA(대수 관계) 쿼리의 개념을 pandas 코드로 구현하는 방법을 보여줍니다.

---

### 핵심 개념 및 pandas 파이프라인 설명

**궁극적인 목표:** 1910년 이후의 아기 이름 데이터에서, 매년 각 성별(남/녀)별로 가장 높은 점유율을 차지한 이름(Top 1)을 찾는 것입니다. 점유율은 해당 연도의 전체 아기 이름 수 대비 특정 이름의 수를 의미합니다.

**데이터 예시 (가상 `babynames` DataFrame):**

| Year | Sex | Name     | Count |
| :--- | :-- | :------- | :---- |
| 1900 | F   | Mary     | 1000  |
| 1900 | M   | John     | 1200  |
| 1910 | F   | Mary     | 1500  |
| 1910 | F   | Helen    | 800   |
| 1910 | M   | John     | 1800  |
| 1910 | M   | William  | 900   |
| 1911 | F   | Elizabeth| 1600  |
| 1911 | F   | Mary     | 1400  |
| 1911 | M   | John     | 2000  |
| ...  | ... | ...      | ...   |

---

#### 1. `.query("Year >= 1910")`

*   **개념:** 특정 조건을 만족하는 행들만 필터링합니다. SQL의 `WHERE` 절과 유사합니다.
*   **설명:** `babynames` 데이터프레임에서 `Year` 컬럼의 값이 1910 이상인 데이터만 선택합니다.
*   **실생활 예시:** 한 회사의 20년간의 고객 주문 데이터가 있다고 가정해봅시다. 이 단계는 "우리는 2020년 이후의 주문 데이터만 분석하고 싶다"고 말하며, 2020년 이전의 모든 주문 기록을 제외하는 것과 같습니다. 위의 예시에서는 1900년 데이터가 제거됩니다.

#### 2. `.assign(year_total=lambda d: d.groupby("Year")["Count"].transform("sum"), share=lambda d: d["Count"]/d["year_total"])`

*   **개념:** 새로운 컬럼을 계산하여 데이터프레임에 추가합니다. 여기서는 두 개의 컬럼(`year_total`과 `share`)을 추가합니다.
    *   `groupby("Year")["Count"].transform("sum")`: `Year`별로 그룹화한 뒤 각 그룹 내의 `Count`를 합산(sum)합니다. 중요한 것은 `transform`을 사용한다는 점인데, 이는 그룹별 합계를 계산한 뒤 그 결과를 원래 데이터프레임의 모든 행에 다시 매핑(broadcasting)하여 `year_total` 컬럼을 생성합니다. 이렇게 하면 각 행이 속한 연도의 총 아기 이름 수가 해당 행에 그대로 표시됩니다.
    *   `share=lambda d: d["Count"]/d["year_total"]`: 각 이름의 `Count`를 해당 연도의 총 아기 이름 수(`year_total`)로 나누어 점유율(`share`)을 계산합니다.
*   **설명:** 먼저 각 `Year`마다 전체 아기 이름 수(`year_total`)를 계산하고, 이어서 각 이름의 `Count`를 해당 연도의 `year_total`로 나누어 연도별 점유율(`share`)을 계산합니다.
*   **실생활 예시:** 당신이 한 학교에서 각 과목의 시험 점수 데이터를 분석한다고 가정해봅시다.
    *   **`year_total`:** 각 학년(Year)의 모든 학생의 총점(Count)을 합산하여 그 학년의 전체 점수 합계(year_total)를 계산합니다. 이때 `transform("sum")`을 사용하면, '1학년'에 해당하는 모든 학생의 행에는 1학년 전체 점수 합계가 동일하게 기입됩니다.
    *   **`share`:** 이제 각 학생의 점수를 그 학생이 속한 학년의 전체 점수 합계로 나누어, 해당 학생의 점수가 학년 전체에서 차지하는 '비율(share)'을 계산하는 것과 같습니다. 이는 특정 이름이 해당 연도에 얼마나 많이 사용되었는지 상대적인 인기를 보여줍니다.

#### 3. `[["Year", "Sex", "Name", "Count", "share"]]`

*   **개념:** 필요한 컬럼들만 선택(투영, Projection)하여 데이터프레임을 구성합니다.
*   **설명:** 계산된 `share` 컬럼을 포함하여 `Year`, `Sex`, `Name`, `Count` 컬럼만 남기고, 다른 임시 컬럼이나 불필요한 컬럼은 제거합니다.
*   **실생활 예시:** 온라인 쇼핑몰에서 상품 판매 데이터를 분석한다고 할 때, 수십 개의 컬럼 중 우리가 정말 필요한 것은 '상품명', '판매 수량', '판매 가격', '카테고리' 뿐이라고 판단하여 나머지 '판매자 ID', '배송 상태' 등의 컬럼은 제외하고 보는 것과 같습니다.

#### 4. `.sort_values(["Year", "Sex", "share"], ascending=[True, True, False])`

*   **개념:** 특정 컬럼들의 값을 기준으로 데이터프레임의 행들을 정렬합니다. `ascending=[True, True, False]`는 각 컬럼에 대한 정렬 순서를 지정합니다.
*   **설명:**
    *   `Year`와 `Sex`를 기준으로 오름차순(True) 정렬합니다. 이렇게 하면 같은 연도, 같은 성별의 이름들이 한데 모입니다.
    *   이어서 `share`를 기준으로 내림차순(False) 정렬합니다. 이렇게 하면 각 `(Year, Sex)` 그룹 내에서 점유율이 가장 높은 이름이 맨 위로 오게 됩니다.
*   **실생활 예시:** 학교 성적표에서 반(Year)별로 먼저 정렬하고, 다음으로 남녀(Sex)별로 정렬한 다음, 마지막으로 점수(share)가 높은 순서(내림차순)로 정렬하는 것과 같습니다. 이렇게 하면 각 반, 각 성별 내에서 성적이 가장 좋은 학생이 맨 위에 오게 됩니다.

#### 5. `.groupby(["Year", "Sex"]).head(1)`

*   **개념:** `Year`와 `Sex`를 기준으로 그룹화한 뒤, 각 그룹의 첫 번째 행만 선택합니다. `head(1)`은 그룹 내에서 가장 위에 있는 하나의 행을 의미합니다.
*   **설명:** 이전 단계에서 `share`를 기준으로 내림차순 정렬했기 때문에, 이 단계에서 각 `(Year, Sex)` 그룹의 `head(1)`을 선택하면 해당 그룹 내에서 `share`가 가장 높은 이름이 선택됩니다. 이것이 바로 "Top 1"을 찾는 과정입니다.
*   **실생활 예시:** 앞선 학교 성적표 예시에서, 모든 정렬이 끝난 후 각 반, 각 성별 그룹별로 가장 위에 있는 학생(즉, 점수가 가장 높은 학생)의 정보만 뽑아내는 것과 같습니다. "각 반에서 남학생 1등, 여학생 1등만 뽑아!"와 같은 지시를 수행하는 것입니다.

#### 6. `.reset_index(drop=True)`

*   **개념:** 데이터프레임의 인덱스를 재설정합니다. `drop=True`는 원래의 인덱스를 새로운 컬럼으로 추가하는 대신 완전히 버리고 새로운 0부터 시작하는 기본 정수 인덱스를 생성합니다.
*   **설명:** `groupby`와 `head` 같은 작업을 수행하면 인덱스가 원래 데이터프레임의 인덱스를 유지하거나 다중 인덱스가 될 수 있습니다. 이 단계를 통해 깔끔하고 연속적인 정수 인덱스로 다시 만듭니다.
*   **실생활 예시:** 여러 부서(그룹)에서 '가장 실적이 좋은 직원'을 한 명씩 뽑아 새로운 '우수 직원 목록'을 만들었다고 가정합시다. 이때 원래 직원 번호(인덱스)가 불규칙하게 남아있을 수 있습니다. 이 목록을 보기 좋게 1번부터 순서대로 번호를 다시 매기는 것과 같습니다. `drop=True`는 원래의 직원 번호 컬럼을 새 목록에 남기지 않고 깔끔하게 정리하는 것입니다.

---

이 파이프라인은 데이터 분석에서 흔히 사용되는 '그룹별 상위 N개 항목 찾기' 문제에 대한 전형적인 해결책을 보여주며, 데이터를 필터링하고, 새로운 파생 변수를 생성하고, 정렬 및 그룹화를 통해 특정 조건을 만족하는 결과를 추출하는 과정을 잘 나타냅니다.

---

## Slide 36

## Query Best Practices (ERA ↔ pandas)

데이터를 효율적이고 정확하게 처리하기 위한 쿼리 모범 사례들을 ERA(관계 대수) 개념과 Pandas 라이브러리 사용법을 연결하여 설명하고, 각 개념에 대한 구체적인 실생활 예시를 제공하겠습니다.

### Selection (선택)

**개념:** ERA에서 '선택(σ)'은 테이블에서 특정 조건(predicate)을 만족하는 행(레코드)만을 추출하는 연산입니다. Pandas에서는 불리언 인덱싱(Boolean Indexing)이나 `.query()` 메서드를 통해 이를 수행합니다.

**모범 사례:**
*   **마스크(Mask) 괄호 사용:** 복잡한 조건을 연결할 때 `(조건1) & (조건2)`와 같이 괄호를 사용하여 연산의 우선순위를 명확히 합니다. 이는 논리 연산자(`&`, `|`)가 파이썬의 비트 연산자와 충돌하여 예상치 못한 결과를 낼 수 있는 Pandas의 특성 때문입니다.
*   `.query()` 사용 고려:** SQL과 유사한 문자열 기반의 쿼리를 작성할 수 있어 가독성을 높일 수 있습니다.

**실생활 예시:**
당신이 대학교 성적 데이터를 가지고 있고, **'컴퓨터공학과' 학생 중 '85점 이상'을 받은 학생들만'** 찾아내고 싶다고 가정해 봅시다.

```python
import pandas as pd

# 학생 성적 데이터프레임 생성
data = {
    '이름': ['김민준', '이서연', '박준서', '최지우', '정수민'],
    '학과': ['컴퓨터공학', '경영학', '컴퓨터공학', '컴퓨터공학', '수학'],
    '점수': [90, 88, 82, 95, 75]
}
df = pd.DataFrame(data)

print("원본 데이터프레임:\n", df)

# 1. 불리언 인덱싱과 괄호 사용 (모범 사례)
selected_students_mask = df[(df['학과'] == '컴퓨터공학') & (df['점수'] >= 85)]
print("\n[불리언 인덱싱 (괄호 사용)] 컴퓨터공학과 85점 이상 학생:\n", selected_students_mask)

# 2. .query() 메서드 사용 (모범 사례)
selected_students_query = df.query('학과 == "컴퓨터공학" and 점수 >= 85')
print("\n[.query() 사용] 컴퓨터공학과 85점 이상 학생:\n", selected_students_query)
```
이 예시에서, `(df['학과'] == '컴퓨터공학') & (df['점수'] >= 85)`는 두 가지 조건을 `&`(AND) 연산자로 결합합니다. 괄호가 없으면 파이썬의 비트 연산 우선순위 때문에 오류가 발생하거나 의도치 않은 결과가 나올 수 있습니다. `.query()`는 이런 복잡한 마스크를 보다 직관적인 문자열로 작성하게 해줍니다.

---

### Generalized Projection (확장 투영)

**개념:** ERA의 '투영(π)'은 테이블에서 특정 열(속성)만을 추출하는 연산입니다. '확장 투영'은 단순히 열을 선택하는 것을 넘어, 기존 열을 기반으로 새로운 열을 계산하여 추가하고, 그 결과를 포함하여 원하는 열들만 선택하는 것을 의미합니다. Pandas에서는 `.assign()`을 통해 새로운 열을 계산하고, 이어서 원하는 열들만 명시적으로 선택합니다.

**모범 사례:**
*   `.assign()`으로 계산된 새 열을 생성한 후, 명시적으로 원하는 열만 선택합니다. 이는 계산 로직과 최종 선택 로직을 분리하여 코드의 가독성을 높입니다.

**실생활 예시:**
위의 학생 성적 데이터에서 **'점수'를 바탕으로 '학점' 열을 새로 만들고, 최종적으로 '이름', '학과', '학점' 열만** 보고 싶다고 해봅시다.

```python
# ... (df 데이터프레임 계속 사용)

# 1. .assign()으로 '학점' 열 계산 및 추가
df_with_grade = df.assign(
    학점=lambda x: ['A' if s >= 90 else 'B' if s >= 80 else 'C' for s in x['점수']]
)

# 2. 최종적으로 원하는 열들만 선택
projected_df = df_with_grade[['이름', '학과', '학점']]
print("\n[확장 투영] 이름, 학과, 학점:\n", projected_df)
```
이 예시에서 `df.assign(...)`은 `점수` 열을 기반으로 `학점`이라는 새로운 열을 생성합니다. 그 후, `[['이름', '학과', '학점']]`을 사용하여 필요한 열들만 최종적으로 선택합니다. 이렇게 함으로써 `학점`을 계산하는 로직과 데이터를 최종적으로 보여주는 로직이 명확하게 분리됩니다.

---

### Set Semantics (집합 의미론)

**개념:** ERA의 집합 연산(합집합, 교집합, 차집합)처럼, 데이터에서 중복된 행을 허용하지 않고 오직 고유한 값들로만 이루어진 '집합'처럼 데이터를 다루는 것을 의미합니다. 일반적인 데이터 테이블은 '가방(bag)' 또는 '멀티셋(multiset)'으로 중복을 허용하지만, 특정 분석에서는 중복을 제거해야 할 때가 있습니다. Pandas에서는 `.drop_duplicates()` 메서드를 사용합니다.

**모범 사례:**
*   진정으로 고유한 행(레코드)을 원할 때 `.drop_duplicates()`를 명시적으로 추가하여 중복을 제거합니다.

**실생활 예시:**
당신이 웹사이트 방문 기록을 분석하고 있는데, **'오늘 웹사이트를 방문한 고유 사용자 ID'만** 알고 싶다고 가정해 봅시다. 한 사용자가 여러 번 방문했더라도 한 번만 카운트되어야 합니다.

```python
# 웹사이트 방문 기록 데이터프레임
visit_data = {
    'VisitorID': [101, 102, 101, 103, 102, 104, 101],
    'PageVisited': ['Home', 'About', 'Product', 'Contact', 'Home', 'Product', 'About'],
    'Timestamp': ['10:00', '10:05', '10:10', '10:15', '10:20', '10:25', '10:30']
}
visits_df = pd.DataFrame(visit_data)

print("원본 방문 기록 (중복 포함 - Bag):\n", visits_df)

# Best practice: .drop_duplicates()를 사용하여 고유 방문자 ID만 추출 (Set)
unique_visitors_df = visits_df.drop_duplicates(subset=['VisitorID'])
print("\n[집합 의미론] 고유 방문자 기록 (VisitorID 기준):\n", unique_visitors_df)

# 만약 '어떤 페이지를 방문했는지'와 상관없이 고유한 'VisitorID'만 얻고 싶다면
unique_visitor_ids = visits_df['VisitorID'].drop_duplicates()
print("\n[집합 의미론] 고유 VisitorID 목록:\n", unique_visitor_ids.tolist())
```
이 예시에서 `visits_df`는 `VisitorID` 101과 102가 여러 번 나타납니다. `drop_duplicates(subset=['VisitorID'])`는 `VisitorID` 열을 기준으로 중복된 행을 제거하여, 각 `VisitorID`에 대해 첫 번째 나타나는 행만 남깁니다. 이렇게 하면 방문 기록이라는 '가방'에서 '고유 방문자'라는 '집합'을 얻을 수 있습니다.

---

### Joins (조인)

**개념:** ERA의 '조인(⋈)'은 두 개 이상의 테이블(데이터프레임)을 공통된 열(키)을 기준으로 결합하여 새로운 테이블을 만드는 연산입니다. Pandas에서는 주로 `.merge()` 메서드를 사용합니다.

**모범 사례:**
*   **항상 키(key) 지정:** 어떤 열을 기준으로 조인할 것인지 `on`, `left_on`, `right_on` 매개변수를 통해 명확하게 지정해야 합니다. 키를 지정하지 않으면 Pandas가 공통된 열 이름을 모두 사용하여 조인할 수 있으나, 이는 의도치 않은 결과를 초래할 수 있습니다.
*   **키 다중성(multiplicities) 확인:** 조인하기 전에 조인 키의 유일성(unique)을 확인해야 합니다. 만약 한쪽 또는 양쪽 테이블에서 키가 중복되는 경우(예: 1대다 또는 다대다 관계), 조인 결과로 행의 수가 예상보다 훨씬 많이 늘어나는 '로우 블로우업(row blow-up)' 현상이 발생할 수 있습니다. 이를 이해하고 제어하거나 피해야 합니다.

**실생활 예시:**
당신이 학생들의 기본 정보와 그들이 수강한 과목 정보를 각각 다른 데이터프레임으로 가지고 있습니다. **'학생 정보'와 '수강 과목 정보'를 연결하여 각 학생이 수강한 모든 과목을'** 확인하고 싶습니다.

```python
# 학생 기본 정보 데이터프레임
students_df = pd.DataFrame({
    'StudentID': [1, 2, 3, 4],
    'Name': ['김영희', '이철수', '박민지', '최현우'],
    'Major': ['컴퓨터공학', '경영학', '컴퓨터공학', '수학']
})

# 수강 과목 정보 데이터프레임 (한 학생이 여러 과목을 들을 수 있음)
courses_df = pd.DataFrame({
    'CourseID': [101, 102, 103, 104, 101, 105],
    'StudentID': [1, 1, 2, 3, 4, 3], # 학생 ID 1은 두 과목, 학생 ID 3은 두 과목
    'CourseName': ['자료구조', '알고리즘', '회계원리', '데이터베이스', '선형대수학', '미적분']
})

print("학생 정보:\n", students_df)
print("\n수강 과목 정보:\n", courses_df)

# Best practice: 항상 키 지정
# StudentID를 기준으로 inner join (양쪽에 모두 존재하는 학생만)
# 키 다중성 확인: courses_df의 StudentID는 중복됩니다 (1대다 관계).
# 이는 StudentID 1번 학생이 두 과목을 듣고, StudentID 3번 학생도 두 과목을 들어
# 조인 시 해당 학생들의 정보가 각각의 과목 수만큼 복제되는 '로우 블로우업'이 예상됩니다.
merged_df = students_df.merge(courses_df, on='StudentID', how='inner')
print("\n[조인] 학생별 수강 과목 (로우 블로우업 발생 예시):\n", merged_df)

# 키 다중성 확인의 중요성:
# 만약 '학생별로 하나의 대표 과목만 연결하고 싶었는데' 이렇게 조인해서
# 데이터가 예상보다 많이 늘어났다면, 이는 분석 목적에 맞지 않을 수 있습니다.
# 이때는 courses_df에서 StudentID별로 '대표 과목'을 미리 집계(예: 첫 번째 과목만 선택)하거나,
# 조인 방식(예: left join 후 `drop_duplicates`)을 달리 고려해야 합니다.
```
`merged_df`를 보면 '김영희'와 '박민지' 학생의 정보가 각각 2번씩 나타나는 것을 볼 수 있습니다. 이는 `students_df`에서는 `StudentID`가 고유하지만, `courses_df`에서는 한 `StudentID`에 여러 `CourseID`가 매핑되어 1대다 관계를 형성하기 때문입니다. 이러한 '로우 블로우업' 현상을 사전에 인지하고 의도된 것인지 확인하거나, 피해야 할 경우 다른 전략을 사용해야 합니다.

---

### Grouping (그룹화)

**개념:** ERA에서 '그룹화'는 특정 열(속성)의 값들을 기준으로 데이터를 묶고, 각 그룹에 대해 합계, 평균, 개수 등과 같은 집계 함수를 적용하는 연산입니다. Pandas에서는 `.groupby()` 메서드를 사용한 후 집계 함수를 적용합니다.

**모범 사례:**
*   **내장(built-in) 함수 선호:** `sum()`, `mean()`, `size()` 등 Pandas에 내장된 집계 함수를 사용하는 것이 성능과 가독성 면에서 좋습니다.
*   **출력 열 이름 지정:** `.agg()` 메서드를 사용할 때 `새로운_열_이름=('기존_열', '집계_함수')` 형태로 출력될 열의 이름을 명시적으로 지정하여 결과 데이터프레임의 가독성을 높입니다.

**실생활 예시:**
당신이 전국 매장들의 판매 데이터를 가지고 있고, **'각 지역별 총 판매액, 평균 판매액, 거래 건수'를'** 분석하고 싶습니다.

```python
# 매장 판매 데이터프레임
sales_data = {
    'Region': ['서울', '경기', '서울', '부산', '경기', '서울', '대전'],
    'Product': ['TV', '냉장고', '세탁기', 'TV', '에어컨', '냉장고', '세탁기'],
    'SalesAmount': [1000, 1500, 1200, 800, 2000, 1100, 900]
}
sales_df = pd.DataFrame(sales_data)

print("원본 판매 데이터:\n", sales_df)

# Best practice: 내장 함수 및 출력 열 이름 지정
region_summary = sales_df.groupby('Region').agg(
    TotalSales=('SalesAmount', 'sum'),
    AverageSales=('SalesAmount', 'mean'),
    NumTransactions=('Product', 'size') # 'size'는 각 그룹의 행 개수를 셉니다.
)
print("\n[그룹화] 지역별 판매 요약:\n", region_summary)
```
이 예시에서 `sales_df.groupby('Region')`은 데이터를 `Region` 열의 값(서울, 경기, 부산, 대전)을 기준으로 묶습니다. `.agg()` 메서드를 사용하여 각 그룹에 대해 `SalesAmount`의 합계와 평균을 계산하고, `Product` 열의 `size` (해당 지역의 거래 건수)를 계산합니다. `TotalSales`, `AverageSales`, `NumTransactions`와 같이 명확한 새 열 이름을 지정하여 결과를 쉽게 이해할 수 있도록 합니다.

---

### Pivot (피벗)

**개념:** 피벗 연산은 데이터를 한 형태(보통 '롱(long) 포맷')에서 다른 형태(보통 '와이드(wide) 포맷' 또는 교차 테이블)로 재구성하는 강력한 도구입니다. 특정 열의 고유 값들을 새로운 열(컬럼)로 만들고, 다른 열의 값을 이 새로운 열들의 값으로 채웁니다. Pandas에서는 `pivot_table()` 메서드를 주로 사용합니다.

**모범 사례:**
*   **'하나의 (행, 열) 교차점에 하나의 값' 보장:** `pivot()` 메서드를 사용할 때는 `index`와 `columns`로 지정된 열들의 조합이 유일해야 합니다. 즉, 하나의 (행, 열) 교차점에 두 개 이상의 값이 존재하면 오류가 발생합니다.
*   **`aggfunc` 제공:** 만약 하나의 (행, 열) 교차점에 여러 값이 존재할 수 있다면, `pivot_table()` 메서드를 사용하고 `aggfunc` (집계 함수, 예: 'mean', 'sum', 'count')을 지정하여 이 여러 값들을 어떻게 처리할지 명시해야 합니다.

**실생활 예시:**
당신이 여러 학생의 과목별 성적 데이터를 가지고 있는데, **'학생을 행으로, 과목을 열로 하여 각 학생의 과목별 평균 점수를 한눈에'** 보고 싶다고 가정해 봅시다. 한 학생이 같은 과목에 대해 여러 번의 시험을 봤을 수 있습니다 (예: 중간고사, 기말고사).

```python
# 학생들의 과목별 시험 점수 데이터프레임 (롱 포맷)
exam_scores_data = {
    'Student': ['김민지', '이재훈', '김민지', '박소현', '이재훈', '김민지'],
    'Subject': ['수학', '수학', '수학', '영어', '영어', '과학'], # 김민지는 수학을 2번 봄
    'Score': [85, 90, 78, 92, 88, 80]
}
exam_scores_df = pd.DataFrame(exam_scores_data)

print("원본 시험 점수 데이터 (롱 포맷):\n", exam_scores_df)

# Best practice: aggfunc 제공 (하나의 (행,열) 교차점에 여러 값이 있을 수 있으므로)
# 김민지 학생이 '수학' 과목에 대해 85점과 78점 두 개의 점수가 있습니다.
# 만약 .pivot()을 사용하면 오류가 발생합니다.
# .pivot_table()을 사용하고 aggfunc='mean'을 지정하여 평균 점수를 계산합니다.
pivoted_df = exam_scores_df.pivot_table(index='Student', columns='Subject', values='Score', aggfunc='mean')
print("\n[피벗] 학생별 과목 평균 점수 (와이드 포맷):\n", pivoted_df)
```
이 예시에서 `exam_scores_df`는 각 시험 결과를 행으로 나열한 롱 포맷입니다. `pivot_table()`을 사용하여 `Student`를 행 인덱스로, `Subject`를 열 이름으로, `Score`를 값으로 설정했습니다. `aggfunc='mean'`은 '김민지' 학생의 '수학' 점수(85, 78)처럼 하나의 (학생, 과목) 교차점에 여러 점수가 있을 경우, 이들의 평균을 계산하여 해당 셀에 채워 넣도록 지시합니다. 만약 `aggfunc`를 지정하지 않고 이렇게 중복된 데이터가 있다면 `pivot_table` (또는 `pivot`)은 오류를 발생시킬 것입니다.

---

## Slide 37

## 결측치 처리 패턴 I

### 1. 결측치 감지 및 플래그 지정 (Detect & flag)

**핵심 개념:** 데이터프레임의 각 행에 하나라도 결측치(NA, NaN)가 존재하는지 여부를 확인하고, 그 결과를 새로운 컬럼으로 저장하는 기법입니다. 이는 특정 행에 문제가 있음을 빠르게 식별하거나, 후속 분석에서 해당 행을 특별히 처리해야 할 때 유용합니다.

**설명:**
`df.isna().any(axis=1)` 코드는 다음과 같은 과정을 거칩니다:
1.  `df.isna()`: 데이터프레임의 모든 값에 대해 결측치 여부를 True/False로 반환합니다.
2.  `.any(axis=1)`: 각 행(axis=1)에서 하나라도 True(결측치)가 있으면 해당 행에 대해 True를 반환합니다.
이렇게 생성된 `na_rows`라는 True/False Series는 `df["has_na"]`라는 새 컬럼으로 데이터프레임에 추가되어, 각 행의 결측치 유무를 쉽게 확인할 수 있는 플래그 역할을 합니다.

**구체적이고 실생활에 가까운 예시:**
당신이 온라인 쇼핑몰의 고객 데이터를 분석하고 있다고 가정해 봅시다. 이 데이터에는 고객 ID, 이름, 이메일 주소, 전화번호, 마지막 구매일 등의 정보가 있습니다.
만약 일부 고객의 이메일 주소나 전화번호가 누락되어 있다면, 이 고객들에게 마케팅 메시지를 보내거나 긴급 연락을 할 수 없습니다.

```python
import pandas as pd
import numpy as np

data = {
    'customer_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'email': ['alice@example.com', np.nan, 'charlie@example.com', 'david@example.com', np.nan],
    'phone': ['111-2222', '333-4444', np.nan, '777-8888', '999-0000'],
    'last_purchase': ['2023-01-15', '2023-02-20', '2023-03-10', '2023-04-01', '2023-05-05']
}
df = pd.DataFrame(data)

print("원본 데이터프레임:")
print(df)

# 각 행에 결측치가 있는지 감지하고 플래그 지정
na_rows = df.isna().any(axis=1)
df["has_na"] = na_rows

print("\n'has_na' 플래그가 추가된 데이터프레임:")
print(df)
```
**예시 설명:**
결과를 보면, `customer_id` 2번(Bob)은 이메일이, 3번(Charlie)은 전화번호가, 5번(Eve)은 이메일이 각각 결측치로 표시되어 `has_na` 컬럼이 `True`로 설정되었습니다. 이제 이 `has_na` 컬럼을 사용하여 다음과 같은 작업을 할 수 있습니다.
*   **빠른 필터링:** `df[df['has_na']]`를 통해 결측치가 있는 고객 목록만 빠르게 추출하여 데이터 보완 작업을 진행할 수 있습니다.
*   **모델 제외:** 만약 이 데이터를 고객 행동 예측 모델에 사용한다면, 결측치가 있는 행은 모델의 정확도를 떨어뜨릴 수 있으므로, 모델 학습에서 제외하거나 특별히 처리할 수 있습니다.
*   **감사 (Audit):** `has_na` 플래그는 어떤 데이터가 원래부터 불완전했는지 기록으로 남아 추후 데이터 품질 감사에 활용될 수 있습니다.

---

### 2. 그룹별 결측치 대체 (Group-wise impute: median/mean/ffill)

**핵심 개념:** 데이터셋 전체의 평균/중앙값으로 결측치를 채우는 대신, 데이터를 특정 그룹으로 나눈 후 *각 그룹 내에서* 계산된 통계량(예: 중앙값, 평균)으로 해당 그룹의 결측치를 채우는 방법입니다. 이는 서로 다른 특성을 가진 그룹 간의 정보 혼동(leakage)을 방지하고, 더 현실적인 값으로 결측치를 대체하는 데 사용됩니다.

**설명:**
`df.groupby("group")["x"].transform(lambda s: s.fillna(s.median()))` 코드는 다음을 수행합니다:
1.  `df.groupby("group")`: 데이터프레임을 "group" 컬럼의 고유 값에 따라 여러 그룹으로 나눕니다.
2.  `["x"]`: 각 그룹에서 "x" 컬럼만 선택합니다.
3.  `.transform(lambda s: s.fillna(s.median()))`: 각 그룹의 "x" 컬럼(Series `s`)에 대해 다음을 적용합니다.
    *   `s.median()`: 해당 그룹의 "x" 컬럼의 중앙값을 계산합니다.
    *   `s.fillna(...)`: 계산된 중앙값으로 해당 그룹의 "x" 컬럼 내 결측치를 채웁니다.
이 방식은 그룹별 특성을 유지하면서 결측치를 채울 수 있도록 합니다.

**구체적이고 실생활에 가까운 예시:**
당신이 여러 지역에 지점을 둔 프랜차이즈 카페의 일별 매출 데이터를 분석한다고 가정해 봅시다. 데이터에는 '지점_ID', '날짜', '총_매출' 정보가 있습니다. 시스템 오류로 인해 일부 지점의 특정 날짜 매출 데이터가 누락될 수 있습니다.

```python
import pandas as pd
import numpy as np

data = {
    'store_id': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-02', '2023-01-03'],
    'sales': [100, np.nan, 120, 50, 60, np.nan, 200, np.nan, 210]
}
df = pd.DataFrame(data)

print("원본 데이터프레임:")
print(df)

# 'store_id' 그룹별로 'sales' 컬럼의 결측치를 해당 그룹의 중앙값으로 대체
df["sales_imputed"] = (df.groupby("store_id")["sales"]
                       .transform(lambda s: s.fillna(s.median())))

print("\n그룹별 중앙값으로 결측치가 대체된 데이터프레임:")
print(df)
```
**예시 설명:**
*   **지점 A:** 1월 2일 매출이 결측치입니다. 지점 A의 다른 매출(100, 120)의 중앙값은 110이므로, 110으로 채워집니다.
*   **지점 B:** 1월 3일 매출이 결측치입니다. 지점 B의 다른 매출(50, 60)의 중앙값은 55이므로, 55로 채워집니다.
*   **지점 C:** 1월 2일 매출이 결측치입니다. 지점 C의 다른 매출(200, 210)의 중앙값은 205이므로, 205로 채워집니다.

만약 전체 데이터의 중앙값(이 경우 약 100)으로 결측치를 채웠다면, 지점 B의 55 매출이 100으로 채워져 실제 지점 B의 매출 경향과 동떨어진 값이 되었을 것입니다. 하지만 그룹별 중앙값으로 채우면 각 지점의 매출 규모와 특성을 반영하여 더 정확한 데이터를 얻을 수 있습니다.

*   **선택 (Choose):** 데이터 분포가 왜곡되어 있을 때는 중앙값(median)이 이상치에 강건하여 더 좋은 선택이며, 데이터 분포가 대칭적일 때는 평균(mean)을 사용할 수 있습니다. `ffill` (forward fill)은 패널 데이터(시간에 따라 동일한 개체를 추적하는 데이터)에서 이전 관측치를 그대로 가져오는 데 사용됩니다.
*   **주의 (Gotcha):** 만약 특정 그룹의 모든 값이 결측치라면, 해당 그룹의 중앙값/평균을 계산할 수 없습니다. 이 경우, 해당 그룹의 결측치는 채워지지 않거나, 전체 데이터의 중앙값/평균과 같은 전역(global) 값으로 대체하는 등의 추가적인 대체 전략이 필요합니다.

---

### 3. 시간 기반 결측치 채우기 (Time-aware fill)

**핵심 개념:** 시계열 데이터에서 결측치를 채울 때, 시간적 순서와 각 개체(entity)의 독립성을 보존하는 방법입니다. 이전 값(forward fill, `ffill`) 또는 이후 값(backward fill, `bfill`)을 사용하여 결측치를 채우는데, 이때 *동일한 개체 내에서만* 시간 순서대로 값을 전달받습니다.

**설명:**
`df.sort_values(["id", "ts"])`
`df["y_filled"] = df.groupby("id")["y"].ffill().bfill()` 코드는 다음을 수행합니다:
1.  `df.sort_values(["id", "ts"])`: 데이터를 'id' (개체 식별자)와 'ts' (시간) 컬럼 기준으로 정렬합니다. 이는 시간 순서를 보장하고 각 개체별로 결측치를 채우기 위한 필수 단계입니다.
2.  `df.groupby("id")["y"]`: 'id'별로 그룹을 나누고 각 그룹에서 'y' 컬럼을 선택합니다.
3.  `.ffill()`: 각 그룹 내에서 결측치를 이전의 유효한 값으로 채웁니다. (Forward Fill)
4.  `.bfill()`: `ffill`로 채워지지 않은 결측치(주로 그룹의 맨 앞에 결측치가 있는 경우)를 이후의 유효한 값으로 채웁니다. (Backward Fill)
이 과정은 시간적 인과관계를 보존하여 센서 데이터, 장바구니 로그, 스트리밍 데이터와 같이 시간에 따른 변화가 중요한 데이터에 적합합니다.

**구체적이고 실생활에 가까운 예시:**
당신이 스마트워치를 통해 여러 사용자의 심박수 데이터를 수집하고 있다고 가정해 봅시다. 각 사용자마다 '사용자_ID', '측정_시각', '심박수' 정보가 있습니다. 스마트워치 연결이 불안정하여 특정 시각의 심박수 데이터가 누락될 수 있습니다.

```python
import pandas as pd
import numpy as np

data = {
    'user_id': ['U1', 'U1', 'U1', 'U1', 'U2', 'U2', 'U2', 'U2'],
    'timestamp': ['09:00', '09:05', '09:10', '09:15', '09:00', '09:05', '09:10', '09:15'],
    'heart_rate': [70, np.nan, 75, 78, np.nan, 65, np.nan, 68]
}
df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp']) # 시간 데이터 형식으로 변환

print("원본 데이터프레임:")
print(df)

# 1. 사용자 ID와 측정 시각을 기준으로 데이터 정렬 (필수!)
df_sorted = df.sort_values(by=['user_id', 'timestamp'])

# 2. 사용자 ID별로 그룹을 나누고, 심박수 결측치를 ffill 후 bfill로 채우기
df_sorted["heart_rate_filled"] = df_sorted.groupby("user_id")["heart_rate"].ffill().bfill()

print("\n시간 기반으로 결측치가 채워진 데이터프레임:")
print(df_sorted)
```
**예시 설명:**
*   **사용자 U1:** 09:05의 심박수가 결측치입니다. 이전 값인 09:00의 70으로 채워집니다.
*   **사용자 U2:**
    *   09:00의 심박수가 결측치입니다. `ffill`로는 채워지지 않습니다 (앞에 값이 없으므로).
    *   09:10의 심박수가 결측치입니다. `ffill`로는 09:05의 65로 채워집니다.
    *   이후 `bfill`이 적용되어, 09:00의 결측치는 09:05에 `ffill`로 채워진 65가 아닌, 09:05의 원래 유효값인 65로 채워집니다. (`ffill()`을 먼저 적용하여 09:10이 65로 채워진 후, 다시 `bfill()`을 적용하면 09:00이 65로 채워집니다.)

이처럼, 사용자 U1의 결측치는 사용자 U1의 이전 심박수로 채워지고, 사용자 U2의 결측치 역시 사용자 U2의 이전/이후 심박수로 채워집니다. 만약 전체 데이터의 평균 심박수(예: 70)로 채웠다면, 사용자 U2의 65라는 낮은 심박수 경향이 무시되었을 것입니다. `ffill()`과 `bfill()`을 함께 사용하는 것은 그룹의 시작이나 끝에 있는 결측치까지 최대한 채우기 위함입니다.

*   **주의 (Gotcha):**
    *   **정렬:** 반드시 `id`와 `timestamp` 순으로 데이터를 정렬해야 합니다. 그렇지 않으면 잘못된 순서로 값이 전달되어 의미 없는 결과가 나올 수 있습니다.
    *   **최대 간격 (Max Gap):** 만약 심박수 데이터가 며칠 동안 누락되었다면, 며칠 전의 심박수로 현재 값을 채우는 것은 매우 비현실적일 수 있습니다. `ffill(limit=N)` 또는 `bfill(limit=N)`처럼 `limit` 파라미터를 사용하여 값을 전달할 최대 시간 간격을 제한하는 것을 고려해야 합니다. 이 제한을 넘어서는 결측치는 채우지 않고 여전히 `np.nan`으로 남겨두는 것이 더 안전할 수 있습니다.

---

## Slide 38

---

### 1. Coerce Numerics Safely (숫자형으로 안전하게 변환)

**핵심 개념:**
데이터프레임의 문자열 타입 열을 숫자형으로 변환하는 과정입니다. 이 과정에서 숫자로 변환할 수 없는 "더러운" 데이터(예: 쉼표, 대시, 통화 기호, 잘못된 텍스트)는 `NaN` (Not a Number)으로 처리하여 프로그램 오류를 방지하고 데이터 문제를 명시적으로 드러냅니다.

**중요성:**
*   숫자형 데이터가 되어야 사칙연산, 통계 계산, 스케일링 등의 수학적 처리가 가능해집니다.
*   잘못된 데이터를 `NaN`으로 변환함으로써 데이터 정제(cleaning) 및 이상치(outlier) 관리를 용이하게 합니다.

**실생활 예시:**
당신이 온라인 쇼핑몰의 판매 데이터를 분석하고 있다고 가정해 봅시다. `가격` 열에는 다음과 같은 다양한 형식의 데이터가 혼재되어 있을 수 있습니다.

*   `"1,500"`
*   `"$25.99"`
*   `"500"`
*   `"가격문의"` (실제 가격이 아닌 텍스트)
*   `"100.50"`

이 데이터들을 단순히 문자열로 둔다면 총 판매액을 계산하거나 평균 가격을 구하는 등의 작업이 불가능합니다. 이때 `pd.to_numeric(df["price"], errors="coerce")`를 사용하면:

*   `"1,500"`은 `1500.00`으로
*   `"$25.99"`는 전처리(예: `df['price'].str.replace('$', '').str.replace(',', '')`와 같은 과정을 거친 후) `25.99`으로
*   `"500"`은 `500.00`으로
*   `"가격문의"`는 `NaN`으로
*   `"100.50"`은 `100.50`으로 변환됩니다.

이제 `NaN` 값을 가진 항목을 제외하고 나머지 숫자들을 이용하여 총합이나 평균을 정확하게 계산할 수 있습니다. `NaN`이 된 "가격문의"는 데이터 품질 문제를 명확히 보여주므로, 해당 항목에 대해 추가적인 조사를 수행할 수 있습니다.

---

### 2. Use Categoricals for Keys (메모리 및 속도 향상을 위한 범주형 사용)

**핵심 개념:**
반복되는 레이블(문자열)이 많은 열을 `category` 데이터 타입으로 변환하는 것입니다. 이는 각 고유한 문자열에 정수 코드를 할당하고 실제 데이터는 이 정수 코드를 저장하는 방식으로 작동하여, 메모리 사용량을 줄이고 특정 연산의 속도를 향상시킵니다.

**중요성:**
*   **메모리 절약:** 고유한 값이 적고 반복되는 값이 많은(낮은 카디널리티) 열의 경우, 긴 문자열을 반복해서 저장하는 대신 작은 정수 코드를 저장하여 메모리 사용량을 크게 줄입니다.
*   **속도 향상:** `groupby()`, `join()`, `sort()`와 같은 연산에서 문자열 비교 대신 정수 비교를 수행하므로 처리 속도가 훨씬 빨라집니다.

**실생활 예시:**
당신이 전 세계 여러 도시에서 들어오는 고객 주문 데이터를 분석하고 있다고 상상해 봅시다. `도시` 열에는 "서울", "부산", "도쿄", "뉴욕"과 같은 도시 이름이 수십만, 수백만 번 반복되어 나타날 수 있습니다.

*   **변환 전 (문자열 타입):** `도시` 열은 각 행마다 "서울", "부산" 등의 문자열 전체를 저장합니다. 이는 많은 메모리를 소비하며, `df.groupby('도시')`와 같은 연산을 수행할 때마다 문자열 전체를 비교해야 하므로 느립니다.
*   **변환 후 (범주형 타입):** `df["city"] = df["city"].astype("category")`를 사용하면:
    *   Pandas는 내부적으로 "서울"에 0, "부산"에 1, "도쿄"에 2, "뉴욕"에 3과 같은 고유한 정수 코드를 할당합니다.
    *   `도시` 열은 더 이상 "서울"이라는 문자열을 저장하지 않고, 대신 해당 도시의 정수 코드(0, 1, 2, 3 등)를 저장합니다.
    *   이제 `df.groupby('도시')`를 수행하면 Pandas는 작은 정수 코드를 기반으로 그룹핑하므로 연산 속도가 비약적으로 빨라지고, 데이터프레임 전체의 메모리 사용량도 크게 줄어듭니다.

이 방식은 성별, 제품 카테고리, 요일 등 고유한 값의 종류가 제한적인 모든 열에 유용하게 적용될 수 있습니다.

---

### 3. Datetime Parsing (Robust) (강건한 날짜/시간 파싱)

**핵심 개념:**
다양한 형식의 날짜 및 시간(타임스탬프) 데이터를 일관된 표준 형식, 특히 타임존이 적용된 UTC(Coordinated Universal Time)로 변환하는 것입니다. `errors='coerce'`는 파싱할 수 없는 날짜/시간은 `NaT` (Not a Time)으로 처리하며, `utc=True`는 모든 변환된 시간을 UTC 기준으로 만듭니다.

**중요성:**
*   **일관된 기준:** 여러 소스에서 오는 날짜/시간 데이터는 형식이 제각각이거나 타임존 정보가 없거나 다르기 쉽습니다. UTC로 표준화하면 모든 시간 데이터를 동일한 기준에서 비교하고 분석할 수 있습니다.
*   **정확한 시계열 분석:** 데이터 샘플링, 롤링 통계 계산 등 시계열 분석의 정확성과 신뢰성을 높여줍니다.
*   **일광 절약 시간(DST) 오류 방지:** DST 전환 시 발생할 수 있는 복잡한 시간 계산 오류를 UTC 표준화를 통해 효과적으로 회피할 수 있습니다.

**실생활 예시:**
당신이 전 세계에 분산된 서버들로부터 시스템 로그를 수집하여 통합 분석하고 있다고 가정해 봅시다. 각 서버는 지역 시간대 기준으로 로그를 기록합니다:

*   **서버 A (뉴욕, UTC-4):** `"2023-10-29 01:30:00 EST"`
*   **서버 B (런던, UTC+1):** `"2023-10-29 09:30:00 BST"`
*   **서버 C (서울, UTC+9):** `"2023-10-29 17:30:00 KST"`

만약 이 타임스탬프들을 단순히 `pd.to_datetime`으로 변환하면, 각각의 시간대가 제대로 고려되지 않거나, 일광 절약 시간 전환(예: 10월 마지막 일요일)으로 인해 실제 이벤트 발생 순서가 뒤섞이거나 중복되는 시간이 발생할 수 있습니다.

이때 `pd.to_datetime(df["ts"], errors="coerce", utc=True)`를 사용하거나, 더 나아가 원본 시간대를 알고 있다면 `dt.tz_localize()`를 먼저 적용한 후 `tz_convert('UTC')`를 사용하면:

1.  **원본 시간대 파악 및 변환:** "2023-10-29 01:30:00 EST"는 뉴욕 시간 기준 새벽 1시 30분입니다. 이를 UTC로 정확히 변환하면 "2023-10-29 05:30:00+00:00" UTC가 됩니다.
2.  **모두 UTC로 표준화:** 모든 서버의 로그 시간이 UTC 기준으로 변환됩니다. 예를 들어, 런던 서버의 "2023-10-29 09:30:00 BST"와 서울 서버의 "2023-10-29 17:30:00 KST"는 동일한 절대 시점인 "2023-10-29 08:30:00+00:00" UTC로 변환될 수 있습니다.

이렇게 모든 로그 시간을 UTC로 통일하면, 전 세계 어디에서 발생했든 모든 이벤트를 정확한 시간 순서대로 정렬하고 분석하여 시스템 장애 발생 시점이나 사용자 활동 패턴 등을 오차 없이 파악할 수 있게 됩니다. 이는 복잡한 분산 시스템이나 글로벌 서비스 운영에서 필수적인 데이터 처리 기법입니다.

---

---

## Slide 39

## 핵심 개념 설명

### 1. 정확한/부분 집합 기반 중복 제거 (Exact / subset-based deduplication)

*   **무엇인가요?** 데이터프레임 내에서 특정 컬럼(들)의 조합이 완전히 동일한 행들을 찾아 제거하고, 유일한 행 하나만 남기는 기술입니다. 슬라이드 예시에서는 `user_id`와 `ts` (timestamp) 컬럼의 조합을 기준으로 중복을 판단합니다.
*   **왜 필요한가요?**
    *   **KPI 이중 계산 방지:** 예를 들어, 웹사이트 방문자 수를 집계할 때, 특정 `user_id`가 매우 짧은 시간 안에 여러 번 새로고침하여 동일한 `user_id`와 `ts`로 여러 로그가 찍혔다면, 이를 중복으로 간주하고 하나만 남겨 정확한 방문자 수를 계산할 수 있습니다.
    *   **머신러닝에서의 레이블 누수(label leakage) 방지:** 데이터셋에 동일한 특징을 가진 중복 샘플이 많으면 모델이 특정 패턴을 과도하게 학습하여 실제 환경에서 성능이 저하될 수 있습니다.
*   **팁:** 어떤 중복 데이터를 남길지는 `sort_values()`로 정렬한 뒤 `drop_duplicates(keep="first")` 또는 `keep="last"` 옵션을 사용하여 제어할 수 있습니다.

*   **실생활 예시:**
    당신이 온라인 쇼핑몰의 데이터 분석가라고 상상해 봅시다. '상품 구매' 이벤트를 추적하는 로그 데이터가 있는데, 네트워크 오류나 사용자의 더블 클릭 등으로 인해 동일한 `사용자 ID`가 같은 `상품 ID`를 거의 동시에 구매한 것으로 기록되는 경우가 발생할 수 있습니다.

    | 사용자 ID | 상품 ID | 구매 시각 (ts)    | 구매 수량 |
    | :-------- | :------ | :----------------- | :-------- |
    | user123   | itemA   | 2023-10-26 10:00:05 | 1         |
    | user456   | itemB   | 2023-10-26 10:01:10 | 1         |
    | user123   | itemA   | 2023-10-26 10:00:05 | 1         |
    | user789   | itemC   | 2023-10-26 10:02:30 | 2         |

    위 데이터에서 `user123`이 `itemA`를 `10:00:05`에 구매한 기록이 두 번 나타납니다. 만약 '총 구매 건수'를 집계해야 한다면, 이 중복된 행을 제거하지 않으면 실제로는 한 번의 구매였음에도 두 번으로 세어질 것입니다. 이때 `df.drop_duplicates(subset=["사용자 ID", "상품 ID", "구매 시각"])`를 사용하면 정확한 구매 건수를 얻을 수 있습니다.

### 2. 정규화된 텍스트 기반 유사 중복 처리 (Near-dup by normalized text)

*   **무엇인가요?** 텍스트 데이터의 사소한 차이(예: 대소문자, 공백, 특수문자) 때문에 다른 값으로 인식되는 것을 방지하기 위해, 텍스트를 표준화된 형태로 변환하여 유사한 항목들을 하나의 '정식 키(canonical key)'로 묶는 기술입니다.
*   **언제 필요한가요?** 여러 시스템에서 데이터를 통합하거나 수동 입력된 데이터가 혼재되어 있을 때, 대소문자, 공백, 구두점 등 서식 차이로 인해 같은 의미의 텍스트가 다르게 저장되는 경우에 유용합니다. 복잡한 퍼지 매칭(fuzzy matching)보다 기본적인 정규화가 더 효율적일 때가 많습니다.
*   **주의사항:** 악센트가 있는 문자(`é`, `ü`)나 복잡한 유니코드 문자 등은 `str.normalize("NFKD")` 같은 기능을 사용해야 할 수 있으며, 여러 개의 공백을 하나의 공백으로 또는 아예 제거하려면 정규표현식(`str.replace(r"\s+", "", regex=True)`)을 활용해야 합니다.

*   **실생활 예시:**
    당신이 여러 공급업체로부터 제품 데이터를 받아오는 재고 관리 시스템을 운영한다고 가정해 봅시다. 각 공급업체는 같은 제품이라도 다른 방식으로 이름을 입력하는 경향이 있습니다.

    | 제품명                           | 재고 수량 |
    | :------------------------------- | :-------- |
    | **Samsung Galaxy S23**           | 100       |
    | samsung galaxy s23               | 50        |
    | SAMSUNG GALAXY S23               | 70        |
    | Samsung Galaxy S23 Ultra         | 20        |
    |   Samsung  Galaxy  S23           | 30        |
    | Samsung_Galaxy_S23               | 40        |

    위 목록에서 "Samsung Galaxy S23"은 사실상 같은 제품을 지칭하지만, 대소문자, 공백, 특수문자 등에 따라 다르게 저장되어 있습니다. 이 상태로는 정확한 '총 Samsung Galaxy S23' 재고를 파악하기 어렵습니다.
    이때, 슬라이드에서처럼 `key = df["name"].str.strip().str.lower().str.replace(r"[ _]", "", regex=True)` 와 같이 정규화 과정을 거치면, 모든 "Samsung Galaxy S23" 관련 제품명은 `samsunggalaxys23`과 같은 통일된 키로 변환될 것입니다. 이 통일된 키를 기준으로 그룹화하거나 중복을 제거하면 정확한 재고 합계를 구할 수 있습니다.

### 3. 분위수 클리핑을 통한 윈저라이징 (Winsorize via quantile clipping)

*   **무엇인가요?** 데이터에 극단적인 이상치(outliers)가 있을 때, 이 이상치들을 제거하지 않고 특정 분위수(예: 상위 1% 또는 하위 1%)에 해당하는 값으로 대체하여 데이터의 범위를 제한하는 기법입니다. 이는 데이터의 평균이나 분산 같은 통계량을 안정화시키는 데 도움을 줍니다.
*   **왜 필요한가요?**
    *   **통계량 안정화:** 극단적인 값은 평균, 표준편차 등 통계량을 왜곡시킬 수 있습니다. 윈저라이징은 데이터를 삭제하지 않으면서 이러한 왜곡을 줄여줍니다.
    *   **모델 견고성 향상:** 머신러닝 모델, 특히 선형 모델은 이상치에 매우 민감하게 반응하여 모델의 성능을 저하시킬 수 있습니다. 윈저라이징은 모델이 이상치의 영향을 덜 받도록 하여 모델의 견고성(robustness)을 높여줍니다.
*   **팁:** 원본 데이터를 유지한 채(예: `x_raw` 컬럼) 윈저라이징된 새 컬럼을 만들면, 나중에 모델 결과나 데이터 변환에 대한 설명을 할 때 도움이 됩니다.

*   **실생활 예시:**
    당신이 한 회사의 직무별 연봉 데이터를 분석하여 평균 연봉을 계산하고, 이를 기반으로 인센티브 정책을 수립한다고 가정해 봅시다.

    | 직원 ID | 직무        | 연봉 (단위: 만 원) |
    | :------ | :---------- | :----------------- |
    | 101     | 주니어 개발자 | 4,000              |
    | 102     | 선임 개발자 | 7,000              |
    | 103     | CEO         | 50,000             |
    | 104     | 인턴        | 2,000              |
    | 105     | 시니어 개발자 | 9,000              |
    | 106     | 주니어 개발자 | 4,500              |
    | ...     | ...         | ...                |
    | 200     | 신입 인턴   | 1,500              |

    위 데이터에서 CEO의 5억 연봉과 매우 짧은 기간 근무한 인턴의 1,500만 원 연봉은 전체 직원 평균 연봉을 크게 왜곡시킬 수 있는 극단적인 이상치입니다. 예를 들어, 전체 평균 연봉을 계산하면 CEO 때문에 실제 대다수 직원의 연봉 수준보다 훨씬 높게 나올 수 있습니다.

    이때, 연봉 데이터를 윈저라이징할 수 있습니다. 예를 들어, 하위 1% 값은 3,000만 원, 상위 99% 값은 12,000만 원이라고 가정해 봅시다.
    *   CEO의 연봉 50,000만 원은 상위 99% 값인 12,000만 원으로 대체됩니다.
    *   인턴의 연봉 1,500만 원은 하위 1% 값인 3,000만 원으로 대체됩니다.

    이렇게 하면 극단적인 값들이 중간 범위로 조정되어, 평균 연봉이 대다수 직원의 연봉 수준을 더 잘 대표하게 되며, 이 데이터를 기반으로 한 인센티브 모델이나 정책 수립이 더 견고해질 수 있습니다. 중요한 것은, 이 과정에서 어떤 직원의 데이터도 삭제되지 않았다는 점입니다.

---

## Slide 40

데이터프레임의 형태를 변경(Reshaping)하는 세 가지 핵심 개념을 설명해 드릴게요.

---

### 1. Wide 형식을 Long 형식으로 변환 (`df.melt()`)

*   **핵심 개념**: 여러 개의 '데이터 값' 컬럼들을 두 개의 컬럼(하나는 '어떤 값'인지 나타내는 컬럼, 다른 하나는 '실제 값' 컬럼)으로 합쳐서 데이터 길이를 늘리는(unpivot) 작업입니다. 주로 깔끔한(tidy) 데이터 분석, 시각화, 그룹별 분석을 위해 사용됩니다.
*   **실생활 예시**:
    *   당신이 온라인 쇼핑몰의 판매 관리자라고 가정해 봅시다. 2023년 각 분기별(Q1, Q2, Q3, Q4)로 각 제품 카테고리(전자제품, 의류, 도서)의 판매량을 기록한 데이터프레임이 있습니다.
    *   `df_wide`:
        | 제품_카테고리 | Q1_판매량 | Q2_판매량 | Q3_판매량 | Q4_판매량 |
        | :---------- | :-------- | :-------- | :-------- | :-------- |
        | 전자제품    | 120       | 150       | 180       | 200       |
        | 의류        | 80        | 90        | 110       | 130       |
        | 도서        | 50        | 60        | 70        | 80        |
    *   이 데이터를 분기별 판매량 추이를 한눈에 보고 싶거나, 모든 카테고리에 대해 분기별 평균 판매량을 계산하고 싶다면, 'Q1_판매량', 'Q2_판매량' 등의 컬럼들을 '분기'라는 하나의 컬럼과 '판매량'이라는 하나의 컬럼으로 모으는 것이 훨씬 편리합니다. `df.melt()`를 사용하면 이렇게 만들 수 있습니다.
    *   `df_long` (melt 후):
        | 제품_카테고리 | 분기       | 판매량 |
        | :---------- | :--------- | :----- |
        | 전자제품    | Q1_판매량  | 120    |
        | 전자제품    | Q2_판매량  | 150    |
        | ...         | ...        | ...    |
        | 도서        | Q4_판매량  | 80     |
    *   **코드**: `long = df_wide.melt(id_vars=["제품_카테고리"], var_name="분기", value_name="판매량")`
    *   `value_vars` 인자를 사용하면 특정 판매량 컬럼만 선택하여 melt 할 수 있습니다. 예를 들어, `value_vars=["Q1_판매량", "Q2_판매량"]`와 같이 사용할 수 있습니다.

### 2. Long 형식을 Wide 형식으로 변환 (`df.pivot_table()`)

*   **핵심 개념**: Long 형식의 데이터를 다시 Wide 형식으로 변환하여 매트릭스 형태로 만듭니다. 이 과정에서 한 셀에 여러 값이 들어갈 수 있는 충돌(duplicate) 상황이 발생할 수 있는데, 이를 `aggfunc` 인자를 사용하여 '어떻게 합칠지'(평균, 합계, 첫 번째 값 등) 지정하여 해결합니다.
*   **실생활 예시**:
    *   위에서 만든 `df_long` 데이터(제품_카테고리, 분기, 판매량)를 다시 `df_wide` 형태로 되돌리거나, 특정 컬럼을 기준으로 집계된 새로운 Wide 형식의 표를 만들고 싶을 때 사용합니다.
    *   예를 들어, 각 제품 카테고리별로 '최고 판매량을 기록한 분기'의 판매량을 새로운 컬럼으로 만들고 싶을 수 있습니다.
    *   `df_long` (이전 예시에서 만든 데이터):
        | 제품_카테고리 | 분기       | 판매량 |
        | :---------- | :--------- | :----- |
        | 전자제품    | Q1_판매량  | 120    |
        | 전자제품    | Q2_판매량  | 150    |
        | 전자제품    | Q1_판매량  | 125    |
        | ...         | ...        | ...    |
    *   만약, 위 데이터에서 '전자제품'에 대해 'Q1_판매량'이 두 개 기록되어 있다면 (`120`과 `125`), `pivot_table`을 사용할 때 이 충돌을 어떻게 처리할지 정해야 합니다. `aggfunc='first'`는 첫 번째 값을, `aggfunc='mean'`은 평균값을, `aggfunc='max'`는 최댓값을 사용합니다. 여기서는 `aggfunc='first'`를 사용하여 첫 번째 값을 선택하도록 해보겠습니다.
    *   **코드**: `wide = df_long.pivot_table(index="제품_카테고리", columns="분기", values="판매량", aggfunc="first").reset_index()`
    *   `aggfunc`를 지정하지 않으면 중복 값이 있을 때 에러가 발생하므로 주의해야 합니다.

### 3. 리스트 형식 데이터 확장 (`df.explode()`)

*   **핵심 개념**: 특정 컬럼의 각 셀이 리스트(또는 배열)와 같은 여러 값을 포함하고 있을 때, 그 리스트의 각 요소를 개별적인 행으로 분리하여 데이터프레임의 행 수를 늘리는 작업입니다.
*   **실생활 예시**:
    *   당신이 영화 추천 서비스를 운영하고 있다고 가정해 봅시다. 각 영화는 여러 개의 '장르' 태그를 가질 수 있습니다.
    *   `df_movies`:
        | 영화_ID | 제목           | 장르                      | 평점 |
        | :------ | :------------- | :------------------------ | :--- |
        | 101     | 어벤져스       | ['액션', 'SF', '히어로'] | 4.5  |
        | 102     | 인터스텔라     | ['SF', '드라마']         | 4.7  |
        | 103     | 노트북         | ['로맨스', '드라마']     | 4.0  |
    *   만약 'SF' 장르에 속하는 영화가 총 몇 편인지, 또는 각 장르별 평균 평점은 얼마인지 분석하고 싶다면, '장르' 컬럼의 리스트 안에 있는 각각의 장르를 개별적인 행으로 분리해야 합니다. `df.explode()`를 사용하면 됩니다.
    *   `df_exploded` (explode 후):
        | 영화_ID | 제목       | 장르   | 평점 |
        | :------ | :--------- | :----- | :--- |
        | 101     | 어벤져스   | 액션   | 4.5  |
        | 101     | 어벤져스   | SF     | 4.5  |
        | 101     | 어벤져스   | 히어로 | 4.5  |
        | 102     | 인터스텔라 | SF     | 4.7  |
        | 102     | 인터스텔라 | 드라마 | 4.7  |
        | 103     | 노트북     | 로맨스 | 4.0  |
        | 103     | 노트북     | 드라마 | 4.0  |
    *   **코드**: `expl = df_movies.explode("장르", ignore_index=True)`
    *   이렇게 데이터를 확장하면 각 장르를 기준으로 쉽게 그룹화하여 통계(예: `df_exploded.groupby('장르')['평점'].mean()`)를 내거나, 특정 장르에 대한 추가 정보(lookup table)를 조인하여 더 풍부한 특징(feature)을 만들 수 있습니다.

---

## Slide 41

## 핵심 개념 요약 및 상세 설명

### 1. Join Hygiene: validate & audit (병합 무결성: 검증 및 감사)

**핵심 개념:** `pd.merge` 함수를 사용하여 두 데이터프레임을 병합할 때, 데이터의 관계(카디널리티)가 예상과 일치하는지 `validate` 인자로 검증하고, 병합 결과의 무결성을 `indicator=True` 인자로 감사하여 데이터 손실이나 중복을 방지하는 기법입니다.

**상세 설명:**
데이터 분석에서 여러 소스의 데이터를 합치는 것은 매우 흔한 작업입니다. 하지만 이 과정에서 조용히 데이터가 중복되거나, 일부 데이터가 누락되는 등의 문제가 발생할 수 있습니다. 이를 'silent data loss' 또는 'fanout'이라고 합니다. `validate` 인자는 이러한 문제를 사전에 방지하는 강력한 도구입니다.

*   **`validate='one_to_one'`**: 병합하려는 두 데이터프레임의 키가 모두 고유(unique)해야 함을 강제합니다. 예를 들어, 왼쪽 데이터프레임의 `customer_id` 하나가 오른쪽 데이터프레임의 `customer_id` 하나와만 정확히 매칭되어야 합니다. 만약 이 조건을 위반하면 Pandas는 오류를 발생시켜 데이터 불일치를 즉시 알려줍니다.
*   **`validate='one_to_many'` (또는 `many_to_one`, `many_to_many`)**: 왼쪽 데이터프레임의 키는 고유해야 하지만, 오른쪽 데이터프레임에서는 해당 키가 여러 번 나타날 수 있음을 허용합니다. 예를 들어, 한 고객(왼쪽)이 여러 주문(오른쪽)을 가질 수 있는 경우에 사용합니다.
*   **`indicator=True`**: 병합 결과에 `_merge`라는 새로운 컬럼을 추가합니다. 이 컬럼은 각 행이 왼쪽 데이터프레임에만 있었는지(`left_only`), 오른쪽 데이터프레임에만 있었는지(`right_only`), 아니면 양쪽에 모두 있었는지(`both`)를 표시합니다. 이를 통해 병합 과정에서 매칭되지 않은 데이터를 쉽게 찾아내 감사할 수 있습니다. 슬라이드의 `anti` 변수처럼 `left_only`인 행을 찾아 왼쪽 데이터프레임에만 있고 오른쪽에는 없는 항목들을 식별할 수 있습니다.

**구체적이고 실생활에 가까운 예시:**

당신은 온라인 쇼핑몰의 재고 관리자입니다.
1.  **`df_products`**: 상품 정보를 담고 있습니다. `product_id` (고유), `product_name`, `price`.
2.  **`df_suppliers`**: 상품별 공급업체 정보를 담고 있습니다. `product_id` (고유), `supplier_name`, `delivery_time`.

두 데이터프레임을 `product_id`를 기준으로 병합하여 각 상품의 공급업체 정보를 보고 싶습니다. 이때 `product_id`는 상품 식별자이므로 각 데이터프레임에서 고유해야 합니다.

```python
import pandas as pd

products_data = {
    'product_id': ['P001', 'P002', 'P003', 'P004'],
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'price': [1200, 25, 75, 300]
}
suppliers_data = {
    'product_id': ['P001', 'P002', 'P003', 'P005'], # P004는 공급업체 정보 없음, P005는 제품 정보 없음
    'supplier_name': ['TechCorp', 'MiceRUs', 'KeyPro', 'GlobalSupplies'],
    'delivery_time': [3, 1, 2, 5]
}

df_products = pd.DataFrame(products_data)
df_suppliers = pd.DataFrame(suppliers_data)

print("--- 원본 데이터프레임 ---")
print("Products:\n", df_products)
print("\nSuppliers:\n", df_suppliers)

# 1. 'one_to_one' 검증 예시:
# 만약 df_suppliers에 'P001'이 두 번 나타나는 오류가 있었다면?
# 예를 들어, suppliers_data = {'product_id': ['P001', 'P002', 'P003', 'P001']}
# 이 경우, validate='one_to_one'을 사용하면 오류를 발생시켜 경고해줍니다.
bad_suppliers_data = {
    'product_id': ['P001', 'P002', 'P003', 'P001'], # P001 중복!
    'supplier_name': ['TechCorp', 'MiceRUs', 'KeyPro', 'FastSupply'],
    'delivery_time': [3, 1, 2, 1]
}
df_bad_suppliers = pd.DataFrame(bad_suppliers_data)

try:
    print("\n--- 'one_to_one' 검증 시도 (실패 예상) ---")
    merged_with_validation = pd.merge(df_products, df_bad_suppliers, on='product_id', how='left', validate='one_to_one')
    print(merged_with_validation)
except Exception as e:
    print(f"오류 발생: {e}")
    print("설명: product_id 'P001'이 오른쪽(df_bad_suppliers)에 중복되어 'one_to_one' 검증에 실패했습니다. 이는 상품 정보가 조용히 중복되는 것을 방지합니다.")

# 2. 'indicator=True' 감사 예시:
print("\n--- 'indicator=True'를 사용한 병합 감사 ---")
merged_audited = pd.merge(df_products, df_suppliers, on='product_id', how='left', indicator=True)
print(merged_audited)

# 감사 결과를 통해 누락된 정보 식별
missing_supplier_info = merged_audited[merged_audited['_merge'] == 'left_only']
print("\n공급업체 정보가 누락된 상품 (left_only):\n", missing_supplier_info[['product_id', 'product_name']])

# 만약 right join을 했다면, 판매되지 않는 공급업체 상품을 찾을 수도 있습니다.
merged_audited_right = pd.merge(df_products, df_suppliers, on='product_id', how='right', indicator=True)
unlisted_products = merged_audited_right[merged_audited_right['_merge'] == 'right_only']
print("\n제품 목록에 없는 공급업체 상품 (right_only):\n", unlisted_products[['product_id', 'supplier_name']])
```
이 예시에서 `validate='one_to_one'`은 `product_id`가 각 테이블에서 한 번만 나타나야 한다는 규칙을 강제하여, 만약 공급업체 데이터에 'P001'이 중복 입력된 실수가 있다면 병합이 실패하게 만들어 즉시 문제를 발견하도록 돕습니다. `indicator=True`는 'P004' 상품에 대한 공급업체 정보가 없음을(`left_only`) 명확히 보여주어 어떤 데이터가 누락되었는지 쉽게 파악하고 후속 조치를 취할 수 있게 합니다.

---

### 2. Text Cleanup (텍스트 데이터 정리)

**핵심 개념:** 텍스트 데이터를 표준화된 형식으로 변환하여, 분석이나 검색, 병합 등의 작업에서 일관성을 확보하고 정확도를 높이는 과정입니다. 여기에는 유니코드 정규화, 공백 제거, 대소문자 통일 등이 포함됩니다.

**상세 설명:**
컴퓨터는 "Apple", "apple ", "APPLE"을 모두 다른 문자열로 인식합니다. 사람이 보기에는 같은 의미라도 컴퓨터에게는 다르게 인식되어 데이터 매칭이나 검색, 통계 분석 등에서 오류가 발생할 수 있습니다. 텍스트 정리는 이러한 비일관성을 제거합니다.

*   **`.str.normalize('NFKC')`**: 유니코드 정규화는 문자가 여러 방식으로 표현될 수 있는 문제를 해결합니다. 예를 들어, 한글의 "ㄱㅏ"와 "가"는 같은 의미지만 유니코드상 다르게 표현될 수 있습니다. `NFKC` (Normalization Form Compatibility Composition)는 이러한 호환성 문자를 표준 형태로 변환하여, 논리적으로 동일한 문자열이 항상 동일하게 표현되도록 합니다. 이는 다양한 인코딩이나 입력 방식으로 인해 발생할 수 있는 잠재적인 매칭 오류를 방지합니다.
*   **`.str.strip()`**: 문자열의 양 끝에 있는 공백(스페이스, 탭, 줄 바꿈 등)을 제거합니다. " Apple "과 "Apple"을 같게 만듭니다.
*   **`.str.lower()`**: 모든 문자를 소문자로 변환합니다. "Apple"과 "APPLE"을 모두 "apple"로 만들어 대소문자 차이로 인한 불일치를 제거합니다.
*   **`Tip: Remove punctuation/#s with str.replace (regex) when appropriate.`**: 구두점이나 특수문자('!', '?', '#', '@' 등) 또한 텍스트 매칭에 방해가 될 수 있습니다. 정규표현식(`regex`)을 활용한 `str.replace()`를 사용하여 이러한 문자들을 제거하거나 다른 문자로 대체할 수 있습니다.

**구체적이고 실생활에 가까운 예시:**

당신은 영화 리뷰 사이트의 데이터 분석가입니다. 사용자들이 입력한 영화 제목 데이터가 매우 지저분하여, 동일한 영화라도 여러 가지 방식으로 입력되어 있습니다.

```python
import pandas as pd

reviews_data = {
    'review_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'user_input_title': [
        'The Matrix',
        'the matrix ',           # 끝에 공백, 소문자
        '  THE MATRIX   ',       # 양끝 공백, 대문자
        'the matrix!',           # 특수문자 포함
        'The Matríx',            # 악센트 문자 (유니코드 변형)
        'matrix',                # 대소문자, 공백, 특수문자 없음
        'The Godfather',
        'the Godfather '
    ]
}
df_reviews = pd.DataFrame(reviews_data)

print("--- 원본 영화 제목 ---")
print(df_reviews['user_input_title'])
print(f"\n원본 데이터의 고유한 제목 개수: {df_reviews['user_input_title'].nunique()}")

# 텍스트 정리 파이프라인 적용
cleaned_titles = (
    df_reviews['user_input_title']
    .str.normalize('NFKC') # 유니코드 정규화 (예: 'í'를 'i'와 호환되게)
    .str.strip()           # 양 끝 공백 제거
    .str.lower()           # 소문자로 변환
    .str.replace(r'[^\w\s]', '', regex=True) # 알파벳, 숫자, 공백을 제외한 모든 특수문자 제거
)
df_reviews['cleaned_title'] = cleaned_titles

print("\n--- 정리된 영화 제목 ---")
print(df_reviews['cleaned_title'])
print(f"\n정리 후 고유한 제목 개수: {df_reviews['cleaned_title'].nunique()}")

# 정리 전후의 고유 값 비교
print("\n--- 고유 제목 목록 비교 ---")
print("정리 전 고유 제목:", df_reviews['user_input_title'].unique())
print("정리 후 고유 제목:", df_reviews['cleaned_title'].unique())
```
정리 전에는 "The Matrix", "the matrix ", "  THE MATRIX   ", "the matrix!", "The Matríx"가 모두 다른 제목으로 인식되어 5개의 고유한 제목으로 계산됩니다. 하지만 `str.normalize()`, `str.strip()`, `str.lower()`, `str.replace()`를 순서대로 적용하여 텍스트를 정리하면, 이 모든 제목이 "the matrix"로 통일됩니다. 이로써 실제로는 2개의 영화 ("the matrix", "the godfather")에 대한 리뷰 데이터임을 정확히 파악하고 분석할 수 있습니다.

---

### 3. Datetime Gotchas (날짜/시간 처리 시 주의사항)

**핵심 개념:** 문자열 형태의 날짜/시간 데이터를 `pd.to_datetime`을 사용하여 파싱하고 표준화하는 과정에서 발생할 수 있는 일반적인 문제점과 해결책을 다룹니다. 특히, 다양한 형식과 시간대 정보를 처리하고 오류를 안전하게 관리하는 방법을 강조합니다.

**상세 설명:**
날짜와 시간 데이터는 다양한 형식으로 존재하며, 시간대(Time Zone) 정보의 유무에 따라 큰 혼란을 야기할 수 있습니다. `pd.to_datetime`은 이러한 문제를 해결하는 Pandas의 핵심 함수입니다.

*   **`errors="coerce"`**: 파싱하려는 문자열이 유효한 날짜/시간 형식이 아닐 경우, 기본적으로 Pandas는 오류를 발생시키며 프로그램을 중단시킵니다. `errors="coerce"`는 이러한 경우 `NaT` (Not a Time) 값으로 변환하여 오류 없이 나머지 데이터 처리를 계속할 수 있게 합니다. 이는 대규모 데이터셋에서 일부 손상된 날짜/시간 문자열이 있을 때 매우 유용합니다.
*   **`utc=True`**: 이 인자는 파싱된 모든 날짜/시간 데이터를 Coordinated Universal Time (UTC)으로 변환합니다. 전 세계적으로 동일한 시간 기준인 UTC로 표준화하면, 데이터가 기록된 로컬 시간대나 일광 절약 시간제(Daylight Saving Time) 변경으로 인한 혼란을 피하고, 모든 데이터를 일관된 기준으로 비교하고 분석할 수 있습니다.
*   **Gotcha: Mixed formats or missing TZ info**: 데이터에 "2023-10-26" 같은 ISO 형식과 "10/26/23" 같은 미국식 형식이 섞여 있거나, "2023-10-26 14:30:00 KST"처럼 시간대 정보가 누락/다른 경우가 흔합니다. `pd.to_datetime`은 지능적으로 형식을 유추하려 하지만, 한계가 있습니다. `errors="coerce"`는 파싱 실패를 감지하는 데 도움을 줍니다.
*   **Auditing `NaT`**: `pd.to_datetime` 적용 후 `df["ts"].isna().mean()`을 사용하여 `NaT` 값의 비율을 확인하면, 파싱에 실패한 데이터가 전체의 몇 퍼센트인지 쉽게 파악하여 데이터 품질을 감사할 수 있습니다.
*   **`.dt` accessor**: 날짜/시간 데이터가 제대로 파싱되면 `.dt` accessor를 사용하여 년, 월, 일, 요일, 시간, 분, 초 등 다양한 시간 구성 요소를 쉽게 추출할 수 있습니다. 이는 시계열 분석이나 특정 시간대의 패턴을 파악하는 데 필수적입니다.

**구체적이고 실생활에 가까운 예시:**

당신은 모바일 앱의 사용자 로그인 기록을 분석하고 있습니다. `login_time` 컬럼에는 다양한 형식의 날짜/시간 문자열이 포함되어 있고, 일부는 잘못된 값도 있습니다.

```python
import pandas as pd

login_data = {
    'user_id': ['A1', 'B2', 'C3', 'D4', 'E5', 'F6'],
    'login_time_str': [
        '2023-10-26 10:30:00',      # 표준 형식
        '2023/10/27 14:15:00',      # 다른 구분자 사용
        '10/28/2023 09:00 AM',      # MM/DD/YYYY, AM/PM 사용
        'October 29, 2023',         # 날짜만, 영문 월
        'invalid date string',      # 잘못된 문자열
        '2023-10-30 18:00:00 KST'   # 시간대 정보 포함 (한국 시간)
    ]
}
df_logins = pd.DataFrame(login_data)

print("--- 원본 로그인 시간 문자열 ---")
print(df_logins['login_time_str'])

# 1. pd.to_datetime으로 안전하게 파싱 및 UTC 표준화
df_logins['parsed_login_time_utc'] = pd.to_datetime(df_logins['login_time_str'], errors="coerce", utc=True)

print("\n--- 파싱 및 UTC 표준화된 로그인 시간 ---")
print(df_logins['parsed_login_time_utc'])

# 2. 파싱 실패(NaT) 값 감사
failed_parses = df_logins['parsed_login_time_utc'].isna().sum()
print(f"\n파싱에 실패한 (NaT) 값의 개수: {failed_parses}개")
print(f"파싱 실패 비율: {df_logins['parsed_login_time_utc'].isna().mean() * 100:.2f}%")

# 3. 파싱된 datetime 컬럼에서 다양한 시간 특징 추출
df_logins['login_year'] = df_logins['parsed_login_time_utc'].dt.year
df_logins['login_month'] = df_logins['parsed_login_time_utc'].dt.month
df_logins['login_day_of_week'] = df_logins['parsed_login_time_utc'].dt.day_name() # 요일 이름
df_logins['login_hour'] = df_logins['parsed_login_time_utc'].dt.hour
df_logins['login_week'] = df_logins['parsed_login_time_utc'].dt.isocalendar().week.astype(int) # 주차

print("\n--- 파싱된 시간 컬럼 및 추출된 특징 ---")
print(df_logins[['user_id', 'login_time_str', 'parsed_login_time_utc', 'login_year', 'login_day_of_week', 'login_hour', 'login_week']])
```
이 예시에서 `pd.to_datetime(..., errors="coerce", utc=True)`는 다양한 형식의 로그인 시간을 일관된 UTC 기준으로 변환합니다. 'invalid date string'은 `NaT`로 처리되어 오류 없이 진행되며, 우리는 `isna().sum()`으로 이러한 문제가 있는 데이터를 쉽게 식별할 수 있습니다. 또한, `KST` (한국 표준시)로 입력된 마지막 값도 자동으로 UTC로 변환되어 다른 시간대 데이터와 함께 정확하게 비교할 수 있습니다 (KST는 UTC+9이므로, 18:00 KST는 09:00 UTC로 변환됩니다). 이후 `.dt` accessor를 통해 년도, 요일, 시간, 주차 등을 추출하여 "주말에 더 많은 로그인이 일어나는가?", "특정 시간대에 로그인 트래픽이 몰리는가?"와 같은 분석 질문에 답변할 수 있는 유용한 특징들을 생성합니다.

---

## Slide 42

## 핵심 개념 설명

### 1. 그룹별 통계량 및 특징 생성 (Group-aware Features)

이 섹션은 데이터를 특정 그룹으로 묶어 각 그룹 내에서 표준화, 순위, 이동 평균과 같은 특징(feature)을 계산하는 방법을 다룹니다. 이는 여러 개체(예: 상점, 고객)를 공정하게 비교하거나 시간 흐름에 따른 추세 및 계절성을 파악하는 데 유용합니다.

#### 1.1. 그룹별 Z-score (표준화)

*   **개념**: 각 데이터 포인트가 속한 그룹의 평균으로부터 얼마나 떨어져 있는지, 그리고 그 차이가 그룹 내 표준편차에 비해 얼마나 큰지를 나타내는 값입니다. 이를 통해 각 그룹의 특성을 고려하여 데이터를 표준화할 수 있습니다.
*   **코드 예시**:
    ```python
    g = df.groupby("store")["sales"]
    df["z"] = (df["sales"] - g.transform("mean")) / g.transform("std")
    ```
*   **실생활 예시**: 전국에 여러 지점을 가진 커피 체인점 '스타벅스'를 생각해봅시다. 각 지점마다 매장 규모, 위치, 유동인구가 다르기 때문에 단순한 일일 매출액만으로 지점의 성과를 비교하는 것은 공정하지 않습니다.
    *   '강남점'은 워낙 유동인구가 많아 일일 매출이 500만원이지만, '여의도점'은 오피스 상권이라 300만원입니다. 단순히 매출액만 보면 강남점이 훨씬 잘하는 것 같지만, 강남점은 평소에도 500만원 내외를 팔고 여의도점은 평소에 200만원을 파는 곳이라면 어떨까요?
    *   이때 **그룹별 Z-score**를 사용합니다. 각 지점(store)을 그룹으로 묶어, 해당 지점의 특정 날짜 매출액이 '그 지점의 평균 매출액'에 비해 얼마나 높거나 낮은지, 그리고 '그 지점의 매출액 변동폭(표준편차)'에 비해 얼마나 유의미한지를 계산합니다.
    *   만약 강남점의 Z-score가 0.5이고 여의도점의 Z-score가 1.5라면, 여의도점의 오늘의 매출이 '자신이 평소에 내는 성과'에 비해 훨씬 더 '뛰어나다'고 평가할 수 있습니다. 이를 통해 서로 다른 환경의 지점들을 공정하게 비교하고 이상치를 감지할 수 있습니다.

#### 1.2. 그룹별 순위 (Ranks)

*   **개념**: 각 데이터 포인트가 속한 그룹 내에서 자신의 값이 몇 번째로 높은(또는 낮은) 순위인지를 부여하는 것입니다.
*   **코드 예시**:
    ```python
    df["rank"] = g.rank(ascending=False, method="dense")
    ```
*   **실생활 예시**: 대학교에서 여러 학과(그룹)가 있고, 각 학과마다 학생들이 시험을 봅니다.
    *   '컴퓨터공학과'와 '수학과' 학생들이 중간고사를 봤다고 가정합시다. 단순히 점수만 보고 "90점은 잘했다"라고 평가할 수 있지만, 만약 컴퓨터공학과에서 90점이 최고 점수라면 매우 우수한 것이고, 수학과에서 90점이 최하위 점수라면 다른 의미가 됩니다.
    *   이때 **그룹별 순위**를 사용합니다. 각 학과(그룹) 내에서 학생들의 시험 점수에 따라 순위를 매깁니다.
    *   "이 학생은 '컴퓨터공학과'에서 100명 중 1등이다", "이 학생은 '수학과'에서 80명 중 5등이다"와 같이 해당 그룹의 맥락 안에서 상대적인 성과를 파악할 수 있습니다. `ascending=False`는 높은 점수가 더 높은 순위(예: 1등)를 얻는다는 의미이며, `method="dense"`는 공동 순위가 있을 경우 다음 순위를 건너뛰지 않고 밀집하게 부여합니다 (예: 1등, 1등, 2등, 3등).

#### 1.3. 그룹별 이동 평균 (Rolling Averages)

*   **개념**: 시계열 데이터에서 특정 기간(윈도우)을 정해 해당 윈도우 내의 값들의 평균을 계산하는 것입니다. 윈도우는 시간 축을 따라 이동하며 계산되는데, 이는 단기적인 노이즈를 제거하고 장기적인 추세나 계절성을 파악하는 데 유용합니다.
*   **코드 예시**:
    ```python
    df = df.sort_values(["store", "ts"]) # 롤링 연산 전에 반드시 정렬해야 함!
    df["roll7"] = (df.groupby("store")["sales"]
                    .rolling(7, min_periods=1).mean()
                    .reset_index(level=0, drop=True))
    ```
*   **실생활 예시**: 온라인 쇼핑몰 '쿠팡'에서 특정 상품의 일일 판매량을 추적한다고 가정해봅시다.
    *   특정 상품의 일일 판매량은 요일, 프로모션 유무, 날씨 등 여러 요인에 따라 들쭉날쭉할 수 있습니다. 예를 들어, 매주 주말에 판매량이 급증하고 주중에는 줄어드는 패턴이 있을 수 있습니다.
    *   **그룹별 이동 평균**은 이러한 단기적인 변동성 속에서 '진정한 추세'를 보고자 할 때 사용됩니다. 각 상품(그룹)별로 최근 7일(rolling(7))간의 평균 판매량(mean)을 계산합니다.
    *   `min_periods=1`은 데이터 초반에 7일치 데이터가 없더라도 최소 1일치만 있으면 평균을 계산하겠다는 뜻입니다 (초기 '웜업' 기간의 편향을 줄임).
    *   이를 통해 "이 상품은 지난 7일간 평균적으로 하루에 몇 개씩 팔리고 있다"는 정보를 얻을 수 있으며, 이는 일별 판매량의 큰 변동에도 불구하고 상품의 주간 판매 추세를 파악하고 재고 관리나 마케팅 전략을 세우는 데 도움을 줍니다. **가장 중요한 팁은 롤링 연산 전에 데이터를 시간 순서대로 정확하게 정렬해야 한다는 것입니다.**

---

### 2. Idempotent 체인 및 파이프라인 (Idempotent Chaining with assign/pipe)

이 섹션은 데이터 전처리 및 변환 과정을 명확하고 재사용 가능하며 디버깅하기 쉬운 '선언적 파이프라인' 형태로 구축하는 방법을 설명합니다. `pipe()`와 `assign()` 메서드를 활용하여 중간 변수 없이 일련의 연산을 연결합니다.

*   **개념**: 데이터를 처리하는 여러 단계를 하나의 연속적인 흐름으로 연결하는 방식입니다. `assign()`은 새 컬럼을 추가하거나 기존 컬럼을 변경할 때 주로 사용되고, `pipe()`는 일반 함수를 데이터프레임에 적용해야 할 때 유용합니다. 이렇게 만들어진 파이프라인은 '멱등성(Idempotent)'을 갖는 경우가 많아, 동일한 입력에 대해 항상 동일한 출력을 보장하고 여러 번 실행해도 결과가 변하지 않습니다.
*   **코드 예시**:
    ```python
    tidy = (df
            .pipe(lambda d: d.dropna(subset=["y"]))
            .assign(x=lambda d: d["x"].fillna(d["x"].median()))
            .sort_values(["id", "ts"]))
    ```
*   **Why**:
    *   **쉬운 디버깅**: 각 단계를 독립적으로 테스트할 수 있어 문제 발생 시 원인을 빠르게 찾을 수 있습니다.
    *   **재현성(Reproducibility)**: 모든 데이터 처리 과정이 명시적으로 기록되어 있어 언제든지 동일한 결과를 얻을 수 있습니다.
    *   **가독성**: 코드의 흐름이 위에서 아래로 명확하게 이어져 이해하기 쉽습니다.
*   **실생활 예시**: 설문조사 데이터를 분석하는 과정을 생각해봅시다. 원본 설문 데이터 `df`는 결측치, 잘못된 형식 등이 많아 정리가 필요합니다.

    1.  **초기 데이터 로드**: `df` (설문 응답 데이터)
    2.  **데이터 클리닝 파이프라인 구축**:
        *   `.pipe(lambda d: d.dropna(subset=["응답_필수항목"]))`: 설문에서 '이메일 주소'와 같은 **필수 응답 항목("y" 컬럼)**에 결측치가 있는 행은 분석에서 제외해야 합니다. `pipe`를 사용하여 `dropna`와 같은 일반 DataFrame 메서드를 적용합니다.
        *   `.assign(만족도_점수=lambda d: d["만족도"].fillna(d["만족도"].median()))`: 응답자가 **'만족도 점수'("x" 컬럼)**를 비워둔 경우, 데이터 손실을 줄이기 위해 전체 설문 응답의 중간값으로 해당 결측치를 채우고, 이를 `만족도_점수`라는 새로운 컬럼에 할당합니다. `assign`은 이런 컬럼 생성/수정에 매우 유용합니다.
        *   `.sort_values(["설문_ID", "응답_시간"])`: 최종적으로 처리된 데이터를 **설문 ID("id")**와 **응답 시간("ts")** 순서로 정렬하여 일관된 상태로 만듭니다.

    *   이렇게 연결된 파이프라인 `tidy`는 원본 `df`를 변경하지 않으면서, 모든 클리닝 및 변환 단계를 명확하고 순차적으로 보여줍니다. 새로운 설문 데이터가 들어와도 이 파이프라인을 그대로 실행하면 항상 동일한 방식으로 깨끗한 데이터를 얻을 수 있습니다. 또한, 각 `pipe`나 `assign` 단계에서 중간 결과를 확인하거나, 특정 단계만 따로 떼어내어 테스트하기가 용이해집니다.

---

