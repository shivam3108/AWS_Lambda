import json
import boto3
client = boto3.client('ec2')


def ec2_instance_id_details():
    response = client.describe_instances()
    instance_id_list = []
    for res in response['Reservations']:
        for instance in res['Instances']:
            if instance['State']['Name'] != 'terminated' and instance['State']['Name'] == 'running':
                instance_id_list.append(instance['InstanceId'])
    return instance_id_list


def start_ec2(instance_id):
    response = client.stop_instances(
        InstanceIds=instance_id
    )
    print(response)

def lambda_handler(event, context):
    instance_id_list1 = ec2_instance_id_details()
    if len(instance_id_list1) > 0:
        start_ec2(instance_id_list1)
    else:
        print("No instance to start")
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

