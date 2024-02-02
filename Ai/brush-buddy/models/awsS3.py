import os

import boto3
import numpy as np
import requests
from dotenv import load_dotenv
from PIL import Image


class AwsS3:
    # S3 연결 함수
    def s3_connection():
        # os 환경변수 불러오기
        load_dotenv(verbose=True)

        # 환경변수 불러오기
        AWS_ACCESS_KEY_ID = os.gete("AWS_ACCESS_KEY_ID")
        AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

        try:
            s3 = boto3.client(
                service_name="s3",
                region_name="ap-northeast-2",  # 자신이 설정한 bucket region
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            )

        except Exception as e:
            print(e)
        else:
            print("s3 bucket connected!")
            return s3
