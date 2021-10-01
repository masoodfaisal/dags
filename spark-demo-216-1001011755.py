from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "spark-demo-216-1001011755",
}

dag = DAG(
    "spark-demo-216-1001011755",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using spark-demo-216.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_d5009697_771e_4f71_bc20_e52d905c9f9d = NotebookOp(
    name="start_spark_cluster",
    namespace="anz-ml",
    task_id="start_spark_cluster",
    notebook="mlops-workshop/airflow/spark/start-spark-cluster.py",
    cos_endpoint="http://minio-ml-workshop-anz-ml.apps.btpns01.apac-1.rht-labs.com",
    cos_bucket="airflow",
    cos_directory="spark-demo-216-1001011755",
    cos_dependencies_archive="start-spark-cluster-d5009697-771e-4f71-bc20-e52d905c9f9d.tar.gz",
    pipeline_outputs=["spark-info.txt"],
    pipeline_inputs=[],
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.5",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "SPARK_CLUSTER": "ross-cluster",
    },
    config_file="None",
    dag=dag,
)

notebook_op_d5009697_771e_4f71_bc20_e52d905c9f9d.image_pull_policy = "Always"


notebook_op_8628c8ac_380d_4460_aa1e_506ffd6b010b = NotebookOp(
    name="run_pyspark_shit",
    namespace="anz-ml",
    task_id="run_pyspark_shit",
    notebook="mlops-workshop/airflow/spark/run-pyspark-shit.py",
    cos_endpoint="http://minio-ml-workshop-anz-ml.apps.btpns01.apac-1.rht-labs.com",
    cos_bucket="airflow",
    cos_directory="spark-demo-216-1001011755",
    cos_dependencies_archive="run-pyspark-shit-8628c8ac-380d-4460-aa1e-506ffd6b010b.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=["spark-info.txt"],
    image="image-registry.openshift-image-registry.svc:5000/anz-ml/s2i-spark-minimal-notebook:py36-spark2.4.5-hadoop2.7.3",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_8628c8ac_380d_4460_aa1e_506ffd6b010b.image_pull_policy = "Always"

(
    notebook_op_8628c8ac_380d_4460_aa1e_506ffd6b010b
    << notebook_op_d5009697_771e_4f71_bc20_e52d905c9f9d
)


notebook_op_91a3738b_783b_4eb6_823c_1b8b013a4d51 = NotebookOp(
    name="Merge_Data",
    namespace="anz-ml",
    task_id="Merge_Data",
    notebook="mlops-workshop/airflow/spark/Merge_Data.ipynb",
    cos_endpoint="http://minio-ml-workshop-anz-ml.apps.btpns01.apac-1.rht-labs.com",
    cos_bucket="airflow",
    cos_directory="spark-demo-216-1001011755",
    cos_dependencies_archive="Merge_Data-91a3738b-783b-4eb6-823c-1b8b013a4d51.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=["spark-info.txt"],
    image="image-registry.openshift-image-registry.svc:5000/anz-ml/s2i-spark-minimal-notebook:py36-spark2.4.5-hadoop2.7.3",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "S3_ENDPOINT": "http://172.30.29.255:9000",
    },
    config_file="None",
    dag=dag,
)

notebook_op_91a3738b_783b_4eb6_823c_1b8b013a4d51.image_pull_policy = "Always"

(
    notebook_op_91a3738b_783b_4eb6_823c_1b8b013a4d51
    << notebook_op_d5009697_771e_4f71_bc20_e52d905c9f9d
)


notebook_op_b6d6a9d3_65b6_4ef6_9ce8_4d713bea5e2f = NotebookOp(
    name="stop_spark_cluster",
    namespace="anz-ml",
    task_id="stop_spark_cluster",
    notebook="mlops-workshop/airflow/spark/stop-spark-cluster.py",
    cos_endpoint="http://minio-ml-workshop-anz-ml.apps.btpns01.apac-1.rht-labs.com",
    cos_bucket="airflow",
    cos_directory="spark-demo-216-1001011755",
    cos_dependencies_archive="stop-spark-cluster-b6d6a9d3-65b6-4ef6-9ce8-4d713bea5e2f.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=["spark-info.txt"],
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.5",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_b6d6a9d3_65b6_4ef6_9ce8_4d713bea5e2f.image_pull_policy = "Always"

(
    notebook_op_b6d6a9d3_65b6_4ef6_9ce8_4d713bea5e2f
    << notebook_op_8628c8ac_380d_4460_aa1e_506ffd6b010b
)

(
    notebook_op_b6d6a9d3_65b6_4ef6_9ce8_4d713bea5e2f
    << notebook_op_91a3738b_783b_4eb6_823c_1b8b013a4d51
)
