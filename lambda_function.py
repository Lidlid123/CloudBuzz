import json
import boto3



def lambda_handler(event, context):



    #1. Parse out query string params
    num1 = event['queryStringParameters']['num1']
    num2 = event['queryStringParameters']['num2']
    new1 = int(num1)
    new2 = int(num2)
    sum = new1 + new2
    notification = f"Here is the SNS notification from lidor koresh lambda function : the sum of the 2 numbers is : {sum}"
    client = boto3.client('sns')
    response = client.publish(
    TargetArn = "arn:aws:sns:us-east-1:765699113794:monitoringTeam",
    Message = json.dumps({'default': notification}),
    MessageStructure = 'json')



    #2. Construct the body of the response object
    Response = {}
    Response['num1'] = num1
    Response['num2'] = num2
    Response['sum'] = sum
    Response['message'] = 'Hello from  Lidor Koresh (:'

	#3. Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(Response)
	

	#4. Return the response object

    return responseObject
