# Install python image
FROM python:3.10-alpine
# Copy requiremment.txt 
COPY ./requirements.txt /app/requirements.txt
# Move to working directory
WORKDIR /app
# Install packages from requirements.txt
RUN pip install -r requirements.txt
# Copy all content to working directory of app
COPY . /app
# Run the application in the container
ENTRYPOINT [ "python"]

CMD ["app.py"]