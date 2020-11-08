# Creating A VPN

A VPN is a secure tunnel between you and the internet, when you connect to a VPN your device acts as if it is on the same local network as the VPN. This means whilst browsing the internet, the device will use an encrypted connection resulting in your identity being protected.

There are multiple tools, both paid and open source, you can use to manage a VPN such as:

- TunnelBear
- Hide.me
- ExpressVPN
- NordVPN

This is **NOT** an exhaustive list or a list of recommendations, but is to highlight there are tools and services which provide VPN services out of the box.

## Pre-requisites

- In order to deploy this IaC in your AWS account you will need a registered domain.

- This stack makes use of an open source service [Dockerised OpenVPN](https://github.com/kylemanna/docker-openvpn) repo. Ultimately this allows you to manage the users allocated to the VPN you are about to create. When you add yourself to the VPN, you may need a VPN client server tool, for example [Tunnelblick](https://tunnelblick.net/). 

## Steps to Follow

The  file contains the minimal infrastructure required to set up a VPN on your AWS account. The script can be deployed using the AWS Console or the AWS cli.

Regardless of the option you choose, clone this repo so you have a copy of the stack.


### Using the AWS Console

1. In your AWS account, navigate to the **CloudFormation** service, make sure you are in the region you wish to deploy your stack in. 
2. Select **Create stack - with new resources (standard)** which will load up a form. Ensure you select upload a template file, and pick the  file.
3. To deploy this stack, fill in all the details required in the form. This includes choosing a VPC, public facing Subnet, your IP address range to name a few.
4. The stack should deploy successfully and your VPN will be ready to use.

