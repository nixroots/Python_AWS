import boto3
ec2 = boto3.resource('ec2')

#Create key file locally
outfile = open('ec2-keypair.pem', 'w')

#calling boto function
key_pair = ec2.create_key_pair(KeyName='ec2-keypair')

#capture key and store it in a file

KeyPairOut = str(key_pair.key_material)
print(KeyPairOut)
outfile.write(KeyPairOut)
