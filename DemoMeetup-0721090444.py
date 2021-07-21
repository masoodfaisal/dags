from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "DemoMeetup-0721090444",
}

dag = DAG(
    "DemoMeetup-0721090444",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using DemoMeetup.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_48752854_0cb5_4b3a_9061_85a910869e0c = NotebookOp(
    name="datasplit",
    namespace="ml-workshop",
    task_id="datasplit",
    notebook="datasplit.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="DemoMeetup-0721090444",
    cos_dependencies_archive="datasplit-48752854-0cb5-4b3a-9061-85a910869e0c.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)


notebook_op_06e64d00_6f37_4d6c_9890_7fadc59dc58d = NotebookOp(
    name="training",
    namespace="ml-workshop",
    task_id="training",
    notebook="training.ipynb",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="DemoMeetup-0721090444",
    cos_dependencies_archive="training-06e64d00-6f37-4d6c-9890-7fadc59dc58d.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="amancevice/pandas:1.1.1",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

(
    notebook_op_06e64d00_6f37_4d6c_9890_7fadc59dc58d
    << notebook_op_48752854_0cb5_4b3a_9061_85a910869e0c
)
