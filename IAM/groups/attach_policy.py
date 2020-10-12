'''
bunny-slope hard-coded policy attachment using Python3 boto3 SDK
'''
import boto3

'''
generate client
'''
iam = boto3.client('iam')

#iam.attach_group_policy(GroupName='brazil_bau',PolicyArn='arn:aws:iam::161728914047:policy/latam_core_ec2_codedeploy')
pz = iam.list_role_policies()
print(pz)
