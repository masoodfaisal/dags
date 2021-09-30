from airflow import DAG

from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.utils.dates import days_ago

args = {
    "project_id": "deploy_model_113-0930015948",
}

dag = DAG(
    "deploy_model_113-0930015948",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 3.1.1 pipeline editor using `deploy_model.pipeline`.",
    is_paused_upon_creation=False,
)


op_9717753b_c990_4c21_88ba_4a46474a32e4 = KubernetesPodOperator(
    name="ocp_deploy",
    namespace="anz-ml",
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.5",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://minio-ml-workshop:9000 --cos-bucket airflow --cos-directory 'deploy_model_113-0930015948' --cos-dependencies-archive 'ocp_deploy-9717753b-c990-4c21-88ba-4a46474a32e4.tar.gz' --file 'mlops_project/deploy/model_deploy/with_airflow/ocp_deploy.py' "
    ],
    task_id="ocp_deploy",
    env_vars={
        "MODEL_NAME": "sdemo2",
        "MODEL_VERSION": "1",
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "deploy_model_113-0930015948-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_9717753b_c990_4c21_88ba_4a46474a32e4.image_pull_policy = "Always"
