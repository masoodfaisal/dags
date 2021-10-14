from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "text_classification_deploy_model_v148-1014032139",
}

dag = DAG(
    "text_classification_deploy_model_v148-1014032139",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using text_classification_deploy_model_v148.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_4879d246_135e_46a2_b36b_01a01ecc22fb = NotebookOp(
    name="ocp_deploy",
    namespace="anz-ml",
    task_id="ocp_deploy",
    notebook="mlops_project/deploy/text_classification/ocp_deploy.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="text_classification_deploy_model_v148-1014032139",
    cos_dependencies_archive="ocp_deploy-4879d246-135e-46a2-b36b-01a01ecc22fb.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.8",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "lstmv14",
        "MODEL_VERSION": "1",
    },
    config_file="None",
    dag=dag,
)

notebook_op_4879d246_135e_46a2_b36b_01a01ecc22fb.image_pull_policy = "Always"
