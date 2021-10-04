from airflow import DAG

from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.utils.dates import days_ago

args = {
    "project_id": "fm_deploy_4-1004020424",
}

dag = DAG(
    "fm_deploy_4-1004020424",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 3.1.1 pipeline editor using `fm_deploy.pipeline`.",
    is_paused_upon_creation=False,
)


op_3e8df95c_f5d4_4de7_af81_264ce7712324 = KubernetesPodOperator(
    name="download_model",
    namespace="anz-ml",
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.5",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://minio-ml-workshop:9000 --cos-bucket airflow --cos-directory 'fm_deploy_4-1004020424' --cos-dependencies-archive 'ocp_deploy-3e8df95c-f5d4-4de7-af81-264ce7712324.tar.gz' --file 'mlops_project/deploy/drift_deploy/with_airflow/ocp_deploy.py' "
    ],
    task_id="download_model",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "fm_deploy_4-1004020424-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_3e8df95c_f5d4_4de7_af81_264ce7712324.image_pull_policy = "Always"


op_739fda54_adc5_4b80_8f1a_cef181615c10 = KubernetesPodOperator(
    name="package_model",
    namespace="anz-ml",
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.5",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://minio-ml-workshop:9000 --cos-bucket airflow --cos-directory 'fm_deploy_4-1004020424' --cos-dependencies-archive 'ocp_deploy-739fda54-adc5-4b80-8f1a-cef181615c10.tar.gz' --file 'mlops_project/deploy/drift_deploy/with_airflow/ocp_deploy.py' "
    ],
    task_id="package_model",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "fm_deploy_4-1004020424-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_739fda54_adc5_4b80_8f1a_cef181615c10.image_pull_policy = "Always"

op_739fda54_adc5_4b80_8f1a_cef181615c10 << op_3e8df95c_f5d4_4de7_af81_264ce7712324


op_cbdec83c_73cd_4fc4_b425_060bdc4b1766 = KubernetesPodOperator(
    name="deploy_model",
    namespace="anz-ml",
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.5",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://minio-ml-workshop:9000 --cos-bucket airflow --cos-directory 'fm_deploy_4-1004020424' --cos-dependencies-archive 'ocp_deploy-cbdec83c-73cd-4fc4-b425-060bdc4b1766.tar.gz' --file 'mlops_project/deploy/drift_deploy/with_airflow/ocp_deploy.py' "
    ],
    task_id="deploy_model",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "fm_deploy_4-1004020424-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_cbdec83c_73cd_4fc4_b425_060bdc4b1766.image_pull_policy = "Always"

op_cbdec83c_73cd_4fc4_b425_060bdc4b1766 << op_739fda54_adc5_4b80_8f1a_cef181615c10


op_ccc5df44_7c58_4a06_910f_f30810a47d43 = KubernetesPodOperator(
    name="test_deployment",
    namespace="anz-ml",
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.5",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://minio-ml-workshop:9000 --cos-bucket airflow --cos-directory 'fm_deploy_4-1004020424' --cos-dependencies-archive 'ocp_deploy-ccc5df44-7c58-4a06-910f-f30810a47d43.tar.gz' --file 'mlops_project/deploy/drift_deploy/with_airflow/ocp_deploy.py' "
    ],
    task_id="test_deployment",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "fm_deploy_4-1004020424-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_ccc5df44_7c58_4a06_910f_f30810a47d43.image_pull_policy = "Always"

op_ccc5df44_7c58_4a06_910f_f30810a47d43 << op_cbdec83c_73cd_4fc4_b425_060bdc4b1766
