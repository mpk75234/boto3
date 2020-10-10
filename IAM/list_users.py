'''
Using the list_users() on a basic level
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.list_users
'''
import boto3
iam = boto3.client('iam')
x = iam.list_users()
print(x)
'''
returned
{'Users': [{'Path': '/', 'UserName': 'mike', 'UserId': 'AIDASLJ6LMJ7RJZ6TRACW'
, 'Arn': 'arn:aws:iam::161728914047:user/mike', 'CreateDate': datetime.datetim
e(2020, 10, 8, 21, 48, 54, tzinfo=tzutc())}], 'IsTruncated': False, 'ResponseM

etadata': {'RequestId': '5e6b0f74-4889-4957-89a2-cde45882ad1d', 'HTTPStatusCod
e': 200, 'HTTPHeaders': {'x-amzn-requestid': '5e6b0f74-4889-4957-89a2-cde45882
ad1d', 'content-type': 'text/xml', 'content-length': '545', 'date': 'Sat, 10 O
'''
print(x['Users'][0]['UserName'])
'''
returned

{'Users': [{'Path': '/', 'UserName': 'mike', 'UserId': 'AIDASLJ6LMJ7RJZ6TRACW'
, 'Arn': 'arn:aws:iam::161728914047:user/mike', 'CreateDate': datetime.datetim
e(2020, 10, 8, 21, 48, 54, tzinfo=tzutc())}], 'IsTruncated': False, 'ResponseM
etadata': {'RequestId': '8f7204ff-6ae8-4274-9c25-3bb800f340dc', 'HTTPStatusCod

e': 200, 'HTTPHeaders': {'x-amzn-requestid': '8f7204ff-6ae8-4274-9c25-3bb800f3
40dc', 'content-type': 'text/xml', 'content-length': '545', 'date': 'Sat, 10 O
ct 2020 15:23:40 GMT'}, 'RetryAttempts': 0}}
mike <---see?
'''
