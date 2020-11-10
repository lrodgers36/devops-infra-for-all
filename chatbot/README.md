# AWS Chatbot & Slack Integration 

At the 2019 re:Invent, AWS announced the launch of [Chatbot](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) - See the [video](https://www.youtube.com/watch?v=u-1SbynvVkA) here.

By integrating AWS Chatbot with Slack, DevOps team can utilise the benefits of the ChatOps model in their day-to-day responsibilities. 

The content provided here is to illustrate the code used behind the scenes for the demostration which took place at the DevOps Meetup on 2020-11-11.

There are numerous IaC scripts available in this directory:

**Slack Channel Setup**
- `chatbot.yml` 

**Chatbot Slack Use Cases**
In the future, additional use cases will be added to this repo.

Invoking Lambda from Slack
- `usecases/serverless.yml`

# Chatbot Infrastructure
*As of 2020-11-09*

## Gotcha's

The purpose of the `chatbot.yml` stack is to subscribe SNS topics on a per Slack channel integration. The functionality of AWS Chatbot and creating IaC (via CloudFormation) is in its infancy. Below are some caveats when using AWS Chatbot as part of your IaC:

| Consideration | Reason | Iac Supported |
| ------------- | ------ | --------- |
| Configuring Clients | Setting up AWS Chatbot requires creating a client for Amazon Chime or Slack. This is only possible through the AWS Console and can not be managed through other services. | No |

## Steps to Follow

1. After the chatbot client is configured and any infrastructure with SNS topics already deployed, the `chatbot.yml` stack can be deployed in CloudFormation.
2. Some of the inputs to the stack require the Slack Workspace and Channel ID. The former can be located in the AWS Console. Obtaining the Slack channel ID is a little ambiguous but the following screenshot from the AWS documentation provides an explanation.
![Slack Channel ID](/images/slack-channel.png)
3. Once the stack is deployed any incoming notifications should start appearing in your Slack channels when SNS topics are triggered.

If you wish to append additional SNS topics to the same Slack channel then the stack can be updated and the list of topics can be extended.

# Invoking Lambda From Slack

This particular example demonstrates the infrastructure used to create a Lambda function which is capable of restarting an EC2 instance by sending a SSM command to the server. 
The Lambda Function is tailored to the demostration shown at the Meetup, however the same principles can be applied when constructing other functionalities.

## Steps to Follow 

The following serverless application is deployed using the [Serverless Framework](https://www.serverless.com/framework/docs/providers/aws/guide/intro/)

1. The `sample.env` is a template to provide AWS resources you wish to pass as environment variables. Rename this file as `.env` and fill in with your AWS resources.
2. In the directory containing the `serverless.yml` execute the following

`sls deploy --region <REGION>`
