import boto3
import logging
from botocore.exceptions import ClientError
import json

# Configure logging
logging.basicConfig(level=logging.INFO)


class R1StrgSDK:
    def __init__(self, endpoint_url, access_key, secret_key) -> None:
        self.endpoint_url = endpoint_url
        self.aws_access_key_id = access_key
        self.aws_secret_access_key = secret_key

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

    def create_bucket(self, bucket_name: str, public=True):
        """
        create a new bucket.
        """
        try:
            self.s3_client.create_bucket(
                Bucket=bucket_name,
                ACL="public-read" if public else "private",
            )
        except ClientError as exc:
            logging.error(exc)

        else:
            return json.dumps({"status": "ok"})

    def delete_bucket(self, bucket_name):
        "delete a Bucket"

        try:
            self.s3_client.delete_bucket(
                Bucket=bucket_name,
            )
        except ClientError as exc:
            logging.error(exc)
        else:
            return json.dumps({"status": "ok"})

    def list_buckets(self):
        """
        :return: will return a list of buckets
        :rtype: list
        """
        try:
            response = self.s3_client.list_buckets(
                Bucket="bucket_name",
            )
            result = []
            for bucket in response["Buckets"]:
                result.append(
                    {
                        "name": bucket["Name"],
                        "CreationDate": bucket["CreationDate"].strftime(
                            "%m/%d/%y %H:%M:%S"
                        ),
                    }
                )
            return json.dumps(result)
        except ClientError as exc:
            logging.error(exc)

    def upload(self, bucket_name=str, path=str, name=str, public=True):
        """
        Upload any File to bucket_name.
        :important: Dont Forget to specify file extention.

        :return: will return a json with name of file, status and url
        """
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

    def download(self, bucket_name=str, name=str, download_path=str):
        """
        Download a File to bucket_name.
        will save file from bucket to download path.
        :return: json with result ok response.
        """
        try:
            bucket = self.s3_resource.Bucket(f"{bucket_name}")
            object_name = f"{name}"
            download_path = f"{download_path}/{name}"
            bucket.download_file(object_name, download_path)

        except ClientError as e:

            logging.error(e)

        else:
            return json.dumps({"status": "ok"})

    def delete(self, bucket_name=str, name=str):
        """
        Delete a File from bucket_name.
        will delete a file from bucket name.
        :return: json with result ok response.
        """
        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            object = bucket.Object(name)
            response = object.delete()
        except ClientError as e:
            logging.error(e)

        else:
            return json.dumps({"status": "ok"})

    def list_items(self, bucket_name=str):
        """
        will return a list of items in bucket
        :return: json of list.
        """
        result = []
        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            for obj in bucket.objects.all():
                result.append(
                    {
                        "date-modified": obj.last_modified.strftime(
                            "%m/%d/%y %H:%M:%S"
                        ),
                        "url": f"https://{bucket_name}.s3.ir-thr-at1.arvanstorage.com/{obj.key}",
                    }
                )
            return json.dumps(result)

        except ClientError as e:
            logging.error(e)
