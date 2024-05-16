# EC2 Instance Operator API


## 🤖 Introduction


This tutorial will walk you through controlling an AWS EC2 instance via an API gateway endpoint, which is connected to a Lambda function. To illustrate, we'll utilize the EC2 instance already set up to deploy our ML Flask app. You can access the app's repository via this GitHub link:[ML Flask App Repository](https://github.com/Baraa-Rayed/ML_Flask_app.git).

## 📋 <a name="features">Features</a>

## 🔋 Features

- Set up an API Gateway endpoint.
- Create a Lambda function.
- Deploy Python code to the Lambda function, enabling it to start and stop the EC2 instance.
- Establish a connection between the API Gateway endpoint and the Lambda function, ensuring the deployment allows invocation of the Lambda function.


## 📋 <a name="table">Table of Contents</a>

## ⚙️ Tech Stack

- Python
- Lambda
- API Gateway
- AWS EC2

## Architecture

<p align="center">
     <img src="https://github.com/Baraa-Rayed/EC2-Instance-Operator-API/assets/101131013/4fa6198d-9619-457c-81c5-67816916efe6"

</p>

## 🧰 Getting Started

### Prerequisites

- An AWS account
- Basic knowledge of Python and Flask
- Familiarity with EC2

## **Steps**

### **1. Clone the project to EC2 link:[ML Flask App Repository](https://github.com/Baraa-Rayed/ML_Flask_app.git)**

- Please refer to the README file for the provided repo link and follow the steps to deploy the project to the EC2 instance.
- Make sure that your project works fine by referring to the HTTP link with the public IP address of the EC2 instance.
- Here we go. If everything works fine, you will see something like the provided SC below.

### **2. Create Lamba Function**

- Now navigate to the AWS consolem in the search box search for lambda click on it.
- Clicks on 'Create a Function' button 
- Enter a function name, something like: **lambdasatrtandstopmachine**
- For python version choose a version >=3.9
- For exection role click on IAM console lin for navigate to IAM
     1. Create a Policy
       - Select JSON, copy the JSON format below, and paste it into the policy editor.
        ```bash
          {
          "Version": "2012-10-17",
          "Statement": [
          {
               "Effect": "Allow",
               "Action": [
               "logs:CreateLogGroup",
               "logs:CreateLogStream",
               "logs:PutLogEvents"
               ],
               "Resource": "arn:aws:logs:*:*:*"
          },
          {
               "Effect": "Allow",
               "Action": [
               "ec2:Start*",
               "ec2:Stop*"
               ],
               "Resource": "*"
          }
          ]
          }
          ```
       - enter Policy name, something like: **lambdasatrtandstopEC2**
       - 