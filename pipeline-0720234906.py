from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "pipeline-0720234906",
}

dag = DAG(
    "pipeline-0720234906",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using pipeline.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_6c2c9db4_ca82_4aff_baef_f4abf09e0b42 = NotebookOp(
    name="datasplit",
    namespace="ml-workshop",
    task_id="datasplit",
    notebook="datasplit.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="pipeline-0720234906",
    cos_dependencies_archive="datasplit-6c2c9db4-ca82-4aff-baef-f4abf09e0b42.tar.gz",
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


notebook_op_ed79c959_df6a_4b3b_a1ca_abb822646f90 = NotebookOp(
    name="training",
    namespace="ml-workshop",
    task_id="training",
    notebook="training.ipynb",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="pipeline-0720234906",
    cos_dependencies_archive="training-ed79c959-df6a-4b3b-a1ca-abb822646f90.tar.gz",
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

(
    notebook_op_ed79c959_df6a_4b3b_a1ca_abb822646f90
    << notebook_op_6c2c9db4_ca82_4aff_baef_f4abf09e0b42
)
