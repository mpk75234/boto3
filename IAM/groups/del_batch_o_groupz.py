'''
ludicrous example of create_group from boto3 Python3 SDK
'''
import boto3

'''
generate IAM client
'''
iam = boto3.client('iam')

g = ['latam_core', 'apac_core', 'nam_core', 'eur_core', 'brazil_core', 'brazil_bau','latam_bau', 'apac_bau', 'nam_bau', 'eur_bau']

h = iter(g)
#print(dir(h))
while(next(h)):
    try:
        #print(next(h))
        iam.delete_group(GroupName=next(h))
    except StopIteration:
        print("DONE")
        '''
        StopIteration exception message isn't printing..will look it up shoon
        '''
