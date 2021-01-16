import json

def new_fun() {
  print("Happy New Year 2021..!!")
  
  print("Happy New Year 2021..!!")

  return "Happy New Year 2021..!!"
}

def lambda_handler(event, context):
    body = "Hello from Lambda!"
    statusCode = 200
    return {
        "statusCode": statusCode,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "application/json"
        }
    }