# Serverless Order Management System

This project implements a fully serverless, event-driven order processing application using AWS services. It is deployed through a continuous integration and deployment (CI/CD) pipeline powered by GitHub Actions and AWS SAM (Serverless Application Model).

## Overview

The system handles order placement, delivery updates, and customer notifications using AWS Lambda, API Gateway, DynamoDB, and SNS. All components are provisioned and managed using Infrastructure-as-Code via `template.yaml`, and deployed automatically on push to the `master` branch.

## Architecture

- API Gateway handles HTTP requests and routes them to corresponding Lambda functions.
- PlaceOrderFunction stores the order in DynamoDB and publishes to an SNS topic.
- UpdateDeliveryFunction updates the delivery status of an existing order.
- NotifyCustomerFunction is subscribed to the SNS topic and notifies the customer via email or Lambda-based processing.

## Architecture Diagram
Client 
  v 
API Gateway 
  v 
PlaceOrderFunction -----> DynamoDB: OrderTable 
                                   v
                          SNS:OrderSNSTopic -----> NotifyCustomerFunction + Email Subscribers
                          UpdateDeliveryFunction <----- PUT/order/update
                                                              v
                                                     DynamnoDB:OrdersTable


## Technology Stack

- Python 3.9
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon SNS
- AWS SAM
- GitHub Actions

## API Endpoints

### POST /order

Places a new order.

bash
curl -X POST https://<api-id>.execute-api.us-east-1.amazonaws.com/Prod/order \
  -H "Content-Type: application/json" \
  -d '{"customer_name": "Alice", "item": "Laptop"}'

## PUT /order/update
curl -X PUT https://<api-id>.execute-api.us-east-1.amazonaws.com/Prod/order/update \
  -H "Content-Type: application/json" \
  -d '{"order_id": "your-order-id", "status": "Shipped"}'
  
## CI/CD Pipeline
This project uses GitHub Actions to automate build and deployment:

Trigger: git push to master branch

Builds using sam build --use-container

Deploys using sam deploy

## Required GitHub Secrets
To securely authenticate with AWS, the following secrets must be set in your GitHub repository:

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

These credentials must have permission to deploy using AWS SAM and manage CloudFormation, Lambda, API Gateway, DynamoDB, and SNS.

## Diagram

project/
├── app/
│   ├── place_order.py
│   ├── update_delivery.py
│   └── notify_customer.py
├── template.yaml
├── samconfig.toml
└── .github/
    └── workflows/
        └── deploy.yml

## Status
All components deployed and functioning as expected

Orders are stored in DynamoDB and updated via API Gateway

SNS notifications trigger both Lambda function and email subscribers

CI/CD pipeline is fully automated and integrated with GitHub Actions

Author
Chen Wang
Johns Hopkins University
GitHub: https://github.com/wchen4521
