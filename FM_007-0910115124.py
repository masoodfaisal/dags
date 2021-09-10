from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "FM_007-0910115124",
}

dag = DAG(
    "FM_007-0910115124",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using FM_007.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_0f4de061_0d9b_4884_a664_7886a8933132 = NotebookOp(
    name="first",
    namespace="ml-workshop",
    task_id="first",
    notebook="first.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="FM_007-0910115124",
    cos_dependencies_archive="first-0f4de061-0d9b-4884-a664-7886a8933132.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="registry.access.redhat.com/ubi8/python-38:1-68",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_0f4de061_0d9b_4884_a664_7886a8933132.image_pull_policy = "IfNotPresent"


notebook_op_8fbe2578_83b5_4a5e_bf32_2abb8e3aee93 = NotebookOp(
    name="second",
    namespace="ml-workshop",
    task_id="second",
    notebook="second.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="FM_007-0910115124",
    cos_dependencies_archive="second-8fbe2578-83b5-4a5e-bf32-2abb8e3aee93.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="registry.access.redhat.com/ubi8/python-38:1-68",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_8fbe2578_83b5_4a5e_bf32_2abb8e3aee93.image_pull_policy = "IfNotPresent"

(
    notebook_op_8fbe2578_83b5_4a5e_bf32_2abb8e3aee93
    << notebook_op_0f4de061_0d9b_4884_a664_7886a8933132
)


notebook_op_bd3a1b9f_c8ff_487c_9e5f_1b1dffb6c9fe = NotebookOp(
    name="second",
    namespace="ml-workshop",
    task_id="second",
    notebook="second.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="FM_007-0910115124",
    cos_dependencies_archive="second-bd3a1b9f-c8ff-487c-9e5f-1b1dffb6c9fe.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="registry.access.redhat.com/ubi8/python-38:1-68",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_bd3a1b9f_c8ff_487c_9e5f_1b1dffb6c9fe.image_pull_policy = "IfNotPresent"

(
    notebook_op_bd3a1b9f_c8ff_487c_9e5f_1b1dffb6c9fe
    << notebook_op_0f4de061_0d9b_4884_a664_7886a8933132
)