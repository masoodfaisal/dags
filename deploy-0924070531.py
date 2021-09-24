from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "deploy-0924070531",
}

dag = DAG(
    "deploy-0924070531",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using deploy.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_da4e84f3_b5c8_4419_a98a_57be1adf8b7b = NotebookOp(
    name="fetch_artifacts",
    namespace="ml-workshop",
    task_id="fetch_artifacts",
    notebook="mlops-workshop/airflow/pipeline/fetch_artifacts.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="deploy-0924070531",
    cos_dependencies_archive="fetch_artifacts-da4e84f3-b5c8-4419-a98a-57be1adf8b7b.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="registry.access.redhat.com/ubi8/python-38:1-68",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "rossdemo",
        "MODEL_VERSION": "1",
    },
    config_file="None",
    dag=dag,
)

notebook_op_da4e84f3_b5c8_4419_a98a_57be1adf8b7b.image_pull_policy = "IfNotPresent"
