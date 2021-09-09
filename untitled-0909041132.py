from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "untitled-0909041132",
}

dag = DAG(
    "untitled-0909041132",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using untitled.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_3c6f0158_f154_4f49_a9f3_8951e90037f0 = NotebookOp(
    name="untitled",
    namespace="ml-workshop",
    task_id="untitled",
    notebook="untitled.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="untitled-0909041132",
    cos_dependencies_archive="untitled-3c6f0158-f154-4f49-a9f3-8951e90037f0.tar.gz",
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


notebook_op_9ac8436e_d4c3_4fa0_bb9c_d5619a10b3fe = NotebookOp(
    name="untitled1",
    namespace="ml-workshop",
    task_id="untitled1",
    notebook="untitled1.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="untitled-0909041132",
    cos_dependencies_archive="untitled1-9ac8436e-d4c3-4fa0-bb9c-d5619a10b3fe.tar.gz",
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
    notebook_op_9ac8436e_d4c3_4fa0_bb9c_d5619a10b3fe
    << notebook_op_3c6f0158_f154_4f49_a9f3_8951e90037f0
)
