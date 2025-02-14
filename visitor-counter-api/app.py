from flask import Flask, jsonify
from azure.cosmos import CosmosClient

app = Flask(__name__)

# CosmosDB Connection
COSMOS_URL = "https://cosmosdbresume.documents.azure.com:443/"
COSMOS_KEY = "YlN6iemHqm61U9ARYINk1u8cgMlQbry7mqP7ooNGQiEbQGWbWlEMeICP8KA2XKpTVW35AcZrxov6ACDbcLvOiQ=="
DATABASE_NAME = "VisitorDB"
CONTAINER_NAME = "Visitors"

client = CosmosClient(COSMOS_URL, COSMOS_KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

@app.route('/visitorCount', methods=['GET'])
def visitor_count():
    item = container.read_item(item="1", partition_key="1")
    item['visits'] += 1
    container.replace_item(item=item, body=item)
    return jsonify({"visits": item['visits']})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
