# AWS API Gateway and Lambda - Image Processing

This repository demonstrates how to build a serverless image processing API using an AWS Lambda function and AWS API Gateway.

## Image Conversion Tools
- [Convert Image to Base64](https://www.base64encoder.io/image-to-base64-converter/)
- [Convert Base64 to Image](https://codebeautify.org/base64-to-image-converter)

## Agenda

### 1. Create the `colorConversionBGR2GRAY` Lambda Function

Follow these steps to create and test the `colorConversionBGR2GRAY` Lambda function:

- Open the [Image-to-Base64 Converter](https://www.base64encoder.io/image-to-base64-converter/) tool.
- Upload a PNG file to the website and copy the Base64 encoded string.
- Go to the AWS Lambda Management Console.
- Configure a test event named `testEvent` with the following JSON:

```json
{
  "body": "Base64EncodedStringValueFromStep2"
}
```

### 2. Create a `python-apigateway-lambda` bucket in S3  (architectures: x86_64)
- Upload python-aws-apigateway-lambda.zip file to python-apigateway-lambda bucket file
- Copy the S3 folder link: https://python-apigateway-lambda.s3.ap-southeast-2.amazonaws.com/python-package.zip
- Open lambda console, click: Layers
- Create Layer:   (architectures: x86_64)
      - name: opencv-numpy-imageProcessingAPI
      - select: Upload a file from Amazon S3
      - Amazon S3 link URL: (paste the S3 folder link here:https://python-apigateway-lambda.s3.ap-southeast-2.amazonaws.com/python-package.zip)
- Compatible runtimes - optional: Python 3.8 (need the same version with the lambda function)

### 3. Back to `colorConverslonBGR2GRAY` lambda function page:
    1. Ccroll all down find Layers -> click: Add a layer
    2. select: Custom layers
    3. select the layer name and version

###  4. In the lambda function:
- Click Test, will get the succes test result as:
```json
    {
      "statusCode": 200,
      "body": "xxx long lines",
      "isBase64Encoded": true,
      "headers": {
        "content-type": "image/png"
      }
    }
```

###  5. Create API Gateway
  1. Go to API Gateway console
  2. REST API -> build 
  3. NEW API -> API name: imageProcessingAPI -> create
  4. Create method -> Method type: POST -> 
      - Integration type: Lambda function -> 
      - select: Lambda proxy integration ->
      - Lambda function: colorConverslonBGR2GRAY
  5. Click: Deploy API
      - stage: *New stage*
      - Stage name: dev

###  6. Test API Gatewar:
  1. Click: Test
  2. Request body: "past Base64 Encoded String values"
  3. Check response status if is 200

### 7. Find your API link and handle it:
  1. Click: Stages (API Gateway console)
  2. Invoke URL: copy it to main.py file API_ENDPOINT variable
  3. back to main.py file, run it, then will call API gateway to get the grey color image.


