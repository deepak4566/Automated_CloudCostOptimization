import boto3

REGION = "ap-south-1"

def get_instance_ids(region):
    ec2 = boto3.client('ec2', region_name=region)
    instance_ids = []

    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    return instance_ids

def start_instances(instance_ids, region):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.start_instances(InstanceIds=instance_ids)

    if response['StartingInstances']:
        print('Instances successfully started: {}'.format(instance_ids))
    else:
        print('Failed to start instances.')

def handler(event, context):
    instance_ids = get_instance_ids(REGION)
    start_instances(instance_ids, REGION)
