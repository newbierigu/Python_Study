### 위클리\_페이퍼\_15

# DAG 와 Task관계 & Operator 종류

---

## `DAG` 란?

- **Directed Acyclic Graph(유향 비순환 그래프)**의 약자
- `Airflow`에서 **워크플로우(Workflow)**를 정의하는 가장 큰 단위
- 여러 개의 `Task(작업)`들이 방향성을 가진 그래프로 연결되어, 실행 순서를 관리함
- 예시: {매일 새벽 3시에 데이터 수집 → 전처리 → 모델 학습 → 리포트 발송} 해당 과정을 정의하는 전체 설계도

## `Task` 란?

- `DAG` 안에서 실행되는 하나의 단일 작업 단위
- 보통 `Operator`를 통해 정의됨
- 예시
  - `데이터 수집` Task : API에서 데이터를 가져오는 작업
  - `전처리` Task : 가져온 데이터를 가공하는 작업
  - `리포트 발송` Task : 이메일로 결과를 보내는 작업

<br>

## `DAG`와 `Task`의 관계

- `DAG` : 데이터 파이프라인 구축
- `Task A` → `Task B` → `Task C`
  - A : 데이터 수집
  - B : 데이터 정제
  - C : 시각화 & 리포트 생성

---

## Airflow에서 `Operator`란?

- `Task`의 구체적인 실행 방법을 정의하는 클래스
- `Task`는 `Operator`의 인스턴스로 만들어짐
- `Operator`는 크게 3가지로 볼 수 있음
  - **Action** : 특정 액션을 수행 (Operator 예시 : `BashOperator`, `PythonOperator` )
  - **Transfer** : 데이터를 한 곳에서 다른 곳으로 이동 (Operator 예시 : `S3ToRedshiftOperator` )
  - **Sensor** : 특정 조건이 충족될 때까지 대기 (Operator 예시 : `S3KeySensor`, `ExternalTaskSensor` )

#### `Operator` 설명

- **`BashOperator`**

  - Bash 명령어를 실행할 수 있도록 해주는 Operator
  - 예: `ls -l`, `echo "Hello Airflow"` 같은 쉘 명령어 실행

- **`PythonOperator`**

  - 파이썬 함수를 실행할 수 있는 Operator
  - 예: 데이터 전처리 함수나 모델 학습 함수를 Task로 실행

- **`S3ToRedshiftOperator`**

  - Amazon S3에 저장된 데이터를 Redshift로 로드하는 데 사용
  - ETL 파이프라인에서 자주 활용 (데이터 적재 단계)

- **`S3KeySensor`**

  - S3에 특정 파일(Key)이 존재하는지 확인하고, 없으면 대기
  - 예: 외부 시스템이 S3에 데이터를 업로드할 때까지 기다림

- **`ExternalTaskSensor`**
  - 다른 DAG 혹은 다른 Task가 끝나기를 기다리는 Sensor
  - 워크플로우 간 의존성이 있을 때 활용

---

<br>

## 마무리

- `DAG`는 워크플로우의 `“설계도”`, `Task`는 그 안의 `“작업 단위”`

- `Operator`는 Task의 실행 방법을 정의하는 `“도구”`

- DAG와 Task의 관계를 이해하면, 복잡한 파이프라인도 단계별로 관리 가능

- 다양한 Operator를 적절히 활용하면 데이터 엔지니어링 및 머신러닝 파이프라인을 유연하게 확장 가능
