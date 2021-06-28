from airflow import DAG
from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "untitled-0628061503",
}

dag = DAG(
    "untitled-0628061503",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.1 pipeline editor using untitled.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_aa7497ee_b8eb_4493_ad05_89cd74ac4389 = NotebookOp(
    name="untitled",
    namespace="default",
    task_id="untitled",
    notebook="untitled.py",
    cos_endpoint="https://minio-ml-workshop-ml-workshop.apps.saocpdt.apac-1.rht-labs.com",
    cos_bucket="data",
    cos_directory="untitled-0628061503",
    cos_dependencies_archive="untitled-aa7497ee-b8eb-4493-ad05-89cd74ac4389.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="amancevice/pandas:1.1.1",
    resources={
        "request_cpu": "1",
    },
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)
