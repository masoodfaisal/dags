from airflow import DAG

from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.utils.dates import days_ago

args = {
    "project_id": "spark-demo-0930023122",
}

dag = DAG(
    "spark-demo-0930023122",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 3.1.1 pipeline editor using `spark-demo.pipeline`.",
    is_paused_upon_creation=False,
)


op_a6da622f_f6d5_46e8_a1aa_c507ea3ce5f5 = KubernetesPodOperator(
    name="start_spark_cluster",
    namespace="anz-ml",
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.5",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://minio-ml-workshop-anz-ml.apps.btpns01.apac-1.rht-labs.com --cos-bucket airflow --cos-directory 'spark-demo-0930023122' --cos-dependencies-archive 'start-spark-cluster-a6da622f-f6d5-46e8-a1aa-c507ea3ce5f5.tar.gz' --file 'mlops-workshop/airflow/spark/start-spark-cluster.py' --outputs 'spark-cluster-info.txt' "
    ],
    task_id="start_spark_cluster",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "spark-demo-0930023122-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_a6da622f_f6d5_46e8_a1aa_c507ea3ce5f5.image_pull_policy = "Always"


op_e7d53549_6161_48c3_8b7d_843cd6819adb = KubernetesPodOperator(
    name="run_pyspark_shit",
    namespace="anz-ml",
    image="image-registry.openshift-image-registry.svc:5000/anz-ml/s2i-spark-minimal-notebook",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://minio-ml-workshop-anz-ml.apps.btpns01.apac-1.rht-labs.com --cos-bucket airflow --cos-directory 'spark-demo-0930023122' --cos-dependencies-archive 'run-pyspark-shit-e7d53549-6161-48c3-8b7d-843cd6819adb.tar.gz' --file 'mlops-workshop/airflow/spark/run-pyspark-shit.py' --inputs 'spark-cluster-info.txt' "
    ],
    task_id="run_pyspark_shit",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "spark-demo-0930023122-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_e7d53549_6161_48c3_8b7d_843cd6819adb.image_pull_policy = "Always"

op_e7d53549_6161_48c3_8b7d_843cd6819adb << op_a6da622f_f6d5_46e8_a1aa_c507ea3ce5f5


op_ade93ee8_9f2b_41ec_b562_f18220a2a130 = KubernetesPodOperator(
    name="stop_spark_cluster",
    namespace="anz-ml",
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.5",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://minio-ml-workshop-anz-ml.apps.btpns01.apac-1.rht-labs.com --cos-bucket airflow --cos-directory 'spark-demo-0930023122' --cos-dependencies-archive 'stop-spark-cluster-ade93ee8-9f2b-41ec-b562-f18220a2a130.tar.gz' --file 'mlops-workshop/airflow/spark/stop-spark-cluster.py' --inputs 'spark-cluster-info.txt' "
    ],
    task_id="stop_spark_cluster",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "spark-demo-0930023122-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_ade93ee8_9f2b_41ec_b562_f18220a2a130.image_pull_policy = "Always"

op_ade93ee8_9f2b_41ec_b562_f18220a2a130 << op_e7d53549_6161_48c3_8b7d_843cd6819adb
