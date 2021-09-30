from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "spark-demo2_7-0930031103",
}

dag = DAG(
    "spark-demo2_7-0930031103",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using spark-demo2_7.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_d5009697_771e_4f71_bc20_e52d905c9f9d = NotebookOp(
    name="start_spark_cluster",
    namespace="anz-ml",
    task_id="start_spark_cluster",
    notebook="mlops-workshop/airflow/spark/start-spark-cluster.py",
    cos_endpoint="http://minio-ml-workshop-anz-ml.apps.btpns01.apac-1.rht-labs.com",
    cos_bucket="airflow",
    cos_directory="spark-demo2_7-0930031103",
    cos_dependencies_archive="start-spark-cluster-d5009697-771e-4f71-bc20-e52d905c9f9d.tar.gz",
    pipeline_outputs=["spark-info.txt"],
    pipeline_inputs=[],
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

notebook_op_d5009697_771e_4f71_bc20_e52d905c9f9d.image_pull_policy = "Always"


notebook_op_8628c8ac_380d_4460_aa1e_506ffd6b010b = NotebookOp(
    name="run_pyspark_shit",
    namespace="anz-ml",
    task_id="run_pyspark_shit",
    notebook="mlops-workshop/airflow/spark/run-pyspark-shit.py",
    cos_endpoint="http://minio-ml-workshop-anz-ml.apps.btpns01.apac-1.rht-labs.com",
    cos_bucket="airflow",
    cos_directory="spark-demo2_7-0930031103",
    cos_dependencies_archive="run-pyspark-shit-8628c8ac-380d-4460-aa1e-506ffd6b010b.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=["spark-info.txt"],
    image="image-registry.openshift-image-registry.svc:5000/anz-ml/s2i-spark-minimal-notebook",
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


notebook_op_c1b8cef9_cbf8_4570_b46a_cd81853e0b2d = NotebookOp(
    name="stop_spark_cluster",
    namespace="anz-ml",
    task_id="stop_spark_cluster",
    notebook="mlops-workshop/airflow/spark/stop-spark-cluster.py",
    cos_endpoint="http://minio-ml-workshop-anz-ml.apps.btpns01.apac-1.rht-labs.com",
    cos_bucket="airflow",
    cos_directory="spark-demo2_7-0930031103",
    cos_dependencies_archive="stop-spark-cluster-c1b8cef9-cbf8-4570-b46a-cd81853e0b2d.tar.gz",
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

notebook_op_c1b8cef9_cbf8_4570_b46a_cd81853e0b2d.image_pull_policy = "Always"

(
    notebook_op_c1b8cef9_cbf8_4570_b46a_cd81853e0b2d
    << notebook_op_8628c8ac_380d_4460_aa1e_506ffd6b010b
)
