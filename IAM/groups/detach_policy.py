'''
detach group policy using Python3 boto3 SDK
'''
import boto3

'''
generate client
'''
iam = boto3.client('iam')
group='brazil_bau'
arn='arn:aws:iam::161728914047:policy/latam_core_ec2_codedeploy'

#iam.detach_group_policy(GroupName=group,PolicyArn=arn)
print(f"listing policies attached to {group}")
iam.list_group_policies(GroupName=group)
