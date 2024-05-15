import boto3

def lambda_handler(event, context):
    # Initialize boto3 client for EC2
    ec2 = boto3.client('ec2')

    # Get all EBS snapshots owned by the current AWS account
    snapshots_response = ec2.describe_snapshots(OwnerIds=['self'])

    # Get all active EC2 instance IDs
    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    
    # Extract active instance IDs using set comprehension for efficiency
    active_instance_ids = set(instance['InstanceId'] for reservation in instances_response['Reservations'] for instance in reservation['Instances'])

    # List to store snapshots to be deleted
    snapshots_to_delete = []

    # Iterate through each snapshot and determine if it should be deleted
    for snapshot in snapshots_response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')

        # Add snapshot to delete list if it's not attached to any volume or the volume is not attached to a running instance
        if not volume_id or volume_id not in active_instance_ids:
            snapshots_to_delete.append(snapshot_id)

    # Delete snapshots in batches of 100 for efficiency
    for i in range(0, len(snapshots_to_delete), 100):
        batch_to_delete = snapshots_to_delete[i:i + 100]
        if batch_to_delete:
            ec2.delete_snapshots(SnapshotIds=batch_to_delete)
            print(f"Deleted {len(batch_to_delete)} EBS snapshots.")

    print("Snapshot cleanup complete.")
