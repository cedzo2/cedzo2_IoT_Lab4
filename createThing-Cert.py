################################################### Connecting to AWS
import boto3

import json
################################################### Create random name for things
import random
import string
import csv

################################################### Parameters for Thing

###################################################

def createThing(tID):
	global thingClient
	thingResponse = thingClient.create_thing(
		thingName = thingName
	)
	data = json.loads(json.dumps(thingResponse, sort_keys=False, indent=4))
	#print(data)
	for element in data: 
		if element == 'thingArn':
			thingArn = data['thingArn']
		elif element == 'thingId':
			thingId = data['thingId']
			print(thingId)
		createCertificate(tID)

def createCertificate(tID):
	global thingClient
	certificateName = '../certificates/device_{}/device_{}.certificate.pem'.format(tID, tID)
	publicName = '../certificates/device_{}/device_{}.public.pem'.format(tID, tID)
	privateName = '../certificates/device_{}/device_{}.private.pem'.format(tID, tID)
	certResponse = thingClient.create_keys_and_certificate(
			setAsActive = True
	)
	data = json.loads(json.dumps(certResponse, sort_keys=False, indent=4))
	print(data)
	for element in data: 
			if element == 'certificateArn':
					certificateArn = data['certificateArn']
			elif element == 'keyPair':
					PublicKey = data['keyPair']['PublicKey']
					PrivateKey = data['keyPair']['PrivateKey']
			elif element == 'certificatePem':
					certificatePem = data['certificatePem']
			elif element == 'certificateId':
					certificateId = data['certificateId']
	
	dataName = '../data/class_{}.csv'.format(tID)
	with open(publicName, 'w') as outfile:
			outfile.write(PublicKey)
	with open(privateName, 'w') as outfile:
			outfile.write(PrivateKey)
	with open(certificateName, 'w') as outfile:
			outfile.write(certificatePem)
	with open(dataName, 'w') as outfile:
			writer = csv.writer(outfile)
			writer.writerows(data)

	response = thingClient.attach_policy(
			policyName = defaultPolicyName,
			target = certificateArn
	)
	response = thingClient.attach_thing_principal(
			thingName = thingName,
			principal = certificateArn
	)

thingClient = boto3.client('iot')
#createThing()
for i in range(24):
	thingArn = ''
	thingId = ''
	thingName = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(15)])
	defaultPolicyName = 'My_Iot_Thing-Policy'
	createThing(i)