from airflow import DAG

from airflow.kubernetes.secret import Secret

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "stop-spark-cluster-2-1010025809",
}

dag = DAG(
    "stop-spark-cluster-2-1010025809",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using stop-spark-cluster-2.pipeline.",
    is_paused_upon_creation=False,
)


# Ensure that the secret named 'demo-cos-secret' is defined in the Kubernetes namespace where this pipeline will be run
env_var_secret_id = Secret(
    deploy_type="env",
    deploy_target="AWS_ACCESS_KEY_ID",
    secret="demo-cos-secret",
    key="AWS_ACCESS_KEY_ID",
)
env_var_secret_key = Secret(
    deploy_type="env",
    deploy_target="AWS_SECRET_ACCESS_KEY",
    secret="demo-cos-secret",
    key="AWS_SECRET_ACCESS_KEY",
)


notebook_op_bca8bfb7_1cfb_4927_8522_5a2ec837e8a8 = NotebookOp(
    name="mlops_workshop_airflow_spark_stop_spark_cluster_2.py",
    namespace="anz-ml",
    task_id="mlops_workshop_airflow_spark_stop_spark_cluster_2.py",
    notebook="mlops-workshop/airflow/spark/stop-spark-cluster-2.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="stop-spark-cluster-2-1010025809",
    cos_dependencies_archive="stop-spark-cluster-2-bca8bfb7-1cfb-4927-8522-5a2ec837e8a8.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.5",
    secrets=[env_var_secret_id, env_var_secret_key],
    in_cluster=True,
    env_vars={"ELYRA_ENABLE_PIPELINE_INFO": "True"},
    config_file="None",
    dag=dag,
)

notebook_op_bca8bfb7_1cfb_4927_8522_5a2ec837e8a8.image_pull_policy = "Always"
