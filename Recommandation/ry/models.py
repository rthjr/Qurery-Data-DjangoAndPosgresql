from django.db import models

# Create your models here.
# mongo_utils.py
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# def connect_to_mongodb():
#     uri = "mongodb+srv://rthjr:<123rthjr123>@rthjr.cbxiety.mongodb.net/?retryWrites=true&w=majority&appName=rthjr"

#     # Create a new client and connect to the server
#     client = MongoClient(uri, server_api=ServerApi('1'))

#     # Send a ping to confirm a successful connection
#     try:
#         client.admin.command('ping')
#         print("Pinged your deployment. You successfully connected to MongoDB!")
#         return client
#     except Exception as e:
#         print(e)
#         return None
