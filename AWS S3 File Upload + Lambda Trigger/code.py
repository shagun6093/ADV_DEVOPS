import json
import boto3
import csv
import io
s3Client = boto3.client('s3')

def lambda_handler(event, context):
   
   print(event)
   bucket = event['Record'][0]['s3']['bucket']['name']
   key=event['Record'][0]['s3']['object']['key']
   
   print(bucket)
   print(key)
   
   #Get our object
   response - s3Client.get_object(Bucket=bucket, Key=key)
   
   #process it
   data=response['Body'].read().decode('utf-8')
   reader=csv.reader(io.StringIO(data))
   next(reader)
   for row in reader:
       print(str.format("Year - {},Mileage - {},price-{}",row[0],row[1],row[2]))
