import boto3
import os
import time

ec2_client = boto3.client('ec2')
ssm_client = boto3.client('ssm', region_name = os.environ['REGION'])

def get_state(instance):
  try:
    response = ec2_client.describe_instances(
      InstanceIds = [
        instance
      ]
    )
    state = response['Reservations'][0]['Instances'][0]['State']['Name']
  except Exception as e:
    message = f'Unable to Retrieve information on Instance - {instance}:\n{e}'
    raise Exception(message)
  return state

def start_server(instance):
  try:
    res = ec2_client.start_instances(
      InstanceIds = [
        instance
      ]
    )
    server = res['StartingInstances'][0]
    state = server['CurrentState']['Name']
    while state != 'running':
      print(f'Server is {state}')
      time.sleep(5) 
      state = get_state(instance)
  except Exception as e:
    message = f'Unable to Start Instance - {instance}:\n{e}'
    raise Exception(message)

def send_command(instance, port):
  print(port)
  print(instance)
  print(get_state(instance))
  try:
    response = ssm_client.send_command(
      InstanceIds = [
        instance 
      ],
      DocumentName = os.environ['SSM_RESTART'],
      Parameters = {
        'websitePort': [
          port
        ]
      }
    )
    status = response['Command']['Status']
  except Exception as e:
    message = f'Unable to Send Command - {instance}:\n{e}'
    raise Exception(message)
  return status

def main(event, context):
  instance = event['INSTANCE']
  instance_state = get_state(instance)
  if instance_state == 'running':
    message = 'No action taken, server is running'
  elif instance_state == 'stopped':
    start_server(instance)
    state = get_state(instance)
    print(state)
    time.sleep(20)
    send_command(instance, "8000")
    message = f'Server State: {state}. Website is running'
  else:
    message = 'ERROR'

  instance_state = get_state(instance)
  body = {
    'response': instance_state,
    'message': message
  }

  return body

if __name__ == "__main__":
  main('', '')