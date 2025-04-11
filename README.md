# Project III – Serverless Order Management System

This serverless application processes and manages customer orders using AWS Lambda, API Gateway, DynamoDB, and SNS. The project is deployed using a CI/CD pipeline with GitHub Actions.

## Components
- API Gateway: Exposes HTTP endpoints
- Lambda Functions:
  - placeOrder
  - updateDeliveryStatus
  - notifyCustomer
- DynamoDB: Stores order records
- SNS: Sends notifications on order placement
- CI/CD: GitHub Actions + AWS SAM

## Deployment

### Pre-requisites
- AWS CLI and SAM CLI installed
- AWS credentials configured
- GitHub secrets set for `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`

### Local Deployment
```bash
sam build
sam deploy --guided
```

### CI/CD
Push to `main` branch triggers auto deployment via GitHub Actions
