from datetime import datetime
import urllib3
import boto3

bucket = "mylambdaworkerstorage"
URL = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'
s3 = boto3.client('s3')
time = datetime.now()

def lambda_handler(event, context):
    http = urllib3.PoolManager()
    response = http.request("GET", URL)
    data = response.data.decode("utf-8")
    s3.put_object(Bucket=bucket, Key="data_{}.json".format(datetime.timestamp(time)), Body=data)