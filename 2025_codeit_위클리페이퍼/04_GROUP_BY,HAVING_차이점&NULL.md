# 위클리\_페이퍼\_04 : GROUP BY, HAVING & NULL

---

## GROUP BY

- 데이터를 특정 속성(컬럼) 기준으로 **그룹화** 하는 것
- `COUNT()`, `SUM()`, `AVG()`, `MAX()`, `MIN()` 등 집계함수와 함께 사용
- 그룹별로 요약된 결과를 출력

#### 기본 문법

```sql
SELECT
    컬럼1,
    집계함수(컬럼2)
FROM 테이블명
GROUP BY 컬럼1;
```

<br>

#### `GROUP BY` 예시

| region | amount |
| ------ | ------ |
| East   | 100    |
| West   | 200    |
| East   | 150    |
| West   | 100    |

```sql
-- 각 지역 별 매출 합계를 구하기
SELECT
    region,
    SUM(amount) AS total_sales
FROM sales
GROUP BY region;  -- GROUP BY로 나눠서 region 값으로 구분
```

#### 결과

| region | total_sales |
| ------ | ----------- |
| East   | 250         |
| West   | 300         |

<br>

### 주의할 점

- `GROUP BY`를 사용할 때 는 **SELECT 절에 있는 컬럼 중에서**  
  집계 함수가 아닌 컬럼은 반드시 `GROUP BY`에 포함되어야 함
- `GROUP BY`는 여러 컬럼을 기준으로 그룹화 가능 (`GROUP BY region, category` 등)

#### 다중 컬럼 그룹화 예시

| region | category | amount |
| ------ | -------- | ------ |
| East   | A        | 100    |
| East   | A        | 150    |
| East   | B        | 200    |
| West   | A        | 300    |
| West   | B        | 100    |

```sql
SELECT
    region,
    category,
    SUM(amount) AS total_sales
FROM sales
GROUP BY region, category;   -- 여러 컬럼을 사용하여 그룹화
```

#### 결과

| region | category | total_sales |
| ------ | -------- | ----------- |
| East   | A        | 250         |
| East   | B        | 200         |
| West   | A        | 300         |
| West   | B        | 100         |

조합이 같은 행들끼리 하나의 그룹으로 묶은 후 `SUM()` 하는 것

---

## HAVING

- 그룹화된 데이터의 조건을 걸기 위해 사용
- `WHERE`은 그룹화 전에 조건을 거는 것이고,
  `HAVING` 은 `GROUP BY`로 그룹화한 뒤 **집계 함수 결과에 조건을 거는 것**
- `WHERE`절 에서는 집계 함수를 사용할 수 없음

<br>

### 기본 문법

- `HAVING`은 아래와 같이 사용됨

```sql
SELECT 컬럼1, 집계함수(컬럼2), ...
FROM 테이블명
GROUP BY 컬럼1, 컬럼2, ...
HAVING 조건;
```

<br>

### `HAVING` 예시

❓지역별(`region`) 매출(`amount`) 합계가 **200을 넘는 지역만 보고 싶다.**

| region | category | amount |
| ------ | -------- | ------ |
| East   | A        | 100    |
| East   | A        | 150    |
| East   | B        | 200    |
| West   | A        | 300    |
| West   | B        | 100    |

```sql
SELECT
    region,
    category,
    SUM(amount) AS total_sales
FROM sales
GROUP BY region, category    -- 아까 본 다중 그룹화를 사용
HAVING SUM(amount) > 200;    -- 조건: amount 합계가 200보다 클 때 가져옴
```

#### 결과

| region | category | total_sales |
| ------ | -------- | ----------- |
| East   | A        | 250         |
| West   | A        | 300         |

보이는 것과 같이 조건에 충족된 값들만 가져옴.

<br>

### ✅ GROUP BY 와 HAVING 정리

| 구분         | 설명                                 | 적용 시점           | 역할                                   |
| ------------ | ------------------------------------ | ------------------- | -------------------------------------- |
| **GROUP BY** | 데이터를 특정 컬럼 기준으로 그룹화함 | 쿼리 실행 중간 단계 | 그룹을 나누고 집계 함수 적용 대상 설정 |
| **HAVING**   | 그룹화된 결과에 조건을 걸어 필터링함 | 그룹화 후           | 그룹별 집계 결과를 조건으로 필터링     |

### ✅ HAVING과 비슷한 기능들과 그 차이점

| 구문        | 사용 시점                   | 적용 대상           | 역할 및 특징                                                 | 지원 DBMS 및 비고                     |
| ----------- | --------------------------- | ------------------- | ------------------------------------------------------------ | ------------------------------------- |
| **HAVING**  | 그룹화 후 (GROUP BY 이후)   | 그룹(집계 결과)     | 그룹별 집계 결과에 조건을 걸어 필터링                        | 대부분 모든 DBMS 지원                 |
| **WHERE**   | 그룹화 전 (FROM, JOIN 이후) | 개별 행(row)        | 조건에 맞는 행을 필터링하여 그룹화 이전 단계에서 데이터 제한 | 대부분 모든 DBMS 지원                 |
| **FILTER**  | 집계 함수 내부              | 집계 함수의 입력 값 | 집계 함수 내에서 조건에 맞는 값만 집계에 포함시키는 역할     | PostgreSQL, Oracle 등 일부 DBMS 지원  |
| **QUALIFY** | 윈도우 함수 결과 이후       | 윈도우 함수 결과 행 | 윈도우 함수 결과를 조건으로 필터링                           | Snowflake, BigQuery 등 일부 DBMS 지원 |

---

## NULL

### NULL값 이란?

- 값이 **"없음"** 을 의미하는 특수한 상태
- 알 수 없거나 존재하지 않는 값을 의미
- `숫자 '0'`과 `빈 문자열("")`과는 다른 값

<br>

#### NULL의 특징

1. 값이 아예 없음: 입력되지 않았거나 정의되지 않는 상태
2. 0이나 빈 문자열이 아님: `0`, `' '`, `" "`들은 실제로 값이 있는 것이고, `NULL`은 값 자체가 없음을 뜻함
3. 연산 불가: `NULL + 5`, `NULL = NULL` 같은 연산은 결과가 `FALSE` 또는 `UNKNOWN`이 됨
4. 비교 불가: `NULL = NULL`은 `TRUE`가 아니라 `UNKNOWN`(따라서 `IS NULL`로 확인해야 함)
5. 조건문에서 주의 필요: `WHERE column = NULL`은 동작하지 않음 → `WHERE column IS NULL`을 사용해야 함.

#### 예시

| id  | name | age  |
| --- | ---- | ---- |
| 1   | Kim  | 25   |
| 2   | Lee  | NULL |
| 3   | Park | 30   |

- 여기서 Lee의 나이는 **입력되지 않았거나 모르는 상태** → `NULL`

---

## NULL을 다루는 문법들

### 데이터 베이스에서 NULL값을 다뤄야하는 이유가 뭘까?

**1. 현실의 불완전한 데이터를 표현**

- 어떤 값들은 아직 미정이거나 존재하지 않거나, 알수 없는 경우가 많음

<BR>

**2. 데이터 정확성과 무결성 유지**

- 없는 값을 0이나 빈 문자열로 대체하면 오해의 소지  
  예: `나이: 0`과 `나이: NULL`은 완전히 다름

- `NULL`은 "값이 아직 없음 또는 모름"을 정확하게 표현하는 방법

<BR>

**3. 통계 및 분석에서 제외 또는 구분 가능**

- 집계 함수가 NULL을 자동으로 제외 → 통계에 영향을 주지 않도록 설계 가능
- 조건문에서 NULL 여부로 데이터 필터링 가능

```sql
SELECT
    AVG(score)   -- 집계 함수 AVG()로 인해 NULL 점수는 제외됨
FROM students;
```

<BR>

**4. 조건 분기 처리에 유용**

- `COALESCE`, `IFNULL` 등을 통해 기본값 지정 가능
- `NULLIF`, `CASE`문을 이용해 의사결정 로직 구현 가능

```sql
SELECT
    COALESCE(email, '이메일 없음')  -- email 값이 NULL인 경우 '이메일 없음'으로 대체됨
FROM members;
```

<BR>

**5. JOIN 및 관계형 모델에서 유연성 제공**

- 외래 키가 아직 연결되지 않은 경우에도 `NULL`로 표현하여 관계 유지를 가능하게 함
- 복잡한 엔터티 간 관계를 표현할 때 필수적

<BR>

#### 정리

| 이유          | 설명                            |
| ------------- | ------------------------------- |
| 현실 표현     | 입력 안 된 값, 모르는 값 표현   |
| 데이터 정확성 | 값이 없는 것과 0을 구분         |
| 분석 유용성   | NULL 제외한 통계 처리 가능      |
| 조건 분기     | 대체값 지정, 의사결정 로직 구현 |
| 관계 모델     | 외래 키 등에서 유연성 확보      |

---

## NULL 처리 함수들

**1. COALESCE(값1, 값2, ...)**

- **NULL이 아닌 첫 번째 값** 반환
- 다양한 대체값 우선순위 설정 가능

```sql
SELECT
    name,
    COALESCE(age, '정보 없음') AS age  -- '정보 없음'으로 대체
FROM users;
```

<br>

**2. IFNULL(값, 대체값)**
(※ MySQL에서 사용)

- **값이 NULL이면 대체값 반환**

```sql
SELECT
    name,
    IFNULL(age, '정보 없음') AS age -- '정보 없음'으로 대체
FROM users;
```

<br>

**3. NULLIF(값1, 값2)**

- 두 값이 같으면 **NULL 반환**, **다르면 첫 번째 값 반환**

```sql
SELECT
    NULLIF(grade, 0) -- grade가 0이면 NULL, 아니면 grade 값 반환
FROM scores;
```

<br>

**4. IS NULL (IS NOT NULL)**
(※ MySQL에서 사용)

- **값이 NULL인지 확인하는 조건식**
- 직접 **비교 연산자**(**=** NULL)는 **절대 사용 불가**

```sql
-- 이메일이 없는 회원 찾기
SELECT *
FROM members
WHERE email IS NULL;  -- 값이 NULL인 회원이 결과로 출력
```

```sql
-- 이메일이 있는 회원만 조회
SELECT *
FROM members
WHERE email IS NOT NULL;  -- 값이 NULL이 아닌 회원이 결과로 출력
```

<br>

_4-1. ISNULL(값)_
_(SQL Server 전용)_

- NULL이면 1, 아니면 0 반환

```sql
SELECT
    ISNULL(age) -- 0 or 1반환
FROM users;
```

<br>

#### 함수 정리

| 기능                    | 문법                           |
| ----------------------- | ------------------------------ |
| NULL 확인               | `IS NULL`, `IS NOT NULL`       |
| NULL을 다른 값으로 대체 | `COALESCE`, `IFNULL`, `ISNULL` |
| 특정 값이면 NULL 반환   | `NULLIF`                       |
| 비교시 주의             | `= NULL` ❌ → `IS NULL` ✅     |
