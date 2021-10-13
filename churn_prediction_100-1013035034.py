from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "churn_prediction_100-1013035034",
}

dag = DAG(
    "churn_prediction_100-1013035034",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using churn_prediction_100.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_3e683b19_9650_4ce4_a014_7acfeddc3a31 = NotebookOp(
    name="ocp_deploy",
    namespace="anz-ml",
    task_id="ocp_deploy",
    notebook="mlops_project/deploy/churn/with_airflow/ocp_deploy.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="churn_prediction_100-1013035034",
    cos_dependencies_archive="ocp_deploy-3e683b19-9650-4ce4-a014-7acfeddc3a31.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.6",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "sd13",
        "MODEL_VERSION": "1",
    },
    config_file="None",
    dag=dag,
)

notebook_op_3e683b19_9650_4ce4_a014_7acfeddc3a31.image_pull_policy = "Always"
