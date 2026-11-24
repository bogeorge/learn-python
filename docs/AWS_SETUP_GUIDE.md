# AWS Setup Guide for Bo

## 🎯 Goal
Set up your AWS environment for Lambda and Bedrock development.

## 📋 Prerequisites
- AWS Account (Free Tier available)
- Administrative access or ability to create IAM users
- Command line access on your computer

## 🚀 Step-by-Step Setup

### Step 1: Create AWS Account (if needed)
1. Go to [aws.amazon.com](https://aws.amazon.com/)
2. Click "Create an AWS Account"
3. Follow the sign-up process
4. **Important**: Set up billing alerts to avoid unexpected charges

### Step 2: Create IAM User for Development
**Never use root credentials for daily work!**

1. **Login to AWS Console** as root user
2. **Navigate to IAM Service**
3. **Create User**:
   - Username: `bo-lambda-dev` (or similar)
   - Select "Programmatic access"
   - Click "Next: Permissions"

4. **Attach Policies**:
   - `AWSLambda_FullAccess`
   - `AmazonBedrockFullAccess` 
   - `IAMFullAccess` (temporary, can scope down later)
   - `AmazonAPIGatewayAdministrator`
   - `AmazonS3FullAccess`
   - `AmazonDynamoDBFullAccess`
   - `CloudWatchFullAccess`

5. **Review and Create**
6. **Save Credentials**:
   - Access Key ID
   - Secret Access Key
   - **Store securely - you won't see Secret Access Key again!**

### Step 3: Install AWS CLI
**macOS (Homebrew):**
```bash
brew install awscli
```

**Linux:**
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

**Windows (PowerShell):**
```powershell
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
```

**Verify Installation:**
```bash
aws --version
```

### Step 4: Configure AWS CLI
```bash
aws configure
```

Enter when prompted:
- **AWS Access Key ID**: From Step 2
- **AWS Secret Access Key**: From Step 2
- **Default region name**: `us-east-1` (or your preferred region)
- **Default output format**: `json`

**Verify Configuration:**
```bash
aws sts get-caller-identity
```
Should return your user ARN.

### Step 5: Set Up AWS SAM (Serverless Application Model)
**AWS SAM helps develop and test Lambdas locally.**

**Install SAM CLI:**
```bash
# macOS
brew tap aws/tap
brew install aws-sam-cli

# Linux
pip install aws-sam-cli

# Windows
# Download from: https://github.com/aws/aws-sam-cli/releases
```

**Verify SAM:**
```bash
sam --version
```

### Step 6: Install Docker (for SAM local testing)
**SAM uses Docker to run Lambdas locally.**

**macOS:**
```bash
brew install --cask docker
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install docker.io

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker
```

**Windows:**
- Download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop)

**Verify Docker:**
```bash
docker --version
```

### Step 7: Set Up Python Environment
**Already done in this workspace, but verify:**

```bash
cd /Users/bogeorge/GitHub/bogeorge/aflac-learning

# Create/activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install AWS SDK
pip install boto3
pip install aws-sam-cli  # If not installed globally
```

### Step 8: Test AWS Access

**Create test script `test_aws.py`:**
```python
import boto3
import json


# Test basic AWS access
def test_aws_access():
    print("Testing AWS Access...")

    # Create clients
    sts = boto3.client("sts")
    lambda_client = boto3.client("lambda")

    # Test STS (always works if credentials are valid)
    identity = sts.get_caller_identity()
    print(f"✅ AWS Identity: {identity['Arn']}")

    # Test Lambda access (list functions)
    try:
        functions = lambda_client.list_functions(MaxItems=5)
        print(f"✅ Lambda Access: Can list functions")
        if functions["Functions"]:
            print(f"   Found {len(functions['Functions'])} functions")
    except Exception as e:
        print(f"⚠️  Lambda Access Issue: {e}")
        print("   This is OK if you haven't created any Lambdas yet")

    # Test region
    session = boto3.Session()
    region = session.region_name
    print(f"✅ Region: {region}")

    return True


if __name__ == "__main__":
    test_aws_access()
```

**Run test:**
```bash
python test_aws.py
```

## 🎮 Your First Lambda Deployment

### Method 1: AWS Console (Easiest)
1. **Go to Lambda Console**
2. **Click "Create function"**
3. **Choose "Author from scratch"**
4. **Configure**:
   - Function name: `hello-world-bo`
   - Runtime: Python 3.12
   - Architecture: x86_64
   - Permissions: Create new role

5. **Write code** in inline editor:
```python
import json


def lambda_handler(event, context):
    return {"statusCode": 200, "body": json.dumps("Hello from Bo's first Lambda!")}
```

6. **Click "Deploy"**
7. **Click "Test"** → Create new test event → Use default template
8. **Click "Test"** to run

### Method 2: AWS CLI
**Create deployment package:**
```bash
mkdir hello-lambda
cd hello-lambda

# Create Lambda code
cat > lambda_function.py << 'EOF'
import json

def lambda_handler(event, context):
    name = event.get('name', 'World')
    return {
        'statusCode': 200,
        'body': json.dumps(f'Hello {name} from CLI deployment!')
    }
EOF

# Create zip (Lambda expects .zip)
zip function.zip lambda_function.py
```

**Deploy via CLI:**
```bash
# Create IAM role first (one-time)
aws iam create-role \
    --role-name lambda-basic-execution \
    --assume-role-policy-document '{
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {"Service": "lambda.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }]
    }'

# Attach policy to role
aws iam attach-role-policy \
    --role-name lambda-basic-execution \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

# Create Lambda function
aws lambda create-function \
    --function-name hello-cli \
    --runtime python3.12 \
    --role arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/lambda-basic-execution \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://function.zip \
    --region us-east-1
```

### Method 3: AWS SAM (Recommended for development)
**Create SAM template `template.yaml`:**
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: hello_world/
      Handler: app.lambda_handler
      Runtime: python3.12
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```

**Create function code `hello_world/app.py`:**
```python
import json


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello from SAM deployment!", "input": event}),
    }
```

**Deploy with SAM:**
```bash
# Build and deploy
sam build
sam deploy --guided
```

## 🔧 Development Workflow

### Local Development with SAM
```bash
# Initialize new SAM project
sam init --runtime python3.12 --name my-lambda-app

# Build project
sam build

# Test locally
sam local invoke HelloWorldFunction --event event.json

# Start local API
sam local start-api

# Deploy to AWS
sam deploy --guided
```

### Testing Lambda Locally
**Create `test_event.json`:**
```json
{
  "httpMethod": "GET",
  "path": "/hello",
  "queryStringParameters": {
    "name": "Bo"
  }
}
```

**Test:**
```bash
sam local invoke HelloWorldFunction -e test_event.json
```

## 📊 Monitoring Setup

### CloudWatch Logs
Lambdas automatically log to CloudWatch. View logs:
```bash
# Get last 10 log events
aws logs get-log-events \
    --log-group-name /aws/lambda/hello-world-bo \
    --log-stream-name $(aws logs describe-log-streams \
        --log-group-name /aws/lambda/hello-world-bo \
        --order-by LastEventTime \
        --descending \
        --max-items 1 \
        --query 'logStreams[0].logStreamName' \
        --output text) \
    --limit 10
```

### CloudWatch Metrics
Monitor invocation metrics:
- Invocations
- Errors
- Duration
- Throttles

## 🛡️ Security Best Practices

### IAM Principle of Least Privilege
Start broad for learning, then tighten:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "lambda:InvokeFunction",
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
```

### Environment Variables for Secrets
**Never hardcode secrets!**
```python
import os
import boto3
from botocore.exceptions import ClientError


def get_secret():
    secret_name = os.environ["DB_PASSWORD_SECRET"]
    region_name = os.environ["AWS_REGION"]

    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    try:
        response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise e

    return response["SecretString"]
```

## 💰 Cost Management

### Free Tier (Always Free):
- 1M Lambda requests/month
- 400,000 GB-seconds of compute time/month
- Basic Bedrock model inference (limited)

### Set Billing Alerts:
1. Go to Billing Dashboard
2. Set up Cost Explorer
3. Create billing alerts at $10, $25, $50 thresholds
4. Use Cost Allocation Tags

## 🚨 Troubleshooting

### Common Issues:

1. **"Access Denied" errors**
   ```bash
   # Check your IAM permissions
   aws iam get-user
   ```

2. **Lambda timeouts**
   - Increase timeout in configuration
   - Optimize code
   - Check external dependencies

3. **Cold starts**
   - Use provisioned concurrency
   - Keep packages small
   - Initialize clients outside handler

4. **Package too large**
   - Use Lambda Layers
   - Remove unnecessary dependencies
   - Compress assets

### Debug Commands:
```bash
# Check Lambda configuration
aws lambda get-function --function-name hello-world-bo

# Invoke Lambda directly
aws lambda invoke --function-name hello-world-bo output.json

# View CloudWatch logs
aws logs tail /aws/lambda/hello-world-bo --follow
```

## 📚 Next Steps for Bo

### Week 1 Goals:
1. ✅ Set up AWS account and CLI
2. ✅ Deploy first Lambda (all 3 methods)
3. ✅ Test Lambda locally with SAM
4. ✅ Set up monitoring
5. ✅ Understand basic IAM roles

### Week 2 Goals:
1. Integrate with S3
2. Use DynamoDB from Lambda
3. Create API Gateway endpoints
4. Implement error handling
5. Set up CI/CD pipeline

### Learning Resources:
- **AWS Lambda Docs**: https://docs.aws.amazon.com/lambda/
- **AWS SAM Docs**: https://docs.aws.amazon.com/serverless-application-model/
- **Serverless Land**: https://serverlessland.com/
- **AWS re:Invent Videos**: Search "Lambda" on YouTube

---

## 🎉 You're Ready to Build!

Your AWS environment is now set up for Lambda development. Start with the exercises in `lambda_day1.py` to practice Lambda patterns, then deploy your own functions.

**Remember**: 
- Start simple and iterate
- Test locally before deploying
- Monitor costs
- Follow security best practices

Happy building with AWS Lambda! 🚀

---

*Setup guide customized for Bo's AWS Lambda learning journey*
*Last updated: November 18, 2024*