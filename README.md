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

### **1. Clone this project to EC2**