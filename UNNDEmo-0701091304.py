from airflow import DAG
from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "UNNDEmo-0701091304",
}

dag = DAG(
    "UNNDEmo-0701091304",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.1 pipeline editor using UNNDEmo.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_725f5587_e368_4925_a0a1_820af45df3de = NotebookOp(
    name="DataProcessing",
    namespace="default",
    task_id="DataProcessing",
    notebook="DataProcessing.py",
    cos_endpoint="https://minio-ml-workshop-ml-workshop.apps.saocpdt.apac-1.rht-labs.com",
    cos_bucket="data",
    cos_directory="UNNDEmo-0701091304",
    cos_dependencies_archive="DataProcessing-725f5587-e368-4925-a0a1-820af45df3de.tar.gz",
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


notebook_op_da8cecb2_03d1_46b9_b785_0ada9dc01969 = NotebookOp(
    name="Training",
    namespace="default",
    task_id="Training",
    notebook="Training.ipynb",
    cos_endpoint="https://minio-ml-workshop-ml-workshop.apps.saocpdt.apac-1.rht-labs.com",
    cos_bucket="data",
    cos_directory="UNNDEmo-0701091304",
    cos_dependencies_archive="Training-da8cecb2-03d1-46b9-b785-0ada9dc01969.tar.gz",
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

notebook_op_da8cecb2_03d1_46b9_b785_0ada9dc01969 << notebook_op_725f5587_e368_4925_a0a1_820af45df3de
