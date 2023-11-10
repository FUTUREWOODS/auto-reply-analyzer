import boto3
import os

s3_client = boto3.client("s3")

s3_bucket_name = "fw-trained-models"
s3_file_name = "auto-reply-categorizer-model.tar.gz"

local_model_path = "/app/bert"

s3_client.download_file(
    s3_bucket_name, s3_file_name, f"{local_model_path}/{s3_file_name}"
)

os.system(f"tar -xzvf {local_model_path}/{s3_file_name} -C {local_model_path}")
