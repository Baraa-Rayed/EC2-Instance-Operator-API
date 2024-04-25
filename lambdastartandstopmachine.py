import json
import os
import boto3

def lambda_handler(event, context):
    # Extract the action from the event
    action = event['queryStringParameters']['action']
    
    print(action)
    # Get the list of EC2 instances from the environment variable
    instances = os.environ.get('EC2_INSTANCES', '').split(",")
    
    # Initialize the EC2 client
    ec2 = boto3.client('ec2')
    
    # Perform the action based on the provided parameter
    if action == "stop":
        ec2.stop_instances(InstanceIds=instances)
        print('Stopped instances: ' + str(instances))
        response_body = 'EC2 instances stopped successfully!'
    elif action == "start":
        ec2.start_instances(InstanceIds=instances)
        print('Started instances: ' + str(instances))
        response_body = 'EC2 instances started successfully!'
    else:
        response_body = 'Invalid action provided!'
    
    # Construct the response object
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'message': response_body, 'instance_ids': instances})
    }
    
    return response

