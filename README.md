# Two-Tier Web Application Architecture on AWS

## Project Description

This project demonstrates a scalable and secure **Two-Tier Web Application Architecture** deployed on AWS using private EC2 instances, Application Load Balancer, Auto Scaling Group, and DynamoDB.

# What is Two-Tier Architecture?

Two-tier architecture divides the application into two logical layers:

## Tier 1 — Application Tier

This layer contains the application components responsible for processing user requests.

Components used:

* Application Load Balancer (ALB)
* Auto Scaling Group (ASG)
* Private EC2 Instances
* Flask Web Application
* Python boto3 SDK

Responsibilities:

* Receive user requests
* Process business logic
* Connect to database layer
* Scale automatically during high traffic

---

## Tier 2 — Database Tier

This layer stores application data.

Component used:

* Amazon DynamoDB

Responsibilities:

* Store user information
* Retrieve stored data
* Provide persistent storage for the application

---

# Architecture Overview

```text
Users
   ↓
Internet
   ↓
Application Load Balancer
   ↓
Private EC2 Instances (Auto Scaling Group)
   ↓
Amazon DynamoDB
```

---

# How This Project Works

The project hosts a Flask application inside private EC2 instances.

Users access the application using the Load Balancer DNS.

The Flask application communicates with DynamoDB using IAM role permissions and boto3 SDK.

Since EC2 instances are deployed in private subnets, they are not directly accessible from the internet.

Management access is provided using AWS Systems Manager Session Manager.

---

# Project Flow

## Step 1 — User Sends Request

Users open:

```text
http://ALB-DNS
```

Traffic first reaches the Application Load Balancer.

---

## Step 2 — Load Balancer Routes Traffic

The Application Load Balancer forwards requests to healthy EC2 instances running inside private subnets.

Benefits:

* High Availability
* Load Distribution
* Fault Tolerance

---

## Step 3 — EC2 Processes Request

Private EC2 instances:

* Run Flask Application
* Execute business logic
* Use boto3 SDK
* Communicate with DynamoDB

The application is deployed through Launch Templates and Auto Scaling.

---

## Step 4 — Data Stored in DynamoDB

The Flask application stores and retrieves data from DynamoDB.

Example:

```text
User submits form
       ↓
Flask receives request
       ↓
boto3 API call
       ↓
DynamoDB stores item
```

---

# Networking Design

## Public Layer

Contains:

* Internet Gateway
* NAT Gateway
* Application Load Balancer

Purpose:

* Receive internet traffic
* Provide outbound internet for private resources

---

## Private Layer

Contains:

* EC2 Instances
* Application Servers

Purpose:

* Increase security
* Prevent direct internet access

---

# Security Implementation

Security mechanisms used:

* Private EC2 Instances
* IAM Roles
* Session Manager Access
* Security Groups
* VPC Endpoints
* No public IP on application servers

---

# High Availability Features

This architecture provides:

* Multi-AZ deployment
* Auto Scaling
* Load Balancing
* Fault Tolerance
* Horizontal Scaling

---

# AWS Services Used

* VPC
* EC2
* Auto Scaling Group
* Application Load Balancer
* DynamoDB
* IAM
* Session Manager
* NAT Gateway
* VPC Endpoints

---

# Conclusion

This project demonstrates how to build a production-style two-tier architecture where the application layer and database layer are separated for scalability, security, and reliability.
