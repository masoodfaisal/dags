from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "faisal_test-0928120756",
}

dag = DAG(
    "faisal_test-0928120756",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using faisal_test.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_ab9e2e03_6ef8_4380_af1d_7e1779e57086 = NotebookOp(
    name="model_deploy_007",
    namespace="anz-ml",
    task_id="model_deploy_007",
    notebook="model_deploy_007.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="faisal_test-0928120756",
    cos_dependencies_archive="model_deploy_007-ab9e2e03-6ef8-4380-af1d-7e1779e57086.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.5",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "rossdemo",
        "MODEL_VERSION": "1",
    },
    config_file="None",
    dag=dag,
)

notebook_op_ab9e2e03_6ef8_4380_af1d_7e1779e57086.image_pull_policy = "Always"
