'''
using the create_user function on a very bunny-slope level:
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.create_user
'''
import boto3
'''first we add the client'''
iam = boto3.client('iam')
'''now we use create_user'''
iam.create_user(UserName='Dashnee')
'''
reading...
mike@mkdc752341u:~/Desktop/AWS/boto3/IAM$ python3 list_users.py
{'Users': [{'Path': '/', 'UserName': 'Dashnee', 'UserId': 'AIDASLJ6LMJ774WV2QZ
PD', 'Arn': 'arn:aws:iam::161728914047:user/Dashnee', 'CreateDate': datetime.d
atetime(2020, 10, 10, 15, 39, 58, tzinfo=tzutc())}, {'Path': '/', 'UserName':
'mike', 'UserId': 'AIDASLJ6LMJ7RJZ6TRACW', 'Arn': 'arn:aws:iam::161728914047:u
ser/mike', 'CreateDate': datetime.datetime(2020, 10, 8, 21, 48, 54, tzinfo=tzu
tc())}], 'IsTruncated': False, 'ResponseMetadata': {'RequestId': '16a59bb0-91e
1-4397-9c42-7ae99c693765', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requ

estid': '16a59bb0-91e1-4397-9c42-7ae99c693765', 'content-type': 'text/xml', 'c
ontent-length': '795', 'date': 'Sat, 10 Oct 2020 15:40:08 GMT'}, 'RetryAttempt
s': 0}}
Dashnee
'''
