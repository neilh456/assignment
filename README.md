# Assignment
## Assignment to build a small app

This repo creates a small flask app that returns the country of the requester IP. Github actions are run to test the python code and the return values of the flask app. I have not added a github action workflow for created a docker image on the local macos dockerd daemon.

## Build Docker image on MacOS
- Start docker desktop
- Checkout latest code
- `docker image build -t ipapp_docker .`
- `docker run -p 4000:4000 -d ipapp_docker`

## Test the application in a browser.
- Enter `https://localhost:4000/hello`- The output should be Hello World
- Enter `https://localhost:4000/country` - The output should be the country of the requestor IP

## Suggested GitHUb action to push to ECR in AWS
````
name: Deploy to AWS ECR

on:
  push:
    branches:
      - main

env:
  AWS_REGION: eu-north-1

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Build Docker image
      run: |
        docker build -t ipapp_docker .

    - name: Login to Amazon ECR
      uses: aws-actions/amazon-ecr-login@v1
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}

    - name: Push Docker image to Amazon ECR
      uses: docker/push-action@v1
      with:
        context: .
        tags: ${{ env.AWS_REGION }}.dkr.ecr.amazonaws.com/ipapp_docker:${{ env.GITHUB_SHA }}
````
- I could not get this working on the mac
````
 - name: Build Docker image
      uses: docker/build-push-action@v2
      with:
        context: .
        push: true
        tags: "address of your local Docker registry"/ipapp_docker
````


