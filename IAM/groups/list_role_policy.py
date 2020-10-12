'''
iam.list_role_policies bunny-slope Python3 boto3 SDK usage
'''
import boto3

'''
generate iam client
'''
iam = boto3.client('iam')
policy = iam.list_attached_role_policies(RoleName='latam_core')
print(policy.keys())
print(policy['AttachedPolicies'])
pname=policy['AttachedPolicies'][0]['PolicyName']
parn = policy['AttachedPolicies'][0]['PolicyArn']
print(f"name:{pname} arn:{parn} just found")
