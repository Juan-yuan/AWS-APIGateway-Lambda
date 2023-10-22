# AWS-APIGateway-Lambda
build a serverless image processing API using a Lambda function and AWS API Gateway 

## Convert Image to Base64: https://www.base64encoder.io/image-to-base64-converter/
## converter Base64 to image: https://codebeautify.org/base64-to-image-converter

## Agenda:
  1. create a colorConverslonBGR2GRAY lambda function
    * test lambda function:
      - 1. open this link: https://www.base64encoder.io/image-to-base64-converter/
      - 2. upload a png file to this web site, and copy the Base64 Encoded String values
      - 3. go to Configure test event
        * Event name: testEvent
        * modify the Event JSON value as: {
            "body": "value from step 2".
          }
  2. create a python-apigateway-lambda bucket in S3  (architectures: x86_64)
    - 1. upload python-aws-apigateway-lambda.zip file to python-apigateway-lambda bucket file
    - 2. copy the S3 folder link: https://python-apigateway-lambda.s3.ap-southeast-2.amazonaws.com/python-package.zip
    - 3. open lambda console, click: Layers
    - 4. Create Layer:   (architectures: x86_64)
          * name: opencv-numpy-imageProcessingAPI
          * select: Upload a file from Amazon S3
          * Amazon S3 link URL: (paste the S3 folder link here:https://python-apigateway-lambda.s3.ap-southeast-2.amazonaws.com/python-package.zip)
    - 5. Compatible runtimes - optional: Python 3.8 (need the same version with the lambda function)

  3. back to colorConverslonBGR2GRAY lambda function page:
    - 1. scroll all down find Layers -> click: Add a layer
    - 2. select: Custom layers
    - 3. select the layer name and version

  4. in the lambda function, click Test, will get the succes test result as:
    {
      "statusCode": 200,
      "body": "xxx long lines",
      "isBase64Encoded": true,
      "headers": {
        "content-type": "image/png"
      }
    }

  5. create API Gateway
    1. go to API Gateway console
    2. REST API -> build 
    3. NEW API -> API name: imageProcessingAPI -> create
    4. Create method -> Method type: POST -> 
        * Integration type: Lambda function -> 
        * select: Lambda proxy integration ->
        * Lambda function: colorConverslonBGR2GRAY
    5. click: Deploy API
        * stage: *New stage*
        * Stage name: dev

  6. Test API Gatewar:
    1. click: Test
    2. Request body: "past Base64 Encoded String values"
    3. Check response status if is 200


