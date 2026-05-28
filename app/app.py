import boto3
from flask import Flask

app = Flask(__name__)

dynamodb = boto3.resource(
    'dynamodb',
    region_name='ap-south-1'
)

table = dynamodb.Table('Users')

@app.route("/")
def home():
    return "Web App Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)