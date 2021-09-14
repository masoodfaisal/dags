from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "hello-python-0914092513",
}

dag = DAG(
    "hello-python-0914092513",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using hello-python.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_f7df6207_1d82_4c0a_9bba_801ea31b9803 = NotebookOp(
    name="untitled",
    namespace="ml-workshop",
    task_id="untitled",
    notebook="ml-workshop/notebook/untitled.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello-python-0914092513",
    cos_dependencies_archive="untitled-f7df6207-1d82-4c0a-9bba-801ea31b9803.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="registry.access.redhat.com/ubi8/python-38",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_f7df6207_1d82_4c0a_9bba_801ea31b9803.image_pull_policy = "IfNotPresent"
