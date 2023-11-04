# python-aws-lambda
A simple example of running a python code snippet serverless using AWS Lambda service via Localstack 

## How to run

**Setup localstack to simulate AWS by docker-compose:**
 - `docker compose up -d`

**Create a Lambda function:**
 - Already existing on `lambda_function.py`

**Compress the python code snippet to a zip file:**
 - `zip lambda.zip lambda_function.py`

**Install `awscli-local` and `awscli`:**

```
pip install awscli-local
pip install awscli
```

**Create a new Lambda function:**

```
awslocal lambda create-function \
    --function-name lambda_function \
    --runtime python3.8 \
    --zip-file fileb://lambda.zip \
    --handler lambda_function.lambda_handler \
    --role arn:aws:iam::000000000000:role/lambda-role
```

**Invoke the Function:**

```
awslocal lambda invoke --function-name lambda_function \
    --payload '{"num1": 5, "num2": 15}' output.txt
```

**Check the result:**
 - `cat output.txt`

```
{"statusCode": 200, "body": 20}
```

**Create a Function URL:**

```
awslocal lambda create-function-url-config \
    --function-name lambda_function \
    --auth-type NONE
```
This will generate a HTTP URL that can be used to invoke the Lambda function. The URL will be in the format `http://<XXXXXXXX>.lambda-url.us-east-1.localhost.localstack.cloud:4566`

**Trigger the Lambda function URL:**

```
curl -X POST \
    'http://iu4s187onr1oabg50dbvm77bk6r5sunk.lambda-url.us-east-1.localhost.localstack.cloud:4566/' \
    -H 'Content-Type: application/json' \
    -d '{"num1": "10", "num2": "10"}'
```
