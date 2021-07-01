from airflow import DAG
from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "RossDemo-0701064240",
}

dag = DAG(
    "RossDemo-0701064240",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.1 pipeline editor using RossDemo.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_3984554b_d09e_4ff1_83ed_9a2cdc24bf20 = NotebookOp(
    name="Untitled",
    namespace="default",
    task_id="Untitled",
    notebook="Untitled.ipynb",
    cos_endpoint="https://minio-ml-workshop-ml-workshop.apps.saocpdt.apac-1.rht-labs.com",
    cos_bucket="data",
    cos_directory="RossDemo-0701064240",
    cos_dependencies_archive="Untitled-3984554b-d09e-4ff1-83ed-9a2cdc24bf20.tar.gz",
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


notebook_op_db3549d6_5ef1_4c4d_9d24_a2b81a3fc010 = NotebookOp(
    name="untitled",
    namespace="default",
    task_id="untitled",
    notebook="untitled.py",
    cos_endpoint="https://minio-ml-workshop-ml-workshop.apps.saocpdt.apac-1.rht-labs.com",
    cos_bucket="data",
    cos_directory="RossDemo-0701064240",
    cos_dependencies_archive="untitled-db3549d6-5ef1-4c4d-9d24-a2b81a3fc010.tar.gz",
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

notebook_op_db3549d6_5ef1_4c4d_9d24_a2b81a3fc010 << notebook_op_3984554b_d09e_4ff1_83ed_9a2cdc24bf20
