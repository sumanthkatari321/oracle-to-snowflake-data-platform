import boto3
import logging

logging.basicConfig(level=logging.INFO)

class S3Uploader:

    def __init__(self):

        self.s3 = boto3.client('s3')

    def upload_file(self, file_path, bucket, s3_key):

        try:

            self.s3.upload_file(
                Filename=file_path,
                Bucket=bucket,
                Key=s3_key
            )

            logging.info(
                f"{file_path} uploaded successfully"
            )

        except Exception as e:
            logging.error(e)
            raise
