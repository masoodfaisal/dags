from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "faisal_test-0928122737",
}

dag = DAG(
    "faisal_test-0928122737",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using faisal_test.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_05a27a2f_6f6e_4456_9d14_b97cc7bbeee4 = NotebookOp(
    name="faisal_test",
    namespace="anz-ml",
    task_id="faisal_test",
    notebook="faisal_test.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="faisal_test-0928122737",
    cos_dependencies_archive="faisal_test-05a27a2f-6f6e-4456-9d14-b97cc7bbeee4.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.5",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_05a27a2f_6f6e_4456_9d14_b97cc7bbeee4.image_pull_policy = "Always"
