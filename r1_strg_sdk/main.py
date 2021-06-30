import boto3
import logging
from botocore.exceptions import ClientError
import json

# Configure logging
logging.basicConfig(level=logging.INFO)


class R1_strg_sdk:
    def __init__(self, endpoint_url, aws_access_key_id, aws_secret_access_key) -> None:
        self.endpoint_url = endpoint_url
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key

        try:
            self.s3_client = boto3.client(
                "s3",
                endpoint_url=self.endpoint_url,
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key,
            )
        except Exception as exc:
            logging.error(exc)

        try:
            self.s3_resource = boto3.resource(
                "s3",
                endpoint_url=self.endpoint_url,
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key,
            )
        except Exception as exc:
            logging.error(exc)

    def list_buckets(self):
        try:
            response = self.s3_client.list_buckets(
                Bucket="bucket_name",
            )
            result = {}
            for id, bucket in enumerate(response["Buckets"]):
                result[f"{id}"] = {
                    "name": bucket["Name"],
                    "CreationDate": bucket["CreationDate"].strftime(
                        "%Y-%m-%d|%H:%M:%S"
                    ),
                }
            return json.dumps(result)
        except ClientError as exc:
            logging.error(exc)

    def put(self, bucket_name=str, path=str, name=str, public=True):

        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            file_path = f"{path}"
            object_name = f"{name}"

            with open(file_path, "rb") as file:
                bucket.put_object(
                    ACL="public-read" if public else "private",
                    Body=file,
                    Key=object_name,
                )
        except ClientError as e:
            result = {
                "status": "faild",
                "file_name": name,
                "bucket_name": bucket_name,
                "result": logging.error(e),
            }
            return json.dumps(result)

        else:
            result = {
                "status": "ok",
                "file_name": name,
                "bucket_name": bucket_name,
                "url": f"https://{bucket_name}.s3.ir-thr-at1.arvanstorage.com/{name}",
            }
            return json.dumps(result)

    def get(self, bucket_name=str, name=str, download_path=str):
        try:
            bucket = self.s3_resource.Bucket(f"{bucket_name}")
            object_name = f"{name}"
            download_path = f"{download_path}/{name}"
            bucket.download_file(object_name, download_path)

        except ClientError as e:

            logging.error(e)

        else:
            return json.dumps({"result": "ok"})

    def delete(self, bucket_name=str, name=str):
        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            object = bucket.Object(name)
            response = object.delete()
        except ClientError as e:
            logging.error(e)

    def list_items(self, bucket_name=str):

        result = {}
        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            for obj in bucket.objects.all():
                result[obj.key] = {
                    "date-modified": obj.last_modified.strftime("%Y-%m-%d|%H:%M:%S"),
                    "url": f"https://{bucket_name}.s3.ir-thr-at1.arvanstorage.com/{obj.key}",
                }
            return json.dumps(result)

        except ClientError as e:
            logging.error(e)
