from flask import Flask, render_template, request
from azure.mgmt.resource import ResourceManagementClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.

# Acquire a credential object
token_credential = DefaultAzureCredential()


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/resource_group_checker", methods=['POST'])
def resource_group_checker():
    subscription_id = request.form['sub_id']
    subscription_id = subscription_id.strip()

    resource_client = ResourceManagementClient(token_credential, subscription_id)

    group_list = resource_client.resource_groups.list()

    return render_template('index.html', resource_groups=group_list)
