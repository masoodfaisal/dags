from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "deploy-2-0924081039",
}

dag = DAG(
    "deploy-2-0924081039",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using deploy-2.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_d2c6eb3c_118d_4cf9_ab14_2e9cb46eca5d = NotebookOp(
    name="fetch_artifacts",
    namespace="ml-workshop",
    task_id="fetch_artifacts",
    notebook="mlops-workshop/airflow/pipeline/fetch_artifacts.ipynb",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="deploy-2-0924081039",
    cos_dependencies_archive="fetch_artifacts-d2c6eb3c-118d-4cf9-ab14-2e9cb46eca5d.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="registry.access.redhat.com/ubi8/python-38:1-68",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "",
        "AWS_SECRET_ACCESS_KEY": "",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MLFLOW_S3_ENDPOINT_URL": "",
        "AWS_REGION": "",
        "AWS_BUCKET_NAME": "",
        "MODEL_NAME": "rossmodel",
        "MODEL_VERSION": "1",
    },
    config_file="None",
    dag=dag,
)

notebook_op_d2c6eb3c_118d_4cf9_ab14_2e9cb46eca5d.image_pull_policy = "IfNotPresent"
