# CSED226 - numpy 상세 해설 노트

> 이 노트는 Gemini 2.5 Flash를 이용해 자동 생성되었습니다.

---

## Slide 1

---
### NumPy Essentials: Arrays, Indexing, Broadcasting, and Performance

**핵심 개념**:
*   **NumPy (Numerical Python)**: Python 기반의 과학 계산 라이브러리로, 다차원 배열 객체인 `ndarray`를 핵심 데이터 구조로 사용합니다. 벡터, 행렬 등 수학적 연산을 효율적으로 수행할 수 있도록 설계되었습니다.
*   **Arrays (배열)**: NumPy의 `ndarray`는 동일한 데이터 타입(homogeneous data type)을 가지는 원소들로 이루어진 다차원 그리드입니다. 파이썬 리스트와 달리 메모리에 연속적으로 저장되어 빠른 접근과 연산이 가능합니다.
*   **Indexing (인덱싱)**: `ndarray`의 특정 요소나 부분 배열(sub-array)에 접근하는 방법입니다. 기본적인 정수 인덱싱 외에 슬라이싱(Slicing), 불리언 인덱싱(Boolean Indexing), 팬시 인덱싱(Fancy Indexing) 등 다양한 고급 기법을 지원합니다.
*   **Broadcasting (브로드캐스팅)**: 서로 다른 형상(shape)을 가진 배열 간에 산술 연산을 수행할 수 있도록 NumPy가 자동으로 작은 차원의 배열을 큰 차원의 배열 형상에 맞게 확장하는 메커니즘입니다. 이를 통해 명시적인 반복문 없이 효율적인 연산이 가능합니다.
*   **Performance (성능)**: NumPy는 내부적으로 C, C++, Fortran과 같은 저수준 언어로 구현된 최적화된 루틴을 사용하기 때문에, 파이썬의 기본 리스트를 사용한 연산보다 월등히 빠른 속도를 제공합니다. 대규모 데이터셋 처리 및 수치 계산에 필수적인 이유입니다.

**코드/수식 해설**:

*   **Arrays (배열) 생성 예시**:

    ```python
    import numpy as np

    # 1차원 배열 (벡터)
    arr1 = np.array([1, 2, 3, 4, 5])
    print("1차원 배열:", arr1)
    print("형상(shape):", arr1.shape) # (5,)

    # 2차원 배열 (행렬)
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    print("\n2차원 배열:\n", arr2)
    print("형상(shape):", arr2.shape) # (2, 3)
    ```

*   **Indexing (인덱싱) 예시**:

    ```python
    arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

    # 기본 인덱싱: (행, 열)
    print("arr[0, 1]:", arr[0, 1]) # 20

    # 슬라이싱: 첫 번째 행의 모든 열
    print("arr[0, :]:", arr[0, :]) # [10 20 30]

    # 불리언 인덱싱: 50보다 큰 원소 선택
    print("arr[arr > 50]:", arr[arr > 50]) # [60 70 80 90]
    ```

*   **Broadcasting (브로드캐스팅) 예시**:

    ```python
    arr = np.array([[1, 2, 3], [4, 5, 6]]) # shape (2, 3)
    scalar = 10 # shape ()

    # 배열과 스칼라 덧셈 (스칼라가 배열 전체에 브로드캐스팅됨)
    result_scalar = arr + scalar
    print("스칼라 덧셈 결과:\n", result_scalar)
    # [[11 12 13]
    #  [14 15 16]]

    vec = np.array([100, 200, 300]) # shape (3,)
    # 배열과 벡터 덧셈 (vec이 행 방향으로 브로드캐스팅됨)
    result_vec = arr + vec
    print("\n벡터 덧셈 결과:\n", result_vec)
    # [[101 202 303]
    #  [104 205 306]]
    ```

**구체적 예시**:

*   **Arrays**: 마치 Excel 스프레드시트와 같습니다. 모든 셀에 숫자만 들어있고, 각 셀이 일정한 규칙(예: 정수, 실수)을 따릅니다. 행과 열로 구성된 표(2차원 배열)는 물론, 더 복잡한 3D 데이터(예: RGB 이미지의 픽셀 데이터)도 효율적으로 저장할 수 있습니다.
*   **Indexing**: 거대한 도서관에서 특정 책(요소)을 찾거나, 특정 섹션(부분 배열)의 책들을 한 번에 꺼내보는 것과 같습니다. 색인(index)을 통해 원하는 위치의 데이터를 정확하고 빠르게 찾아낼 수 있습니다.
*   **Broadcasting**: 모든 반 학생들에게 일괄적으로 5점씩 가산점을 주는 상황을 상상해 보세요. 각 학생의 점수에 5점을 더하는 과정을 학생 수만큼 반복할 필요 없이, "모든 점수에 5점을 더하라"는 한 번의 지시로 처리되는 것과 유사합니다. NumPy는 이 과정을 내부적으로 효율적으로 처리하여 개발자가 반복문을 작성할 필요를 없애줍니다.
*   **Performance**: 대량의 계산을 처리할 때, NumPy는 '특급 고속도로'와 같습니다. 일반 파이썬 리스트가 '국도'를 이용하는 것과 비교하면, NumPy는 C/C++로 만들어진 '고성능 엔진'을 장착하여 훨씬 빠르게 목적지에 도달합니다. 이는 데이터 과학 및 머신러닝에서 대규모 데이터를 다룰 때 필수적인 요소입니다.

**시험 포인트**:
*   ⭐ **NumPy `ndarray`의 특징**: 파이썬 `list`와의 차이점 (동일 데이터 타입, 메모리 연속성, 빠른 연산 속도)을 명확히 이해해야 합니다.
*   ⭐ **인덱싱 기법**: 정수 인덱싱, 슬라이싱, 불리언 인덱싱, 팬시 인덱싱의 사용법과 각 상황에서의 장단점을 구분할 수 있어야 합니다.
*   ⭐ **브로드캐스팅 규칙**: 서로 다른 형상의 배열이 어떻게 연산될 수 있는지 기본적인 브로드캐스팅 규칙을 이해하고 예제를 통해 설명할 수 있어야 합니다.
*   ⭐ **NumPy가 파이썬 기본 리스트보다 빠른 이유**: 내부 구현 방식(C/C++ 루틴 활용)과 메모리 구조(연속적인 메모리 할당)를 기반으로 설명할 수 있어야 합니다. 이는 데이터 분석의 효율성을 결정하는 핵심 개념입니다.
---

---
## Slide 2

**핵심 개념**
이 슬라이드는 `데이터분석 입문 (CSED226)` 강의에서 NumPy 라이브러리의 핵심 내용을 학습하기 위한 로드맵을 제시합니다. NumPy는 Python에서 과학 계산, 특히 다차원 배열(N-dimensional array, `ndarray`)을 효율적으로 처리하기 위한 기본 라이브러리입니다. 이 로드맵은 NumPy의 기본적인 개념부터 고급 최적화 기법 및 실전 활용까지 체계적인 학습 경로를 안내합니다.

주요 학습 내용은 다음과 같습니다:
1.  **NumPy at a Glance**: NumPy의 전반적인 소개 및 중요성.
2.  **Creation: Semantics**: NumPy 배열을 생성하는 다양한 방법과 그 의미.
3.  **Operations: Semantics**: NumPy 배열에 대한 기본적인 연산의 의미와 규칙.
4.  **Arrays and DTypes**: NumPy의 핵심 자료구조인 `ndarray`의 이해와 데이터 타입(dtype) 관리.
5.  **Indexing and Shaping**: 배열의 특정 요소에 접근(인덱싱)하고, 배열의 형태(shape)를 변경하는 방법.
6.  **Math and Linear Algebra**: NumPy를 활용한 기본적인 수학 연산 및 선형 대수학 연산.
7.  **Broadcasting**: 형태가 다른 배열 간의 연산을 가능하게 하는 브로드캐스팅 메커니즘.
8.  **Vectorization and Performance**: 벡터화된 연산을 통해 Python 리스트보다 NumPy가 훨씬 빠른 이유와 성능 최적화 기법.
9.  **Case Studies**: 실제 데이터 분석 문제에 NumPy를 적용한 사례 연구.
10. **Debugging and Best Practices**: NumPy 코드를 디버깅하는 방법 및 효율적인 코딩 습관.

**코드/수식 해설**
이 슬라이드 자체에는 코드가 없지만, 로드맵에서 다룰 NumPy의 핵심 기능들을 예시 코드를 통해 미리 엿볼 수 있습니다. NumPy는 벡터 및 행렬 연산을 고성능으로 수행하는 데 필수적입니다.

*   **배열 생성 및 기본 연산 (Creation, Operations, Arrays and DTypes 관련)**
    ```python
    import numpy as np

    # 1. 배열 생성 (Creation: Semantics, Arrays and DTypes)
    # 1차원 배열
    arr_1d = np.array([1, 2, 3, 4, 5])
    print(f"1D Array: {arr_1d}, Type: {arr_1d.dtype}, Shape: {arr_1d.shape}")

    # 2차원 배열 (행렬)
    arr_2d = np.array([[10, 20], [30, 40]])
    print(f"2D Array:\n{arr_2d}, Shape: {arr_2d.shape}")

    # 2. 기본 연산 (Operations: Semantics)
    # 배열 전체에 스칼라 값 더하기 (Broadcasting 예시)
    added_arr = arr_2d + 5
    print(f"2D Array + 5:\n{added_arr}")

    # 두 배열 간의 요소별(element-wise) 덧셈
    another_arr_2d = np.array([[1, 1], [1, 1]])
    elementwise_sum = arr_2d + another_arr_2d
    print(f"Element-wise sum:\n{elementwise_sum}")
    ```

*   **선형 대수학 연산 (Math and Linear Algebra 관련)**
    선형 대수학은 머신러닝의 핵심 기반이며, NumPy는 행렬 곱셈과 같은 연산을 효율적으로 지원합니다.
    ```python
    # 행렬 곱셈 (Dot product)
    mat1 = np.array([[1, 2], [3, 4]])
    mat2 = np.array([[5, 6], [7, 8]])

    # @ 연산자 또는 np.dot 함수 사용
    matrix_product = mat1 @ mat2
    # matrix_product = np.dot(mat1, mat2)
    print(f"Matrix Product:\n{matrix_product}")
    ```
    수식으로 표현된 행렬 곱셈($\mathbf{C} = \mathbf{A}\mathbf{B}$)은 다음과 같습니다:
    $$ C_{ij} = \sum_k A_{ik} B_{kj} $$
    예를 들어, 위 코드의 `mat1`과 `mat2`에 대해 $C_{11}$은 다음과 같이 계산됩니다:
    $$ C_{00} = A_{00}B_{00} + A_{01}B_{10} = (1)(5) + (2)(7) = 5 + 14 = 19 $$

**구체적 예시**
데이터 분석에서 NumPy는 이미지 처리, 음성 인식, 머신러닝 모델 구현 등 다양한 분야에서 활용됩니다. 예를 들어, 이미지는 픽셀 값의 2D 또는 3D 배열(RGB 채널 포함)로 표현될 수 있습니다.
*   **이미지 데이터 처리**: 512x512 크기의 컬러 이미지는 `(512, 512, 3)` 형태의 NumPy 배열로 표현됩니다 (높이, 너비, RGB 채널).
    *   **Indexing and Shaping**: 이미지의 특정 영역을 자르거나(cropping), 크기를 변경(resizing)하는 작업은 NumPy의 인덱싱 및 형태 변경 기능을 사용합니다.
    *   **Math and Linear Algebra**: 이미지 필터(예: 블러, 샤프닝)는 사실상 이미지 배열과 특정 커널(작은 행렬) 간의 컨볼루션 연산으로, NumPy의 행렬 연산을 활용합니다.
    *   **Broadcasting**: 이미지의 모든 픽셀 값을 특정 비율로 조정하여 밝기를 변경하는 작업은 스칼라 값(예: 0.8)을 이미지 배열 전체에 브로드캐스팅하여 곱하는 방식으로 효율적으로 처리됩니다.
    *   **Vectorization and Performance**: 이러한 복잡한 이미지 연산을 Python의 기본 `list`로 처리하면 엄청난 시간이 걸리지만, NumPy의 벡터화된 연산 덕분에 수 밀리초 내에 완료될 수 있습니다.

**시험 포인트**
*   ⭐ NumPy는 Python 기반 데이터 분석 및 머신러닝의 핵심 도구이므로, 이 로드맵에 제시된 **모든 항목을 정확히 이해하고 실제 코드에 적용할 수 있는 능력**이 필수적입니다.
*   ⭐ 특히 **`ndarray`의 생성, 인덱싱/슬라이싱, 브로드캐스팅, 그리고 벡터화 연산을 통한 성능 이점**에 대한 깊은 이해는 시험에서 자주 다루어지는 핵심 개념입니다.
*   ⭐ 각 개념이 **서로 어떻게 연결되는지(예: 브로드캐스팅이 연산 성능에 미치는 영향)** 파악하는 것이 중요하며, 이론적 이해뿐만 아니라 **다양한 예제를 통해 실습**해 보는 것이 중요합니다.

---
## Slide 3

### Why NumPy

-   **핵심 개념**:
    *   **고성능 N차원 배열**: NumPy는 N차원 배열(ndarray)을 제공하며, 메모리에 연속적으로(contiguous) 저장되어 데이터 접근 및 처리 속도가 매우 빠릅니다. 이는 파이썬 리스트와 달리 데이터 타입이 동일한 요소들로 구성되어 메모리 효율성을 높입니다.
    *   **벡터화된 연산 (Vectorized Computation)**: 개별 요소를 반복문으로 처리하는 대신, 배열 전체에 대해 한 번에 연산을 수행하는 방식을 의미합니다. 이를 통해 C/Fortran과 같은 저수준 언어로 최적화된 내부 코드를 활용하고 SIMD(Single Instruction, Multiple Data)와 같은 CPU 기능을 사용하여 대규모 데이터셋에서 엄청난 속도 향상을 얻을 수 있습니다.
    *   **풍부한 함수 라이브러리**: 보편적인 함수(universal functions, ufuncs), 통계적 환원(reductions, 예: sum, mean), 선형 대수(linear algebra) 연산 등 광범위한 수학적 기능을 제공합니다.
    *   **브로드캐스팅 (Broadcasting)**: 서로 다른(호환 가능한) 형태(shape)의 배열 간에도 수학 연산을 수행할 수 있도록 자동으로 배열의 형태를 맞춰주는 기능입니다. 이를 통해 간결하고 효율적인 코드를 작성할 수 있습니다.
    *   **과학 파이썬 스택의 기반**: NumPy는 pandas, matplotlib, scikit-learn 등 파이썬의 다른 주요 과학 및 데이터 분석 라이브러리의 핵심 기반으로 사용됩니다.

-   **코드/수식 해설**:
    *   **벡터화된 연산**:
        일반 파이썬 리스트를 사용하여 두 리스트를 더하는 경우:
        ```python
        a = [1, 2, 3]
        b = [4, 5, 6]
        c = []
        for i in range(len(a)):
            c.append(a[i] + b[i])
        print(c) # [5, 7, 9]
        ```
        NumPy 배열을 사용하여 벡터화된 연산을 수행하는 경우:
        ```python
        import numpy as np
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        c = a + b # 배열 전체에 대한 연산
        print(c) # [5 7 9]
        ```
        수식적으로는 각 요소에 대한 연산 $c_i = a_i + b_i$ 대신, 배열/벡터 전체에 대한 연산으로 표현됩니다:
        $$ C = A + B $$
        여기서 $A, B, C$는 벡터 또는 행렬을 나타냅니다.

    *   **브로드캐스팅**:
        스칼라 값을 배열에 더하는 경우:
        ```python
        import numpy as np
        arr = np.array([1, 2, 3])
        result = arr + 10 # 스칼라 10이 arr의 모든 요소에 더해짐
        print(result) # [11 12 13]
        ```
        수식적으로는 다음과 같이 볼 수 있습니다 (스칼라 $s$가 벡터 $A$의 각 요소에 더해짐):
        $$ C_i = A_i + s $$
        NumPy 내부적으로는 스칼라 $s$가 배열 $A$의 shape에 맞게 확장(broadcast)되어 연산이 수행됩니다.

-   **구체적 예시**:
    *   **이미지 처리**: 흑백 이미지의 모든 픽셀 값을 2배로 밝게 만들고 싶을 때, 파이썬 리스트로 처리하면 이중 반복문을 돌려야 하지만, NumPy를 사용하면 `image_array * 2`와 같이 단 한 줄로 모든 픽셀에 대한 연산이 완료됩니다.
    *   **통계 분석**: 수십만 개의 데이터 포인트로 구성된 시계열 데이터에서 이동 평균(moving average)을 계산하거나, 전체 데이터셋의 평균과 표준편차를 구하는 작업을 할 때, NumPy의 벡터화된 연산과 `np.mean()`, `np.std()`와 같은 universal functions를 사용하면 매우 빠르고 효율적으로 처리할 수 있습니다.
    *   **머신러닝**: 경사 하강법(Gradient Descent)과 같은 최적화 알고리즘에서 가중치 벡터에 특정 값을 더하거나 곱하는 연산, 두 행렬의 내적(dot product) 연산 등이 빈번하게 발생합니다. NumPy는 이러한 선형 대수 연산을 최적화된 방식으로 제공하여 머신러닝 모델 학습 속도를 향상시킵니다.

-   **시험 포인트**:
    *   ⭐ **NumPy를 사용하는 가장 큰 이유**는 "N차원 배열을 통한 **벡터화된 연산**"이며, 이는 "메모리 **연속성**"과 "최적화된 저수준 코드(C/Fortran, SIMD)" 덕분에 가능합니다.
    *   ⭐ **브로드캐스팅**의 개념과 그 역할 (간결한 코드, 다른 shape 간 연산 가능)을 정확히 이해해야 합니다.
    *   ⭐ NumPy가 **다른 데이터 과학 라이브러리(pandas, scikit-learn 등)의 기반**이 된다는 점을 기억하세요. 이는 NumPy의 중요성을 뒷받침합니다.
    *   ⭐ 파이썬 `for` 루프를 사용하는 것과 NumPy의 벡터화된 연산의 **성능 차이**를 설명할 수 있어야 합니다.

---
## Slide 4

**핵심 개념**
이 슬라이드는 NumPy의 핵심 이점 중 하나인 **벡터화(Vectorization)**의 중요성을 보여줍니다. 벡터화는 데이터 배열에 대한 연산을 개별 요소에 대한 반복적인 루프 대신, 전체 배열에 대해 한 번에 수행하여 성능을 극적으로 향상시키는 기법입니다. 파이썬의 `for` 루프는 인터프리터 오버헤드로 인해 대규모 데이터셋에서는 느려질 수 있지만, NumPy는 내부적으로 C나 Fortran과 같은 저수준 언어로 구현된 최적화된 연산을 사용하여 이러한 문제를 해결합니다. 이 예시에서는 두 벡터의 내적(dot product)을 계산하는 과정을 순수 파이썬 루프 방식과 NumPy의 벡터화된 방식으로 비교하여 성능 차이를 시연합니다.

**코드/수식 해설**

1.  **초기 설정 및 데이터 생성**:
    ```python
    import numpy as np, time

    rng = np.random.default_rng(0) # 난수 생성기 초기화 (재현성을 위해 seed 0 사용)
    x = rng.random(400_000)      # 40만 개의 랜덤 실수로 구성된 1차원 NumPy 배열 x 생성
    y = rng.random(400_000)      # 40만 개의 랜덤 실수로 구성된 1차원 NumPy 배열 y 생성
    ```
    *   `import numpy as np, time`: NumPy 라이브러리를 `np`로, 시간 측정 모듈 `time`을 임포트합니다.
    *   `np.random.default_rng(0)`: 재현 가능한(reproducible) 난수를 생성하기 위해 난수 생성기를 특정 시드(seed, 여기서는 0)로 초기화합니다. 같은 시드를 사용하면 항상 동일한 난수 시퀀스가 생성됩니다.
    *   `rng.random(400_000)`: 0과 1 사이의 균등 분포를 따르는 400,000개의 부동 소수점 숫자로 이루어진 1차원 NumPy 배열 `x`와 `y`를 각각 생성합니다.

2.  **루프 기반 계산 (순수 파이썬)**:
    ```python
    t0 = time.perf_counter() # 시작 시간 기록
    s_loop = 0.0             # 합계를 저장할 변수 초기화
    for i in range(x.size):  # 배열 x의 크기만큼 반복
        s_loop += x[i] * y[i] # 각 요소의 곱을 더함
    t1 = time.perf_counter() # 종료 시간 기록
    ```
    *   `time.perf_counter()`: 코드 블록의 정확한 실행 시간을 측정하기 위해 사용됩니다. 시스템 전체 시간을 기준으로 가장 높은 해상도의 타이머를 제공합니다.
    *   `for i in range(x.size)`: `x.size`는 배열 `x`의 요소 개수(400,000)를 나타냅니다. 이 루프는 `x`와 `y`의 모든 요소를 순회하며, 각 인덱스 `i`에 대해 `x[i]`와 `y[i]`를 곱한 값을 `s_loop`에 누적합니다. 이는 파이썬의 표준 `for` 루프 방식이며, 각 반복마다 파이썬 인터프리터의 오버헤드가 발생합니다.

3.  **벡터화된 계산 (NumPy)**:
    ```python
    t2 = time.perf_counter()   # 시작 시간 기록
    s_vec = (x * y).sum()      # NumPy의 벡터화된 연산으로 계산
    t3 = time.perf_counter()   # 종료 시간 기록
    ```
    *   `x * y`: NumPy 배열 `x`와 `y`에 대해 `*` 연산자를 사용하면, 각 배열의 해당 위치에 있는 요소들끼리 곱하는 **원소별 곱셈(element-wise multiplication)**이 수행됩니다. 이 연산은 내부적으로 매우 최적화되어 C 언어 수준의 속도로 실행됩니다.
    *   `.sum()`: 원소별 곱셈의 결과로 생성된 새로운 NumPy 배열의 모든 요소를 합산합니다. 이 또한 최적화된 NumPy 함수입니다.
    *   이 전체 과정은 단 두 줄의 코드로 `for` 루프와 동일한 결과를 훨씬 빠르게 얻을 수 있습니다.

4.  **시간 출력**:
    ```python
    print("loop:", t1 - t0, "sec")
    # print("vectorized:", t3 - t2, "sec") # 벡터화된 시간 비교를 위해 보통 이와 같이 출력
    ```
    *   두 방식의 실행 시간(`t1 - t0`과 `t3 - t2`)을 비교하여 NumPy 벡터화의 성능 우위를 보여줍니다.

**수식:**
위 코드는 두 벡터 $\mathbf{x}$와 $\mathbf{y}$의 내적(Dot Product)을 계산하는 과정을 보여줍니다. $n$은 벡터의 크기(여기서는 400,000)입니다.
$$
\mathbf{x} \cdot \mathbf{y} = \sum_{i=0}^{n-1} x_i y_i = x_0 y_0 + x_1 y_1 + \dots + x_{n-1} y_{n-1}
$$

**구체적 예시**

*   **실생활 비유**:
    당신이 40만 명의 학생들의 두 가지 시험 점수(x 과목 점수, y 과목 점수)를 가지고 있고, 각 학생의 두 점수를 곱한 후 그 총합을 구해야 한다고 가정해 봅시다.
    *   **루프 방식**: 조교 한 명이 학생 한 명씩 찾아가서 "너 x랑 y 점수 곱하면 얼마니?"라고 묻고, 그 답을 받아 적은 후 다음 학생에게 가는 것을 40만 번 반복하는 것과 같습니다. 이 과정은 시간이 매우 오래 걸릴 것입니다.
    *   **벡터화 방식**: 조교가 40만 명의 학생들에게 "각자 x 점수와 y 점수를 곱한 값을 적어서 제출하세요!"라고 한 번에 지시하고, 학생들이 동시에 계산하여 제출하면, 조교는 제출된 값들을 빠르게 합산하는 것과 같습니다. 이 방식은 개별 학생과 대화하는 오버헤드 없이 훨씬 효율적이고 빠릅니다.

*   **데이터 과학 예시**:
    머신러닝 모델, 특히 신경망(Neural Network)에서는 입력 데이터 벡터와 가중치(weights) 벡터를 곱하고 더하는 연산(가중합, weighted sum)이 빈번하게 발생합니다. 이러한 연산은 수많은 데이터 포인트와 가중치에 대해 이루어지므로, NumPy의 벡터화는 모델 훈련 및 추론 속도를 결정하는 핵심 요소가 됩니다. 예를 들어, 이미지 처리에서 모든 픽셀에 동일한 연산을 적용하거나, 통계 분석에서 대규모 데이터셋의 각 특징(feature)에 대해 계산을 수행할 때 벡터화는 필수적입니다.

**시험 포인트**

*   ⭐ **벡터화(Vectorization)의 정의와 중요성**을 설명하고, 왜 NumPy가 데이터 과학에서 필수적인 도구인지 논하시오. (성능 최적화, 코드 간결성)
*   ⭐ **NumPy 배열 연산이 순수 파이썬 루프보다 훨씬 빠른 이유**를 설명할 수 있어야 합니다. (내부적으로 C/Fortran으로 구현, 파이썬 인터프리터 오버헤드 감소, SIMD(Single Instruction Multiple Data) 활용 가능성 등)
*   ⭐ `np.random.default_rng(seed)`의 역할과 **재현 가능한(reproducible) 난수 생성**의 의미를 이해하고 설명할 수 있어야 합니다.
*   ⭐ `time.perf_counter()`를 사용하여 **코드 블록의 실행 시간을 측정하는 방법**을 숙지해야 합니다.
*   ⭐ `(x * y).sum()`과 같이 **벡터화된 코드를 작성**하여 특정 연산(예: 내적, 원소별 곱셈 등)을 효율적으로 수행하는 능력을 보여줄 수 있어야 합니다.
*   Python 리스트와 NumPy 배열 간의 **성능 차이 및 메모리 효율성** 측면에서 비교하는 문제가 출제될 수 있습니다.
*   데이터 과학 및 머신러닝에서 **NumPy의 역할과 적용 사례**에 대한 이해가 중요합니다.

---
## Slide 5

---
**핵심 개념**

*   **NumPy Array (ndarray)**: NumPy 라이브러리의 핵심 데이터 구조로, 효율적인 수치 계산을 위해 설계된 다차원 배열입니다. 파이썬 리스트와 달리 모든 원소가 동일한 데이터 타입(homogeneous data type)을 가지며, 메모리 효율성과 연산 속도에서 큰 이점을 가집니다.
*   **Shape**: 배열의 각 차원(dimension 또는 axis)의 크기를 나타내는 튜플입니다. 예를 들어, (3, 4)는 3개의 행과 4개의 열을 가진 2차원 배열을 의미합니다.
*   **Indexing**: 배열 내의 특정 원소에 접근하는 방법입니다. NumPy 배열은 0-기반(0-based) 인덱싱을 사용하며, `A[i, j]`와 같이 콤마로 구분된 인덱스를 사용하여 다차원 배열의 특정 위치에 접근할 수 있습니다.
*   **Dtype (Data Type)**: 배열 내 모든 원소가 가지는 데이터 타입입니다. `np.int32`, `np.float64` 등 다양한 데이터 타입을 지정할 수 있으며, 이는 메모리 사용량과 연산 정밀도에 영향을 미칩니다.

**코드/수식 해설**

아래 코드는 2차원 NumPy 배열을 생성하고 그 주요 속성을 확인하는 예시입니다.

```python
import numpy as np

# 3행 4열의 2차원 NumPy 배열 A를 생성합니다.
# dtype=np.int32는 배열의 모든 원소가 32비트 정수형임을 명시합니다.
A = np.array([[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]], dtype=np.int32)

# 배열 A의 shape(형태)를 출력합니다.
print(A.shape) # 출력: (3, 4)

# 배열 A의 (1, 2) 인덱스에 해당하는 원소를 출력합니다.
# (0-기반 인덱싱이므로, 두 번째 행, 세 번째 열을 의미합니다.)
print(A[1, 2]) # 출력: 7
```

위 코드로 생성된 배열 $A$는 다음과 같은 3x4 행렬로 시각화할 수 있습니다.
$$
A = \begin{bmatrix} 1 & 2 & 3 & 4 \\ 5 & 6 & 7 & 8 \\ 9 & 10 & 11 & 12 \end{bmatrix}
$$
이때, $A$의 `shape`은 $(3, 4)$이며, 이는 3개의 행(axis 0의 길이 = 3)과 4개의 열(axis 1의 길이 = 4)을 가진다는 의미입니다.

인덱싱은 0-기반으로 이루어지며, 특정 원소 $A[i, j]$는 다음과 같이 표현됩니다.
$i \in \{0, 1, 2\}$ (행 인덱스)
$j \in \{0, 1, 2, 3\}$ (열 인덱스)
예를 들어, $A[1, 2]$는 두 번째 행(인덱스 1), 세 번째 열(인덱스 2)에 위치한 값인 $7$을 나타냅니다.

**구체적 예시**

어떤 반의 세 학생(학생 1, 학생 2, 학생 3)이 네 과목(국어, 영어, 수학, 과학)의 시험 점수를 받았다고 가정해 봅시다. 이 점수들을 NumPy 배열로 표현하면 다음과 같습니다.

*   학생 1: 국어 1점, 영어 2점, 수학 3점, 과학 4점
*   학생 2: 국어 5점, 영어 6점, 수학 7점, 과학 8점
*   학생 3: 국어 9점, 영어 10점, 수학 11점, 과학 12점

이 데이터를 `A`라는 NumPy 배열로 만들면,
`A.shape`은 `(3, 4)`가 되어 "3명의 학생"과 "4개의 과목"이라는 구조를 명확히 보여줍니다.
`A[1, 2]`는 인덱스 1번 학생(두 번째 학생)의 인덱스 2번 과목(세 번째 과목, 즉 수학) 점수인 `7`을 나타냅니다. 모든 점수는 정수형(`np.int32`)으로 통일되어 저장되므로, 메모리 공간을 효율적으로 사용하며, 나중에 평균 계산이나 통계 분석과 같은 연산을 빠르게 수행할 수 있습니다.

**시험 포인트**

*   **NumPy Array의 핵심 특징**: ⭐모든 원소가 동일한 데이터 타입(`dtype`)을 가진다는 점과 0-기반 인덱싱을 사용한다는 점을 반드시 기억해야 합니다. 이는 파이썬 리스트와의 주요 차이점입니다.
*   **`shape` 속성**: ⭐NumPy 배열의 `shape`이 무엇을 의미하는지 (각 차원의 길이), 그리고 이를 어떻게 확인하는지 (`A.shape`) 이해해야 합니다. 특히 `axis 0`과 `axis 1`이 각각 무엇을 가리키는지 (일반적으로 행과 열) 숙지해야 합니다.
*   **인덱싱**: ⭐다차원 배열에서 특정 원소에 접근하는 방법 (`A[row_index, col_index]`)을 정확히 이해하고, 0-기반 인덱싱 규칙에 따라 올바른 값을 찾아낼 수 있어야 합니다. (예: `A[1, 2]`가 어떤 값을 가리키는가?)
*   **배열 생성**: `np.array()` 함수를 사용하여 파이썬 리스트로부터 NumPy 배열을 생성하는 방법과 `dtype` 인자의 사용법을 알아야 합니다.

---
## Slide 6

## NumPy Array: Metadata vs. Elements (1/2)

### 핵심 개념

NumPy 배열은 데이터 자체뿐만 아니라 데이터를 설명하는 여러 속성(metadata)을 가지고 있습니다. 이 슬라이드는 NumPy 배열을 구성하는 핵심적인 **메타데이터(metadata)**와 실제 **요소(elements)** 및 그 접근 방식에 대한 수학적/개념적 정의를 다룹니다.

*   **메타데이터(Fixed parameters)**:
    *   **랭크(Rank)**: 배열의 차원 수 (number of axes). `n`으로 표현됩니다. 예를 들어, 스칼라는 랭크 0, 벡터는 랭크 1, 행렬은 랭크 2입니다.
    *   **형태(Shape)**: 각 차원의 길이를 나타내는 튜플 `(s1, s2, ..., sn)`입니다. `sk`는 k번째 축의 길이를 의미합니다. 이를 통해 배열의 '모양'과 크기를 알 수 있습니다.
    *   **데이터 타입(Data Type, dtype)**: 배열 내 모든 요소의 데이터 타입을 지정합니다. `int64`, `float64` 등 특정 값 도메인($\mathcal{V}_\tau$)을 가집니다. NumPy 배열의 중요한 특징 중 하나는 모든 요소가 동일한 데이터 타입을 가져야 한다는 것입니다.
*   **요소 및 의미론(Index set and semantics)**:
    *   **인덱스 집합(Index set)**: 배열 내의 특정 요소에 접근하기 위한 유효한 인덱스들의 집합입니다. 각 차원의 길이에 따라 `0`부터 `길이-1`까지의 정수 인덱스로 구성됩니다.
    *   **배열 인스턴스(Array instance)**: 특정 형태와 데이터 타입을 가진 실제 배열은 인덱스 집합의 각 인덱스를 데이터 타입의 값 도메인으로 매핑하는 함수로 볼 수 있습니다. 즉, 각 인덱스에 해당하는 특정 값을 저장합니다.

### 코드/수식 해설

*   **랭크(Rank)**: 배열의 차원 수를 나타내는 자연수.
    $n \in \mathbb{N}$
*   **형태(Shape)**: 각 축의 길이를 나타내는 튜플. $s_k$는 $k$번째 축의 길이를 의미하며, $1$ 이상의 자연수입니다.
    $s = (s_1, \dots, s_n)$
*   **데이터 타입(Data type, dtype)**: 배열 요소의 타입 $\tau$와 그 값 도메인 $\mathcal{V}_\tau$ (예: `int64`, `float64`).
*   **인덱스 집합(Index set)**: 주어진 형태 $s=(s_1, \dots, s_n)$에 대한 유효한 인덱스들의 집합. 각 $i_k$는 $k$번째 축의 인덱스이며, $0$부터 $s_k-1$까지의 정수입니다.
    $I_s = \{ i = (i_1, \dots, i_n) \in \mathbb{Z}^n \mid 0 \le i_k < s_k \forall k \}$
*   **배열들의 우주(Universe of arrays)**: 주어진 형태 $s$와 데이터 타입 $\tau$를 가지는 모든 가능한 배열들의 집합.
    $\mathcal{V}_\tau^{I_s} = \prod_{i \in I_s} \mathcal{V}_\tau$
*   **특정 배열 인스턴스(A particular array instance)**: 실제 배열 $A$는 인덱스 집합 $I_s$에서 값 도메인 $\mathcal{V}_\tau$로의 함수로 볼 수 있습니다.
    $A \in \mathcal{V}_\tau^{I_s}$ (equivalently, $A : I_s \to \mathcal{V}_\tau$)
*   **요소 값(Element values)**: 인덱스 집합 $I_s$의 임의의 인덱스 $i$에 대해, 배열 $A$의 해당 요소 $A[i]$는 값 도메인 $\mathcal{V}_\tau$에 속합니다.
    For $i \in I_s$, $A[i] \in \mathcal{V}_\tau$.

```python
import numpy as np

# 2x3 행렬 (rank 2) 생성
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# 메타데이터 확인
print(f"Rank (ndim): {arr.ndim}")        # 출력: 2
print(f"Shape: {arr.shape}")             # 출력: (2, 3)
print(f"Data type (dtype): {arr.dtype}") # 출력: int64 (혹은 시스템에 따라 int32)

# 요소 접근 (인덱스 집합 내의 인덱스 사용)
print(f"Element at (0, 1): {arr[0, 1]}") # 출력: 2
print(f"Element at (1, 2): {arr[1, 2]}") # 출력: 6
# print(arr[0, 3]) # IndexError 발생 - 인덱스 집합을 벗어남
```

### 구체적 예시

**예시 1: 성적표 배열**
여러 학생의 과목별 성적을 저장하는 NumPy 배열을 생각해 봅시다.

```python
import numpy as np

# 3명의 학생, 4개의 과목 성적 (가상의 데이터)
# 학생 A: 90, 85, 92, 78
# 학생 B: 75, 80, 88, 95
# 학생 C: 82, 90, 70, 85
grades = np.array([
    [90, 85, 92, 78],
    [75, 80, 88, 95],
    [82, 90, 70, 85]
], dtype=np.float64) # 성적은 소수점 가능성이 있으므로 float64로 저장

# 메타데이터
print(f"성적표 배열의 랭크 (ndim): {grades.ndim}")   # 출력: 2 (2차원: 학생, 과목)
print(f"성적표 배열의 형태 (shape): {grades.shape}") # 출력: (3, 4) (3명의 학생, 4개의 과목)
print(f"성적표 배열의 데이터 타입 (dtype): {grades.dtype}") # 출력: float64

# 요소 접근 (인덱스 집합 활용)
# 학생 B의 3번째 과목 성적 (인덱스 (1, 2))
student_b_subject_3_grade = grades[1, 2]
print(f"학생 B의 3번째 과목 성적: {student_b_subject_3_grade}") # 출력: 88.0

# 이처럼 (1, 2)는 grades 배열의 인덱스 집합 I_s 에 포함되는 유효한 인덱스이며,
# grades[1, 2]의 값 88.0은 float64 값 도메인 V_float64 에 속합니다.
```

**예시 2: 실생활 비유 - 도서관 책장**
도서관의 책장을 NumPy 배열에 비유해 볼 수 있습니다.
*   **랭크**: 책장의 차원 수 (예: 층수, 열 수).
*   **형태**: `(층수, 열수)` 튜플. 예를 들어, `(5, 10)`은 5층짜리 책장이 각 층마다 10열을 가지고 있음을 의미합니다.
*   **데이터 타입**: 각 책장에 어떤 종류의 책(소설, 전공서적, 만화 등)만 들어갈 수 있는지 정해진 규칙. 예를 들어, '전공 서적' 타입으로 지정되면 해당 책장에는 전공 서적만 꽂힐 수 있습니다.
*   **인덱스 집합**: 특정 책을 찾기 위한 주소(예: '3층 5열'). 이 주소는 책장의 형태에 따라 유효한 범위 내에 있어야 합니다.
*   **요소**: 실제로 책장에 꽂혀있는 개별 책들. 이 책들은 정해진 데이터 타입(규칙)을 따라야 합니다.

### 시험 포인트

*   ⭐ **NumPy 배열의 세 가지 핵심 메타데이터** (랭크, 형태, 데이터 타입)를 정확히 이해하고 설명할 수 있어야 합니다.
*   ⭐ **랭크(ndim)**와 **형태(shape)**의 차이점을 명확히 구분할 수 있어야 합니다. (랭크는 차원의 *수*, 형태는 각 차원의 *길이*).
*   ⭐ **데이터 타입(dtype)**이 NumPy 배열에서 가지는 중요성(동질성)과 그 역할에 대해 설명할 수 있어야 합니다. (모든 요소가 동일한 타입)
*   ⭐ **인덱스 집합**이 배열의 형태에 의해 어떻게 결정되는지, 그리고 유효한 인덱스 범위($0 \le i_k < s_k$)를 이해하고 적용할 수 있어야 합니다.
*   주어진 NumPy 배열의 `ndim`, `shape`, `dtype` 속성을 코드로 확인하고 해석하는 문제가 출제될 수 있습니다.
*   배열의 메타데이터와 실제 요소 값 간의 관계를 비유나 구체적인 예시로 설명하는 문제가 나올 수 있습니다.

---
## Slide 7

**핵심 개념**:
NumPy 배열의 메모리 구현은 내부적으로 $(s, \tau, \sigma, p)$ 네 가지 핵심 정보로 구성됩니다. 이 정보들을 통해 다차원 배열의 원소들이 실제 메모리에 어떻게 배치되고 접근되는지 정의합니다.

*   **$s$ (shape)**: 배열의 각 차원(axis)의 크기를 나타냅니다. 예를 들어, `(2, 3)`은 2행 3열 배열을 의미합니다. (슬라이드에는 `Is`로 간접 언급)
*   **$\tau$ (dtype, itemsize)**: 배열 원소의 데이터 타입(예: `int32`, `float64`)과 각 원소가 차지하는 바이트 크기(`itemsize`)를 정의합니다.
*   **$\sigma = (\sigma_1, \dots, \sigma_n)$ (strides)**: 각 차원을 따라 인덱스를 1 증가시킬 때 메모리 주소가 얼마나 많은 바이트만큼 건너뛰어야 하는지를 나타냅니다. 이는 `byte strides`라고도 불립니다.
*   **$p$ (base address)**: 배열의 첫 번째 원소 $A[0, \dots, 0]$가 시작되는 메모리 주소입니다.

NumPy는 이 정보를 활용하여 어떠한 다차원 배열의 원소라도 상수 시간 $O(1)$에 접근할 수 있도록 설계되었습니다.

**코드/수식 해설**:

NumPy 배열 $A$의 임의의 인덱스 $i = (i_1, i_2, \dots, i_n)$에 해당하는 원소 $A[i_1, i_2, \dots, i_n]$의 메모리 주소 $\text{addr}(i)$는 다음과 같은 공식으로 계산됩니다.

$$ \text{addr}(i) = p + \sum_{k=1}^n i_k \sigma_k $$

*   $p$: 배열의 시작 메모리 주소. Python에서는 `arr.__array_interface__['data'][0]`으로 확인 가능합니다.
*   $i_k$: $k$-번째 차원의 인덱스 값.
*   $\sigma_k$: $k$-번째 차원의 stride 값. Python에서는 `arr.strides[k-1]`으로 확인 가능합니다.

**stride $\sigma_k$의 정의**:
$k$-번째 축을 따라 인덱스를 1 증가시킬 때, 메모리 주소의 변화량(바이트 단위)을 의미합니다. 이때 다른 모든 축의 인덱스는 고정됩니다.

$$ \sigma_k = \text{addr}(i + e_k) - \text{addr}(i) $$

여기서 $e_k$는 $k$-번째 위치만 1이고 나머지는 0인 표준 기저 벡터입니다.

**구체적 예시**:

2행 3열의 `int64` (8바이트) 배열 `arr_2d`를 가정해 봅시다.

```python
import numpy as np

# 2행 3열 int64 (8바이트) 배열 생성 (C-contiguous, 행 우선)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int64)

print(f"배열:\n{arr_2d}")
print(f"데이터 타입 (dtype): {arr_2d.dtype}")
print(f"원소 크기 (itemsize): {arr_2d.itemsize} bytes") # 각 원소는 8바이트
print(f"스트라이드 (strides): {arr_2d.strides}")
print(f"기본 주소 (base address, p): {arr_2d.__array_interface__['data'][0]}")

# strides 해석: (24, 8)
# - 첫 번째 차원 (행)의 stride = 24 바이트: 한 행을 건너뛰려면 24바이트를 이동해야 합니다.
#   (이는 3개 열 * 8바이트/원소 = 24바이트와 같습니다.)
# - 두 번째 차원 (열)의 stride = 8 바이트: 한 열을 건너뛰려면 8바이트를 이동해야 합니다.
#   (이는 1개 원소 * 8바이트/원소 = 8바이트와 같습니다.)

# 예시: arr_2d[1, 0] (값 4)의 메모리 주소 계산
# 인덱스 i = (1, 0)
# p = arr_2d.__array_interface__['data'][0]
# sigma_1 = arr_2d.strides[0] = 24
# sigma_2 = arr_2d.strides[1] = 8

p = arr_2d.__array_interface__['data'][0]
sigma_row = arr_2d.strides[0] # 24
sigma_col = arr_2d.strides[1] # 8

# addr(1, 0) = p + (1 * sigma_row) + (0 * sigma_col)
addr_1_0 = p + (1 * sigma_row) + (0 * sigma_col)
print(f"\n계산된 arr_2d[1, 0]의 주소: {addr_1_0}")

# 예시: arr_2d[0, 2] (값 3)의 메모리 주소 계산
# addr(0, 2) = p + (0 * sigma_row) + (2 * sigma_col)
addr_0_2 = p + (0 * sigma_row) + (2 * sigma_col)
print(f"계산된 arr_2d[0, 2]의 주소: {addr_0_2}")
```

**시험 포인트**:

*   ⭐ NumPy 배열의 메모리 구현을 구성하는 4가지 핵심 요소 ($s, \tau, \sigma, p$)를 정확히 설명할 수 있어야 합니다. 특히 **`p` (base address)**와 **`$\sigma$` (strides)**의 역할이 중요합니다.
*   ⭐ 임의의 다차원 인덱스 $(i_1, \dots, i_n)$에 대한 배열 원소의 메모리 주소를 계산하는 공식을 정확히 작성하고 각 항의 의미를 설명할 수 있어야 합니다: $\text{addr}(i) = p + \sum_{k=1}^n i_k \sigma_k$.
*   ⭐ NumPy에서 원소 접근 비용이 **$O(1)$**인 이유와 이것이 고성능 수치 연산에 미치는 중요성을 설명할 수 있어야 합니다. (배열 크기와 상관없이 항상 일정한 시간 내에 원소에 접근 가능)
*   ⭐ `strides`의 개념을 이해하고, `np.ndarray.strides` 속성을 통해 배열의 메모리 레이아웃을 파악하는 방법을 알아야 합니다. C-contiguous(행 우선)와 Fortran-contiguous(열 우선) 배열에서 `strides` 값이 어떻게 달라지는지 설명할 수 있어야 합니다.

---
## Slide 8

## NumPy 배열의 형식적 정의 이해: `shape`, `dtype`, `strides`

이 슬라이드는 NumPy 배열의 내부 구조를 이해하기 위한 핵심 속성들을 다룹니다. 배열의 차원, 데이터 타입, 그리고 메모리 상에서의 데이터 배치 방식(`strides`)을 구체적인 예시 코드를 통해 확인합니다.

---

### **핵심 개념**

*   **배열의 기본 속성**:
    *   `shape`: 배열의 각 차원(축)의 크기를 튜플 형태로 나타냅니다. (예: `(3, 4)`는 3행 4열).
    *   `ndim`: 배열의 차원 수(axis의 개수)를 나타냅니다.
    *   `size`: 배열의 전체 원소 개수를 나타냅니다. `shape`의 모든 원소를 곱한 값과 같습니다.
    *   `dtype`: 배열 원소의 자료형을 나타냅니다. (예: `np.int32`).
    *   `itemsize`: 배열의 각 원소가 차지하는 메모리 크기(바이트)를 나타냅니다.
*   **`strides`**: NumPy 배열의 가장 중요한 내부 속성 중 하나로, 각 차원에서 다음 원소로 이동하기 위해 건너뛰어야 할 바이트 수를 나타내는 튜플입니다.
    *   `strides`는 메모리 효율적인 데이터 접근 방식과 직접적으로 연관됩니다.
*   **메모리 연속성 (Memory Contiguity)**:
    *   **C-contiguous (Row-major order)**: C/Python에서 기본적으로 사용하는 방식으로, 마지막 차원의 인덱스가 가장 빠르게 변하면서 메모리에 연속적으로 저장됩니다. 즉, 행 단위로 메모리에 붙어 있습니다.
    *   **F-contiguous (Column-major order)**: Fortran에서 주로 사용하는 방식으로, 첫 번째 차원의 인덱스가 가장 빠르게 변하면서 메모리에 연속적으로 저장됩니다. 즉, 열 단위로 메모리에 붙어 있습니다.

---

### **코드/수식 해설**

아래 코드는 3행 4열의 `int32` 배열 `X`와 그에 상응하는 F-contiguous 배열 `XF`를 생성하고, 다양한 속성들을 출력하며 그 의미를 설명합니다.

```python
import numpy as np

# 1. C-contiguous (행-우선) 배열 생성
X = np.arange(12, dtype=np.int32).reshape(3, 4, order='C')
# X는 다음과 같은 2D 배열이 됨:
# [[ 0,  1,  2,  3],
#  [ 4,  5,  6,  7],
#  [ 8,  9, 10, 11]]

# 2. F-contiguous (열-우선) 배열 생성
XF = np.asfortranarray(X)
# XF는 X와 동일한 값을 가지지만 메모리 저장 방식이 다름

# 3. 기본 속성 확인
print("shape:", X.shape, "ndim:", X.ndim, "size:", X.size)
# 출력: shape: (3, 4) ndim: 2 size: 12
# 해설: 3행 4열, 2차원, 총 12개의 원소

print("dtype:", X.dtype, "itemsize:", X.itemsize)
# 출력: dtype: int32 itemsize: 4
# 해설: 각 원소는 32비트 정수이며, 4바이트의 메모리를 차지

# 4. C-contiguous 배열의 strides 및 연속성 확인
print("strides (C):", X.strides, "C-contig?", X.flags['C_CONTIGUOUS'])
# 출력: strides (C): (16, 4) C-contig? True
# 해설:
#   - 첫 번째 차원(행)에서 다음 행으로 이동하려면 16바이트를 건너뛰어야 함. (4열 * 4바이트/원소 = 16)
#   - 두 번째 차원(열)에서 다음 열으로 이동하려면 4바이트를 건너뛰어야 함. (1원소 * 4바이트/원소 = 4)
#   - 'C_CONTIGUOUS' 플래그가 True이므로 C-contiguous 배열임.

# 5. F-contiguous 배열의 strides 및 연속성 확인
print("strides (F):", XF.strides, "F-contig?", XF.flags['F_CONTIGUOUS'])
# 출력: strides (F): (4, 12) F-contig? True
# 해설:
#   - 첫 번째 차원(행)에서 다음 행으로 이동하려면 4바이트를 건너뛰어야 함. (1원소 * 4바이트/원소 = 4)
#   - 두 번째 차원(열)에서 다음 열으로 이동하려면 12바이트를 건너뛰어야 함. (3행 * 4바이트/원소 = 12)
#   - 'F_CONTIGUOUS' 플래그가 True이므로 F-contiguous 배열임.

# 6. shape와 size의 관계 확인
prod = 1
for s in X.shape:
    prod *= s
print("product(shape) == size ?", prod == X.size)
# 출력: product(shape) == size ? True
# 해설: shape 튜플의 원소들을 곱한 값(3 * 4 = 12)은 배열의 총 원소 개수(12)와 일치합니다.
```

**`strides` 계산 공식 (2차원 배열의 경우)**:
배열의 `shape`이 $(R, C)$이고 `itemsize`가 $S$ 바이트일 때:
*   **C-contiguous (Row-major)**:
    *   첫 번째 차원(행) stride: $C \times S$ 바이트
    *   두 번째 차원(열) stride: $1 \times S$ 바이트
    *   즉, `strides`는 $(C \times S, S)$
*   **F-contiguous (Column-major)**:
    *   첫 번째 차원(행) stride: $1 \times S$ 바이트
    *   두 번째 차원(열) stride: $R \times S$ 바이트
    *   즉, `strides`는 $(S, R \times S)$

---

### **구체적 예시**

NumPy 배열을 아파트 단지에 비유해 볼 수 있습니다. 각 아파트 호수가 배열의 원소이고, 아파트가 배열 자체입니다.

*   **`shape`**: "3개 동, 각 동에 4개 층이 있는 단지"와 같습니다. (3, 4)
*   **`size`**: "총 12개의 호실(원소)이 있습니다."
*   **`itemsize`**: "각 호실의 면적이 4평입니다." (바이트 단위)

**`strides` 비유**:
여러분은 아파트 단지 관리인입니다.
*   **C-contiguous (행-우선)**: 옆 호실로 이동하는 것이 더 쉽고 가깝습니다. 같은 층에서는 4평만 옆으로 가면 되고, 다음 동으로 가려면 아래층에 해당하는 4개 호실을 다 건너뛰어야 합니다 (16평).
    *   `X[0,0]` (1동 1층) 에서 `X[0,1]` (1동 2층) 로 가려면 4바이트 (4평)만 이동.
    *   `X[0,0]` (1동 1층) 에서 `X[1,0]` (2동 1층) 으로 가려면 16바이트 (16평) 이동.
*   **F-contiguous (열-우선)**: 아래층 호실로 이동하는 것이 더 쉽고 가깝습니다. 같은 동에서는 4평만 아래로 가면 되고, 다음 동으로 가려면 해당 동의 모든 층(3개 호실)을 다 건너뛰어야 합니다 (12평).
    *   `XF[0,0]` (1동 1층) 에서 `XF[1,0]` (2동 1층) 으로 가려면 4바이트 (4평)만 이동.
    *   `XF[0,0]` (1동 1층) 에서 `XF[0,1]` (1동 2층) 으로 가려면 12바이트 (12평) 이동.

이처럼 `strides` 값은 메모리 상에서 원소들이 어떻게 배치되어 있는지, 그리고 특정 원소에 접근하기 위해 얼마나 건너뛰어야 하는지를 직접적으로 나타냅니다.

---

### **시험 포인트**

*   ⭐**`shape`, `ndim`, `size`, `dtype`, `itemsize`**가 각각 배열의 어떤 정보를 나타내는지 명확히 설명할 수 있어야 합니다.
*   ⭐**`strides`의 개념**을 정확히 이해하고, 주어진 `shape`과 `itemsize`를 바탕으로 **C-contiguous 및 F-contiguous 배열의 `strides` 값을 계산**할 수 있어야 합니다. (특히 2차원 배열).
*   ⭐**C-contiguous (행-우선)**와 **F-contiguous (열-우선)** 메모리 레이아웃의 **차이점**을 설명하고, 각각이 어떤 언어/환경에서 주로 사용되는지 이해해야 합니다. NumPy에서 `order='C'`와 `order='F'` 옵션의 의미를 파악하는 것이 중요합니다.
*   ⭐**`X.flags['C_CONTIGUOUS']`**와 같은 플래그를 통해 배열의 메모리 연속성 상태를 확인하는 방법을 알아야 합니다.

---
## Slide 9

**핵심 개념**

*   **NumPy 배열의 메모리 소유권**: NumPy 배열은 `base` 속성을 통해 메모리 소유 관계를 나타냅니다. `base`가 `None`이면 해당 배열이 데이터를 직접 소유하며(원본), `None`이 아니면 다른 배열의 메모리를 공유하는 **뷰(view)**입니다. 슬라이딩이나 `reshape` 연산은 종종 뷰를 생성합니다.
*   **뷰(View) vs. 복사(Copy)**:
    *   **뷰**: 원본 배열의 메모리를 공유합니다. 뷰의 데이터를 변경하면 원본 배열의 데이터도 변경됩니다. `base` 속성은 항상 데이터의 가장 원본이 되는 메모리 소유자 배열을 가리킵니다.
    *   **복사 (Deep Copy)**: `copy()` 메서드를 통해 생성되며, 원본과 완전히 독립적인 새로운 메모리 공간에 데이터를 저장합니다. 복사본을 변경해도 원본은 영향을 받지 않습니다. `base` 속성이 `None`입니다.
*   **스트라이드(Strides)**: 배열의 각 차원을 따라 다음 요소로 이동할 때 건너뛰어야 할 바이트 수를 나타내는 튜플입니다. C-order(행 우선) 배열의 경우 `(열_개수 * itemsize, itemsize)` 형태를 가집니다. 이 값들을 이용하여 특정 인덱스의 요소가 메모리상 어디에 위치하는지 계산할 수 있습니다.
*   **전치(Transpose)**: NumPy에서 배열을 전치(`X.T`)하는 것은 대부분의 경우 실제 데이터를 메모리에서 재배치하지 않고, `shape`와 `strides` 속성만 교환하여 뷰를 생성합니다. 이는 메모리 효율성을 높이는 중요한 특징입니다.

**코드/수식 해설**

```python
import numpy as np

# 1. 3x4 크기의 int32 배열 X 생성
# np.arange(12)로 생성된 1D 배열을 3x4로 재구성하며, C-order(행 우선)로 저장됩니다.
# X는 내부적으로 np.arange(12)의 결과물인 1D 배열의 뷰로 간주될 수 있습니다.
X = np.arange(12, dtype=np.int32).reshape(3, 4, order='C')
# X의 shape은 (3, 4), 각 요소는 4바이트(int32).
# C-order이므로 strides는 (4열 * 4바이트, 4바이트) = (16, 4)입니다.
# 즉, 행을 바꿀 때 16바이트, 열을 바꿀 때 4바이트 이동합니다.

# 2. X의 뷰 V 생성 (스트라이드 슬라이싱)
# X의 0, 2번째 행과 0, 2번째 열을 선택하여 V를 생성합니다.
# V는 X의 메모리 일부를 공유하는 뷰입니다.
V = X[::2, ::2]

# 3. X의 딥 복사 C 생성
# X의 모든 데이터를 새로운 메모리 공간에 복사하여 C를 생성합니다.
C = X.copy()

# 4. `.base` 속성을 이용한 메모리 소유 관계 검증
# X는 np.arange(12)로 생성된 1D 배열의 뷰이므로, base는 None이 아닙니다.
print("X.base is None?", X.base is None) # False

# V의 base는 중간 뷰인 X가 아니라, X의 base와 동일한 가장 원본 메모리 소유자(np.arange(12)의 결과물)를 가리킵니다.
print("V.base is X?", V.base is X)       # False (V.base is X.base는 True)

# C는 X의 복사본이므로 독립적인 메모리를 소유하며, base는 None입니다.
print("C.base is None?", C.base is None) # True

# 5. 메모리 주소 공식 검증
# X의 첫 번째 요소의 메모리 주소를 가져옵니다.
data = X.ctypes.data
i, j = 2, 1 # 검증할 요소의 인덱스 (X[2, 1])

# 주어진 인덱스 (i, j)의 요소 메모리 주소를 스트라이드를 이용하여 계산합니다.
# Address(i, j) = base_address + i * strides[0] + j * strides[1]
expected = data + i * X.strides[0] + j * X.strides[1]

# 실제 X[i, j] 요소의 메모리 주소를 1x1 슬라이싱을 통해 얻습니다.
addr_ij = X[i:i+1, j:j+1].ctypes.data

# 계산된 주소와 실제 주소가 일치하는지 확인합니다.
print("address formula holds?", addr_ij == expected) # True
```
2차원 배열 `A`에서 인덱스 $(i, j)$에 해당하는 요소의 메모리 주소는 다음 수식으로 계산됩니다:
$$ \text{Address}(i, j) = A_{\text{base}} + i \cdot A.\text{strides}[0] + j \cdot A.\text{strides}[1] $$
여기서 $A_{\text{base}}$는 배열 `A`의 첫 번째 요소 메모리 주소입니다.

```python
# 6. 전치(Transpose) 연산 확인
# X.T는 X의 shape과 strides를 교환하여 뷰를 생성합니다.
XT = X.T
print("X.T shape:", XT.shape, "strides:", XT.strides)
# X.shape=(3, 4), X.strides=(16, 4)
# XT.shape=(4, 3), XT.strides=(4, 16)
# shape과 strides가 서로 교환된 것을 확인할 수 있습니다.
```

**구체적 예시**

도서관에 책이 꽂힌 큰 서가가 있다고 상상해 봅시다.
*   **원본 배열 (X)**: 이 서가 전체가 `X`입니다. 모든 책이 장르와 저자 순서로 깔끔하게 정리되어 있습니다. `X`는 사실 도서관에 새로 책을 배치한 것이 아니라, 기존에 분류되지 않은 책더미(1D `np.arange` 결과)를 정돈하여 보여주는 "정돈된 뷰"일 수 있습니다. 그래서 `X.base`가 `None`이 아닙니다.
*   **뷰 (V)**: "최신 인기 소설 코너"입니다. 이 코너는 실제 책들을 따로 옮겨놓은 것이 아니라, 서가(`X`)에 있는 책들 중 특정 조건을 만족하는 책들만 가리키는 안내판 역할만 합니다. 이 코너에서 책을 빼면 서가에서도 책이 없어집니다. `V.base`가 `X`를 직접 가리키는 것이 아니라, 서가가 정돈되기 전의 원래 책더미를 가리키는 것은, 모든 뷰는 결국 가장 근원적인 데이터를 가리키기 때문입니다.
*   **복사본 (C)**: 당신이 관심 있는 책들의 목록을 만들어서 당신의 책상에 따로 복사본을 만들어 놓는 것입니다. 이 복사본은 서가의 책들과 완전히 독립적이므로, 당신이 복사본에 메모를 하거나 훼손해도 서가의 원본 책에는 아무런 영향이 없습니다. `C.base is None`은 이 목록이 완전히 새로운, 독립적인 정보임을 의미합니다.
*   **메모리 주소 공식 및 스트라이드**: 서가에서 특정 책(`X[i, j]`)의 정확한 위치를 찾는 방법입니다. "시작점부터 몇 번째 줄(i * strides[0])에 있고, 그 줄에서 몇 번째 칸(j * strides[1])에 있는지"를 계산하여 정확한 책의 위치를 찾아낼 수 있습니다.
*   **전치 (X.T)**: 서가의 책들을 물리적으로 옮기지 않고, '장르별-저자별' 진열 순서를 '저자별-장르별' 진열 순서로 바꾸는 안내판을 새로 만드는 것과 같습니다. 실제 책의 위치는 그대로지만, 책을 찾는 규칙(`shape`와 `strides`)만 바뀌는 것입니다.

**시험 포인트**

*   **⭐ `.base` 속성의 기능과 의미**: `base` 속성이 `None`인 경우와 특정 배열 객체를 가리키는 경우의 차이점, 즉 해당 배열이 메모리를 소유하는 원본인지 아니면 다른 배열의 뷰인지를 구분할 수 있어야 합니다. (슬라이싱, `reshape`가 뷰를 생성할 때 `.base`가 어떻게 동작하는지 이해)
*   **⭐ 뷰(View)와 복사(Copy)의 명확한 구분**: 두 연산의 결과가 메모리 소유권, 원본 데이터에 대한 영향, 생성 방식(`[:]` 슬라이싱, `.reshape()` vs. `.copy()`)에서 어떻게 다른지 정확히 설명할 수 있어야 합니다.
*   **⭐ NumPy 배열 요소의 메모리 주소 계산**: `base_address`, `strides`, 그리고 요소의 인덱스를 사용하여 특정 `(i, j)` 위치의 데이터가 메모리 상의 어느 주소에 저장되는지 계산하는 공식을 이해하고 적용할 수 있어야 합니다.
*   **⭐ 전치(Transpose) 연산의 특징**: `X.T`와 같은 전치 연산이 대부분의 경우 데이터를 물리적으로 재배치하지 않고 `shape`와 `strides`만 교환하여 뷰를 생성한다는 점과 그 메모리 효율성을 이해하는 것이 중요합니다.

---
## Slide 10

**핵심 개념**
*   **NumPy 배열 생성 방법**: Python의 리스트나 튜플로부터 `np.array()`를 사용하여 배열을 생성하거나, 특정 값(0, 1, 상수)으로 채워진 배열을 `np.zeros()`, `np.ones()`, `np.full()`로 생성할 수 있습니다. 특정 범위의 값으로 배열을 만들 때는 `np.arange()`를 사용합니다. `np.empty()`는 초기화되지 않은 메모리를 할당하여 배열을 생성합니다.
*   **메모리 복사(Copy) vs 뷰(View)**: NumPy 배열을 생성하거나 조작할 때, 원본 데이터를 복사하여 새로운 배열을 만들 수도 있고, 원본 데이터의 메모리를 공유하는 '뷰'를 생성할 수도 있습니다.
    *   `np.array()`는 기본적으로 항상 새로운 메모리를 할당하여 데이터를 복사합니다.
    *   `np.asarray()`는 가능하다면 원본 데이터의 메모리를 공유하는 뷰를 생성하고, 불가능하면 복사본을 생성합니다.
    *   뷰는 메모리 효율적이지만, 뷰를 변경하면 원본 데이터도 변경됩니다. 복사본은 안전하지만 메모리 오버헤드가 있습니다.
*   **배열의 주요 속성**:
    *   **Shape**: 배열의 각 차원(axis)의 길이를 나타내는 튜플입니다. 예를 들어 `(2, 3)`은 2행 3열의 2차원 배열을 의미합니다.
    *   **Dtype**: 배열 요소의 데이터 타입을 나타냅니다. `np.int16`, `np.float32`, `np.int32` 등이 있습니다. 모든 요소는 동일한 `dtype`을 가집니다.

**코드/수식 해설**

```python
import numpy as np

# 1. 리스트로부터 배열 생성 (복사)
a = np.array([[1, 2], [3, 4]], dtype=np.int16) # build from lists (copy)

# 2. arange를 이용한 배열 생성 및 재구성
b_src = np.arange(6, dtype=np.float32).reshape(2, 3)

# 3. 뷰(view) 생성: b_src의 메모리를 공유 (가능하다면)
b_view = np.asarray(b_src) # may be a view (no copy)

# 4. 강제 복사(copy) 생성: b_src의 데이터를 복사하여 새로운 배열 생성
b_copy = np.array(b_src) # forced copy

# 5. 특정 값으로 채워진 배열 생성
z = np.zeros((2, 3), dtype=np.int32)  # fill with 0s
o = np.ones((2, 3), dtype=np.int32)   # fill with 1s
f = np.full((2, 3), 7, dtype=np.int32) # fill with constant
e = np.empty((2, 3), dtype=np.int32)  # uninitialized data (메모리의 현재 값)

# 배열의 속성 출력
print("a:", a.shape, a.dtype)
print("b_view shares base?", b_view.base is b_src) # b_view가 b_src의 메모리를 공유하는지 확인 (True/False)
print("b_copy shares base?", b_copy.base is b_src) # b_copy가 b_src의 메모리를 공유하는지 확인 (True/False)
print("z/o/f/e shapes:", z.shape, o.shape, f.shape, e.shape)
```
*   `a = np.array([[1, 2], [3, 4]], dtype=np.int16)`: 2x2 크기의 정수형(16비트) 배열 `a`를 생성합니다. `dtype`을 지정하여 메모리 사용량을 최적화할 수 있습니다.
*   `b_src = np.arange(6, dtype=np.float32).reshape(2, 3)`: 0부터 5까지의 float32 타입 1차원 배열을 생성한 후, `(2, 3)` 형태의 2차원 배열로 재구성합니다.
*   `b_view = np.asarray(b_src)`: `b_src`와 같은 데이터를 가리키는 뷰 `b_view`를 생성합니다. 이 경우 `b_view`와 `b_src`는 동일한 메모리 주소를 공유하므로 `b_view.base is b_src`는 `True`를 반환합니다. `b_view`의 요소를 변경하면 `b_src`도 변경됩니다.
*   `b_copy = np.array(b_src)`: `b_src`의 내용을 완전히 복사하여 새로운 배열 `b_copy`를 생성합니다. `b_copy`는 `b_src`와 별도의 메모리를 사용하므로 `b_copy.base is b_src`는 `False`를 반환합니다. `b_copy`의 요소를 변경해도 `b_src`는 변경되지 않습니다.
*   `np.zeros((2, 3), dtype=np.int32)`: 모든 요소가 0인 2x3 정수형 배열을 생성합니다.
*   `np.ones((2, 3), dtype=np.int32)`: 모든 요소가 1인 2x3 정수형 배열을 생성합니다.
*   `np.full((2, 3), 7, dtype=np.int32)`: 모든 요소가 7인 2x3 정수형 배열을 생성합니다.
*   `np.empty((2, 3), dtype=np.int32)`: 2x3 크기의 정수형 배열을 위한 메모리 공간을 할당하지만, 초기화하지 않습니다. 따라서 해당 메모리 주소에 이전에 있던 "쓰레기" 값이 들어있을 수 있습니다. 이는 데이터를 즉시 덮어쓸 경우 성능 상의 이점을 제공합니다.
*   `.shape`: 배열의 차원 정보를 튜플 형태로 반환합니다.
*   `.dtype`: 배열 요소의 데이터 타입을 반환합니다.
*   `.base is other_array`: 두 배열이 같은 메모리 블록을 공유하는지 여부를 `True`/`False`로 반환합니다. (`.base` 속성은 배열이 다른 배열의 뷰인 경우 그 "기본" 배열을 가리킵니다. 기본 배열이 없는 경우 `None`입니다.)

**구체적 예시**
```python
import numpy as np

# 1. np.array로 리스트에서 배열 생성
my_list = [[10, 20], [30, 40]]
arr1 = np.array(my_list, dtype=np.float64)
print("arr1:\n", arr1)
print("arr1 shape:", arr1.shape, ", arr1 dtype:", arr1.dtype)

# 2. np.arange와 reshape로 배열 생성
arr2_src = np.arange(0, 10, 2) # [0, 2, 4, 6, 8]
arr2 = arr2_src.reshape(5, 1)
print("\narr2:\n", arr2)
print("arr2 shape:", arr2.shape, ", arr2 dtype:", arr2.dtype)

# 3. 메모리 복사 vs 뷰 예시
original_array = np.array([1, 2, 3])
view_array = np.asarray(original_array) # 뷰 생성
copy_array = np.array(original_array)    # 복사본 생성

print("\nOriginal:", original_array)
print("View shares base?", view_array.base is original_array) # True 출력
print("Copy shares base?", copy_array.base is original_array) # False 출력

# 뷰를 변경하면 원본도 변경됩니다.
view_array[0] = 99
print("Original after view change:", original_array) # [99, 2, 3]
print("View after view change:", view_array)       # [99, 2, 3]

# 복사본을 변경해도 원본은 변경되지 않습니다.
copy_array[0] = 100
print("Original after copy change:", original_array) # [99, 2, 3] (변화 없음)
print("Copy after copy change:", copy_array)         # [100, 2, 3]

# 4. zeros, ones, full, empty 예시
zeros_arr = np.zeros((2, 2))
ones_arr = np.ones((3, 1), dtype=np.int8)
full_arr = np.full((2, 4), 5.5)
empty_arr = np.empty((1, 3)) # 값은 예측 불가능

print("\nZeros array:\n", zeros_arr)
print("Ones array:\n", ones_arr)
print("Full array:\n", full_arr)
print("Empty array (uninitialized):\n", empty_arr)
```
**시험 포인트**
*   ⭐**`np.array()`와 `np.asarray()`의 핵심 차이점(복사 vs 뷰)을 이해하고 설명할 수 있어야 합니다.** 특히 `np.array()`는 항상 복사를 수행하고, `np.asarray()`는 가능하다면 뷰를 생성하여 메모리를 공유한다는 점을 기억하세요. `.base` 속성을 통해 메모리 공유 여부를 확인할 수 있습니다.
*   ⭐**`np.zeros()`, `np.ones()`, `np.full()`, `np.empty()` 각 함수의 용도와 차이점을 명확히 알고 있어야 합니다.** 특히 `np.empty()`가 초기화되지 않은 데이터를 포함한다는 점을 유의하세요.
*   ⭐**NumPy 배열의 `shape`와 `dtype` 속성이 무엇을 의미하는지 정확히 설명하고, 주어진 배열에 대해 이들을 확인할 수 있어야 합니다.**
*   메모리 복사와 뷰의 개념은 NumPy에서 매우 중요하며, 성능 최적화 및 의도치 않은 데이터 변경을 방지하는 데 필수적인 지식입니다. 이는 시험뿐만 아니라 실제 데이터 분석 작업에서도 계속해서 활용될 것입니다.

---
## Slide 11

## NumPy 배열 생성 루틴: 수학적 의미와 실제 사용

### 핵심 개념

NumPy는 다양한 방식으로 배열(array)을 생성하는 루틴을 제공하며, 각 루틴은 배열의 초기 내용과 속성(shape, dtype 등)을 결정합니다. 여기서 `s`는 배열의 형태(shape), `$\tau$`는 데이터 타입(dtype), `$\mathcal{V}_{\tau}$`는 해당 데이터 타입이 나타낼 수 있는 값의 집합을 의미합니다.

1.  **시퀀스로부터 배열 생성 (np.array, np.asarray)**
    *   Python의 중첩된 시퀀스(리스트 등)를 NumPy 배열로 변환합니다.
    *   내부 원소들은 지정된 `dtype` `$\tau$`의 값 집합 `$\mathcal{V}_{\tau}$`에 맞게 승격(promotion)되거나 변환(conversion)됩니다.
    *   **`np.array`**: 항상 새로운 배열 객체를 **복사(copy)**하여 반환합니다. 원본 데이터와 독립적입니다.
    *   **`np.asarray`**: 원본 데이터가 이미 `ndarray`이고 `dtype` 및 메모리 레이아웃이 일치하는 경우, 원본 배열에 대한 **뷰(view)**를 반환할 수 있습니다. 메모리 효율적이며, 뷰를 수정하면 원본도 변경될 수 있습니다.

2.  **특정 값으로 채워진 배열 생성 (Zeros/Ones/Full)**
    *   지정된 `shape` `s`를 가지며 모든 원소가 특정 값으로 초기화된 배열을 생성합니다.
    *   `np.zeros(s)`: 모든 원소가 `0`으로 초기화됩니다.
    *   `np.ones(s)`: 모든 원소가 `1`으로 초기화됩니다.
    *   `np.full(s, c)`: 모든 원소가 지정된 값 `c`로 초기화됩니다. `c`는 `$\mathcal{V}_{\tau}$`에 속하는 값이어야 합니다.

3.  **초기화되지 않은 배열 생성 (Empty)**
    *   `np.empty(s)`: 지정된 `shape` `s`를 가지는 배열을 생성하지만, 메모리 내용은 초기화되지 않은(unspecified) 상태입니다. 즉, 임의의 버퍼 내용(쓰레기 값)을 가질 수 있습니다. 이는 배열을 빠르게 할당하고 나중에 직접 값을 채울 때 유용합니다.

### 코드/수식 해설

**수식:**

*   `np.zeros(s)`의 원소 `X[i]`에 대한 수학적 정의:
    $$ X[i] = 0_{\tau} $$
*   `np.ones(s)`의 원소 `X[i]`에 대한 수학적 정의:
    $$ X[i] = 1_{\tau} $$
*   `np.full(s, c)`의 원소 `X[i]`에 대한 수학적 정의:
    $$ X[i] = c \in \mathcal{V}_{\tau} \quad (\forall i \in I_s) $$
    (여기서 $I_s$는 shape $s$를 가지는 배열의 유효한 인덱스 집합을 의미합니다.)

**코드:**

```python
import numpy as np

# 1. 시퀀스로부터 배열 생성
my_list = [1, 2, 3]
arr_copy = np.array(my_list) # 복사본 생성
arr_view = np.asarray(my_list) # 리스트의 경우 복사본이 생성될 수 있음

print(f"Original list: {my_list}")
print(f"np.array result: {arr_copy}")
print(f"np.asarray result: {arr_view}")

# np.asarray가 view를 반환하는 경우 (ndarray가 입력으로 들어올 때)
original_np_arr = np.array([10, 20, 30])
view_of_arr = np.asarray(original_np_arr) # view 반환 가능성이 높음 (dtype, layout 일치 시)

print(f"\nOriginal NumPy array: {original_np_arr}")
print(f"np.asarray view: {view_of_arr}")

# 2. 특정 값으로 채워진 배열 생성
# (2, 3) shape (2행 3열)의 0으로 채워진 배열
zeros_arr = np.zeros((2, 3))
print(f"\nZeros array:\n{zeros_arr}")

# (3,) shape (길이 3)의 1로 채워진 배열, dtype 지정
ones_arr = np.ones(3, dtype=int)
print(f"Ones array:\n{ones_arr}")

# (2, 2) shape의 7로 채워진 배열
full_arr = np.full((2, 2), 7)
print(f"Full array (filled with 7):\n{full_arr}")

# 3. 초기화되지 않은 배열 생성
# (2, 2) shape의 초기화되지 않은 배열
empty_arr = np.empty((2, 2))
print(f"\nEmpty array (contents are arbitrary):\n{empty_arr}")
```

### 구체적 예시

**np.array vs np.asarray의 차이:**

당신이 `original_data = [1, 2, 3]`이라는 리스트를 가지고 있다고 상상해봅시다.
*   `arr_a = np.array(original_data)`는 이 리스트의 내용을 복사하여 새로운 NumPy 배열 `arr_a`를 만듭니다. `original_data`가 변경되어도 `arr_a`는 변하지 않습니다.
*   `arr_b = np.asarray(original_data)` 역시 리스트로부터는 보통 복사본을 만듭니다. 하지만 만약 `original_data`가 이미 `np.array([1, 2, 3])`와 같은 NumPy 배열이었다면, `np.asarray`는 메모리 복사를 피하고 `original_data`를 "바라보는" 새로운 뷰 `arr_b`를 반환할 수 있습니다. 이 경우 `arr_b[0] = 99`와 같이 변경하면 `original_data[0]`도 99로 바뀝니다. 마치 같은 책을 두 사람이 같이 읽는 것과 같습니다. 한 사람이 밑줄을 그으면 다른 사람도 그 밑줄을 보게 됩니다.

**np.empty의 비유:**

`np.empty`는 새로 이사 갈 빈집을 짓는 것과 같습니다. 집은 완공되었지만, 아직 아무런 가구나 살림살이가 들어있지 않고, 심지어 이전 거주자가 남긴 벽의 낙서나 쓰레기가 그대로 남아있을 수 있습니다. 대신 가구를 채우는 비용(초기화 비용)이 들지 않으므로, 이삿짐을 바로 가져올 계획이라면 가장 빠르고 효율적인 방법입니다.

### 시험 포인트

*   ⭐ **`np.array`와 `np.asarray`의 주요 차이점**: `np.array`는 항상 복사본을 반환하지만, `np.asarray`는 가능한 경우 뷰(view)를 반환하여 메모리 사용을 최적화할 수 있습니다. 뷰를 반환할 경우 원본 데이터의 변경이 뷰에도 반영됩니다.
*   ⭐ **`np.zeros`, `np.ones`, `np.full`의 용도**: 각각 0, 1, 또는 특정 상수 값으로 배열을 초기화하는 함수임을 이해하고, `shape` 인자 전달 방법을 알아야 합니다.
*   ⭐ **`np.empty`의 특징**: 배열을 할당하지만 메모리를 초기화하지 않으므로, 배열의 내용이 예측 불가능한(garbage) 상태가 될 수 있습니다. 이는 성능 최적화를 위해 사용됩니다.
*   각 함수에 `dtype` 인자를 추가하여 데이터 타입을 명시적으로 지정할 수 있다는 점도 중요합니다.

---
## Slide 12

**핵심 개념**:
*   **`numpy.reshape()`**: NumPy 배열의 차원(shape)을 변경하는 함수입니다. 이 연산은 배열 내 원소들의 개수와 순서를 보존하며, 가능한 경우 원본 배열의 **뷰(view)**를 반환합니다. 뷰는 원본 데이터를 복사하지 않고, 동일한 메모리 공간을 다른 형태로 해석하여 사용하므로 매우 효율적입니다.
*   **`-1`을 이용한 차원 추론**: `reshape` 메서드를 사용할 때, 특정 차원의 크기를 `-1`로 지정하면 NumPy가 전체 원소 개수를 바탕으로 해당 차원의 크기를 자동으로 계산하여 추론합니다. 이는 편리하게 배열의 형태를 조절할 수 있도록 돕습니다.
*   **`order` 매개변수**: `reshape` 시 `order` 매개변수는 메모리 상에서 원소들을 어떻게 읽고 배치할 것인지를 결정합니다.
    *   `'C'` (C-style, row-major): 기본값으로, 가장 마지막 축(axis)의 인덱스가 가장 빠르게 변합니다. 행 우선 방식입니다.
    *   `'F'` (Fortran-style, column-major): 가장 첫 번째 축(axis)의 인덱스가 가장 빠르게 변합니다. 열 우선 방식입니다.
    이 설정은 배열의 `strides` (각 차원을 따라 다음 원소로 이동하기 위해 필요한 바이트 수)에 영향을 줄 수 있습니다.
*   **`ravel()` vs. `flatten()`**: 두 메서드 모두 다차원 배열을 1차원 배열로 평탄화(flatten)합니다.
    *   `numpy.ravel()`: 가능한 경우 원본 배열의 **뷰(view)**를 반환합니다. 만약 원본 배열의 메모리 레이아웃이 변경되어야 1차원으로 만들 수 있는 경우에만 복사본을 반환합니다. 뷰를 반환하는 경우, `ravel()` 결과에 대한 변경은 원본 배열에도 영향을 미칩니다.
    *   `numpy.flatten()`: **항상 새로운 복사본(copy)**을 반환합니다. 원본 배열과 완전히 독립적인 새로운 메모리 공간에 데이터를 저장합니다. 따라서 `flatten()` 결과에 대한 변경은 원본 배열에 영향을 미치지 않습니다.

**코드/수식 해설**:
```python
import numpy as np

# 0부터 11까지의 정수를 포함하는 1차원 배열 생성 (총 12개 원소)
# x의 shape은 (12,)
x = np.arange(12)

# x를 (3, 4) 형태로 재구성합니다.
# 일반적으로 reshape는 뷰를 반환하므로 A는 x의 메모리를 공유합니다.
A = x.reshape(3, 4)

# x를 (-1, 6) 형태로 재구성합니다. -1은 NumPy가 자동으로 차원을 추론하게 합니다.
# 전체 원소 개수가 12이고 열이 6개이므로, 행은 12/6 = 2가 됩니다.
# 따라서 B의 shape은 (2, 6)이 됩니다. B 역시 x의 뷰입니다.
B = x.reshape(-1, 6)

# x를 (3, 4) 형태로 재구성하되, order='F' (Fortran-style)를 사용합니다.
# 이는 메모리 상에서 원소를 읽고 배치하는 순서에 영향을 줍니다.
# C 역시 x의 뷰일 가능성이 높습니다.
C = x.reshape(3, 4, order='F')

# A를 1차원으로 평탄화합니다. ravel은 가능한 경우 뷰를 반환합니다.
# A의 메모리 레이아웃은 1차원으로 평탄화하기에 적합하므로 D는 A의 뷰입니다.
D = A.ravel()

# A를 1차원으로 평탄화합니다. flatten은 항상 복사본을 반환합니다.
# E는 A와 독립적인 새로운 배열입니다.
E = A.flatten()

# A, B, C의 shape을 출력합니다.
print(A.shape, B.shape, C.shape)
# 예상 출력: (3, 4) (2, 6) (3, 4)

# A가 원본 배열 x와 메모리 공간을 공유하는지 확인합니다.
# A.base는 배열이 뷰일 경우 원본 배열을 가리킵니다. x와 동일하면 True.
print("A shares base?", A.base is x)
# 예상 출력: A shares base? True (일반적으로 True)

# E (flatten 결과)가 복사본인지 확인합니다.
# E.base가 None이면 E가 독립적인 메모리를 소유하고 있다는 의미이며, 복사본입니다.
print("flatten is copy?", E.base is None)
# 예상 출력: flatten is copy? True
```

**구체적 예시**:
1.  **`reshape`의 뷰(view) 특성**:
    ```python
    import numpy as np
    original_arr = np.array([1, 2, 3, 4, 5, 6])
    reshaped_view = original_arr.reshape(2, 3)
    print(f"원본 배열: {original_arr}") # [1 2 3 4 5 6]
    print(f"재구성된 뷰: \n{reshaped_view}")
    # [[1 2 3]
    #  [4 5 6]]

    # 뷰를 통해 값을 변경하면 원본 배열에도 변경이 반영됩니다.
    reshaped_view[0, 0] = 99
    print(f"뷰 변경 후 원본 배열: {original_arr}") # [99  2  3  4  5  6]
    ```

2.  **`-1` 사용 예시**:
    ```python
    import numpy as np
    data = np.arange(15) # [0, 1, ..., 14]
    # 행의 개수는 자동으로 계산 (15 / 5 = 3), 열의 개수는 5로 지정
    matrix_auto_rows = data.reshape(-1, 5)
    print(f"shape: {matrix_auto_rows.shape}") # (3, 5)
    print(f"행 자동 추론 결과: \n{matrix_auto_rows}")
    # [[ 0  1  2  3  4]
    #  [ 5  6  7  8  9]
    #  [10 11 12 13 14]]
    ```

3.  **`ravel()`과 `flatten()`의 차이**:
    ```python
    import numpy as np
    multi_dim_arr = np.array([[1, 2, 3], [4, 5, 6]])

    # ravel(): 뷰를 반환 (원본과 메모리 공유)
    raveled_arr = multi_dim_arr.ravel()
    # flatten(): 복사본을 반환 (원본과 독립)
    flattened_arr = multi_dim_arr.flatten()

    raveled_arr[0] = 99 # 뷰를 변경하면 원본에도 영향
    print(f"ravel 변경 후 원본 배열: \n{multi_dim_arr}")
    # [[99  2  3]
    #  [ 4  5  6]]

    flattened_arr[0] = 100 # 복사본을 변경해도 원본에는 영향 없음
    print(f"flatten 변경 후 원본 배열: \n{multi_dim_arr}")
    # [[99  2  3] (변화 없음)
    #  [ 4  5  6]]
    ```

**시험 포인트**:
*   ⭐ **`reshape`가 가능한 경우 `view`를 반환한다는 사실**: 이는 메모리 효율성과 함께 뷰를 통한 데이터 변경이 원본 배열에 직접 영향을 미친다는 중요한 의미를 가집니다.
*   ⭐ **`-1`의 역할**: `reshape` 시 알지 못하는 한 차원의 크기를 NumPy가 자동으로 계산하도록 지시하는 편리한 기능입니다.
*   ⭐ **`ravel()`과 `flatten()`의 명확한 차이**:
    *   `ravel()`은 가능한 경우 `view`를 반환하여 메모리 효율적이지만, 원본 데이터와 연동됩니다.
    *   `flatten()`은 항상 `copy`를 생성하여 원본과 독립적이며 안전하지만, 메모리 오버헤드가 발생할 수 있습니다. 이 차이는 성능과 잠재적인 버그 발생 가능성 때문에 매우 중요합니다.
*   ⭐ **`order='C'` (행 우선)와 `order='F'` (열 우선)의 차이**: 다차원 배열의 메모리 상 데이터 배치 순서에 대한 이해는 고급 최적화 및 다른 언어(C/C++, Fortran)와의 연동 시 중요합니다.
*   `array.base` 속성을 활용하여 특정 배열이 다른 배열의 뷰인지(`base`가 원본 배열을 가리킴) 혹은 독립적인 복사본인지(`base`가 `None`)를 확인할 수 있습니다.

---
## Slide 13

---

### **핵심 개념**

NumPy 배열에 새로운 축(axis)을 추가하는 것은 배열의 차원(dimensionality)을 1만큼 늘리고, 이 새로운 축의 크기를 1로 만드는 과정입니다. 이는 주로 다음과 같은 목적을 가집니다:

1.  **브로드캐스팅(Broadcasting) 준비**: 서로 다른 차원의 배열 간에 연산을 수행하기 위해 차원 수를 일치시키거나 특정 축을 확장하여 NumPy의 브로드캐스팅 규칙을 활용합니다.
2.  **데이터 형식 맞추기**: 특정 라이브러리(예: scikit-learn)나 머신러닝 모델(예: 딥러닝 모델의 배치 입력)이 요구하는 입력 데이터 형식(shape)에 맞춰주기 위함입니다.
3.  **행 벡터/열 벡터 변환**: 1차원 배열을 2차원 행렬 연산(예: 내적)을 위해 2차원 행 벡터(`(1, N)`) 또는 열 벡터(`(N, 1)`)로 변환할 때 사용됩니다.

새로운 축을 추가하는 세 가지 주요 방법이 있으며, 슬라이드는 이러한 방법들을 "idioms"로 소개합니다: 슬라이싱과 `None`/`np.newaxis` 사용, `np.expand_dims()` 함수 사용, 그리고 `reshape()` 메서드 사용입니다.

---

### **코드/수식 해설**

이 슬라이드에서는 NumPy 배열의 형태(shape)를 조작하는 다양한 방법을 보여줍니다. 기본적인 1차원 배열 `v`와 2차원 배열 `M`을 생성한 후, 각 방법에 따라 어떻게 차원이 확장되는지 설명합니다.

```python
import numpy as np

v = np.arange(4) # v는 [0, 1, 2, 3]이며, shape는 (4,) 입니다.

# 1. 1차원 배열을 2차원 행 벡터 (1, 4)로 변환
# 기존 벡터 v: $v \in \mathbb{R}^4$ (shape: $(4,)$)
# 변환 후 행 벡터: $v_{row} \in \mathbb{R}^{1 \times 4}$ (shape: $(1, 4)$)
v_row1 = v[None, :]           # None을 사용하여 0번 축에 새 축 추가
v_row2 = v[np.newaxis, :]     # np.newaxis는 None의 명시적인 형태
v_row3 = np.expand_dims(v, axis=0) # np.expand_dims 함수 사용, axis=0에 새 축 추가
v_row4 = v.reshape(1, -1)     # reshape 사용, -1은 자동으로 차원 계산 (여기서는 4)

# 2. 1차원 배열을 2차원 열 벡터 (4, 1)로 변환
# 기존 벡터 v: $v \in \mathbb{R}^4$ (shape: $(4,)$)
# 변환 후 열 벡터: $v_{col} \in \mathbb{R}^{4 \times 1}$ (shape: $(4, 1)$)
v_col1 = v[:, None]           # None을 사용하여 마지막 축에 새 축 추가 (axis=1)
v_col2 = np.expand_dims(v, axis=1) # np.expand_dims 함수 사용, axis=1에 새 축 추가
v_col3 = v.reshape(-1, 1)     # reshape 사용, -1은 자동으로 차원 계산 (여기서는 4)

# 3. 2차원 배열에 새로운 축 삽입 (브로드캐스팅 또는 특정 데이터 형식 맞추기 위함)
M = np.arange(6).reshape(2, 3) # M은 [[0,1,2],[3,4,5]]이며, shape는 (2, 3) 입니다.
# 기존 행렬 M: $M \in \mathbb{R}^{2 \times 3}$ (shape: $(2, 3)$)

M0 = M[None, :, :] # 0번 축에 새 축 추가. (1, 2, 3). 'batch axis'로 사용.
# 변환 후 M0: $M_0 \in \mathbb{R}^{1 \times 2 \times 3}$ (shape: $(1, 2, 3)$)

M1 = M[:, None, :] # 1번 축에 새 축 추가. (2, 1, 3). 'pairwise-prep' (쌍별 비교)에 유용.
# 변환 후 M1: $M_1 \in \mathbb{R}^{2 \times 1 \times 3}$ (shape: $(2, 1, 3)$)

M2 = M[:, :, None] # 2번 축에 새 축 추가. (2, 3, 1). 'channel axis'로 사용.
# 변환 후 M2: $M_2 \in \mathbb{R}^{2 \times 3 \times 1}$ (shape: $(2, 3, 1)$)

print(v_row1.shape, v_col1.shape, M0.shape, M1.shape, M2.shape)
# 출력: (1, 4) (4, 1) (1, 2, 3) (2, 1, 3) (2, 3, 1)
```

*   **`None` / `np.newaxis`**: 배열 슬라이싱 시 인덱싱 위치에 `None` 또는 `np.newaxis`를 사용하면 해당 위치에 크기가 1인 새로운 축이 추가됩니다. 예를 들어, `v[None, :]`는 `v`의 0번 인덱스 위치에 새로운 축을 추가하여 `(4,)`를 `(1, 4)`로 만듭니다.
*   **`np.expand_dims(arr, axis)`**: 함수 형태로, 첫 번째 인자로 배열을 받고 두 번째 인자로 새로운 축을 삽입할 `axis` 번호를 지정합니다. `None`/`np.newaxis`와 기능적으로 동일하며, 더 명시적인 코드를 작성할 때 유용합니다.
*   **`arr.reshape(shape)`**: 배열의 총 요소 수는 유지하면서 형태를 변경할 때 사용합니다. `(1, -1)`이나 `(-1, 1)`처럼 `-1`을 사용하면 해당 차원의 크기가 자동으로 계산되어 편리합니다. `reshape`는 크기가 1인 축을 추가하는 것 외에도 다양한 형태 변경에 사용될 수 있는 강력한 메서드입니다.

---

### **구체적 예시**

1.  **행/열 벡터 변환**:
    *   `v = np.array([1, 2, 3])`와 같은 1차원 벡터를 다른 2차원 행렬과의 행렬 곱셈(`np.dot()` 또는 `@` 연산자)에 사용하려면, 이를 2차원 형태로 변환해야 할 때가 많습니다.
    *   예를 들어, `v.reshape(1, -1)`은 `[[1, 2, 3]]` 형태의 행 벡터를 만들고, `v.reshape(-1, 1)`은 `[[1], [2], [3]]` 형태의 열 벡터를 만듭니다. 이는 선형대수학에서 벡터와 행렬의 곱셈 규칙을 따르기 위함입니다.

2.  **브로드캐스팅을 위한 차원 확장**:
    *   두 개의 1차원 배열 `A = np.array([1, 2, 3])`와 `B = np.array([10, 20])`가 있을 때, `A`의 모든 요소와 `B`의 모든 요소 간의 차이를 계산하고 싶다고 가정해봅시다.
    *   `A[:, None] - B[None, :]` 와 같이 `A`를 `(3, 1)`로, `B`를 `(1, 2)`로 확장하면, NumPy의 브로드캐스팅 규칙에 의해 `(3, 2)` 형태의 결과 배열 `[[ -9, -19], [-8, -18], [-7, -17]]`을 얻을 수 있습니다. 이는 두 배열의 모든 쌍(pairwise)에 대한 연산을 효율적으로 수행하게 해줍니다.

3.  **머신러닝 입력 데이터 형식 맞추기**:
    *   **Batch Axis**: 딥러닝 모델(예: CNN)은 보통 `(batch_size, height, width, channels)`와 같은 4차원 입력을 받습니다. 만약 단일 이미지 `img` (shape: `(height, width, channels)`)를 모델에 입력하려면, `img[None, :, :, :]` 또는 `np.expand_dims(img, axis=0)`를 사용하여 `(1, height, width, channels)` 형태로 변환해야 합니다. 여기서 추가된 `1`은 배치 크기가 1임을 의미합니다.
    *   **Channel Axis**: 흑백 이미지의 경우 `(height, width)`와 같은 2차원 형태일 수 있습니다. 하지만 일부 모델은 `(height, width, 1)`과 같이 마지막에 채널 축을 기대할 수 있습니다. 이때 `img[:, :, None]` 또는 `np.expand_dims(img, axis=-1)`을 사용하여 채널 축을 추가할 수 있습니다.

---

### **시험 포인트**

*   ⭐ **`None` (또는 `np.newaxis`)과 `np.expand_dims`의 기능적 동등성**: 두 방법 모두 크기가 1인 새로운 축을 추가하는 데 사용되며, 어떤 상황에서 어떤 방법을 선호하는지 이해하는 것이 중요합니다 (간결성 vs. 명시성).
*   ⭐ **`reshape(1, -1)`과 `reshape(-1, 1)`을 이용한 행/열 벡터 변환의 의미**: 1차원 배열을 2차원 행 벡터 또는 열 벡터로 변환하는 가장 일반적이고 효율적인 방법임을 이해하고 있어야 합니다.
*   ⭐ **새로운 축을 추가하는 세 가지 방법(슬라이싱, `expand_dims`, `reshape`)의 차이점 및 적절한 사용 상황**: 각 방법의 문법적 특징과 어떤 목적에 더 적합한지 구분할 수 있어야 합니다.
*   ⭐ **브로드캐스팅을 위한 차원 조작의 중요성**: 왜 새로운 축을 추가해야 하는지, 그리고 이것이 어떻게 다른 차원의 배열 간 연산을 가능하게 하는지 이해하는 것이 핵심입니다. 특히 `(N,)` 배열을 `(N, 1)`이나 `(1, N)`으로 만들어 브로드캐스팅에 활용하는 예시를 기억하세요.
*   ⭐ **딥러닝에서 'batch axis', 'channel axis'와 같이 특정 위치에 축을 추가하는 이유**: 머신러닝/딥러닝 분야에서 데이터의 차원을 조작하는 것이 왜 필수적인지, 그리고 각 축이 일반적으로 어떤 의미를 가지는지 (예: 배치, 높이, 너비, 채널) 설명할 수 있어야 합니다.

---

---

## Slide 14

**핵심 개념**

*   **`keepdims=True`**: 배열 연산(예: `sum`, `mean`) 시 차원을 축소하더라도 해당 차원을 크기 1인 차원으로 유지합니다. 이는 나중에 브로드캐스팅(broadcasting)을 할 때 차원 수를 일치시켜 편리하게 연산할 수 있도록 돕습니다.
*   **`np.squeeze()`**: 배열에서 길이가 1인 차원(singleton dimension)을 제거합니다. 특정 `axis`를 지정하여 해당 축만 제거할 수도 있습니다. `keepdims=True`로 인해 생성된 불필요한 차원을 정리할 때 유용합니다.
*   **`np.swapaxes()`, `np.moveaxis()`, `arr.transpose()`**: 이 함수들은 배열의 축(axes) 순서를 재배열합니다.
    *   `swapaxes`: 두 개의 지정된 축의 위치를 서로 맞바꿉니다.
    *   `moveaxis`: 하나 이상의 원본 축을 지정된 대상 위치로 이동시킵니다. 다른 축들의 상대적 순서는 유지됩니다.
    *   `transpose`: 모든 축의 순서를 사용자가 지정한 순서로 완전히 재배열합니다.
*   **`np.atleast_2d()`, `np.atleast_3d()`**: 입력 배열이 최소한 지정된 수의 차원을 갖도록 만듭니다. 필요한 경우 차원 크기가 1인 축을 추가하여 차원을 확장합니다. 주로 브로드캐스팅을 위해 낮은 차원의 배열을 높은 차원의 배열과 호환시키고자 할 때 사용됩니다.

**코드/수식 해설**

```python
import numpy as np

# 기본 3차원 배열 생성 (2행, 3열, 4깊이)
X = np.arange(24).reshape(2, 3, 4)
# X의 초기 형태: (2, 3, 4)

# Reductions: keep singleton axes for safe broadcasting later
# axis=1을 기준으로 합계를 계산하고, keepdims=True로 해당 축을 유지
r = X.sum(axis=1, keepdims=True)  # 결과 형태: (2, 1, 4)
# axis=1 (두 번째 축, 크기 3)이 합계로 사라지지만, keepdims=True 때문에 크기 1의 축으로 유지됨.

# Remove size-1 axes explicitly
# r에서 axis=1인 크기 1의 축을 명시적으로 제거
r_squeeze = np.squeeze(r, axis=1) # 결과 형태: (2, 4)
# r에서 두 번째 축(크기 1)이 제거되어, 형태가 (2, 4)로 변경됨.

# Rearranging axes
# X의 0번 축과 1번 축을 맞바꿈
T1 = np.swapaxes(X, 0, 1) # 결과 형태: (3, 2, 4)
# (2, 3, 4) -> (3, 2, 4)

# X의 2번 축을 0번 위치로 이동
T2 = np.moveaxis(X, 2, 0) # 결과 형태: (4, 2, 3)
# (2, 3, 4) -> 2번 축(크기 4)이 0번으로 이동하여 (4, 2, 3)

# X의 축 순서를 (1, 0, 2)로 재배열
T3 = X.transpose(1, 0, 2) # 결과 형태: (3, 2, 4)
# (2, 3, 4) -> 1번 축(크기 3)이 0번, 0번 축(크기 2)이 1번, 2번 축(크기 4)이 2번으로.

# Quick promotion helpers
# 1차원 배열을 최소 2차원 배열로 만듦
a2 = np.atleast_2d(np.arange(3)) # 결과 형태: (1, 3)
# np.arange(3)은 (3,) 형태 -> (1, 3)으로 확장

# 1차원 배열을 최소 3차원 배열로 만듦
a3 = np.atleast_3d(np.arange(3)) # 결과 형태: (1, 3, 1)
# np.arange(3)은 (3,) 형태 -> (1, 3, 1)으로 확장
```

**구체적 예시**

예를 들어, 이미지 처리에서 여러 장의 흑백 이미지(2D 배열)를 배치로 다룰 때 각 이미지를 `(height, width, 1)` 형태로 만들고 싶을 수 있습니다. 여기서 마지막 `1`은 채널 수를 나타냅니다. 이때 `np.atleast_3d()`를 사용하면 `(height, width)` 형태의 2D 이미지를 `(1, height, width)` 또는 `(height, width, 1)` 등으로 쉽게 확장할 수 있습니다.

또 다른 예로, `keepdims=True`는 평균을 계산한 뒤 원래 배열과 브로드캐스팅 연산을 수행할 때 유용합니다. 3D 배열 `X`의 각 '슬라이스' 평균을 빼고 싶다고 가정해 봅시다.
`X.mean(axis=1)`은 `(2, 4)` 형태를 반환하지만, `X.mean(axis=1, keepdims=True)`는 `(2, 1, 4)` 형태를 반환합니다. 후자는 `X` (`(2, 3, 4)`)와 브로드캐스팅이 훨씬 자연스럽습니다. `X - X.mean(axis=1, keepdims=True)`는 각 슬라이스에서 해당 슬라이스의 평균을 뺄 수 있게 해줍니다.

**시험 포인트**

*   ⭐ `keepdims=True`의 역할과 `np.squeeze()`의 역할은 무엇이며, 이들이 어떻게 상호 보완적으로 사용될 수 있는지 이해해야 합니다. (특히 브로드캐스팅과 관련하여)
*   ⭐ `np.swapaxes()`, `np.moveaxis()`, `arr.transpose()`의 차이점을 명확히 구분하고, 주어진 배열과 축 변경 요청에 따라 어떤 함수를 사용해야 하는지, 그리고 결과 형태가 어떻게 되는지 파악할 수 있어야 합니다.
    *   `transpose`는 모든 축을 한 번에 재정의하는 데 적합하고, `swapaxes`는 두 축만 바꿀 때, `moveaxis`는 특정 축을 원하는 위치로 옮길 때 유용합니다.
*   ⭐ `np.atleast_nd()` 계열 함수들이 언제, 왜 필요한지 (특히 브로드캐스팅 시 차원 일치 목적) 이해하고 있어야 합니다. 예를 들어, 1차원 배열 `np.array([1, 2, 3])`을 `np.atleast_2d()`로 변환했을 때 `(1, 3)`이 되는지 `(3, 1)`이 되는지 혼동하지 않도록 주의해야 합니다. (기본적으로 첫 번째 축을 확장하는 방향으로 동작)

---
## Slide 15

**핵심 개념**:
이 슬라이드는 NumPy 라이브러리를 사용하여 1차원(1D) 좌표 배열을 생성하고, 이를 기반으로 2차원(2D) 격자(Grid) 구조 또는 특정 패턴의 2D 행렬을 구성하는 방법을 다룹니다. 이는 데이터 시각화, 머신러닝 모델의 입력 데이터 생성, 이미지 처리 등 다양한 분야에서 좌표계나 구조화된 데이터를 만드는 데 필수적인 기술입니다.

*   **1D 좌표 생성**: `np.arange`는 지정된 시작점부터 끝점 미만까지 고정된 간격으로 숫자를 생성하며, `np.linspace`는 지정된 시작점과 끝점(양 끝점 포함) 사이를 균등하게 나눈 특정 개수의 점들을 생성합니다.
*   **1D에서 2D 격자 변환 (브로드캐스팅)**: `np.newaxis`를 사용하여 1D 배열의 차원을 확장함으로써, 두 개의 1D 좌표 배열(`xs`, `ys`)을 브로드캐스팅 연산에 적합한 형태로 변환하고, 이를 결합하여 2D Cartesian 격자 좌표 (`X`, `Y`)를 생성할 수 있습니다. 이는 2차원 평면상의 모든 점의 x, y 좌표를 효율적으로 표현합니다.
*   **표준 2D 패턴 생성**: `np.eye`는 단위 행렬 또는 특정 대각선에 1을 채운 행렬을 생성하며, `np.diag`는 주어진 1D 배열을 2D 행렬의 특정 대각선에 배치합니다. 이들은 특정한 구조를 가진 행렬을 만들 때 유용합니다.

**코드/수식 해설**:

```python
import numpy as np

# 1D coordinate generators
r = np.arange(2, 10, 3) # [2, 5, 8] -> step on a half-open interval [start, stop)
l = np.linspace(0.0, 1.0, 5) # [0.0, 0.25, 0.5, 0.75, 1.0] -> 5 evenly spaced points in [0, 1] (inclusive)
```
*   `np.arange(start, stop, step)`: `start`부터 `stop` 미만까지 `step` 간격으로 숫자를 생성합니다. 결과는 `[2, 5, 8]`입니다.
*   `np.linspace(start, stop, num)`: `start`부터 `stop`까지 `num`개의 균등하게 분할된 점을 생성합니다 (양 끝점 포함). 결과는 `[0.0, 0.25, 0.5, 0.75, 1.0]`입니다.

```python
# Turn 1D coordinates into a 2D Cartesian grid via broadcasting
xs = np.arange(4) # [0, 1, 2, 3], shape (4,)
ys = np.arange(3) # [0, 1, 2], shape (3,)

# np.newaxis를 사용하여 차원을 확장하고 브로드캐스팅 준비
X = xs[np.newaxis, :] # shape (1, 4) -> [[0, 1, 2, 3]]
Y = ys[:, np.newaxis] # shape (3, 1) -> [[0], [1], [2]]

# X와 Y를 브로드캐스팅하여 2D 격자 생성
G = X + 10*Y
```
*   `xs`는 x축 좌표 `[0, 1, 2, 3]`을, `ys`는 y축 좌표 `[0, 1, 2]`를 나타냅니다.
*   `X = xs[np.newaxis, :]`는 `xs` 배열을 `(1, 4)` 형태로 변환하여, 연산 시 행 방향으로 브로드캐스팅될 수 있도록 준비합니다.
*   `Y = ys[:, np.newaxis]`는 `ys` 배열을 `(3, 1)` 형태로 변환하여, 연산 시 열 방향으로 브로드캐스팅될 수 있도록 준비합니다.
*   `G = X + 10*Y` 연산에서 `X`는 `(3, 4)`로, `Y`는 `(3, 4)`로 브로드캐스팅되어 최종적으로 `(3, 4)` 형태의 2D 배열 `G`가 생성됩니다. 이 `G`는 2D 격자의 각 점에 대한 특정 레이블 또는 값을 나타냅니다.
브로드캐스팅된 `X`는 `[[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]`이 되고,
브로드캐스팅된 `Y`는 `[[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]]`이 됩니다.
따라서 $G$는 다음과 같이 계산됩니다:
$$
G = \begin{bmatrix}
0 & 1 & 2 & 3 \\
0 & 1 & 2 & 3 \\
0 & 1 & 2 & 3
\end{bmatrix}
+ 10 \times
\begin{bmatrix}
0 & 0 & 0 & 0 \\
1 & 1 & 1 & 1 \\
2 & 2 & 2 & 2
\end{bmatrix}
=
\begin{bmatrix}
0 & 1 & 2 & 3 \\
10 & 11 & 12 & 13 \\
20 & 21 & 22 & 23
\end{bmatrix}
$$

```python
# Canonical 2D patterns
E = np.eye(3, k=1) # ones on the first superdiagonal
D = np.diag([9, 8, 7], k=-1) # place vector on the subdiagonal
```
*   `np.eye(N, k=offset)`: `N`x`N` 크기의 2D 배열을 생성하며, `k`로 지정된 대각선에 1을 채웁니다 (나머지는 0). `k=0`은 주 대각선, `k=1`은 주 대각선 위 첫 번째 대각선(superdiagonal)입니다.
    $$
    E = \begin{bmatrix}
    0 & 1 & 0 \\
    0 & 0 & 1 \\
    0 & 0 & 0
    \end{bmatrix}
    $$
*   `np.diag(v, k=offset)`: 1D 배열 `v`를 `k`로 지정된 대각선에 배치하여 2D 배열을 생성합니다. `k=-1`은 주 대각선 아래 첫 번째 대각선(subdiagonal)입니다. `v`의 길이에 따라 적절한 크기의 2D 배열이 생성됩니다.
    $$
    D = \begin{bmatrix}
    0 & 0 & 0 & 0 \\
    9 & 0 & 0 & 0 \\
    0 & 8 & 0 & 0 \\
    0 & 0 & 7 & 0
    \end{bmatrix}
    $$

**구체적 예시**:

*   **3D 함수 시각화를 위한 좌표 격자 생성**: `X`와 `Y`는 3D 그래프를 그릴 때 $Z = f(X, Y)$와 같은 함수 값을 계산하는 데 사용되는 2D 평면상의 좌표 격자입니다. 예를 들어, `matplotlib`를 사용하여 $Z = \sin(\sqrt{X^2 + Y^2})$와 같은 파동 형태의 곡면을 그릴 때 이러한 격자 좌표가 필요합니다.
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y) # np.newaxis를 이용한 방법과 유사하게 2D 격자 X, Y 생성
    Z = np.sin(np.sqrt(X**2 + Y**2))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title('3D Surface Plot of Z = sin(sqrt(X^2 + Y^2))')
    plt.show()
    ```
*   **컴퓨터 비전에서의 필터 마스크**: `np.eye`나 `np.diag`로 생성된 대각선 행렬은 이미지 처리에서 엣지 검출(edge detection) 등 특정 패턴을 찾는 데 사용되는 콘볼루션(convolution) 커널(kernel)로 활용될 수 있습니다. 예를 들어, 대각선 방향의 엣지를 강조하는 필터를 만들 수 있습니다.

**시험 포인트**:

*   ⭐ `np.arange(start, stop, step)`은 `stop`을 포함하지 않고 `step` 간격으로 숫자를 생성하며, `np.linspace(start, stop, num)`은 `start`와 `stop`을 포함하여 `num`개의 균등한 간격의 숫자를 생성한다는 **두 함수의 핵심 차이점**을 설명할 수 있어야 합니다.
*   ⭐ **`np.newaxis`의 역할과 브로드캐스팅 메커니즘**을 이해하는 것이 중요합니다. 1D 배열을 2D 격자(`X`, `Y`)로 변환할 때 `np.newaxis`가 어떻게 차원을 확장하고, 이 확장된 배열들이 브로드캐스팅 연산(`X + 10*Y`)에서 어떻게 상호작용하여 최종 2D 배열을 만드는지 설명할 수 있어야 합니다.
*   ⭐ `np.eye(N, k)`와 `np.diag(v, k)` 함수가 **특정 대각선을 가진 2D 행렬을 생성**하는 데 사용되며, `k` 인자가 대각선의 위치(주 대각선, 상위 대각선, 하위 대각선 등)를 어떻게 지정하는지 정확히 이해해야 합니다.
*   ⭐ 주어진 1D 배열(`xs`, `ys`)로부터 `np.newaxis`를 사용하여 생성된 `X`, `Y` 배열의 **최종 형태(shape)**와, 이를 활용한 `G = X + 10*Y`와 같은 연산의 **결과 배열 형태 및 값**을 예측하고 설명할 수 있어야 합니다.

---
## Slide 16

**핵심 개념**
NumPy의 `arange`와 `linspace` 함수는 특정 범위 내에서 숫자 시퀀스를 생성하여 NumPy 배열(array)을 만드는 데 사용되는 핵심 도구입니다. 이들은 특히 균일한 간격의 데이터를 생성할 때 유용하며, 데이터 분석 및 과학 계산에서 그리드(grid)나 인덱스를 구성할 때 필수적입니다.

**코드/수식 해설**

### `np.arange(a, b, h, dtype)`

`np.arange`는 지정된 시작 값(`a`), 종료 값(`b`), 그리고 단계 값(`h`)을 사용하여 균일한 간격의 시퀀스를 생성합니다. `b`는 시퀀스에 포함되지 않습니다 (배타적). `dtype`은 반환될 배열의 데이터 타입을 지정합니다.

-   `a`: 시퀀스의 시작 값 (포함).
-   `b`: 시퀀스의 종료 값 (배타적).
-   `h`: 단계 값 (step size). `h`는 0이 아니어야 합니다.
-   `dtype`: 선택적으로, 반환될 배열의 데이터 타입.

생성되는 배열의 길이(`N`)는 다음 조건을 만족하는 가장 큰 음이 아닌 정수 `n`으로 정의됩니다:
$$ N = \max \left\{ n \in \mathbb{N}_0 : a + nh \in \begin{cases} [a, b) & \text{if } h > 0, \\ (b, a] & \text{if } h < 0 \end{cases} \right\} $$
생성되는 시퀀스의 각 원소 $x_i$는 다음과 같이 계산됩니다:
$$ x_i = a + ih \quad \text{for } i \in \{0, 1, \dots, N-1\} $$
단계 값 `h`와 시작 값 `a`가 정수이면 시퀀스는 정확하게 매핑되지만, 부동 소수점 값일 경우 반올림 오차가 발생할 수 있습니다.

### `np.linspace(a, b, num=N, endpoint=True)`

`np.linspace`는 지정된 시작 값(`a`)과 종료 값(`b`) 사이를 `num`개의 동일한 간격으로 나눈 시퀀스를 생성합니다. `num`은 생성할 샘플의 개수를 지정하며, 기본값은 50입니다. `endpoint` 인수는 종료 값 `b`를 시퀀스에 포함할지 여부를 결정합니다.

-   `a`: 시퀀스의 시작 값 (포함).
-   `b`: 시퀀스의 종료 값. `endpoint=True`이면 포함, `endpoint=False`이면 배타적.
-   `num=N`: 생성할 샘플의 개수.
-   `endpoint=True`: 선택적으로, 종료 값 `b`를 시퀀스에 포함할지 여부. 기본값은 `True`.

생성되는 시퀀스의 각 원소 $x_i$는 `endpoint` 인수에 따라 다음과 같이 계산됩니다:
$$ x_i = \begin{cases} a + \frac{i}{N-1}(b-a), & \text{if endpoint is True and } N \geq 2, \\ a + \frac{i}{N}(b-a), & \text{if endpoint is False and } N \geq 1. \end{cases} $$
여기서 $i$는 `endpoint=True`일 때 $0, 1, \dots, N-1$이며, `endpoint=False`일 때도 $0, 1, \dots, N-1$입니다 (단, `endpoint=False`일 때는 `N` 등분하여 `b` 바로 전까지 생성).

**구체적 예시**

```python
import numpy as np

# np.arange 예시
print("np.arange(0, 10, 2):", np.arange(0, 10, 2))
# 출력: np.arange(0, 10, 2): [0 2 4 6 8]

print("np.arange(10, 0, -2):", np.arange(10, 0, -2))
# 출력: np.arange(10, 0, -2): [10  8  6  4  2]

print("np.arange(0.5, 3.0, 0.5):", np.arange(0.5, 3.0, 0.5))
# 출력: np.arange(0.5, 3.0, 0.5): [0.5 1.  1.5 2.  2.5] (3.0 미포함)

# np.linspace 예시
print("\nnp.linspace(0, 10, num=5):", np.linspace(0, 10, num=5))
# 출력: np.linspace(0, 10, num=5): [ 0.   2.5  5.   7.5 10. ] (0과 10 포함, 5개)

print("np.linspace(0, 10, num=5, endpoint=False):", np.linspace(0, 10, num=5, endpoint=False))
# 출력: np.linspace(0, 10, num=5, endpoint=False): [0. 2. 4. 6. 8.] (0부터 10 미포함, 5개)

print("np.linspace(1, 5, num=3):", np.linspace(1, 5, num=3))
# 출력: np.linspace(1, 5, num=3): [1. 3. 5.] (1과 5 포함, 3개)
```

**실생활 비유:**

*   **`np.arange`**: '0부터 10 미만까지 두 칸씩 건너뛰어 가기'와 비슷합니다. 예를 들어, 0부터 시작하여 2칸씩 뛰어가면 0, 2, 4, 6, 8에 멈춥니다 (10은 도착지점이지만 넘어가면 안 되므로 8까지만). 지하철 역을 건너뛰면서 가는 것과 유사합니다.
*   **`np.linspace`**: '출발점과 도착점 사이에 N개의 깃발을 균등하게 꽂기'와 같습니다. `endpoint=True`이면 출발점과 도착점에도 깃발을 꽂고 그 사이를 균등하게 나누어 깃발을 꽂습니다. `endpoint=False`이면 출발점에는 꽂지만 도착점에는 꽂지 않고 그 사이를 균등하게 나누어 깃발을 꽂습니다. 마라톤 코스의 표지판이나 등산로의 이정표처럼 구간을 정확히 나누는 데 사용될 수 있습니다.

**시험 포인트**

*   ⭐ **`np.arange`와 `np.linspace`의 주요 차이점**:
    *   `np.arange`: `시작`, `끝`(배타적), `간격`을 인자로 받습니다. (`stop`이 포함되지 않음)
    *   `np.linspace`: `시작`, `끝`(포함 여부 설정), `개수`를 인자로 받습니다. (`endpoint` 인자를 통해 `stop` 포함 여부 결정)
*   ⭐ **종료 값 포함 여부**: `np.arange`는 기본적으로 종료 값을 포함하지 않습니다. `np.linspace`는 `endpoint=True`가 기본값으로 종료 값을 포함합니다. 이 차이점을 이해하고 있어야 합니다.
*   ⭐ **부동 소수점 정밀도 문제**: `np.arange`는 부동 소수점 인자로 인해 예상치 못한 결과(예: 마지막 요소의 포함 여부)를 낼 수 있으므로, 정확한 개수가 필요한 경우 `np.linspace`가 더 안전한 선택일 수 있습니다.
*   `N` 계산 방식: 각 함수의 `N` (생성될 요소의 개수)이 어떻게 결정되는지 수식과 함께 이해하는 것이 중요합니다. 특히 `np.linspace`의 `N-1`과 `N`의 차이를 구분해야 합니다.
*   매개변수의 의미와 역할: `a`, `b`, `h`, `num`, `endpoint` 각 매개변수가 시퀀스 생성에 어떻게 영향을 미치는지 명확히 알아야 합니다.

---
## Slide 17

---
**핵심 개념**
NumPy에서 벡터 인덱싱(슬라이싱)은 1차원 배열(`ndarray`)의 특정 부분집합을 `a[i:j:k]` 형태로 선택하는 방법입니다.

*   **Half-open (반개방) 원칙**: 슬라이싱은 시작 인덱스 `i`의 요소는 포함하지만, 종료 인덱스 `j`의 요소는 포함하지 않습니다. 이는 수학에서의 $[i, j)$ 구간과 유사합니다. `k`는 스텝(step)으로, 요소를 건너뛰는 간격을 의미합니다.
*   **음수 인덱스 및 스텝**: 배열의 끝에서부터 요소를 참조할 때 음수 인덱스를 사용할 수 있습니다 (예: `-1`은 마지막 요소). 스텝 `k`가 음수이면 배열을 역순으로 슬라이싱합니다.
*   **뷰(View) 특성**: NumPy 슬라이스는 대부분의 경우 원본 배열의 복사본(copy)이 아닌 '뷰(view)'를 반환합니다. 이는 슬라이스를 통해 요소를 변경하면 원본 배열의 해당 요소도 함께 변경된다는 것을 의미합니다.

---
**코드/수식 해설**
NumPy 1차원 배열 `a`에 대한 슬라이싱 문법은 다음과 같습니다.

```python
a[start:stop:step]
```
*   `start` (i): 슬라이싱을 시작할 인덱스입니다. 생략되면 0 (배열의 첫 번째 요소)으로 간주됩니다.
*   `stop` (j): 슬라이싱을 멈출 인덱스입니다. 이 인덱스에 해당하는 요소는 결과에 포함되지 않습니다 (half-open). 생략되면 배열의 끝으로 간주됩니다.
*   `step` (k): 각 요소를 건너뛸 간격입니다. 생략되면 1로 간주됩니다. 음수 값은 역순으로 슬라이싱합니다.

---
**구체적 예시**
```python
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"Original array: {arr}\n")

# 1. 기본 슬라이싱: 인덱스 2부터 7 직전(6)까지
slice1 = arr[2:7]
print(f"arr[2:7]: {slice1}") # [2 3 4 5 6]

# 2. 스텝 사용: 인덱스 1부터 9 직전까지 2칸씩
slice2 = arr[1:9:2]
print(f"arr[1:9:2]: {slice2}") # [1 3 5 7]

# 3. 음수 인덱스: 끝에서 5번째부터 끝까지
slice3 = arr[-5:]
print(f"arr[-5:]: {slice3}") # [5 6 7 8 9]

# 4. 음수 스텝: 배열 전체를 역순으로 (start와 stop 생략, step은 -1)
slice4 = arr[::-1]
print(f"arr[::-1]: {slice4}\n") # [9 8 7 6 5 4 3 2 1 0]

# 5. 슬라이스는 뷰(view) 예시
view_slice = arr[2:5]
print(f"Original array before modification: {arr}") # [0 1 2 3 4 5 6 7 8 9]
print(f"View slice before modification: {view_slice}") # [2 3 4]

view_slice[0] = 99 # 뷰 슬라이스의 첫 번째 요소 변경

print(f"View slice after modification: {view_slice}") # [99  3  4]
print(f"Original array after modification: {arr}") # [ 0  1 99  3  4  5  6  7  8  9]
# View_slice를 변경했더니 원본 배열 arr의 인덱스 2의 값(원래 2)이 99로 변경됨을 확인할 수 있습니다.
# 만약 복사본을 원한다면 `arr[2:5].copy()`와 같이 사용해야 합니다.
```

---
**시험 포인트**
*   ⭐ **Half-open (반개방) 원칙**: NumPy 슬라이싱 `a[i:j:k]`에서 시작 `i`는 포함하지만 종료 `j`는 포함하지 않는다는 것을 정확히 이해하고 있어야 합니다. 특정 인덱스의 포함 여부를 묻는 문제가 자주 출제됩니다.
*   ⭐ **음수 인덱스와 스텝의 활용**: 음수 인덱스가 배열의 끝에서부터 역방향으로 인덱싱하며, 음수 스텝이 배열을 역순으로 슬라이싱한다는 점을 숙지해야 합니다. `[::-1]`을 이용한 배열 역순 만들기는 매우 빈번하게 사용되므로 반드시 기억해야 합니다.
*   ⭐ **슬라이스는 뷰(view) 특성**: NumPy 슬라이싱은 특별한 경우를 제외하고 원본 배열의 '뷰'를 반환하며, 이는 슬라이스 객체의 요소를 변경하면 원본 배열의 해당 요소도 변경된다는 것을 의미합니다. 이 개념은 데이터 변경 시 예상치 못한 결과를 초래할 수 있으므로, 복사본이 필요한 경우 `.copy()` 메서드를 명시적으로 사용해야 함을 함께 기억해야 합니다. 이 개념은 NumPy에서 매우 중요합니다.

---
## Slide 18

**핵심 개념**
NumPy 배열 슬라이싱은 배열의 특정 부분을 추출하여 새로운 뷰(view) 또는 복사본을 생성하는 강력한 기능입니다. 이는 파이썬 리스트의 슬라이싱 문법과 동일하게 `[start:end:step]` 형식을 따릅니다.

**코드/수식 해설**

먼저 NumPy 라이브러리를 `np`라는 별칭으로 임포트하고, 0부터 9까지의 정수로 구성된 1차원 배열 `a`를 생성합니다.
```python
import numpy as np
a = np.arange(10) # a = [0 1 2 3 4 5 6 7 8 9]
```

슬라이싱 문법 `a[start:end:step]`에서 각 인자의 기본값은 다음과 같습니다:
*   `start` (시작 인덱스 `i`): 생략 시 기본값은 `0`입니다.
*   `end` (종료 인덱스 `j`): 생략 시 기본값은 배열의 길이 `len(a)`입니다. `end` 인덱스에 해당하는 요소는 결과에 포함되지 않습니다.
*   `step` (간격 `k`): 생략 시 기본값은 `1`입니다.

다음은 다양한 슬라이싱 예시와 그 결과입니다.
```python
print(a[2:7])    # 결과: [2 3 4 5 6] (시작 인덱스 2부터 종료 인덱스 7 전까지, 간격 1)
print(a[:5])     # 결과: [0 1 2 3 4] (시작 인덱스 생략으로 0부터, 종료 인덱스 5 전까지)
print(a[5:])     # 결과: [5 6 7 8 9] (시작 인덱스 5부터, 종료 인덱스 생략으로 배열 끝까지)
print(a[::2])    # 결과: [0 2 4 6 8] (시작/종료 인덱스 생략, 간격 2)
print(a[::-1])   # 결과: [9 8 7 6 5 4 3 2 1 0] (시작/종료 인덱스 생략, 간격 -1로 배열을 역순으로)
```

**구체적 예시**

배열 `a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`를 예시로 들어보면:
*   `a[2:7]`은 인덱스 2(`2`)부터 시작하여 인덱스 6(`6`)까지의 요소들(`2, 3, 4, 5, 6`)을 추출합니다. 인덱스 7의 요소는 포함되지 않습니다.
*   `a[:5]`는 `start`가 생략되어 배열의 처음(인덱스 0)부터 시작하여 인덱스 4(`4`)까지의 요소들(`0, 1, 2, 3, 4`)을 추출합니다.
*   `a[5:]`는 `end`가 생략되어 인덱스 5(`5`)부터 배열의 끝까지의 요소들(`5, 6, 7, 8, 9`)을 추출합니다.
*   `a[::2]`는 `start`와 `end`가 생략되어 배열 전체에서 `step` 2 간격으로 요소들(`0, 2, 4, 6, 8`)을 추출합니다.
*   `a[::-1]`은 `step`이 `-1`인 특별한 경우로, 배열의 모든 요소를 역순으로 정렬하여 `[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]`을 반환합니다.

음수 인덱싱은 배열의 끝에서부터 요소를 참조할 때 사용됩니다.
*   `-1`은 배열의 마지막 요소를 나타냅니다.
*   `-2`는 배열의 뒤에서 두 번째 요소를 나타냅니다.
예를 들어, `a[-1]`은 `9`를, `a[-2]`는 `8`을 반환합니다.

**시험 포인트**

*   ⭐ 슬라이싱 문법 `[start:end:step]`에서 `end` 인덱스는 포함되지 않고 (`exclusive`), `start` 인덱스는 포함된다는 점(`inclusive`)을 명확히 이해해야 합니다.
*   ⭐ `start`, `end`, `step` 각 인자가 생략되었을 때의 기본값을 정확히 숙지해야 합니다 (`start`는 `0`, `end`는 `len(array)`, `step`은 `1`).
*   ⭐ 음수 인덱싱의 활용법, 특히 `[::-1]`을 사용하여 배열을 역순으로 만드는 기법은 시험에 자주 출제될 수 있습니다.
*   ⭐ NumPy 슬라이싱 결과는 일반적으로 원본 배열의 '뷰(view)'를 반환하므로, 슬라이싱된 결과 배열을 수정하면 원본 배열에도 영향을 줄 수 있음에 유의하세요. (깊은 복사 vs 얕은 복사 개념과 연결될 수 있습니다.)

---
## Slide 19

**핵심 개념**:
*   **하프-오픈 인터벌 (Half-Open Interval)**: 파이썬의 `range()` 함수, 리스트 슬라이싱, 그리고 NumPy 배열 슬라이싱은 모두 **시작 인덱스 (inclusive)**는 포함하고 **종료 인덱스 (exclusive)**는 포함하지 않는 개념을 사용합니다. 이는 수학적 표기인 `[시작, 끝)`과 동일합니다.
*   **슬라이싱 길이 계산**: `start:stop:step` 형식의 슬라이싱에서 생성되는 요소의 개수를 특정 수식을 통해 계산할 수 있습니다.
*   **역방향 슬라이싱**: 스텝(step)이 음수일 경우, 슬라이싱은 역방향으로 진행되며, 이때도 종료 인덱스는 여전히 포함되지 않습니다.

**코드/수식 해설**:

```python
import numpy as np

# 0부터 9까지의 정수로 구성된 NumPy 배열 생성 (인덱스 0부터 9까지)
a = np.arange(10) # a는 [0 1 2 3 4 5 6 7 8 9]

# 배열 a를 인덱스 2부터 7(포함 안 함)까지 슬라이싱
# 즉, 인덱스 2, 3, 4, 5, 6의 요소를 포함
s = a[2:7] # 기대되는 길이 = 5, 포함되는 인덱스는 2, 3, 4, 5, 6
print(len(s), s) # 출력: 5 [2 3 4 5 6]

# 파이썬의 range 함수와 비교
# range(2, 7)은 숫자 2부터 시작하여 7(포함 안 함) 직전인 6까지의 숫자를 생성
print(list(range(2, 7))) # 출력: [2, 3, 4, 5, 6] (NumPy 슬라이싱과 동일한 하프-오픈 개념)
```

*   **양의 스텝($k > 0$)을 사용할 때의 슬라이스 길이**:
    `a[i:j:k]` 형태의 슬라이싱에서, 스텝 $k$가 양수일 때 생성되는 요소의 개수는 다음 수식으로 계산됩니다. $i$는 시작 인덱스, $j$는 종료 인덱스 (exclusive), $k$는 스텝입니다. $\lceil \cdot \rceil$는 올림(ceiling) 함수를 나타냅니다.

    $$ \text{Length} = \max\{0, \lceil (j-i)/k \rceil \} $$

*   **음의 스텝($k < 0$)을 사용할 때의 슬라이스 동작**:
    `a[i:j:k]` 형태의 슬라이싱에서 스텝 $k$가 음수일 때 (역방향 슬라이싱), 인덱스는 $i, i+k, i+2k, \dots$ 순으로 진행됩니다. 이 과정은 현재 인덱스가 $j$보다 크거나 같을 때까지 (즉, $j$는 여전히 포함되지 않는 exclusive 기준) 계속됩니다.

**구체적 예시**:

1.  **기본 슬라이싱**:
    `arr = np.array([10, 20, 30, 40, 50, 60])`
    `arr[1:4]`는 인덱스 1(값 20)부터 인덱스 4 직전(인덱스 3, 값 40)까지를 포함합니다.
    결과: `[20, 30, 40]`

2.  **슬라이스 길이 계산 예시**:
    `arr = np.arange(20)` (`[0, 1, ..., 19]`)
    `arr[2:15:3]` 의 길이를 계산해 봅시다. $i=2, j=15, k=3$.
    $\text{Length} = \max\{0, \lceil (15-2)/3 \rceil \} = \max\{0, \lceil 13/3 \rceil \} = \max\{0, \lceil 4.33 \rceil \} = 5$.
    실제로 `[2, 5, 8, 11, 14]` 5개의 요소가 생성됩니다.

3.  **역방향 슬라이싱 예시**:
    `arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])`
    `arr[6:1:-2]` 를 살펴봅시다. $i=6, j=1, k=-2$.
    시작 인덱스는 6(값 7), 스텝은 -2이므로 인덱스는 6, 4, 2 순으로 감소합니다.
    종료 인덱스 1은 포함하지 않으므로, 1보다 큰 인덱스 2까지 포함됩니다.
    결과: `[7, 5, 3]`

**시험 포인트**:

*   ⭐ **하프-오픈 인터벌 개념**: Python의 `range()`, 리스트 슬라이싱 (`list[start:stop]`), NumPy 배열 슬라이싱 (`ndarray[start:stop]`)이 모두 `start`는 포함하고 `stop`은 포함하지 않는다는 것을 정확히 이해하고 있어야 합니다. 이는 데이터 분석 라이브러리를 사용할 때 매우 기본적인 약속입니다.
*   ⭐ **슬라이싱 결과 예측**: 주어진 `start`, `stop`, `step` (특히 `step`이 양수 또는 음수일 때)을 사용하여 슬라이싱의 결과로 어떤 요소들이 포함되는지 정확하게 예측할 수 있어야 합니다.
*   ⭐ **슬라이스 길이 계산 공식**: 양의 스텝($k > 0$)일 때의 슬라이스 길이 계산 공식 ($ \max\{0, \lceil (j-i)/k \rceil \} $)을 이해하고 적용할 수 있어야 합니다. 이는 슬라이싱 동작을 논리적으로 이해하고 디버깅하는 데 중요합니다.

---
## Slide 20

**핵심 개념**:
*   **뷰 (View)**: NumPy 배열의 일부를 참조하는 새로운 배열 객체입니다. 원본 배열과 동일한 메모리 버퍼를 공유하므로, 뷰를 수정하면 원본 배열의 해당 부분도 변경됩니다. 메모리 효율성을 위해 주로 사용됩니다.
*   **복사본 (Copy)**: NumPy 배열의 일부 또는 전체를 완전히 새로운 메모리 공간에 복사하여 생성된 독립적인 배열 객체입니다. 복사본을 수정해도 원본 배열은 변경되지 않습니다.
*   **Basic Slicing (기본 슬라이싱)**: 콜론(`:`) 문법을 사용하여 배열의 특정 범위를 선택하는 방법입니다. 대부분의 경우 **뷰**를 반환합니다.
*   **Advanced Indexing (고급 인덱싱)**: 정수형 리스트, NumPy 배열, 또는 불리언(Boolean) 마스크를 사용하여 배열의 특정 요소를 선택하는 방법입니다. 항상 **복사본**을 반환합니다.

**코드/수식 해설**:

```python
import numpy as np

# 원본 NumPy 배열 생성
a = np.arange(6)
# a는 [0, 1, 2, 3, 4, 5]

# 1. Basic Slicing (뷰 생성 예시)
# a[1:5]는 a의 인덱스 1부터 4까지 (5 미포함)를 선택합니다.
# 이 연산은 원본 배열 a의 메모리 버퍼를 참조하는 '뷰'를 생성합니다.
v = a[1:5] # v는 [1, 2, 3, 4]를 나타내지만, 실제 데이터는 a와 공유
print(f"초기 a: {a}") # 초기 a: [0 1 2 3 4 5]
print(f"v (a의 뷰): {v}") # v (a의 뷰): [1 2 3 4]

# 뷰 v의 첫 번째 요소(원본 a의 인덱스 1에 해당)를 수정합니다.
# v[0]에 999를 대입하면, 원본 배열 a의 a[1] 값도 999로 변경됩니다.
v[0] = 999
print(f"v 수정 후 a: {a}")
# 출력: v 수정 후 a: [  0 999   2   3   4   5]
# a[1]이 1에서 999로 변경된 것을 확인할 수 있습니다.

# 2. Advanced Indexing (복사본 생성 예시)
# 현재 a: [  0 999   2   3   4   5]

# 인덱스 리스트 정의
idx = [1, 2, 3]

# a[idx]는 idx에 명시된 인덱스(1, 2, 3)에 해당하는 요소들을 선택합니다.
# 이 연산은 원본 a와는 독립적인 새로운 메모리 공간에 데이터를 복사하여 '복사본' c를 생성합니다.
c = a[idx] # c는 [999, 2, 3]을 나타내는 복사본. 새로운 메모리 사용
print(f"c (a의 복사본): {c}")
# c (a의 복사본): [999   2   3]

# 복사본 c의 첫 번째 요소(현재 값 999)를 수정합니다.
# c는 독립적인 복사본이므로, c[0]을 -1로 변경해도 원본 배열 a에는 영향을 주지 않습니다.
c[0] = -1
print(f"c 수정 후 c: {c}") # c 수정 후 c: [-1  2  3]
print(f"c 수정 후 a: {a}")
# 출력: c 수정 후 a: [  0 999   2   3   4   5]
# a는 변경되지 않고 유지되는 것을 확인할 수 있습니다.
```
이 슬라이드에서는 특별한 수학적 수식이 다뤄지지 않습니다.

**구체적 예시**:
*   **뷰 (View) 예시**: 공유 드라이브에 있는 파일을 여러 명이 동시에 편집하는 상황과 비슷합니다. 한 사람이 파일을 수정하면, 모든 사람이 그 변경된 내용을 보게 됩니다. NumPy의 뷰는 원본 데이터의 메모리 주소를 가리키므로, 뷰를 통해 데이터를 바꾸면 원본 데이터 자체가 바뀝니다.
*   **복사본 (Copy) 예시**: 친구가 중요한 문서의 복사본을 만들어달라고 했을 때, 원본 문서는 사무실에 두고 복사기를 사용해 사본을 만들어서 주는 상황입니다. 친구가 그 사본에 무엇을 쓰거나 지우더라도, 사무실의 원본 문서에는 아무런 영향이 없습니다. NumPy의 복사본은 원본 데이터와 완전히 분리된 별개의 메모리 공간을 사용합니다.

**시험 포인트**:
*   ⭐ **NumPy에서 `basic slicing` (콜론 `:` 사용)과 `advanced indexing` (리스트, 배열, 불리언 마스크 사용)이 각각 뷰와 복사본 중 무엇을 반환하는지 정확히 이해하고 구분할 수 있어야 합니다.**
*   ⭐ 뷰를 통해 데이터를 수정했을 때 원본 배열에 어떤 변화가 생기는지, 그리고 복사본을 통해 수정했을 때는 원본에 어떤 변화가 없는지를 설명하고 예시를 들 수 있어야 합니다.
*   `numpy.ndarray.base` 속성을 활용하여 특정 배열이 다른 배열의 뷰인지 확인할 수 있습니다. (`v.base is a`는 True, `c.base is a`는 False)
*   메모리 사용 및 성능 관점에서 뷰와 복사본의 장단점을 이해하는 것이 중요합니다. (뷰는 메모리 절약, 복사본은 안전성)

---
## Slide 21

## Slice Assignment (슬라이스 대입)

### 핵심 개념
NumPy 배열에서 슬라이싱을 사용하여 특정 범위 또는 조건에 해당하는 요소들에 값을 대입하는 방법을 설명합니다. 값을 대입할 때 우항(right-hand side)은 스칼라 값일 수도 있고, 슬라이싱 결과로 형성된 부분 배열의 길이와 정확히 일치하는 다른 배열일 수도 있습니다.

### 코드/수식 해설

1.  **스칼라 값 브로드캐스팅(Scalar Broadcasting)**
    슬라이스에 스칼라 값을 대입하면 해당 슬라이스의 모든 요소에 스칼라 값이 **브로드캐스트(broadcast)**되어 적용됩니다.

    ```python
    import numpy as np

    a = np.arange(10) # a는 [0 1 2 3 4 5 6 7 8 9]
    a[2:7] = -1      # 인덱스 2부터 6까지 (7 미포함)의 요소에 -1 대입
    print(a)
    # 출력: [0 1 -1 -1 -1 -1 -1 7 8 9]
    ```
    이 예시에서 `a[2:7]`은 `[2, 3, 4, 5, 6]`의 5개 요소를 가리키며, `-1`이라는 스칼라 값이 이 5개 요소 각각에 대입됩니다.

2.  **스텝(Step)을 사용한 슬라이스 대입**
    슬라이싱 시 `start:end:step` 문법을 사용하여 특정 간격으로 요소를 선택하고 값을 대입할 수 있습니다.

    ```python
    import numpy as np

    a = np.arange(10) # a는 [0 1 2 3 4 5 6 7 8 9]
    a[::2] = 100     # 처음부터 끝까지 2칸 간격으로(짝수 인덱스) 요소에 100 대입
    print(a)
    # 출력: [100 1 100 3 100 5 100 7 100 9]
    ```
    `a[::2]`는 인덱스 `0, 2, 4, 6, 8`의 요소를 선택하며, 이들 각각에 `100`이 대입됩니다.

3.  **배열을 사용한 슬라이스 대입**
    슬라이스에 배열을 대입할 때는 우항 배열의 길이가 좌항 슬라이스의 길이와 **정확히 일치**해야 합니다.

    ```python
    import numpy as np

    a = np.arange(6)     # a는 [0 1 2 3 4 5]
    a[0:3] = [9, 8, 7]   # 인덱스 0부터 2까지 (3 미포함)의 요소에 [9, 8, 7] 대입
    print(a)
    # 출력: [9 8 7 3 4 5]
    ```
    `a[0:3]`은 `[0, 1, 2]`의 3개 요소를 가리킵니다. 우항의 `[9, 8, 7]` 배열도 길이가 3이므로, 각 위치에 대응하는 값이 대입됩니다 (`a[0]=9`, `a[1]=8`, `a[2]=7`). 만약 우항 배열의 길이가 다르다면 오류가 발생합니다.

### 구체적 예시
여러분 컴퓨터의 파일 시스템을 생각해보세요. 특정 폴더(`a`)에 10개의 파일(0번부터 9번까지)이 있다고 가정합시다.
*   **스칼라 대입**: 2번부터 6번 파일까지의 이름을 일괄적으로 '백업'으로 변경하는 것과 같습니다. (예: `a[2:7] = '백업'`)
*   **스텝 대입**: 홀수 번호의 파일(1, 3, 5, 7, 9번)만 선택하여 '읽기 전용' 속성을 부여하는 것과 유사합니다. (예: `a[1::2] = '읽기 전용'`)
*   **배열 대입**: 처음 3개 파일(0, 1, 2번)의 이름을 각각 '보고서', '계획서', '데이터'로 정확히 지정하여 변경하는 것과 같습니다. 이때 이름을 지정할 파일 개수와 변경할 이름의 개수가 일치해야 합니다.

### 시험 포인트
*   ⭐**슬라이스 대입의 두 가지 주요 방식**: 스칼라 값 대입(브로드캐스팅)과 배열 값 대입.
*   ⭐**배열 값 대입 시 길이 일치**: 우항의 배열 길이는 좌항 슬라이스의 길이와 정확히 일치해야 함을 이해하고 설명할 수 있어야 합니다. 일치하지 않을 경우 `ValueError`가 발생합니다.
*   ⭐다양한 슬라이싱 문법(예: `start:end`, `::step`, `:end`, `start:`)이 어떻게 동작하는지 정확히 이해하고, 각 경우에 어떤 요소들이 선택되고 값이 대입되는지 예측할 수 있어야 합니다. 특히 `end` 인덱스는 **포함되지 않음**에 유의하세요.

---
## Slide 22

**핵심 개념**:
*   **음수 인덱싱 (Negative Indexing)**: NumPy 배열에서 음수 인덱스는 배열의 끝에서부터 요소를 참조합니다. `-1`은 마지막 요소, `-2`는 뒤에서 두 번째 요소를 의미합니다.
*   **음수 스텝 (Negative Steps) 슬라이싱**: 슬라이싱 `[start:stop:step]`에서 `step` 값이 음수($k < 0$)인 경우, 배열은 오른쪽에서 왼쪽 방향으로 탐색됩니다.
    *   `start` 인덱스가 생략되면 배열의 마지막 요소부터 시작합니다.
    *   `stop` 인덱스가 생략되면 배열의 첫 번째 요소 전까지 탐색합니다.
    *   **주의**: `stop` 인덱스는 여전히 "half-open" (배타적) 규칙을 따릅니다. 즉, 해당 인덱스의 요소는 결과에 포함되지 않습니다. 유효한 슬라이싱을 위해서는 일반적으로 `start`가 `stop`보다 커야 합니다 (음수 스텝의 경우).

**코드/수식 해설**:
NumPy 배열 `a = np.arange(10)`은 `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`를 생성합니다.

1.  **음수 인덱싱 예시**:
    ```python
    a = np.arange(10)
    print(a[-3:]) # last 3 -> [7 8 9]
    print(a[:-3]) # all but last 3 -> [0 1 2 3 4 5 6]
    ```
    *   `a[-3:]`: 인덱스 `-3`은 배열의 뒤에서 세 번째 요소(값 7)를 가리킵니다. `[-3:]`는 이 인덱스부터 배열의 끝까지 슬라이싱합니다.
    *   `a[:-3]`: 배열의 시작부터 인덱스 `-3`(값 7) **전까지** 슬라이싱합니다.

2.  **음수 스텝 슬라이싱 예시**:
    ```python
    # walking backwards (k < 0)
    print(a[8:3:-2]) # indices: 8,6,4 -> [8 6 4]
    print(a[::-3])   # [9 6 3 0]
    ```
    *   `a[8:3:-2]`:
        *   `start = 8` (값 8)
        *   `stop = 3` (값 3)
        *   `step = -2`
        *   인덱스 8부터 시작하여 2칸씩 왼쪽으로 이동합니다. 인덱스는 8, 6, 4가 됩니다.
        *   다음 인덱스는 `4 + (-2) = 2`가 되지만, `stop` 인덱스 3에 도달했으므로 3의 값은 포함하지 않고 3 **전**에서 멈춥니다. 따라서 인덱스 2는 포함되지 않습니다.
    *   `a[::-3]`:
        *   `start` 생략: 음수 스텝이므로 배열의 마지막(인덱스 9)부터 시작합니다.
        *   `stop` 생략: 음수 스텝이므로 배열의 처음(인덱스 0) 전까지 탐색합니다.
        *   `step = -3`
        *   인덱스 9부터 시작하여 3칸씩 왼쪽으로 이동합니다. 인덱스는 9, 6, 3, 0이 됩니다.
        *   다음 인덱스 `0 + (-3) = -3`은 배열의 범위를 벗어나므로 탐색을 멈춥니다.

**구체적 예시**:
도서관 서가에 책들이 순서대로 1번부터 10번까지 꽂혀 있다고 상상해 봅시다.
*   `books[-3:]`는 서가의 마지막 세 권의 책(8번, 9번, 10번)을 가져옵니다.
*   `books[:-3]`는 마지막 세 권을 제외한 나머지 책들(1번부터 7번까지)을 가져옵니다.
*   `books[::-1]`는 서가에 꽂힌 책들을 역순으로(10번부터 1번까지) 가져옵니다. 이는 모든 책을 뒤에서부터 하나씩 가져오는 것과 같습니다.
*   `books[8:3:-2]`는 9번째 책(인덱스 8)부터 시작하여 2칸씩 건너뛰며 4번째 책(인덱스 3) 전까지 가져옵니다. 즉, 9번째, 7번째, 5번째 책을 가져오는 것입니다.

**시험 포인트**:
*   ⭐ **음수 인덱싱과 양수 인덱싱의 관계**: `arr[-k]`는 `arr[len(arr) - k]`와 동일한 위치를 가리킨다는 것을 이해해야 합니다.
*   ⭐ **음수 스텝 슬라이싱의 방향성**: `step`이 음수이면 슬라이싱 방향이 오른쪽에서 왼쪽으로 바뀐다는 점을 기억하세요. 이때는 `start` 인덱스가 `stop` 인덱스보다 커야 합니다.
*   ⭐ **`stop` 인덱스의 "half-open" 규칙**: 음수 스텝이든 양수 스텝이든 `stop` 인덱스 자체의 요소는 결과에 포함되지 않습니다. 이는 슬라이싱에서 가장 헷갈리기 쉬운 부분입니다.
*   ⭐ **생략된 `start`/`stop` 인덱스의 기본값**: 음수 스텝일 때 `start`가 생략되면 배열의 끝에서, `stop`이 생략되면 배열의 시작(전)까지 탐색한다는 것을 알아야 합니다.

---
## Slide 23

---
## Slicing and Strides (Performance Intuition)

### 핵심 개념

*   **NumPy `strides`**: NumPy 배열의 `strides` 속성은 배열의 각 차원을 따라 다음 원소로 이동하기 위해 필요한 바이트 수를 튜플 형태로 나타냅니다. 예를 들어 `(32, 8)`은 첫 번째 차원(행)에서 다음 원소로 가려면 32바이트, 두 번째 차원(열)에서 다음 원소로 가려면 8바이트를 건너뛰어야 함을 의미합니다. 이는 메모리 상에서 배열 원소들이 어떻게 배치되어 있는지를 보여주는 핵심 정보입니다.
*   **Contiguous View (연속적 뷰)**: 배열의 원소들이 메모리 상에 순서대로 (틈 없이) 저장되어 있을 때를 의미합니다. 이러한 뷰는 CPU 캐시 효율성이 높아 데이터 접근 및 연산 속도가 빠를 수 있습니다.
*   **Strided View (보폭 뷰)**: 배열의 원소들이 메모리 상에 일정한 간격(보폭)을 두고 떨어져 저장되어 있을 때를 의미합니다. 중간에 다른 원소들이 끼어있어 메모리 접근이 '점프'하는 형태로 이루어지며, 캐시 미스 발생 확률을 높여 연산 속도를 저하시킬 수 있습니다.
*   **Slicing과 `strides` 변화**: NumPy 배열을 슬라이싱하면 새로운 뷰(view)가 생성되는데, 이 뷰는 원본 배열의 메모리를 공유하며 `strides`가 변경될 수 있습니다. 특히 C-order (row-major) 메모리 레이아웃에서는 **행(row) 슬라이싱은 종종 연속적인 뷰**를 생성하는 반면, **열(column) 슬라이싱은 보폭 뷰**를 생성합니다.

### 코드/수식 해설

주어진 코드는 2차원 NumPy 배열 `X`를 생성하고, 이 배열에서 행(row)과 열(column)을 슬라이싱하여 새로운 뷰를 만든 후, 각 뷰의 `strides`를 비교합니다.

```python
import numpy as np

# 3x4 형태의 2차원 배열 X 생성
# X의 dtype은 시스템에 따라 다르지만, 일반적으로 np.int64 (8 bytes) 또는 np.int32 (4 bytes)
# 여기서는 np.int64를 가정하여 strides를 계산합니다.
X = np.arange(12).reshape(3, 4)

# X의 두 번째 행을 슬라이싱하여 'row' 뷰 생성
# X[1, :]는 X의 인덱스 1에 해당하는 행 (두 번째 행)을 의미합니다.
row = X[1, :] # contiguous view of a row

# X의 세 번째 열을 슬라이싱하여 'col' 뷰 생성
# X[:, 2]는 X의 인덱스 2에 해당하는 열 (세 번째 열)을 의미합니다.
col = X[:, 2] # strided view of a column

# 각 뷰와 그 strides 값을 출력
print("row:", row, "row.strides:", row.strides)
print("col:", col, "col.strides:", col.strides)
```

**`X` 배열의 생성 및 메모리 배치 (np.int64, 즉 itemsize = 8 bytes 가정)**:
`X = np.arange(12).reshape(3, 4)`는 다음과 같은 2차원 배열을 생성합니다.
```
[[ 0,  1,  2,  3],
 [ 4,  5,  6,  7],
 [ 8,  9, 10, 11]]
```
NumPy는 기본적으로 **C-order (row-major)** 방식으로 메모리에 데이터를 저장합니다. 즉, 같은 행의 원소들이 메모리에 연속적으로 배치됩니다.
`X` 배열의 `itemsize`가 8바이트 (int64)라고 가정하면,
*   `X.shape`는 `(3, 4)`
*   `X.strides`는 `(4 * 8, 1 * 8) = (32, 8)`이 됩니다.
    *   첫 번째 차원(행)에서 다음 행의 첫 원소로 이동하려면 $4 \times 8 = 32$ 바이트를 건너뛰어야 합니다.
    *   두 번째 차원(열)에서 같은 행의 다음 열 원소로 이동하려면 $1 \times 8 = 8$ 바이트를 건너뛰어야 합니다.

**`row = X[1, :]` 해설**:
`X[1, :]`는 `X`의 두 번째 행 `[4, 5, 6, 7]`에 대한 뷰를 생성합니다.
*   `row.shape`는 `(4,)`
*   `row.strides`는 `(8,)`이 됩니다. (itemsize가 8바이트이므로)
    *   `row` 배열의 원소 `4, 5, 6, 7`은 `X`의 메모리에서 연속적으로 배치되어 있습니다. 따라서 `row`는 **contiguous view**이며, 다음 원소로 가기 위해 자신의 `itemsize`인 8바이트만큼만 건너뛰면 됩니다.

**`col = X[:, 2]` 해설**:
`X[:, 2]`는 `X`의 세 번째 열 `[2, 6, 10]`에 대한 뷰를 생성합니다.
*   `col.shape`는 `(3,)`
*   `col.strides`는 `(32,)`가 됩니다.
    *   `col` 배열의 원소 `2, 6, 10`은 `X` 배열의 메모리에서 32바이트씩 떨어져 있습니다 (한 행 전체의 바이트 크기). 따라서 `col`은 **strided view**이며, 다음 원소로 가기 위해 `X`의 한 행 길이인 32바이트만큼 건너뛰어야 합니다.

### 구체적 예시

`X` 배열이 `np.int64` (8바이트) 정수를 저장한다고 가정할 때, 메모리 상의 원소 배치와 `strides`를 통해 동작을 이해해봅시다.

**1. 원본 배열 `X`:**
```
X = [[ 0,  1,  2,  3],
     [ 4,  5,  6,  7],
     [ 8,  9, 10, 11]]
```
가상 메모리 주소(시작 주소 0x00)와 데이터 배치:
```
Memory Address | Data (int64)
---------------+-------------
0x00           | 0
0x08           | 1
0x10           | 2
0x18           | 3   <-- Row 0 끝
0x20           | 4
0x28           | 5
0x30           | 6
0x38           | 7   <-- Row 1 끝
0x40           | 8
0x48           | 9
0x50           | 10
0x58           | 11  <-- Row 2 끝
```
`X.strides`는 `(32, 8)`:
*   다음 **행**으로 가려면 32바이트 (예: `0x00` (값 0)에서 `0x20` (값 4), `0x20`에서 `0x40`) 건너뜁니다.
*   다음 **열**로 가려면 8바이트 (예: `0x00` (값 0)에서 `0x08` (값 1), `0x20`에서 `0x28`) 건너뜁니다.

**2. 행 슬라이싱 `row = X[1, :]`:**
`row` 배열은 `[4, 5, 6, 7]`입니다.
이 원소들은 `X`의 메모리 주소 `0x20, 0x28, 0x30, 0x38`에 **연속적으로** 저장되어 있습니다.
```
Memory Address | Data (int64)
---------------+-------------
0x20           | 4
0x28           | 5
0x30           | 6
0x38           | 7
```
`row.strides`는 `(8,)`:
*   `row` 배열 내에서 다음 원소로 가려면 $8$ 바이트 (`0x20` -> `0x28`, `0x28` -> `0x30`)만 건너뛰면 됩니다. 이는 `row`가 **contiguous view**임을 의미합니다. CPU 캐시가 이 연속된 메모리 블록을 효율적으로 읽어올 수 있어 성능에 이점이 있습니다.

**3. 열 슬라이싱 `col = X[:, 2]`:**
`col` 배열은 `[2, 6, 10]`입니다.
이 원소들은 `X`의 메모리 주소 `0x10, 0x30, 0x50`에 저장되어 있습니다. 중간에 다른 원소들이 끼어있습니다.
```
Memory Address | Data (int64)
---------------+-------------
0x10           | 2
... (3, 4, 5) ...
0x30           | 6
... (7, 8, 9) ...
0x50           | 10
```
`col.strides`는 `(32,)`:
*   `col` 배열 내에서 다음 원소로 가려면 $32$ 바이트 (`0x10` -> `0x30`, `0x30` -> `0x50`)를 건너뛰어야 합니다. 이는 `col`이 **strided view**임을 의미합니다. 원소들이 메모리 상에서 불연속적으로 떨어져 있어, CPU가 데이터를 가져올 때 더 많은 캐시 미스가 발생할 수 있고 이는 연산 성능 저하로 이어질 수 있습니다.

### 시험 포인트

*   ⭐ **`strides`의 정의와 역할**: NumPy 배열에서 `strides`가 무엇을 의미하고, 메모리 접근 방식과 어떤 관련이 있는지 명확하게 설명할 수 있어야 합니다. (각 차원별 다음 원소로 이동하는 데 필요한 바이트 수).
*   ⭐ **C-order 배열에서의 행/열 슬라이싱과 `strides` 변화**: C-order (row-major) 메모리 레이아웃을 가정했을 때, 행 슬라이싱(`X[i, :]`)과 열 슬라이싱(`X[:, j]`)이 각각 어떤 `strides`를 가지게 되는지, 그리고 왜 그렇게 되는지 (contiguous vs. strided view) 설명하고 예시를 들 수 있어야 합니다.
*   ⭐ **성능적 의미**: Contiguous 메모리 접근과 Strided 메모리 접근이 CPU 캐시 효율성 및 연산 성능에 어떤 영향을 미치는지 이해해야 합니다. Contiguous 접근은 캐시 효율성이 높아 연산 속도가 빠르고, Strided 접근은 캐시 미스가 잦아 연산 속도가 느릴 수 있습니다.
*   NumPy 배열의 `itemsize`가 `strides` 계산에 어떻게 사용되는지 이해하는 것이 중요합니다. `strides`의 값은 `itemsize`의 배수입니다.
*   슬라이싱이 원본 배열의 뷰를 생성하고 메모리를 공유한다는 점도 중요합니다 (복사가 아님).

---
## Slide 24

**핵심 개념**
NumPy 배열의 1차원(1D) 슬라이싱은 배열의 특정 부분집합(sub-array)을 효율적으로 추출하는 강력한 방법입니다. `arr[start:stop:step]` 형식으로 사용되며, `start` 인덱스(포함), `stop` 인덱스(미포함), 그리고 `step` (건너뛸 간격)을 지정하여 유연하게 데이터를 선택할 수 있습니다. 이를 통해 반복문 없이도 데이터 윈도우 생성, 특정 간격으로 건너뛰기, 배열 뒤집기 등의 작업을 수행할 수 있어 코드가 간결하고 실행 속도가 빠릅니다.

**코드 해설**

아래 코드는 `np.arange(10)`으로 생성된 0부터 9까지의 정수를 담고 있는 1차원 NumPy 배열 `a`에 대해 다양한 슬라이싱 패턴을 보여줍니다.

```python
import numpy as np

a = np.arange(10) # a는 array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# 첫 3개 요소 선택: start 생략 시 0부터 시작, stop은 미포함
first3 = a[:3]    # 결과: [0 1 2]

# 마지막 3개 요소 선택: 음수 인덱스는 배열의 끝에서부터 계산 (마지막 요소는 -1)
last3 = a[-3:]    # 결과: [7 8 9]

# 인덱스 3부터 6까지 선택 (인덱스 7 미포함)
middle = a[3:7]   # 결과: [3 4 5 6]

# 짝수 인덱스 요소 선택: start/stop 생략 시 전체 배열, step 2
evens = a[::2]    # 결과: [0 2 4 6 8]

# 홀수 인덱스 요소 선택: start를 1로 지정하여 첫 번째 홀수 인덱스부터 시작
odds = a[1::2]    # 결과: [1 3 5 7 9]

# 배열 뒤집기: step을 -1로 지정하면 배열을 역순으로 반환
reverse = a[::-1] # 결과: [9 8 7 6 5 4 3 2 1 0]
```

*   **`start:stop:step` 설명**:
    *   `start`: 슬라이싱을 시작할 인덱스 (포함). 생략하면 0 (배열의 시작)입니다.
    *   `stop`: 슬라이싱을 종료할 인덱스 (미포함). 생략하면 배열의 끝입니다.
    *   `step`: 요소를 건너뛸 간격. 생략하면 1입니다. 음수 값은 역방향 슬라이싱을 의미합니다.

이 슬라이드에서는 특별한 수학적 수식이 사용되지 않습니다.

**구체적 예시**

실생활 비유를 들어볼까요?
*   **`a[:3]` (첫 3개)**: 10권짜리 책꽂이에서 "맨 앞에서부터 세 번째 책 직전까지"의 책들을 고르는 것과 같습니다.
*   **`a[-3:]` (마지막 3개)**: "맨 뒤에서 세 번째 책부터 끝까지"의 책들을 고르는 것과 같습니다.
*   **`a[3:7]` (중간 4개)**: "네 번째 책(인덱스 3)부터 일곱 번째 책(인덱스 6)까지"를 고르는 것입니다. 여덟 번째 책(인덱스 7)은 포함되지 않습니다.
*   **`a[::2]` (짝수 인덱스)**: "첫 번째 책부터 시작해서 한 권 건너 한 권씩" 고르는 것, 즉 홀수 번째 책들(첫 번째, 세 번째, 다섯 번째 등)을 고르는 것과 같습니다.
*   **`a[1::2]` (홀수 인덱스)**: "두 번째 책(인덱스 1)부터 시작해서 한 권 건너 한 권씩" 고르는 것, 즉 짝수 번째 책들(두 번째, 네 번째, 여섯 번째 등)을 고르는 것과 같습니다.
*   **`a[::-1]` (뒤집기)**: 책꽂이에 꽂힌 책들을 순서대로 모두 빼서 거꾸로 다시 꽂는 것과 같습니다.

**시험 포인트**

*   ⭐ **`start`, `stop`, `step` 인자의 역할과 기본값, 특히 `stop`이 미포함(exclusive)이라는 점을 정확히 이해하고 있어야 합니다.**
*   ⭐ **음수 인덱싱(`-3:`과 같은 형태)이 배열의 끝에서부터 카운트된다는 것을 알아야 합니다.**
*   ⭐ **`step` 값을 2로 설정했을 때(예: `::2`, `1::2`) 짝수/홀수 인덱스 요소를 어떻게 선택하는지 이해하는 것이 중요합니다.**
*   ⭐ **`[::-1]`과 같이 `step`이 음수인 경우 배열을 역순으로 뒤집는다는 것을 반드시 기억해야 합니다.**
*   **슬라이싱은 반복문(loop)을 사용하지 않고 데이터를 처리하여 성능상 이점이 있다는 점을 명심하세요.** (Numpy의 벡터화 연산의 일환)

---
## Slide 25

**핵심 개념**:
*   **의사 난수(Pseudo-random numbers)**: 컴퓨터는 진정한 의미의 무작위 숫자를 생성하기 어렵기 때문에, 특정 알고리즘에 기반하여 무작위처럼 보이는 숫자를 생성합니다. 이를 의사 난수라고 합니다.
*   **난수 생성기(Random Number Generator, RNG)**: NumPy의 `np.random.default_rng()`와 같이 난수 시퀀스를 생성하는 객체입니다. 이 객체는 생성할 난수의 분포와 형태를 지정하여 여러 난수를 뽑아낼 수 있습니다.
*   **시드(Seed)**: 난수 생성기의 초기 상태를 결정하는 숫자입니다. 동일한 시드를 사용하면 난수 생성기는 항상 동일한 순서의 난수 시퀀스를 생성합니다. 이는 **실험의 재현성(Reproducibility)**을 보장하는 데 필수적입니다.
*   **확률 분포(Probability Distribution)**: 난수가 추출될 통계적 분포를 나타냅니다. 예를 들어, `normal`은 정규 분포를, `uniform`은 균등 분포를 따릅니다. 각 분포는 특정 파라미터(예: 정규 분포의 평균과 표준편차)를 가집니다.
*   **배열 형태(Shape)**: 생성될 난수 배열의 차원과 각 차원의 크기를 지정합니다.

**코드/수식 해설**:

```python
import numpy as np

# 시드(seed) 42를 사용하여 두 개의 난수 생성기 객체 G1과 G2를 생성합니다.
# np.random.default_rng()는 최신 NumPy에서 권장되는 난수 생성 방식입니다.
# 동일한 시드(42)를 사용했으므로, G1과 G2는 내부적으로 동일한 초기 상태를 가집니다.
G1 = np.random.default_rng(42)
G2 = np.random.default_rng(42)

# G1 생성기를 사용하여 난수를 생성합니다.
# loc=0.0: 정규 분포의 평균(mean)을 0.0으로 설정합니다.
# scale=1.0: 정규 분포의 표준편차(standard deviation)를 1.0으로 설정합니다.
# size=(2, 3): 2행 3열의 2차원 배열 형태로 난수를 생성합니다.
X = G1.normal(loc=0.0, scale=1.0, size=(2, 3))

# G2 생성기를 사용하여 G1과 동일한 파라미터로 난수 배열 Y를 생성합니다.
# G1과 G2가 동일한 시드에서 시작했기 때문에, X와 Y는 수학적으로 동일한 난수 시퀀스를 뽑아냅니다.
Y = G2.normal(loc=0.0, scale=1.0, size=(2, 3))

# 생성된 배열 X와 Y의 형태를 출력합니다.
print(X.shape, Y.shape) # 출력: (2, 3) (2, 3)

# numpy.allclose() 함수는 두 배열의 모든 요소가 상대적/절대적 허용 오차 내에서 근사적으로 같은지 확인합니다.
# 동일한 시드에서 생성된 동일한 난수 시퀀스이므로, 이 비교 결과는 True가 됩니다.
print(np.allclose(X, Y)) # 출력: True (same seed -> same draws)
```

코드에서 사용된 정규 분포(Normal Distribution)의 확률 밀도 함수(Probability Density Function, PDF)는 다음과 같습니다:
$$
f(x | \mu, \sigma) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x - \mu}{\sigma}\right)^2}
$$
여기서 $\mu$는 평균(코드의 `loc`), $\sigma$는 표준편차(코드의 `scale`)입니다.

**구체적 예시**:
데이터 과학 프로젝트를 진행할 때, 머신러닝 모델의 가중치를 무작위로 초기화하거나, 데이터셋을 훈련 세트와 테스트 세트로 분할(train-test split)할 때 난수를 사용하게 됩니다. 만약 시드를 설정하지 않으면, 코드를 실행할 때마다 다른 난수가 생성되어 모델의 초기화 상태나 데이터 분할 방식이 달라질 수 있습니다. 이로 인해 같은 코드라도 실행할 때마다 다른 학습 결과가 나오거나, 버그를 찾아내기 어려워질 수 있습니다. 시드를 42와 같이 특정 숫자로 고정해두면, 언제, 누가 코드를 실행하더라도 동일한 난수 시퀀스가 생성되어 항상 같은 결과를 얻을 수 있으며, 이는 동료와 협업하거나 논문에 결과를 발표할 때 매우 중요합니다.

**시험 포인트**:
*   ⭐ **난수 시드(seed)의 역할과 중요성**: 왜 난수 시드를 설정해야 하는지, 그리고 시드를 설정했을 때 데이터 분석 및 머신러닝 실험에서 얻을 수 있는 이점(예: **재현성** 확보)을 설명할 수 있어야 합니다.
*   ⭐ `np.random.default_rng()`를 사용하여 난수 생성기를 초기화하는 방법과, `.normal()`, `.uniform()` 등 특정 분포에서 난수를 추출하는 메서드의 `loc`, `scale`, `size`와 같은 주요 인자들의 의미를 정확히 이해해야 합니다.
*   ⭐ `np.allclose()`와 같이 부동 소수점 배열의 근사적 일치를 확인하는 함수의 필요성과 활용법을 알아야 합니다.
*   ⭐ `numpy.random` 모듈이 제공하는 다양한 확률 분포(정규 분포, 균등 분포 등)의 특징과 각각을 어떤 상황에서 사용해야 하는지 구분할 수 있어야 합니다.

---
## Slide 26

**핵심 개념**:
*   **난수 생성기의 초기화 및 재현성**: `np.random.default_rng(seed)`를 사용하여 난수 생성기 객체를 생성하며, `seed` 값을 통해 동일한 난수 시퀀스를 재현할 수 있습니다. 이는 실험 결과를 일관되게 유지하고 디버깅을 용이하게 하는 데 중요합니다.
*   **다양한 확률 분포에서의 난수 생성**: NumPy의 난수 생성기는 기본적인 [0, 1) 범위의 균일 분포는 물론, 특정 범위의 균일 분포(`uniform`), 정규 분포(`normal`) 등 다양한 확률 분포에서 난수를 추출하는 기능을 제공합니다.
*   **연속형 및 이산형 난수 생성**:
    *   `G.random()`, `G.uniform()`, `G.normal()` 등은 연속형 분포에서 실수(float) 난수를 생성합니다.
    *   `G.integers()`는 이산형 분포(정수)에서 난수를 생성하며, 이때 `endpoint` 인자에 따라 상한값의 포함 여부가 결정됩니다.
*   **독립적이고 동일하게 분포된(i.i.d.) 난수**: 생성되는 모든 난수 $X[i]$는 서로에게 영향을 주지 않으며(독립적), 동일한 확률 분포를 따릅니다(동일하게 분포됨). 이는 통계 및 머신러닝 모델링의 기본 가정 중 하나입니다.

**코드/수식 해설**:

```python
import numpy as np

# 1. 난수 생성기 초기화 (seed를 사용해 재현 가능하게 설정)
# G = np.random.default_rng(seed)
# seed 값을 동일하게 설정하면 항상 같은 난수 시퀀스가 생성됩니다.
G = np.random.default_rng(seed=42)
print(f"Random generator initialized: {G}")

# 2. G.random(s): [0, 1) 범위의 연속 균일 분포 난수 생성
# X ∈ [0, 1)^s with X[i] i.i.d. ~ Unif(0, 1) (continuous)
random_0_1 = G.random(5) # 0.0 이상 1.0 미만의 실수 5개 생성
print(f"\nRandom numbers from Unif(0,1): {random_0_1}")

# 3. G.normal(mu, sigma, s): 정규 분포(Normal Distribution) 난수 생성
# X[i] i.i.d. ~ N(μ, σ^2)
mu = 0     # 평균 (mean)
sigma = 1  # 표준편차 (standard deviation)
normal_numbers = G.normal(mu, sigma, 5) # 평균 0, 표준편차 1인 정규 분포에서 5개 생성
print(f"\nRandom numbers from N(0,1): {normal_numbers}")

# 4. G.uniform(low, high, s): [low, high) 범위의 연속 균일 분포 난수 생성
# X[i] i.i.d. ~ Unif(ℓ, h) (continuous)
low_bound = 10
high_bound = 20
uniform_custom = G.uniform(low_bound, high_bound, 5) # 10.0 이상 20.0 미만의 실수 5개 생성
print(f"\nRandom numbers from Unif(10,20): {uniform_custom}")

# 5. G.integers(low, high, size, endpoint=False): [low, high-1] 범위의 이산 균일 분포 정수 난수 생성
# X[i] i.i.d. ~ DiscreteUniform({a, a+1, ..., b-1})
a_int = 1
b_int = 10
integers_exclusive = G.integers(a_int, b_int, 5, endpoint=False) # 1부터 9까지의 정수 5개 생성
print(f"\nIntegers (endpoint=False, range [1, 9]): {integers_exclusive}")

# 6. G.integers(low, high, size, endpoint=True): [low, high] 범위의 이산 균일 분포 정수 난수 생성
# With endpoint=True, the support is {a, ..., b}
integers_inclusive = G.integers(a_int, b_int, 5, endpoint=True) # 1부터 10까지의 정수 5개 생성
print(f"\nIntegers (endpoint=True, range [1, 10]): {integers_inclusive}")
```

*   **이산 균일 분포 확률 수식 (endpoint=False)**:
    $Pr\{X[i] = k\} = \frac{1}{b-a}$ for $k \in \{a, \dots, b-1\}$
    *   $b-a$는 가능한 정수의 총 개수입니다. (예: $a=1, b=10$일 때 $10-1=9$개의 정수 {1, 2, ..., 9} 중 하나가 선택될 확률은 1/9)

*   **이산 균일 분포 확률 수식 (endpoint=True)**:
    $Pr\{X[i] = k\} = \frac{1}{b-a+1}$ for $k \in \{a, \dots, b\}$
    *   $b-a+1$은 가능한 정수의 총 개수입니다. (예: $a=1, b=10$일 때 $10-1+1=10$개의 정수 {1, 2, ..., 10} 중 하나가 선택될 확률은 1/10)

**구체적 예시**:

*   **재현 가능한 시뮬레이션**: 머신러닝 모델의 성능을 여러 번 평가하거나 다른 사람과 코드를 공유할 때, `G = np.random.default_rng(seed=1234)`와 같이 `seed`를 고정하면 항상 동일한 '무작위' 데이터셋으로 시작할 수 있어 실험 결과의 일관성과 비교 가능성을 보장합니다.

*   **가상 주사위 굴리기**:
    `dice_rolls = G.integers(1, 6, size=10, endpoint=True)`
    이는 1부터 6까지의 정수 중에서 10개의 난수를 생성하여 주사위를 10번 굴리는 상황을 시뮬레이션합니다. `endpoint=True` 덕분에 6이 포함되어 실제 주사위와 같은 결과를 얻습니다.

*   **가상 투표 결과 시뮬레이션**:
    `voting_results = G.normal(loc=0.5, scale=0.1, size=1000)`
    이는 평균 0.5(50%), 표준편차 0.1(10%)를 갖는 정규 분포를 사용하여 1000개의 가상 투표 결과를 시뮬레이션합니다. 실제 여론조사 오차를 고려한 데이터 생성에 활용될 수 있습니다.

**시험 포인트**:

*   ⭐ **`np.random.default_rng(seed)`의 역할**: 난수 생성기의 "재현성(reproducibility)"을 보장하는 핵심 기능입니다. seed를 고정하면 매번 같은 난수 시퀀스를 얻을 수 있어 디버깅 및 실험 비교에 필수적입니다.
*   ⭐ **`G.integers` 함수의 `endpoint` 인자 이해**:
    *   `endpoint=False`일 경우: `[low, high-1]` 범위의 정수를 반환합니다. (상한값 `high`는 미포함)
    *   `endpoint=True`일 경우: `[low, high]` 범위의 정수를 반환합니다. (상한값 `high`는 포함)
    *   이 두 경우에 대한 각 정수가 선택될 확률을 정확히 계산할 수 있어야 합니다 (즉, 총 가능한 정수의 개수를 정확히 파악).
*   ⭐ **i.i.d. (independent and identically distributed)의 의미**: 생성되는 모든 $X[i]$가 서로 독립적이며 동일한 확률 분포를 따른다는 것을 이해해야 합니다. 이는 많은 통계적 모델과 머신러닝 알고리즘의 근본적인 가정입니다.
*   연속형 균일 분포(`G.random`, `G.uniform`)와 이산형 균일 분포(`G.integers`)의 차이를 명확히 구분할 수 있어야 합니다. 특히, 반환 값의 형태(실수 vs. 정수)와 분포 범위가 다름을 인지해야 합니다.

---
## Slide 27

---
**핵심 개념**

*   **가상 난수(Pseudo-random Numbers)**: 컴퓨터는 진정한 의미의 무작위 숫자를 생성할 수 없습니다. 대신, 특정 알고리즘에 따라 무작위처럼 보이는 일련의 숫자를 생성하는데, 이를 가상 난수라고 합니다.
*   **난수 시드(Random Seed)**: 가상 난수 생성 알고리즘의 시작점 역할을 하는 정수입니다. 동일한 시드를 사용하면 항상 동일한 난수 시퀀스가 생성됩니다.
*   **재현성(Reproducibility)**: 데이터 분석 및 과학 컴퓨팅에서 동일한 코드와 입력으로 항상 동일한 결과를 얻는 능력입니다. 난수 생성 시 시드를 설정함으로써 난수 생성 과정을 재현할 수 있습니다.
*   **정규 분포(Normal Distribution)**: 평균(loc)과 표준편차(scale)에 의해 특성 지어지는 연속 확률 분포입니다. 자연 현상에서 자주 관찰되는 중요한 분포입니다.

**코드/수식 해설**

```python
import numpy as np

# 1. 난수 생성기 객체 초기화
# np.random.default_rng(seed)는 특정 seed 값을 사용하여 난수 생성기 객체를 반환합니다.
# seed 값이 같으면 두 개의 다른 생성기 객체(G1, G2)라도 동일한 난수 시퀀스를 생성합니다.
G1 = np.random.default_rng(42)
G2 = np.random.default_rng(42)

# 2. 정규 분포에서 난수 샘플링
# G.normal(loc=평균, scale=표준편차, size=생성할 난수의 개수)
# 평균이 0.0, 표준편차가 1.0인 표준 정규 분포에서 100,000개의 난수를 생성합니다.
# G1과 G2가 동일한 시드로 초기화되었으므로 X와 Y는 동일한 숫자 배열을 가집니다.
X = G1.normal(loc=0.0, scale=1.0, size=(100000,))
Y = G2.normal(loc=0.0, scale=1.0, size=(100000,))

# 3. 두 배열의 동일성 비교
# np.allclose(a, b)는 두 배열 a와 b가 요소별로 일정 오차 범위 내에서 거의 동일한지 확인합니다.
# 여기서는 G1과 G2가 동일한 시드로 초기화되어 X와 Y가 정확히 같으므로 True를 반환합니다.
print("same draws?", np.allclose(X, Y))

# 4. 생성된 난수 배열의 통계량 계산
# X.mean()은 배열 X의 평균을 계산합니다.
# X.std()는 배열 X의 표준편차를 계산합니다.
# 표준 정규 분포(평균 0, 표준편차 1)에서 충분히 많은 샘플을 뽑았으므로,
# 샘플의 평균은 0에 가깝고, 표준편차는 1에 가깝게 나옵니다.
print("mean, std ~ 0,1:", X.mean(), X.std())
```

**수식:**
*   **평균 ($\bar{x}$)**: $N$개의 데이터 포인트 $x_1, x_2, \ldots, x_N$에 대해 다음과 같이 정의됩니다.
    $$ \bar{x} = \frac{1}{N} \sum_{i=1}^{N} x_i $$
*   **표준편차 ($s$)**: $N$개의 데이터 포인트 $x_1, x_2, \ldots, x_N$에 대해 다음과 같이 정의됩니다 (NumPy의 `std()`는 기본적으로 모집단 표준편차를 계산).
    $$ s = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \bar{x})^2} $$

**구체적 예시**

상상해 보세요. 당신이 어떤 게임의 몬스터가 드롭할 아이템을 무작위로 결정하는 코드를 작성하고 있습니다. 만약 난수 시드를 설정하지 않으면, 매번 게임을 다시 시작할 때마다 몬스터가 드롭하는 아이템의 종류와 확률이 달라질 수 있습니다. 이는 개발자가 버그를 찾거나 게임 밸런스를 테스트하기 어렵게 만듭니다. 하지만 `np.random.default_rng(42)`와 같이 특정 시드를 설정하면, 몬스터가 드롭하는 아이템 시퀀스가 항상 동일하게 유지되어, 테스트와 디버깅을 훨씬 쉽게 할 수 있습니다. 마치 특정 레시피(시드)로 요리하면 항상 같은 맛의 음식이 나오는 것과 같습니다.

**시험 포인트**

*   ⭐ **난수 시드(Random Seed)의 중요성**: 왜 난수 시드를 설정해야 하는지, 그리고 데이터 분석에서 재현성(Reproducibility)이 왜 중요한지 설명할 수 있어야 합니다. (동일한 시드는 동일한 난수 시퀀스를 생성하며, 이는 결과의 재현성을 보장합니다.)
*   ⭐ `np.random.default_rng()`의 역할: 이 함수가 난수 생성기 객체를 반환하고, 이 객체를 통해 다양한 분포의 난수를 생성할 수 있음을 이해해야 합니다.
*   ⭐ `normal()` 함수의 인자 이해: `loc` (평균), `scale` (표준편차), `size` (생성할 난수의 개수 및 배열 형태)가 각각 무엇을 의미하는지 알고 있어야 합니다.
*   `np.allclose()`의 활용: 두 부동 소수점 배열이 허용 오차 내에서 동일한지 확인하는 데 사용됨을 알아두세요.
*   충분히 큰 샘플에서 계산된 평균과 표준편차가 모평균과 모표준편차에 근접하는 이유 (대수의 법칙).

---
## Slide 28

**핵심 개념**:
`numpy.eye` 함수는 NumPy 라이브러리에서 특정 대각선에 1을 채우고 나머지는 0으로 채워진 2차원 배열(행렬)을 생성하는 데 사용됩니다. 주로 선형대수학에서 사용되는 단위 행렬(identity matrix)을 생성하거나, 주 대각선(main diagonal) 외에 다른 위치의 대각선에 1을 채운 행렬을 만들 때 유용하게 활용됩니다. 이 함수는 지정된 크기의 행렬에서 대각선의 위치를 `k` 인자를 통해 조절할 수 있게 합니다.

**코드/수식 해설**:
`np.eye` 함수의 기본 형태는 다음과 같습니다.
```python
import numpy as np

np.eye(N, M=None, k=0, dtype=float)
```
*   `N`: 생성할 행렬의 행(row)의 개수를 지정합니다.
*   `M`: 생성할 행렬의 열(column)의 개수를 지정합니다. 이 인자가 생략되면 `N`과 동일하게 설정되어 정방 행렬(square matrix)을 생성합니다.
*   `k`: 대각선의 위치를 지정하는 정수입니다.
    *   $k = 0$: 주 대각선(main diagonal)에 1이 채워집니다. 이는 행 인덱스 `i`와 열 인덱스 `j`가 같을 때 ($i=j$)를 의미합니다.
    *   $k > 0$: 주 대각선보다 위(오른쪽)에 있는 대각선(superdiagonal)에 1이 채워집니다. `k`가 커질수록 주 대각선에서 더 오른쪽으로 멀어집니다. 이는 $j - i = k$ 관계를 갖는 요소들을 의미합니다.
    *   $k < 0$: 주 대각선보다 아래(왼쪽)에 있는 대각선(subdiagonal)에 1이 채워집니다. `k`가 작아질수록 주 대각선에서 더 아래로 멀어집니다. 이는 $j - i = k$ 관계를 갖는 요소들을 의미합니다.
*   `dtype`: 배열의 데이터 타입을 지정합니다. 기본값은 `float`입니다.

행렬의 요소 $a_{ij}$는 다음과 같이 정의됩니다:
$$
a_{ij} = \begin{cases} 1 & \text{if } j - i = k \\ 0 & \text{otherwise} \end{cases}
$$
여기서 $i$는 행 인덱스(0부터 시작), $j$는 열 인덱스(0부터 시작)를 나타냅니다.

**구체적 예시**:
1.  **3x3 단위 행렬 생성 (k=0, 주 대각선)**
    ```python
    import numpy as np
    matrix_identity = np.eye(3)
    print("np.eye(3):\n", matrix_identity)
    ```
    출력:
    ```
    np.eye(3):
     [[1. 0. 0.]
      [0. 1. 0.]
      [0. 0. 1.]]
    ```
    이는 슬라이드의 `np.eye(3)` 예시와 동일하며, $3 \times 3$ 크기의 단위 행렬을 생성합니다.

2.  **2x4 행렬에서 k=1 대각선 생성 (superdiagonal)**
    ```python
    import numpy as np
    matrix_superdiag = np.eye(2, 4, k=1)
    print("\nnp.eye(2, 4, k=1):\n", matrix_superdiag)
    ```
    출력:
    ```
    np.eye(2, 4, k=1):
     [[0. 1. 0. 0.]
      [0. 0. 1. 0.]]
    ```
    이는 슬라이드의 `np.eye(2, 4, k=1)` 예시와 동일하며, $2 \times 4$ 크기의 행렬에서 주 대각선보다 한 칸 위(오른쪽)의 대각선(예: `[0,1]`, `[1,2]`)에 1이 채워집니다.

3.  **4x4 행렬에서 k=-1 대각선 생성 (subdiagonal)**
    ```python
    import numpy as np
    matrix_subdiag = np.eye(4, k=-1)
    print("\nnp.eye(4, k=-1):\n", matrix_subdiag)
    ```
    출력:
    ```
    np.eye(4, k=-1):
     [[0. 0. 0. 0.]
      [1. 0. 0. 0.]
      [0. 1. 0. 0.]
      [0. 0. 1. 0.]]
    ```
    이는 슬라이드의 `np.eye(4, k=-1)` 예시와 동일하며, $4 \times 4$ 크기의 행렬에서 주 대각선보다 한 칸 아래(왼쪽)의 대각선(예: `[1,0]`, `[2,1]`, `[3,2]`)에 1이 채워집니다.

**시험 포인트**:
*   ⭐ `np.eye` 함수의 기본 사용법과 인자 (`N`, `M`, `k`)의 역할을 정확히 이해해야 합니다.
*   ⭐ 특히 `k` 인자의 값에 따른 대각선 위치 변화(주 대각선, superdiagonal, subdiagonal)를 구분할 수 있어야 합니다. ($k=0$은 주 대각선, $k>0$은 superdiagonal, $k<0$은 subdiagonal)
*   ⭐ 주어진 `N`, `M`, `k` 값으로 `np.eye` 함수가 생성할 행렬의 형태와 내용을 예측할 수 있어야 합니다. 이는 코드를 직접 실행하지 않고도 결과를 파악하는 능력을 요구합니다.
*   `np.eye`가 단위 행렬(identity matrix)을 만드는 데 사용되는 대표적인 함수임을 기억하세요.

---
## Slide 29

**핵심 개념**:
`numpy.eye` 함수는 지정된 크기의 2차원 배열(행렬)을 생성하며, 주 대각선(main diagonal) 또는 특정 위치로 이동(shift)된 대각선에만 1의 값을, 그 외의 모든 요소에는 0의 값을 채워 넣습니다.
*   **Identity Matrix**: `k=0`일 때 정사각 행렬을 생성하면, 이는 선형대수학에서 항등 행렬(Identity Matrix, $I$)과 동일합니다.
*   **Shifted Identity Matrix**: `k` 값을 조절하여 1로 채워질 대각선의 위치를 위나 아래로 이동시킬 수 있습니다.
*   **Rectangular Shapes**: 정사각 행렬뿐만 아니라 직사각 행렬 형태도 지원합니다.

**코드/수식 해설**:

`np.eye` 함수의 시그니처는 다음과 같습니다:
`np.eye(N, M=None, k=0, dtype=float)`

*   `N`: 생성할 행렬의 행(row)의 개수입니다.
*   `M`: 생성할 행렬의 열(column)의 개수입니다. 생략(None)하면 `N`과 동일하게 설정되어 정사각 행렬이 됩니다.
*   `k`: 1로 채워질 대각선의 위치를 지정하는 오프셋(offset)입니다.
    *   `k=0`: 주 대각선(main diagonal)
    *   `k > 0`: 주 대각선보다 위에 위치한 대각선 (오른쪽으로 `k`칸 이동)
    *   `k < 0`: 주 대각선보다 아래에 위치한 대각선 (왼쪽으로 `k`칸 이동)
*   `dtype`: 생성될 배열 요소들의 데이터 타입입니다. 기본값은 `float`입니다.

함수가 반환하는 행렬 $E$의 각 요소 $E_{ij}$는 다음 수식에 따라 결정됩니다:
$$
E_{ij} = \begin{cases}
1_{\tau}, & \text{if } j - i = k \\
0_{\tau}, & \text{otherwise}
\end{cases}
$$
여기서 $i$는 행 인덱스, $j$는 열 인덱스입니다. $1_\tau$와 $0_\tau$는 지정된 `dtype`($\tau$)으로 표현된 1과 0을 의미합니다. 만약 지정된 대각선이 행렬 범위를 벗어나면, 해당 대각선의 모든 요소는 0으로 채워집니다.

**구체적 예시**:

```python
import numpy as np

# 1. 3x3 항등 행렬 (기본 k=0)
arr1 = np.eye(3)
print("np.eye(3):\n", arr1)

# 2. 4x4 행렬, k=1 (주 대각선보다 위에 1이 위치)
arr2 = np.eye(4, k=1)
print("\nnp.eye(4, k=1):\n", arr2)

# 3. 5x3 직사각 행렬, k=-1 (주 대각선보다 아래에 1이 위치)
arr3 = np.eye(5, M=3, k=-1)
print("\nnp.eye(5, M=3, k=-1):\n", arr3)

# 4. k가 행렬 범위를 벗어나는 경우 (모두 0)
arr4 = np.eye(3, k=3)
print("\nnp.eye(3, k=3):\n", arr4)

# 5. 데이터 타입 지정 (정수형)
arr5 = np.eye(2, dtype=int)
print("\nnp.eye(2, dtype=int):\n", arr5)
```

**시험 포인트**:

*   ⭐ `np.eye` 함수가 생성하는 행렬의 특성(`1`과 `0`으로 구성된 대각 행렬)과 `np.identity` (정사각 항등 행렬만 생성)와의 차이점을 이해하는 것이 중요합니다. `np.eye`는 직사각 행렬과 대각선 이동(`k` 매개변수)이 가능합니다.
*   ⭐ `k` 매개변수의 역할(`k=0`은 주 대각선, `k>0`은 위, `k<0`은 아래)을 정확히 알고, 주어진 `N`, `M`, `k` 값으로 생성될 행렬의 형태를 예측할 수 있어야 합니다.
*   ⭐ 선형대수학에서 항등 행렬 $I$의 개념과 `np.eye`로 이를 생성하는 방법, 그리고 `$\lambda I$` 형태의 정규화(regularization) 등 실제 응용 사례를 연결하여 이해해두세요.
*   `j - i = k` 수식의 의미를 이해하고, 특정 `(i, j)` 위치의 원소가 `1`이 될 조건을 설명할 수 있어야 합니다.

---
## Slide 30

**핵심 개념**
*   **k-th Diagonal (k번째 대각선)**: 행렬 $A \in \mathbb{R}^{N \times M}$에서 $k$-th diagonal은 행렬 요소 $A_{i,j}$ 중 열 인덱스($j$)와 행 인덱스($i$)의 차이($j-i$)가 $k$와 같은 모든 요소들의 집합입니다. NumPy에서는 0-based 인덱싱을 사용합니다.
*   **k의 의미**:
    *   $k=0$: 주 대각선(main diagonal)을 나타냅니다. ($j=i$)
    *   $k>0$: 주 대각선 위에 있는 대각선들(superdiagonals)을 나타냅니다. $k$가 커질수록 더 위에 있는 대각선입니다.
    *   $k<0$: 주 대각선 아래에 있는 대각선들(subdiagonals)을 나타냅니다. $k$가 작아질수록 더 아래에 있는 대각선입니다.

**코드/수식 해설**
*   **k-th diagonal의 정의 (집합 표기)**:
    행렬 $A$의 $k$-th diagonal은 다음과 같이 정의됩니다.
    $$\{ A_{i,j} \mid j - i = k, 0 \le i < N, 0 \le j < M \}$$
    여기서 $N$은 행렬의 행 수, $M$은 열 수이며, $i$와 $j$는 각각 행과 열 인덱스를 나타냅니다. 이 정의는 인덱스 $(i, j)$가 행렬 범위 내에 있으면서 $j-i=k$를 만족하는 모든 요소를 포함한다는 의미입니다.

*   **k-th diagonal의 길이 (Length)**:
    *   **$N \times M$ 크기의 일반 행렬에 대한 길이 $L$**:
        $$L = \max(0, \min(N - \max(0, -k), M - \max(0, k)))$$
        이 공식은 $k$ 값에 따라 대각선이 시작하는 행/열이 달라지고, 그에 따라 유효한 행/열의 수가 변화하는 것을 반영하여 대각선의 길이를 계산합니다. `max(0, -k)`는 음수 $k$를 양수로 만들어 행 제한에 영향을 주고, `max(0, k)`는 양수 $k$를 그대로 두어 열 제한에 영향을 줍니다.
    *   **$n \times n$ 크기의 정사각형 행렬에 대한 길이 $L$**:
        $$L = \max(0, n - |k|)$$
        정사각형 행렬의 경우, 대각선의 길이는 행렬의 차원 $n$에서 $|k|$ (k의 절댓값)을 뺀 값이 됩니다. 만약 $|k|$가 $n$보다 크거나 같으면, 해당 대각선은 존재하지 않으므로 길이는 0이 됩니다.

**구체적 예시**
주어진 $4 \times 5$ 행렬 $A$를 예로 들어봅시다.
$$A = \begin{bmatrix} a_{0,0} & a_{0,1} & a_{0,2} & a_{0,3} & a_{0,4} \\ a_{1,0} & a_{1,1} & a_{1,2} & a_{1,3} & a_{1,4} \\ a_{2,0} & a_{2,1} & a_{2,2} & a_{2,3} & a_{2,4} \\ a_{3,0} & a_{3,1} & a_{3,2} & a_{3,3} & a_{3,4} \end{bmatrix}$$

*   **$k=0$ (주 대각선)**: $j-i=0 \implies j=i$를 만족하는 요소들.
    $(a_{0,0}, a_{1,1}, a_{2,2}, a_{3,3})$
    길이: $L = \max(0, \min(4 - \max(0, 0), 5 - \max(0, 0))) = \min(4, 5) = 4$.

*   **$k=1$ (첫 번째 상위 대각선)**: $j-i=1 \implies j=i+1$을 만족하는 요소들.
    $(a_{0,1}, a_{1,2}, a_{2,3}, a_{3,4})$
    길이: $L = \max(0, \min(4 - \max(0, -1), 5 - \max(0, 1))) = \min(4 - 0, 5 - 1) = \min(4, 4) = 4$.

*   **$k=-1$ (첫 번째 하위 대각선)**: $j-i=-1 \implies j=i-1$을 만족하는 요소들.
    $(a_{1,0}, a_{2,1}, a_{3,2})$
    길이: $L = \max(0, \min(4 - \max(0, 1), 5 - \max(0, -1))) = \min(4 - 1, 5 - 0) = \min(3, 5) = 3$.

**NumPy를 이용한 예시**:
NumPy에서는 `np.diag()` 함수를 사용하여 특정 대각선 요소를 추출할 수 있습니다. `k` 인자는 대각선의 위치를 지정합니다 (슬라이드의 $k$와 동일).

```python
import numpy as np

# 예시 행렬 (4x5)
A = np.array([
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19]
])

print("Matrix A:")
print(A)

# k=0 (주 대각선) 추출
diag_k0 = np.diag(A, k=0)
print(f"\nk=0 diagonal (main): {diag_k0}") # 결과: [ 0  6 12 18]

# k=1 (첫 번째 상위 대각선) 추출
diag_k1 = np.diag(A, k=1)
print(f"k=1 diagonal (super): {diag_k1}") # 결과: [ 1  7 13 19]

# k=-1 (첫 번째 하위 대각선) 추출
diag_k_neg1 = np.diag(A, k=-1)
print(f"k=-1 diagonal (sub): {diag_k_neg1}") # 결과: [ 5 11 17]

# 정사각형 행렬 (3x3)에 대한 길이 예시
B = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]) # n=3

# k=0 (주 대각선) 길이: L = max(0, 3 - |0|) = 3
# k=1 (상위 대각선) 길이: L = max(0, 3 - |1|) = 2
# k=2 (상위 대각선) 길이: L = max(0, 3 - |2|) = 1
# k=3 (존재하지 않음) 길이: L = max(0, 3 - |3|) = 0
```

**시험 포인트**
*   ⭐ **k-th diagonal의 정의**: $j-i=k$ 관계를 정확히 이해하고, $k$ 값에 따른 대각선의 위치(주 대각선, 상위 대각선, 하위 대각선)를 설명할 수 있어야 합니다.
*   ⭐ **NumPy `np.diag(matrix, k=...)` 함수의 기능**: 특정 $k$ 값에 해당하는 대각선 요소를 효율적으로 추출하는 방법을 알고 실제 코드에서 활용할 수 있어야 합니다.
*   ⭐ **대각선의 길이 계산**: 특히 정사각형 행렬($n \times n$)의 경우 $L = \max(0, n - |k|)$ 공식을 이해하고 이를 통해 대각선의 유효한 길이를 예측할 수 있어야 합니다.

---
## Slide 31

---
### `np.diag` 함수 활용: 대각 행렬 생성 및 추출

`np.diag` 함수는 NumPy에서 배열의 차원에 따라 대각 행렬을 생성하거나 기존 행렬에서 대각 요소를 추출하는 두 가지 중요한 기능을 수행합니다. 이 함수의 동작 방식을 이해하는 것은 선형 대수 및 행렬 연산을 다루는 데 필수적입니다.

---

**핵심 개념**

NumPy의 `np.diag` 함수는 입력 데이터의 형태(1차원 벡터 또는 2차원 행렬)에 따라 동작이 달라집니다.

1.  **벡터 입력**: 1차원 배열(벡터)이 주어지면, 해당 벡터의 요소를 주대각선(main diagonal) 또는 오프셋(offset) 대각선으로 하는 2차원 대각 행렬을 **생성**합니다.
2.  **행렬 입력**: 2차원 배열(행렬)이 주어지면, 해당 행렬의 주대각선 또는 오프셋 대각선 요소를 **추출**하여 1차원 배열로 반환합니다.

`k` 인수는 대각선의 위치를 지정합니다:
*   `k = 0`: 주대각선 (기본값)
*   `k > 0`: `k`번째 상부 대각선 (superdiagonal)
*   `k < 0`: `k`번째 하부 대각선 (subdiagonal)

---

**코드/수식 해설**

**1. 벡터로부터 대각 행렬 생성 (Construct from a vector)**

*   **기본 주대각선 생성 ($k=0$)**
    주어진 1차원 벡터 $v$를 사용하여 주대각선에 $v$의 요소를 배치하고 나머지는 0으로 채워진 대각 행렬을 생성합니다.
    ```python
    import numpy as np

    v = np.array([9, 8, 7])
    diag_matrix_k0 = np.diag(v)
    print(diag_matrix_k0)
    ```
    수식 표현:
    $$
    v = \begin{bmatrix} 9 \\ 8 \\ 7 \end{bmatrix} \implies \text{np.diag}(v) = \begin{bmatrix} 9 & 0 & 0 \\ 0 & 8 & 0 \\ 0 & 0 & 7 \end{bmatrix}
    $$

*   **상부 대각선 생성 ($k > 0$)**
    `k` 값을 양수로 지정하면, 벡터 `v`의 요소들이 주대각선보다 위에 위치하는 상부 대각선에 배치됩니다. 이때, 생성되는 행렬의 크기는 벡터 `v`의 길이와 `k` 값에 따라 자동으로 조절됩니다.
    ```python
    import numpy as np

    v = np.array([9, 8, 7])
    diag_matrix_k1 = np.diag(v, k=1)
    print(diag_matrix_k1)
    ```
    수식 표현:
    $$
    v = \begin{bmatrix} 9 \\ 8 \\ 7 \end{bmatrix} \implies \text{np.diag}(v, k=1) = \begin{bmatrix} 0 & 9 & 0 & 0 \\ 0 & 0 & 8 & 0 \\ 0 & 0 & 0 & 7 \\ 0 & 0 & 0 & 0 \end{bmatrix}
    $$

**2. 행렬로부터 대각 요소 추출 (Extract from a matrix)**

*   **주대각선 추출 ($k=0$)**
    주어진 2차원 행렬 $A$에서 주대각선에 해당하는 요소를 추출하여 1차원 배열로 반환합니다.
    ```python
    import numpy as np

    A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    main_diagonal = np.diag(A)
    print(main_diagonal)
    ```
    수식 표현:
    $$
    A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix} \implies \text{np.diag}(A) = \begin{bmatrix} 1 \\ 5 \\ 9 \end{bmatrix}
    $$

*   **하부 대각선 추출 ($k < 0$)**
    `k` 값을 음수로 지정하면, 주대각선보다 아래에 위치하는 하부 대각선의 요소들을 추출합니다.
    ```python
    import numpy as np

    A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    sub_diagonal_k_neg1 = np.diag(A, k=-1)
    print(sub_diagonal_k_neg1)
    ```
    수식 표현:
    $$
    A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix} \implies \text{np.diag}(A, k=-1) = \begin{bmatrix} 4 \\ 8 \end{bmatrix}
    $$

---

**구체적 예시**

어떤 데이터 분석 프로젝트에서 이미지 처리 시, 필터의 대각선 성분만으로 새로운 필터를 만들거나, 행렬의 특정 대각선 방향의 변화량을 분석할 때 `np.diag`를 유용하게 사용할 수 있습니다.

**예시 1: 데이터 특성을 대각 행렬로 표현하기**
만약 각 도시의 인구수, 면적, 경제 규모와 같은 세 가지 독립적인 특성을 나타내는 벡터 `[인구, 면적, 경제]`가 있고, 이 특성들이 서로에게 미치는 영향이 없다고 가정하여 독립적인 가중치 행렬을 구성하고 싶다면, `np.diag`를 활용하여 각 특성만을 반영하는 대각 행렬을 쉽게 만들 수 있습니다.

```python
# 도시의 중요도 지표 (벡터)
city_importance_factors = np.array([0.9, 0.8, 0.7])

# 이 지표를 주대각선으로 하는 가중치 행렬 생성
weight_matrix = np.diag(city_importance_factors)
print("가중치 행렬:\n", weight_matrix)

# 만약 한 칸 옆 대각선에 중요도 지표를 배치하고 싶다면 (k=1)
shifted_weight_matrix = np.diag(city_importance_factors, k=1)
print("\nShifted 가중치 행렬 (k=1):\n", shifted_weight_matrix)
```

**예시 2: 데이터 매트릭스에서 특정 추세 추출**
주식 가격 변화를 기록한 3x3 행렬이 있다고 가정해 봅시다. 여기서 대각선은 특정 시점의 가격을, 대각선 주변 요소들은 그 전후의 가격 변동을 나타낼 수 있습니다. 특정 기간 동안의 주된 가격 흐름(주대각선)이나 특정 패턴(상/하부 대각선)을 빠르게 추출하여 분석할 수 있습니다.

```python
# 3일간의 주식 가격 변화 행렬 (예시)
stock_prices = np.array([[100, 102, 105],
                         [ 98, 101, 104],
                         [ 95,  99, 103]])

# 주된 가격 흐름 (주대각선) 추출
main_trend = np.diag(stock_prices)
print("주된 가격 흐름 (주대각선):\n", main_trend)

# 하루 전 가격과의 비교 추세 (k=-1) 추출 (하부 대각선)
prev_day_comparison = np.diag(stock_prices, k=-1)
print("\n하루 전 가격 비교 추세 (하부 대각선, k=-1):\n", prev_day_comparison)
```

---

**시험 포인트**

*   ⭐ `np.diag`는 **입력 배열의 차원**에 따라 **행렬 생성**과 **대각선 추출**이라는 전혀 다른 두 가지 기능을 수행한다는 것을 정확히 이해해야 합니다.
    *   1D array (vector) 입력 $\implies$ 2D array (matrix) 출력 (construct)
    *   2D array (matrix) 입력 $\implies$ 1D array (vector) 출력 (extract)
*   ⭐ `k` 파라미터의 역할을 숙지하세요: `k=0` (주대각선), `k>0` (상부 대각선), `k<0` (하부 대각선).
*   ⭐ 벡터로 행렬을 생성할 때 `k` 값이 양수 또는 음수가 되면, 결과 행렬의 크기가 자동으로 확장될 수 있음을 기억해야 합니다.
---

---
## Slide 32

**핵심 개념**:
`np.diag` 함수는 NumPy 배열에서 대각선(diagonal)을 **생성(construct)**하거나 **추출(extract)**하는 데 사용됩니다. `k` 파라미터를 통해 주 대각선(main diagonal, $k=0$)뿐만 아니라 오프셋된 대각선도 다룰 수 있습니다. 입력이 1차원 벡터인지, 2차원 행렬인지에 따라 기능이 달라집니다.

**코드/수식 해설**:

1.  **벡터 입력 (대각 행렬 생성)**
    `np.diag(v, k=0)`에 1차원 벡터 `v`를 입력하면, `v`의 원소를 `k`번째 대각선에 배치하고 나머지는 0으로 채워진 2차원 배열(행렬)을 생성합니다.
    *   $v$: 길이 $L$인 1차원 벡터
    *   $k$: 대각선의 오프셋. $k=0$은 주 대각선, $k>0$은 위쪽 대각선, $k<0$은 아래쪽 대각선을 의미합니다.
    *   생성되는 행렬 $D$의 원소는 다음과 같습니다:
        $$D_{i, i+k} = v_i \quad (\text{zeros elsewhere})$$
    *   출력되는 2차원 배열의 형태(shape)는 다음과 같습니다:
        $$(L + |k|) \times (L + |k|)$$

2.  **행렬 입력 (대각선 추출)**
    `np.diag(A, k=0)`에 $N \times M$ 크기의 2차원 배열(행렬) `A`를 입력하면, `A`의 `k`번째 대각선 원소들을 추출하여 1차원 배열로 반환합니다.
    *   $A$: $N \times M$ 크기의 2차원 배열
    *   $k$: 추출할 대각선의 오프셋.
    *   추출된 1차원 배열의 길이는 다음과 같습니다:
        $$ \begin{cases} \min(N, M - k) & \text{if } k \ge 0 \\ \min(N + k, M) & \text{if } k < 0 \end{cases} $$
    *   이는 $A_{i, i+k}$ 형태의 모든 유효한 원소들을 포함합니다.

3.  **관련 함수**:
    *   `np.diagonal(a, offset=0, axis1=0, axis2=1)`: N차원 배열에서 지정된 축들을 따라 대각선 원소들을 반환합니다. `np.diag`보다 더 일반적인 N차원 대각선 추출에 사용됩니다.
    *   `np.fill_diagonal(a, val, wrap=True)`: 2차원 배열의 주 대각선을 특정 값으로 채웁니다. 원본 배열을 직접 수정합니다(in-place operation).

**구체적 예시**:

```python
import numpy as np

# 1. 벡터 입력 (대각 행렬 생성)
v = np.array([1, 2, 3])

print("--- 벡터 입력 예시 ---")
# k=0 (주 대각선)
diag_matrix_0 = np.diag(v)
print("np.diag(v, k=0):\n", diag_matrix_0)
# 출력 형태: (3+|0|) x (3+|0|) = 3x3

# k=1 (위쪽 대각선)
diag_matrix_1 = np.diag(v, k=1)
print("\nnp.diag(v, k=1):\n", diag_matrix_1)
# 출력 형태: (3+|1|) x (3+|1|) = 4x4

# k=-1 (아래쪽 대각선)
diag_matrix_neg1 = np.diag(v, k=-1)
print("\nnp.diag(v, k=-1):\n", diag_matrix_neg1)
# 출력 형태: (3+|-1|) x (3+|-1|) = 4x4


# 2. 행렬 입력 (대각선 추출)
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print("\n--- 행렬 입력 예시 ---")
print("Original Matrix A (shape: {}):\n{}".format(A.shape, A))

# k=0 (주 대각선)
diag_extract_0 = np.diag(A)
print("\nnp.diag(A, k=0):", diag_extract_0)
# 추출 길이: min(3, 4 - 0) = 3

# k=1 (위쪽 대각선)
diag_extract_1 = np.diag(A, k=1)
print("np.diag(A, k=1):", diag_extract_1)
# 추출 길이: min(3, 4 - 1) = 3

# k=-1 (아래쪽 대각선)
diag_extract_neg1 = np.diag(A, k=-1)
print("np.diag(A, k=-1):", diag_extract_neg1)
# 추출 길이: min(3 + (-1), 4) = min(2, 4) = 2

# k=3 (가장 오른쪽 위 대각선)
diag_extract_3 = np.diag(A, k=3)
print("np.diag(A, k=3):", diag_extract_3)
# 추출 길이: min(3, 4 - 3) = 1


# 3. np.fill_diagonal 예시
matrix_to_fill = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])
print("\n--- np.fill_diagonal 예시 ---")
print("Matrix before fill_diagonal:\n", matrix_to_fill)
np.fill_diagonal(matrix_to_fill, 99) # 주 대각선을 99로 채움 (원본 배열 수정)
print("Matrix after fill_diagonal(99):\n", matrix_to_fill)
```

**시험 포인트**:
*   ⭐ `np.diag`는 입력이 **벡터**일 때 대각 행렬을 **생성**하고, 입력이 **행렬**일 때 대각선을 **추출**하는 이중적인 기능을 가짐을 정확히 이해하고 구분해야 합니다.
*   ⭐ `k` 파라미터의 역할(대각선 오프셋)을 숙지하고, 양수/음수 값에 따른 대각선 위치 변화를 알아야 합니다 ($k=0$ 주 대각선, $k>0$ 위쪽, $k<0$ 아래쪽).
*   ⭐ 벡터 입력 시 생성되는 행렬의 **크기(shape)**를 계산할 수 있어야 합니다. (공식: $(L+|k|) \times (L+|k|)$)
*   ⭐ 행렬 입력 시 추출되는 대각선 1차원 배열의 **길이**를 계산할 수 있어야 합니다. (공식: $k \ge 0$ 일 때 $\min(N, M - k)$, $k < 0$ 일 때 $\min(N + k, M)$)
*   `np.diagonal`은 다차원 배열에 대한 대각선 추출에 더 일반적이며, `np.fill_diagonal`은 2차원 배열의 주 대각선을 직접 수정(in-place)한다는 점을 기억하세요.

---
## Slide 33

**핵심 개념**:
NumPy Broadcasting은 서로 다른 shape을 가진 두 배열에 대해 산술 연산(덧셈, 뺄셈, 곱셈 등)을 수행할 수 있도록 하는 강력한 기능입니다. NumPy는 작은 배열의 데이터를 더 큰 배열의 shape에 맞춰 자동으로 "반복(repeat)"하여 확장하는 방식으로 연산을 가능하게 하며, 이는 명시적으로 배열을 복사하거나 반복하는 코드를 작성할 필요 없이 효율적으로 연산을 수행하게 해줍니다.

**코드/수식 해설**:
```python
import numpy as np

# 배열 A 초기화: np.arange(6)으로 [0, 1, 2, 3, 4, 5] 생성 후 (2, 3) shape으로 재구성
A = np.arange(6).reshape(2, 3) # shape (2, 3)
# A는 다음과 같습니다:
# [[0, 1, 2],
#  [3, 4, 5]]

# 배열 b 초기화: 1차원 배열
b = np.array([10, 20, 30]) # shape (3,)

# 배열 c 초기화: 2차원 배열 (세로 벡터 형태)
c = np.array([[100], [200]]) # shape (2, 1)

# Y1 = A + b 연산 해설:
# A.shape: (2, 3)
# b.shape: (3,)
# 브로드캐스팅 규칙 적용:
# 1. 두 배열의 shape을 오른쪽부터 정렬하고 비교합니다. 짧은 b는 (1, 3)으로 간주될 수 있습니다.
#    A: (2, 3)
#    b: (1, 3)  (내부적으로 차원 확장)
# 2. 각 차원(axis)을 비교합니다:
#    - 마지막 차원: A의 3과 b의 3은 같으므로 OK. 결과 차원은 3.
#    - 두 번째(가장 왼쪽) 차원: A의 2와 b의 1은 다르지만, 하나가 1이므로 OK. 1은 2로 확장. 결과 차원은 2.
# 3. 결과 shape: (2, 3)
# 연산 과정: b 배열이 A의 각 행에 대해 반복되어 더해집니다.
# Y1 = [[0+10, 1+20, 2+30],  => [10, 21, 32]
#       [3+10, 4+20, 5+30]]  => [13, 24, 35]

# Y2 = A + c 연산 해설:
# A.shape: (2, 3)
# c.shape: (2, 1)
# 브로드캐스팅 규칙 적용:
# 1. 두 배열의 shape을 오른쪽부터 정렬하고 비교합니다.
#    A: (2, 3)
#    c: (2, 1)
# 2. 각 차원(axis)을 비교합니다:
#    - 마지막 차원: A의 3과 c의 1은 다르지만, 하나가 1이므로 OK. 1은 3으로 확장. 결과 차원은 3.
#    - 두 번째(가장 왼쪽) 차원: A의 2와 c의 2는 같으므로 OK. 결과 차원은 2.
# 3. 결과 shape: (2, 3)
# 연산 과정: c 배열이 A의 각 열에 대해 반복되어 더해집니다.
# Y2 = [[0+100, 1+100, 2+100],  => [100, 101, 102]
#       [3+200, 4+200, 5+200]]  => [203, 204, 205]

print(Y1.shape, Y2.shape)
# 출력: (2, 3) (2, 3)
print(Y1[0], Y2[0]) # 첫 번째 행 출력
# 출력: [10 21 32] [100 101 102]
```

**브로드캐스팅 규칙 요약**:
두 배열의 shape을 `(d1, d2, ..., dn)`과 `(e1, e2, ..., em)` (여기서 $n \ge m$)이라고 할 때, 브로드캐스팅은 다음 규칙을 따릅니다:
1.  **차원 정렬**: 두 배열의 shape을 오른쪽부터 정렬합니다. 더 적은 차원을 가진 배열은 왼쪽에 1을 채워 차원 수를 맞춥니다 (예: `(3,)`는 `(1, 3)`으로 간주).
2.  **차원 호환성**: 각 차원(axis)에 대해 다음 조건 중 하나를 만족해야 합니다.
    *   두 차원의 크기가 같다.
    *   두 차원 중 하나의 크기가 1이다.
    만약 이 조건을 만족하지 않는 차원이 하나라도 있다면, 브로드캐스팅은 불가능하며 에러가 발생합니다.
3.  **확장 (Repeating)**: 크기가 1인 차원은 다른 배열의 해당 차원 크기에 맞게 논리적으로 확장(반복)됩니다. 이때 실제 데이터가 복사되는 것이 아니라, 마치 확장된 것처럼 동작하여 메모리 효율적입니다.
4.  **결과 Shape**: 연산 결과 배열의 각 차원 크기는 두 배열의 해당 차원 크기 중 더 큰 값으로 결정됩니다 (규칙 2를 만족하는 경우).

**구체적 예시**:
당신이 여러 학생(2명)의 3가지 과목(수학, 영어, 과학) 점수 데이터를 2D NumPy 배열 `A`로 가지고 있다고 상상해 봅시다.
*   **`A + b`**: 만약 `b`가 [과목별 가산점] (예: [수학+10점, 영어+20점, 과학+30점])이라면, 브로드캐스팅은 `b`를 모든 학생의 점수에 각각 적용합니다. 즉, 1번 학생의 수학, 영어, 과학 점수에 `b`가 더해지고, 2번 학생의 수학, 영어, 과학 점수에도 `b`가 더해집니다. `b`가 각 행에 대해 "반복"되는 효과를 줍니다.
*   **`A + c`**: 만약 `c`가 [[반 전체 가산점1], [반 전체 가산점2]]와 같이 학생 그룹별 가산점이라면, 브로드캐스팅은 `c`를 각 학생의 모든 과목 점수에 적용합니다. 즉, 1번 학생의 모든 과목 점수에 100점이 더해지고, 2번 학생의 모든 과목 점수에 200점이 더해집니다. `c`가 각 열에 대해 "반복"되는 효과를 줍니다.
이처럼 브로드캐스팅은 명시적인 반복문 없이 대규모 데이터에 효율적으로 일괄적인 연산을 적용할 수 있게 해줍니다.

**시험 포인트**:
*   ⭐ **브로드캐스팅의 정의**: 서로 다른 shape의 배열 간 연산을 가능하게 하는 NumPy의 기능이며, 효율성을 위해 데이터 복사 없이 논리적으로 확장됨을 이해합니다.
*   ⭐ **브로드캐스팅 규칙**: 특히 `shape`을 **오른쪽**부터 비교하며, 각 차원에서 크기가 같거나 **둘 중 하나가 1**이어야 한다는 두 가지 핵심 규칙을 정확히 기억해야 합니다.
*   ⭐ 주어진 두 배열의 shape을 보고 브로드캐스팅 **가능 여부**와 브로드캐스팅이 성공할 경우 **결과 배열의 shape**를 정확히 예측할 수 있어야 합니다.
*   ⭐ 실제 연산이 어떻게 일어나는지 (어떤 배열이 어떻게 확장되어 다른 배열과 더해지는지) 이해하고, 결과 배열의 **특정 원소 값**을 계산할 수 있어야 합니다. (예: `Y1[0, 1]`의 값은 얼마인가?)

---
## Slide 34

**핵심 개념**:
NumPy의 브로드캐스팅(Broadcasting)은 서로 다른 형태(shape)의 배열 간에 이항 연산(예: 덧셈, 뺄셈, 곱셈)을 가능하게 하는 강력한 기능입니다. 배열의 차원 수가 다르거나, 차원 수는 같지만 각 차원의 크기가 다를 때, NumPy는 작은 크기의 배열을 더 큰 배열의 형태로 '늘려서'(stretch) 연산을 수행합니다. 이는 명시적으로 배열을 복제하는 것보다 훨씬 효율적입니다.

브로드캐스팅이 가능하려면 두 배열의 차원(dimension)을 뒤에서부터(오른쪽부터) 비교했을 때 다음 규칙을 만족해야 합니다.
1.  두 차원의 크기가 같아야 합니다.
2.  둘 중 하나의 차원 크기가 1이어야 합니다. 이 경우, 크기가 1인 차원이 다른 차원의 크기에 맞춰 늘려집니다.
3.  한 배열이 아예 차원을 가지고 있지 않은 경우(스칼라), 해당 스칼라 값이 모든 요소에 적용됩니다.

위 규칙을 만족하지 않으면 브로드캐스팅은 불가능하며 `ValueError`가 발생합니다. 예를 들어, 슬라이드에서 `(4 \times 3)` 배열과 `(1 \times 3)` 또는 `(4 \times 1)` 배열 간의 연산이 브로드캐스팅 규칙에 따라 성공적으로 수행되는 것을 볼 수 있습니다.

**코드/수식 해설**:
슬라이드에 명시된 수식은 없지만, NumPy 배열 연산 예시를 통해 브로드캐스팅 과정을 설명할 수 있습니다. 각 연산의 최종 형태는 브로드캐스팅 규칙에 따라 결정됩니다.

```python
import numpy as np

# 예시 1: 같은 shape의 배열 덧셈 (브로드캐스팅 필요 없음)
# 4x3 array + 4x3 array -> 4x3 array
arr1 = np.array([[0,0,0], [10,10,10], [20,20,20], [30,30,30]])
arr2 = np.array([[0,1,2], [0,1,2], [0,1,2], [0,1,2]])
result1 = arr1 + arr2
print("--- 예시 1 결과 (4x3 + 4x3) ---")
print(result1)
# 출력:
# [[ 0  1  2]
#  [10 11 12]
#  [20 21 22]
#  [30 31 32]]

# 예시 2: 4x3 배열 + 1x3 (또는 1차원 배열)
# arr3 (shape (4,3)) + arr4 (shape (3,))
# NumPy는 arr4를 (1,3)으로 간주하여 arr3의 각 행에 대해 브로드캐스팅합니다.
# (4,3) + (1,3) -> (4,3)
arr3 = np.array([[0,0,0], [10,10,10], [20,20,20], [30,30,30]])
arr4 = np.array([0,1,2]) # shape (3,), 브로드캐스팅 시 (1,3)으로 간주
result2 = arr3 + arr4
print("\n--- 예시 2 결과 (4x3 + [0,1,2]) ---")
print(result2)
# 출력:
# [[ 0  1  2]
#  [10 11 12]
#  [20 21 22]
#  [30 31 32]]

# 예시 3: 4x1 배열 + 1x3 (또는 1차원 배열)
# arr5 (shape (4,1)) + arr6 (shape (3,))
# arr5는 열 방향으로 stretch되어 (4,3)이 되고, arr6는 (1,3)으로 간주되어 행 방향으로 stretch되어 (4,3)이 됩니다.
# (4,1) + (1,3) -> (4,3)
arr5 = np.array([[0], [10], [20], [30]]) # shape (4,1)
arr6 = np.array([0,1,2]) # shape (3,), 브로드캐스팅 시 (1,3)으로 간주
result3 = arr5 + arr6
print("\n--- 예시 3 결과 (4x1 + [0,1,2]) ---")
print(result3)
# 출력:
# [[ 0  1  2]
#  [10 11 12]
#  [20 21 22]
#  [30 31 32]]
```

**구체적 예시**:

슬라이드의 세 가지 시각적 예시를 통해 브로드캐스팅의 동작 방식을 이해할 수 있습니다. 각 경우 모두 최종 결과는 동일한 $4 \times 3$ 형태의 배열 $\begin{pmatrix} 0 & 1 & 2 \\ 10 & 11 & 12 \\ 20 & 21 & 22 \\ 30 & 31 & 32 \end{pmatrix}$입니다.

1.  **동일한 형태의 배열 덧셈**: $4 \times 3$ 형태의 배열 두 개를 더하는 경우입니다.
    $\begin{pmatrix} 0 & 0 & 0 \\ 10 & 10 & 10 \\ 20 & 20 & 20 \\ 30 & 30 & 30 \end{pmatrix} + \begin{pmatrix} 0 & 1 & 2 \\ 0 & 1 & 2 \\ 0 & 1 & 2 \\ 0 & 1 & 2 \end{pmatrix}$
    두 배열의 형태가 일치하므로 브로드캐스팅이 필요하지 않으며, 각 위치의 요소끼리 바로 더해집니다. 이는 브로드캐스팅이 목표로 하는 최종 결과 형태를 보여주는 기준이 됩니다.

2.  **행 방향 브로드캐스팅**: $4 \times 3$ 배열과 $1 \times 3$ (슬라이드에서는 '3'으로 표현된 1차원 배열 `[0,1,2]`) 배열을 더합니다.
    $\begin{pmatrix} 0 & 0 & 0 \\ 10 & 10 & 10 \\ 20 & 20 & 20 \\ 30 & 30 & 30 \end{pmatrix} + \begin{pmatrix} 0 & 1 & 2 \end{pmatrix}$
    여기서 1차원 배열 `[0,1,2]`는 NumPy에 의해 $(1,3)$ 형태로 간주되고, $4 \times 3$ 배열의 각 행에 적용될 수 있도록 세로 방향으로 '늘려집니다'(stretch). 즉, `[0,1,2]`가 가상적으로 $\begin{pmatrix} 0 & 1 & 2 \\ 0 & 1 & 2 \\ 0 & 1 & 2 \\ 0 & 1 & 2 \end{pmatrix}$ 형태로 확장된 후 첫 번째 배열과 요소별 덧셈이 수행됩니다.

3.  **행과 열 방향 브로드캐스팅**: $4 \times 1$ 형태의 배열과 $1 \times 3$ (슬라이드에서는 '3'으로 표현된 1차원 배열 `[0,1,2]`) 배열을 더합니다.
    $\begin{pmatrix} 0 \\ 10 \\ 20 \\ 30 \end{pmatrix} + \begin{pmatrix} 0 & 1 & 2 \end{pmatrix}$
    *   $4 \times 1$ 배열은 열의 크기가 1이므로, 두 번째 배열의 열 크기(3)에 맞춰 가로 방향으로 '늘려집니다'. 즉, $\begin{pmatrix} 0 & 0 & 0 \\ 10 & 10 & 10 \\ 20 & 20 & 20 \\ 30 & 30 & 30 \end{pmatrix}$처럼 가상적으로 확장됩니다.
    *   동시에 $1 \times 3$ 배열은 행의 크기가 1이므로, 첫 번째 배열의 행 크기(4)에 맞춰 세로 방향으로 '늘려집니다'. 즉, $\begin{pmatrix} 0 & 1 & 2 \\ 0 & 1 & 2 \\ 0 & 1 & 2 \\ 0 & 1 & 2 \end{pmatrix}$처럼 가상적으로 확장됩니다.
    이렇게 두 배열 모두 $4 \times 3$ 형태로 확장된 후 요소별 덧셈이 수행됩니다. 이러한 "늘리기"는 실제 메모리 복사가 아닌 논리적 확장으로, 메모리 효율성을 극대화합니다.

**시험 포인트**:

*   ⭐ **브로드캐스팅의 정의와 목적**: 서로 다른 형태의 배열 간 연산을 효율적으로 가능하게 한다는 핵심 개념을 명확히 이해해야 합니다.
*   ⭐ **브로드캐스팅 규칙**: 두 배열의 차원을 뒤에서부터 비교했을 때 '크기가 같거나' 또는 '둘 중 하나의 크기가 1'이어야 한다는 핵심 규칙을 정확히 알고 있어야 합니다. 이 규칙을 통해 주어진 배열 쌍이 브로드캐스팅 가능한지, 가능하다면 어떤 형태로 확장되어 연산될지 판단할 수 있어야 합니다.
*   ⭐ **시각적 이해 및 예시 적용**: 슬라이드의 예시처럼, 작은 배열이 어떻게 늘려져서 더 큰 배열의 형태에 맞춰지는지 시각적으로 설명하고, 특정 배열 형태 조합($ (N \times 1) + (1 \times M) \rightarrow (N \times M) $ 등)에 대한 브로드캐스팅 과정을 설명할 수 있어야 합니다.
*   ⭐ **코드 적용**: 주어진 NumPy 배열에 대해 브로드캐스팅 연산의 결과를 예측하고, 이를 코드로 구현할 수 있어야 합니다. (예: $ \text{np.array}([[1],[2]]) + \text{np.array}([10,20,30]) $ 의 결과 예측)
*   **주의사항**: 브로드캐스팅 규칙을 만족하지 않으면 `ValueError`가 발생한다는 점도 알아두세요.

---

## Slide 35

**핵심 개념**:
이 슬라이드는 1차원 누적 거리(cumulative distance) 배열로부터 모든 도시 쌍 간의 2차원 거리 배열(pairwise distance matrix)을 구성하는 문제에 대한 소개를 다룹니다. 주어진 `mileposts` 배열은 시카고로부터의 누적 거리를 나타내며, 목표는 이 정보를 이용하여 임의의 두 도시 $i$와 $j$ 사이의 실제 거리를 계산하고 이를 2차원 배열 형태로 표현하는 것입니다. 이는 데이터 분석에서 개체 간의 유사성 또는 관계를 측정할 때 자주 활용되는 기본적인 데이터 전처리 과정입니다.

**코드/수식 해설**:
주어진 1차원 배열 `mileposts`는 각 도시의 시카고로부터의 누적 거리를 마일 단위로 나타냅니다.

```python
# NumPy 배열을 활용하기 위해 import
import numpy as np

# Route 66 상의 도시들의 시카고로부터의 누적 거리 (예시)
mileposts = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
```

두 도시 $i$와 $j$ 사이의 거리는 각 도시의 누적 거리 값의 차이의 절댓값으로 계산됩니다. 도시 $i$의 누적 거리를 $m_i$, 도시 $j$의 누적 거리를 $m_j$라고 할 때, 두 도시 사이의 거리 $D_{ij}$는 다음과 같습니다.

$$ D_{ij} = |m_i - m_j| $$

이 슬라이드에서는 문제의 정의만 다루고 있으며, 이 2차원 거리 배열을 효율적으로 구성하는 구체적인 NumPy 코드는 후속 슬라이드에서 브로드캐스팅(Broadcasting) 등의 개념을 통해 설명될 예정입니다.

**구체적 예시**:
미국 국도 66번(Route 66) 상의 여러 도시들을 예로 들어봅시다. `mileposts` 배열의 첫 번째 값 `0`은 시카고를 의미하며, 이는 기준점입니다.

*   `mileposts[0] = 0` (시카고)
*   `mileposts[1] = 198` (예: 세인트루이스 근처)
*   `mileposts[2] = 303` (예: 다른 중간 도시)
*   `mileposts[9] = 2448` (예: 캘리포니아의 최종 지점)

우리의 목표는 다음과 같은 모든 쌍의 거리를 계산하는 것입니다:

*   **시카고(0마일)와 세인트루이스 근처(198마일) 사이의 거리**: $|0 - 198| = 198$ 마일
*   **세인트루이스 근처(198마일)와 다른 중간 도시(303마일) 사이의 거리**: $|198 - 303| = |-105| = 105$ 마일
*   **시카고(0마일)와 캘리포니아 최종 지점(2448마일) 사이의 거리**: $|0 - 2448| = 2448$ 마일

이처럼 모든 가능한 $N \times N$ 쌍에 대한 거리를 계산하여 2차원 배열(거리 행렬)로 만드는 것이 이 문제의 핵심입니다.

**시험 포인트**:
*   ⭐ **누적 거리(cumulative distance)와 쌍별 거리(pairwise distance)의 차이점**: 1차원 배열이 누적 거리를, 2차원 배열이 쌍별 거리를 나타냄을 명확히 이해해야 합니다.
*   ⭐ **거리 계산의 기본 원리**: 두 지점 $m_i$와 $m_j$ 사이의 거리가 $|m_i - m_j|$로 계산된다는 것을 숙지하세요.
*   ⭐ 이 문제는 NumPy의 **브로드캐스팅(Broadcasting)** 기능을 활용하여 효율적으로 해결하는 대표적인 예시이므로, 해당 개념이 어떻게 적용될지 미리 생각해보고 후속 슬라이드를 통해 학습하는 것이 중요합니다.

---
## Slide 36

- **핵심 개념**:
  이 슬라이드는 1차원(1D) 공간, 즉 단일 도로 모델에서 두 지점(예: 도시) 간의 거리를 'milepost' 개념을 사용하여 정의하는 방법을 설명합니다. 'pairwise distance'는 이러한 방식으로 계산된 모든 가능한 두 지점 쌍 간의 거리를 의미합니다. 핵심은 두 지점의 milepost 값의 절대 차이를 거리로 본다는 것입니다.

- **코드/수식 해설**:
  두 지점 $i$와 $j$ 사이의 거리 $d(i, j)$는 다음과 같은 수식으로 표현됩니다:

  $$d(i, j) = |\text{milepost}(j) - \text{milepost}(i)|$$

  여기서 $\text{milepost}(i)$는 $i$번째 지점의 milepost 값을, $\text{milepost}(j)$는 $j$번째 지점의 milepost 값을 나타냅니다. 1차원 공간에서는 지점의 위치가 단일 숫자로 표현되며, 거리는 항상 양수여야 하므로 두 위치 값의 차이에 절대값을 취합니다.

  이러한 계산은 Python의 NumPy 라이브러리를 통해 효율적으로 수행될 수 있습니다. 예를 들어, 여러 도시의 milepost가 NumPy 배열로 주어졌을 때 두 도시의 거리를 계산하는 것은 다음과 같습니다:

  ```python
  import numpy as np

  # 도시들의 milepost 값 예시
  mileposts = np.array([0, 100, 250]) # 0th city, i-th city, j-th city

  # i-th city (인덱스 1)와 j-th city (인덱스 2) 간 거리
  i_city_idx = 1
  j_city_idx = 2

  distance = np.abs(mileposts[j_city_idx] - mileposts[i_city_idx])
  print(f"Distance between i-th city and j-th city: {distance}")
  ```
  이 개념은 나중에 데이터 분석에서 여러 데이터 포인트 간의 유사성 또는 비유사성을 측정하는 데 사용될 '거리 행렬(distance matrix)'을 구축하는 기초가 됩니다.

- **구체적 예시**:
  슬라이드 그림을 참고하여 milepost 값을 가정해 봅시다.
  - 0th city (Chicago): milepost 0
  - i-th city: milepost 100
  - j-th city: milepost 250

  이때, 각 도시 쌍 간의 거리는 다음과 같습니다.
  - 0th city (Chicago)와 i-th city 간 거리: $|100 - 0| = 100$
  - i-th city와 j-th city 간 거리: $|250 - 100| = 150$
  - 0th city (Chicago)와 j-th city 간 거리: $|250 - 0| = 250$

  이는 직선 상에서 두 지점 사이의 물리적인 거리를 나타내며, 항상 양수의 값을 가집니다.

- **시험 포인트**:
  - ⭐1차원 공간에서 두 지점 간의 거리는 각 지점의 위치(milepost) 값의 **절대 차이**로 정의된다는 것을 정확히 이해하고 수식을 작성할 수 있어야 합니다.
  - ⭐이 기본적인 거리 개념이 향후 데이터 분석, 특히 클러스터링, 분류 등 머신러닝 알고리즘에서 데이터 포인트 간의 유사성을 측정하는 다양한 거리 함수(예: 유클리드 거리, 맨해튼 거리 등)의 기초가 됨을 인지해야 합니다.
  - ⭐NumPy를 활용하여 이러한 1차원 거리 계산을 효율적으로 수행하는 방법에 대한 이해가 중요합니다 (예: `np.abs()`, 배열 인덱싱).

---
## Slide 37

## NumPy 브로드캐스팅을 이용한 거리 계산

---

### 핵심 개념

*   **NumPy 브로드캐스팅 (Broadcasting)**: NumPy 배열 연산 시, 서로 다른 형상(shape)을 가진 배열들을 호환 가능하도록 자동으로 확장하여 연산을 수행하는 강력한 기능입니다. 명시적인 루프나 메모리 복사 없이 효율적인 연산을 가능하게 합니다.
*   **`np.newaxis`**: 배열에 새로운 차원(axis)을 추가하는 데 사용되는 NumPy의 특수 객체입니다. 이를 통해 1차원 배열을 2차원 배열(예: 행 벡터 또는 열 벡터)로 변환하여 브로드캐스팅 규칙을 활용할 수 있습니다.
*   **짝지은 차이 (Pairwise Differences) 계산**: 주어진 배열의 모든 요소 쌍 간의 차이를 계산하여 행렬 형태로 나타내는 문제입니다. 예를 들어, 여러 지점 간의 거리를 모두 구하는 데 활용됩니다.

### 코드/수식 해설

```python
import numpy as np

mileposts = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])

# Broadcasting trick: (N,) and (N,1) -> (N,N)
distance_array = np.abs(mileposts - mileposts[:, np.newaxis])

print(distance_array)
# Each (i,j) entry is |mileposts[j] - mileposts[i]|
```

1.  **`mileposts = np.array(...)`**: `mileposts`라는 이름의 1차원 NumPy 배열을 생성합니다. 이 배열의 형상은 `(N,)`입니다 (여기서 `N=10`).
2.  **`mileposts[:, np.newaxis]`**: `mileposts` 배열에 새로운 축을 추가하여 형상을 `(N, 1)`로 만듭니다. 즉, 1차원 배열을 열 벡터 형태로 변환합니다.
    *   `mileposts`의 형상: `(N,)`
    *   `mileposts[:, np.newaxis]`의 형상: `(N, 1)`
3.  **`mileposts - mileposts[:, np.newaxis]`**: 여기서 브로드캐스팅이 발생합니다.
    *   좌변 `mileposts` (`(N,)` 형상)는 브로드캐스팅 규칙에 따라 `(1, N)` 형상처럼 확장됩니다.
    *   우변 `mileposts[:, np.newaxis]` (`(N, 1)` 형상)는 브로드캐스팅 규칙에 따라 `(N, N)` 형상으로 확장됩니다.
    *   최종 연산 결과는 `(N, N)` 형상의 2차원 배열이 됩니다.

    이 연산의 각 요소 $D_{ij}$는 다음 수식으로 표현됩니다:
    $$ D_{ij} = \text{mileposts}[j] - \text{mileposts}[i] $$
    이는 $i$번째 지점과 $j$번째 지점 간의 차이를 의미합니다.
4.  **`np.abs(...)`**: 위에서 계산된 차이 배열의 모든 요소에 대해 절대값을 취합니다. 거리는 음수가 될 수 없으므로 절대값을 적용하여 양수로 만듭니다. 최종 `distance_array`의 $(i,j)$번째 요소는 $i$번째 지점과 $j$번째 지점 사이의 거리 또는 차이의 절댓값입니다.
    $$ \text{distance\_array}_{ij} = |\text{mileposts}[j] - \text{mileposts}[i]| $$

### 구체적 예시

간단한 예시를 통해 브로드캐스팅 과정을 이해해 봅시다.

`mileposts = np.array([10, 20, 30])` (여기서 `N=3`) 일 경우:

1.  `mileposts`의 형상은 `(3,)`입니다.
2.  `mileposts[:, np.newaxis]`는 `[[10], [20], [30]]` 형태가 되며, 형상은 `(3, 1)`입니다.
3.  `mileposts - mileposts[:, np.newaxis]` 연산 과정:
    *   `mileposts`는 `[[10, 20, 30], [10, 20, 30], [10, 20, 30]]`로 확장됩니다.
    *   `mileposts[:, np.newaxis]`는 `[[10, 10, 10], [20, 20, 20], [30, 30, 30]]`로 확장됩니다.
    *   이 두 확장된 배열이 요소별로 빼기 연산됩니다:

    ```
    [[10, 20, 30],   -   [[10, 10, 10],   =   [[ 0, 10, 20],
     [10, 20, 30],         [20, 20, 20],         [-10, 0, 10],
     [10, 20, 30]]         [30, 30, 30]]         [-20,-10, 0]]
    ```

4.  `np.abs()`를 적용하면:

    ```
    [[ 0, 10, 20],
     [10,  0, 10],
     [20, 10,  0]]
    ```

이 결과는 각 지점(10, 20, 30) 사이의 모든 짝지은 거리(절대 차이)를 나타내는 행렬입니다. 예를 들어, `(0, 1)` 요소는 `|20 - 10| = 10`이고, `(2, 0)` 요소는 `|10 - 30| = 20`입니다.

### 시험 포인트

*   ⭐ **NumPy 브로드캐스팅 규칙**: 서로 다른 형상의 배열이 어떻게 연산될 때 확장되는지 정확히 이해하고 설명할 수 있어야 합니다. 특히 `(N,)`과 `(N,1)` 형상 간의 연산에서 `(N,N)` 결과가 도출되는 과정을 이해하는 것이 중요합니다.
*   ⭐ **`np.newaxis`의 역할**: `np.newaxis`가 배열의 차원을 어떻게 변경하고, 이 변경이 브로드캐스팅에 어떤 영향을 미치는지 설명할 수 있어야 합니다. 이는 1차원 배열을 행/열 벡터로 변환하는 핵심적인 방법입니다.
*   ⭐ **짝지은 차이(Pairwise Differences) 계산 효율성**: 브로드캐스팅을 이용하여 명시적인 `for` 루프 없이 모든 요소 간의 차이를 계산하는 방법을 이해하고 구현할 수 있어야 합니다. 이는 데이터 분석에서 거리 행렬이나 유사도 행렬을 계산할 때 매우 중요합니다.
*   ⭐ **코드 결과 예측**: 주어진 코드 스니펫에서 `distance_array`의 최종 형상(shape)과 특정 `(i,j)` 위치의 값이 무엇을 의미하는지 정확하게 예측하고 설명할 수 있어야 합니다.

---
## Slide 38

**핵심 개념**:
*   **NumPy 브로드캐스팅(Broadcasting)**: 서로 다른 형상(shape)을 가진 배열(array) 간에 산술 연산을 가능하게 하는 NumPy의 강력한 기능입니다. NumPy는 작은 배열을 더 큰 배열의 형상에 맞춰 자동으로 확장(duplicate)하여 연산을 수행합니다. 이를 통해 명시적인 반복문(for-loop) 없이 효율적인 배열 연산이 가능해집니다.
*   **쌍별 차이(Pairwise Difference)**: 두 벡터 `A`와 `B`의 모든 요소 쌍 `(a, b)`에 대해 `a - b` 또는 `b - a`와 같은 차이를 계산하여 새로운 행렬을 생성하는 연산입니다. 이 슬라이드에서는 `Row Vector - Column Vector` 연산을 통해 `M[i, j] = Row Vector[j] - Column Vector[i, 0]` 형태의 쌍별 차이를 계산합니다.

**코드/수식 해설**:
슬라이드에서 제시된 예시는 1차원 배열(Row Vector, 형상 `(10,)`)에서 2차원 배열(Column Vector, 형상 `(10,1)`)을 빼는 연산을 브로드캐스팅을 통해 수행하는 것을 보여줍니다.

```python
import numpy as np

# 슬라이드의 Row Vector와 Column Vector에 사용된 값들
values = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])

# Row Vector (1D array)
row_vector = values  # shape (10,)

# Column Vector (2D array, column vector)
# np.newaxis를 사용하여 1차원 배열을 2차원 열 벡터로 변환 (shape (10, 1))
column_vector = values[:, np.newaxis]

# 브로드캐스팅을 이용한 쌍별 차이 계산
# row_vector (10,) 와 column_vector (10,1) 간의 연산
# NumPy의 브로드캐스팅 규칙에 따라 두 배열의 형상이 (10, 10)으로 확장되어 요소별 뺄셈이 수행됩니다.
result_matrix = row_vector - column_vector

print("Row Vector (10,):\n", row_vector)
print("\nColumn Vector (10,1):\n", column_vector)
print("\nResult Matrix (10,10):\n", result_matrix)
```

**브로드캐스팅 원리**:
1.  **차원 확장**: `row_vector`의 형상 `(10,)`는 연산을 위해 개념적으로 `(1, 10)`으로 확장됩니다. `column_vector`의 형상 `(10,1)`은 그대로 유지됩니다.
2.  **형상 매칭**: NumPy는 `(1, 10)`과 `(10, 1)` 두 배열의 형상을 비교합니다.
    *   첫 번째 차원(행): `1` (row_vector)과 `10` (column_vector)이므로, `row_vector`가 `10`으로 확장됩니다.
    *   두 번째 차원(열): `10` (row_vector)과 `1` (column_vector)이므로, `column_vector`가 `10`으로 확장됩니다.
    *   결과적으로 두 배열 모두 `(10, 10)` 형상으로 확장된 것처럼 동작하며 요소별 연산이 수행됩니다.
3.  **요소별 연산**: 결과 행렬 $M$의 각 요소 $M_{ij}$는 다음과 같이 계산됩니다:
    $$M_{ij} = \text{row\_vector}[j] - \text{column\_vector}[i, 0]$$
    여기서 $i$는 행 인덱스, $j$는 열 인덱스를 나타냅니다.

**구체적 예시**:
위 코드의 `values`를 사용하여 `result_matrix`의 몇몇 요소를 직접 계산해봅시다.
`row_vector = [0, 198, 303, ...]`
`column_vector = [[0], [198], [303], ...]`

*   $M_{0,0} = \text{row\_vector}[0] - \text{column\_vector}[0, 0] = 0 - 0 = 0$
*   $M_{0,1} = \text{row\_vector}[1] - \text{column\_vector}[0, 0] = 198 - 0 = 198$
*   $M_{1,0} = \text{row\_vector}[0] - \text{column\_vector}[1, 0] = 0 - 198 = -198$
*   $M_{1,1} = \text{row\_vector}[1] - \text{column\_vector}[1, 0] = 198 - 198 = 0$
*   $M_{2,1} = \text{row\_vector}[1] - \text{column\_vector}[2, 0] = 198 - 303 = -105$

이 값들은 슬라이드의 `Result Matrix` 내용과 정확히 일치하며, 각 셀이 `(열 벡터의 해당 행 값) - (행 벡터의 해당 열 값)`이 아니라 `(행 벡터의 해당 열 값) - (열 벡터의 해당 행 값)`으로 계산됨을 보여줍니다. 이러한 쌍별 차이 계산은 예를 들어 금융 데이터에서 여러 시점의 주가 간의 모든 가능한 차이(수익률)를 한 번에 계산하거나, 기하학적 거리 행렬을 계산할 때 유용하게 활용될 수 있습니다.

**시험 포인트**:
*   ⭐**NumPy 브로드캐스팅의 기본 규칙 이해**: 두 배열의 차원 수가 다르거나 길이가 다를 때(예: `(N,)` vs `(M,1)`), 어떻게 확장이 일어나 연산이 가능한지 설명할 수 있어야 합니다.
*   ⭐**`np.newaxis` 또는 `.reshape()`를 사용하여 배열의 차원 변경**: 1차원 배열을 명시적으로 행 벡터 `(1, N)` 또는 열 벡터 `(N, 1)`로 변환하는 방법을 알아야 합니다. (예: `arr[:, np.newaxis]` 또는 `arr.reshape(-1, 1)`).
*   ⭐**브로드캐스팅 연산의 결과 형상 예측**: `(N,)`와 `(M,1)` 배열의 연산 결과 형상이 `(M,N)`이 됨을 이해하고, 이 예시에서는 `(10,)`와 `(10,1)`의 연산 결과가 `(10,10)`이 되는 이유를 설명할 수 있어야 합니다.
*   ⭐**브로드캐스팅의 효율성**: 명시적인 반복문(for-loop) 대신 브로드캐스팅을 활용하면 C 언어로 구현된 효율적인 저수준 연산을 사용하므로, 대규모 데이터 처리 시 속도 향상에 큰 이점이 있다는 것을 알아야 합니다.

---
## Slide 39

**핵심 개념**
NumPy 브로드캐스팅(Broadcasting)은 서로 다른 형태(shape)를 가진 두 배열에 대해 산술 연산과 같은 요소별(element-wise) 연산을 수행할 수 있도록 하는 강력한 기능입니다. 이 과정은 크게 두 단계로 나뉩니다: 첫째, 두 배열의 형태를 정렬하고 호환성을 확인합니다. 둘째, 호환 가능한 경우 최종 결과 배열의 형태를 결정합니다.

**코드/수식 해설**

두 배열 $X$와 $Z$가 있다고 가정합니다. $X$의 형태는 $s = (s_1, \dots, s_n)$이고 $Z$의 형태는 $t = (t_1, \dots, t_m)$입니다. NumPy는 `np.add`, `np.maximum`과 같은 요소별 이항 함수 $g$를 적용할 때 다음 규칙을 따릅니다.

**Step A: Right-align & check compatibility (오른쪽 정렬 및 호환성 확인)**

1.  **차원 맞추기**: 두 배열의 차원 수 중 더 큰 값을 $r$로 정의합니다.
    $$ r = \max(n, m) $$
    더 짧은 형태의 배열 앞에 `1`을 붙여서 두 배열의 차원 수를 $r$로 맞춥니다. 이렇게 정렬된 형태를 각각 $\tilde{s}$와 $\tilde{t}$라고 합니다.
    예를 들어, $s=(3,)$ 이고 $t=(2,3)$ 이면 $n=1, m=2$ 이므로 $r=2$ 입니다. $s$의 앞에 `1`을 붙여 $\tilde{s}=(1,3)$ 으로 만들고 $\tilde{t}=(2,3)$ 은 그대로 둡니다.

2.  **호환성 확인**: 각 축(axis) $j$에 대해 다음 조건 중 하나를 만족해야 합니다.
    $$ \tilde{s}_j = \tilde{t}_j \quad \text{or} \quad \tilde{s}_j = 1 \quad \text{or} \quad \tilde{t}_j = 1 $$
    즉, 두 배열의 해당 축 크기가 같거나, 둘 중 하나의 축 크기가 1이어야 합니다.
    만약 어떤 축이라도 이 조건을 만족하지 못하면, NumPy는 `ValueError`를 발생시킵니다.

**Step B: Broadcasted result shape (브로드캐스트된 결과 형태)**

위의 호환성 조건을 만족하면, 브로드캐스트된 결과 배열의 형태 $u$는 각 축 $j$에 대해 두 정렬된 형태의 해당 축 크기 중 최댓값으로 결정됩니다.
$$ u = \text{broadcast}(s, t) := (\max(\tilde{s}_1, \tilde{t}_1), \dots, \max(\tilde{s}_r, \tilde{t}_r)) $$

**구체적 예시**

```python
import numpy as np

# 예시 1: (3, 1) + (1, 4)
# X shape s = (3, 1), Z shape t = (1, 4)
# n=2, m=2 => r=2
# Aligned shapes: s_tilde = (3, 1), t_tilde = (1, 4)
# Axis 0: s_tilde_0=3, t_tilde_0=1 -> Compatible (one is 1)
# Axis 1: s_tilde_1=1, t_tilde_1=4 -> Compatible (one is 1)
# Result shape: (max(3,1), max(1,4)) = (3, 4)
a = np.array([[0], [1], [2]])  # Shape (3, 1)
b = np.array([0, 1, 2, 3])     # Shape (4,)
# b를 (1, 4)로 확장하여 생각
print(f"a.shape: {a.shape}")
print(f"b.shape (original): {b.shape}")
b_reshaped = b.reshape(1, -1) # broadcasting에서는 (4,)를 (1,4)로 간주
print(f"b.shape (effective for broadcasting): {b_reshaped.shape}")
result1 = a + b_reshaped
print(f"Result 1 shape: {result1.shape}")
print(f"Result 1:\n{result1}\n")


# 예시 2: (3, 4) + (4,)
# X shape s = (3, 4), Z shape t = (4,)
# n=2, m=1 => r=2
# Aligned shapes: s_tilde = (3, 4), t_tilde = (1, 4) (앞에 1이 붙음)
# Axis 0: s_tilde_0=3, t_tilde_0=1 -> Compatible (one is 1)
# Axis 1: s_tilde_1=4, t_tilde_1=4 -> Compatible (equal)
# Result shape: (max(3,1), max(4,4)) = (3, 4)
c = np.arange(12).reshape(3, 4) # Shape (3, 4)
d = np.array([10, 20, 30, 40])  # Shape (4,)
print(f"c.shape: {c.shape}")
print(f"d.shape: {d.shape}")
result2 = c + d
print(f"Result 2 shape: {result2.shape}")
print(f"Result 2:\n{result2}\n")

# 예시 3: Incompatible shapes - ValueError 발생
# X shape s = (2, 3), Z shape t = (3, 2)
# n=2, m=2 => r=2
# Aligned shapes: s_tilde = (2, 3), t_tilde = (3, 2)
# Axis 0: s_tilde_0=2, t_tilde_0=3 -> Not compatible (2 != 3, neither is 1)
# Axis 1: s_tilde_1=3, t_tilde_1=2 -> Not compatible (3 != 2, neither is 1)
e = np.array([[1, 2, 3], [4, 5, 6]]) # Shape (2, 3)
f = np.array([[1, 2], [3, 4], [5, 6]]) # Shape (3, 2)
print(f"e.shape: {e.shape}")
print(f"f.shape: {f.shape}")
try:
    _ = e + f
except ValueError as ve:
    print(f"Incompatible shapes for broadcasting: {ve}")
```

**시험 포인트**

*   ⭐ **브로드캐스팅 규칙의 두 가지 주요 단계** (오른쪽 정렬 및 호환성 확인, 결과 형태 결정)를 정확히 이해하고 설명할 수 있어야 합니다.
*   ⭐ **호환성 조건**($\tilde{s}_j = \tilde{t}_j$ 또는 $\tilde{s}_j = 1$ 또는 $\tilde{t}_j = 1$)을 반드시 기억하고 적용할 수 있어야 합니다. 특히 한쪽 차원이 1일 때 확장되는 원리를 중요하게 다룹니다.
*   ⭐ **NumPy가 `ValueError`를 발생시키는 경우** (호환되지 않는 형태)를 인지해야 합니다.
*   ⭐ 주어진 두 배열의 형태에 대해 **브로드캐스팅 가능 여부와 가능하다면 최종 결과 형태를 예측**할 수 있어야 합니다. (예시처럼 단계별로 설명하는 연습이 필요합니다.)

---
## Slide 40

**핵심 개념**
NumPy 브로드캐스팅(Broadcasting)은 서로 다른 형태(shape)를 가진 두 배열 간에 산술 연산을 수행할 때, 배열의 형태를 자동으로 확장하여 연산을 가능하게 하는 메커니즘입니다. 특히 이 슬라이드는 브로드캐스팅된 결과 배열의 특정 위치($i$)에 들어갈 요소를 어떻게 결정하는지, 즉 각 원소를 어떤 인덱스에서 가져와 연산할 것인지에 대한 규칙을 설명합니다.

**코드/수식 해설**

두 배열 $X$와 $Z$가 있고, 이들의 브로드캐스팅된 형태가 각각 $\tilde{s}$와 $\tilde{t}$이며, 결과 배열의 형태가 $u$라고 가정합니다. 결과 배열 $Y$의 특정 위치 $i = (i_1, \dots, i_r)$에 대한 요소 $Y[i]$를 계산하는 규칙은 다음과 같습니다:

1.  **각 축($j$)에 대한 인덱스 결정**:
    *   배열 $X$의 $j$번째 축의 크기가 1($\tilde{s}_j = 1$)인 경우, $X$에서는 해당 축의 인덱스로 항상 0을 사용합니다.
    *   그렇지 않은 경우($\tilde{s}_j \ne 1$), $X$에서는 결과 배열의 인덱스 $i_j$를 그대로 사용합니다.
    *   배열 $Z$의 $j$번째 축의 크기가 1($\tilde{t}_j = 1$)인 경우, $Z$에서는 해당 축의 인덱스로 항상 0을 사용합니다.
    *   그렇지 않은 경우($\tilde{t}_j \ne 1$), $Z$에서는 결과 배열의 인덱스 $i_j$를 그대로 사용합니다.

2.  **연산 수행**:
    위에서 결정된 인덱스를 사용하여 $X$와 $Z$에서 각각 요소를 가져온 후, 정의된 연산 $g$를 수행합니다.
    $$ Y[i] = g(X[\text{picked indices for X}], Z[\text{picked indices for Z}]) $$

예를 들어, 배열 $X$의 브로드캐스팅된 형태가 $\tilde{s} = (2, 3)$이고, 배열 $Z$의 브로드캐스팅된 형태가 $\tilde{t} = (1, 3)$이라고 가정해 봅시다.
이 경우, $Z$의 첫 번째 축($j=0$)의 크기가 1($\tilde{t}_0 = 1$)이므로, $Z$는 결과 배열의 첫 번째 인덱스 $i_0$를 무시하고 항상 인덱스 0을 사용합니다.
반면, $Z$의 두 번째 축($j=1$)의 크기가 3($\tilde{t}_1 = 3$)이고 $X$의 두 번째 축도 3($\tilde{s}_1 = 3$)이므로, $X$와 $Z$ 모두 해당 축에서는 결과 배열의 인덱스 $i_1$을 사용합니다.

따라서, 만약 $Y = X + Z_{\text{broadcast}}$ 연산을 수행한다면, 결과 배열 $Y$의 $(i_0, i_1)$ 위치의 요소는 다음과 같이 계산됩니다:
$$ Y[i_0, i_1] = X[i_0, i_1] + Z[0, i_1] $$

**구체적 예시**

위 예시에서 $X$가 (2,3) 형태의 2차원 배열이고 $Z$가 (1,3) 형태의 2차원 배열이라고 할 때,
$Z_{\text{broadcast}}$는 다음과 같이 확장됩니다.
$Z$가 `[[z0, z1, z2]]` 형태였다면, 브로드캐스팅 규칙에 따라 첫 번째 축이 확장되어 (2,3) 형태가 됩니다.
$$ Z_{\text{broadcast}} = \begin{bmatrix} z_0 & z_1 & z_2 \\ z_0 & z_1 & z_2 \end{bmatrix} $$
여기서 $z_0, z_1, z_2$는 원본 $Z$ 배열의 `Z[0,0]`, `Z[0,1]`, `Z[0,2]` 값입니다.
이는 결국 $Z$의 첫 번째 축이 크기 1이므로, $Y[i_0, i_1]$을 계산할 때 $Z$에서는 항상 첫 번째 축의 인덱스로 0을 사용한다는 규칙을 보여줍니다. $X$의 경우 $\tilde{s}=(2,3)$으로 어떤 축도 1이 아니므로, $X$는 $i_0, i_1$을 그대로 사용합니다.

**시험 포인트**
*   ⭐**브로드캐스팅 시 각 축의 인덱스 선택 규칙**: 특정 축의 크기가 1인 경우 해당 축의 인덱스는 항상 0을 사용하고, 그렇지 않은 경우 결과 배열의 인덱스를 그대로 사용한다는 점을 정확히 이해해야 합니다.
*   ⭐주어진 두 배열의 `shape`와 연산에 대해, 결과 배열의 특정 요소($Y[i_0, i_1]$ 등)가 원본 배열의 어떤 인덱스($X[?,?]$, $Z[?,?]$)에서 값을 가져와 계산되는지 파악하는 문제가 나올 수 있습니다.
*   브로드캐스팅 규칙이 두 배열 중 어느 한 쪽의 차원이 1일 때만 적용되는 것이 아니라, 각 축(axis)별로 독립적으로 적용된다는 것을 기억해야 합니다.

---
## Slide 41

POSTECH 컴퓨터공학과 전공 튜터입니다. 데이터분석 입문 (CSED226) 강의 슬라이드 중 "Broadcasting (many arrays): informal recipe"에 대한 마크다운 노트입니다.

---

### **핵심 개념**

*   **브로드캐스팅 (Broadcasting)**: NumPy에서 서로 다른 형태(shape)를 가진 배열(array) 간에 산술 연산 (pointwise function)을 효율적으로 수행할 수 있도록 배열의 형태를 자동으로 맞춰주는 메커니즘입니다. 명시적인 반복문(loop)이나 배열 복제(replication) 없이 연산을 가능하게 하여 코드를 간결하게 하고 메모리 사용을 최적화합니다.

### **코드/수식 해설**

NumPy 브로드캐스팅의 비공식적인 규칙은 다음과 같습니다:

1.  **차원 수 맞추기 (Right-align shapes)**
    *   연산에 참여하는 모든 배열의 차원(axis) 수를 동일하게 맞춥니다.
    *   차원 수가 부족한 배열은 그 형태의 *선행(leading)* 부분에 크기가 1인 차원을 추가하여 차원 수를 맞춥니다.
    *   예: `(2, 3)` 형태의 배열과 `(3,)` 형태의 배열이 연산할 경우, `(3,)`은 `(1, 3)`으로 변환됩니다.

2.  **축별 호환성 검사 (Axis check)**
    *   모든 배열의 차원 수가 맞춰진 상태에서, 각 축(axis)에 대해 오른쪽부터 왼쪽으로(trailing axes first) 호환성을 검사합니다.
    *   특정 축에서, 모든 배열의 해당 축 크기가 다음 세 가지 조건 중 하나를 만족해야 합니다:
        1.  모든 배열의 해당 축 크기가 *같다*.
        2.  하나 이상의 배열의 해당 축 크기가 *1이다*.
    *   **브로드캐스팅 실패 조건**: ⭐만약 두 배열의 해당 축 크기가 1이 아니면서 서로 다르다면 (예: `(2, 3)`과 `(4, 3)`의 첫 번째 축 2와 4), 브로드캐스팅은 실패하고 `ValueError`가 발생합니다.

3.  **결과 형태 결정 (Result shape)**
    *   각 축의 결과 형태는 연산에 참여하는 배열들의 해당 축 크기 중 *최댓값*으로 결정됩니다.
    *   예: `(4, 1)`과 `(1, 5)`의 연산 결과는 `(4, 5)`가 됩니다 (첫 번째 축: $\max(4, 1) = 4$, 두 번째 축: $\max(1, 5) = 5$).

4.  **값 사용 방식 (How values are used)**
    *   어떤 축의 크기가 1인 배열은 해당 축을 따라 결과 형태의 크기에 맞춰 *개념적으로 확장(stretched)* 또는 *재사용(reused)* 됩니다. 이는 물리적인 데이터 복사 없이 논리적으로 같은 값이 반복되는 것처럼 동작하여 메모리 효율성을 유지합니다.
    *   해당 축의 크기가 결과 형태의 크기와 같은 배열은 인덱스가 변경 없이 그대로 사용됩니다.

5.  **스칼라 처리 (Scalars)**
    *   스칼라(scalar) 값은 형태가 `()`인 배열처럼 취급됩니다. 따라서 어떤 형태의 배열과도 항상 브로드캐스팅될 수 있습니다.

**메모리 주의사항 (Memory note)**
*   브로드캐스팅 자체는 크기가 1인 축을 따라 데이터를 복사하지 않습니다.
*   하지만, 연산의 *결과* 배열은 일반적으로 새로운 메모리 공간에 할당됩니다 (특별히 `out=` 인자를 사용하여 기존 배열에 결과를 저장하는 경우가 아니라면).

### **구체적 예시**

**예시 1: 벡터와 스칼라 덧셈**

```python
import numpy as np

a = np.array([1, 2, 3])  # shape: (3,)
b = 5                    # scalar

# 브로드캐스팅 과정:
# 1. 차원 수 맞추기: (3,) 와 () -> (3,) 와 (1,)
# 2. 축별 호환성 검사:
#    - 첫 번째 축: a는 3, b는 1. (한쪽이 1이므로) 호환성 OK.
# 3. 결과 형태 결정: max(3, 1) = 3 -> (3,)
# 4. 값 사용: 스칼라 b=5는 개념적으로 [5, 5, 5]로 확장되어 a와 요소별로 더해집니다.

c = a + b
print(c)
# 출력: [6 7 8]
```

**예시 2: 서로 다른 차원의 배열 덧셈**

```python
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]]) # shape: (2, 3)

B = np.array([10, 20, 30]) # shape: (3,)

# 브로드캐스팅 과정:
# 1. 차원 수 맞추기: (2, 3) 와 (3,) -> (2, 3) 와 (1, 3)
# 2. 축별 호환성 검사 (오른쪽부터):
#    - 두 번째 축 (index 1): A는 3, B는 3. (크기가 같으므로) 호환성 OK.
#    - 첫 번째 축 (index 0): A는 2, B는 1. (한쪽이 1이므로) 호환성 OK.
# 3. 결과 형태 결정:
#    - 첫 번째 축: max(2, 1) = 2
#    - 두 번째 축: max(3, 3) = 3
#    -> 결과 형태: (2, 3)
# 4. 값 사용: B = [10, 20, 30]은 [[10, 20, 30], [10, 20, 30]]으로 개념적으로 확장되어 A와 더해집니다.

C = A + B
print(C)
# 출력:
# [[11 22 33]
#  [14 25 36]]
```

**예시 3: 브로드캐스팅 실패**

```python
import numpy as np

X = np.array([[1, 2],
              [3, 4]]) # shape: (2, 2)

Y = np.array([10, 20, 30]) # shape: (3,)

# 브로드캐스팅 과정:
# 1. 차원 수 맞추기: (2, 2) 와 (3,) -> (2, 2) 와 (1, 3)
# 2. 축별 호환성 검사 (오른쪽부터):
#    - 두 번째 축 (index 1): X는 2, Y는 3.
#      두 크기가 1이 아니면서 서로 다르다 (2 != 3).
#      -> 브로드캐스팅 실패!

try:
    Z = X + Y
    print(Z)
except ValueError as e:
    print(f"Error: {e}")
# 출력:
# Error: operands could not be broadcast together with shapes (2,2) (3,)
```

### **시험 포인트**

*   ⭐**브로드캐스팅의 정의 및 목적**: NumPy에서 형태가 다른 배열 간 연산을 효율적으로 수행하는 메커니즘. (메모리 효율성 및 코드 간결성 측면 강조)
*   ⭐**브로드캐스팅 성공/실패 조건**: 다음 단계를 따릅니다.
    1.  모든 배열의 차원 수를 맞춥니다 (부족한 차원에 1을 패딩).
    2.  각 축에 대해 크기가 같거나, 한쪽의 크기가 1이어야 합니다.
    3.  **두 배열의 해당 축 크기가 1이 아니면서 서로 다르면 무조건 실패**합니다.
*   ⭐**결과 형태(Result Shape) 결정 방법**: 각 축에서 가장 큰 크기를 취합니다.
*   ⭐**스칼라 처리**: 스칼라는 `()` 형태의 배열처럼 동작하며 모든 배열과 브로드캐스팅 가능합니다.
*   **메모리 효율성**: 브로드캐스팅은 데이터를 복사하지 않고 개념적으로 확장하므로 메모리 효율적입니다. 그러나 *결과 배열은 새로 할당됩니다*.

---

## Slide 42

**핵심 개념**
NumPy 브로드캐스팅(Broadcasting)은 서로 다른 형태(shape)를 가진 배열(array) 간에 이항 연산(예: 덧셈, 뺄셈, 곱셈)을 수행할 수 있도록 배열의 크기를 자동으로 확장하는 메커니즘입니다. 핵심 원리는 다음 세 가지 규칙을 따릅니다:
1.  두 배열의 차원(dimension) 수가 다르면, 더 작은 차원 수의 배열의 왼쪽에 1이 추가되어 차원 수를 맞춥니다.
2.  각 차원에서 두 배열의 크기가 같거나, 둘 중 하나의 크기가 1이어야 합니다.
3.  만약 두 배열의 해당 차원 크기가 모두 1보다 크고 서로 다르다면, 브로드캐스팅은 불가능하며 에러가 발생합니다.
성공적으로 브로드캐스팅이 이루어지면, 결과 배열의 형태는 각 차원별로 입력 배열의 최대 크기를 따르게 됩니다.

**코드/수식 해설**

**1. 호환 가능한 경우 (Compatible)**
-   **예시 1: 여러 배열의 브로드캐스팅**
    -   A의 형태: (2, 1, 3)
    -   B의 형태: (1, 4, 1)
    -   C의 형태: (2, 4, 1)
    -   각 차원별로 비교하여 결과 형태를 결정합니다 (오른쪽에서 왼쪽으로 비교하는 것이 일반적이나, 결과 형태 결정 시에는 각 차원별로 가장 큰 값을 취합니다).
        -   **Axis 0 (가장 왼쪽 차원):** A (2), B (1), C (2) $\rightarrow$ 최대값은 2. (B가 1에서 2로 확장)
        -   **Axis 1 (중간 차원):** A (1), B (4), C (4) $\rightarrow$ 최대값은 4. (A가 1에서 4로 확장)
        -   **Axis 2 (가장 오른쪽 차원):** A (3), B (1), C (1) $\rightarrow$ 최대값은 3. (B와 C가 1에서 3으로 확장)
    -   결과 형태: (2, 4, 3)

**2. 스칼라와 벡터의 브로드캐스팅**
-   **예시 2: M, v, c의 브로드캐스팅**
    -   M의 형태: (7, 1)
    -   v의 형태: (1,) (1차원 배열) $\rightarrow$ 브로드캐스팅을 위해 (1, 1)로 간주될 수 있음 (앞에 1을 추가하여 차원 수 맞춤).
    -   c의 형태: () (스칼라) $\rightarrow$ 모든 차원에서 1로 간주될 수 있으며, 어떤 형태로든 확장 가능.
    -   각 차원별로 비교하여 결과 형태를 결정합니다.
        -   **Axis 0:** M (7), v (1), c (1) $\rightarrow$ 최대값은 7. (v와 c가 1에서 7로 확장)
        -   **Axis 1:** M (1), v (1), c (1) $\rightarrow$ 최대값은 1. (모두 1이므로 확장이 필요 없음)
    -   결과 형태: (7, 1)

**3. 호환 불가능한 경우 (Incompatible)**
-   **예시 3: X, Y, Z의 브로드캐스팅**
    -   X의 형태: (2, 3)
    -   Y의 형태: (3, 1)
    -   Z의 형태: (2, 2)
    -   오른쪽에서부터 각 차원을 비교하여 호환성을 검사합니다.
        -   **Axis 1 (가장 오른쪽 차원):** X (3), Y (1), Z (2)
            -   여기에 1이 아닌 크기 3과 2가 존재하고, 이 둘은 서로 다릅니다. 이는 브로드캐스팅 규칙의 3번째 조건("두 배열의 해당 차원 크기가 모두 1보다 크고 서로 다르다면 에러")을 위반합니다.
    -   상태: "error at last axis: sizes {3, 1, 2} => non-1 sizes 3 and 2 conflict"

**구체적 예시**

예를 들어, 우리가 학생들의 과목별 점수를 담은 2차원 배열과, 과목별 평균 점수를 나타내는 1차원 배열을 더하고 싶다고 가정해 봅시다.
학생 점수 `scores = np.array([[80, 90, 70], [75, 85, 95]])` (형태: (2, 3) - 2명의 학생, 3과목)
과목별 가중치 `weights = np.array([0.2, 0.5, 0.3])` (형태: (3,) - 3과목 가중치)

여기서 `scores`에 `weights`를 곱하려고 할 때, NumPy는 `weights`의 형태 (3,)를 `(1, 3)`으로 간주하여 `scores`의 형태 (2, 3)와 브로드캐스팅하여 각 학생의 점수에 과목별 가중치를 곱할 수 있도록 해줍니다. `weights`의 첫 번째 차원(크기 1)이 `scores`의 첫 번째 차원(크기 2)으로 확장되는 식입니다.

```python
import numpy as np

# 호환 가능한 경우 (예시 1)
A = np.arange(2*1*3).reshape(2, 1, 3) # (2, 1, 3)
B = np.arange(1*4*1).reshape(1, 4, 1) # (1, 4, 1)
C = np.arange(2*4*1).reshape(2, 4, 1) # (2, 4, 1)

# 브로드캐스팅이 가능하다고 가정하면, 결과 형태는 (2, 4, 3)
# 실제 연산은 각 차원에서 1인 부분이 확장되어 이루어짐
print(f"A shape: {A.shape}")
print(f"B shape: {B.shape}")
print(f"C shape: {C.shape}")
# 연산을 직접 보여줄 수는 없지만, shape은 예상됨
# print(f"Result shape of A + B + C: {(A+B+C).shape}") # (2, 4, 3) 예상

# 스칼라와 벡터 (예시 2)
M = np.arange(7).reshape(7, 1) # (7, 1)
v = np.arange(1) # (1,)
c = 10 # () scalar

# M + v + c 연산의 결과 형태는 (7, 1)
print(f"\nM shape: {M.shape}")
print(f"v shape: {v.shape}")
print(f"c is scalar")
print(f"Result shape of M + v + c: {(M + v + c).shape}") # (7, 1)

# 호환 불가능한 경우 (예시 3)
X = np.zeros((2, 3)) # (2, 3)
Y = np.zeros((3, 1)) # (3, 1)
Z = np.zeros((2, 2)) # (2, 2)

try:
    _ = X + Y + Z
except ValueError as e:
    print(f"\nError for X + Y + Z: {e}")
    # Error will be similar to: operands could not be broadcast together with shapes (2,3) (3,1) (2,2)
```

**시험 포인트**

*   ⭐ **브로드캐스팅의 기본 규칙 3가지**를 정확히 이해하고 설명할 수 있어야 합니다. 특히, "두 배열의 해당 차원 크기가 모두 1보다 크고 서로 다르다면 에러"가 발생하는 조건은 중요합니다.
*   ⭐ 주어진 배열 형태(shape)들을 보고 **브로드캐스팅 결과 형태**를 예측하거나, **브로드캐스팅 실패 여부와 이유**를 판단할 수 있어야 합니다. 특히, 스칼라(scalar)나 1차원 배열(vector)이 다차원 배열과 브로드캐스팅될 때의 규칙을 잘 알아두세요.
*   "값(values)이 크기 1인 축(axis)에서 확장(stretch)된다"는 개념을 이해해야 합니다.
*   NumPy는 차원 비교 시 **가장 오른쪽(trailing) 차원부터 시작**한다는 점을 기억하세요 (특히 호환성 검사 시).

---
## Slide 43

**핵심 개념**
NumPy 브로드캐스팅(Broadcasting)은 서로 다른 형태(shape)를 가진 NumPy 배열(ndarray) 간에 산술 연산(덧셈, 뺄셈, 곱셈, 나눗셈 등)을 수행할 수 있도록 배열의 크기를 자동으로 조정하는 강력한 메커니즘입니다. 이 기능은 명시적인 반복문이나 배열 복제를 피함으로써 코드를 간결하게 하고, 메모리 효율성을 높여줍니다.

**브로드캐스팅 규칙**:
두 배열의 차원(dimension)을 비교할 때, 오른쪽에서부터 왼쪽으로 차원별 크기를 비교합니다.
1.  **차원 개수가 다르면**: 더 작은 차원의 배열의 shape 앞에 1이 추가되어 차원 개수를 맞춥니다. (예: `(3,)`는 `(1, 3)`으로 간주)
2.  **차원 크기가 다르면**:
    *   한 쪽 차원 크기가 1이면, 해당 차원은 다른 배열의 크기에 맞춰 확장됩니다.
    *   두 쪽 차원 크기가 같으면 일치합니다.
    *   두 쪽 차원 크기가 다르고 1도 아니면, 브로드캐스팅이 불가능하여 `ValueError`가 발생합니다.
3.  이 규칙들을 모두 통과해야 브로드캐스팅이 성공하며, 결과 배열의 shape는 각 차원에서 더 큰 크기를 따릅니다.

**코드/수식 해설**

```python
import numpy as np

# 배열 A 생성: 2x3 행렬
A = np.arange(6).reshape(2, 3)
# A = [[0, 1, 2],
#      [3, 4, 5]]
# shape: (2, 3)

# 배열 b 생성: 1D 벡터
b = np.array([10, 20, 30])
# b = [10, 20, 30]
# shape: (3,)

# 배열 c 생성: 2x1 행렬 (열 벡터)
c = np.array([[100], [200]])
# c = [[100],
#      [200]]
# shape: (2, 1)

# 브로드캐스팅 연산 예시

# Y1 = A + b
# A.shape: (2, 3)
# b.shape: (3,) -> (1, 3) (규칙 1 적용)
# (2, 3) + (1, 3) -> 결과 shape (2, 3)
#   - 마지막 차원: 3 == 3 (일치)
#   - 첫 번째 차원: 2 vs 1 -> 1이 2로 확장
Y1 = A + b

# Y2 = A + c
# A.shape: (2, 3)
# c.shape: (2, 1)
# (2, 3) + (2, 1) -> 결과 shape (2, 3)
#   - 마지막 차원: 3 vs 1 -> 1이 3으로 확장
#   - 첫 번째 차원: 2 == 2 (일치)
Y2 = A + c

# Y3 = b + c
# b.shape: (3,) -> (1, 3) (규칙 1 적용)
# c.shape: (2, 1)
# (1, 3) + (2, 1) -> 결과 shape (2, 3)
#   - 마지막 차원: 3 vs 1 -> 1이 3으로 확장
#   - 첫 번째 차원: 1 vs 2 -> 1이 2로 확장
Y3 = b + c

# 결과 배열들의 shape 출력
print("shapes:", Y1.shape, Y2.shape, Y3.shape)
# 예상 출력: shapes: (2, 3) (2, 3) (2, 3)

# Y1과 Y2가 값적으로 동일한지 확인
print(np.allclose(Y1, Y2))
# Y1과 Y2는 브로드캐스팅 방식이 다르므로, 결과가 다를 것입니다.
# 따라서 False가 출력됩니다.
```

**구체적 예시**

각 연산이 실제로 어떻게 브로드캐스팅되고 결과가 도출되는지 살펴보겠습니다.

1.  **`Y1 = A + b` (Shape: `(2, 3) + (3,)`)**
    `b`는 `(3,)` 형태이지만, 연산을 위해 `(1, 3)`으로 간주된 후 첫 번째 차원이 `A`의 2에 맞춰 확장됩니다.
    ```
    A = [[0, 1, 2],       b_broadcasted = [[10, 20, 30],
         [3, 4, 5]]                       [10, 20, 30]]
    --------------------------------------------------
    Y1 = [[0+10, 1+20, 2+30],
          [3+10, 4+20, 5+30]]
       = [[10, 21, 32],
          [13, 24, 35]]
    ```

2.  **`Y2 = A + c` (Shape: `(2, 3) + (2, 1)`)**
    `c`는 `(2, 1)` 형태이지만, 연산을 위해 두 번째 차원이 `A`의 3에 맞춰 확장됩니다.
    ```
    A = [[0, 1, 2],       c_broadcasted = [[100, 100, 100],
         [3, 4, 5]]                       [200, 200, 200]]
    -----------------------------------------------------
    Y2 = [[0+100, 1+100, 2+100],
          [3+200, 4+200, 5+200]]
       = [[100, 101, 102],
          [203, 204, 205]]
    ```
    위의 예시에서 `Y1`과 `Y2`의 최종 결과 배열이 다르다는 것을 확인할 수 있습니다. 따라서 `np.allclose(Y1, Y2)`는 `False`를 반환합니다.

3.  **`Y3 = b + c` (Shape: `(3,) + (2, 1)`)**
    `b`는 `(3,)`에서 `(1, 3)`으로, `c`는 `(2, 1)` 형태입니다.
    `b`의 첫 번째 차원 1은 `c`의 첫 번째 차원 2에 맞춰 확장되고,
    `c`의 두 번째 차원 1은 `b`의 두 번째 차원 3에 맞춰 확장됩니다.
    ```
    b_broadcasted = [[10, 20, 30],    c_broadcasted = [[100, 100, 100],
                     [10, 20, 30]]                     [200, 200, 200]]
    ------------------------------------------------------------------
    Y3 = [[10+100, 20+100, 30+100],
          [10+200, 20+200, 30+200]]
       = [[110, 120, 130],
          [210, 220, 230]]
    ```

**시험 포인트**
*   ⭐ **NumPy 브로드캐스팅의 기본 원리**: 서로 다른 shape의 배열이 어떻게 연산될 수 있는지 이해하는 것이 중요합니다.
*   ⭐ **브로드캐스팅 규칙의 적용**: 주어진 두 배열의 shape를 보고 브로드캐스팅이 가능한지, 그리고 연산 결과의 shape가 어떻게 되는지 정확하게 예측할 수 있어야 합니다. 특히 `(N,)` 형태의 1차원 배열이 `(1, N)`으로 간주되어 브로드캐스팅 규칙이 적용되는 방식을 이해해야 합니다.
*   ⭐ **실제 연산 결과 추론**: 브로드캐스팅된 후 각 배열의 형태가 어떻게 변하고, 어떤 값들이 서로 더해지거나 곱해지는지 단계별로 추론하여 최종 결과 배열의 내용을 예측할 수 있어야 합니다. (예: `Y1`과 `Y2`가 다른 결과임을 이해)
*   `np.allclose()` 함수의 사용 목적: 부동 소수점 연산에서 발생할 수 있는 미세한 오차를 허용하면서 두 배열이 "거의 같은지" 비교할 때 사용됨을 알아둡시다.

---
## Slide 44

## NumPy 연산의 세 가지 직관: Elementwise, Pairwise, Reduction

### 핵심 개념

*   **Elementwise (원소별 연산)**:
    *   배열의 각 원소에 대해 개별적으로 연산을 수행합니다.
    *   주로 스칼라(scalar)와의 연산 또는 동일한 형태의 두 배열 간의 연산에 사용됩니다. NumPy의 [브로드캐스팅(broadcasting)](https://numpy.org/doc/stable/user/basics.broadcasting.html) 규칙에 따라 다양한 형태의 배열 간에도 Elementwise 연산이 가능합니다.
*   **Pairwise (쌍별 연산 - Outer Product)**:
    *   한 배열의 모든 원소($x_i$)와 다른 배열의 모든 원소($y_j$)를 조합하여 연산을 수행합니다.
    *   결과 배열의 차원은 입력 배열들의 차원의 합이 됩니다 (예: 1차원 배열 두 개로 2차원 배열 생성).
    *   주로 두 벡터의 모든 조합에 대한 연산이 필요할 때 사용됩니다. `numpy.add.outer()`, `numpy.multiply.outer()` 등이 대표적입니다.
*   **Reduction (축소 연산)**:
    *   배열의 특정 축(axis)을 따라 여러 원소를 하나의 값으로 "축소"하는 연산입니다.
    *   합계(sum), 최댓값(max), 최솟값(min), 평균(mean), 표준편차(std) 등이 대표적인 Reduction 연산입니다.
    *   `axis` 파라미터를 통해 어떤 축을 기준으로 축소할지 지정합니다.

### 코드/수식 해설

```python
import numpy as np

# 1. 초기 배열 정의
x = np.array([1., 2., 3.])            # 1차원 배열, shape (3,)
y = np.array([10., 20., 30., 40.])    # 1차원 배열, shape (4,)

# 2. Elementwise 연산 예시: 스칼라 곱셈
E = x * 2.0  # x의 각 원소에 2.0을 곱함 (브로드캐스팅 적용)
# 결과: E = [2., 4., 6.], shape (3,)
# 수식: E_i = x_i * 2.0

# 3. Pairwise (outer) 연산 예시: np.add.outer
P = np.add.outer(x, y) # x의 각 원소와 y의 각 원소를 모두 더하여 2차원 배열 생성
# 결과: P = [[1.+10., 1.+20., 1.+30., 1.+40.],
#              [2.+10., 2.+20., 2.+30., 2.+40.],
#              [3.+10., 3.+20., 3.+30., 3.+40.]]
#          = [[11., 21., 31., 41.],
#             [12., 22., 32., 42.],
#             [13., 23., 33., 43.]], shape (3, 4)
# 수식: P_{ij} = x_i + y_j

# 4. Reduction 연산을 위한 2차원 배열 생성
M = np.arange(12).reshape(3, 4) # 0부터 11까지의 숫자로 3x4 행렬 생성
# M = [[ 0,  1,  2,  3],
#      [ 4,  5,  6,  7],
#      [ 8,  9, 10, 11]], shape (3, 4)

# 5. Reduction 연산 예시: M.sum()
r0 = M.sum(axis=0) # axis=0 (행 방향)을 따라 합산. 각 열의 합계를 구함.
# 결과: r0 = [0+4+8, 1+5+9, 2+6+10, 3+7+11] = [12, 15, 18, 21], shape (4,)
# 수식: r0_j = \sum_{i} M_{ij}

r1 = M.sum(axis=1) # axis=1 (열 방향)을 따라 합산. 각 행의 합계를 구함.
# 결과: r1 = [0+1+2+3, 4+5+6+7, 8+9+10+11] = [6, 22, 38], shape (3,)
# 수식: r1_i = \sum_{j} M_{ij}

# 각 결과 배열의 shape 출력
# print(E.shape, P.shape, r0.shape, r1.shape)
# 출력: (3,) (3, 4) (4,) (3,)
```

### 구체적 예시

*   **Elementwise**:
    *   **상황**: 학생들의 중간고사 점수 배열이 `[70, 80, 90]`으로 주어졌을 때, 모든 점수에 5점의 가산점을 주는 경우.
    *   **코드**: `scores = np.array([70, 80, 90]); bonus_scores = scores + 5`
    *   **결과**: `bonus_scores`는 `[75, 85, 95]`가 됩니다. 각 원소에 5를 더하는 Elementwise 연산입니다.

*   **Pairwise (Outer)**:
    *   **상황**: 상품 A의 할인율 옵션 `[0.1, 0.2]`와 상품 B의 할인율 옵션 `[0.05, 0.15, 0.25]`가 있을 때, 두 상품을 함께 구매했을 때 가능한 모든 할인율 조합의 합계를 계산하는 경우.
    *   **코드**: `discounts_A = np.array([0.1, 0.2]); discounts_B = np.array([0.05, 0.15, 0.25]); total_discounts = np.add.outer(discounts_A, discounts_B)`
    *   **결과**: `total_discounts`는 `[[0.15, 0.25, 0.35], [0.25, 0.35, 0.45]]` (shape `(2, 3)`)가 됩니다. 모든 `(할인율 A, 할인율 B)` 쌍에 대해 합계가 계산됩니다.

*   **Reduction**:
    *   **상황**: 5명의 학생이 3과목 시험을 본 성적표가 `(학생 수, 과목 수)` 형태의 2차원 배열로 주어졌을 때.
    *   **코드**: `grades = np.array([[80, 90, 70], [75, 85, 95], [60, 70, 80], [90, 80, 70], [70, 70, 70]])` (shape `(5, 3)`)
    *   `grades_per_subject = grades.sum(axis=0)`: 각 **과목별** 총점을 계산합니다. `axis=0`은 행을 따라 내려가며 합산하므로, 각 열(과목)의 합이 됩니다. 결과 shape `(3,)`.
    *   `grades_per_student = grades.sum(axis=1)`: 각 **학생별** 총점을 계산합니다. `axis=1`은 열을 따라 가며 합산하므로, 각 행(학생)의 합이 됩니다. 결과 shape `(5,)`.

### 시험 포인트

*   ⭐ **Elementwise, Pairwise (outer), Reduction 연산의 정의와 사용 목적, 그리고 각각의 결과 배열 shape 변화를 정확히 이해해야 합니다.**
*   ⭐ 특히 `Reduction` 연산에서 `axis` 파라미터의 역할이 중요합니다. `axis=0`은 "열 방향 연산 (행을 축소)"을 의미하여 각 열의 결과를 반환하고, `axis=1`은 "행 방향 연산 (열을 축소)"을 의미하여 각 행의 결과를 반환합니다. 이로 인해 결과 배열의 shape가 어떻게 변하는지 반드시 숙지해야 합니다.
*   ⭐ `np.add.outer`와 같은 `outer` 함수들이 `pairwise` 연산을 통해 어떻게 입력 배열들의 차원을 '확장'하는지도 이해해야 합니다. 예를 들어, 두 1차원 배열로부터 2차원 배열을 생성합니다.

---
## Slide 45

- **핵심 개념**:
    *   **Elementwise (Pointwise) 연산**: 두 개 이상의 배열(피연산자)이 있을 때, 동일한 위치(인덱스)에 있는 원소들끼리 연산을 수행하는 방식입니다. 브로드캐스팅(broadcasting) 규칙이 적용되어 모양이 다른 배열도 연산에 참여할 수 있으며, 출력 배열의 각 원소는 입력 배열의 해당 위치 원소(및 브로드캐스팅된 원소)에만 의존합니다. 단항(unary) 또는 이항(binary) 함수가 적용됩니다.
    *   **Pairwise (Outer) 연산**: 두 벡터 $x$와 $y$의 모든 가능한 원소 쌍 $(x_i, y_j)$에 대해 이항 함수 $f$를 적용하여 결과를 $M \times N$ 형태의 행렬로 생성하는 방식입니다. 출력 행렬의 각 원소 $F_{ij}$는 첫 번째 벡터의 $i$-번째 원소 $x_i$와 두 번째 벡터의 $j$-번째 원소 $y_j$에 의해 결정됩니다.

- **코드/수식 해설**:
    *   **Elementwise (Pointwise) 연산**:
        브로드캐스팅이 적용된 유니터리(unary) 또는 바이너리(binary) 함수 $u$를 사용하여 $Y=u(X)$ 또는 $Y=u(X, Z)$ 형태로 표현됩니다. 형상 정렬(shape alignment) 후, 각 출력 인덱스 $i$는 각 피연산자로부터 최대 하나의 인덱스에 의존합니다.
    *   **Pairwise (Outer) 연산**:
        두 벡터 $x \in \mathcal{V}_{\alpha}^{\{0,...,M-1\}}$와 $y \in \mathcal{V}_{\beta}^{\{0,...,N-1\}}$에 이변량(bivariate) 함수 $f$를 적용하여 $M \times N$ 크기의 행렬 $F$를 생성합니다.
        수식은 다음과 같습니다.
        $$ F \in \mathcal{V}_{\gamma}^{M \times N} $$
        $$ F_{ij} = f(x_i, y_j) $$
        NumPy에서는 `np.subtract.outer`, `np.multiply.outer`와 같은 `outer` 함수를 통해 구현되거나, `np.newaxis`를 이용한 브로드캐스팅으로 구현될 수 있습니다.

- **구체적 예시**:
    *   **Elementwise (Pointwise) 예시**:
        ```python
        import numpy as np

        # 두 배열의 Elementwise 덧셈
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([10, 20, 30])
        result_elementwise = arr1 + arr2
        print("Elementwise 덧셈:", result_elementwise)
        # 출력: Elementwise 덧셈: [11 22 33]

        # 브로드캐스팅을 사용한 Elementwise 연산
        arr3 = np.array([[1, 2], [3, 4]])
        scalar = 5
        result_broadcast = arr3 * scalar
        print("브로드캐스팅 (Elementwise):\n", result_broadcast)
        # 출력:
        # 브로드캐스팅 (Elementwise):
        #  [[ 5 10]
        #   [15 20]]
        ```

    *   **Pairwise (Outer) 예시**:
        ```python
        import numpy as np

        vec1 = np.array([1, 2, 3]) # M=3
        vec2 = np.array([10, 20]) # N=2

        # np.subtract.outer를 사용한 Pairwise 뺄셈
        result_outer_subtract = np.subtract.outer(vec1, vec2)
        print("Pairwise (Outer) 뺄셈:\n", result_outer_subtract)
        # 출력:
        # Pairwise (Outer) 뺄셈:
        #  [[-9 -19]  # 1-10, 1-20
        #   [-8 -18]  # 2-10, 2-20
        #   [-7 -17]] # 3-10, 3-20

        # 브로드캐스팅을 사용한 Pairwise 덧셈
        # vec1을 (3, 1) 형태로, vec2를 (1, 2) 형태로 만들어 브로드캐스팅
        result_outer_add_broadcast = vec1[:, np.newaxis] + vec2[np.newaxis, :]
        print("Pairwise (Outer) 덧셈 (브로드캐스팅):\n", result_outer_add_broadcast)
        # 출력:
        # Pairwise (Outer) 덧셈 (브로드캐스팅):
        #  [[11 21]  # 1+10, 1+20
        #   [12 22]  # 2+10, 2+20
        #   [13 23]] # 3+10, 3+20
        ```

- **시험 포인트**:
    *   ⭐ **Elementwise와 Pairwise 연산의 근본적인 차이점을 명확히 이해하고 설명할 수 있어야 합니다.** Elementwise는 "같은 위치" 원소 간의 연산이며 브로드캐스팅이 적용될 수 있는 반면, Pairwise는 "모든 가능한 쌍" 원소 간의 연산으로 차원이 확장됩니다.
    *   ⭐ **NumPy에서 Pairwise (Outer) 연산을 구현하는 두 가지 주요 방법(ex: `np.outer` 계열 함수와 `np.newaxis`를 활용한 브로드캐스팅)을 알고 있어야 합니다.** 특히 `[:, np.newaxis]`를 이용한 차원 확장이 Pairwise 연산을 구현하는 핵심 브로드캐스팅 기법임을 이해하는 것이 중요합니다.
    *   ⭐ 각 연산 방식이 어떤 상황에서 유용하게 사용되는지 (예: Elementwise는 벡터/행렬의 일상적인 산술 연산, Pairwise는 두 집합 간의 거리/유사도 행렬 계산 등) 그 활용 예시를 연결하여 생각할 수 있어야 합니다.

---
## Slide 46

### **핵심 개념**

*   **인덱스 분리 ($i_A$와 $i_{\bar{A}}$)**: 다차원 배열(텐서)의 전체 인덱스 집합을 두 부분으로 나누는 개념입니다.
    *   $i_A$: 특정 연산(예: 축소/Reduction)이 적용될 축(axes)에 해당하는 인덱스들의 튜플입니다.
    *   $i_{\bar{A}}$: 축소 연산 후 남아있는 축(axes)에 해당하는 인덱스들의 튜플로, 결과 배열의 특정 위치를 지정합니다.
*   **축소 (Reduction) 연산**: 배열의 특정 축들을 따라 연산(예: 합계, 평균, 최댓값 등)을 수행하여 해당 축을 제거하고 배열의 차원을 줄이는 과정입니다. 예를 들어, `np.sum(X, axis=k)`는 $k$번째 축을 따라 모든 요소를 더하여 해당 축을 제거합니다.
*   **수학적 축과 NumPy 축 매핑**:
    *   슬라이드에서 제시된 수학적 축 인덱스는 1부터 시작합니다 (예: 축 1, 축 2, 축 3).
    *   NumPy에서는 항상 **0부터 시작하는 축 인덱스**를 사용합니다 (예: `axis=0`, `axis=1`, `axis=2`).
    *   따라서 슬라이드 예시에서 '수학적 축 2'는 NumPy의 `axis=1`에 해당하며, 이는 `X`의 두 번째 차원(크기가 3인 차원)을 의미합니다.

### **코드/수식 해설**

주어진 텐서 $X$의 형태가 $s = (s_0, s_1, s_2)$ (NumPy 기준) 또는 $(s_1, s_2, s_3)$ (수학적 기준)일 때, 축소할 축의 집합을 $A = \{2\}$ (수학적 축 인덱스)라고 가정합니다. 이는 NumPy `axis=1`에 해당합니다.
전체 인덱스를 $i = (i_1, i_2, i_3)$ (수학적 인덱스)라고 할 때:

*   **인덱스 분리**:
    $$ i = (i_1, i_2, i_3) \in I_{\{1,2,3\}} \implies i_A = (i_2) \in I_{\{2\}}, \quad i_{\bar{A}} = (i_1, i_3) \in I_{\{1,3\}} $$
    여기서 $I_S$는 집합 $S$에 해당하는 인덱스들의 가능한 값들의 도메인을 나타냅니다. 축소될 인덱스 $i_A$는 수학적 축 2에 해당하는 $i_2$이며, 결과 인덱스 $i_{\bar{A}}$는 나머지 축 1과 축 3에 해당하는 $i_1, i_3$입니다.

*   **축소 연산 (합계 예시)**:
    $A$ 축을 따라 합계를 수행하는 `reduce_{A,+}{X}` 연산의 $i_{\bar{A}}$ 위치에서의 값은 다음과 같습니다:
    $$ (\text{reduce}_{A,+}{X})[i_{\bar{A}}] = \sum_{i_2=0}^{s_2-1} X[i_1, i_2, i_3] $$
    여기서 $s_2$는 수학적 축 2 (NumPy `axis=1`)의 크기입니다. 슬라이드 예시 `X`의 `shape=(2,3,4)`에서 $s_2=3$이므로, $i_2$는 $0, 1, 2$의 값을 가질 수 있습니다.

*   **NumPy 코드**:
    ```python
    import numpy as np

    # X는 (2, 3, 4) 형태의 3D 배열이며, 0부터 23까지의 숫자로 채워짐
    X = np.arange(24).reshape(2, 3, 4) # shape (2,3,4)

    # NumPy axis=1을 따라 합계 연산 수행.
    # 이는 수학적 축 2에 해당하며, shape (2,3,4)에서 가운데 축(크기 3)을 없애
    # 결과 R의 shape는 (2, 4)가 됨
    R = np.sum(X, axis=1) # reduce along math-axis 2 -> numpy axis=1

    # 특정 인덱스 (i1, i3) = (1, 2)에 대해 수동 계산된 합계와 NumPy 결과 비교
    i1, i3 = 1, 2
    # R[1, 2]는 X[1, :, 2]를 axis=1(두 번째 축)을 따라 모두 더한 값과 같아야 함
    # 즉, X[1, 0, 2] + X[1, 1, 2] + X[1, 2, 2] 와 같아야 함
    assert R[i1, i3] == X[i1, 0, i3] + X[i1, 1, i3] + X[i1, 2, i3]
    ```
    이 `assert` 문은 `np.sum(X, axis=1)`의 결과 `R`의 특정 요소 `R[1, 2]`가 해당 축(`axis=1`)을 따라 모든 요소($X[1, 0, 2]$, $X[1, 1, 2]$, $X[1, 2, 2]$)를 더한 값과 정확히 일치하는지 검증합니다.

### **구체적 예시**

`X`가 학급 학생들의 성적 데이터라고 가정해봅시다:
*   `axis=0`: 학생 인덱스 (예: 0번 학생, 1번 학생)
*   `axis=1`: 과목 인덱스 (예: 0번 과목, 1번 과목, 2번 과목)
*   `axis=2`: 시험 회차 인덱스 (예: 0차 시험, 1차 시험, 2차 시험, 3차 시험)
따라서 `X`의 `shape=(2, 3, 4)`는 2명의 학생이 3과목에 대해 각각 4번의 시험을 치른 점수를 나타낸다고 볼 수 있습니다.

이때 `R = np.sum(X, axis=1)`을 수행하는 것은 **"각 학생별로, 각 시험 회차에 대해, 모든 과목의 점수를 합산"**하는 것과 같습니다. 예를 들어, `R[0, 1]`은 0번 학생이 1차 시험에서 치른 모든 과목의 총점을 의미하게 됩니다. `axis=1` (과목 축)이 제거되었으므로, 결과 `R`은 `shape=(2, 4)`를 가지며, 이는 "학생 x 시험 회차"별 총점을 나타냅니다.

슬라이드의 예시 `(reduce_{{2},+}{X})[1, 2]`는 NumPy 코드에서 `R[1, 2]`에 해당합니다. 이는 "1번 학생이 2차 시험에서 치른 모든 과목의 총점"을 의미하며, `X[1, 0, 2] + X[1, 1, 2] + X[1, 2, 2]` (1번 학생의 2차 시험에서 0번 과목 점수 + 1번 과목 점수 + 2번 과목 점수)와 같습니다.

### **시험 포인트**

*   ⭐ **NumPy `axis` 인덱싱**: 수학적 축 인덱스와 NumPy의 0-based `axis` 인덱스 간의 매핑 관계를 정확히 이해하고 변환할 수 있어야 합니다.
*   ⭐ **축소 (Reduction) 연산의 원리**: `np.sum()`, `np.mean()`, `np.max()` 등과 같은 축소 함수들이 특정 `axis`를 따라 작동할 때, 해당 축의 차원이 어떻게 사라지고 결과 배열의 `shape`가 어떻게 변하는지 설명할 수 있어야 합니다.
*   ⭐ **`assert` 문을 통한 개념 검증**: 슬라이드의 `assert` 문처럼, NumPy 연산의 특정 결과 값(예: `R[1, 2]`)을 수동으로 계산한 (명시적인 합계나 평균 등) 값과 비교하여 개념을 이해했는지 묻는 문제가 나올 수 있습니다.
*   ⭐ **`i_A`와 `i_{\bar{A}}$의 구분**: 주어진 배열의 `shape`와 축소될 `axis`에 대해, 축소 연산에 사용될 인덱스 ($i_A$)와 결과 배열의 인덱스 ($i_{\bar{A}}$)를 정확히 구분하고 설명할 수 있어야 합니다.

---
## Slide 47

**핵심 개념**:
- **차원 축소 (Reduction)**: 다차원 배열 `X`의 특정 축(axis)들을 따라 원소들을 결합하는 연산으로, 배열의 차원을 줄이는 과정입니다. 이 슬라이드에서는 이러한 차원 축소 연산을 수학적 기호와 함께 정의합니다.
- **결합 연산자 ($\bigoplus$)**: 차원 축소 시 원소들을 결합하는 데 사용되는 이항 연산자입니다. 이 연산자는 반드시 **결합법칙(associative)**이 성립하고 **항등원(identity element) `e`**를 가져야 합니다.
    - 예시: 덧셈($+$)의 항등원은 `0`, 최댓값(max)의 항등원은 `$-\infty$`, 논리곱(AND, $\land$)의 항등원은 `True`입니다.
- **축(Axes) 구분**:
    - `A`: 차원 축소 대상이 되는 축들의 집합입니다.
    - `$\bar{A}$`: 차원 축소 후에도 유지되는 축들의 집합입니다. (즉, `$\bar{A} = \{1, \dots, n\} \setminus A$`)
- **결과 형태(Shape)**: 축소 연산의 결과로 생성되는 배열의 형태는 유지되는 축 `$\bar{A}$`에 해당하는 차원들로 구성됩니다. `keepdims` 옵션을 사용하면 축소된 축들이 크기 `1`을 가진 채로 유지됩니다.

**코드/수식 해설**:
- **수식 표기법**:
    - `X`: `n`-차원 배열. 형태는 `s = (s_1, \dots, s_n)`입니다.
    - `$\bigoplus$`: 결합 연산자 (예: 덧셈, 최댓값).
    - `A`: 축소할 축들의 집합.
    - `$\bar{A}$`: 유지할 축들의 집합.
    - `For any axis set J, the index set $I_J = \prod_{k \in J} \{0, \dots, s_k - 1\}$ (Cartesian product over those axes).`: 축 집합 `J`에 대한 인덱스 `I_J`는 `J`에 속한 모든 축의 인덱스 범위를 곱한 카테시안 곱입니다.
    - `Indices are split as $i_A \in I_A$ and $i_{\bar{A}} \in I_{\bar{A}}$.`: 배열 `X`의 전체 인덱스는 축소될 축(`A`)에 해당하는 부분 인덱스 `i_A`와 유지될 축(`$\bar{A}$`)에 해당하는 부분 인덱스 `i_{\bar{A}}$`로 나눌 수 있습니다.

- **차원 축소의 수학적 정의**:
    $$ (reduce_{A, \bigoplus} X)[i_{\bar{A}}] = \bigoplus_{i_A \in I_A} X[i_A, i_{\bar{A}}] $$
    이 수식은 유지되는 축 `$\bar{A}$`에 해당하는 인덱스 `i_{\bar{A}}$`가 고정되었을 때, 축소될 축 `A`에 해당하는 모든 인덱스 `i_A`에 대해 `X[i_A, i_{\bar{A}}]` 값들을 결합 연산자 `$\bigoplus$`으로 모두 연산한 결과가 축소된 배열의 `$[i_{\bar{A}}]$` 위치 값이 됨을 의미합니다. 즉, 유지되는 축들을 따라 "슬라이스"를 만들고, 각 슬라이스 내에서 축소될 축들을 따라 연산을 수행합니다.

- **NumPy 매핑**:
    NumPy 라이브러리에서는 이러한 차원 축소 연산을 `axis` 인자를 사용하여 수행합니다.
    - `reduce_{A,+} \iff np.sum(X, axis=...)`
    - `reduce_{A,max} \iff np.max(X, axis=...)`
    - ⭐**주의사항**: 수학적 표기에서는 축 번호가 `1`부터 `n`까지이지만, NumPy에서는 `0`부터 `n-1`까지입니다. 따라서 수학적 `k` 축은 NumPy의 `k-1` 축에 해당합니다.

**구체적 예시**:
2차원 NumPy 배열 `X`를 사용하여 `axis` 인자의 동작을 살펴보겠습니다.

```python
import numpy as np

# 2x3 배열 X 생성 (수학적 표기의 X)
X = np.array([[1, 2, 3],
              [4, 5, 6]])
print("Original X:\n", X)
print("Shape of X:", X.shape) # (2, 3)

# 수학적 표기: 축 1 (행), 축 2 (열)
# NumPy 표기: 축 0 (행), 축 1 (열)

# 예시 1: 축 0 (행)을 축소 (합계 연산)
# A = {1} (수학적 표기), A = {0} (NumPy 표기)
print("\n--- 예시 1: np.sum(X, axis=0) ---")
reduced_X_axis0 = np.sum(X, axis=0)
print("Result:\n", reduced_X_axis0) # [5 7 9]
print("Shape:", reduced_X_axis0.shape) # (3,)
# 해설: 각 열 방향으로 원소들을 합산합니다. [1+4, 2+5, 3+6] = [5, 7, 9].
# 원래 축 0 (행)이 사라지고, 축 1 (열)만 유지되어 형태가 (3,)이 됩니다.

# 예시 2: 축 1 (열)을 축소 (최댓값 연산)
# A = {2} (수학적 표기), A = {1} (NumPy 표기)
print("\n--- 예시 2: np.max(X, axis=1) ---")
reduced_X_axis1 = np.max(X, axis=1)
print("Result:\n", reduced_X_axis1) # [3 6]
print("Shape:", reduced_X_axis1.shape) # (2,)
# 해설: 각 행 방향으로 최댓값을 찾습니다. [max(1,2,3), max(4,5,6)] = [3, 6].
# 원래 축 1 (열)이 사라지고, 축 0 (행)만 유지되어 형태가 (2,)가 됩니다.

# 예시 3: keepdims=True 사용
print("\n--- 예시 3: np.sum(X, axis=0, keepdims=True) ---")
reduced_X_axis0_keepdims = np.sum(X, axis=0, keepdims=True)
print("Result:\n", reduced_X_axis0_keepdims) # [[5 7 9]]
print("Shape:", reduced_X_axis0_keepdims.shape) # (1, 3)
# 해설: 축 0이 축소되었지만, keepdims=True로 인해 크기 1의 차원으로 유지됩니다.
# 원래 (2, 3) 형태에서 축 0이 사라지는 대신 (1, 3) 형태로 변경됩니다. 이는 브로드캐스팅 등에서 유용하게 사용될 수 있습니다.
```

**시험 포인트**:
- ⭐**차원 축소의 개념과 목적**: `np.sum()`, `np.max()`, `np.mean()` 등과 같은 NumPy 함수들이 배열의 특정 `axis`를 따라 어떻게 동작하며, 왜 이러한 연산을 `reduction`이라고 부르는지 이해하는 것이 중요합니다.
- ⭐**`axis` 인자의 역할**: `axis` 인자가 어떤 축을 기준으로 연산을 수행할지 지정하며, 이로 인해 배열의 어떤 차원이 사라지고 어떤 차원이 유지되는지 정확히 파악해야 합니다. 특히, 수학적 표기(1부터 n)와 NumPy 표기(0부터 n-1) 간의 `axis` 번호 차이를 명확히 인지하고 있어야 합니다.
- ⭐**`keepdims` 옵션의 이해**: `keepdims=True`가 결과 배열의 형태에 어떻게 영향을 미치는지 (축소된 차원이 크기 1로 유지됨) 정확히 설명하고, 왜 이러한 옵션이 필요한지 (예: 브로드캐스팅과의 연관성) 이해해야 합니다.
- ⭐**결합 연산자($\bigoplus$)의 특성**: 차원 축소에 사용되는 연산자가 반드시 가져야 하는 수학적 특성(결합법칙, 항등원 존재)을 인지해야 합니다. 이는 다양한 `reduction` 함수가 동작하는 근본 원리입니다.

---
## Slide 48

**핵심 개념**:
*   **Elementwise Operation (요소별 연산)**: 배열의 각 요소에 대해 독립적으로 스칼라 연산 또는 동일한 형태의 다른 배열과의 연산을 수행하는 방식입니다. NumPy에서는 대부분의 이항(binary) 연산자(+, -, *, /)가 기본적으로 요소별로 동작하며, 이는 효율적인 벡터화 연산의 기본이 됩니다.
*   **Pairwise Operation (쌍별 연산) / Outer Operation (외적 연산)**: 두 배열의 모든 가능한 요소 쌍에 대해 연산을 수행하여, 입력 배열들의 차원 수를 합한 형태의 고차원 결과를 생성하는 연산입니다. NumPy의 `broadcasting` 메커니즘을 활용하여 효율적으로 구현하거나, `np.add.outer`와 같은 명시적인 `outer` 함수를 사용할 수 있습니다. `outer sum`은 각 `x`의 요소와 각 `y`의 요소의 합으로 이루어진 행렬을 생성합니다.
*   **Reductions (축소 연산)**: 배열의 특정 `axis`(축)를 따라 연산을 수행하여 해당 축의 차원을 줄이는(축소하는) 연산입니다. 예를 들어, `sum`, `mean`, `max`, `min`, `std` 등이 있으며, `axis` 인자를 통해 어떤 축을 따라 연산을 수행할지 지정할 수 있습니다. `keepdims=True` 옵션을 사용하면 축소된 차원을 크기 1로 유지하여 차원 수를 보존할 수 있으며, 이는 후속 `broadcasting` 연산을 용이하게 합니다.

**코드/수식 해설**:

```python
import numpy as np

# 1. 배열 초기화
x = np.array([1.0, 2.0, 3.0])  # 1D 배열, shape: (3,)
y = np.array([10.0, 20.0, 30.0, 40.0]) # 1D 배열, shape: (4,)
```
- `x`와 `y`는 각각 3개, 4개의 요소를 가진 1차원 NumPy 배열입니다.

```python
# 2. Elementwise Operation (요소별 연산)
E = x + 2.0 # elementwise unary
```
- `E`는 `x` 배열의 각 요소에 스칼라 값 `2.0`을 더한 결과를 저장합니다.
- `x`의 각 요소 $x_i$에 $2.0$을 더한 $x_i + 2.0$을 계산합니다.
- `E`의 `shape`은 `x`와 동일한 `(3,)`입니다.
- 결과: `[3.0, 4.0, 5.0]`

```python
# 3. Pairwise Operation (쌍별 연산) - Broadcasting을 이용한 Outer Sum
B = x[:, None] + y[None, :] # pairwise via broadcasting -> outer sum
```
- `x[:, None]`는 `x`의 형태를 `(3,)`에서 `(3, 1)`로 변경합니다. 이는 새로운 축(axis)을 추가하여 열 벡터처럼 만듭니다.
- `y[None, :]`는 `y`의 형태를 `(4,)`에서 `(1, 4)`로 변경합니다. 이는 새로운 축을 추가하여 행 벡터처럼 만듭니다.
- `(3, 1)` 형태의 배열과 `(1, 4)` 형태의 배열을 더할 때 NumPy의 `broadcasting` 규칙이 적용되어, 두 배열은 `(3, 4)` 형태로 확장된 후 요소별 덧셈이 수행됩니다.
- 이 연산은 `outer sum`을 계산하며, 결과 `B`는 `(3, 4)` 형태의 2차원 배열이 됩니다. 각 요소 $B_{ij} = x_i + y_j$가 됩니다.

```python
# 4. Pairwise Operation (쌍별 연산) - 명시적인 Outer 함수 사용
O = np.add.outer(x, y) # explicit outer
```
- `np.add.outer(x, y)`는 `x`의 모든 요소와 `y`의 모든 요소의 가능한 조합에 대해 `add` 연산을 수행하여 `outer sum`을 명시적으로 계산하는 편리한 함수입니다.
- 결과 `O`는 `B`와 동일한 `(3, 4)` 형태의 2차원 배열이 되며, 내용도 동일합니다.

```python
# 5. Reductions (축소 연산)
M = np.arange(12).reshape(3, 4)
# M은 다음과 같은 3x4 행렬:
# [[ 0,  1,  2,  3],
#  [ 4,  5,  6,  7],
#  [ 8,  9, 10, 11]]
r0 = M.sum(axis=0) # reduce over rows
```
- `M.sum(axis=0)`는 `axis=0` (행)을 따라 합계를 계산합니다. 즉, 각 열(column)의 모든 요소를 더합니다.
- 결과 `r0`의 `shape`은 `(4,)`입니다.
- 결과: `[0+4+8, 1+5+9, 2+6+10, 3+7+11] = [12, 15, 18, 21]`

```python
r1 = M.sum(axis=1) # reduce over cols
```
- `M.sum(axis=1)`는 `axis=1` (열)을 따라 합계를 계산합니다. 즉, 각 행(row)의 모든 요소를 더합니다.
- 결과 `r1`의 `shape`은 `(3,)`입니다.
- 결과: `[0+1+2+3, 4+5+6+7, 8+9+10+11] = [6, 22, 38]`

```python
r1_keep = M.sum(axis=1, keepdims=True)
```
- `M.sum(axis=1, keepdims=True)`는 `r1`과 동일한 연산을 수행하지만, 축소된 차원의 크기를 1로 유지합니다.
- 결과 `r1_keep`의 `shape`은 `(3, 1)`입니다.
- 결과: `[[6], [22], [38]]`

```python
# 6. 결과 출력 및 검증
print("B shape:", B.shape, "O == B?", np.allclose(O, B))
print("r0/r1 shapes:", r0.shape, r1.shape, r1_keep.shape)
```
- 첫 번째 `print` 문은 `B`의 형태 `(3, 4)`와 `O`와 `B`가 수치적으로 동일한지(`True`)를 출력합니다.
- 두 번째 `print` 문은 `r0`의 형태 `(4,)`, `r1`의 형태 `(3,)`, `r1_keep`의 형태 `(3, 1)`를 출력합니다.

**구체적 예시**:

1.  **Elementwise (`E = x + 2.0`)**:
    *   학생들의 시험 점수 `x = [70, 80, 90]`에 일괄적으로 2점의 가산점을 부여하는 경우, `E = [72, 82, 92]`가 됩니다. 각 학생의 점수에 독립적으로 연산이 적용됩니다.

2.  **Pairwise (`B = x[:, None] + y[None, :]` 또는 `O = np.add.outer(x, y)`)**:
    *   `x`가 세 가지 제품의 기본 가격 `[100, 200, 300]`이고, `y`가 네 가지 추가 배송료 옵션 `[5, 10, 15, 20]`이라고 가정해봅시다. `np.add.outer(x, y)`는 각 제품의 기본 가격에 각 배송료 옵션을 더한 모든 가능한 조합을 계산하여 3x4 행렬을 생성합니다.
    *   예시 결과:
        ```
        # B (또는 O)
        # [[100+5, 100+10, 100+15, 100+20],
        #  [200+5, 200+10, 200+15, 200+20],
        #  [300+5, 300+10, 300+15, 300+20]]
        # 즉,
        # [[105., 110., 115., 120.],
        #  [205., 210., 215., 220.],
        #  [305., 310., 315., 320.]]
        ```

3.  **Reductions (`M.sum(axis=0)`, `M.sum(axis=1)`, `M.sum(axis=1, keepdims=True)`)**:
    *   `M`이 3개 반(행)의 학생 4명씩(열)의 수행평가 점수라고 가정합니다.
        ```
        # M = [[반1_학생1, 반1_학생2, 반1_학생3, 반1_학생4],
        #      [반2_학생1, 반2_학생2, 반2_학생3, 반2_학생4],
        #      [반3_학생1, 반3_학생2, 반3_학생3, 반3_학생4]]
        ```
    *   `M.sum(axis=0)`는 `axis=0` (행)을 따라 각 반의 같은 번호 학생들의 점수를 합산하여, `[학생1총점, 학생2총점, 학생3총점, 학생4총점]`과 같은 결과를 반환합니다.
    *   `M.sum(axis=1)`는 `axis=1` (열)을 따라 각 반 학생들의 점수를 합산하여, `[반1총점, 반2총점, 반3총점]`과 같은 결과를 반환합니다.
    *   `M.sum(axis=1, keepdims=True)`는 `r1`과 동일하게 각 반별 총점을 계산하지만, 결과 형태를 `(3, 1)`로 유지하여 `[[반1총점], [반2총점], [반3총점]]`과 같이 2차원 배열 형태로 만듭니다. 이는 예를 들어, 이 결과를 원본 `M`과 `broadcasting`하여 각 학생의 점수를 반 총점으로 나누는 등의 연산을 할 때 유용합니다.

**시험 포인트**:

*   ⭐ **NumPy Broadcasting 개념 및 동작 방식**: 특히 `x[:, None]`와 `y[None, :]`를 이용한 차원 확장이 `pairwise` 연산 (`outer sum`)을 어떻게 구현하는지, 그리고 이 과정에서 배열의 `shape` 변화가 어떻게 이루어지는지 정확히 이해해야 합니다.
*   ⭐ **`axis` 인자의 역할**: `sum`, `mean` 등 `reduction` 연산에서 `axis=0`와 `axis=1` (또는 N차원 배열의 다른 축)이 각각 어떤 축을 따라 연산을 수행하며, 결과 배열의 `shape`에 어떻게 영향을 미치는지 반드시 알아야 합니다.
*   ⭐ **`keepdims=True` 옵션**: `reduction` 연산 시 `keepdims=True`가 결과 배열의 `shape`에 어떤 영향을 미치며, 왜 유용한지 (특히 `broadcasting`과의 연관성) 설명할 수 있어야 합니다. `keepdims=True`를 통해 차원 정보가 유지되어, 브로드캐스팅 시 더 직관적이고 유연한 연산이 가능합니다.
*   `np.add.outer`와 같은 명시적인 `outer` 함수가 `broadcasting`을 통한 구현과 동일한 결과를 내는 이유를 이해하는 것도 중요합니다.

---
## Slide 49

### 핵심 개념

*   **행렬 곱셈 (Matrix Multiplication)**: 두 행렬의 곱은 첫 번째 행렬의 행 벡터와 두 번째 행렬의 열 벡터의 내적(dot product)들의 결과로 구성됩니다. 즉, "공유되는 축(shared axis)을 따라 원소별 곱셈의 합(sum of products)"으로 정의됩니다. NumPy에서는 `@` 연산자를 사용하여 수행할 수 있습니다.
*   **행렬-벡터 곱셈 (Matrix-Vector Multiplication)**: 행렬 곱셈의 특수한 경우로, 행렬과 벡터를 곱하는 연산입니다. 이 역시 `@` 연산자로 수행됩니다.
*   **아인슈타인 합 규약 (Einstein Summation Convention) `np.einsum`**: 다차원 배열(텐서) 연산을 인덱스 레이블을 사용하여 간결하게 표현하는 강력한 방법입니다. 특히, 행렬 곱셈과 같은 텐서 수축(tensor contraction) 연산을 명시적으로 인덱스 관계를 지정하여 수행할 수 있습니다. `einsum`은 어떤 축을 곱하고, 어떤 축을 합하여 제거(수축)할 것인지를 문자열 인덱스 표현으로 지정합니다.

### 코드/수식 해설

```python
import numpy as np

# A: 2x3 행렬
# [[0, 1, 2],
#  [3, 4, 5]]
A = np.arange(6).reshape(2, 3) # (2, 3)

# B: 3x2 행렬
# [[0, 1],
#  [2, 3],
#  [4, 5]]
B = np.arange(6).reshape(3, 2) # (3, 2)

# u: 길이 3의 1차원 벡터
# [1., 2., 3.]
u = np.array([1., 2., 3.])     # (3,)

# M = A @ B: 행렬 곱셈
# A (2,3) @ B (3,2) = M (2,2)
# shared dim: 3
# 계산 예: M[0,0] = A[0,0]*B[0,0] + A[0,1]*B[1,0] + A[0,2]*B[2,0]
#                = 0*0 + 1*2 + 2*4 = 0 + 2 + 8 = 10
M = A @ B                      # (2, 2): sum of products along shared dim

# d = A @ u: 행렬-벡터 곱셈
# A (2,3) @ u (3,) = d (2,)
# shared dim: 3
# 계산 예: d[0] = A[0,0]*u[0] + A[0,1]*u[1] + A[0,2]*u[2]
#              = 0*1. + 1*2. + 2*3. = 0 + 2 + 6 = 8
d = A @ u                      # (2,): matrix-vector

# E = np.einsum('ij,jk->ik', A, B): 아인슈타인 합 규약을 이용한 행렬 곱셈
# 'ij': 첫 번째 배열(A)의 인덱스. i는 행, j는 열을 나타냅니다.
# 'jk': 두 번째 배열(B)의 인덱스. j는 행, k는 열을 나타냅니다.
# '->ik': 결과 배열의 인덱스. 공유되는 인덱스 'j'는 합산되어 사라지고, 'i'와 'k'가 남습니다.
# 이는 (AB)_ik = sum_j A_ij * B_jk 와 동일합니다.
E = np.einsum('ij,jk->ik', A, B) # same as A @ B

# M, d, E의 형태와 M과 E가 거의 동일한지 여부를 출력
print(M.shape, d.shape, np.allclose(M, E))
# 출력: (2, 2) (2,) True
```

**행렬 곱셈의 수식 표현**:
두 행렬 $A$와 $B$가 있을 때, $A$는 $m \times n$ 행렬이고 $B$는 $n \times p$ 행렬이라면, 그들의 곱 $C = AB$는 $m \times p$ 행렬이 됩니다. 결과 행렬 $C$의 각 원소 $C_{ik}$는 다음과 같이 계산됩니다.

$$ C_{ik} = \sum_{j=1}^{n} A_{ij} B_{jk} $$

여기서 $A_{ij}$는 행렬 $A$의 $i$번째 행, $j$번째 열의 원소이고, $B_{jk}$는 행렬 $B$의 $j$번째 행, $k$번째 열의 원소입니다. `np.einsum('ij,jk->ik', A, B)`는 이 수식을 그대로 파이썬 코드로 옮긴 것입니다.

### 구체적 예시

위 코드 예시에서 사용된 행렬 A, B, 벡터 u의 실제 값으로 연산을 살펴보겠습니다.

*   `A` (2x3):
    ```
    [[0, 1, 2],
     [3, 4, 5]]
    ```
*   `B` (3x2):
    ```
    [[0, 1],
     [2, 3],
     [4, 5]]
    ```
*   `u` (3,):
    ```
    [1., 2., 3.]
    ```

1.  **`M = A @ B` (행렬 곱셈)**
    결과는 (2, 2) 행렬이 됩니다.
    *   $M_{00} = A_{00}B_{00} + A_{01}B_{10} + A_{02}B_{20} = (0 \times 0) + (1 \times 2) + (2 \times 4) = 0 + 2 + 8 = 10$
    *   $M_{01} = A_{00}B_{01} + A_{01}B_{11} + A_{02}B_{21} = (0 \times 1) + (1 \times 3) + (2 \times 5) = 0 + 3 + 10 = 13$
    *   $M_{10} = A_{10}B_{00} + A_{11}B_{10} + A_{12}B_{20} = (3 \times 0) + (4 \times 2) + (5 \times 4) = 0 + 8 + 20 = 28$
    *   $M_{11} = A_{10}B_{01} + A_{11}B_{11} + A_{12}B_{21} = (3 \times 1) + (4 \times 3) + (5 \times 5) = 3 + 12 + 25 = 40$
    ```
    M = [[10, 13],
         [28, 40]]
    ```

2.  **`d = A @ u` (행렬-벡터 곱셈)**
    결과는 (2,) 벡터가 됩니다.
    *   $d_0 = A_{00}u_0 + A_{01}u_1 + A_{02}u_2 = (0 \times 1) + (1 \times 2) + (2 \times 3) = 0 + 2 + 6 = 8$
    *   $d_1 = A_{10}u_0 + A_{11}u_1 + A_{12}u_2 = (3 \times 1) + (4 \times 2) + (5 \times 3) = 3 + 8 + 15 = 26$
    ```
    d = [ 8, 26]
    ```

3.  **`E = np.einsum('ij,jk->ik', A, B)`**
    `np.einsum`은 위에서 계산된 행렬 곱셈 `M`과 정확히 같은 결과를 반환합니다. `np.allclose(M, E)`가 `True`를 출력함으로써 이를 확인할 수 있습니다.
    `einsum`은 마치 텐서 연산을 위한 미니 프로그래밍 언어와 같습니다. 각 텐서의 차원에 이름을 붙여(예: `i`, `j`, `k`) 어떤 차원을 곱하고(공통된 인덱스), 어떤 차원을 합해서 없앨지(`->` 기호 좌변에만 있고 우변에는 없는 인덱스), 그리고 최종 결과의 차원 구성이 어떻게 될지(`->` 기호 우변의 인덱스)를 직관적으로 표현할 수 있습니다.

### 시험 포인트

*   ⭐ **NumPy `@` 연산자의 의미**: 행렬 곱셈(`A @ B`)과 행렬-벡터 곱셈(`A @ u`)의 사용법 및 결과의 차원(shape)을 정확히 이해해야 합니다.
*   ⭐ **행렬 곱셈의 정의**: "공유되는 차원(shared axis)을 따라 원소들의 곱셈의 합(sum of products)"으로 정의된다는 것을 설명할 수 있어야 합니다.
*   ⭐ **`np.einsum`의 역할과 문법**:
    *   `np.einsum`이 텐서 수축(tensor contraction)을 표현하는 강력한 방법임을 이해해야 합니다.
    *   `'ij,jk->ik'`와 같은 인덱스 문자열의 의미 (입력 배열의 인덱스, 출력 배열의 인덱스)를 해석하고, 이를 통해 행렬 곱셈이나 다른 텐서 연산을 어떻게 표현하는지 알아야 합니다.
    *   `einsum`을 사용했을 때 행렬 곱셈(`@`)과 동일한 결과를 얻을 수 있음을 인지하고 있어야 합니다. (`np.allclose`의 사용 목적도 중요)
*   ⭐ **차원 일치 조건**: 행렬 곱셈에서 두 행렬의 "공유되는 차원"이 반드시 일치해야 함을 이해해야 합니다. 예를 들어, $A$가 $(m, n)$ 행렬이고 $B$가 $(p, q)$ 행렬일 때, $A @ B$가 가능하려면 $n=p$여야 합니다.

---
## Slide 50

## Matrix Products and Tensor Contractions

### 핵심 개념

*   **행렬 곱셈 (Matrix multiply)**:
    *   NumPy에서 `@` 연산자 또는 `np.matmul` 함수를 사용하여 수행합니다.
    *   수학적인 행렬 곱셈 정의에 정확히 따르며, 선행 배치 차원(leading batch axes)을 자동으로 처리합니다. 예를 들어, `(..., n, k) @ (..., k, m)` 형태의 행렬을 곱하면 결과는 `(..., n, m)` 형태가 됩니다. 이는 딥러닝에서 여러 샘플에 대한 가중치 곱을 효율적으로 계산할 때 유용합니다.
*   **내적 (Dot product)**:
    *   `np.dot` 함수를 사용합니다.
    *   1차원 배열의 경우 스칼라 내적(inner product)을 수행합니다.
    *   2차원 배열의 경우 행렬 곱셈과 동일하게 작동합니다.
    *   고차원 배열의 경우 첫 번째 배열의 *마지막* 축과 두 번째 배열의 *두 번째-마지막* 축을 축약(contract)하여 곱셈을 수행합니다. `np.dot`은 배치 차원 처리에 있어 `np.matmul`과 다르게 작동할 수 있으므로 주의해야 합니다.
*   **일반적인 텐서 축약 (General contractions)**:
    *   `np.tensordot`: 특정 축(axes)을 명시하여 텐서 곱셈과 축약을 수행합니다. 복잡한 텐서 연산을 유연하게 제어할 수 있습니다.
    *   `np.einsum`: 아인슈타인 표기법(Einstein summation convention)을 사용하여 텐서 연산을 매우 간결하고 강력하게 표현할 수 있습니다. 축 순서 변경, 대각선 추출, 합계 등 다양한 작업을 수행할 수 있습니다.
*   **쌍별 거리 (Pairwise distances)**:
    *   두 개의 데이터셋 $X$와 $Y$의 모든 가능한 샘플 쌍 $(X_i, Y_j)$에 대해 유클리드 거리($L_2$ norm)를 계산하는 것을 의미합니다.
    *   이는 클러스터링, 분류, 추천 시스템 등 다양한 머신러닝 알고리즘에서 데이터 포인트 간의 유사도를 측정하는 데 기초가 됩니다. $X_i$는 $X$의 $i$-번째 행(샘플)이고, $Y_j$는 $Y$의 $j$-번째 행(샘플)을 나타냅니다.
    *   계산 결과는 $M \times N$ 크기의 거리 행렬 $D$가 됩니다.

### 코드/수식 해설

*   **행렬 곱셈 수식**:
    두 행렬 $A \in \mathbb{R}^{n \times k}$ 와 $B \in \mathbb{R}^{k \times m}$ 에 대한 행렬 곱 $C = A @ B$ 의 $i$행 $j$열 요소는 다음과 같습니다.
    $$(A@B)_{ij} = \sum_{\ell=1}^{k} A_{i\ell} B_{\ell j}$$
    배치 차원(leading batch axes)을 포함하는 경우의 차원 변환은 다음과 같습니다.
    $$(..., n, k) @ (..., k, m) \rightarrow (..., n, m)$$

*   **쌍별 거리 수식**:
    $X \in \mathbb{R}^{M \times d}$ 와 $Y \in \mathbb{R}^{N \times d}$ 두 데이터셋에 대해, $X$의 $i$-번째 샘플 $X_i$와 $Y$의 $j$-번째 샘플 $Y_j$ 사이의 유클리드 거리 $D_{ij}$는 다음과 같이 정의됩니다.
    $$D_{ij} = \|X_i - Y_j\|_2$$
    이를 풀어쓰면 각 차원 $t$에 대한 차이의 제곱 합의 제곱근이 됩니다.
    $$D_{ij} = \sqrt{\sum_{t=1}^{d} (X_{it} - Y_{jt})^2}$$
    또한, 이를 내적 형태로 전개하면 다음과 같이 표현할 수 있습니다. 이 형태는 계산 효율성을 높이는 데 자주 사용됩니다.
    $$D_{ij} = \sqrt{\|X_i\|_2^2 + \|Y_j\|_2^2 - 2 X_i \cdot Y_j}$$
    여기서 $X_i \cdot Y_j$는 두 벡터 $X_i$와 $Y_j$의 내적입니다.

*   **NumPy 연산 예시**:
    ```python
    import numpy as np

    # Matrix multiply (@ or np.matmul)
    A = np.array([[1, 2], [3, 4]]) # (2, 2)
    B = np.array([[5, 6], [7, 8]]) # (2, 2)
    C_matmul = A @ B
    print("A @ B:\n", C_matmul)

    # Batch matrix multiply
    A_batch = np.random.rand(2, 3, 4) # (batch, n, k)
    B_batch = np.random.rand(2, 4, 5) # (batch, k, m)
    C_batch_matmul = A_batch @ B_batch # (batch, n, m) -> (2, 3, 5)
    print("\nA_batch @ B_batch shape:", C_batch_matmul.shape)

    # Dot product (np.dot)
    vec1 = np.array([1, 2, 3])
    vec2 = np.array([4, 5, 6])
    inner_prod = np.dot(vec1, vec2) # 1*4 + 2*5 + 3*6 = 32
    print("\nInner product (np.dot):", inner_prod)

    # np.dot for 2D is same as matrix multiply
    C_dot = np.dot(A, B)
    print("np.dot(A, B):\n", C_dot)

    # General contractions (np.tensordot, np.einsum)
    A_tensor = np.arange(1, 28).reshape(3, 3, 3) # (3, 3, 3)
    B_tensor = np.arange(1, 65).reshape(4, 4, 4) # (4, 4, 4) - simplified example

    # Example: np.tensordot for matrix multiply
    # np.tensordot(A, B, axes=([1], [0])) is equivalent to A @ B for 2D
    # For higher dim tensors, axes specify which axes to contract

    # np.einsum for matrix multiply (A_ik B_kj -> C_ij)
    C_einsum = np.einsum('ik,kj->ij', A, B)
    print("\nnp.einsum('ik,kj->ij', A, B):\n", C_einsum)

    # np.einsum for inner product (A_i B_i -> sum)
    inner_prod_einsum = np.einsum('i,i->', vec1, vec2)
    print("np.einsum('i,i->', vec1, vec2):", inner_prod_einsum)
    ```

### 구체적 예시

*   **딥러닝 신경망에서의 행렬 곱셈**:
    신경망의 한 레이어에서 입력 데이터 $X$와 가중치 행렬 $W$를 곱하여 다음 레이어의 활성화 입력 $Z$를 계산할 때 행렬 곱셈이 사용됩니다.
    $Z = XW + b$
    여기서 $X$는 `(batch_size, input_dim)` 형태이고, $W$는 `(input_dim, output_dim)` 형태입니다. `X @ W` 연산은 각 배치 샘플에 대해 효율적으로 가중치 곱셈을 수행하여 `(batch_size, output_dim)` 형태의 결과를 얻게 됩니다.
*   **K-NN (K-Nearest Neighbors) 알고리즘에서의 쌍별 거리 계산**:
    새로운 데이터 포인트가 주어졌을 때, 이 포인트와 기존 훈련 데이터셋의 모든 포인트 사이의 거리를 계산해야 합니다. 이때 쌍별 거리 계산이 활용됩니다. 훈련 데이터 $X_{train}$과 테스트 데이터 $X_{test}$가 있을 때, $D_{ij} = \|X_{test,i} - X_{train,j}\|_2$를 계산하여 테스트 데이터의 각 샘플에 대해 가장 가까운 훈련 데이터 샘플을 찾습니다. 이 거리 행렬을 효율적으로 계산하는 것은 알고리즘의 성능에 매우 중요합니다.

### 시험 포인트

*   ⭐ **`@` 연산자, `np.matmul`, `np.dot`의 차이점을 정확히 이해하고 설명할 수 있어야 합니다.** 특히 고차원 배열(텐서)에서 `np.dot`이 마지막 축과 두 번째-마지막 축을 축약하는 방식과 `np.matmul`이 배치 차원을 처리하는 방식의 차이를 인지해야 합니다.
*   ⭐ **`np.einsum`의 강력함과 유연성**: 아인슈타인 표기법을 사용하여 다양한 텐서 연산(행렬 곱셈, 내적, 전치, 합계 등)을 구현하는 예시를 제시하거나 해석할 수 있어야 합니다.
*   ⭐ **쌍별 거리 공식**: $D_{ij} = \sqrt{\|X_i\|_2^2 + \|Y_j\|_2^2 - 2 X_i \cdot Y_j}$ 공식의 유도 과정과 이를 NumPy를 이용해 효율적으로 구현하는 방법을 이해해야 합니다. 특히, `np.sum(np.square(X_i - Y_j))` 형태의 직접 계산보다 내적을 이용한 계산이 더 효율적일 수 있음을 알아야 합니다.
*   **배치 차원(batch axes)의 개념**: 딥러닝에서 여러 샘플을 한 번에 처리할 때 행렬 곱셈이 배치 차원을 어떻게 보존하고 연산하는지 이해하는 것이 중요합니다.

---
## Slide 51

- **핵심 개념**:
    이 슬라이드는 두 가지 방식으로 여러 점들 간의 모든 쌍별 거리(pairwise distance)를 계산하는 방법을 비교합니다: `np.expand_dims`와 `np.tile`을 명시적으로 사용하는 방법과 NumPy의 브로드캐스팅(broadcasting) 기능을 활용하는 방법입니다. 핵심은 브로드캐스팅이 중간에 거대한 임시 배열을 생성하는 비용(메모리 및 시간)을 줄여 더 효율적이라는 점입니다.

- **코드/수식 해설**:
    데이터는 `samples`라는 `(15, 5)` 형태의 NumPy 배열로, 15개의 5차원 벡터(점)를 나타냅니다. 목표는 이 15개 점들 사이의 모든 쌍별 유클리드 거리 $D_{ij} = ||x_i - x_j||_2$를 계산하는 것입니다.

    수식:
    $D_{ij} = \sqrt{\sum_{k=1}^{d} (x_{ik} - x_{jk})^2}$
    여기서 $x_i$는 $i$번째 점, $x_j$는 $j$번째 점, $d$는 차원의 수(여기서는 5)입니다.

    두 가지 접근 방식은 다음과 같습니다:

    1.  **명시적 Tiling (`np.expand_dims` + `np.tile`)**:
        ```python
        rng = np.random.default_rng(0)
        samples = rng.random((15, 5)) # 15 points in R^5

        # expand_dims로 차원을 추가하여 (15, 1, 5) 또는 (1, 15, 5) 형태로 만든 후
        # tile을 사용하여 (15, 15, 5) 크기의 배열을 명시적으로 생성합니다.
        expanded1 = np.expand_dims(samples, axis=1) # (15, 1, 5)
        tile1 = np.tile(expanded1, (1, samples.shape[0], 1)) # (15, 15, 5)

        expanded2 = np.expand_dims(samples, axis=0) # (1, 15, 5)
        tile2 = np.tile(expanded2, (samples.shape[0], 1, 1)) # (15, 15, 5)

        # 두 (15, 15, 5) 배열의 차이를 계산
        diff_nb = tile2 - tile1 # (15, 15, 5)

        # 각 (i, j) 쌍에 대해 5차원 벡터의 L2 norm (유클리드 거리) 계산
        dist_nb = np.linalg.norm(diff_nb, axis=-1) # (15, 15)
        ```
        *   `np.expand_dims(samples, axis=1)`: `(15, 5)` 배열에 두 번째 축을 추가하여 `(15, 1, 5)` 형태로 만듭니다. 이는 각 5차원 점을 하나의 "행"으로 가진 배열로 만듭니다.
        *   `np.tile(expanded1, (1, samples.shape[0], 1))`: `expanded1`을 두 번째 축으로 `samples.shape[0]` (즉, 15)번 반복하여 `(15, 15, 5)` 배열을 만듭니다. 이 배열의 `tile1[i, j]`는 `samples[i]`가 됩니다.
        *   `np.expand_dims(samples, axis=0)`: `(15, 5)` 배열에 첫 번째 축을 추가하여 `(1, 15, 5)` 형태로 만듭니다. 이는 15개의 5차원 점 전체를 하나의 "덩어리"로 가진 배열로 만듭니다.
        *   `np.tile(expanded2, (samples.shape[0], 1, 1))`: `expanded2`를 첫 번째 축으로 `samples.shape[0]` (즉, 15)번 반복하여 `(15, 15, 5)` 배열을 만듭니다. 이 배열의 `tile2[i, j]`는 `samples[j]`가 됩니다.
        *   `diff_nb = tile2 - tile1`: `tile2`의 `j`번째 점과 `tile1`의 `i`번째 점의 차이를 계산하여 `diff_nb[i, j]`는 `samples[j] - samples[i]`가 됩니다.
        *   `np.linalg.norm(diff_nb, axis=-1)`: `diff_nb` 배열의 마지막 축(5차원 벡터)에 대해 L2 norm(유클리드 거리)을 계산합니다. 결과 `dist_nb[i, j]`는 $||samples[j] - samples[i]||_2$가 됩니다.

    2.  **브로드캐스팅 (`np.newaxis`)**:
        ```python
        # Broadcasting: no materialization of tiles
        # np.newaxis를 사용하여 명시적인 tile 없이 브로드캐스팅 규칙을 활용합니다.
        diff_bc = samples[:, np.newaxis, :] - samples[np.newaxis, :, :] # (15, 15, 5)
        dist_bc = np.linalg.norm(diff_bc, axis=-1) # (15, 15)
        ```
        *   `samples[:, np.newaxis, :]`: `(15, 5)` 배열을 `(15, 1, 5)` 형태로 만듭니다. 이는 `expanded1`과 동일합니다.
        *   `samples[np.newaxis, :, :]`: `(15, 5)` 배열을 `(1, 15, 5)` 형태로 만듭니다. 이는 `expanded2`와 동일합니다.
        *   `samples[:, np.newaxis, :] - samples[np.newaxis, :, :]`: NumPy의 브로드캐스팅 규칙에 따라 두 배열은 암묵적으로 `(15, 15, 5)` 형태로 확장되어 연산됩니다. 즉, `(15, 1, 5)`는 첫 번째 축을 따라 15번, `(1, 15, 5)`는 두 번째 축을 따라 15번 "가상으로" 확장되어 `(15, 15, 5)` 크기의 `diff_bc`를 생성합니다. 이때 명시적인 복사(materialization)는 발생하지 않아 메모리 효율적입니다.
        *   `np.linalg.norm(diff_bc, axis=-1)`: 위와 동일하게 L2 norm을 계산합니다.

    두 방법은 동일한 결과 `(dist_nb, dist_bc)`와 형태를 가집니다. `np.allclose(dist_nb, dist_bc)` 결과가 참(True)인 것을 통해 확인합니다.

    하단 문구: "Both compute $D_{ij} = ||x_i - x_j||_2$. Broadcasting avoids the $O(n^2d)$ temporary created by tile."
    이는 두 방법 모두 쌍별 거리를 계산하지만, 브로드캐스팅은 `np.tile`이 생성하는 `O(n^2d)` 크기의 임시 배열(`tile1`, `tile2`)을 만들지 않아 메모리 및 성능 측면에서 더 유리하다는 것을 의미합니다. 여기서 $n$은 점의 개수(15), $d$는 차원의 수(5)입니다.

-   **구체적 예시**:
    만약 3개의 2차원 점 A(1,1), B(2,2), C(3,3)이 있다고 가정해 봅시다. `samples`는 `[[1,1], [2,2], [3,3]]` 형태가 될 것입니다.

    *   **Tiling 방식**:
        `expanded1`은 `[[[1,1]], [[2,2]], [[3,3]]]` 형태(`(3,1,2)`).
        `tile1`은 `[[[1,1],[1,1],[1,1]], [[2,2],[2,2],[2,2]], [[3,3],[3,3],[3,3]]]` 형태(`(3,3,2)`). (각 행이 세 번 복사)
        `expanded2`는 `[[[1,1],[2,2],[3,3]]]` 형태(`(1,3,2)`).
        `tile2`는 `[[[1,1],[2,2],[3,3]], [[1,1],[2,2],[3,3]], [[1,1],[2,2],[3,3]]]` 형태(`(3,3,2)`). (각 열이 세 번 복사)
        `diff_nb`는 `tile2 - tile1`이 되어, `diff_nb[0,1]`은 `[2,2] - [1,1] = [1,1]`이 됩니다.

    *   **브로드캐스팅 방식**:
        `samples[:, np.newaxis, :]`는 `expanded1`과 동일하게 `[[[1,1]], [[2,2]], [[3,3]]]` 형태.
        `samples[np.newaxis, :, :]`는 `expanded2`와 동일하게 `[[[1,1],[2,2],[3,3]]]` 형태.
        이 두 배열이 빼기 연산을 할 때, NumPy는 첫 번째 배열의 두 번째 축(크기 1)을 3으로 확장하고, 두 번째 배열의 첫 번째 축(크기 1)을 3으로 확장하여 `(3,3,2)` 형태의 중간 연산을 수행합니다. 이 과정에서 `tile1`이나 `tile2`처럼 데이터를 물리적으로 복사하여 거대한 임시 배열을 미리 만들지 않고, 연산이 필요할 때만 데이터를 "가상으로" 확장하여 처리하므로 더 효율적입니다.

-   **시험 포인트**:
    *   ⭐**NumPy 브로드캐스팅의 개념과 동작 원리**: 서로 다른 형태의 배열 간 연산 시 NumPy가 어떻게 자동으로 형태를 맞춰주는지 이해해야 합니다. 특히 `np.newaxis` 또는 `None`을 사용하여 차원을 추가하고 브로드캐스팅을 활용하는 방법을 알아야 합니다.
    *   ⭐**`np.expand_dims`와 `np.newaxis`의 역할**: 둘 다 배열의 차원을 추가하는 데 사용되지만, `np.newaxis`는 인덱싱 내에서 편리하게 사용될 수 있습니다.
    *   ⭐**`np.tile`의 사용법**: 특정 배열을 여러 번 반복하여 더 큰 배열을 만드는 방법을 알아야 합니다.
    *   ⭐**메모리 효율성**: 브로드캐스팅이 `np.tile`을 이용한 명시적 확장에 비해 메모리 사용량 측면에서 왜 더 효율적인지 설명할 수 있어야 합니다. 특히 `O(n^2d)` 임시 메모리 생성 회피에 대한 이해가 중요합니다.
    *   **`np.linalg.norm`의 `axis` 파라미터**: 주어진 축을 따라 norm(벡터의 크기)을 계산하는 방법을 이해해야 합니다. 여기서는 마지막 축(`axis=-1`)을 따라 5차원 벡터의 유클리드 거리를 계산합니다.
    *   **쌍별 거리 계산 (Pairwise Distance)**: 주어진 데이터셋에서 모든 점 쌍 간의 거리를 효율적으로 계산하는 방법을 구현하는 능력.

---
## Slide 52

**핵심 개념**:
*   **행렬 곱셈 (Matrix Multiplication)**: 두 행렬을 곱하는 연산으로, 첫 번째 행렬의 열 수와 두 번째 행렬의 행 수가 같아야 합니다. NumPy에서는 `@` 연산자나 `np.matmul()` 함수로 수행하며, 결과 행렬의 모양은 (첫 번째 행렬의 행 수, 두 번째 행렬의 열 수)가 됩니다.
*   **내적 (Inner Product)**: 두 벡터의 각 요소를 곱하여 더하는 스칼라 결과값을 생성하는 연산입니다. 주로 `np.dot()` 함수를 사용하여 수행합니다.
*   **배치 행렬 곱셈 (Batched Matrix Multiplication)**: 3차원 이상의 배열에서 마지막 두 차원을 행렬로 간주하고, 나머지 앞선 차원들을 배치(batch) 차원으로 간주하여 여러 행렬 쌍에 대해 동시에 행렬 곱셈을 수행하는 연산입니다. 딥러닝에서 여러 샘플을 한 번에 처리할 때 유용합니다. NumPy에서는 배치 차원이 추가된 배열에 대해 `@` 연산자를 사용하여 수행할 수 있습니다.
*   **`np.einsum()`**: Einstein summation convention(아인슈타인 합 규약)을 따르는 유연한 배열 연산 함수입니다. 인덱스 문자열을 통해 텐서의 축소(contraction), 전치(transpose), 원소별 곱셈(element-wise multiplication) 후 합계 등 다양한 작업을 간결하게 표현할 수 있습니다.
*   **`np.tensordot()`**: 두 텐서의 특정 축들을 축소(contract)하여 곱셈을 수행하는 함수입니다. `axes` 인자를 통해 어떤 축들을 축소할지 명시적으로 지정하여 일반적인 행렬 곱셈(`axes=(1, 0)`)부터 고차원 텐서의 복잡한 곱셈까지 가능합니다.

**코드/수식 해설**:

```python
import numpy as np

# 일반 행렬 곱셈 (`@` 연산자 또는 np.matmul)
A = np.arange(6).reshape(2, 3) # (2, 3) 행렬 생성
# [[0 1 2]
#  [3 4 5]]
B = np.arange(12).reshape(3, 4) # (3, 4) 행렬 생성
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print("(A @ B).shape:", (A @ B).shape) # 결과 (2, 4)
```
두 행렬 $A \in \mathbb{R}^{m \times k}$와 $B \in \mathbb{R}^{k \times n}$의 행렬 곱 $C = AB$는 $C \in \mathbb{R}^{m \times n}$ 형태의 행렬이 됩니다. 결과 행렬 $C$의 $i$행 $j$열 원소 $C_{ij}$는 다음과 같이 계산됩니다:
$$ C_{ij} = \sum_{p=0}^{k-1} A_{ip} B_{pj} $$

```python
# 1D 벡터의 내적 (np.dot)
u = np.array([1.0, 2.0, 3.0])
v = np.array([4.0, 5.0, 6.0])
print("dot 1D:", np.dot(u, v)) # 내적: (1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32.0)
```
두 벡터 $\mathbf{u} = [u_0, u_1, \ldots, u_{n-1}]$와 $\mathbf{v} = [v_0, v_1, \ldots, v_{n-1}]$의 내적은 스칼라 값으로 다음과 같습니다:
$$ \mathbf{u} \cdot \mathbf{v} = \sum_{i=0}^{n-1} u_i v_i $$

```python
# 배치 행렬 곱셈 (Batched matmul)
# 두 개의 (2,3) 행렬 (A, A+100)을 스택하여 (2, 2, 3) 배치 행렬 Ab 생성
Ab = np.stack([A, A + 100], axis=0) # Ab.shape == (2, 2, 3)
# 두 개의 (3,4) 행렬 (B, B+100)을 스택하여 (2, 3, 4) 배치 행렬 Bb 생성
Bb = np.stack([B, B + 100], axis=0) # Bb.shape == (2, 3, 4)
print("batched matmul shape:", (Ab @ Bb).shape) # 결과 (2, 2, 4)
```
배치 행렬 곱셈 $C = Ab @ Bb$에서, $Ab \in \mathbb{R}^{B \times m \times k}$와 $Bb \in \mathbb{R}^{B \times k \times n}$일 때, 결과 $C \in \mathbb{R}^{B \times m \times n}$가 됩니다. 즉, 배치 차원 $B$에 대해 각 행렬 곱셈이 독립적으로 수행됩니다:
$$ C_{b, i, j} = \sum_{p=0}^{k-1} Ab_{b, i, p} Bb_{b, p, j} $$

```python
# einsum을 이용한 배치 행렬 곱셈 (Same as batched matmul)
E = np.einsum('bij,bjk->bik', Ab, Bb)
# 'bij': 첫 번째 텐서 Ab (b: 배치, i: 행, j: 열)
# 'bjk': 두 번째 텐서 Bb (b: 배치, j: 행, k: 열)
# 'bik': 결과 텐서 E (b: 배치, i: 행, k: 열)
# j가 축소(summation)되는 축입니다.
print("einsum equals batched?", np.allclose(E, Ab @ Bb)) # True
```
`einsum` 표기법 `bij,bjk->bik`는 다음과 같은 연산을 의미하며, 배치 행렬 곱셈의 정의와 동일합니다:
$$ E_{b,i,k} = \sum_j Ab_{b,i,j} Bb_{b,j,k} $$

```python
# tensordot을 이용한 행렬 곱셈 (Same as np.matmul)
# A의 마지막 축(axis=1)과 B의 첫 번째 축(axis=0)을 축소(contract)
TD = np.tensordot(A, B, axes=(1, 0))
# axes=(1, 0)는 A의 1번 축(컬럼)과 B의 0번 축(로우)을 따라 합한다는 의미.
# 즉, A의 (2, 3)에서 3을, B의 (3, 4)에서 3을 축소.
print("tensordot == matmul?", np.allclose(TD, A @ B)) # True
```
`np.tensordot(A, B, axes=(1, 0))`는 $A_{ip}$와 $B_{pj}$를 곱하고 $p$에 대해 합산하는 연산이며, 이는 일반적인 행렬 곱셈과 동일합니다:
$$ (A \otimes_c B)_{ij} = \sum_{p} A_{ip} B_{pj} $$
여기서 `axes=(1, 0)`는 $A$의 1번째 축과 $B$의 0번째 축이 contraction axes임을 의미합니다.

**구체적 예시**:
*   **일반 행렬 곱셈 (`@`, `np.matmul`)**: 컴퓨터 그래픽스에서 3D 오브젝트의 변환(회전, 이동, 스케일)을 위해 변환 행렬을 좌표 벡터에 적용할 때 사용됩니다. $A$가 3x3 변환 행렬이고 $B$가 3x1 좌표 벡터일 경우, $A @ B$는 변환된 좌표를 나타냅니다.
*   **내적 (`np.dot`)**: 머신러닝에서 신경망의 한 뉴런이 입력 벡터와 가중치 벡터를 받아들여 출력을 계산할 때 사용됩니다. 입력 벡터 $\mathbf{x}$와 가중치 벡터 $\mathbf{w}$의 내적 $\mathbf{x} \cdot \mathbf{w}$에 활성화 함수를 적용하여 뉴런의 출력을 얻습니다.
*   **배치 행렬 곱셈 (`@` with higher dimensions)**: 딥러닝 모델에서 미니 배치(mini-batch) 학습을 수행할 때 매우 중요합니다. 예를 들어, 32개의 이미지로 구성된 배치가 있고 각 이미지가 Convolution 레이어의 가중치 행렬과 곱해져야 할 때, `(32, height, width, channels)` 형태의 입력 텐서와 `(channels, new_channels, filter_h, filter_w)` 형태의 필터 텐서에 대해 효율적인 연산을 수행하기 위해 배치 행렬 곱셈을 활용합니다.
*   **`np.einsum`**: 이미지 텐서 `(N, H, W, C)`를 배치 차원(`N`)과 채널 차원(`C`)을 교환한 `(C, N, H, W)` 형태로 전치하고 싶을 때, `np.einsum('nhwc->cnhw', image_tensor)`와 같이 간결하게 표현할 수 있습니다. 이는 복잡한 `np.transpose`나 `np.swapaxes` 조합보다 훨씬 직관적입니다.

**시험 포인트**:
*   ⭐ **`np.matmul` (`@` 연산자)의 행렬 곱셈 규칙**: 두 행렬 $A(m, k)$와 $B(k, n)$의 곱셈 결과가 $C(m, n)$이 되는 이유와 각 원소가 어떻게 계산되는지 설명할 수 있어야 합니다. 즉, 차원 일치 조건과 결과 차원 결정 방식을 정확히 이해해야 합니다.
*   ⭐ **`np.dot`과 `np.matmul`의 차이점**: 1D 배열(벡터)에 대한 동작 방식(스칼라 내적 vs. 행렬 곱셈 시도), 그리고 2D 이상 배열(텐서)에 대한 동작 방식(`np.dot`은 마지막-두 번째 축, `np.matmul`은 마지막 두 축)의 주요 차이점을 숙지해야 합니다.
*   ⭐ **배치 행렬 곱셈의 개념 및 `np.stack`과의 연계**: 여러 개의 행렬을 묶어 한 번에 효율적으로 행렬 곱셈을 수행하는 방법과, 이를 위해 `np.stack` 등의 함수로 배치 차원을 추가하는 과정을 이해해야 합니다.
*   ⭐ **`np.einsum`의 인덱스 표기법**: `einsum` 문자열(`'bij,bjk->bik'`)이 어떤 의미를 가지며, 각 축이 연산에 어떻게 참여하고 축소되는지 이해하는 것이 중요합니다. 특히 배치 행렬 곱셈과 같이 복잡한 텐서 연산을 `einsum`으로 표현하는 예시는 필수적으로 알아두세요.
*   ⭐ **`np.tensordot`의 `axes` 인자 활용**: `np.tensordot(A, B, axes=(contract_A_axes, contract_B_axes))`에서 `axes` 인자가 무엇을 의미하며, 이를 통해 일반 행렬 곱셈을 어떻게 구현할 수 있는지 (`axes=(1, 0)`) 설명할 수 있어야 합니다.

---
## Slide 53

---
### **핵심 개념**
`numpy.hstack`과 `numpy.vstack`은 NumPy 배열(array)들을 결합(concatenate)하는 함수입니다. 이들은 여러 배열을 수평(horizontal) 또는 수직(vertical) 방향으로 이어 붙여 하나의 새로운 배열을 생성합니다.

-   **`numpy.hstack(tup)`**: 튜플 `tup`에 포함된 배열들을 **수평 방향(열, columns)**으로 이어 붙입니다.
    -   결합하려는 모든 배열은 **동일한 개수의 행(rows)**을 가져야 합니다.
    -   이는 `numpy.concatenate(tup, axis=1)`과 동일하게 동작합니다.
-   **`numpy.vstack(tup)`**: 튜플 `tup`에 포함된 배열들을 **수직 방향(행, rows)**으로 이어 붙입니다.
    -   결합하려는 모든 배열은 **동일한 개수의 열(columns)**을 가져야 합니다.
    -   이는 `numpy.concatenate(tup, axis=0)`과 동일하게 동작합니다.

### **코드/수식 해설**
주어진 슬라이드의 예시를 바탕으로 `hstack`과 `vstack`의 동작을 설명합니다.

```python
import numpy as np

# 배열 a (3x4)
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

# 배열 c (3x2)
c = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# 배열 b (2x4)
b = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8]])

print("Array a:\n", a)
print("Shape of a:", a.shape)
print("\nArray c:\n", c)
print("Shape of c:", c.shape)
print("\nArray b:\n", b)
print("Shape of b:", b.shape)

# np.hstack((a, c)) 예시: a와 c를 수평으로 결합
# a (3x4)와 c (3x2)는 모두 3개의 행을 가지므로 hstack 가능.
# 결과 배열은 (3 x (4+2)) = 3x6 형태가 됩니다.
hstacked_array = np.hstack((a, c))
print("\nnp.hstack((a, c)):\n", hstacked_array)
print("Shape of hstacked_array:", hstacked_array.shape)

# np.vstack((a, b)) 예시: a와 b를 수직으로 결합
# a (3x4)와 b (2x4)는 모두 4개의 열을 가지므로 vstack 가능.
# 결과 배열은 ((3+2) x 4) = 5x4 형태가 됩니다.
vstacked_array = np.vstack((a, b))
print("\nnp.vstack((a, b)):\n", vstacked_array)
print("Shape of vstacked_array:", vstacked_array.shape)
```

**수식:**
`hstack`과 `vstack`은 행렬 연산이라기보다는 배열의 재구조화(reshaping) 또는 결합(concatenation)에 가깝습니다. 만약 $A$와 $C$가 각각 $m \times n_1$과 $m \times n_2$ 형태의 행렬이라면, `hstack((A, C))`의 결과 행렬 $H$는 다음과 같이 표현할 수 있습니다:
$$ H = [A \quad C] $$
여기서 $H$는 $m \times (n_1 + n_2)$ 형태의 행렬이 됩니다.

마찬가지로, $A$와 $B$가 각각 $m_1 \times n$과 $m_2 \times n$ 형태의 행렬이라면, `vstack((A, B))`의 결과 행렬 $V$는 다음과 같이 표현할 수 있습니다:
$$ V = \begin{pmatrix} A \\ B \end{pmatrix} $$
여기서 $V$는 $(m_1 + m_2) \times n$ 형태의 행렬이 됩니다.

### **구체적 예시**
슬라이드의 예시를 통해 `hstack`과 `vstack`의 작동 방식을 시각적으로 이해할 수 있습니다.

1.  **`np.hstack((a, c))`**:
    *   `a` 배열은 3행 4열($3 \times 4$)입니다.
    *   `c` 배열은 3행 2열($3 \times 2$)입니다.
    *   두 배열 모두 3개의 **행**을 가지므로, `hstack`으로 수평 결합이 가능합니다.
    *   결과 배열은 `a`의 4개 열과 `c`의 2개 열이 옆으로 이어 붙여져 총 $3 \times (4+2) = 3 \times 6$ 형태의 배열이 됩니다. 마치 두 개의 표를 옆으로 나란히 붙여 하나의 더 큰 표를 만드는 것과 같습니다.

2.  **`np.vstack((a, b))`**:
    *   `a` 배열은 3행 4열($3 \times 4$)입니다.
    *   `b` 배열은 2행 4열($2 \times 4$)입니다.
    *   두 배열 모두 4개의 **열**을 가지므로, `vstack`으로 수직 결합이 가능합니다.
    *   결과 배열은 `a`의 3개 행과 `b`의 2개 행이 위아래로 이어 붙여져 총 $(3+2) \times 4 = 5 \times 4$ 형태의 배열이 됩니다. 마치 두 개의 표를 위아래로 쌓아 하나의 더 길고 큰 표를 만드는 것과 같습니다.

### **시험 포인트**
*   ⭐ **`hstack`과 `vstack`의 목적과 사용법을 정확히 이해하고 구분할 것.**
    *   `hstack`은 수평(열) 방향 결합, `vstack`은 수직(행) 방향 결합.
*   ⭐ **각 함수가 요구하는 배열의 차원(shape) 일치 조건을 명확히 숙지할 것.**
    *   `hstack`: 모든 배열의 **행의 개수**가 같아야 합니다.
    *   `vstack`: 모든 배열의 **열의 개수**가 같아야 합니다.
*   ⭐ `hstack`은 `np.concatenate(..., axis=1)`과, `vstack`은 `np.concatenate(..., axis=0)`과 동일한 결과를 낸다는 점을 기억할 것. (이해를 돕는 개념이며, `hstack`/`vstack`이 편의 함수임을 알면 좋습니다.)
*   ⭐ 조건이 충족되지 않을 경우 `ValueError`가 발생함을 인지하고, 오류 메시지를 통해 문제점을 파악할 수 있어야 합니다. (예: `ValueError: all the input array dimensions except for the concatenation axis must match exactly`)
*   ⭐ 실제 데이터 분석 과정에서 다른 차원의 데이터를 결합해야 할 때, 적절한 함수를 선택하여 사용할 수 있는 능력이 중요합니다.
---

---
## Slide 54

- **핵심 개념**:
    NumPy는 배열을 여러 방식으로 결합(stacking)하는 다양한 함수를 제공합니다.
    *   **`np.hstack` (Horizontal Stack)**: 주어진 배열들을 수평 방향(열 방향, axis=1)으로 결합합니다. 이때, 결합되는 배열들의 행의 개수(첫 번째 차원의 크기)가 동일해야 합니다.
    *   **`np.vstack` (Vertical Stack)**: 주어진 배열들을 수직 방향(행 방향, axis=0)으로 결합합니다. 이때, 결합되는 배열들의 열의 개수(두 번째 차원의 크기)가 동일해야 합니다. `np.vstack`은 1차원 배열을 2차원 행 벡터(row vector)로 변환하여 결합합니다.
    *   **`np.column_stack`**: 주어진 1차원 배열들을 2차원 열 벡터(column vector)로 변환한 후 수평으로 결합합니다. 2차원 배열은 그대로 유지됩니다. 주로 여러 1차원 데이터를 컬럼 형태로 묶어 새로운 2차원 배열을 생성하거나, 기존 2차원 배열에 열을 추가할 때 유용합니다. `np.hstack`과 달리 1차원 배열을 자동으로 열 벡터로 처리해줍니다.

- **코드/수식 해설**:
주어진 예시에서는 다음과 같은 NumPy 배열들이 사용됩니다:
```python
import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]) # 형태 (3, 4)

c = np.array([1, 3, 5])         # 형태 (3,)

b = np.array([1, 2, 3, 4])      # 형태 (4,)
```

1.  **`np.hstack((a, c[:, None]))`**:
    *   `c[:, None]`는 1차원 배열 `c`의 차원을 확장하여 `(3,)` 형태를 `(3, 1)` 형태의 2차원 열 벡터로 만듭니다. `None` 또는 `np.newaxis`를 사용하여 특정 축에 새로운 차원을 추가할 수 있습니다.
    *   `a` (3x4)와 `c[:, None]` (3x1)는 행의 개수가 3으로 같으므로, `hstack`으로 수평 결합이 가능합니다.
    *   결과 배열은 $3 \times (4+1) = 3 \times 5$ 형태가 되며, `a`의 오른쪽에 `c`가 열로 추가된 형태입니다.

2.  **`np.column_stack((a, c))`**:
    *   `np.column_stack`은 입력으로 1차원 배열 `c`를 받으면 자동으로 `(3, 1)` 형태의 열 벡터로 변환하여 `a`와 수평 결합합니다. 이는 `c[:, None]`를 명시적으로 사용할 필요 없이 1차원 배열을 열로 추가할 때 편리합니다.
    *   이 코드의 결과는 `np.hstack((a, c[:, None]))`의 결과와 동일합니다.

3.  **`np.vstack((a, b))`**:
    *   `a` (3x4)와 1차원 배열 `b` (4,)를 수직으로 결합합니다.
    *   `np.vstack`은 1차원 배열 `b`를 `(1, 4)` 형태의 2차원 행 벡터로 간주하여 처리합니다.
    *   `a`의 열의 개수(4)와 `b`가 행 벡터로 간주되었을 때의 열의 개수(4)가 같으므로 수직 결합이 가능합니다.
    *   결과 배열은 $(3+1) \times 4 = 4 \times 4$ 형태가 되며, `a`의 아래쪽에 `b`가 행으로 추가된 형태입니다.

- **구체적 예시**:
회사의 직원 데이터를 관리한다고 상상해 봅시다.
*   `a`는 3명의 직원에 대한 (사원번호, 이름, 부서, 직급) 정보를 담은 행렬이라고 할 수 있습니다.
*   `c`는 이 3명의 직원의 (연봉) 정보라고 할 수 있습니다.
    *   `np.column_stack((a, c))`는 기존 직원 정보 옆에 연봉 정보를 새로운 컬럼으로 추가하여, 각 직원의 모든 정보를 한 눈에 볼 수 있는 확장된 데이터 테이블을 만드는 것과 유사합니다.
*   `b`는 새로 입사한 한 명의 직원에 대한 (사원번호, 이름, 부서, 직급) 정보라고 할 수 있습니다.
    *   `np.vstack((a, b))`는 기존 직원 데이터 테이블 아래에 새로운 직원의 정보를 한 행으로 추가하여, 전체 직원의 목록을 업데이트하는 것과 같습니다.

- **시험 포인트**:
*   ⭐ **`np.hstack`, `np.vstack`, `np.column_stack` 세 함수의 정확한 기능과 1차원 배열 처리 방식의 차이점을 명확히 이해해야 합니다.** 특히 `column_stack`이 1차원 배열을 자동으로 열 벡터로 변환한다는 점을 기억하세요.
*   ⭐ **배열 결합 시 입력 배열 간에 어떤 차원이 일치해야 하는지 파악하는 것이 중요합니다.** `hstack`은 행의 개수, `vstack`은 열의 개수가 일치해야 합니다.
*   ⭐ **`c[:, None]`와 같이 `np.newaxis` 또는 `None`을 사용하여 배열의 차원을 확장하는 인덱싱 기법을 이해하고 활용할 수 있어야 합니다.** 이는 1차원 배열을 2차원 열 벡터로 변환하는 데 필수적입니다.

---
## Slide 55

### 핵심 개념

NumPy의 벡터 또는 배열을 결합(staking)하는 다양한 방법을 다룹니다. 주로 1차원 배열(벡터)을 수평(horizontal), 수직(vertical), 또는 열(column) 방향으로 쌓아 더 큰 배열을 만드는 방법을 이해하는 것이 목표입니다.

*   **수평 스태킹 (Horizontal Stacking)**: 배열들을 옆으로 나란히 연결하여 새로운 배열을 생성합니다. (예: `np.hstack`, `np.r_`)
*   **수직 스태킹 (Vertical Stacking)**: 배열들을 위아래로 쌓아 새로운 배열을 생성합니다. (예: `np.vstack`, `np.r_`)
*   **열 스태킹 (Column Stacking)**: 여러 1차원 배열을 각각 열 벡터로 변환한 후 수평으로 결합하여 2차원 배열을 생성합니다. (예: `np.column_stack`, `np.c_`)

### 코드/수식 해설

NumPy 라이브러리를 사용하여 두 개의 1차원 배열 `a`와 `b`를 정의하고 다양한 방식으로 결합합니다.

```python
import numpy as np

a = np.array([1, 2, 3]) # shape: (3,)
b = np.array([4, 5, 6]) # shape: (3,)
```

1.  **수평 스태킹 (Horizontal Stacking)**
    *   `np.hstack((a, b))`는 두 배열을 가로로 이어 붙입니다.
    *   결과 배열의 `shape`는 요소들의 총 개수가 됩니다.
    *   `np.r_[a, b]`는 `np.hstack`의 편리한 단축 문법입니다.

    ```python
    result_hstack = np.hstack((a, b))
    # output: array([1, 2, 3, 4, 5, 6]), shape: (6,)

    result_r_ = np.r_[a, b]
    # output: array([1, 2, 3, 4, 5, 6]), shape: (6,)
    ```

2.  **수직 스태킹 (Vertical Stacking)**
    *   `np.vstack((a, b))`는 두 배열을 세로로 쌓아 올립니다.
    *   1차원 배열이 스택될 때는 각각 하나의 행으로 간주되어 2차원 배열을 생성합니다.
    *   `np.r_[a, b]` 또한 1차원 배열을 콤마로 구분하여 사용하면 수평 스태킹과 동일하게 작동하며, 수직 스태킹을 위해서는 `a[:, np.newaxis]` 형태로 차원을 명시해야 합니다. 슬라이드에서는 `np.vstack` 예시만 있습니다.

    ```python
    result_vstack = np.vstack((a, b))
    # output:
    # [[1 2 3]
    #  [4 5 6]]
    # shape: (2, 3)
    ```

3.  **열 스태킹 (Column Stacking)**
    *   `np.column_stack((a, b))`는 각 1차원 배열을 열(column)으로 변환한 뒤, 이를 수평으로 결합하여 새로운 2차원 배열을 생성합니다.
    *   이 과정은 내부적으로 `a[:, None]` (또는 `a[:, np.newaxis]`)와 같이 각 1차원 배열을 2차원 열 벡터로 변환한 후 `np.hstack`을 수행하는 것과 같습니다.
    *   `np.c_[a, b]`는 `np.column_stack`의 편리한 단축 문법입니다.

    ```python
    result_column_stack = np.column_stack((a, b))
    # output:
    # [[1 4]
    #  [2 5]
    #  [3 6]]
    # shape: (3, 2)

    # 내부 동작 방식 (개념적으로):
    a_reshaped = a[:, None] # output: [[1],[2],[3]], shape: (3, 1)
    b_reshaped = b[:, None] # output: [[4],[5],[6]], shape: (3, 1)
    result_manual_column = np.hstack((a_reshaped, b_reshaped))
    # output:
    # [[1 4]
    #  [2 5]
    #  [3 6]]
    # shape: (3, 2)

    result_c_ = np.c_[a, b]
    # output:
    # [[1 4]
    #  [2 5]
    #  [3 6]]
    # shape: (3, 2)
    ```

### 구체적 예시

**실생활 비유:**

*   **`np.hstack` (수평 스태킹)**:
    *   여러 개의 단어 카드를 옆으로 나란히 붙여 긴 문장을 만드는 것과 같습니다. "빨강", "파랑", "노랑" 카드를 "빨강파랑노랑"으로 만드는 거죠.
    *   또는 기차의 여러 칸을 앞뒤로 연결하는 것과 비슷합니다. [1호칸, 2호칸] 다음에 [3호칸, 4호칸]을 연결하면 [1호칸, 2호칸, 3호칸, 4호칸]이 됩니다.

*   **`np.vstack` (수직 스태킹)**:
    *   여러 권의 책을 책장에 위아래로 쌓는 것과 같습니다. 첫 번째 줄에 "인공지능 개론" 책을 놓고, 그 아래에 "데이터 과학" 책을 놓는 식입니다.
    *   또는 엑셀 시트에서 여러 행 데이터를 순서대로 추가하는 것과 유사합니다.

*   **`np.column_stack` (열 스태킹)**:
    *   새로운 표(테이블)를 만들 때, "이름" 열과 "나이" 열을 각각 별도로 작성한 후, 이 두 열을 합쳐 하나의 테이블로 만드는 것과 같습니다.
        *   `a` (이름): [철수, 영희, 민수]
        *   `b` (나이): [20, 22, 21]
        *   `np.column_stack((a, b))` 결과:
            ```
            [[철수, 20],
             [영희, 22],
             [민수, 21]]
            ```
        이처럼 각 1차원 배열이 테이블의 한 열이 됩니다.

### 시험 포인트

*   ⭐ **`np.hstack`과 `np.vstack`의 차이점**: 1차원 배열을 결합할 때, `hstack`은 1차원 배열을 유지하며 길이를 늘리고, `vstack`은 2차원 배열을 생성하여 행의 수를 늘립니다.
*   ⭐ **`np.column_stack`의 특성**: `np.column_stack`은 1차원 배열을 인자로 받으면 자동으로 각 배열을 2차원 열 벡터로 변환한 후 수평으로 쌓습니다. 이는 `a[:, None]`과 같은 차원 확장 후 `np.hstack`을 수행하는 것과 동일합니다.
*   ⭐ **`np.r_`과 `np.c_`의 사용법 및 결과**:
    *   `np.r_[arr1, arr2]`는 `np.hstack((arr1, arr2))`와 유사하게 작동합니다.
    *   `np.c_[arr1, arr2]`는 `np.column_stack((arr1, arr2))`와 유사하게 작동합니다. 이 두 단축 문법의 역할과 언제 각각을 사용해야 하는지 명확히 알아두세요.
*   ⭐ **결과 배열의 `shape` 예측**: 각 스태킹 함수가 인자로 받은 배열들의 `shape`에 따라 최종 결과 배열의 `shape`가 어떻게 변하는지 이해하는 것이 중요합니다. 특히 1차원 배열을 2차원 배열로 만드는 `vstack`과 `column_stack`의 경우를 잘 파악해야 합니다.

---
## Slide 56

### 핵심 개념
`np.vstack()` 함수는 NumPy 배열들을 수직(vertical) 방향으로, 즉 행(row)을 추가하는 방식으로 쌓아(stack) 하나의 배열로 합치는 함수입니다. 이는 `axis=0`을 따라 배열의 크기를 확장합니다.

*   **수직 쌓기 (Stack on top)**: 입력 배열들을 위에서 아래로 쌓아 올립니다. 결과적으로 새로운 배열의 행(axis 0)의 수가 증가합니다.
*   **1차원 배열 처리**: `vstack`은 1차원 배열(e.g., `(N,)` 형태)을 스택하기 전에 단일 행(single row)을 가진 2차원 배열(e.g., `(1, N)` 형태)로 변환하여 처리합니다.
*   **호환성 조건**: `vstack`으로 합쳐지는 모든 배열은 첫 번째 축(axis 0)을 제외한 나머지 축들의 크기가 같아야 합니다. 즉, 2차원 배열의 경우 열의 개수가 같아야 합니다.

### 코드/수식 해설

```python
import numpy as np

# 예시 1: 1차원 배열 vstack
a = np.array([1, 2, 3])      # shape (3,)
b = np.array([10, 20, 30])   # shape (3,)
V = np.vstack([a, b])
# a와 b는 각각 (3,) shape의 1차원 배열입니다.
# np.vstack은 이들을 (1, 3) shape의 2차원 배열로 간주하여 스택합니다.
# V의 내용은 [[ 1,  2,  3], [10, 20, 30]] 이 됩니다.
# 따라서 V.shape는 (2, 3)이 됩니다.

# 예시 2: 2차원 배열 vstack
A = np.arange(4).reshape(2, 2) # shape (2, 2)
# A의 내용은 [[0, 1], [2, 3]]
B = (A + 100)                  # shape (2, 2)
# B의 내용은 [[100, 101], [102, 103]]
V2 = np.vstack([A, B])
# A와 B는 모두 (2, 2) shape의 2차원 배열입니다.
# np.vstack은 이들을 그대로 수직으로 쌓습니다.
# V2의 내용은 [[  0,   1], [  2,   3], [100, 101], [102, 103]] 이 됩니다.
# 따라서 V2.shape는 (4, 2)가 됩니다.

print(V.shape, V2.shape)
# 출력: (2, 3) (4, 2)
# 이 출력은 위에서 설명한 V와 V2의 최종 shape를 확인시켜 줍니다.
```

### 구체적 예시

여러 부서의 직원 명단이 각각 NumPy 배열로 주어졌다고 상상해 봅시다. 각 명단은 '직원 ID', '이름', '부서'와 같은 동일한 형식(열의 개수)을 가지고 있습니다.

*   `department_a = np.array([[101, '김철수', '개발'], [102, '이영희', '개발']])`
*   `department_b = np.array([[201, '박지영', '인사'], [202, '최민준', '인사']])`

이 두 배열을 `np.vstack([department_a, department_b])`를 사용하여 합치면, 전체 직원의 명단이 담긴 하나의 큰 배열을 얻을 수 있습니다. 여기서 `department_a`와 `department_b`는 각기 다른 행을 가지지만, '직원 ID', '이름', '부서'라는 세 개의 열을 동일하게 가지고 있으므로 `vstack`이 문제없이 작동합니다. 결과 배열은 `(4, 3)`의 shape를 가지게 되어 모든 직원의 데이터를 포함하게 됩니다.

1차원 배열의 경우, 예를 들어 한 학생의 과목별 점수가 `korean_scores = np.array([90, 85, 92])`와 같이 있고, 다른 학생의 점수가 `math_scores = np.array([78, 88, 95])`와 같이 있을 때, `np.vstack([korean_scores, math_scores])`는 각 학생의 점수 배열을 하나의 행으로 간주하여 `[[90, 85, 92], [78, 88, 95]]`와 같이 쌓아 올립니다.

### 시험 포인트

*   ⭐ **`np.vstack()`의 역할과 작동 방식**: 배열들을 수직 방향(axis 0)으로 쌓아 올리며 행의 수를 증가시킵니다.
*   ⭐ **1차원 배열 처리 방식**: 1차원 배열은 `vstack` 전에 단일 행을 가진 2차원 배열(`(1, N)`)로 변환됩니다.
*   ⭐ **스택을 위한 배열의 호환성 조건**: 스택하려는 배열들은 `axis=0`을 제외한 다른 축들의 크기(예: 열의 개수)가 모두 같아야 합니다.
*   `np.vstack`과 유사한 함수(`np.hstack`, `np.concatenate`)의 차이점을 함께 이해하는 것이 중요합니다. (`np.hstack`은 수평 방향, `np.concatenate`는 지정된 축을 따라 스택)

---
## Slide 57

**핵심 개념**

`np.vstack`은 NumPy 배열들을 수직(row-wise)으로 쌓아 새로운 배열을 생성하는 함수입니다. "formal semantics"는 이러한 스택킹 작업이 어떻게 내부적으로 정의되고 수행되는지에 대한 수학적이고 명확한 규칙을 설명합니다.

1.  **1D 배열 처리 (Promotion)**: `np.vstack`에 1차원 배열이 입력되면, 이를 먼저 `(1, N)` 형태의 2차원 '행' 배열로 승격(promote)시킵니다. 예를 들어, `[1, 2, 3]`은 `[[1, 2, 3]]`이 됩니다.
2.  **입력 배열 제약 조건**: 승격 작업 후, 모든 입력 배열은 다음 조건을 만족해야 합니다.
    *   모든 배열은 최소 2차원($d \ge 2$)이어야 하며, 동일한 차원 수($d$)를 가져야 합니다.
    *   첫 번째 차원(axis 0, 행의 개수)을 제외한 나머지 차원들(axes $1 \dots d-1$)의 크기가 모두 동일해야 합니다. 즉, 열의 개수, 깊이 등의 후속 차원 크기는 일치해야 합니다.
3.  **결과 배열의 형태**: 최종 결과 배열 `Y`의 형태는 다음과 같이 결정됩니다.
    *   첫 번째 차원(axis 0)의 크기는 모든 승격된 입력 배열들의 첫 번째 차원 크기의 합이 됩니다.
    *   나머지 차원들(axes $1 \dots d-1$)의 크기는 첫 번째 입력 배열(또는 일치하는 어떤 입력 배열)의 해당 차원 크기와 동일합니다.
4.  **데이터 배치**: 각 입력 배열 `A^(r)`의 데이터는 결과 배열 `Y` 내의 특정 위치에 배치됩니다. 이때 `o_r`이라는 오프셋을 사용하여 `r`번째 배열이 `Y`에서 시작하는 행 인덱스를 결정합니다.
5.  **`np.concatenate`와의 관계**: `np.vstack`은 1차원 배열을 2차원으로 승격시키는 과정을 포함한다는 점을 제외하면, 사실상 `np.concatenate`를 `axis=0`으로 사용하는 것과 동일합니다.

---

**코드/수식 해설**

*   **입력 배열**: $m$개의 배열 $(A^{(r)})_{r=1}^m$이 주어지며, 각각의 형태는 $s^{(r)} = (s_0^{(r)}, \dots, s_{d-1}^{(r)})$이고 동일한 데이터 타입 $\tau$를 가집니다.

*   **1D 배열 승격**:
    1차원 입력 `x` (형태 $(N,)$)는 `x^` (형태 $(1, N)$)로 승격됩니다.
    $$ x^\uparrow[0,j] = x[j] $$

*   **결과 배열의 형태**:
    $\tilde{s}^{(r)}$을 승격된 배열들의 형태라고 할 때, 최종 결과 배열 $Y$의 형태는 다음과 같습니다.
    $$ \left( \sum_{r=1}^m \tilde{s}_0^{(r)}, \tilde{s}_1^{(1)}, \dots, \tilde{s}_{d-1}^{(1)} \right) $$
    *   $\sum_{r=1}^m \tilde{s}_0^{(r)}$: 모든 승격된 배열들의 첫 번째 차원(행의 개수)을 합한 값입니다.
    *   $\tilde{s}_1^{(1)}, \dots, \tilde{s}_{d-1}^{(1)}$: 첫 번째 승격된 배열의 두 번째 차원부터 마지막 차원까지의 크기입니다. (이 차원들은 모든 입력 배열에서 동일해야 합니다.)

*   **데이터 배치 공식**:
    $o_r$은 `r`번째 배열이 결과 `Y`에서 시작하는 행 오프셋을 의미합니다.
    $$ o_r = \sum_{p<r} \tilde{s}_0^{(p)} $$
    이 오프셋을 이용하여, `r`번째 승격된 입력 배열 $\tilde{A}^{(r)}$의 요소가 결과 배열 $Y$에 어떻게 배치되는지 정의됩니다.
    $$ Y[o_r + i, j_1, \dots, j_{d-1}] = \tilde{A}^{(r)}[i, j_1, \dots, j_{d-1}] $$
    *   `i`는 `r`번째 배열 내에서의 행 인덱스, `j1`부터 `jd-1`은 그 이후의 차원 인덱스를 의미합니다.

*   **`np.vstack` 예시**:
    ```python
    import numpy as np

    # 1D 배열 승격 예시
    a1 = np.array([1, 2, 3])
    a2 = np.array([4, 5, 6])
    print(f"a1.shape: {a1.shape}") # (3,)
    print(f"np.vstack([a1, a2]).shape: {np.vstack([a1, a2]).shape}") # (2, 3) -> 1D 배열이 (1,3)으로 승격된 후 스택됨

    # 2D 배열 스택킹 예시
    b1 = np.array([[1, 2], [3, 4]])
    b2 = np.array([[5, 6], [7, 8]])
    print(f"b1.shape: {b1.shape}") # (2, 2)
    result = np.vstack([b1, b2])
    print(f"np.vstack([b1, b2]):\n{result}")
    # [[1, 2],
    #  [3, 4],
    #  [5, 6],
    #  [7, 8]]
    print(f"result.shape: {result.shape}") # (4, 2) -> (2+2, 2)
    ```

---

**구체적 예시**

`np.vstack`은 마치 여러 장의 종이를 한 줄로 세로로 붙여 긴 두루마리를 만드는 것과 유사합니다. 각 종이(배열)는 일정한 너비(axis 1 이후의 차원)를 가져야 하고, 그 높이(axis 0)만 달라도 됩니다.

1.  **1차원 배열의 승격 및 스택킹**:
    학생들의 중간고사 점수 리스트 `s1 = [80, 90, 75]`와 기말고사 점수 리스트 `s2 = [85, 92, 78]`가 있다고 가정해 봅시다.
    ```python
    import numpy as np
    s1 = np.array([80, 90, 75])
    s2 = np.array([85, 92, 78])
    # np.vstack은 s1을 [[80, 90, 75]]로, s2를 [[85, 92, 78]]로 승격한 후 쌓습니다.
    scores_matrix = np.vstack([s1, s2])
    print(scores_matrix)
    # 결과:
    # [[80, 90, 75],
    #  [85, 92, 78]]
    print(f"Shape: {scores_matrix.shape}") # (2, 3)
    # (s1의 (1,) 승격 -> (1,3), s2의 (1,) 승격 -> (1,3))
    # 최종 shape = (1+1, 3) = (2, 3)
    ```
    여기서 각 행은 한 시험의 점수를 나타내고, 각 열은 각 학생의 점수를 나타냅니다.

2.  **2차원 배열의 스택킹 (일반적인 경우)**:
    두 부서의 월별 판매 데이터를 담은 행렬이 있습니다.
    ```python
    dept_A_sales = np.array([[100, 120, 110],  # 1월, 2월, 3월
                             [150, 130, 140]]) # 4월, 5월, 6월
    dept_B_sales = np.array([[200, 210, 220],
                             [180, 190, 170]])
    
    total_sales = np.vstack([dept_A_sales, dept_B_sales])
    print(total_sales)
    # 결과:
    # [[100, 120, 110],
    #  [150, 130, 140],
    #  [200, 210, 220],
    #  [180, 190, 170]]
    print(f"Shape: {total_sales.shape}") # (4, 3)
    # dept_A_sales (2,3), dept_B_sales (2,3)
    # 최종 shape = (2+2, 3) = (4, 3)
    ```
    각 부서의 데이터가 세로로 쌓여 전체 판매 데이터를 나타내는 하나의 행렬이 되었습니다.

3.  **오류 발생하는 경우 (차원 불일치)**:
    만약 열의 개수가 일치하지 않으면 오류가 발생합니다.
    ```python
    matrix1 = np.array([[1, 2], [3, 4]]) # (2, 2)
    matrix2 = np.array([[5, 6, 7]])     # (1, 3)
    
    try:
        np.vstack([matrix1, matrix2])
    except ValueError as e:
        print(f"Error: {e}")
    # Error: all input array dimensions for the concatenation axis must match exactly, but along dimension 1, the array at index 0 has size 2 and the array at index 1 has size 3
    ```
    이 오류 메시지는 `axis=1` (열)의 크기가 `matrix1`은 2인데 `matrix2`는 3이라서 스택킹할 수 없다는 것을 명확히 보여줍니다.

---

**시험 포인트**

*   **⭐ `np.vstack`의 주요 기능과 스택킹 방향**: 배열을 수직(행 기준, `axis=0`)으로 쌓는다는 것을 이해해야 합니다.
*   **⭐ 1차원 배열 처리 방식**: 1차원 배열이 `(1, N)` 형태의 2차원 배열로 자동 '승격'된다는 점을 아는 것이 중요합니다.
*   **⭐ 입력 배열의 필수 조건**: `vstack`을 성공적으로 사용하기 위한 입력 배열들의 제약 조건(승격 후 동일한 차원 수, `axis=0`을 제외한 모든 차원 크기 일치)을 정확히 설명할 수 있어야 합니다. 특히 `axis=1..d-1`이 일치해야 한다는 점!
*   **⭐ 결과 배열의 형태 계산**: 주어진 입력 배열들의 형태를 바탕으로 `vstack` 결과 배열의 형태를 예측할 수 있어야 합니다. (sum of `axis=0` dimensions, others preserved)
*   **⭐ `np.concatenate`와의 관계**: `np.vstack`이 1차원 배열 승격 단계를 포함하는 `np.concatenate(..., axis=0)`의 특수한 경우임을 이해하고 설명할 수 있어야 합니다.

---
## Slide 58

**핵심 개념**

`numpy.hstack()`은 NumPy 배열을 "수평 방향(horizontally)"으로 결합하거나 쌓아서 새로운 배열을 생성하는 함수입니다. 이 함수의 동작은 입력 배열의 차원에 따라 다르게 적용됩니다.

1.  **1차원 (1D) 배열의 경우**: 여러 1차원 배열들을 순서대로 이어 붙여(concatenate) 더 긴 하나의 1차원 배열을 만듭니다. 이는 벡터 연결(vector concatenation)과 동일합니다.
2.  **2차원 (2D) 이상의 배열의 경우**: 배열들을 옆으로 나란히 쌓아 올립니다. 즉, 두 번째 축(axis 1, 열)을 따라 확장하여 열의 수가 증가한 새로운 배열을 만듭니다. 이 경우, 첫 번째 축(axis 0, 행)의 크기는 결합하려는 모든 배열에서 동일해야 합니다.

**코드/수식 해설**

아래 코드는 `np.hstack`이 1차원 및 2차원 배열에 대해 어떻게 동작하는지 보여주는 예시입니다.

```python
import numpy as np

# 1차원 배열 예시
a = np.array([1, 2, 3])        # a는 (3,) shape의 1차원 배열
b = np.array([10, 20, 30])     # b는 (3,) shape의 1차원 배열
H = np.hstack([a, b])          # a와 b를 수평으로 연결하여 새로운 1차원 배열 생성
                               # H는 [1, 2, 3, 10, 20, 30] 이 되며 shape는 (6,)

# 2차원 배열 예시
A = np.arange(4).reshape(2, 2) # 0부터 3까지의 숫자로 (2, 2) 형태의 2차원 배열 생성
                               # A: [[0, 1],
                               #     [2, 3]]
                               # A의 shape는 (2, 2)
B = (A + 100)                  # A의 각 원소에 100을 더하여 새로운 2차원 배열 B 생성
                               # B: [[100, 101],
                               #     [102, 103]]
                               # B의 shape는 (2, 2)
H2 = np.hstack([A, B])         # A와 B를 수평으로 쌓음 (열 방향으로 확장)
                               # H2: [[  0,   1, 100, 101],
                               #      [  2,   3, 102, 103]]
                               # H2의 shape는 (2, 4)

print(H.shape, H2.shape)       # 최종적으로 H의 shape와 H2의 shape를 출력: (6,) (2, 4)
```

**수식 설명**:
`np.hstack`을 통한 배열의 차원 및 형태 변화는 다음과 같이 표현할 수 있습니다.

1.  **1차원 배열 연결**:
    두 개의 1차원 배열 $\mathbf{v}_1 \in \mathbb{R}^{m}$과 $\mathbf{v}_2 \in \mathbb{R}^{n}$을 `hstack`하면, 결과는 $\mathbf{v}_{\text{new}} \in \mathbb{R}^{m+n}$인 1차원 배열이 됩니다.
    $$ \text{hstack}([\mathbf{v}_1, \mathbf{v}_2]) = [\mathbf{v}_1[0], \dots, \mathbf{v}_1[m-1], \mathbf{v}_2[0], \dots, \mathbf{v}_2[n-1]] $$

2.  **2차원 배열 수평 스택**:
    두 개의 2차원 배열 $\mathbf{M}_1 \in \mathbb{R}^{r \times c_1}$과 $\mathbf{M}_2 \in \mathbb{R}^{r \times c_2}$를 `hstack`하면, 결과는 $\mathbf{M}_{\text{new}} \in \mathbb{R}^{r \times (c_1+c_2)}$인 2차원 배열이 됩니다.
    이때, 두 배열의 행의 수 $r$은 반드시 같아야 합니다.
    $$ \text{hstack}([\mathbf{M}_1, \mathbf{M}_2]) = \begin{pmatrix} \mathbf{M}_1[0,0] & \dots & \mathbf{M}_1[0,c_1-1] & \mathbf{M}_2[0,0] & \dots & \mathbf{M}_2[0,c_2-1] \\ \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ \mathbf{M}_1[r-1,0] & \dots & \mathbf{M}_1[r-1,c_1-1] & \mathbf{M}_2[r-1,0] & \dots & \mathbf{M}_2[r-1,c_2-1] \end{pmatrix} $$

**구체적 예시**

`np.hstack`은 마치 여러 개의 LEGO 블록을 옆으로 길게 이어서 더 큰 구조물을 만드는 것과 같습니다.

1.  **1차원 배열 ($a, b$)**: `a = [1, 2, 3]`이라는 3칸짜리 띠 블록과 `b = [10, 20, 30]`이라는 또 다른 3칸짜리 띠 블록을 옆으로 나란히 이으면, `H = [1, 2, 3, 10, 20, 30]`과 같은 총 6칸짜리 긴 띠 블록이 됩니다. 이는 데이터 포인트를 단순히 이어 붙이는 경우에 유용합니다.

2.  **2차원 배열 ($A, B$)**:
    `A = [[0, 1], [2, 3]]`은 2행 2열의 정사각형 블록입니다.
    `B = [[100, 101], [102, 103]]` 역시 2행 2열의 정사각형 블록입니다.
    이 두 블록을 `hstack`으로 연결하면, 높이(행)는 그대로 둔 채 너비(열)만 확장됩니다. 각 행이 옆으로 이어 붙여져 새로운 배열 `H2`는 `[[0, 1, 100, 101], [2, 3, 102, 103]]`과 같은 2행 4열의 직사각형 블록이 됩니다. 이는 서로 다른 특성(feature) 셋을 가진 두 데이터 테이블을 병합하여 새로운 특성 공간을 만들 때와 같은 상황에 비유할 수 있습니다. 예를 들어, 한 테이블은 학생들의 이름과 학번을, 다른 테이블은 학번과 전공을 가지고 있을 때, 학번을 기준으로 이들을 수평으로 합쳐서 이름, 학번, 전공을 모두 포함하는 하나의 테이블을 만드는 것과 유사합니다.

**시험 포인트**

*   ⭐ **`np.hstack`의 기본 개념**: 배열을 수평 방향(열 방향, axis=1)으로 결합하거나 쌓는다는 것을 이해해야 합니다.
*   ⭐ **1차원 배열과 2차원 이상의 배열 처리 방식 차이**:
    *   1차원 배열: 단순 연결 (concatenation).
    *   2차원 이상 배열: 열 방향 확장 (두 번째 축 확장).
*   ⭐ **입력 배열의 호환성 조건**:
    *   `np.hstack`으로 결합하려는 2차원 이상의 배열들은 반드시 **첫 번째 축(axis 0, 행)의 크기(row count)**가 동일해야 합니다. (예: `(2, 3)`과 `(2, 5)`는 `hstack` 가능하지만, `(2, 3)`과 `(3, 3)`은 불가능)
*   `np.vstack` (수직 스택), `np.concatenate` (축 지정 스택), `np.stack` (새로운 축 생성 스택) 등 다른 스태킹 함수들과의 차이점을 비교하고 각각의 사용 시점을 구분할 수 있어야 합니다.

---
## Slide 59

NumPy의 `hstack` 함수에 대한 상세 내용입니다. `hstack`은 "horizontal stack"의 약자로, 배열들을 수평 방향(열 방향)으로 이어 붙일 때 사용됩니다.

---

**핵심 개념**:
*   `numpy.hstack`은 여러 NumPy 배열을 열 방향(column-wise)으로 쌓아 하나의 배열로 결합하는 함수입니다.
*   `hstack`의 동작은 입력 배열의 차원(dimension)에 따라 두 가지 주요 케이스로 나뉩니다.
*   이는 사실 `np.concatenate(arrays, axis=1)`과 동등하며, 1차원 배열의 경우 `axis=0`에서 동작하는 `np.concatenate`와 유사하게 작동합니다.
*   `hstack` 사용 시 **1차원 배열과 2차원 이상의 배열을 혼합하여 입력으로 제공할 수 없습니다.** (ValueError 발생)

---

**코드/수식 해설**:

`hstack` 함수는 $m$개의 입력 배열 $(A^{(r)})_{r=1}^m$을 받아 하나의 결과 배열 $Y$를 생성합니다. 각 입력 배열 $A^{(r)}$은 형태(shape) $s^{(r)} = (s^{(r)}_0, \dots, s^{(r)}_{d_r-1})$와 데이터 타입 $\tau$를 가집니다.

1.  **Case 1: 모든 입력이 1차원(1D) 배열인 경우**
    *   `hstack`은 모든 1차원 배열을 단순히 순서대로 이어 붙입니다.
    *   결과 배열 $Y$의 총 길이는 모든 입력 배열의 길이의 합입니다. 각 $s^{(r)}_0$는 $r$-번째 1차원 배열 $A^{(r)}$의 길이를 나타냅니다.
        $$ \text{Result length} = \sum_{r=1}^m s^{(r)}_0 $$
    *   결과 배열 $Y$의 원소는 각 입력 배열 $A^{(r)}$의 원소에 다음과 같이 매핑됩니다. 여기서 $o_r$은 $A^{(r)}$이 결과 배열 내에서 시작하는 오프셋(이전 배열들의 길이 합)입니다.
        $$ Y[o_r + j] = A^{(r)}[j] \quad \text{where } o_r = \sum_{p<r} s^{(p)}_0 $$

2.  **Case 2: 모든 입력이 2차원(2D) 이상의 배열인 경우**
    *   모든 입력 배열은 동일한 차원 $d \ge 2$를 가져야 합니다.
    *   또한, 두 번째 축(`axis=1`)을 제외한 나머지 모든 축들($\{0, 2, \dots, d-1\}$)의 크기가 모든 입력 배열에서 동일해야 합니다.
    *   결과 배열 $Y$의 형태는 다음과 같습니다. 첫 번째 차원 $s_0^{(1)}$은 모든 배열에서 동일해야 하고, 두 번째 차원 $s_1^{(r)}$들만 합쳐지며, 이후의 차원들 $s_2^{(1)}, \dots, s_{d-1}^{(1)}$도 모든 배열에서 동일해야 합니다.
        $$ (s_0^{(1)}, \sum_{r=1}^m s_1^{(r)}, s_2^{(1)}, \dots, s_{d-1}^{(1)}) $$
    *   각 입력 배열 $A^{(r)}$의 원소가 결과 배열 $Y$에 매핑되는 방식은 다음과 같습니다. 여기서 $o_r$은 $A^{(r)}$이 결과 배열의 두 번째 차원(`axis=1`)에서 시작하는 오프셋(이전 배열들의 `axis=1` 크기 합)입니다.
        $$ o_r = \sum_{p<r} s_1^{(p)} $$
        $$ Y[i, o_r + j, j_2, \dots, j_{d-1}] = A^{(r)}[i, j, j_2, \dots, j_{d-1}] $$
    *   이 동작은 `np.concatenate(arrays, axis=1)`과 완전히 동일합니다.

---

**구체적 예시**:

```python
import numpy as np

# Case 1: 1차원(1D) 배열들을 hstack
print("--- Case 1: 1D 배열 hstack ---")
arr_1d_a = np.array([1, 2, 3]) # shape (3,)
arr_1d_b = np.array([4, 5])    # shape (2,)
arr_1d_c = np.array([6, 7, 8, 9]) # shape (4,)

result_1d = np.hstack([arr_1d_a, arr_1d_b, arr_1d_c])
print("입력 배열 shapes:", arr_1d_a.shape, arr_1d_b.shape, arr_1d_c.shape)
print("hstack 결과:", result_1d)
print("결과 shape:", result_1d.shape) # (3+2+4,) = (9,)
# 수식 예시: Y[0]=A(a)[0], Y[1]=A(a)[1], Y[2]=A(a)[2] (o_a=0)
# Y[3]=A(b)[0], Y[4]=A(b)[1] (o_b=3)
# Y[5]=A(c)[0], Y[6]=A(c)[1], Y[7]=A(c)[2], Y[8]=A(c)[3] (o_c=5)

print("\n--- Case 2: 2차원(2D) 배열들을 hstack ---")
# 조건: axis=0의 크기는 동일해야 함 (여기서는 2)
arr_2d_a = np.array([[1, 2], [3, 4]]) # shape (2, 2)
arr_2d_b = np.array([[5, 6, 7], [8, 9, 10]]) # shape (2, 3)
arr_2d_c = np.array([[11], [12]]) # shape (2, 1)

result_2d = np.hstack([arr_2d_a, arr_2d_b, arr_2d_c])
print("입력 배열 shapes:", arr_2d_a.shape, arr_2d_b.shape, arr_2d_c.shape)
print("hstack 결과:\n", result_2d)
print("결과 shape:", result_2d.shape) # (2, 2+3+1) = (2, 6)
# 수식 예시: axis=1을 따라 결합.
# s(a)=(2,2), s(b)=(2,3), s(c)=(2,1)
# Result shape = (s0_a, s1_a + s1_b + s1_c) = (2, 2+3+1) = (2,6)
# o_a = 0
# o_b = s1_a = 2
# o_c = s1_a + s1_b = 2 + 3 = 5

print("\n--- Case 2: 3차원(3D) 배열들을 hstack (개념 설명) ---")
# 조건: axis=0, axis=2의 크기는 동일해야 함
arr_3d_x = np.zeros((2, 3, 4)) # shape (2, 3, 4)
arr_3d_y = np.zeros((2, 5, 4)) # shape (2, 5, 4)
arr_3d_z = np.zeros((2, 1, 4)) # shape (2, 1, 4)

# axis=1만 크기가 다르고 합쳐짐
result_3d_shape = np.hstack([arr_3d_x, arr_3d_y, arr_3d_z]).shape
print("입력 배열 shapes:", arr_3d_x.shape, arr_3d_y.shape, arr_3d_z.shape)
print("hstack 결과 shape:", result_3d_shape) # (2, 3+5+1, 4) = (2, 9, 4)

print("\n--- 허용되지 않는 경우: 1D와 2D 배열 혼합 ---")
try:
    np.hstack([arr_1d_a, arr_2d_a])
except ValueError as e:
    print(f"에러 발생: {e}")
# 출력: 에러 발생: all the input array dimensions except for the concatenation axis must match exactly
```

---

**시험 포인트**:
*   ⭐ `np.hstack`이 1D 배열과 2D 이상 배열을 처리하는 방식의 **주요 차이점**을 정확히 이해해야 합니다. 1D는 단순히 이어 붙이기, 2D 이상은 `axis=1`을 기준으로 결합입니다.
*   ⭐ `np.hstack`은 1D 배열의 경우 `np.concatenate(arrays, axis=0)`과 유사하고, 2D 이상의 배열의 경우 `np.concatenate(arrays, axis=1)`과 **동일하다**는 점을 기억하세요.
*   ⭐ `np.hstack` 사용 시 **1D 배열과 2D 이상 배열을 혼합하여 입력으로 사용할 수 없습니다.** 이를 시도하면 `ValueError`가 발생합니다.
*   ⭐ 2D 이상의 배열을 `hstack`할 때, **`axis=1`을 제외한 모든 다른 축의 크기**($s_0, s_2, \dots, s_{d-1}$)는 모든 입력 배열에서 **일치해야 합니다.** 불일치할 경우 `ValueError`가 발생합니다.

---
## Slide 60

**핵심 개념**
*   **NumPy 배열 스태킹 (Stacking)**: 여러 개의 NumPy 배열을 특정 축을 기준으로 합쳐(stack) 하나의 큰 배열을 만드는 연산입니다. 주로 `np.vstack`과 `np.hstack` 함수를 사용하며, 이는 `np.concatenate`의 특수한 경우입니다.
*   **`np.vstack` (Vertical Stack)**: 배열들을 수직(vertical) 방향으로 쌓습니다. 결과적으로 배열의 행(row) 수가 증가하며, 이는 `axis=0`을 기준으로 결합하는 것과 같습니다.
    *   1차원 배열을 입력으로 받으면, 각 1차원 배열을 (1, N) 형태의 2차원 배열(행 벡터)로 변환한 후 수직으로 쌓습니다.
*   **`np.hstack` (Horizontal Stack)**: 배열들을 수평(horizontal) 방향으로 쌓습니다. 결과적으로 배열의 열(column) 수가 증가하며, 이는 `axis=1`을 기준으로 결합하는 것과 같습니다.
    *   1차원 배열을 입력으로 받으면, 단순히 모든 원소를 이어 붙여(concatenate) 하나의 긴 1차원 배열을 만듭니다.
*   **`np.concatenate`**: NumPy 배열을 지정된 축(`axis`)을 따라 결합하는 일반적인 함수입니다. `vstack`은 `concatenate(axis=0)`와, `hstack`은 `concatenate(axis=1)`와 유사한 동작을 합니다.

**코드/수식 해설**

```python
import numpy as np

# 1D inputs
a = np.array([1, 2, 3])  # shape: (3,)
b = np.array([10, 20, 30]) # shape: (3,)

V1 = np.vstack([a, b])  # (2, 3): 1D -> rows, then axis=0 concat
H1 = np.hstack([a, b])  # (6,): 1D concatenation

print("V1 shape:", V1.shape, "\n", V1)
print("H1 shape:", H1.shape, "\n", H1)
```
*   `a`와 `b`는 각각 3개의 원소를 가진 1차원 배열입니다.
*   `np.vstack([a, b])`는 1차원 배열 `a`와 `b`를 각각 `[[1, 2, 3]]`과 `[[10, 20, 30]]` 형태의 2차원 행 벡터로 변환한 후 수직으로 쌓습니다. 결과 `V1`은 `[[ 1,  2,  3], [10, 20, 30]]`이 되며, `shape`은 `(2, 3)`입니다.
*   `np.hstack([a, b])`는 1차원 배열 `a`와 `b`의 원소들을 단순히 이어 붙여 하나의 1차원 배열을 만듭니다. 결과 `H1`은 `[ 1,  2,  3, 10, 20, 30]`이 되며, `shape`은 `(6,)`입니다.

```python
# 2D inputs
A = np.arange(6).reshape(2, 3)     # [[0, 1, 2], [3, 4, 5]]
B = np.arange(100, 106).reshape(2, 3) # [[100, 101, 102], [103, 104, 105]]

V2 = np.vstack([A, B])  # (4, 3): stack rows
H2 = np.hstack([A, B])  # (2, 6): stack columns

print("V2 shape:", V2.shape, "\n", V2)
print("H2 shape:", H2.shape, "\n", H2)
```
*   `A`와 `B`는 각각 (2, 3) 형태의 2차원 배열입니다.
*   `np.vstack([A, B])`는 `A`의 행들 아래에 `B`의 행들을 쌓습니다. 즉, `[[0, 1, 2], [3, 4, 5]]` 아래에 `[[100, 101, 102], [103, 104, 105]]`가 붙습니다. 결과 `V2`는 4행 3열의 배열이 되며, `shape`은 `(4, 3)`입니다.
*   `np.hstack([A, B])`는 `A`의 열들 옆에 `B`의 열들을 쌓습니다. 즉, `[[0, 1, 2], [3, 4, 5]]`의 오른쪽에 `[[100, 101, 102], [103, 104, 105]]`가 붙습니다. 결과 `H2`는 2행 6열의 배열이 되며, `shape`은 `(2, 6)`입니다.

```python
# Equivalence to concatenate
V2_eq = np.concatenate([A, B], axis=0) # V2와 동일
H2_eq = np.concatenate([A, B], axis=1) # H2와 동일

print("V2 == concat0?", np.array_equal(V2, V2_eq))
print("H2 == concat1?", np.array_equal(H2, H2_eq))
```
*   `np.vstack`은 `np.concatenate` 함수에서 `axis=0` (행 방향)으로 결합하는 것과 정확히 동일합니다.
*   `np.hstack`은 `np.concatenate` 함수에서 `axis=1` (열 방향)으로 결합하는 것과 정확히 동일합니다.
*   `np.array_equal(arr1, arr2)`는 두 배열의 요소와 shape이 모두 동일한지 확인하여 `True` 또는 `False`를 반환합니다. 이 코드는 `vstack`/`hstack`과 `concatenate`의 동등성을 확인합니다.

**구체적 예시**
*   **학생 정보 관리**:
    *   두 개의 엑셀 파일이 있다고 가정해 봅시다. 하나는 학생들의 이름, 학번, 전공 정보(`student_info_1`), 다른 하나는 학년, 반, 이메일 정보(`student_info_2`)입니다.
    *   `np.hstack([student_info_1, student_info_2])`: 각 학생의 정보를 가로로 합쳐 하나의 완전한 학생 프로필 테이블을 만들 수 있습니다. (예: `[이름, 학번, 전공, 학년, 반, 이메일]`)
    *   두 개의 엑셀 파일이 있다고 가정해 봅시다. 하나는 1반 학생들의 성적 데이터(`class1_grades`), 다른 하나는 2반 학생들의 성적 데이터(`class2_grades`)입니다.
    *   `np.vstack([class1_grades, class2_grades])`: 1반 학생들 데이터 아래에 2반 학생들 데이터를 붙여 전체 학년 학생들의 통합 성적표를 만들 수 있습니다. (예: `[[1반 학생1 성적], [1반 학생2 성적], [2반 학생1 성적], [2반 학생2 성적]]`)

**시험 포인트**
*   ⭐ `np.vstack`과 `np.hstack`이 1차원 배열을 처리하는 방식의 차이를 정확히 이해하고 있어야 합니다. (`vstack`은 1D를 2D로 승격하여 행으로 쌓고, `hstack`은 1D를 그대로 이어 붙여 더 긴 1D를 만듭니다.)
*   ⭐ `np.vstack`은 `np.concatenate(axis=0)`와, `np.hstack`은 `np.concatenate(axis=1)`와 각각 어떤 관계를 가지는지 설명할 수 있어야 합니다.
*   ⭐ 주어진 NumPy 배열에 대해 `vstack` 또는 `hstack` 연산을 수행했을 때, 결과 배열의 **`shape`**을 정확하게 예측하고 설명할 수 있어야 합니다.
*   ⭐ 특히, 2D 배열을 `vstack` 또는 `hstack` 할 때, 각 배열의 차원 수가 동일해야 함을 기억해야 합니다 (특히 스택하는 방향과 수직인 차원). 예를 들어, `vstack`은 열의 수가 같아야 하고, `hstack`은 행의 수가 같아야 합니다.

---
## Slide 61

데이터분석 입문 (CSED226) 강의 노트: Batched Matrix Multiplication (배치 행렬 곱)

---

### **핵심 개념**

배치 행렬 곱(Batched Matrix Multiplication)은 여러 개의 행렬 곱셈을 동시에 수행하는 연산입니다. NumPy의 `@` 연산자 또는 `np.matmul` 함수는 이 기능을 지원하며, 특히 딥러닝과 같이 대량의 데이터를 병렬 처리할 때 매우 유용합니다.

*   **2D 행렬의 경우**: 일반적인 행렬 곱셈과 동일합니다. 예를 들어, $(M, K)$ 형태의 행렬과 $(K, N)$ 형태의 행렬을 곱하면 $(M, N)$ 형태의 행렬이 됩니다.
*   **고차원 배열의 경우**:
    *   **마지막 두 축(last two axes)**: 실제 행렬 곱셈이 일어나는 행렬의 차원(행과 열)으로 간주됩니다.
    *   **선행 축(all leading axes)**: 독립적인 행렬 곱셈을 위한 "배치(batch)" 차원으로 간주됩니다. 즉, 각 배치 인덱스에 대해 독립적인 2D 행렬 곱셈이 수행됩니다.

### **코드/수식 해설**

**1. Shape Rule (형태 규칙)**

두 배열 $A$와 $B$가 주어졌을 때, 배치 행렬 곱의 형태 규칙은 다음과 같습니다.

$A \in \mathbb{R}^{\cdots \times M \times K}$
$B \in \mathbb{R}^{\cdots \times K \times N}$
$\implies Y = A @ B \in \mathbb{R}^{\text{broadcast}(\cdots) \times M \times N}$

*   여기서 $\cdots$는 하나 이상의 "선행 배치 축(leading batch axes)"을 나타냅니다.
*   $M, K, N$은 실제 행렬 곱셈의 차원입니다. $A$의 마지막 두 축은 $M \times K$이고, $B$의 마지막 두 축은 $K \times N$입니다.
*   결과 $Y$의 마지막 두 축은 $(M, N)$이 됩니다.
*   결과 $Y$의 선행 배치 축들은 $A$와 $B$의 선행 배치 축들에 NumPy의 **브로드캐스팅(broadcasting) 규칙**이 적용되어 결정됩니다. 즉, 선행 배치 축들은 크기가 같거나, 어느 한쪽이 1이어서 브로드캐스트될 수 있어야 합니다.

**2. Values (값 계산)**

각 배치 인덱스 $\beta$에 대한 결과 행렬 $Y[\beta]$의 $(i, n)$번째 원소는 다음과 같이 계산됩니다.

$$Y[\beta, i, n] = \sum_{j=0}^{K-1} A[\beta, i, j] B[\beta, j, n]$$

*   이 수식은 특정 배치 $\beta$에 속하는 행렬 $A[\beta]$ (크기 $M \times K$)와 행렬 $B[\beta]$ (크기 $K \times N$) 사이의 표준 행렬 곱셈을 정의합니다.
*   즉, 모든 배치에 대해 동일한 행렬 곱셈 연산이 병렬적으로 수행됨을 의미합니다.

### **구체적 예시**

```python
import numpy as np

# 예시 1: 3D 배열 (1개의 배치 차원)
# A: (batch_size, M, K) = (2, 3, 4)
# B: (batch_size, K, N) = (2, 4, 5)
A = np.random.rand(2, 3, 4)
B = np.random.rand(2, 4, 5)

print(f"A.shape: {A.shape}") # (2, 3, 4)
print(f"B.shape: {B.shape}") # (2, 4, 5)

# 배치 행렬 곱 수행
C = A @ B
print(f"C.shape: {C.shape}") # (2, 3, 5)

# 결과 확인: C[0]은 A[0] @ B[0]과 같고, C[1]은 A[1] @ B[1]과 같음
print(f"Are C[0] and A[0] @ B[0] close? {np.allclose(C[0], A[0] @ B[0])}")
print(f"Are C[1] and A[1] @ B[1] close? {np.allclose(C[1], A[1] @ B[1])}")

# 예시 2: 브로드캐스팅을 포함하는 배치 행렬 곱
# A: (batch_size_outer, batch_size_inner, M, K) = (1, 2, 3, 4)
# B: (batch_size_outer, batch_size_inner, K, N) = (5, 1, 4, 5)
# A의 선행 배치 축: (1, 2)
# B의 선행 배치 축: (5, 1)
# 브로드캐스팅 결과 선행 배치 축: (5, 2)

A_broadcast = np.random.rand(1, 2, 3, 4)
B_broadcast = np.random.rand(5, 1, 4, 5)

print(f"\nA_broadcast.shape: {A_broadcast.shape}") # (1, 2, 3, 4)
print(f"B_broadcast.shape: {B_broadcast.shape}") # (5, 1, 4, 5)

D = A_broadcast @ B_broadcast
print(f"D.shape: {D.shape}") # (5, 2, 3, 5)
```

**실생활 비유**:
여러 고객의 주문 내역을 동시에 처리하는 상황을 생각해봅시다. 각 고객의 주문은 독립적인 데이터셋(즉, 하나의 "배치")으로 간주할 수 있고, 각 주문 내역에 대해 품목 가격과 수량을 곱하여 총액을 계산하는 작업(행렬 곱셈과 유사)을 해야 합니다. 배치 행렬 곱은 이 모든 고객의 계산을 효율적으로 한 번에 처리하는 것과 같습니다.

### **시험 포인트**

*   **⭐ 배치 행렬 곱의 정의**: 고차원 배열에서 `np.matmul` 또는 `@` 연산자가 **마지막 두 축**을 행렬의 행/열로, **모든 선행 축**을 배치 차원으로 간주한다는 것을 정확히 이해해야 합니다.
*   **⭐ Shape Matching 및 Broadcasting 규칙**:
    *   행렬 곱셈이 일어나는 마지막 두 축($M \times K$ 와 $K \times N$)에서, $A$의 마지막 축 크기($K$)와 $B$의 뒤에서 두 번째 축 크기($K$)는 반드시 일치해야 합니다.
    *   선행 배치 축들은 NumPy의 **브로드캐스팅 규칙**에 따라 호환되어야 합니다 (크기가 같거나, 어느 한쪽이 1이어야 함).
*   **⭐ 결과 Shape 계산**: 입력 배열의 shape로부터 결과 배열의 shape를 정확히 예측할 수 있어야 합니다. (예: `(B1, B2, M, K)` @ `(B1_prime, B2_prime, K, N)` -> `(broadcasted B1, broadcasted B2, M, N)`).
*   **⭐ 수식의 의미**: 주어진 수학적 수식이 각 배치 인덱스에 대해 독립적인 표준 행렬 곱셈을 의미한다는 것을 파악해야 합니다. 이는 단순히 반복되는 루프가 아니라, 병렬 처리에 최적화된 연산임을 이해하는 것이 중요합니다.

---
## Slide 62

### 핵심 개념
이 슬라이드는 NumPy 라이브러리를 사용하여 다차원 배열(ndarrays)의 행렬 곱셈(matrix multiplication)과 브로드캐스팅(broadcasting) 개념을 다양한 shape 예시를 통해 설명합니다.

1.  **NumPy 배열 생성 및 형태 변경**: `np.arange()`로 1차원 배열을 생성하고 `.reshape()` 메서드를 통해 원하는 다차원 배열 형태로 변환합니다.
2.  **행렬 곱셈 (`@` 연산자)**: NumPy에서 `@` 연산자는 두 배열의 행렬 곱셈을 수행합니다. 이는 `np.matmul()` 함수와 동일합니다. 다차원 배열의 경우, 마지막 두 축에 대해 행렬 곱셈이 수행되고, 선행하는 축(batch dimensions)들은 동일하거나 브로드캐스팅 가능해야 합니다.
    *   일반적인 규칙: `(..., M, K) @ (..., K, N) -> (..., M, N)`
3.  **브로드캐스팅(Broadcasting) 적용**: 행렬 곱셈 시 두 배열의 차원(shape)이 완벽하게 일치하지 않더라도 특정 규칙에 따라 자동으로 확장되어 연산이 가능하게 하는 기능입니다. 이 슬라이드에서는 배치(batch) 차원에서 브로드캐스팅이 일어나는 예시를 보여줍니다.
    *   **Right Broadcasting**: `(B, M, K) @ (K, N)` 형태의 곱셈에서 `(K, N)` 배열이 `B` 차원으로 브로드캐스팅되어 `B`개의 `(M, K) @ (K, N)` 연산이 수행됩니다.
    *   **Left Broadcasting**: `(M, K) @ (B, K, N)` 형태의 곱셈에서 `(M, K)` 배열이 `B` 차원으로 브로드캐스팅되어 `B`개의 `(M, K) @ (K, N)` 연산이 수행됩니다.

### 코드/수식 해설

```python
import numpy as np

# 차원 변수 정의
B, M, K, N = 2, 2, 3, 4

# 1. 배치 행렬 곱셈 (Batch Matrix Multiplication)
# (B, M, K) @ (B, K, N) -> (B, M, N)
A = np.arange(B*M*K).reshape(B, M, K) # shape: (2, 2, 3)
C = np.arange(B*K*N).reshape(B, K, N) # shape: (2, 3, 4)
Y = A @ C # Y의 shape는 (2, 2, 4)
print(A.shape, C.shape, Y.shape) # 결과: (2, 2, 3) (2, 3, 4) (2, 2, 4)

# 2. Right Broadcasting 예시
# (B, M, K) @ (K, N) -> (B, M, N) (right broadcasts)
W = np.arange(K*N).reshape(K, N) # shape: (3, 4)
Y2 = A @ W # Y2의 shape는 (2, 2, 4)
print(Y2.shape) # 결과: (2, 2, 4)

# 3. Left Broadcasting 예시
# (M, K) @ (B, K, N) -> (B, M, N) (left broadcasts)
X = np.arange(M*K).reshape(M, K) # shape: (2, 3)
Y3 = X @ C # Y3의 shape는 (2, 2, 4)
print(Y3.shape) # 결과: (2, 2, 4)
```

**행렬 곱셈의 일반적인 차원 변환 규칙:**
주어진 두 행렬 $A$와 $B$가 있을 때, 행렬 곱 $C = A \cdot B$의 차원은 다음과 같이 결정됩니다.
만약 $A$의 차원이 $(d_1, d_2, ..., d_{m-2}, M, K)$이고 $B$의 차원이 $(d_1, d_2, ..., d_{m-2}, K, N)$이라면, 결과 $C$의 차원은 $(d_1, d_2, ..., d_{m-2}, M, N)$이 됩니다. 여기서 $(d_1, d_2, ..., d_{m-2})$는 배치(batch) 차원을 나타냅니다.

### 구체적 예시

*   **배치 행렬 곱셈 (`Y = A @ C`)**:
    *   `A`는 `(2, 2, 3)` 형태이고, `C`는 `(2, 3, 4)` 형태입니다. 여기서 첫 번째 `2`는 배치 차원입니다.
    *   NumPy는 `A[0]` (shape `(2, 3)`)과 `C[0]` (shape `(3, 4)`)을 곱하고, `A[1]` (shape `(2, 3)`)과 `C[1]` (shape `(3, 4)`)을 곱하여 두 결과를 합쳐 `(2, 2, 4)` 형태의 `Y`를 만듭니다. 즉, 동일한 배치 인덱스끼리 행렬 곱셈이 수행됩니다.

*   **Right Broadcasting (`Y2 = A @ W`)**:
    *   `A`는 `(2, 2, 3)` 형태이고, `W`는 `(3, 4)` 형태입니다.
    *   `W`는 `A`의 배치 차원 `2`에 맞춰 자동으로 `(2, 3, 4)` 형태로 확장된 후 연산이 수행되는 것처럼 동작합니다. 즉, `A[0] @ W`와 `A[1] @ W`가 각각 계산되어 결과적으로 `(2, 2, 4)` 형태의 `Y2`가 생성됩니다. 마치 `W`가 각 배치마다 복사되어 사용되는 것과 같습니다.

*   **Left Broadcasting (`Y3 = X @ C`)**:
    *   `X`는 `(2, 3)` 형태이고, `C`는 `(2, 3, 4)` 형태입니다.
    *   `X`는 `C`의 배치 차원 `2`에 맞춰 자동으로 `(2, 2, 3)` 형태로 확장된 후 연산이 수행되는 것처럼 동작합니다. 즉, `X @ C[0]`와 `X @ C[1]`가 각각 계산되어 결과적으로 `(2, 2, 4)` 형태의 `Y3`가 생성됩니다.

### 시험 포인트

*   ⭐ **NumPy의 `@` 연산자가 다차원 배열에 대해 어떻게 동작하는지 정확히 이해하고 있어야 합니다.** 이는 딥러닝 라이브러리(TensorFlow, PyTorch)에서도 유사한 방식으로 사용되므로 중요합니다.
*   **다차원 배열의 행렬 곱셈 시 최종 결과의 shape를 예측할 수 있어야 합니다.** 특히 배치(batch) 차원이 있는 경우 `(..., M, K) @ (..., K, N)`이 `(..., M, N)`이 된다는 규칙을 암기해두세요.
*   ⭐ **NumPy 브로드캐스팅의 개념과 행렬 곱셈 시 적용되는 방식(특히 배치 차원에서의 확장)을 설명하고 예시를 통해 증명할 수 있어야 합니다.** `(B, M, K) @ (K, N)` 또는 `(M, K) @ (B, K, N)`과 같이 차원이 다른 배열 간의 곱셈에서 어떤 배열이 어떻게 브로드캐스팅되는지 파악하는 것이 핵심입니다.
*   `np.arange()`와 `.reshape()`를 사용하여 원하는 형태의 배열을 생성하는 기본적인 문법은 숙지해야 합니다.

---
## Slide 63

**핵심 개념**:
*   **NumPy 배열 연결 (`np.vstack`, `np.hstack`)**: 여러 NumPy 배열을 특정 축(axis)을 따라 연결하여 하나의 큰 배열을 생성하는 기능입니다.
*   **`np.vstack` (Vertical Stack)**: 배열들을 수직으로 쌓아 올리듯이 연결합니다. 이는 첫 번째 축(`axis=0`)을 따라 배열의 행(row)을 추가하는 방식으로 동작합니다. 연결하려는 배열들의 `axis=0`을 제외한 나머지 차원들은 모두 동일해야 합니다.
*   **`np.hstack` (Horizontal Stack)**: 배열들을 수평으로 나열하듯이 연결합니다. 이는 두 번째 축(`axis=1`)을 따라 배열의 열(column)을 추가하는 방식으로 동작합니다. 연결하려는 배열들의 `axis=1`을 제외한 나머지 차원들은 모두 동일해야 합니다.
*   **차원 일치 규칙과 예외**:
    *   `np.vstack`은 1차원 배열을 2차원 배열(행 벡터, `(1, N)`)로 자동 변환하여 다른 2차원 배열과 연결할 수 있는 유연성을 가집니다.
    *   `np.hstack`은 연결하려는 배열들의 차원 수가 서로 다르면 오류를 발생시킵니다 (예: 1차원과 2차원 배열 혼합 불가).

**코드/수식 해설**:

1.  **`np.vstack`을 이용한 3차원 배열 연결 (axis=0 확장)**
    ```python
    import numpy as np

    # Higher dims: vstack grows axis 0
    C = np.zeros((3, 2, 2)) # Shape (3, 2, 2)
    D = np.ones((4, 2, 2))  # Shape (4, 2, 2)
    V3 = np.vstack([C, D])
    print("V3 shape:", V3.shape) # Output: V3 shape: (7, 2, 2)
    ```
    *   `C`와 `D`는 각각 `(3, 2, 2)`와 `(4, 2, 2)` 형태의 3차원 배열입니다. `axis=0`을 제외한 나머지 차원 `(2, 2)`가 동일합니다.
    *   `np.vstack([C, D])`는 `axis=0`을 따라 배열을 연결하여, 결과 `V3`의 `axis=0`은 `3+4=7`이 되고, 나머지 차원은 유지되어 `(7, 2, 2)` 형태가 됩니다.

2.  **`np.hstack`을 이용한 3차원 배열 연결 (axis=1 확장)**
    ```python
    # Higher dims: hstack grows axis 1
    E = np.zeros((5, 1, 2)) # Shape (5, 1, 2)
    F = np.ones((5, 3, 2))  # Shape (5, 3, 2)
    H3 = np.hstack([E, F])
    print("H3 shape:", H3.shape) # Output: H3 shape: (5, 4, 2)
    ```
    *   `E`와 `F`는 각각 `(5, 1, 2)`와 `(5, 3, 2)` 형태의 3차원 배열입니다. `axis=1`을 제외한 나머지 차원 `(5, 2)`가 동일합니다.
    *   `np.hstack([E, F])`는 `axis=1`을 따라 배열을 연결하여, 결과 `H3`의 `axis=1`은 `1+3=4`이 되고, 나머지 차원은 유지되어 `(5, 4, 2)` 형태가 됩니다.

3.  **`np.vstack`의 1차원-2차원 배열 혼합 처리**
    ```python
    # vstack allows 1D with 2D (1D promoted to row)
    V_mix = np.vstack([np.array([1, 2, 3]), np.array([[4, 5, 6]])])
    print("V_mix shape:", V_mix.shape) # Output: V_mix shape: (2, 3)
    ```
    *   `np.array([1, 2, 3])`는 형태 `(3,)`인 1차원 배열입니다.
    *   `np.array([[4, 5, 6]])`는 형태 `(1, 3)`인 2차원 배열입니다.
    *   `np.vstack`은 1차원 배열 `[1, 2, 3]`을 2차원 행 벡터 `[[1, 2, 3]]` (형태 `(1, 3)`)로 자동 승격시킨 후, 형태 `(1, 3)`의 배열과 연결합니다.
    *   결과 `V_mix`의 형태는 `(1+1, 3)` 즉, `(2, 3)`이 됩니다.

4.  **`np.hstack`의 1차원-2차원 배열 혼합 오류**
    ```python
    # hstack mixing 1D and 2D is not allowed
    try:
        np.hstack([np.array([1, 2, 3]), np.array([[4, 5, 6]])])
    except Exception as e:
        print("hstack mix error:", type(e).__name__) # Output: hstack mix error: ValueError
    ```
    *   `np.array([1, 2, 3])`는 1차원 배열이고, `np.array([[4, 5, 6]])`는 2차원 배열입니다.
    *   `np.hstack`은 차원이 다른 배열(특히 1D와 2D)을 직접 연결하는 것을 허용하지 않으므로 `ValueError`를 발생시킵니다. 이는 `hstack`이 `axis=1`을 기준으로 연결하는데 1차원 배열은 이 축이 명확하게 정의되어 있지 않기 때문입니다.

**구체적 예시**:
*   **데이터 테이블 합치기 비유**:
    *   **`vstack`**: 여러 개의 설문조사 응답 테이블이 있는데, 각 테이블은 동일한 질문(열)과 다른 사람들의 응답(행)을 담고 있다고 가정해 봅시다. `vstack`은 이 응답 테이블들을 수직으로 쌓아 올려, 모든 응답자의 데이터를 포함하는 하나의 큰 설문조사 데이터셋을 만듭니다. (질문 수는 같고, 응답자 수가 늘어남)
    *   **`hstack`**: 특정 사람들의 기본 인적 사항(이름, 학번, 성별 등)을 담은 테이블과, 동일한 사람들의 성적 데이터(과목A, 과목B 점수 등)를 담은 다른 테이블이 있다고 가정해 봅시다. `hstack`은 이 두 테이블을 수평으로 나란히 연결하여, 각 사람에 대한 모든 정보를 담는 포괄적인 테이블을 만듭니다. (사람 수는 같고, 정보의 종류(열)가 늘어남)

**시험 포인트**:
*   ⭐ `np.vstack`은 `axis=0`을, `np.hstack`은 `axis=1`을 기준으로 배열을 연결한다는 점을 정확히 이해해야 합니다.
*   ⭐ `np.vstack`과 `np.hstack` 모두 연결하려는 배열들의 다른 축(연결하는 축이 아닌)의 크기는 반드시 일치해야 합니다. 불일치 시 오류가 발생합니다.
*   ⭐ `np.vstack`은 1차원 배열을 2차원 행 벡터로 자동 변환하여 2차원 배열과 연결할 수 있는 반면, `np.hstack`은 1차원과 2차원 배열의 직접적인 혼합 연결을 허용하지 않고 `ValueError`를 발생시킨다는 핵심적인 차이점을 숙지해야 합니다.
*   ⭐ 주어진 배열들의 `shape`을 보고 `vstack` 또는 `hstack` 연산 후의 결과 `shape`을 정확히 예측할 수 있어야 합니다.

---
## Slide 64

## NumPy 배열 생성 및 속성 확인

### 핵심 개념
NumPy(Numerical Python)는 파이썬에서 고성능 과학 계산을 위한 핵심 라이브러리입니다. 특히 다차원 배열(nd-array) 객체를 효율적으로 다룰 수 있도록 지원하며, 벡터화된 연산을 통해 빠른 데이터 처리가 가능합니다. 이 슬라이드는 NumPy 배열을 생성하는 다양한 방법과 생성된 배열의 주요 속성을 확인하는 방법을 소개합니다.

주요 배열 생성 함수:
*   `np.array()`: 파이썬 리스트나 튜플로부터 배열을 생성합니다. 데이터 타입을 명시적으로 지정할 수 있습니다.
*   `np.arange()`: 특정 범위의 정수 값을 갖는 1차원 배열을 생성합니다. (Python의 `range()`와 유사)
*   `np.linspace()`: 지정된 시작 값과 끝 값 사이를 균일한 간격으로 나눈 `num`개의 값으로 구성된 배열을 생성합니다.

주요 배열 속성:
*   `.shape`: 배열의 각 차원(dimension) 크기를 나타내는 튜플입니다.
*   `.dtype`: 배열 요소들의 데이터 타입입니다.
*   `.ndim`: 배열의 차원 수입니다.
*   `.size`: 배열 내의 총 요소 개수입니다.
*   `.T`: 배열의 전치(transpose)를 반환합니다. 2차원 배열의 경우 행과 열이 바뀝니다.

### 코드/수식 해설

```python
import numpy as np

# 1. np.array(): 파이썬 리스트로부터 1차원 배열 생성
# dtype=np.int32로 데이터 타입을 명시적으로 32비트 정수로 지정합니다.
a = np.array([1, 2, 3], dtype=np.int32)

# 2. np.arange(): 0부터 5까지 (6 미만)의 정수를 갖는 1차원 배열을 생성한 후,
# .reshape(2, 3)을 사용하여 2행 3열의 2차원 배열로 변환합니다.
b = np.arange(6).reshape(2, 3)

# 3. np.linspace(): 0.0부터 1.0까지의 범위에서 5개의 숫자를 균등한 간격으로 생성합니다.
c = np.linspace(0.0, 1.0, num=5)

# 배열 a의 shape (형태), dtype (데이터 타입), ndim (차원 수)를 출력합니다.
print(a.shape, a.dtype, a.ndim)

# 배열 b의 shape, size (총 요소 수), b.T (전치된 배열)의 shape를 출력합니다.
print(b.shape, b.size, b.T.shape)

# 배열 c의 내용을 출력합니다.
print(c)
```

`np.linspace(start, stop, num)` 함수는 다음과 같이 균등한 간격을 계산합니다:
$$ \text{step} = \frac{\text{stop} - \text{start}}{\text{num} - 1} $$
생성되는 $i$-번째 값은 $\text{start} + i \times \text{step}$ ($0 \le i < \text{num}$)입니다.

### 구체적 예시
위 코드를 실행했을 때의 출력 결과는 다음과 같습니다.

```
(3,) int32 1
(2, 3) 6 (3, 2)
[0.   0.25 0.5  0.75 1.  ]
```

*   `a`: `[1 2 3]`
    *   `(3,)`: 1차원 배열이며 요소가 3개입니다.
    *   `int32`: 각 요소는 32비트 정수입니다.
    *   `1`: 1차원 배열입니다.
*   `b`:
    ```
    [[0 1 2]
     [3 4 5]]
    ```
    *   `(2, 3)`: 2행 3열의 2차원 배열입니다.
    *   `6`: 총 요소가 6개입니다 (2 * 3).
    *   `(3, 2)`: `b`를 전치하면 3행 2열의 배열이 됩니다.
        ```
        [[0 3]
         [1 4]
         [2 5]]
        ```
*   `c`: `[0.   0.25 0.5  0.75 1.  ]`
    *   0.0부터 1.0까지 5개의 숫자가 균등하게 분포되어 있습니다. (간격: (1.0-0.0)/(5-1) = 0.25)

실생활 비유:
*   `np.array()`는 특정 데이터를 직접 입력하여 목록(예: 학생들의 시험 점수)을 만드는 것과 같습니다.
*   `np.arange()`는 0부터 시작하는 일련의 번호(예: 1번부터 10번까지의 학생)를 빠르게 생성하는 것과 비슷합니다.
*   `np.linspace()`는 특정 범위(예: 0분부터 60분까지)를 정해진 간격(예: 15분 간격)으로 나누어 표본 지점들을(0분, 15분, 30분, 45분, 60분) 만드는 것과 같습니다.

### 시험 포인트
*   ⭐**`np.array()`, `np.arange()`, `np.linspace()` 각 함수의 역할과 차이점, 그리고 어떤 상황에 적합한지 명확히 이해해야 합니다.**
    *   `np.array()`: 기존 파이썬 시퀀스로부터 배열 생성 (주로 고정된 데이터).
    *   `np.arange()`: 특정 범위의 연속된 정수 배열 생성 (주로 인덱스, 시퀀스 데이터).
    *   `np.linspace()`: 특정 범위 내에서 균등한 간격의 실수 배열 생성 (주로 샘플링, 그래프 축).
*   ⭐**`.shape`, `.dtype`, `.ndim`, `.size`, `.T` 와 같은 NumPy 배열의 핵심 속성들이 무엇을 나타내는지 정확히 알아야 합니다.** 주어진 배열에 대해 각 속성 값을 예측할 수 있어야 합니다.
*   ⭐`reshape()` 메서드를 통해 배열의 차원을 변경하는 방법과 이것이 데이터에 어떻게 영향을 미치는지 이해하는 것이 중요합니다.
*   `dtype`을 명시적으로 지정하는 이유 (메모리 효율성, 연산 정확성)를 알고 있으면 좋습니다. 예를 들어, 큰 정수 배열을 다룰 때 `np.int64` 대신 `np.int32`를 사용하면 메모리를 절약할 수 있습니다.

---
## Slide 65

### 핵심 개념
*   **NumPy DType 추론 및 Upcasting**: NumPy는 배열을 생성할 때 제공된 데이터로부터 가장 적절한 데이터 타입(dtype)을 자동으로 추론합니다. 여러 가지 파이썬 타입이 혼합되어 있을 경우, 데이터 손실을 최소화하기 위해 더 넓은 범위의 공통 dtype으로 **upcast**됩니다. 예를 들어, 정수(integer)와 부동소수점(float)이 혼합된 경우, 모든 요소를 표현할 수 있는 부동소수점 타입으로 자동 변환됩니다.
*   **문자열의 영향**: 숫자형 데이터를 포함해야 할 배열에 문자열이 하나라도 포함되면, NumPy는 해당 배열의 dtype을 더 이상 숫자형으로 유지하지 못하고 `object` 또는 `string` 타입으로 강제 변환합니다. 이는 산술 연산이 불가능해지는 등의 예기치 않은 동작을 유발할 수 있습니다.
*   **명시적 DType 지정**: 이러한 자동 추론으로 인한 '예상치 못한' 동작을 방지하기 위해, 배열 생성 시 `dtype` 인자를 사용하여 원하는 데이터 타입을 명시적으로 지정하는 것이 권장됩니다.
*   **명시적 타입 변환(Casting)**: 이미 생성된 배열의 데이터 타입을 변경해야 할 경우, `astype()` 메서드를 사용하여 명시적으로 변환할 수 있습니다. 이 과정에서 데이터 손실이 발생할 수도 있음을 인지해야 합니다 (예: 부동소수점 수를 정수로 변환 시 소수점 이하 버림).

### 코드/수식 해설
*   **배열 생성 시 `dtype` 지정**:
    ```python
    import numpy as np

    arr_float = np.array([1, 2, 3], dtype=np.float64) # 정수 리스트를 float64 타입으로 생성
    arr_int = np.array([1.5, 2.3, 3.9], dtype=np.int32) # float 리스트를 int32 타입으로 생성 (소수점 버림)
    ```
*   **`astype()`을 사용한 타입 변환**:
    ```python
    arr = np.array([1.1, 2.5, 3.8])
    print(arr.dtype) # float64

    arr_int_converted = arr.astype(np.int32) # float64를 int32로 변환
    print(arr_int_converted.dtype) # int32
    print(arr_int_converted) # [1 2 3] (소수점 버림 확인)

    arr_str_converted = arr.astype(str) # float64를 문자열로 변환
    print(arr_str_converted.dtype) # <U32 (유니코드 문자열)
    print(arr_str_converted) # ['1.1' '2.5' '3.8']
    ```

### 구체적 예시
1.  **자동 Upcasting 예시**:
    ```python
    import numpy as np

    arr1 = np.array([1, 2, 3]) # 모든 요소가 정수
    print(arr1.dtype) # int64 (시스템 환경에 따라 int32일 수도 있음)

    arr2 = np.array([1, 2.0, 3]) # 정수와 부동소수점 혼합
    print(arr2.dtype) # float64 (모든 요소를 float으로 upcast)

    arr3 = np.array([1, 2.0, '3']) # 정수, 부동소수점, 문자열 혼합
    print(arr3.dtype) # <U21 (유니코드 문자열 또는 object)
    print(arr3) # ['1' '2.0' '3'] (모든 요소가 문자열로 변환)
    ```
    *   `arr2`의 경우, `1`과 `3`은 정수이지만 `2.0`이 부동소수점이기 때문에 NumPy는 모든 요소를 `float64`로 upcast하여 데이터의 정확성을 유지합니다.
    *   `arr3`의 경우, 숫자와 문자열이 섞여 있으므로 NumPy는 가장 일반적인 타입인 `string` 또는 `object`로 변환하며, 이 경우 배열 내 값들은 더 이상 숫자로서의 특성을 잃습니다.

2.  **명시적 `dtype` 지정 및 `astype()` 사용 예시**:
    ```python
    import numpy as np

    # 1. 배열 생성 시 명시적 dtype 지정
    arr_explicit_float = np.array([1, 2, 3], dtype=np.float32)
    print(arr_explicit_float.dtype) # float32
    print(arr_explicit_float) # [1. 2. 3.]

    # 2. 문자열이 섞이는 것을 방지하기 위해 dtype 지정 (오류 발생 가능성 인지)
    # arr_mixed_int = np.array([1, 2, 'three'], dtype=np.int32) # ValueError 발생
    # print(arr_mixed_int)
    # => 'three'는 정수로 변환될 수 없으므로 ValueError가 발생합니다.
    #    이는 의도치 않은 문자열 혼입을 초기에 발견하는 데 도움이 됩니다.

    # 3. astype()을 이용한 타입 변환 (float -> int 시 데이터 손실)
    arr_data = np.array([1.9, 2.1, 3.7])
    arr_int_cast = arr_data.astype(np.int32)
    print(arr_int_cast.dtype) # int32
    print(arr_int_cast) # [1 2 3] (소수점 이하가 버려졌음을 확인)
    ```

### 시험 포인트
*   ⭐**NumPy의 자동 DType Upcasting 규칙을 이해하고 예시를 들 수 있어야 합니다.** 특히 `int`와 `float`이 섞였을 때 `float`으로 upcast 되는 경우를 기억하세요.
*   ⭐**배열에 숫자형이 아닌 문자열이 포함될 경우 NumPy 배열의 DType이 어떻게 변하는지 (object 또는 string) 설명할 수 있어야 합니다.** 이로 인해 발생하는 문제점(산술 연산 불가 등)도 함께 설명할 수 있어야 합니다.
*   ⭐**예기치 않은 DType 추론을 방지하기 위해 배열 생성 시 `dtype` 인자를 사용하는 방법을 알아야 합니다.**
*   ⭐**이미 생성된 NumPy 배열의 데이터 타입을 명시적으로 변환하기 위해 `astype()` 메서드를 사용하는 방법을 알아야 합니다.**
*   ⭐**`astype()`을 사용하여 DType을 변환할 때, 특히 float을 int로 변환하는 경우와 같이 타입의 범위가 좁아지는 경우 데이터 손실(예: 소수점 이하 버림)이 발생할 수 있음을 인지하고 설명할 수 있어야 합니다.**

---
## Slide 66

**핵심 개념**

*   **NumPy 데이터 타입 (dtype)**: NumPy 배열은 단일 데이터 타입(homogeneous)을 가집니다. 이는 메모리 효율성과 빠른 연산을 가능하게 하는 핵심적인 특징입니다. 각 요소는 `int32`, `float64`, `bool`, `object` 등 특정 데이터 타입을 따릅니다.
*   **자동 타입 추론 (Upcasting)**: `np.array()`로 배열을 생성할 때, NumPy는 입력된 데이터의 모든 요소를 담을 수 있는 가장 일반적인(general) 데이터 타입으로 자동으로 "업캐스팅(upcast)"합니다. 예를 들어, 정수와 실수가 섞여 있으면 모든 요소를 실수(float) 타입으로 만듭니다.
*   **`object` dtype의 문제점**: 배열 내에 숫자와 문자열 등 호환되지 않는 여러 종류의 데이터가 섞여 있으면, NumPy는 이를 `object` 타입으로 추론합니다. `object` 타입 배열은 파이썬 리스트와 유사하게 동작하여, 각 요소가 실제 파이썬 객체에 대한 참조를 저장합니다. 이는 메모리 사용량을 늘리고, 특히 수치 연산 시 성능 저하를 초래하며, 예상치 못한 오류를 발생시킬 수 있습니다. 수학적 연산에는 `object` 타입을 피해야 합니다.
*   **명시적 dtype 지정**: 배열 생성 시 `dtype` 매개변수를 사용하여 원하는 데이터 타입을 명시적으로 지정할 수 있습니다. 예를 들어, `dtype=np.float64`는 모든 요소를 64비트 실수로 만듭니다.
*   **dtype 변경 (`.astype()`)**: 이미 생성된 배열의 데이터 타입을 변경하려면 `.astype()` 메서드를 사용합니다. 이 메서드는 지정된 새 데이터 타입으로 변환된 새 배열을 반환합니다. 이 과정에서 데이터 손실(예: float에서 int로 변경 시 소수점 이하 버림)이 발생할 수 있으므로 주의해야 합니다.

**코드/수식 해설**

```python
import numpy as np

# 1. 정수와 실수 혼합: 실수(float)로 자동 업캐스팅
x = np.array([1, 2.5, 3]) # float dtype due to upcast

# 2. 정수와 문자열 혼합: object dtype으로 추론 (수학 연산에 부적합)
y = np.array([1, "2", 3]) # string/object dtype; avoid for math

# 3. 명시적으로 dtype 지정: 모든 요소를 float64로 강제 지정
z = np.array([1, 2, 3], dtype=np.float64)

# 각 배열의 데이터 타입 출력
print(x.dtype, y.dtype, z.dtype)

# z 배열의 데이터 타입을 int64로 변경하여 출력
print(z.astype(np.int64))
```

*   `x = np.array([1, 2.5, 3])`: `1`과 `3`은 정수지만 `2.5`가 실수이므로, NumPy는 모든 요소를 64비트 부동소수점(`float64`)으로 변환합니다. `x.dtype`은 `float64`가 됩니다.
*   `y = np.array([1, "2", 3])`: `1`과 `3`은 정수지만 `"2"`가 문자열이므로, NumPy는 모든 요소를 파이썬 객체(`object`)로 저장합니다. `y.dtype`은 `object`가 됩니다. 이런 배열에 사칙연산 등을 시도하면 에러가 발생하거나 예상치 못한 결과가 나올 수 있습니다.
*   `z = np.array([1, 2, 3], dtype=np.float64)`: 초기 데이터는 정수이지만, `dtype=np.float64`를 통해 명시적으로 `float64` 타입을 지정했으므로, 배열 `z`는 `[1., 2., 3.]`과 같이 실수형으로 저장됩니다. `z.dtype`은 `float64`가 됩니다.
*   `print(x.dtype, y.dtype, z.dtype)`: 이 줄을 실행하면 `float64 object float64`와 같은 출력을 볼 수 있습니다 (정확한 `object` 타입명은 환경에 따라 달라질 수 있음).
*   `print(z.astype(np.int64))`: `z`는 `[1., 2., 3.]`이므로, `.astype(np.int64)`를 적용하면 소수점 이하가 버려지고 `[1 2 3]` 형태의 64비트 정수 배열이 됩니다.

**구체적 예시**

*   **자동 타입 추론 예시**: `np.array([1, 2, 3])`은 `int64` (또는 `int32`)로 추론되지만, `np.array([1, 2, 3.0])`은 `float64`로 추론됩니다. 이는 모든 요소를 손실 없이 표현할 수 있는 가장 넓은 범위를 선택하는 것입니다.
*   **`object` dtype의 위험성**:
    ```python
    import numpy as np
    arr_obj = np.array([1, "hello", 3])
    # arr_obj * 2  # 이 연산은 TypeError를 발생시킵니다.
    # 하지만 arr_obj[1] * 2 는 "hellohello"를 반환합니다.
    # 이는 문자열 "hello"에 대한 파이썬 기본 연산이 적용되기 때문입니다.
    # NumPy의 벡터화된 수치 연산을 기대할 수 없습니다.
    ```
*   **`.astype()` 예시**:
    ```python
    a = np.array([1.9, 2.1, 3.5])
    print(a.astype(int)) # 출력: [1 2 3] (소수점 이하 버림)

    b = np.array([0, 1, 0], dtype=bool)
    print(b) # 출력: [False  True False]
    print(b.astype(int)) # 출력: [0 1 0]
    ```

**시험 포인트**

*   ⭐ **NumPy 배열이 homogeneous(동질적) 데이터 타입을 가지는 이유와 장점**을 설명할 수 있어야 합니다. (메모리 효율성, 빠른 연산)
*   ⭐ **자동 타입 추론(upcasting)의 원리**를 이해하고, 어떤 경우에 `float`나 `object` 타입으로 업캐스팅되는지 구체적인 예시를 들어 설명할 수 있어야 합니다.
*   ⭐ **`object` dtype 배열이 왜 수치 연산에 부적합한지** 그 이유(성능 저하, 예상치 못한 결과, 에러 발생 가능성)를 설명할 수 있어야 합니다.
*   ⭐ **`np.array()` 생성 시 `dtype` 매개변수를 사용하는 방법**과 **`.astype()` 메서드를 이용해 데이터 타입을 변경하는 방법**을 정확히 알고 적용할 수 있어야 합니다.
*   ⭐ `astype()` 사용 시 **데이터 손실(예: float에서 int로 변환 시)이 발생할 수 있음**을 인지하고 있어야 합니다.

---
## Slide 67

다음은 "Indexing and Slicing" 슬라이드에 대한 마크다운 노트입니다.

---

### **핵심 개념**

*   **뷰 (View)**: NumPy 배열에서 **기본 슬라이싱(Basic Slicing)**(`arr[start:end]`, `arr[:, col]`)을 수행할 때 반환되는 객체입니다. 뷰는 원본 배열의 메모리 공간을 직접 참조하며 공유합니다. 따라서 뷰를 수정하면 원본 배열의 해당 부분도 함께 수정됩니다. 메모리 효율성이 높지만, 의도치 않은 원본 데이터 변경에 주의해야 합니다.
*   **복사본 (Copy)**: NumPy 배열에서 **정수 배열 인덱싱(Integer Array Indexing)**(`arr[[idx1, idx2]]`) 또는 **불리언 배열 인덱싱(Boolean Array Indexing)**(`arr[arr > value]`)을 수행할 때 반환되는 객체입니다. 복사본은 원본 배열의 데이터와는 독립적인 새로운 메모리 공간에 데이터를 저장합니다. 따라서 복사본을 수정해도 원본 배열은 변경되지 않습니다.
*   **메모리 동작 방식의 중요성**: 특히 대규모 데이터 처리나 성능에 민감한 코드를 작성할 때는 뷰와 복사본의 차이를 명확히 이해해야 합니다. 불필요한 복사본 생성은 메모리 사용량을 늘리고 연산 시간을 지연시킬 수 있습니다.

### **코드/수식 해설**

1.  **기본 슬라이싱 (Basic Slicing) - 뷰 예시**:
    ```python
    import numpy as np

    arr = np.arange(10)
    print("원본 배열:", arr) # [0 1 2 3 4 5 6 7 8 9]

    # 기본 슬라이싱은 뷰를 반환합니다.
    s = arr[2:5]
    print("슬라이스 (뷰):", s)     # [2 3 4]
    # 'base' 속성으로 원본 배열을 참조하는지 확인할 수 있습니다.
    print("뷰가 원본 메모리를 공유하는가?", s.base is arr) # True

    # 뷰를 수정하면 원본 배열도 함께 수정됩니다.
    s[0] = 99
    print("수정된 슬라이스:", s)    # [99 3 4]
    print("슬라이스 수정 후 원본 배열:", arr) # [ 0  1 99  3  4  5  6  7  8  9]
    ```

2.  **정수 배열 인덱싱 (Integer Array Indexing) - 복사본 예시**:
    ```python
    import numpy as np

    arr = np.arange(10)
    print("원본 배열:", arr) # [0 1 2 3 4 5 6 7 8 9]

    # 정수 배열 인덱싱은 복사본을 반환합니다.
    idx = np.array([0, 2, 4])
    c_int = arr[idx]
    print("인덱싱된 배열 (복사본):", c_int) # [0 2 4]
    print("인덱싱된 배열이 원본 메모리를 공유하는가?", c_int.base is arr) # False (또는 None)

    # 복사본을 수정해도 원본 배열은 수정되지 않습니다.
    c_int[0] = 100
    print("수정된 인덱싱된 배열:", c_int) # [100   2   4]
    print("인덱싱된 배열 수정 후 원본 배열:", arr) # [0 1 2 3 4 5 6 7 8 9]
    ```

3.  **불리언 배열 인덱싱 (Boolean Array Indexing) - 복사본 예시**:
    ```python
    import numpy as np

    arr = np.arange(10)
    print("원본 배열:", arr) # [0 1 2 3 4 5 6 7 8 9]

    # 불리언 배열 인덱싱은 복사본을 반환합니다.
    mask = arr % 2 == 0 # 짝수만 선택하는 마스크
    c_bool = arr[mask]
    print("마스킹된 배열 (복사본):", c_bool) # [0 2 4 6 8]
    print("마스킹된 배열이 원본 메모리를 공유하는가?", c_bool.base is arr) # False (또는 None)

    # 복사본을 수정해도 원본 배열은 수정되지 않습니다.
    c_bool[0] = 200
    print("수정된 마스킹된 배열:", c_bool) # [200   2   4   6   8]
    print("마스킹된 배열 수정 후 원본 배열:", arr) # [0 1 2 3 4 5 6 7 8 9]
    ```

### **구체적 예시**

NumPy 배열을 회사에서 관리하는 '원본 데이터베이스'라고 상상해 봅시다.

*   **뷰 (View) - 공동 작업 문서**: 팀원에게 데이터베이스의 특정 범위(예: 1월부터 3월까지의 판매 기록)를 보여주기 위해 '공동 작업 문서'를 공유하는 것과 같습니다. 이 문서는 원본 데이터베이스의 해당 부분을 직접 보여주는 '창'이며, 팀원이 이 문서에 데이터를 입력하거나 수정하면 **원본 데이터베이스에도 즉시 반영**됩니다. 모든 팀원이 항상 최신 데이터를 보고 공동으로 수정할 수 있다는 장점이 있지만, 한 명의 실수가 전체 데이터에 영향을 미칠 수 있습니다.

*   **복사본 (Copy) - 개인 작업용 사본**: 특정 분석을 위해 데이터베이스에서 특정 조건(예: 특정 제품의 판매 기록만)에 해당하는 데이터를 '개인 작업용 사본'으로 다운로드받는 것과 같습니다. 이 사본은 원본과 완전히 독립적이며, 개인 작업용 사본에서 어떤 분석을 하거나 데이터를 수정하더라도 **원본 데이터베이스는 전혀 영향을 받지 않습니다.** 안전하게 실험하고 테스트할 수 있지만, 사본을 만드는 데 시간과 저장 공간이 필요하며, 사본은 원본 데이터의 최신 상태를 반영하지 않을 수 있습니다.

### **시험 포인트**

*   ⭐ **NumPy 인덱싱/슬라이싱의 '뷰'와 '복사본' 개념을 정확히 이해하고 각각의 특징, 생성 조건, 그리고 원본 데이터에 미치는 영향을 설명할 수 있어야 합니다.**
*   ⭐ **기본 슬라이싱이 뷰를 반환하여 원본을 수정할 수 있다는 점, 그리고 정수/불리언 배열 인덱싱이 복사본을 반환하여 원본이 유지된다는 점을 명확히 구분해야 합니다.**
*   ⭐ **`ndarray.base` 속성을 사용하여 배열이 뷰인지 복사본인지 확인하는 방법을 알고 있어야 합니다.** (뷰인 경우 `base`가 원본 배열을 참조하고, 복사본인 경우 `None` 또는 다른 객체를 참조합니다.)
*   ⭐ **성능 최적화 관점에서 불필요한 복사본 생성을 피하는 방법(예: 뷰 활용, 필요한 경우 `arr.copy()` 명시적 사용)을 고려할 수 있어야 합니다.** 이는 메모리 사용량과 실행 시간에 직접적인 영향을 미치기 때문입니다.

---
## Slide 68

## Elementwise Ops and Reductions

### 핵심 개념

*   **요소별 연산 (Elementwise Operations)**: 배열의 각 요소에 대해 독립적으로 수행되는 연산입니다. 스칼라 값과 배열 간의 연산, 또는 두 배열 간의 연산 시 같은 위치의 요소끼리 연산됩니다. NumPy는 C/Fortran으로 구현된 내부 루틴을 통해 이러한 연산을 매우 효율적으로 처리합니다 (벡터화). 슬라이드에 제시된 `+`, `-`, `*`, `/` 같은 기본 산술 연산자와 `np.multiply`, `np.sqrt`, `np.exp`, `np.log`와 같은 유니버설 함수(ufuncs)가 여기에 해당합니다.

*   **축소 연산 (Reductions / Aggregation Operations)**: 배열 내의 여러 요소를 단일 값(스칼라) 또는 더 낮은 차원의 배열로 줄이는 연산입니다. `sum`, `prod`, `min`, `max`, `argmin`, `argmax`, `mean`, `std`, `var` 등이 대표적인 축소 연산입니다. 이 연산들은 `axis` (축) 매개변수를 사용하여 어느 차원을 따라 연산을 수행할지 지정할 수 있습니다.
    *   `axis=None` (기본값): 전체 배열의 모든 요소를 대상으로 연산을 수행하여 스칼라 값을 반환합니다.
    *   `axis=0`: 각 열(column)을 따라 연산을 수행합니다. 즉, 각 열의 모든 행을 집계하여 행의 차원을 줄입니다. 결과는 1차원 배열(또는 `keepdims=True`인 경우 2차원 배열)이 됩니다.
    *   `axis=1`: 각 행(row)을 따라 연산을 수행합니다. 즉, 각 행의 모든 열을 집계하여 열의 차원을 줄입니다. 결과는 1차원 배열(또는 `keepdims=True`인 경우 2차원 배열)이 됩니다.

*   **형태 (Shape)의 중요성**: 축소 연산의 결과 형태는 `axis` 매개변수와 `keepdims` 매개변수에 따라 달라집니다. 또한, 크기가 다른 배열 간에 연산이 가능하도록 배열을 확장하는 NumPy의 **브로드캐스팅(Broadcasting)** 기능에서 배열의 형태 정렬(alignment)은 핵심적인 역할을 합니다. 연산하려는 두 배열의 형태가 브로드캐스팅 규칙에 맞지 않으면 오류가 발생합니다.

### 코드/수식 해설

**1. 요소별 연산 (Elementwise Operations)**

```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
scalar = 10

# 기본 산술 연산 (Elementwise)
print(f"arr1 + arr2: {arr1 + arr2}") # [5 7 9]
print(f"arr1 * scalar: {arr1 * scalar}") # [10 20 30]

# 유니버설 함수 (ufuncs)
arr_data = np.array([1, 4, 9])
print(f"np.sqrt(arr_data): {np.sqrt(arr_data)}") # [1. 2. 3.]

arr_exp_log = np.array([0, 1, 2])
print(f"np.exp(arr_exp_log): {np.exp(arr_exp_log)}") # [ 1.         2.71828183 7.3890561 ] (e^0, e^1, e^2)
print(f"np.log(np.exp(arr_exp_log)): {np.log(np.exp(arr_exp_log))}") # [0. 1. 2.]
```

**2. 축소 연산 (Reductions with axis)**

축소 연산은 배열의 차원을 줄이거나 스칼라 값을 얻는 데 사용됩니다. `axis`를 지정하여 특정 축을 따라 연산합니다.

```python
import numpy as np

# 2차원 배열 예시
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("Matrix:\n", matrix)

# 전체 배열에 대한 연산 (axis=None 또는 생략)
print(f"Sum (overall): {matrix.sum()}") # 45 (1+2+3+4+5+6+7+8+9)
print(f"Mean (overall): {matrix.mean()}") # 5.0

# axis=0 (열(column)을 따라 연산, 각 열의 요소들을 집계)
# 결과 배열의 shape는 (열의 개수,) 또는 (1, 열의 개수) if keepdims=True
print(f"Sum along axis=0: {matrix.sum(axis=0)}") # [12 15 18] (1+4+7, 2+5+8, 3+6+9)
print(f"Mean along axis=0: {matrix.mean(axis=0)}") # [4. 5. 6.]

# axis=1 (행(row)을 따라 연산, 각 행의 요소들을 집계)
# 결과 배열의 shape는 (행의 개수,) 또는 (행의 개수, 1) if keepdims=True
print(f"Sum along axis=1: {matrix.sum(axis=1)}") # [ 6 15 24] (1+2+3, 4+5+6, 7+8+9)
print(f"Max along axis=1: {matrix.max(axis=1)}") # [3 6 9]

# argmin, argmax: 최솟값/최댓값이 있는 인덱스를 반환
print(f"Argmin along axis=0: {matrix.argmin(axis=0)}") # [0 0 0] (각 열에서 최솟값의 인덱스는 0)
print(f"Argmax along axis=1: {matrix.argmax(axis=1)}") # [2 2 2] (각 행에서 최댓값의 인덱스는 2)

# keepdims=True: 연산 후에도 차원 수를 유지
print(f"Sum along axis=0 (keepdims=True):\n {matrix.sum(axis=0, keepdims=True)}")
# [[12 15 18]] (shape: (1, 3))
```

**3. 브로드캐스팅 (Broadcasting) 및 Shapes matter**

```python
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]]) # shape (2, 3)

b = np.array([10, 20, 30]) # shape (3,)

# A + b 연산 (브로드캐스팅 적용)
# b가 A의 각 행에 맞춰 확장되어 연산됩니다.
print(f"A + b:\n {A + b}")
# [[11 22 33]
#  [14 25 36]]

# 브로드캐스팅 오류 예시: shape가 맞지 않을 때
# c = np.array([1, 2]) # shape (2,)
# print(A + c) # Error! cannot broadcast shape (2,3) with (2,)
```

### 구체적 예시

*   **요소별 연산**:
    *   **성적 처리**: 학생들의 과목별 점수가 `np.array`로 주어졌을 때, 모든 학생의 점수에 일괄적으로 5점씩 가산점을 부여하거나 (`scores + 5`), 두 학기의 성적표(`midterm_scores`, `final_scores`)를 합산하여 최종 점수를 계산할 때 (`midterm_scores + final_scores`) 요소별 연산이 사용됩니다.
    *   **이미지 처리**: 이미지의 각 픽셀 밝기 값을 조정하거나, 두 이미지를 합성할 때 (`image1 * 0.5 + image2 * 0.5`) 픽셀 단위로 연산이 이루어집니다.

*   **축소 연산**:
    *   **데이터 분석**: 주식 가격 데이터 배열에서 하루 최고가/최저가 (`.max()`, `.min()`)를 찾거나, 특정 기간 동안의 평균 거래량 (`.mean()`), 표준 편차 (`.std()`)를 계산할 때 사용됩니다.
    *   **설문조사 결과**: 설문조사 응답 데이터를 2D 배열로 저장했을 때, 각 질문에 대한 평균 응답 점수 (`axis=0`으로 `.mean()`)나 각 응답자의 총점 (`axis=1`로 `.sum()`)을 쉽게 계산할 수 있습니다.
    *   **최고/최저점 학생 찾기**: 시험 점수 배열에서 가장 높은 점수를 받은 학생의 인덱스 (`.argmax()`)를 찾아 해당 학생의 정보를 조회할 때 유용합니다.

### 시험 포인트

*   ⭐ **요소별 연산과 축소 연산의 개념 및 근본적인 차이점을 명확히 이해해야 합니다.** 요소별 연산은 배열의 각 요소에 개별적으로 적용되어 결과 배열의 크기가 유지되거나(두 배열 간 연산), 스칼라 연산의 경우 원본 배열과 동일한 형태를 가집니다. 축소 연산은 배열의 차원을 줄이거나 하나의 값으로 집계합니다.

*   ⭐ **`axis` 매개변수의 의미와 2차원 배열 (`axis=0`, `axis=1`)에서의 동작 방식을 정확히 알아야 합니다.** 어떤 `axis` 값을 주느냐에 따라 연산의 결과가 어떻게 달라지는지 그림을 그리거나 예시를 통해 스스로 설명할 수 있어야 합니다.

*   ⭐ `min`/`max`와 `argmin`/`argmax`의 차이를 숙지하세요. `min`/`max`는 **값(value)**을 반환하고, `argmin`/`argmax`는 해당 값의 **인덱스(index)**를 반환합니다.

*   ⭐ **브로드캐스팅(Broadcasting) 규칙을 이해하는 것이 중요합니다.** 서로 다른 형태의 배열이 어떻게 연산될 수 있는지, 그리고 언제 오류가 발생하는지 파악해야 합니다. 특히, `keepdims=True`가 축소 연산 결과의 형태에 어떻게 영향을 미치는지 이해하고 있어야 브로드캐스팅을 활용한 연산을 올바르게 수행할 수 있습니다. 예를 들어, `(N, D)` 형태의 배열에서 `axis=0`으로 평균을 낸 후, 이 평균 값을 원본 배열에서 빼려면 브로드캐스팅을 위해 `keepdims=True`로 평균을 계산하여 `(1, D)` 형태로 만들어야 할 수 있습니다.

---
## Slide 69

```python
import numpy as np
```

### **핵심 개념**

이 슬라이드는 NumPy 배열에서 수행할 수 있는 다양한 종류의 곱셈 연산들을 비교 설명합니다. 주요 개념은 다음과 같습니다:

1.  **행렬 곱셈 (Matrix Multiplication)**: 선형대수학에서 정의하는 표준적인 행렬 곱셈입니다. `@` 연산자 또는 `np.matmul()` 함수를 사용합니다. 두 행렬의 내측 차원(inner dimensions)이 일치해야 합니다.
2.  **닷 프로덕트 (Dot Product)**: `np.dot()` 함수를 사용하며, 입력 배열의 차원에 따라 동작이 달라집니다.
    *   두 벡터의 닷 프로덕트는 스칼라 값을 반환합니다.
    *   행렬과 벡터의 닷 프로덕트는 행렬-벡터 곱셈을 수행합니다.
    *   두 행렬의 닷 프로덕트는 행렬 곱셈을 수행합니다 (이는 `np.matmul()`과 유사하나, 1D 배열 처리 방식 등에서 미묘한 차이가 있을 수 있습니다).
3.  **요소별 곱셈 (Element-wise Multiplication)**: 두 배열의 같은 위치에 있는 요소들끼리 곱하는 연산입니다. `*` 연산자 또는 `np.multiply()` 함수를 사용합니다. 두 배열의 형태(shape)가 동일하거나 NumPy의 브로드캐스팅(broadcasting) 규칙에 따라 호환되어야 합니다.
4.  **스칼라 곱셈 (Scalar Multiplication)**: 배열의 모든 요소에 스칼라 값을 곱하는 연산입니다. 이는 요소별 곱셈의 특수한 경우로, 브로드캐스팅이 자동으로 적용됩니다.

### **코드/수식 해설**

아래 코드는 `A`, `B` 행렬과 `x` 벡터를 정의한 후, 다양한 곱셈 연산을 수행합니다.

```python
A = np.arange(6).reshape(2, 3) # A는 2x3 행렬: [[0, 1, 2], [3, 4, 5]]
B = np.arange(6).reshape(3, 2) # B는 3x2 행렬: [[0, 1], [2, 3], [4, 5]]
x = np.array([1.0, 2.0, 3.0]) # x는 1x3 벡터: [1.0, 2.0, 3.0]
```

1.  **행렬 곱셈 (Matrix Multiply)**: `A @ B`
    *   **코드**: `print(A @ B)`
    *   **설명**: 2x3 행렬 A와 3x2 행렬 B의 행렬 곱셈을 수행합니다. 결과는 2x2 행렬이 됩니다. `@` 연산자는 `np.matmul()`과 동일합니다.
    *   **수식**: 두 행렬 $A$ ($m \times n$)와 $B$ ($n \times p$)의 곱 $C = AB$는 $m \times p$ 행렬이며, 각 요소 $C_{ij}$는 다음과 같이 정의됩니다.
        $$C_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}$$
    *   **계산 과정**:
        *   $A = \begin{pmatrix} 0 & 1 & 2 \\ 3 & 4 & 5 \end{pmatrix}$, $B = \begin{pmatrix} 0 & 1 \\ 2 & 3 \\ 4 & 5 \end{pmatrix}$
        *   $C_{11} = (0 \times 0) + (1 \times 2) + (2 \times 4) = 0 + 2 + 8 = 10$
        *   $C_{12} = (0 \times 1) + (1 \times 3) + (2 \times 5) = 0 + 3 + 10 = 13$
        *   $C_{21} = (3 \times 0) + (4 \times 2) + (5 \times 4) = 0 + 8 + 20 = 28$
        *   $C_{22} = (3 \times 1) + (4 \times 3) + (5 \times 5) = 3 + 12 + 25 = 40$
    *   **출력**:
        ```
        [[10 13]
         [28 40]]
        ```

2.  **행렬-벡터 곱셈 (Matrix-Vector Dot Product)**: `np.dot(A, x)`
    *   **코드**: `print(np.dot(A, x))`
    *   **설명**: 2x3 행렬 A와 1x3 벡터 x의 닷 프로덕트를 수행합니다. 이 경우 행렬-벡터 곱셈으로 해석됩니다. 결과는 1x2 벡터가 됩니다.
    *   **수식**: 행렬 $A$ ($m \times n$)와 벡터 $x$ ($n \times 1$)의 곱 $y = Ax$는 $m \times 1$ 벡터이며, 각 요소 $y_i$는 다음과 같이 정의됩니다.
        $$y_i = \sum_{k=1}^{n} A_{ik} x_k$$
    *   **계산 과정**:
        *   $A = \begin{pmatrix} 0 & 1 & 2 \\ 3 & 4 & 5 \end{pmatrix}$, $x = \begin{pmatrix} 1.0 \\ 2.0 \\ 3.0 \end{pmatrix}$
        *   $y_1 = (0 \times 1.0) + (1 \times 2.0) + (2 \times 3.0) = 0 + 2.0 + 6.0 = 8.0$
        *   $y_2 = (3 \times 1.0) + (4 \times 2.0) + (5 \times 3.0) = 3.0 + 8.0 + 15.0 = 26.0$
    *   **출력**:
        ```
        [ 8. 26.]
        ```

3.  **요소별 스칼라 곱셈 (Element-wise Scale)**: `A * 2`
    *   **코드**: `print(A * 2)`
    *   **설명**: 2x3 행렬 A의 모든 요소에 스칼라 값 2를 곱합니다. NumPy의 브로드캐스팅 기능에 의해 자동으로 요소별 곱셈이 됩니다.
    *   **수식**: 스칼라 $c$와 행렬 $A$에 대해, $cA$ 행렬의 각 요소는 $(cA)_{ij} = c \cdot A_{ij}$ 로 정의됩니다.
    *   **계산 과정**:
        *   $A = \begin{pmatrix} 0 & 1 & 2 \\ 3 & 4 & 5 \end{pmatrix}$
        *   $2A = \begin{pmatrix} 0 \times 2 & 1 \times 2 & 2 \times 2 \\ 3 \times 2 & 4 \times 2 & 5 \times 2 \end{pmatrix} = \begin{pmatrix} 0 & 2 & 4 \\ 6 & 8 & 10 \end{pmatrix}$
    *   **출력**:
        ```
        [[ 0  2  4]
         [ 6  8 10]]
        ```

4.  **요소별 제곱 (Element-wise Square)**: `np.multiply(A, A)`
    *   **코드**: `print(np.multiply(A, A))`
    *   **설명**: 2x3 행렬 A의 각 요소를 자기 자신과 곱하여 제곱합니다. 이는 `A * A`와 동일하게 작동합니다.
    *   **수식**: 두 행렬 $A$와 $B$ (동일한 형태)의 요소별 곱(Hadamard product) $A \odot B$는 각 요소가 $(A \odot B)_{ij} = A_{ij} \cdot B_{ij}$ 로 정의됩니다. 여기서는 $A \odot A$에 해당합니다.
    *   **계산 과정**:
        *   $A = \begin{pmatrix} 0 & 1 & 2 \\ 3 & 4 & 5 \end{pmatrix}$
        *   $A \odot A = \begin{pmatrix} 0 \times 0 & 1 \times 1 & 2 \times 2 \\ 3 \times 3 & 4 \times 4 & 5 \times 5 \end{pmatrix} = \begin{pmatrix} 0 & 1 & 4 \\ 9 & 16 & 25 \end{pmatrix}$
    *   **출력**:
        ```
        [[ 0  1  4]
         [ 9 16 25]]
        ```

### **구체적 예시**

*   **행렬 곱셈 (Matrix Multiplication)**:
    *   **머신러닝**: 신경망에서 입력 데이터(특징 벡터)와 가중치 행렬을 곱하여 다음 계층의 입력 또는 출력을 계산할 때 사용됩니다. $y = Wx + b$ (여기서 $W$는 가중치 행렬, $x$는 입력 벡터).
    *   **컴퓨터 그래픽스**: 3D 객체의 회전, 이동, 크기 조절과 같은 변환(transformation)을 표현하는 행렬들을 연속적으로 곱하여 최종 변환 행렬을 구할 때 사용됩니다.
*   **닷 프로덕트 (Dot Product)**:
    *   **머신러닝**: 두 벡터의 유사도(similarity)를 측정할 때 (예: 코사인 유사도 계산에 활용), 또는 특정 방향으로의 투영(projection)을 계산할 때 사용됩니다.
    *   **물리학**: 일(Work) 계산 ($W = F \cdot d$, 힘과 변위 벡터의 내적) 등.
*   **요소별 곱셈 (Element-wise Multiplication)**:
    *   **이미지 처리**: 이미지의 각 픽셀 값에 특정 스케일 팩터(예: 밝기 조절)를 곱하거나, 두 이미지의 픽셀을 합성할 때 사용됩니다. `A * 0.5`는 이미지 A의 밝기를 절반으로 줄이는 것과 같습니다.
    *   **데이터 정규화**: 특정 통계량(예: 표준편차)으로 데이터셋의 각 요소를 나누어 정규화할 때 사용될 수 있습니다.
    *   **신경망**: 활성화 함수를 적용한 후, 특정 계층의 출력을 마스킹(masking)하거나, 드롭아웃(dropout)과 같은 정규화 기법을 적용할 때 요소별 곱셈이 사용됩니다.

### **시험 포인트**

*   ⭐ **행렬 곱셈과 요소별 곱셈의 명확한 차이**: `A @ B` (`np.matmul()`)는 선형대수학적 행렬 곱셈이고, `A * B` (`np.multiply()`)는 같은 위치의 요소들끼리 곱하는 연산입니다. 이 둘을 혼동하면 안 됩니다.
*   ⭐ `np.dot()` 함수의 다용도성: 입력 배열의 차원에 따라 스칼라 닷 프로덕트, 행렬-벡터 곱셈, 행렬 곱셈으로 동작할 수 있음을 이해해야 합니다.
*   ⭐ **브로드캐스팅 (Broadcasting)**: 스칼라를 배열에 곱할 때 (`A * 2`), 스칼라가 자동으로 배열의 모든 요소에 맞게 확장되어 요소별 연산이 가능해지는 개념을 알아야 합니다. (더 복잡한 브로드캐스팅 규칙도 있지만, 이 슬라이드에서는 스칼라 곱셈이 예시입니다.)
*   ⭐ **행렬 곱셈의 차원 호환성**: $m \times n$ 행렬과 $p \times q$ 행렬을 곱하려면 $n=p$ (첫 번째 행렬의 열 수와 두 번째 행렬의 행 수)여야 하며, 결과 행렬의 차원은 $m \times q$가 됩니다.

---
## Slide 70

## NumPy를 활용한 선형대수 연산 하이라이트

### **핵심 개념**
*   **행렬 곱셈 (Matrix Multiplication)**: 두 행렬의 곱셈을 수행합니다. NumPy에서는 `np.matmul` 함수 또는 `@` 연산자를 사용하여 표현합니다.
*   **선형 연립 방정식 해법 (Solving Linear Systems)**: $Ax = b$ 형태의 선형 연립 방정식을 풀 때, 역행렬($A^{-1}$)을 직접 계산하여 $x = A^{-1}b$를 구하기보다는 `np.linalg.solve(A, b)` 함수를 사용하는 것이 **수치적 안정성(numerical stability)** 측면에서 권장됩니다.
*   **행렬 분해 (Matrix Decomposition)**:
    *   **고유값 분해 (Eigen Decomposition)**: 정방 행렬을 고유값(eigenvalues)과 고유벡터(eigenvectors)로 분해하는 과정입니다. `np.linalg.eig` 함수를 사용합니다.
    *   **특이값 분해 (Singular Value Decomposition, SVD)**: 임의의 행렬을 세 개의 행렬(좌측 특이 벡터, 특이값 대각 행렬, 우측 특이 벡터)로 분해하는 과정입니다. `np.linalg.svd` 함수를 사용합니다.

### **코드/수식 해설**

1.  **행렬 곱셈 (`np.matmul` 또는 `@`)**
    행렬 $A$와 $B$의 곱 $C = AB$를 계산합니다. 이는 $A$의 열의 개수와 $B$의 행의 개수가 같아야 합니다.
    ```python
    import numpy as np

    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    # np.matmul 사용
    C_matmul = np.matmul(A, B)
    print("np.matmul 결과:\n", C_matmul)

    # @ 연산자 사용 (Python 3.5+ 부터 지원)
    C_at = A @ B
    print("@ 연산자 결과:\n", C_at)
    ```

2.  **선형 연립 방정식 풀이 (`np.linalg.solve` vs `np.linalg.inv @ b`)**
    $Ax = b$ 형태의 선형 연립 방정식에서 $x$를 찾는 문제.
    *   `np.linalg.solve(A, b)`는 내부적으로 LU 분해 등 더 안정적인 알고리즘을 사용하여 $x$를 직접 계산합니다.
    *   `np.linalg.inv(A) @ b`는 먼저 $A$의 역행렬 $A^{-1}$을 계산한 후 $A^{-1}$과 $b$를 곱하는 방식입니다. 행렬이 특이(singular)하거나 거의 특이(near-singular)할 경우 역행렬 계산 시 수치 오차가 크게 발생할 수 있습니다.
    ```python
    import numpy as np

    A = np.array([[2, 1], [1, 1]]) # 계수 행렬
    b = np.array([4, 3])        # 상수 벡터

    # 권장 방법: 수치적으로 안정적
    x_solve = np.linalg.solve(A, b)
    print("np.linalg.solve(A, b) 결과 (x):\n", x_solve)

    # 피해야 할 방법: 수치적으로 불안정할 수 있음
    A_inv = np.linalg.inv(A)
    x_inv_mul = A_inv @ b
    print("np.linalg.inv(A) @ b 결과 (x):\n", x_inv_mul)
    ```
    이 예시에서는 두 방법의 결과가 같지만, 복잡한 실제 데이터나 근사 해를 다룰 때 `solve`의 장점이 두드러집니다.

3.  **고유값 분해 (`np.linalg.eig`) 및 특이값 분해 (`np.linalg.svd`)**
    *   **고유값 분해 (Eigen Decomposition)**: $A$가 정방 행렬일 때, $Av = \lambda v$를 만족하는 스칼라 $\lambda$ (고유값)와 벡터 $v$ (고유벡터)를 찾습니다.
        ```python
        import numpy as np

        A = np.array([[1, 2], [2, 1]])
        eigenvalues, eigenvectors = np.linalg.eig(A)
        print("고유값 (Eigenvalues):\n", eigenvalues)
        print("고유벡터 (Eigenvectors):\n", eigenvectors)
        # eigenvectors의 각 열이 대응하는 고유값의 고유벡터입니다.
        ```
    *   **특이값 분해 (Singular Value Decomposition, SVD)**: 임의의 $m \times n$ 행렬 $A$를 $A = U \Sigma V^T$로 분해합니다. 여기서 $U$는 $m \times m$ 직교 행렬, $\Sigma$는 $m \times n$ 대각 행렬(대각 성분은 특이값), $V^T$는 $n \times n$ 직교 행렬입니다.
        ```python
        import numpy as np

        A = np.array([[1, 1, 1], [2, 2, 2]])
        U, s, Vt = np.linalg.svd(A) # s는 특이값 벡터, Vt는 V의 전치 행렬

        print("U 행렬:\n", U)
        print("특이값 (Singular values):\n", s)
        print("V 전치 행렬 (Vt):\n", Vt)
        ```

### **구체적 예시**
*   **행렬 곱셈**: 이미지 처리에서 이미지에 필터(예: 블러, 샤프닝)를 적용하는 것이 행렬 곱셈의 일종입니다. 3D 그래픽스에서는 객체의 회전, 이동, 크기 조절 등의 변환을 행렬 곱셈으로 표현합니다.
*   **선형 연립 방정식 풀이**: 머신러닝에서 선형 회귀 모델의 최적 계수를 찾을 때, 정규 방정식 $X^T X \beta = X^T y$를 풀어야 합니다. 이때 $\beta$를 계산하는 데 `np.linalg.solve`가 활용됩니다.
*   **고유값 분해**: 주성분 분석(PCA)에서 데이터의 분산 구조를 가장 잘 설명하는 주성분(principal components)을 찾을 때 사용됩니다. 공분산 행렬의 고유벡터가 바로 주성분이 됩니다.
*   **특이값 분해**: 추천 시스템에서 사용자-아이템 평점 행렬의 차원을 축소하여 잠재 요인을 추출하거나, 이미지 압축, 자연어 처리의 토픽 모델링 등 데이터의 패턴을 찾고 노이즈를 제거하는 데 광범위하게 활용됩니다.

### **시험 포인트**
*   ⭐ `np.matmul`과 `@` 연산자가 행렬 곱셈에 사용된다는 것을 정확히 이해하고, 실제 코드에서 활용할 수 있어야 합니다. (점곱 `np.dot`과의 차이점도 명확히 알아두세요!)
*   ⭐ 선형 연립 방정식 $Ax=b$를 풀 때, `np.linalg.solve(A, b)`가 `np.linalg.inv(A) @ b`보다 **수치적으로 더 안정적이고 효율적**이며 **권장되는 이유**를 설명할 수 있어야 합니다. (수치 오차 및 계산 복잡성 측면)
*   ⭐ 고유값 분해(`np.linalg.eig`)와 특이값 분해(`np.linalg.svd`)가 각각 어떤 목적으로 사용되는지, 그리고 **데이터 분석 및 머신러닝에서 어떤 핵심적인 역할(예: PCA, 추천 시스템)**을 하는지 구체적인 활용 사례와 함께 이해하는 것이 매우 중요합니다.

---
## Slide 71

---

### **핵심 개념**

*   **고유값 (Eigenvalues) 및 고유벡터 (Eigenvectors)**:
    *   선형 변환 $A$가 벡터 $v$에 작용할 때, 벡터의 방향은 변하지 않고 크기만 $\lambda$배로 변하는 특별한 관계를 가진 벡터 $v$를 고유벡터, 그 스케일 팩터 $\lambda$를 고유값이라고 합니다.
    *   수식으로 표현하면 $Av = \lambda v$ 입니다. 여기서 $A$는 정방 행렬, $v$는 0이 아닌 벡터, $\lambda$는 스칼라입니다.
    *   데이터 분석에서는 차원 축소(PCA), 스펙트럼 분석 등에 활용됩니다.

*   **선형 시스템 해 찾기 (Solving Linear Systems)**:
    *   $Ax = b$ 형태의 연립 선형 방정식의 해 벡터 $x$를 찾는 과정입니다. 여기서 $A$는 계수 행렬, $x$는 미지수 벡터, $b$는 상수 벡터입니다.
    *   $A$의 역행렬 $A^{-1}$이 존재한다면, $x = A^{-1}b$로 해를 구할 수 있습니다. 하지만 실제 계산에서는 역행렬을 직접 계산하는 것보다 더 효율적이고 안정적인 수치 해석 방법을 사용합니다.
    *   NumPy의 `linalg.solve` 함수는 이 방법을 내부적으로 사용하여 $x$를 계산합니다.

### **코드/수식 해설**

**코드**
```python
import numpy as np

# 2x2 행렬 A 정의
A = np.array([[3.0, 1.0],
              [0.0, 2.0]])

# 행렬 A의 고유값(w)과 고유벡터(V) 계산
# w: 고유값들을 담고 있는 1차원 배열
# V: 고유벡터들을 열벡터로 갖는 2차원 행렬. 즉, V[:, i]가 i번째 고유값에 해당하는 고유벡터
w, V = np.linalg.eig(A) # eigenvalues, eigenvectors

# 상수 벡터 b 정의
b = np.array([9.0, 4.0])

# 선형 시스템 Ax = b 의 해 x 계산
# np.linalg.solve(A, b)는 A의 역행렬을 계산하지 않고 직접 Ax = b를 푸는 효율적인 방법을 사용
x = np.linalg.solve(A, b)

# 계산된 고유값 w 출력
print(w)
# 계산된 선형 시스템의 해 x 출력
print(x)
```

**수식**
1.  **고유값 및 고유벡터 정의**:
    $Av = \lambda v$
    여기서 $A$는 $n \times n$ 행렬, $v$는 0이 아닌 $n \times 1$ 벡터, $\lambda$는 스칼라입니다.

2.  **선형 시스템**:
    $Ax = b$
    여기서 $A$는 $n \times n$ 행렬, $x$는 $n \times 1$ 미지수 벡터, $b$는 $n \times 1$ 상수 벡터입니다.

### **구체적 예시**

*   **고유값/고유벡터**: 어떤 이미지를 회전시키거나 늘리는 변환(행렬 $A$)을 가했을 때, 원래 이미지의 특정 특징(고유벡터)은 회전되지 않고 그 크기만 변할 수 있습니다(고유값). 예를 들어, 얼굴 인식에서 주성분 분석(PCA)은 얼굴 이미지의 "주요 특징 방향"을 고유벡터로 찾아내고, 각 특징이 얼마나 중요한지를 고유값으로 나타냅니다.

*   **선형 시스템 해**:
    *   **공정 제어**: 화학 공정에서 여러 변수(온도, 압력, 농도 등)가 서로 상호작용할 때, 원하는 결과(b)를 얻기 위해 각 변수(x)를 어떻게 조절해야 하는지 나타내는 시스템 $Ax=b$를 풀어 최적의 조건을 찾을 수 있습니다.
    *   **경제 모델**: 경제학에서 여러 시장의 공급과 수요 균형을 나타내는 연립방정식을 $Ax=b$ 형태로 표현하고, 이 시스템의 해 $x$는 각 시장의 균형 가격이나 수량을 의미할 수 있습니다.

### **시험 포인트**

*   **NumPy `linalg` 모듈의 핵심 함수** ⭐: `np.linalg.eig()`, `np.linalg.solve()`의 정확한 용도와 반환 값을 이해하고 있어야 합니다.
    *   `np.linalg.eig(A)`는 고유값(`w`)과 고유벡터 행렬(`V`)을 튜플로 반환합니다. 이때 고유벡터 행렬 `V`의 각 **열**이 하나의 고유벡터를 나타냅니다.
    *   `np.linalg.solve(A, b)`는 행렬 $A$와 벡터 $b$가 주어졌을 때 $Ax=b$의 해 벡터 $x$를 반환합니다.
*   **고유값과 고유벡터의 개념적 의미** ⭐: 선형 변환 시 방향이 변하지 않는 특별한 벡터와 그 스케일링 인자라는 정의를 명확히 이해해야 합니다.
*   **$Ax=b$ 형태의 선형 시스템 해를 구하는 것의 의미** ⭐: 여러 미지수가 얽힌 연립방정식의 해를 구하는 수학적, 계산적 방법임을 알아야 합니다.

---
## Slide 72

**핵심 개념**
NumPy 브로드캐스팅(Broadcasting)은 서로 다른 형태(shape)를 가진 배열들 간에 산술 연산이 가능하도록 하는 강력한 메커니즘입니다. 일반적으로 배열 연산은 동일한 형태를 가져야 하지만, 브로드캐스팅 규칙이 적용되면 NumPy는 작은 배열을 더 큰 배열의 형태에 맞게 "확장"하여 연산을 수행합니다. 이는 데이터 복사를 최소화하여 효율적인 연산을 가능하게 합니다. 슬라이드에서는 이러한 브로드캐스팅이 작동하는 네 가지 핵심 규칙을 설명합니다.

1.  **후행 차원부터 왼쪽으로 형태 비교**: 두 배열의 형태를 가장 오른쪽 차원부터 왼쪽으로 이동하면서 차원별로 비교합니다.
2.  **차원 호환성 조건**: 두 차원이 호환되려면 다음 중 하나를 만족해야 합니다.
    *   두 차원의 크기가 정확히 같아야 합니다.
    *   두 차원 중 하나의 크기가 1이어야 합니다.
3.  **선행 차원 처리**: 차원의 수가 다른 경우, 더 작은 차원을 가진 배열의 선행(왼쪽) 차원은 크기가 1인 것으로 간주됩니다.
4.  **결과 형태 결정**: 연산 결과 배열의 형태는 각 차원별로 비교된 두 차원 중 최댓값으로 결정됩니다. (즉, 크기가 1인 차원은 다른 차원의 크기에 맞춰 확장됩니다.)

**코드/수식 해설**

브로드캐스팅 규칙은 수식이 아닌 알고리즘적 규칙으로 이해하는 것이 적합합니다. 각 규칙에 대한 설명을 파이썬 코드 예시와 함께 제공합니다.

```python
import numpy as np

# Rule 1: Compare shapes from the trailing dimensions moving left.
# Rule 3: Missing leading dimensions are treated as 1.
# 예시: (2, 3)과 (3,) 형태의 배열 비교
a = np.array([[1, 2, 3], [4, 5, 6]]) # shape: (2, 3)
b = np.array([10, 20, 30])           # shape: (3,)

# 비교 과정:
# b의 형태는 브로드캐스팅을 위해 (1, 3)으로 간주됩니다.
# (2, 3)
# (1, 3)
# 오른쪽부터 비교:
#   차원 1 (가장 오른쪽): 3 vs 3 -> 같으므로 호환 (Rule 2)
#   차원 0 (다음 왼쪽):   2 vs 1 -> 하나가 1이므로 호환 (Rule 2)

# Rule 2: Dimensions are compatible if equal or one of them is 1.
# 호환 가능한 경우:
arr1 = np.ones((2, 3)) # shape (2, 3)
arr2 = np.ones((1, 3)) # shape (1, 3) - 차원 0: 2 vs 1 (호환), 차원 1: 3 vs 3 (호환)
print(f"Compatible shapes: {arr1.shape} and {arr2.shape}")
print(arr1 + arr2) # 연산 가능

arr3 = np.ones((2, 1)) # shape (2, 1)
arr4 = np.ones((1, 3)) # shape (1, 3) - 차원 0: 2 vs 1 (호환), 차원 1: 1 vs 3 (호환)
print(f"\nCompatible shapes: {arr3.shape} and {arr4.shape}")
print(arr3 + arr4) # 연산 가능

# 호환 불가능한 경우:
# 차원 0: 2 vs 5 (다르고, 어느 하나도 1이 아님) -> 호환 불가능
# arr5 = np.ones((2, 3)) # shape (2, 3)
# arr6 = np.ones((5, 3)) # shape (5, 3)
# print(arr5 + arr6) # ValueError: operands could not be broadcast together with shapes (2,3) (5,3)

# Rule 4: Result shape is the elementwise maximum along each dimension.
# arr3 (2, 1) + arr4 (1, 3)
# 비교: (2, 1) vs (1, 3)
#   가장 오른쪽 차원: max(1, 3) = 3
#   다음 왼쪽 차원:   max(2, 1) = 2
# 결과 형태는 (2, 3)이 됩니다.
print(f"\nResult shape of {arr3.shape} + {arr4.shape} is {(arr3 + arr4).shape}")
```

**구체적 예시**

1.  **스칼라(Scalar)와 배열 연산**: 스칼라는 (1,) 형태를 가지며, 모든 차원에서 1로 간주되어 모든 배열 차원에 브로드캐스트됩니다.
    ```python
    import numpy as np
    arr = np.array([[1, 2, 3], [4, 5, 6]]) # shape (2, 3)
    scalar = 10
    result = arr + scalar
    print("Scalar + Array example:")
    print(result)
    # arr.shape: (2, 3)
    # scalar: 10 (브로드캐스팅 시 (1,)으로 간주되어 (1, 1) -> (2, 3)으로 확장)
    # 결과 shape: (2, 3)
    ```

2.  **1D 배열과 2D 배열 연산**: `(M,)` 형태의 1D 배열은 `(1, M)` 형태로 브로드캐스트되어 2D 배열의 각 행에 적용됩니다.
    ```python
    import numpy as np
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]]) # shape (2, 3)
    arr_1d = np.array([10, 20, 30])           # shape (3,)
    result = arr_2d + arr_1d
    print("\n1D Array + 2D Array example:")
    print(result)
    # arr_2d.shape: (2, 3)
    # arr_1d.shape: (3,) -> 브로드캐스팅 시 (1, 3)으로 간주됨
    # 비교:
    #   (2, 3)
    #   (1, 3)
    #   오른쪽: 3 vs 3 (같음)
    #   왼쪽:   2 vs 1 (하나가 1)
    # 결과 shape: (max(2,1), max(3,3)) = (2, 3)
    # 내부적으로 arr_1d가 [[10, 20, 30], [10, 20, 30]] 처럼 확장되어 연산됩니다.
    ```

3.  **`(`M, 1`)` 형태와 `(`1, N`)` 형태의 배열 연산 (외적과 유사)**:
    ```python
    import numpy as np
    col_vec = np.array([[10], [20]]) # shape (2, 1)
    row_vec = np.array([1, 2, 3])    # shape (3,) -> 브로드캐스팅 시 (1, 3)으로 간주됨
    result = col_vec + row_vec
    print("\n(M, 1) + (1, N) example:")
    print(result)
    # col_vec.shape: (2, 1)
    # row_vec.shape: (1, 3) (브로드캐스팅 후)
    # 비교:
    #   (2, 1)
    #   (1, 3)
    #   오른쪽: 1 vs 3 (하나가 1)
    #   왼쪽:   2 vs 1 (하나가 1)
    # 결과 shape: (max(2,1), max(1,3)) = (2, 3)
    # col_vec이 [[10, 10, 10], [20, 20, 20]]으로,
    # row_vec이 [[1, 2, 3], [1, 2, 3]]으로 확장되어 연산됩니다.
    ```

**시험 포인트**

*   ⭐ **브로드캐스팅의 정의와 목적**: 브로드캐스팅이 무엇이며 왜 사용하는지 (서로 다른 형태의 배열 연산, 메모리 효율성)를 설명할 수 있어야 합니다.
*   ⭐ **브로드캐스팅 규칙의 정확한 적용**: 슬라이드의 네 가지 규칙을 순서대로 정확하게 설명하고 실제 배열 형태에 적용할 수 있어야 합니다. 특히 '후행 차원부터 비교', '하나라도 1이면 호환', '선행 차원 1 간주', '결과 형태는 최댓값' 규칙을 이해하는 것이 중요합니다.
*   ⭐ **호환 가능한/불가능한 형태 식별**: 주어진 두 배열의 형태가 브로드캐스팅 규칙에 따라 연산 가능한지 여부를 판단할 수 있어야 합니다. (예: `(2,3)`과 `(5,3)`은 호환되지 않음)
*   ⭐ **결과 배열의 형태 예측**: 브로드캐스팅이 성공적으로 적용될 경우, 최종 결과 배열의 형태(shape)를 정확히 예측할 수 있어야 합니다.
*   ⭐ **코드 예시 분석**: 주어진 NumPy 코드에서 브로드캐스팅이 어떻게 적용되고 어떤 결과가 나오는지 설명할 수 있어야 합니다.

---
## Slide 73

다음은 슬라이드를 분석한 마크다운 노트입니다.

---

### 핵심 개념

NumPy 브로드캐스팅(Broadcasting)은 서로 다른 형태(shape)를 가진 배열(ndarray) 간에 산술 연산을 수행할 수 있도록 하는 강력한 기능입니다. NumPy는 명시적인 반복문(loop) 없이도 작은 배열이 큰 배열의 형태에 맞게 자동으로 확장(stretch)되도록 하여 연산을 가능하게 합니다. 이는 코드의 간결성을 높이고, 파이썬 루프 사용으로 인한 성능 저하 없이 효율적인 벡터화 연산을 가능하게 합니다.

브로드캐스팅이 작동하기 위한 두 가지 주요 규칙:
1.  **차원 수 일치**: 차원 수가 더 작은 배열의 형태(shape)는 왼쪽에 1이 채워져 큰 배열의 차원 수에 맞춰집니다.
2.  **차원 호환성**: 오른쪽부터 차원들을 비교하여, 다음 조건 중 하나를 만족해야 합니다.
    *   두 차원의 크기가 동일하다.
    *   두 차원 중 하나의 크기가 1이다.

### 코드/수식 해설

```python
import numpy as np

# u는 1차원 배열(벡터)로, 형태는 (3,)
u = np.array([1.0, 2.0, 3.0]) 

# M은 4x3 형태의 2차원 배열(행렬)로, 0부터 11까지의 숫자를 실수형으로 가집니다.
M = np.arange(12).reshape(4, 3) * 1.0 

# M과 u를 더하는 연산입니다. 여기서 브로드캐스팅이 발생합니다.
print(M + u) 

# 이 코드는 M + u와 동일한 결과를 얻는 "정렬된 형태"를 의도합니다.
# 하지만 슬라이드에 제시된 (M.T + u).T 코드는 ValueError를 발생시킬 수 있습니다.
# (M.T + u[:, np.newaxis]).T 와 같이 u를 명시적으로 열 벡터로 만들어야 정상 동작합니다.
print((M.T + u).T) 
```

1.  **`u = np.array([1.0, 2.0, 3.0])`**:
    *   형태(shape): `(3,)`
    *   `u`는 세 개의 요소를 가진 1차원 배열입니다.

2.  **`M = np.arange(12).reshape(4, 3) * 1.0`**:
    *   형태(shape): `(4, 3)`
    *   `M`은 4행 3열의 2차원 배열로, 초기값은 0.0부터 11.0까지입니다.

3.  **`print(M + u)`**:
    *   `M`의 형태는 `(4, 3)`이고, `u`의 형태는 `(3,)`입니다.
    *   브로드캐스팅 규칙에 따라, `u`는 가상의 `(1, 3)` 형태로 간주된 후 `M`의 각 행에 맞게 `(4, 3)` 형태로 확장되어 더해집니다.
    *   이는 `M`의 각 요소 $M_{ij}$에 해당 열 인덱스 $j$의 `u` 요소 $u_j$를 더하는 것과 같습니다.
    *   수식적 표현: $Result_{ij} = M_{ij} + u_j$

4.  **`print((M.T + u).T)`**:
    *   **⚠️ 슬라이드 표기 오류 및 설명**:
        *   `M.T`의 형태는 `(3, 4)`입니다.
        *   `u`의 형태는 `(3,)`입니다.
        *   표준 NumPy 브로드캐스팅 규칙에 따르면, `M.T` (`(3, 4)`)와 `u` (`(3,)`)는 마지막 차원(4와 3)이 일치하지 않으며, 둘 중 하나가 1이 아니므로 호환되지 않습니다. 따라서 `M.T + u` 연산은 `ValueError`를 발생시킵니다.
        *   슬라이드는 `M + u`와 동일한 결과를 얻는 "정렬된 형태"를 의도했으므로, `u`가 열 벡터 (`(3, 1)`)로 취급되어야 합니다. 즉, **`u[:, np.newaxis]` 또는 `u.reshape(-1, 1)`** 와 같이 명시적으로 열 벡터로 만들어주어야 합니다.
        *   **올바른 "정렬된 형태"**: `(M.T + u[:, np.newaxis]).T`
            *   `M.T`의 형태는 `(3, 4)`.
            *   `u[:, np.newaxis]`의 형태는 `(3, 1)`.
            *   이 경우, `u[:, np.newaxis]`는 `M.T`의 각 열에 맞게 `(3, 4)` 형태로 확장되어 더해집니다.
            *   이 결과를 다시 전치(`.T`)하면 `M + u`와 동일한 최종 결과를 얻습니다.

### 구체적 예시

주어진 `u`와 `M` 배열은 다음과 같습니다:
```
u = [1.0, 2.0, 3.0]

M = [[ 0.0,  1.0,  2.0],
     [ 3.0,  4.0,  5.0],
     [ 6.0,  7.0,  8.0],
     [ 9.0, 10.0, 11.0]]
```

`M + u` 연산 결과는 다음과 같이 계산됩니다:
`u`는 각 행에 대해 `[1.0, 2.0, 3.0]`으로 복제되어 더해집니다.
```
M + u = [[ 0.0+1.0,  1.0+2.0,  2.0+3.0],
         [ 3.0+1.0,  4.0+2.0,  5.0+3.0],
         [ 6.0+1.0,  7.0+2.0,  8.0+3.0],
         [ 9.0+1.0, 10.0+2.0, 11.0+3.0]]

      = [[ 1.0,  3.0,  5.0],
         [ 4.0,  6.0,  8.0],
         [ 7.0,  9.0, 11.0],
         [10.0, 12.0, 14.0]]
```

### 시험 포인트

*   ⭐ **브로드캐스팅의 개념**: 서로 다른 형태의 배열 간 연산을 효율적으로 수행하는 NumPy의 메커니즘을 설명하고, 이것이 왜 중요한지 (메모리 효율성, 코드 간결성, 성능 향상) 이해해야 합니다.
*   ⭐ **브로드캐스팅 규칙 적용**: 주어진 두 배열의 형태에 대해 브로드캐스팅 규칙(차원 수 일치, 차원 호환성)을 적용하여 연산이 가능한지, 가능하다면 결과 배열의 형태는 어떻게 될지 예측할 수 있어야 합니다.
*   ⭐ **1차원 배열(`(N,)` 형태)의 브로드캐스팅**: 1차원 배열이 2차원 배열과 연산될 때, 어떤 차원에 대해 확장되는지 정확히 이해하는 것이 중요합니다. (예: `(M, N)` 형태의 배열에 `(N,)` 형태의 배열을 더하면, `(N,)` 배열은 `(1, N)`으로 간주되어 각 행에 브로드캐스팅됩니다.)
*   ⭐ **명시적 차원 추가 (`np.newaxis`, `reshape`)**: `u[:, np.newaxis]`와 같이 `np.newaxis`나 `reshape`를 사용하여 배열의 차원을 명시적으로 조정함으로써 브로드캐스팅의 동작 방식을 제어할 수 있음을 알아야 합니다. 이는 특정 연산을 의도할 때 중요하며, 슬라이드와 같은 잠재적인 오류를 피하는 데 도움이 됩니다.

---
## Slide 74

## Common Broadcasting Pitfalls

### 핵심 개념
NumPy의 브로드캐스팅(Broadcasting)은 서로 다른 형태(shape)를 가진 배열 간에 연산을 수행할 수 있도록 자동으로 배열을 확장하는 강력한 기능입니다. 하지만 이 기능은 예상치 못한 결과를 초래할 수 있으므로, 몇 가지 일반적인 함정을 이해하고 대비하는 것이 중요합니다. 주요 함정으로는 배열의 **방향성 불일치**, **의도치 않은 차원 확장**, 그리고 이를 명확하게 제어하기 위한 **`np.newaxis`의 중요성**이 있습니다.

### 코드/수식 해설

#### 1. 방향성 불일치 (Mismatched orientation)
`op1 + op2`와 `op1 + op2.T`는 `op2`가 1차원 벡터이거나, `op2`의 형태에 따라 완전히 다른 결과를 만들어낼 수 있습니다. 이는 브로드캐스팅이 배열의 차원과 형태에 따라 어떻게 동작하는지를 명확히 이해해야 함을 의미합니다. 특히 2차원 배열에서 전치(transpose)는 행과 열의 역할을 바꾸므로 브로드캐스팅 방식에 큰 영향을 줍니다.

```python
import numpy as np

# 예시 1: 1차원 배열의 브로드캐스팅
# NumPy는 1차원 배열을 다른 차원에 맞춰 적절히 확장하려 시도합니다.
a = np.array([1, 2, 3]) # shape: (3,)
b = np.array([10, 20, 30]) # shape: (3,)

# 1차원 배열 + 1차원 배열: 요소별 연산
print(f"a + b: {a + b}") # [11 22 33]

# 2차원 배열 (행 벡터) + 2차원 배열 (열 벡터)
# (1, 3) + (3, 1) -> (3, 3)으로 확장
row_vec = a[np.newaxis, :] # shape: (1, 3)
col_vec = b[:, np.newaxis] # shape: (3, 1)
print(f"row_vec + col_vec:\n{row_vec + col_vec}")
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]

# 예시 2: 행렬과 벡터의 덧셈에서 T (전치)의 영향
matrix = np.array([[1, 2], [3, 4]]) # shape: (2, 2)
vector = np.array([10, 20])        # shape: (2,)

# matrix + vector: vector는 마지막 차원 (2,)에 맞춰 확장됨. (2, 2) + (2,) -> (2, 2)
print(f"matrix + vector:\n{matrix + vector}")
# [[11 22]
#  [13 24]]

# matrix + vector.T: vector.T는 (2,)이므로 T를 해도 동일한 (2,) 형태.
# 따라서 위의 결과와 동일하게 동작함.
print(f"matrix + vector.T:\n{matrix + vector.T}")
# [[11 22]
#  [13 24]]

# 만약 vector가 (1, 2)나 (2, 1) 형태의 2차원 배열이었다면 결과가 달라짐.
vector_row = np.array([[10, 20]]) # shape: (1, 2)
print(f"matrix + vector_row:\n{matrix + vector_row}")
# [[11 22]
#  [13 24]]

vector_col = np.array([[10], [20]]) # shape: (2, 1)
print(f"matrix + vector_col:\n{matrix + vector_col}")
# [[11 12]
#  [23 24]]

print(f"matrix + vector_col.T:\n{matrix + vector_col.T}") # vector_col.T는 (1, 2)
# [[11 22]
#  [13 24]]
```

#### 2. 차원이 1일 때의 의도치 않은 확장 (Unintended expansion)
배열의 특정 차원(dimension)의 크기가 1인 경우, NumPy는 해당 차원을 다른 배열의 해당 차원 크기에 맞게 자동으로 확장(broadcasting)합니다. 이는 때때로 편리하지만, 개발자가 의도하지 않은 방향으로 배열이 확장되어 오류나 예상치 못한 결과를 초래할 수 있습니다. `.shape` 속성을 사용하여 배열의 실제 형태를 항상 확인해야 합니다.

```python
import numpy as np

A = np.array([[1, 2, 3]]) # shape: (1, 3)
B = np.array([[10], [20], [30]]) # shape: (3, 1)
C = np.array([100, 200, 300]) # shape: (3,)

# A + B: (1, 3)과 (3, 1)은 (3, 3)으로 브로드캐스팅되어 덧셈
print(f"A.shape: {A.shape}, B.shape: {B.shape}")
print(f"A + B:\n{A + B}")
# [[11 12 13]
#  [21 22 23]
#  [31 32 33]]

# A + C: (1, 3)과 (3,)의 덧셈.
# C는 (3,)이므로, A의 마지막 차원 (3)과 일치.
# A의 첫 번째 차원 (1)에 맞춰 C가 확장됨. 결과는 (1, 3).
print(f"A.shape: {A.shape}, C.shape: {C.shape}")
print(f"A + C:\n{A + C}")
# [[101 202 303]]

# C + A: 순서만 바뀌었을 뿐, 결과는 동일하게 브로드캐스팅됨.
print(f"C + A:\n{C + A}")
# [[101 202 303]]

# 만약 C를 열 벡터로 만들고 싶었다면?
# C_col = C[:, np.newaxis] # shape: (3, 1)
# print(f"A + C_col:\n{A + C_col}")
# [[101 102 103]
#  [201 202 203]
#  [301 302 303]]
```

#### 3. `np.newaxis`를 사용하여 의도 명확화
`np.newaxis`는 배열에 새로운 차원(크기 1)을 명시적으로 추가하여 브로드캐스팅 의도를 분명히 하고 코드의 가독성을 높이는 데 사용됩니다. 이는 특히 1차원 배열을 행 벡터나 열 벡터로 명확하게 변환하고자 할 때 유용합니다.

```python
import numpy as np

arr = np.array([1, 2, 3]) # shape: (3,)

# arr를 행 벡터 (1, 3)로 만듦
row_vector = arr[np.newaxis, :]
print(f"row_vector: {row_vector}, shape: {row_vector.shape}")
# [[1 2 3]], shape: (1, 3)

# arr를 열 벡터 (3, 1)로 만듦
col_vector = arr[:, np.newaxis]
print(f"col_vector:\n{col_vector}, shape: {col_vector.shape}")
# [[1]
#  [2]
#  [3]], shape: (3, 1)

# 명시적인 형태를 이용한 덧셈
matrix = np.array([[10, 20, 30], [40, 50, 60]]) # shape: (2, 3)

# matrix에 각 행마다 arr를 더하고 싶을 때 (row-wise addition)
# matrix + arr (arr는 (3,)이므로 matrix의 마지막 차원에 브로드캐스팅됨)
print(f"matrix + arr:\n{matrix + arr}")
# [[11 22 33]
#  [41 52 63]]

# matrix에 각 열마다 arr를 더하고 싶을 때 (column-wise addition)
# arr를 열 벡터 (3, 1)로 만들어서 브로드캐스팅해야 함
print(f"matrix + arr[:, np.newaxis]:\n{matrix + arr[:, np.newaxis]}")
# Broadcasting error! shape (2, 3)와 (3, 1)은 호환되지 않음.
# Error: operands could not be broadcast together with shapes (2,3) (3,1)

# 올바른 column-wise addition 예시: matrix에 (2,1) 형태의 벡터를 더할 때
vector_to_add_col = np.array([100, 200])[:, np.newaxis] # shape: (2, 1)
print(f"matrix + vector_to_add_col:\n{matrix + vector_to_add_col}")
# [[110 120 130]
#  [240 250 260]]
```

### 구체적 예시
데이터 분석에서 평균(mean)이나 표준편차(standard deviation)로 데이터를 정규화(Normalization)할 때 브로드캐스팅이 자주 사용됩니다. 예를 들어, `(N, D)` 형태의 데이터 행렬에서 각 특성(feature)별 평균을 빼고 표준편차로 나누는 경우를 생각해봅시다.

데이터 행렬 `X` (N개의 샘플, D개의 특성): `X.shape`은 `(N, D)`
각 특성별 평균 `mu`: `mu.shape`은 `(D,)` 또는 `(1, D)`
각 특성별 표준편차 `sigma`: `sigma.shape`은 `(D,)` 또는 `1, D)`

```python
import numpy as np

# 가상 데이터 행렬 (N=4, D=3)
data_matrix = np.array([
    [10, 20, 30],
    [12, 22, 33],
    [15, 25, 36],
    [13, 23, 31]
], dtype=float)

# 각 특성(열)별 평균 계산
# axis=0: 열 방향으로 평균을 계산하여 각 열의 평균값을 얻음
feature_means = np.mean(data_matrix, axis=0) # shape: (3,)
print(f"Feature means: {feature_means}, shape: {feature_means.shape}")
# [12.5 22.5 32.5]

# 각 특성(열)별 표준편차 계산
feature_stds = np.std(data_matrix, axis=0) # shape: (3,)
print(f"Feature stds: {feature_stds}, shape: {feature_stds.shape}")
# [1.92028646 1.92028646 2.5]

# 정규화: (X - mu) / sigma
# data_matrix (4, 3) - feature_means (3,) -> (4, 3)으로 브로드캐스팅
normalized_data = (data_matrix - feature_means) / feature_stds
print(f"Normalized data:\n{normalized_data}")
# [[-1.30189914 -1.30189914 -0.99999999]
#  [-0.26037983 -0.26037983  0.2       ]
#  [ 1.30189914  1.30189914  1.4       ]
#  [ 0.26037983  0.26037983 -0.6       ]]

# 만약 평균과 표준편차를 행 벡터 (1, D) 형태로 사용하고 싶었다면,
# np.newaxis를 이용해 명시적으로 차원을 추가할 수 있습니다.
feature_means_row = feature_means[np.newaxis, :] # shape: (1, 3)
feature_stds_row = feature_stds[np.newaxis, :]   # shape: (1, 3)

normalized_data_explicit = (data_matrix - feature_means_row) / feature_stds_row
print(f"Normalized data (explicit row vector):\n{normalized_data_explicit}")
# 위와 동일한 결과. 이 경우 1차원 배열 (3,)이 자동으로 (1,3)처럼 동작했기 때문.
# 하지만 np.newaxis를 사용하면 의도를 더 명확히 할 수 있음.
```

### 시험 포인트
*   ⭐**브로드캐스팅 규칙의 정확한 이해**: 두 배열의 차원을 비교할 때, 뒤에서부터 차례대로 비교하며, 두 차원이 같거나 둘 중 하나가 1인 경우에만 브로드캐스팅이 가능합니다. 이 규칙을 벗어나면 `ValueError: operands could not be broadcast together` 오류가 발생합니다.
*   ⭐**`배열.shape`의 활용**: 브로드캐스팅 오류를 디버깅하거나 의도치 않은 확장을 방지하기 위해 연산 전후 배열의 `shape`을 항상 확인하는 습관을 들이는 것이 중요합니다.
*   ⭐**`np.newaxis`의 역할**: 1차원 배열을 행 벡터(`arr[np.newaxis, :]`)나 열 벡터(`arr[:, np.newaxis]`)로 명시적으로 변환하여 브로드캐스팅의 의도를 명확히 하고 잠재적인 오류를 방지하는 방법을 숙지해야 합니다. `op2`와 `op2.T`가 결과에 미치는 영향은 `op2`가 1차원 벡터인지, 2차원 이상의 배열인지에 따라 달라진다는 점을 이해해야 합니다. 특히 1차원 배열의 경우 `.T` 속성은 아무런 변화를 주지 않습니다.
*   ⭐**1차원 배열의 브로드캐스팅 함정**: 1차원 배열 (`(N,)` 형태)이 다른 배열과 연산될 때, NumPy는 암묵적으로 1차원 배열을 다른 배열의 마지막 차원에 맞춰 브로드캐스팅합니다. 이는 편리하지만, 2차원 배열의 행/열 벡터(`(1, N)` 또는 `(N, 1)`)와 혼동되어 의도치 않은 결과를 낼 수 있으므로 주의해야 합니다.

---
## Slide 75

**핵심 개념**
*   **Pairwise Distances (쌍별 거리)**: 주어진 점들의 집합 내에서 모든 가능한 점 쌍 사이의 거리를 계산하는 것을 의미합니다. 데이터 분석에서 유사성 또는 비유사성을 측정하는 데 필수적인 연산입니다.
*   **NumPy Broadcasting (브로드캐스팅)**: NumPy 배열 연산 시, 서로 다른 형태(shape)를 가진 배열들이 자동으로 확장(broadcast)되어 연산이 가능하도록 하는 강력한 기능입니다. 이를 통해 명시적인 반복문(for-loop) 없이 효율적이고 간결하게 배열 연산을 수행할 수 있습니다.
*   **`np.newaxis`**: 배열에 새로운 차원을 추가하는 데 사용되는 특별한 인덱싱 객체입니다. `(N,)` 형태의 1차원 배열을 `(N, 1)` 형태의 2차원 배열로 만들거나, `(N, M)` 형태의 배열을 `(N, 1, M)` 또는 `(1, N, M)` 형태로 만들어 브로드캐스팅을 위한 사전 준비를 할 때 유용하게 쓰입니다.

**코드/수식 해설**

*   **초기 점(Points) 정의**: 2차원 공간($R^2$)에 세 개의 점을 정의합니다. 각 행이 하나의 점 $(x, y)$을 나타냅니다.
    ```python
    import numpy as np

    # Points in R^2
    P = np.array([[0.0, 0.0],  # P_0
                  [1.0, 0.0],  # P_1
                  [0.0, 1.0]]) # P_2
    # P의 shape: (3, 2) (3개의 점, 각 점은 2개의 좌표)
    ```

*   **브로드캐스팅을 이용한 점 벡터 간 차이 계산**: `diff` 배열은 모든 점 쌍 $(P_i, P_j)$에 대한 벡터 차이 $P_i - P_j$를 저장합니다. `np.newaxis`를 사용하여 배열의 차원을 확장한 후 브로드캐스팅을 통해 효율적으로 계산합니다.
    ```python
    # P[:, np.newaxis, :] 의 shape: (3, 1, 2)
    # P[np.newaxis, :, :] 의 shape: (1, 3, 2)
    # 브로드캐스팅 규칙에 따라 두 배열은 (3, 3, 2) 형태로 확장되어 빼기 연산 수행.
    diff = P[:, np.newaxis, :] - P[np.newaxis, :, :] # shape (3, 3, 2)
    ```
    *   `P[:, np.newaxis, :]`는 `P`의 각 행(점)을 새로운 중간 차원에 위치시킵니다. `(3, 2)` -> `(3, 1, 2)`
    *   `P[np.newaxis, :, :]`는 `P`의 전체를 새로운 첫 번째 차원에 위치시킵니다. `(3, 2)` -> `(1, 3, 2)`
    *   이 두 배열을 빼면, 첫 번째 차원은 `P_i` 인덱스, 두 번째 차원은 `P_j` 인덱스, 세 번째 차원은 좌표(x, y)를 나타내는 `(3, 3, 2)` 형태의 `diff` 배열이 생성됩니다. `diff[i, j, k]`는 $P_i$의 $k$-번째 좌표에서 $P_j$의 $k$-번째 좌표를 뺀 값이 됩니다.

*   **유클리드 거리 행렬 계산**: `diff` 배열을 이용하여 모든 점 쌍 간의 유클리드 거리(Euclidean Distance)를 계산하고 `D` 행렬에 저장합니다.
    ```python
    D = np.sqrt((diff ** 2).sum(axis=2)) # shape (3, 3)
    print(D)
    ```
    두 점 $P_i = (x_i, y_i)$와 $P_j = (x_j, y_j)$ 사이의 유클리드 거리는 다음 수식으로 표현됩니다.
    $$D_{ij} = \|P_i - P_j\|_2 = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}$$
    일반적인 $N$차원 벡터의 경우:
    $$D_{ij} = \|P_i - P_j\|_2 = \sqrt{\sum_{k=1}^{N} (P_{ik} - P_{jk})^2}$$
    코드의 각 단계는 이 수식에 대응됩니다:
    *   `diff ** 2`: 각 좌표별 차이를 제곱합니다. $(P_{ik} - P_{jk})^2$
    *   `.sum(axis=2)`: 마지막 축(axis=2, 즉 좌표 축)을 따라 합산합니다. $\sum_{k=1}^{N} (P_{ik} - P_{jk})^2$
    *   `np.sqrt(...)`: 합산 결과에 제곱근을 취합니다. $\sqrt{\sum_{k=1}^{N} (P_{ik} - P_{jk})^2}$

**구체적 예시**

주어진 점들은 다음과 같습니다:
$P_0 = (0.0, 0.0)$ (원점)
$P_1 = (1.0, 0.0)$ ($x축 위)
$P_2 = (0.0, 1.0)$ ($y축 위)

1.  **`diff` 배열 생성 과정**:
    *   $P_0 - P_1 = (0.0 - 1.0, 0.0 - 0.0) = (-1.0, 0.0)$
    *   $P_0 - P_2 = (0.0 - 0.0, 0.0 - 1.0) = (0.0, -1.0)$
    *   $P_1 - P_2 = (1.0 - 0.0, 0.0 - 1.0) = (1.0, -1.0)$
    ...이러한 모든 쌍의 차이가 `diff` 배열에 `(3, 3, 2)` 형태로 저장됩니다.

2.  **`D` (거리 행렬) 계산 과정**:
    *   $D_{00} = \text{거리}(P_0, P_0) = \sqrt{(0-0)^2 + (0-0)^2} = 0.0$
    *   $D_{01} = \text{거리}(P_0, P_1) = \sqrt{(0-1)^2 + (0-0)^2} = \sqrt{(-1)^2 + 0^2} = \sqrt{1} = 1.0$
    *   $D_{02} = \text{거리}(P_0, P_2) = \sqrt{(0-0)^2 + (0-1)^2} = \sqrt{0^2 + (-1)^2} = \sqrt{1} = 1.0$
    *   $D_{12} = \text{거리}(P_1, P_2) = \sqrt{(1-0)^2 + (0-1)^2} = \sqrt{1^2 + (-1)^2} = \sqrt{1+1} = \sqrt{2} \approx 1.41421356$

최종 출력 `D`는 다음과 같을 것입니다:
```
[[0.         1.         1.        ]
 [1.         0.         1.41421356]
 [1.         1.41421356 0.        ]]
```
이는 대칭 행렬이며, 대각선 원소는 자신과의 거리이므로 0입니다.

**시험 포인트**
*   ⭐ **NumPy Broadcasting의 원리 및 활용**: `np.newaxis`를 사용하여 배열의 차원을 확장하고, 서로 다른 형태의 배열이 어떻게 브로드캐스팅 규칙에 따라 연산되는지 정확히 이해하고 설명할 수 있어야 합니다. 특히, `(N, 1, D)`와 `(1, M, D)` 형태가 `(N, M, D)`로 확장되는 과정을 시뮬레이션할 수 있어야 합니다.
*   ⭐ **유클리드 거리 공식과 코드의 연관성**: 파이썬 코드가 유클리드 거리의 수학적 공식을 어떻게 구현했는지 각 코드 라인(`diff ** 2`, `.sum(axis=2)`, `np.sqrt`)과 수식의 부분이 연결되는지 설명할 수 있어야 합니다.
*   **`axis` 인자의 의미**: `sum(axis=2)`와 같이 `axis` 인자를 사용하는 것이 어떤 차원(축)을 따라 연산이 이루어지는지를 결정하는지 정확히 이해해야 합니다. 이 경우, 각 점의 x, y 좌표에 대한 합산이 이루어집니다.
*   **성능 이점**: 브로드캐스팅이 명시적인 반복문(for-loop)을 사용하는 것보다 대규모 데이터셋 처리 시 훨씬 효율적이라는 점을 알고 있어야 합니다. 이는 벡터화 연산의 핵심입니다.

---
## Slide 76

**핵심 개념**:
벡터화(Vectorization)는 데이터 처리 작업을 파이썬의 명시적인 반복문(for-loop) 대신, 전체 배열(array) 또는 벡터(vector)에 대해 한 번에 연산을 수행하는 방식입니다. NumPy와 같은 라이브러리에서 이 벡터화 기법을 사용하여 대규모 데이터 처리 성능을 극대화합니다. 슬라이드는 벡터화를 사용하는 세 가지 주요 이유를 제시합니다:
1.  **성능 향상 (Optimized C routines)**: 파이썬 루프에서 수행될 작업을 NumPy 내부의 고도로 최적화된 C 언어 루틴으로 옮겨 처리합니다. C 언어는 파이썬보다 훨씬 빠르게 동작하여 연산 속도가 비약적으로 향상됩니다.
2.  **오버헤드 감소 및 캐시 효율 (Fewer interpreter overheads and better cache locality)**: 파이썬 인터프리터가 반복적으로 호출되는 오버헤드를 줄이고, NumPy 배열의 데이터가 메모리에 연속적으로 저장되어 CPU 캐시(Cache) 활용률이 높아집니다. 이는 데이터를 빠르게 접근하고 처리하는 데 결정적인 역할을 합니다.
3.  **코드 명확성 및 간결성 (Clear, declarative code)**: 배열 대수(array algebra)에 직접 매핑되는 간결하고 선언적인 코드를 작성할 수 있게 하여, 코드의 가독성과 유지보수성을 크게 향상시킵니다.

**코드/수식 해설**:
파이썬 리스트의 원소를 루프를 사용하여 더하는 방식과 NumPy 배열을 사용하여 벡터화된 덧셈을 수행하는 방식을 비교해 봅시다.

**파이썬 루프를 사용한 덧셈 (비벡터화)**
```python
import time

list1 = list(range(1000000))
list2 = list(range(1000000))
result_list = []

start_time = time.time()
for i in range(len(list1)):
    result_list.append(list1[i] + list2[i])
end_time = time.time()
print(f"Python loop time: {end_time - start_time:.4f} seconds")
```

**NumPy 벡터화를 사용한 덧셈**
```python
import numpy as np
import time

array1 = np.arange(1000000)
array2 = np.arange(1000000)

start_time = time.time()
result_array = array1 + array2 # 벡터화된 연산
end_time = time.time()
print(f"NumPy vectorization time: {end_time - start_time:.4f} seconds")
```
위 예시에서 `array1 + array2`는 NumPy가 내부적으로 최적화된 C 루틴을 호출하여, 각 원소를 파이썬 루프 없이 한 번에 더하는 벡터화된 연산입니다. 실제 실행 시 NumPy 방식이 훨씬 빠름을 확인할 수 있습니다.

수식적으로 벡터화는 두 벡터 $A = [a_1, a_2, \dots, a_n]$와 $B = [b_1, b_2, \dots, b_n]$의 합을 다음과 같이 간결하게 표현하고 효율적으로 계산합니다. 이는 각 원소별 덧셈 $c_i = a_i + b_i$를 의미하지만, 연산 지시는 한 번에 이루어집니다.

$$ C = \begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{bmatrix} + \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{bmatrix} = \begin{bmatrix} a_1+b_1 \\ a_2+b_2 \\ \vdots \\ a_n+b_n \end{bmatrix} $$

**구체적 예시**:
데이터 분석 시 수백만 개의 데이터 포인트를 처리해야 할 때 벡터화의 중요성은 더욱 커집니다. 예를 들어, 100만 개의 주택 가격 데이터가 있고, 각 가격에 대해 세금 5%를 계산한 후 10만원의 고정 수수료를 더하는 작업을 수행한다고 가정해 봅시다.
*   **비벡터화 방식 (Python list)**: `for` 루프를 사용하여 100만 개의 주택 가격을 하나씩 가져와 `price * 0.05 + 100000`를 계산하고 새로운 리스트에 저장합니다. 이 과정에서 100만 번의 루프 반복과 파이썬 인터프리터의 오버헤드가 발생합니다.
*   **벡터화 방식 (NumPy array)**: 모든 주택 가격을 NumPy 배열로 저장한 후, `tax_due = prices_array * 0.05 + 100000`과 같은 연산을 한 번에 적용합니다. NumPy는 이 연산을 내부적으로 최적화된 C 루틴으로 빠르게 처리하며, 결과 역시 NumPy 배열로 즉시 반환됩니다.

이것은 마치 한 사람의 요리사가 주문이 들어올 때마다 한 접시씩 요리하는 것(Python 루프)과, 대규모 공장에서 모든 재료를 한 번에 처리하고 대량 생산하는 자동화된 시스템(NumPy 벡터화)의 차이와 같습니다. 자동화된 시스템이 훨씬 빠르고 효율적이며, 대량의 데이터를 일관성 있게 처리하는 데 유리합니다.

**시험 포인트**:
*   ⭐ **벡터화의 정의 및 주요 이점**: 왜 데이터 분석에서 벡터화가 필수적이며, 세 가지 핵심 이점(C routines, interpreter overhead/cache locality, code clarity)을 정확히 설명할 수 있어야 합니다.
*   ⭐ **NumPy가 벡터화를 통해 성능을 향상시키는 원리**: NumPy가 어떻게 파이썬의 단점(느린 루프)을 극복하고 고성능 연산을 제공하는지 설명할 수 있어야 합니다. (예: C 언어 기반의 내부 구현, 연속적인 메모리 할당을 통한 캐시 효율성)
*   파이썬 루프와 NumPy 벡터화 연산 간의 성능 차이를 이해하고, 간단한 연산(예: 배열 덧셈, 스칼라 곱셈)에 대한 코드 예시를 통해 설명할 수 있어야 합니다.
*   데이터 분석 및 머신러닝 알고리즘 구현 시 벡터화가 코드의 간결성과 연산 효율성에 미치는 영향을 인지해야 합니다.

---
## Slide 77

## Cartesian Grid와 Route-Style 거리 행렬 (Distance Matrix)

### 핵심 개념

*   **카테시안 그리드 (Cartesian Grid) 구성**: 1차원 좌표 배열들을 이용하여 2차원 그리드 형태의 `X`와 `Y` 좌표 행렬을 구성하는 방식입니다. 이는 주로 NumPy의 브로드캐스팅(broadcasting) 기능을 통해 효율적으로 구현됩니다.
    *   예를 들어, x-좌표들을 담은 1차원 배열과 y-좌표들을 담은 1차원 배열이 있을 때, 이들을 각각 특정 차원으로 확장하여 서로 빼거나 더하는 연산을 통해 모든 가능한 점 쌍에 대한 x-좌표 차이 또는 y-좌표 차이를 포함하는 2차원 행렬을 생성할 수 있습니다.
*   **거리 행렬 (Distance Matrix)**: 주어진 여러 위치(점)들의 모든 쌍에 대해 거리를 계산하여 저장한 행렬입니다. 각 원소 $d_{ij}$는 $i$번째 점과 $j$번째 점 사이의 거리를 나타냅니다.
*   **브로드캐스팅 (Broadcasting)의 중요성**: NumPy의 브로드캐스팅은 명시적인 중첩(nested) Python `for` 루프 없이도 배열 간의 연산을 가능하게 하여 코드의 간결성, 가독성, 그리고 무엇보다 **성능**을 크게 향상시킵니다. 데이터 분석 및 머신러닝에서 대량의 데이터를 처리할 때 매우 중요한 기법입니다.

### 코드/수식 해설

**유클리드 거리 (Euclidean Distance) 수식**:
두 점 $(x_i, y_i)$와 $(x_j, y_j)$ 사이의 유클리드 거리 $d_{ij}$는 다음과 같이 계산됩니다.

$$
d_{ij} = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}
$$

### 구체적 예시

주어진 점들의 집합에 대해 모든 쌍 간의 유클리드 거리를 계산하여 거리 행렬을 만드는 NumPy 브로드캐스팅 예시입니다.

```python
import numpy as np

# 3개의 2차원 점 (좌표)
points = np.array([[1, 2],
                   [4, 6],
                   [0, 3]])

# x-좌표와 y-좌표를 분리
x_coords = points[:, 0] # [1, 4, 0]
y_coords = points[:, 1] # [2, 6, 3]

# 브로드캐스팅을 위한 차원 확장
# x_coords[:, np.newaxis] -> [[1], [4], [0]] (3, 1) 형태
# x_coords[np.newaxis, :] -> [[1, 4, 0]] (1, 3) 형태
# x_diffs[i, j]는 i번째 점의 x좌표와 j번째 점의 x좌표 차이
x_diffs = x_coords[:, np.newaxis] - x_coords[np.newaxis, :]
y_diffs = y_coords[:, np.newaxis] - y_coords[np.newaxis, :]

# 유클리드 거리 계산
distance_matrix = np.sqrt(x_diffs**2 + y_diffs**2)

print("원본 점들:\n", points)
print("\nx-좌표 차이 행렬 (x_diffs):\n", x_diffs)
print("\ny-좌표 차이 행렬 (y_diffs):\n", y_diffs)
print("\n거리 행렬 (distance_matrix):\n", distance_matrix)
```

**예시 결과 해석**:
`x_diffs` 행렬의 `(i, j)`번째 원소는 `points[i]`의 x좌표와 `points[j]`의 x좌표 간의 차이입니다. 마찬가지로 `y_diffs`도 동일하게 구성됩니다. 이 두 행렬을 제곱하고 더한 후 제곱근을 취하면 모든 점 쌍 간의 유클리드 거리를 포함하는 `distance_matrix`가 완성됩니다.
예를 들어, `distance_matrix[0, 1]`은 `points[0]` (1, 2)와 `points[1]` (4, 6) 사이의 거리 $\sqrt{(1-4)^2 + (2-6)^2} = \sqrt{(-3)^2 + (-4)^2} = \sqrt{9+16} = \sqrt{25} = 5.0$ 입니다.

### 시험 포인트

*   ⭐ **브로드캐스팅의 개념과 장점**: 브로드캐스팅이 무엇이며, 왜 중첩 루프 대신 사용하는 것이 효율적인지 설명할 수 있어야 합니다. (성능, 코드 간결성, 가독성)
*   ⭐ **거리 행렬 구성 원리**: 유클리드 거리 공식을 사용하여 거리 행렬의 특정 원소 값을 직접 계산할 수 있어야 합니다.
*   ⭐ **`np.newaxis` 또는 `None`을 이용한 차원 확장**: 브로드캐스팅을 위해 배열의 차원을 조작하는 방법을 이해하고 실제 코드에 적용할 수 있는지 묻는 문제가 나올 수 있습니다. 예를 들어, `(N,)` 형태의 배열을 `(N, 1)` 또는 `(1, N)` 형태로 바꾸는 방법.
*   카테시안 그리드 구성 시 `X`와 `Y` 좌표를 만드는 과정에서 브로드캐스팅이 어떻게 활용되는지 (예: `meshgrid`의 내부 동작) 이해하는 것이 중요합니다.

---
## Slide 78

**핵심 개념**

*   **NumPy 브로드캐스팅(Broadcasting)**: NumPy 배열 연산 시, 서로 다른 형태(shape)의 배열을 연산할 때 자동으로 형태를 맞춰주는 메커니즘입니다. 차원이 확장되거나 특정 차원이 1인 경우 다른 배열의 해당 차원에 맞춰 반복됩니다. `np.newaxis`는 배열에 새로운 차원(길이 1인)을 추가하여 브로드캐스팅을 위한 형태를 만드는 데 사용됩니다.
*   **거리 행렬 (Distance Matrix)**: 주어진 점들의 집합 내에서 모든 가능한 점 쌍 간의 거리를 계산하여 저장하는 행렬입니다. `D[i, j]`는 `i`번째 점과 `j`번째 점 사이의 거리를 나타냅니다.
*   **Manhattan 거리 (L1 Norm)**: 두 점 $P_1(x_1, y_1)$과 $P_2(x_2, y_2)$ 사이의 거리로, 각 좌표축을 따라 이동한 거리의 절댓값 합입니다. 도시의 블록을 따라 이동하는 경로에 비유하여 '택시 거리(Taxicab distance)'라고도 합니다.
*   **Euclidean 거리 (L2 Norm)**: 두 점 $P_1(x_1, y_1)$과 $P_2(x_2, y_2)$ 사이의 가장 짧은 직선 거리입니다. 피타고라스 정리를 확장한 개념입니다.

---

**코드/수식 해설**

```python
xs = np.array([0.0, 1.0, 2.0, 3.0])
ys = np.array([0.0, 1.0, 2.0])
```
*   `xs`: x좌표들을 담는 1차원 NumPy 배열 (shape: `(4,)`)
*   `ys`: y좌표들을 담는 1차원 NumPy 배열 (shape: `(3,)`)

```python
X = xs[np.newaxis, :]  # shape (1, 4)
Y = ys[:, np.newaxis]  # shape (3, 1)
```
*   `X`: `xs` 배열에 `np.newaxis`를 사용하여 첫 번째 차원을 확장합니다. `(4,)` 형태가 `(1, 4)` 형태로 변경됩니다. 이는 `xs`의 각 원소를 하나의 '행'으로 간주하여 다른 배열과 '열' 방향으로 브로드캐스팅하기 위함입니다.
*   `Y`: `ys` 배열에 `np.newaxis`를 사용하여 두 번째 차원을 확장합니다. `(3,)` 형태가 `(3, 1)` 형태로 변경됩니다. 이는 `ys`의 각 원소를 하나의 '열'로 간주하여 다른 배열과 '행' 방향으로 브로드캐스팅하기 위함입니다.

```python
# Manhattan distances on the grid as an example
D1 = np.abs(X - X.T) + np.abs(Y - Y.T)  # shape (3, 3) via broadcasting (comment in slide)
```
*   `X - X.T`:
    *   `X`의 shape는 `(1, 4)`입니다.
    *   `X.T` (X의 전치)의 shape는 `(4, 1)`입니다.
    *   이 두 배열을 빼면 브로드캐스팅 규칙에 따라 `(4, 4)` 형태의 배열이 생성됩니다. 결과 `(X - X.T)[i, j]`는 `X[0, j] - X.T[i, 0]` 즉 `xs[j] - xs[i]`가 됩니다.
    *   `np.abs(X - X.T)`는 모든 x좌표 쌍의 절댓값 차이 `|xs[j] - xs[i]|`를 담는 `(4, 4)` 행렬을 만듭니다.
*   `Y - Y.T`:
    *   `Y`의 shape는 `(3, 1)`입니다.
    *   `Y.T` (Y의 전치)의 shape는 `(1, 3)`입니다.
    *   이 두 배열을 빼면 브로드캐스팅 규칙에 따라 `(3, 3)` 형태의 배열이 생성됩니다. 결과 `(Y - Y.T)[i, j]`는 `Y[i, 0] - Y.T[0, j]` 즉 `ys[i] - ys[j]`가 됩니다.
    *   `np.abs(Y - Y.T)`는 모든 y좌표 쌍의 절댓값 차이 `|ys[i] - ys[j]|`를 담는 `(3, 3)` 행렬을 만듭니다.
*   `D1 = ... + ...`: `np.abs(X - X.T)` 결과 (shape `(4, 4)`)와 `np.abs(Y - Y.T)` 결과 (shape `(3, 3)`)를 직접 더하는 것은 **NumPy 브로드캐스팅 규칙에 따라 불가능하며 `ValueError: operands could not be broadcast together` 오류를 발생시킵니다.** 슬라이드의 주석 `# shape (3, 3)`은 `np.abs(Y - Y.T)`의 결과만을 지칭하거나, 코드의 의도가 현재 표현과 다를 수 있습니다.
*   **Manhattan 거리 수식**: 두 점 $(x_i, y_i)$와 $(x_j, y_j)$ 사이의 Manhattan 거리는 다음과 같습니다.
    $$D_M((x_i, y_i), (x_j, y_j)) = |x_i - x_j| + |y_i - y_j|$$

```python
# Euclidean distances between arbitrary points
P = np.stack([xs, np.linspace(0.0, 3.0, 4)], axis=1)  # shape (4, 2)
```
*   `np.linspace(0.0, 3.0, 4)`: 0.0부터 3.0까지 4개의 균일한 간격의 값을 생성합니다. `[0.0, 1.0, 2.0, 3.0]` (shape: `(4,)`).
*   `np.stack([xs, ...], axis=1)`: `xs`와 `np.linspace(...)`로 생성된 두 1차원 배열을 `axis=1`을 따라 쌓습니다. 결과 `P`는 `[[0.0, 0.0], [1.0, 1.0], [2.0, 2.0], [3.0, 3.0]]` 형태의 `(4, 2)` 2차원 배열이 됩니다. `P[i]`는 $i$번째 2차원 점 $(x, y)$를 나타냅니다.

```python
diff = P[:, np.newaxis, :] - P[np.newaxis, :, :]
```
*   이것은 `P`에 있는 모든 점 쌍 간의 차이 벡터를 계산하는 일반적인 패턴입니다.
*   `P[:, np.newaxis, :]`: `P` (shape `(4, 2)`)를 `(4, 1, 2)` 형태로 확장합니다. 각 행 `P[i, :]`가 `P[i, np.newaxis, :]`가 됩니다.
*   `P[np.newaxis, :, :]`: `P` (shape `(4, 2)`)를 `(1, 4, 2)` 형태로 확장합니다. 각 행 `P[j, :]`가 `P[np.newaxis, j, :]`가 됩니다.
*   `diff = (4, 1, 2) - (1, 4, 2)`: 브로드캐스팅을 통해 `(4, 4, 2)` 형태의 배열이 생성됩니다. `diff[i, j, k]`는 $P_{i,k} - P_{j,k}$ (즉, $i$번째 점의 $k$번째 좌표와 $j$번째 점의 $k$번째 좌표의 차이)를 의미합니다.

```python
D2 = np.sqrt((diff ** 2).sum(axis=2))
```
*   `diff ** 2`: `diff` 배열의 모든 원소를 제곱합니다. shape는 `(4, 4, 2)` 그대로 유지됩니다. `(x_i - x_j)^2`와 `(y_i - y_j)^2`를 계산합니다.
*   `.sum(axis=2)`: `diff ** 2`의 마지막 축(axis=2, 즉 좌표 차원)을 따라 합산합니다. `(x_i - x_j)^2 + (y_i - y_j)^2`와 같은 형태로, 각 점 쌍에 대한 제곱 차이의 합이 계산됩니다. 결과 shape는 `(4, 4)`가 됩니다.
*   `np.sqrt(...)`: `sum` 결과에 제곱근을 취하여 최종적으로 각 점 쌍 간의 유클리디안 거리를 계산합니다. `D2[i, j]`는 `P[i]`와 `P[j]` 사이의 유클리디안 거리입니다.
*   **Euclidean 거리 수식**: 두 점 $(x_i, y_i)$와 $(x_j, y_j)$ 사이의 Euclidean 거리는 다음과 같습니다.
    $$D_E((x_i, y_i), (x_j, y_j)) = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}$$

```python
print(D1.shape, D2.shape)
```
*   앞서 설명했듯, `D1` 계산은 `ValueError`를 발생시키므로, 이 `print` 문은 정상적으로 실행되지 않습니다. 만약 `D1`이 정상적으로 계산되었다고 가정하거나, `np.abs(Y - Y.T)`만을 `D1`로 간주한다면 `D1.shape`는 `(3, 3)`일 것이고, `D2.shape`는 `(4, 4)`입니다.

---

**구체적 예시**

*   **`np.newaxis`의 효과**:
    *   `xs`는 `[0., 1., 2., 3.]` (shape `(4,)`)
    *   `X = xs[np.newaxis, :]`는 `[[0., 1., 2., 3.]]` (shape `(1, 4)`)
    *   `ys`는 `[0., 1., 2.]` (shape `(3,)`)
    *   `Y = ys[:, np.newaxis]`는 `[[0.], [1.], [2.]]` (shape `(3, 1)`)
    이처럼 1차원 배열에 새로운 차원을 추가하여 2차원 배열처럼 보이게 만들고, 이를 통해 브로드캐스팅이 가능해집니다.

*   **`diff` (Euclidean 거리 계산)의 브로드캐스팅**:
    *   `P` (shape `(4, 2)`)의 각 점은 `[[x0, y0], [x1, y1], [x2, y2], [x3, y3]]`입니다.
    *   `P[:, np.newaxis, :]`는 `P`를 `(4, 1, 2)` 형태로 만듭니다. 각 `P[i, :]` (예: `[x0, y0]`)가 `[[x0, y0]]` (길이 1인 중간 차원이 추가됨)처럼 확장됩니다.
    *   `P[np.newaxis, :, :]`는 `P`를 `(1, 4, 2)` 형태로 만듭니다. `P` 전체가 `P` 앞에 길이 1인 차원이 추가됩니다.
    *   이 둘을 빼면 `(4, 1, 2)`와 `(1, 4, 2)`가 브로드캐스팅되어 `(4, 4, 2)` 형태의 `diff` 배열이 됩니다.
        *   `diff[0, 1, 0]`는 `P[0, 0] - P[1, 0]` (즉, $x_0 - x_1$)
        *   `diff[0, 1, 1]`는 `P[0, 1] - P[1, 1]` (즉, $y_0 - y_1$)
    *   이렇게 `diff[i, j, :]`는 `P[i]`와 `P[j]` 두 점 사이의 $(x, y)$ 좌표 차이 벡터가 됩니다.

*   **`sum(axis=2)`의 의미**:
    *   `diff ** 2`의 `diff[i, j, :]`는 `[(x_i - x_j)^2, (y_i - y_j)^2]` 형태입니다.
    *   여기에 `sum(axis=2)`를 적용하면, 이 벡터의 마지막 차원(인덱스 2)에 있는 원소들을 합산합니다. 즉, `(x_i - x_j)^2 + (y_i - y_j)^2`를 계산하게 됩니다. 이는 유클리디안 거리 공식의 제곱합 부분에 해당합니다.

---

**시험 포인트**

*   ⭐ **NumPy 브로드캐스팅**: `np.newaxis`를 사용하여 배열의 차원을 효과적으로 확장하고, 이를 통해 서로 다른 형태의 배열 간 연산을 수행하는 원리를 정확히 이해해야 합니다. 특히 `array[:, np.newaxis]`와 `array[np.newaxis, :]`의 차이점을 숙지하세요.
*   ⭐ **거리 행렬 계산 패턴**: 모든 점 쌍에 대한 차이 벡터를 계산하는 `diff = P[:, np.newaxis, :] - P[np.newaxis, :, :]`와 같은 브로드캐스팅 패턴은 머신러닝 및 데이터 분석에서 매우 중요하므로 반드시 익혀두세요.
*   ⭐ **Manhattan & Euclidean 거리**: 두 거리 공식의 차이점을 정확히 이해하고, 각 거리를 NumPy를 사용하여 효율적으로 계산하는 방법을 구현할 수 있어야 합니다.
*   ⭐ **`axis` 인자의 활용**: `sum()`, `mean()`, `max()` 등 NumPy 집계 함수에서 `axis` 인자가 어떤 차원을 따라 연산을 수행하는지 명확하게 이해하는 것이 중요합니다. 시각화하여 어떤 차원이 합쳐지는지 파악하는 연습을 하세요.

---
## Slide 79

# Debugging Friends

## 핵심 개념
본 슬라이드는 NumPy를 사용하여 데이터 분석 작업을 수행할 때 발생할 수 있는 오류를 줄이고 성능을 최적화하기 위한 모범 사례 및 디버깅 팁을 제시합니다. 주로 배열의 속성 확인, 브로드캐스팅 검증, 선형 대수 문제 해결 방법, 그리고 성능 향상을 위한 벡터화 및 메모리 복사 관리에 중점을 둡니다.

## 코드/수식 해설

1.  **`arr.shape` 및 `arr.dtype` 확인**:
    대규모 연산을 시작하기 전에 NumPy 배열의 차원(`shape`)과 데이터 타입(`dtype`)을 확인하여 예상치 못한 동작이나 오류를 방지합니다.

    ```python
    import numpy as np

    # 예시 배열 생성
    arr = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=np.float64)

    # shape 확인: 배열의 각 차원 크기를 튜플 형태로 반환
    print(f"Array shape: {arr.shape}")
    # Output: Array shape: (2, 3)

    # dtype 확인: 배열 요소의 데이터 타입을 반환
    print(f"Array dtype: {arr.dtype}")
    # Output: Array dtype: float64

    # 잘못된 dtype으로 연산 시도 (예: 정수형으로 부동소수점 저장)
    int_arr = np.array([1.1, 2.2], dtype=np.int32)
    print(f"Integer array: {int_arr}, dtype: {int_arr.dtype}")
    # Output: Integer array: [1 2], dtype: int32 (소수점 이하 버림)
    ```

2.  **작은 슬라이스 출력으로 브로드캐스팅 방향 검증**:
    NumPy의 브로드캐스팅은 편리하지만, 복잡한 상황에서는 예상과 다른 방식으로 동작할 수 있습니다. 이때는 전체 배열 대신 작은 부분 배열(slice)을 출력하여 브로드캐스팅이 의도한 대로 동작하는지 확인합니다.

    ```python
    import numpy as np

    # 서로 다른 shape의 배열 생성
    matrix = np.array([[1, 2, 3], [4, 5, 6]]) # shape (2, 3)
    vector = np.array([10, 20, 30])         # shape (3,)

    # 브로드캐스팅이 일어나는 연산
    result = matrix + vector
    print(f"Matrix + Vector:\n{result}")
    # Output:
    # Matrix + Vector:
    # [[11 22 33]
    #  [14 25 36]]

    # 브로드캐스팅 방향 검증을 위한 작은 슬라이스 출력
    print(f"\nMatrix first row slice: {matrix[0, :]}") # [1 2 3]
    print(f"Vector slice: {vector}")                     # [10 20 30]
    # (2,3) 행렬과 (3,) 벡터 연산 시, 벡터가 각 행에 맞춰 (1,3)으로 확장되어 연산됨을 시각적으로 확인
    ```

3.  **`np.linalg.solve` 사용 권장**:
    선형 방정식 $Ax=b$를 풀 때, 역행렬 $A^{-1}$을 명시적으로 계산하는($x=A^{-1}b$) 대신 `np.linalg.solve(A, b)` 함수를 사용하는 것이 수치적으로 더 안정적이고 효율적입니다.

    선형 방정식: $Ax = b$
    $A$: 계수 행렬, $x$: 미지수 벡터, $b$: 상수 벡터

    ```python
    import numpy as np

    # 계수 행렬 A와 상수 벡터 b 정의
    A = np.array([[3, 1], [1, 2]])
    b = np.array([9, 8])

    # 비권장: 역행렬을 직접 계산하는 방법
    # A_inv = np.linalg.inv(A)
    # x_inv = A_inv @ b
    # print(f"Solution via inverse: {x_inv}")

    # 권장: np.linalg.solve 사용 (더 안정적이고 효율적)
    x_solve = np.linalg.solve(A, b)
    print(f"Solution via np.linalg.solve: {x_solve}")
    # Output: Solution via np.linalg.solve: [2. 3.]
    # (x=2, y=3 이 해임: 3*2+1*3=9, 1*2+2*3=8)
    ```

4.  **벡터화된 표현 사용 및 불필요한 복사 방지**:
    성능이 중요한 상황에서는 파이썬 `for` 루프 대신 NumPy의 벡터화된 연산을 사용하여 속도를 향상시킵니다. 또한, 의도치 않은 메모리 복사를 피하여 메모리 사용 효율과 실행 시간을 최적화합니다.

    *   **벡터화된 연산 예시**:
        ```python
        import numpy as np
        import time

        arr = np.arange(1000000)

        # 벡터화된 연산 (매우 빠름)
        start_time = time.time()
        result_vec = arr * 2
        end_time = time.time()
        print(f"Vectorized operation time: {end_time - start_time:.6f} seconds")
        # Output: (예시) Vectorized operation time: 0.002123 seconds

        # 일반 파이썬 for 루프 (느림)
        start_time = time.time()
        result_loop = [x * 2 for x in arr]
        end_time = time.time()
        print(f"Loop operation time: {end_time - start_time:.6f} seconds")
        # Output: (예시) Loop operation time: 0.165432 seconds (수십 배 느림)
        ```
    *   **불필요한 복사 방지 예시**:
        ```python
        import numpy as np

        original_arr = np.arange(10)
        print(f"Original array: {original_arr}") # [0 1 2 3 4 5 6 7 8 9]

        # 슬라이싱은 기본적으로 '뷰(view)'를 반환 (원본 데이터의 참조)
        view = original_arr[::2] # 짝수 인덱스 요소만 선택
        print(f"View: {view}")    # [0 2 4 6 8]

        # 뷰를 수정하면 원본 배열도 변경됨
        view[0] = 99
        print(f"View after modification: {view}")       # [99  2  4  6  8]
        print(f"Original array after view modification: {original_arr}") # [99  1  2  3  4  5  6  7  8  9]

        # 명시적 복사 (원본 데이터와 독립적인 새로운 배열 생성)
        copy_arr = original_arr[::2].copy()
        print(f"\nCopied array: {copy_arr}") # [99  2  4  6  8] (이전 수정된 original_arr에서 복사)

        # 복사본을 수정해도 원본 배열은 변경되지 않음
        copy_arr[0] = 0
        print(f"Copied array after modification: {copy_arr}") # [0  2  4  6  8]
        print(f"Original array after copy modification: {original_arr}") # [99  1  2  3  4  5  6  7  8  9]
        ```

## 구체적 예시

*   **`shape` 및 `dtype` 확인**: 마치 건축가가 건물을 짓기 전에 설계 도면(shape)과 재료의 종류(dtype)를 확인하는 것과 같습니다. 잘못된 도면이나 재료로는 원하는 건물을 지을 수 없듯이, 잘못된 배열 속성으로는 원하는 계산 결과를 얻을 수 없습니다.
*   **브로드캐스팅 검증**: 두 개의 다른 크기 물통에 물을 채울 때, 작은 물통을 큰 물통에 직접 붓는 것이 아니라, 큰 물통의 각 칸에 맞춰 작은 물통의 내용물을 복사해서 채우는 것을 상상해 보세요. 이때 '어떤 물통이 어떻게 확장되어 채워지는가?'를 확인하는 것이 브로드캐스팅 방향 검증과 비슷합니다.
*   **`np.linalg.solve` 사용**: 연립방정식을 풀 때, 손으로 일일이 역행렬을 계산해서 곱하는 것보다 공학용 계산기나 특정 소프트웨어의 "해 찾기" 기능을 이용하는 것이 더 정확하고 빠르며, 오차 발생 위험이 적은 것과 같습니다. 특히 숫자가 복잡하거나 많을수록 전자의 방식은 실수를 유발하기 쉽습니다.
*   **벡터화 및 복사 방지**: 수백만 개의 전구를 동시에 켜거나 끌 때, 전구 하나하나의 스위치를 개별적으로 조작하는 것(for 루프)보다 중앙 제어 시스템으로 일괄적으로 명령하는 것(벡터화)이 훨씬 빠릅니다. 또한, 전구의 상태를 기록할 때 불필요하게 모든 전구의 상태를 매번 복사해서 저장하는 대신, 변경된 부분만 참조하여 기록하는 것이 효율적인 것과 유사합니다.

## 시험 포인트

*   ⭐**`arr.shape`과 `arr.dtype` 확인은 NumPy 연산의 가장 기본적인 디버깅 습관이자 성능 문제 해결의 첫걸음입니다.**
*   ⭐**브로드캐스팅은 편리하지만 복잡한 연산에서는 예측하기 어려울 수 있으므로, 작은 슬라이스를 출력하여 연산 방향을 검증하는 것이 매우 중요합니다.**
*   ⭐**선형 시스템 $Ax=b$를 풀 때 `np.linalg.solve`는 역행렬을 명시적으로 계산하는 것보다 수치적으로 더 안정적이고 효율적입니다.** 특히 대규모 행렬이나 조건이 나쁜(ill-conditioned) 행렬에 대한 연산에서 그 중요성이 더욱 부각됩니다.
*   ⭐**NumPy에서 고성능을 얻기 위한 핵심은 벡터화된 연산을 활용하는 것이며, 불필요한 메모리 복사는 성능 저하의 주범이 될 수 있으므로 주의해야 합니다.** 이는 특히 대규모 데이터셋 처리 시 **성능 병목 지점**으로 작용할 수 있습니다.

---
## Slide 80

---

### Key Takeaways (NumPy Essentials)

#### 1. `shape`과 `dtype` 이해의 중요성

*   **핵심 개념**: NumPy 배열의 `shape` (차원 및 각 차원의 크기)와 `dtype` (배열 요소의 데이터 타입)은 연산의 **정확성(correctness)**과 **속도(speed)**를 결정하는 핵심 요소입니다.
*   **코드/수식 해설**:
    *   `shape`: 배열이 몇 개의 차원을 가지며, 각 차원에 몇 개의 요소가 있는지 나타냅니다. 예를 들어, `(3, 4)`는 3행 4열의 2차원 배열을 의미합니다.
    *   `dtype`: 배열 내 모든 요소가 저장되는 방식을 정의합니다 (예: `int32`, `float64`, `bool`). 적절한 `dtype`을 사용하면 메모리 사용을 최적화하고 연산 속도를 향상시킬 수 있습니다.
    ```python
    import numpy as np

    arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
    print(f"Shape: {arr.shape}") # Output: Shape: (2, 3)
    print(f"Dtype: {arr.dtype}") # Output: Dtype: float32

    # 잘못된 dtype 사용 예시: 오버플로우
    large_num_int8 = np.array([200], dtype=np.int8)
    print(f"Int8 with 200: {large_num_int8}") # Output: Int8 with 200: [-56] (오버플로우 발생)
    ```
*   **구체적 예시**:
    *   **정확성**: 행렬 곱셈 `np.dot(A, B)`에서 `A`의 열 수와 `B`의 행 수가 일치하지 않으면 `ValueError`가 발생합니다. 이는 `shape`의 중요성을 보여줍니다. 또한, 정수형 `dtype`으로 부동소수점 연산을 수행하면 소수점 이하가 잘려나가 정확도가 떨어질 수 있습니다.
    *   **속도**: `float32`를 사용하는 것이 `float64`를 사용하는 것보다 메모리 사용량이 절반이고, 특정 환경에서는 연산 속도도 더 빠를 수 있습니다. 특히 대규모 데이터셋에서는 이러한 차이가 중요해집니다.
*   **시험 포인트**: ⭐ `shape`과 `dtype`이 NumPy 연산의 정확성과 성능에 미치는 영향에 대해 설명할 수 있어야 합니다.

#### 2. `np.newaxis` 또는 `np.expand_dims`를 이용한 브로드캐스팅

*   **핵심 개념**: 브로드캐스팅(broadcasting)은 서로 다른 형태(shape)를 가진 NumPy 배열 간에 연산을 가능하게 하는 강력한 기능입니다. 이때 `np.newaxis`나 `np.expand_dims`를 사용하여 차원을 명시적으로 확장하고 축(axis)을 정렬하는 것이 중요합니다.
*   **코드/수식 해설**:
    *   **브로드캐스팅 규칙**:
        1.  두 배열의 차원 수가 다르면, 차원 수가 적은 배열의 `shape` 앞쪽에 1을 추가하여 차원 수를 같게 만듭니다.
        2.  두 배열의 `shape`을 비교하여, 둘 중 어느 한 차원의 크기가 1이면 다른 차원의 크기에 맞춰 늘어납니다.
        3.  두 배열의 `shape`이 다르지만 위의 규칙으로 정렬되지 않으면 오류가 발생합니다.
    *   `np.newaxis`: 배열의 특정 위치에 새로운 차원(크기 1)을 추가합니다. 인덱싱 문법 내에서 사용됩니다.
    *   `np.expand_dims(arr, axis)`: 배열 `arr`의 지정된 `axis` 위치에 새로운 차원(크기 1)을 추가합니다.
    ```python
    import numpy as np

    a = np.array([1, 2, 3]) # shape: (3,)
    b = np.array([[10], [20], [30]]) # shape: (3, 1)

    # a를 (1, 3)으로 만들어 브로드캐스팅
    result_newaxis = a[np.newaxis, :] + b
    print(f"Using newaxis:\n{result_newaxis}")
    # Output:
    # Using newaxis:
    # [[11 12 13]
    #  [21 22 23]
    #  [31 32 33]]
    print(f"Shape after newaxis: {a[np.newaxis, :].shape}") # Output: Shape after newaxis: (1, 3)

    # np.expand_dims 사용 예시
    c = np.array([1, 2, 3]) # shape: (3,)
    c_expanded = np.expand_dims(c, axis=0) # shape: (1, 3)
    print(f"Using expand_dims:\n{c_expanded + b}")
    # Output:
    # Using expand_dims:
    # [[11 12 13]
    #  [21 22 23]
    #  [31 32 33]]
    ```
*   **구체적 예시**: 2차원 이미지 데이터(높이, 너비, 채널)에서 각 채널에 특정 편향(bias)을 더하는 경우를 생각해봅시다. 편향이 (채널 수,) 형태의 1차원 배열이라면, `image + bias[np.newaxis, np.newaxis, :]`와 같이 `newaxis`를 사용하여 편향 배열의 차원을 (1, 1, 채널 수)로 만들어 이미지 데이터의 각 픽셀에 올바르게 브로드캐스팅되도록 할 수 있습니다.
*   **시험 포인트**: ⭐ 브로드캐스팅의 개념을 설명하고, `np.newaxis` 또는 `np.expand_dims`를 사용하여 배열의 차원을 확장하고 브로드캐스팅을 제어하는 방법을 코드 예시와 함께 설명할 수 있어야 합니다.

#### 3. 벡터화 및 안정적인 선형대수 루틴 선호

*   **핵심 개념**: 파이썬의 `for` 루프 대신 NumPy의 **벡터화(vectorization)**된 연산을 사용하여 코드를 작성해야 합니다. 또한, 수치적으로 **안정적인(stable)** 선형대수 루틴을 활용하여 계산 오차를 최소화해야 합니다.
*   **코드/수식 해설**:
    *   **벡터화**: NumPy는 C/Fortran으로 구현된 효율적인 저수준 코드를 사용하여 배열 연산을 수행합니다. 이는 파이썬 `for` 루프보다 훨씬 빠릅니다. 예를 들어, 두 벡터의 내적(dot product)을 계산할 때:
        $$ \mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^{n} a_i b_i $$
        이를 `np.dot(a, b)` 또는 `a @ b`로 구현하는 것이 벡터화된 방식입니다.
    *   **안정적인 선형대수 루틴**: `np.linalg` 모듈의 함수들은 고성능 및 수치적 안정성을 위해 최적화되어 있습니다. 예를 들어, 선형 시스템 $Ax=b$를 풀 때, 행렬 `A`의 역행렬을 직접 계산하는 `np.linalg.inv(A) @ b`보다 `np.linalg.solve(A, b)`를 사용하는 것이 일반적으로 더 안정적이고 빠릅니다.
    ```python
    import numpy as np
    import time

    size = 1000

    # 벡터화된 연산
    a = np.random.rand(size)
    b = np.random.rand(size)

    start_time = time.time()
    c_vec = a * b
    end_time = time.time()
    print(f"Vectorized multiplication time: {end_time - start_time:.6f} seconds")

    # For 루프를 이용한 연산 (비교용)
    c_loop = np.zeros(size)
    start_time = time.time()
    for i in range(size):
        c_loop[i] = a[i] * b[i]
    end_time = time.time()
    print(f"Loop multiplication time: {end_time - start_time:.6f} seconds")

    # 선형대수 루틴 예시
    A = np.array([[2, 1], [1, 1]])
    b = np.array([4, 3])
    x = np.linalg.solve(A, b) # 역행렬 계산보다 안정적
    print(f"Solution x for Ax=b: {x}") # Output: Solution x for Ax=b: [1. 2.]
    ```
*   **구체적 예시**: 머신러닝에서 경사 하강법(Gradient Descent)을 구현할 때, 가중치 업데이트를 위해 행렬-벡터 곱셈을 자주 사용합니다. 이를 명시적인 `for` 루프 대신 `np.dot`이나 `@` 연산자를 사용하여 벡터화하면 수십 배 이상의 속도 향상을 얻을 수 있습니다.
*   **시험 포인트**: ⭐ 벡터화의 개념과 성능 이점, 그리고 수치적으로 안정적인 선형대수 루틴을 사용해야 하는 이유를 설명할 수 있어야 합니다.

#### 4. 작은 예시로 검증 후 확장

*   **핵심 개념**: 복잡한 연산이나 알고리즘을 구현할 때는 먼저 **작고 간단한 데이터셋(small examples)**으로 코드가 올바르게 작동하는지 철저히 검증한 후, 실제 **대규모 데이터(scale up)**에 적용해야 합니다.
*   **코드/수식 해설**: (특별한 코드/수식 없음. 개발 방법론에 가까운 개념)
*   **구체적 예시**:
    *   **데이터 전처리 파이프라인**: 대용량 이미지 데이터를 전처리하는 파이프라인을 구축할 때, 먼저 2~3장의 작은 이미지로 모든 변환(리사이징, 정규화, 증강 등)이 의도대로 동작하는지 확인합니다. 그 후에 수만 장의 전체 데이터셋에 적용합니다.
    *   **사용자 정의 함수**: 복잡한 통계량 계산 함수를 만들 때, 예측 가능한 출력값을 가진 몇 개의 간단한 입력값으로 함수를 테스트하여 논리적 오류가 없는지 확인합니다.
*   **시험 포인트**: ⭐ 데이터 분석 및 머신러닝 프로젝트 진행 시 "작은 예시로 검증 후 확장" 전략의 중요성과 그 이유(디버깅 용이성, 효율성 등)를 설명할 수 있어야 합니다.

---

---

