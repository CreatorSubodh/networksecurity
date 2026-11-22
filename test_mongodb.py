from pymongo import MongoClient
uri = "mongodb+srv://subodhkumar7951_db_user:L3YlM10GWCt7Yokv@cluster0.3ulei01.mongodb.net/"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)