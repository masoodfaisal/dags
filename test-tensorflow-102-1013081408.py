from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "test-tensorflow-102-1013081408",
}

dag = DAG(
    "test-tensorflow-102-1013081408",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using test-tensorflow-102.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_32a32b67_af9e_41f0_a74e_c615d6f07643 = NotebookOp(
    name="untitled",
    namespace="anz-ml",
    task_id="untitled",
    notebook="mlops-workshop/airflow/spark/untitled.py",
    cos_endpoint="http://minio-ml-workshop-anz-ml.apps.btpns01.apac-1.rht-labs.com",
    cos_bucket="airflow",
    cos_directory="test-tensorflow-102-1013081408",
    cos_dependencies_archive="untitled-32a32b67-af9e-41f0-a74e-c615d6f07643.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.7",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_32a32b67_af9e_41f0_a74e_c615d6f07643.image_pull_policy = "IfNotPresent"
