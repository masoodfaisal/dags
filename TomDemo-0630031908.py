from airflow import DAG
from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "TomDemo-0630031908",
}

dag = DAG(
    "TomDemo-0630031908",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.1 pipeline editor using TomDemo.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_5546a344_fa5b_4776_92db_1e4d04568ecf = NotebookOp(
    name="untitled",
    namespace="default",
    task_id="untitled",
    notebook="untitled.py",
    cos_endpoint="https://minio-ml-workshop-ml-workshop.apps.saocpdt.apac-1.rht-labs.com",
    cos_bucket="data",
    cos_directory="TomDemo-0630031908",
    cos_dependencies_archive="untitled-5546a344-fa5b-4776-92db-1e4d04568ecf.tar.gz",
    pipeline_outputs=["a.out"],
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


notebook_op_0a52729c_6268_4b0b_96d3_0c17ae14b2d9 = NotebookOp(
    name="Untitled",
    namespace="default",
    task_id="Untitled",
    notebook="Untitled.ipynb",
    cos_endpoint="https://minio-ml-workshop-ml-workshop.apps.saocpdt.apac-1.rht-labs.com",
    cos_bucket="data",
    cos_directory="TomDemo-0630031908",
    cos_dependencies_archive="Untitled-0a52729c-6268-4b0b-96d3-0c17ae14b2d9.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=["a.out"],
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

notebook_op_0a52729c_6268_4b0b_96d3_0c17ae14b2d9 << notebook_op_5546a344_fa5b_4776_92db_1e4d04568ecf
