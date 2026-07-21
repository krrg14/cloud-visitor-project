## 🚨Currently this project is live now check out at : https://dzh12lth55m0i.cloudfront.net/

# AWS Cloud-Visitor-Project

## Project Overview

~ This project is an implementation of the AWS Cloud Visitor Challenge. It hosts a static website on Amazon S3 and displays a live visitor counter using a serverless backend.

~ The frontend is served through Amazon CloudFront, while API Gateway, AWS Lambda, and DynamoDB work together to update and retrieve the visitor count.

## Architecture
<img width="1361" height="670" alt="Screenshot 2026-07-15 143924" src="https://github.com/user-attachments/assets/7c737bd5-df7e-4269-a687-13165a4e1044" />

## Architecture Flow

1. CloudFront receives the request from user.
2. CloudFront serves the static website stored in Amazon S3.
3. JavaScript on the webpage sends an HTTP request to API Gateway.
4. API Gateway triggers the AWS Lambda function.
5. Lambda reads the current visitor count from DynamoDB.
6. Lambda increments the visitor count.
7. Lambda updates DynamoDB with the new count.
8. Lambda returns the updated visitor count to API Gateway.
9. API Gateway sends the response back to the website.
10. JavaScript displays the latest visitor count on the webpage.


## AWS Services Used

- Amazon S3
- Amazon CloudFront
- Amazon Route 53 
- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB
- AWS IAM

# Implementation Steps

# Step 1
Created the project structure for the frontend (HTML, CSS, and JavaScript) and backend (AWS Lambda).

---

# Step 2

Provisioned the Amazon S3 static website hosting infrastructure using Terraform.
---

<img width="817" height="1014" alt="Screenshot 2026-07-15 153351" src="https://github.com/user-attachments/assets/c2299ec4-a12a-49e1-85be-715f7c721591" />

---

# Step 3
Configured Amazon S3 for static website hosting and uploaded the frontend application files.
---
<img width="1919" height="806" alt="Screenshot 2026-07-15 161636" src="https://github.com/user-attachments/assets/e76be1a2-7b33-4ac7-ba21-b03aa8a7a67b" />

---

# Step 4
Created a CloudFront distribution with the S3 bucket as the origin to improve performance and enable secure content delivery.
---
<img width="1919" height="815" alt="Screenshot 2026-07-15 162232" src="https://github.com/user-attachments/assets/9f567b4c-dd64-4a55-b76f-250e0f351d92" />

---

# Step 5
Created a DynamoDB table to store the visitor count.
---
<img width="1919" height="801" alt="Screenshot 2026-07-15 162709" src="https://github.com/user-attachments/assets/9bde0ba6-2e53-47b8-a501-25f24c4821bc" />

---

# Step 6
Developed an AWS Lambda function to retrieve, increment, and update the visitor count in DynamoDB.
---
<img width="1919" height="807" alt="image" src="https://github.com/user-attachments/assets/23a87695-8fbb-455c-981a-ce685bcfb429" />

---

# Step 7
Created an IAM role and attached the required permissions for Lambda to access DynamoDB and CloudWatch Logs.
---
<img width="1918" height="800" alt="Screenshot 2026-07-15 163957" src="https://github.com/user-attachments/assets/e7076c3e-8020-4d0f-8900-32b5a5159b85" />

---

# Step 8
Created a HTTP API using Amazon API Gateway and integrated it with the Lambda function.
---
<img width="1915" height="809" alt="Screenshot 2026-07-15 164420" src="https://github.com/user-attachments/assets/ff1ccf36-aa16-4be1-a4d6-e164db21d92f" />

---

# Step 9
Updated the frontend JavaScript to invoke the API Gateway endpoint and display the live visitor count.
---
<img width="1919" height="1019" alt="Screenshot 2026-07-15 165751" src="https://github.com/user-attachments/assets/b012968d-0a2a-46f4-a4bc-27caf61ebc2a" />

---

# Step 10
Verified that the visitor counter increments successfully on each page visit.
---
<img width="1919" height="1016" alt="Screenshot 2026-07-15 170204" src="https://github.com/user-attachments/assets/cd92b890-40a9-4c69-9cca-58cfedb600d4" />

---

# Workflow
```
   User
    ↓
CloudFront
    ↓
S3 Website
    ↓
JavaScript Fetch API
    ↓
API Gateway
    ↓
Lambda Function
    ↓
DynamoDB
    ↓
Lambda Response
    ↓
API Gateway
    ↓
Website Updates Visitor Count
```
---

## Features

- Static website hosting
- Serverless backend
- Live visitor counter
- Global content delivery using CloudFront
- Custom domain with Route 53
- No server management required
- Highly scalable architecture

---
