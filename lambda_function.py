def lambda_handler(event, context):
    num1 = event['num1']
    num2 = event['num2']
    sum = num1 + num2
    return {
        'statusCode': 200,
        'body': sum
    }
