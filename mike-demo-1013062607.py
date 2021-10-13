from airflow import DAG

from airflow.kubernetes.secret import Secret

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "mike-demo-1013062607",
}

dag = DAG(
    "mike-demo-1013062607",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using mike-demo.pipeline.",
    is_paused_upon_creation=False,
)


# Ensure that the secret named 'demo-cos-secret' is defined in the Kubernetes namespace where this pipeline will be run
env_var_secret_id = Secret(
    deploy_type="env",
    deploy_target="AWS_ACCESS_KEY_ID",
    secret="demo-cos-secret",
    key="AWS_ACCESS_KEY_ID",
)
env_var_secret_key = Secret(
    deploy_type="env",
    deploy_target="AWS_SECRET_ACCESS_KEY",
    secret="demo-cos-secret",
    key="AWS_SECRET_ACCESS_KEY",
)


notebook_op_c0b286b9_a312_482c_a29e_5c0f58c1ea09 = NotebookOp(
    name="Untitled",
    namespace="anz-ml",
    task_id="Untitled",
    notebook="Untitled.ipynb",
    cos_endpoint="http://minio-ml-workshop-anz-ml.apps.btpns01.apac-1.rht-labs.com",
    cos_bucket="airflow",
    cos_directory="mike-demo-1013062607",
    cos_dependencies_archive="Untitled-c0b286b9-a312-482c-a29e-5c0f58c1ea09.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="amancevice/pandas:1.1.1",
    secrets=[env_var_secret_id, env_var_secret_key],
    in_cluster=True,
    env_vars={"ELYRA_ENABLE_PIPELINE_INFO": "True"},
    config_file="None",
    dag=dag,
)
