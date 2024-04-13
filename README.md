# Automated Cloud Cost Optimization

This project aims to automate cloud cost optimization using Lambda functions and CloudWatch Events. By automatically managing resources such as EC2 instances, EBS snapshots, S3 buckets, and security groups, it helps to minimize unnecessary spending and improve overall efficiency in AWS environments.
![diagram](https://github.com/deepak4566/Automated_CloudCostOptimization/blob/main/cloudcost.png)

## Targeted Resources

### 1. AWS EC2
EC2 instances are fundamental components of many AWS workloads. This project includes functionalities to start, stop, and terminate EC2 instances based on predefined conditions, such as usage patterns and business hours. By dynamically managing EC2 instances, it ensures that resources are only active when needed, reducing costs associated with idle instances. 

### 2. EBS Snapshots
Elastic Block Store (EBS) snapshots are backups of EBS volumes, which can accrue costs over time. This project provides automation to manage EBS snapshots by deleting stale snapshots that are no longer needed. By defining criteria such as snapshot age and usage, it helps to minimize storage costs and optimize resource utilization.

### 3. AWS S3
Amazon Simple Storage Service (S3) is a scalable object storage service used for storing and retrieving data. This project includes functionality to manage S3 buckets by automatically deleting stale buckets that are no longer in use. By identifying and removing unused buckets, it helps to streamline storage costs and maintain a tidy AWS environment.

### 4. AWS Security Groups
Security groups act as virtual firewalls for controlling inbound and outbound traffic to AWS resources. This project implements automation to delete unused security groups, ensuring that only necessary security configurations are retained. By regularly cleaning up unused security groups, it enhances security posture and reduces clutter in AWS accounts.

## Usage
To use this automated cloud cost optimization solution, follow these steps:

1. **Deploy Lambda Functions**: Deploy the provided Lambda functions to your AWS account using the AWS Management Console or AWS CLI.

2. **Configure CloudWatch Events**: Set up CloudWatch Events rules to trigger the Lambda functions based on predefined schedules or conditions. Define event patterns and targets to specify when and how the Lambda functions should be executed.

3. **Customize Parameters**: Customize parameters such as cutoff times, resource criteria, and scheduling options according to your specific requirements. Adjust these parameters to align with your organization's cost optimization goals and usage patterns.

4. **Monitor and Refine**: Continuously monitor the performance and effectiveness of the automated cost optimization solution. Analyze cost savings, resource utilization, and system behavior to identify areas for further refinement and improvement.

## Example CloudWatch Event Rules:
1.Schedule to Start/Stop EC2 Instances:
Schedule a CloudWatch Event rule to trigger the Lambda function to start/stop EC2 instances at specific times of the day (e.g., start instances at 8 AM and stop instances at 6 PM).

2.Snapshot Age Threshold:
Create a CloudWatch Event rule to trigger the Lambda function to delete EBS snapshots older than a certain threshold (e.g., 30 days) every day at midnight.

3.Bucket Usage Threshold:
Set up a CloudWatch Event rule to trigger the Lambda function to delete S3 buckets that have been empty for a specified period (e.g., 90 days) every week on Sunday.

4.Security Group Cleanup:
Configure a CloudWatch Event rule to trigger the Lambda function to delete unused security groups every month on the first day of the month.

## Contributing
Contributions to this project are welcome! If you have ideas for additional features, improvements, or bug fixes, feel free to open an issue or submit a pull request on the GitHub repository.




