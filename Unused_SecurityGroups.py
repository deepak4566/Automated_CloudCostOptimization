import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    # Create EC2 client
    ec2 = boto3.client('ec2')

    # Get current timestamp
    current_time = datetime.now()

    # Define a timedelta for cutoff time (e.g., 30 days)
    cutoff_time = current_time - timedelta(days=30)

    # Delete unused security groups
    delete_unused_security_groups(ec2, cutoff_time)

def delete_unused_security_groups(ec2, cutoff_time):
    # Get list of all security groups
    security_groups_response = ec2.describe_security_groups()

    # Iterate through each security group
    for security_group in security_groups_response['SecurityGroups']:
        group_id = security_group['GroupId']

        # Check if the security group is associated with any network interfaces
        interfaces_response = ec2.describe_network_interfaces(Filters=[{'Name': 'group-id', 'Values': [group_id]}])
        if not interfaces_response['NetworkInterfaces']:
            # Check if the security group was created more than 30 days ago
            create_time = security_group['CreateDate']
            if create_time < cutoff_time:
                print(f"Deleting unused security group: {group_id}")
                ec2.delete_security_group(GroupId=group_id)
