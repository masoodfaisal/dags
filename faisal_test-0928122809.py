from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "faisal_test-0928122809",
}

dag = DAG(
    "faisal_test-0928122809",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using faisal_test.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_31760156_5e57_411e_89f0_a8cbd5e67a7d = NotebookOp(
    name="faisal_test",
    namespace="anz-ml",
    task_id="faisal_test",
    notebook="faisal_test.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="faisal_test-0928122809",
    cos_dependencies_archive="faisal_test-31760156-5e57-411e-89f0-a8cbd5e67a7d.tar.gz",
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

notebook_op_31760156_5e57_411e_89f0_a8cbd5e67a7d.image_pull_policy = "Always"
