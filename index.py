import pandas as pd
from elasticsearch import Elasticsearch
import urllib3

# Used to Suppress SSL warnings 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Connect to Elasticsearch
es = Elasticsearch(
        'https://localhost:9200',
        basic_auth=('elastic', 'DVkCvO-E*HBr5T6CRleN'),
        verify_certs=False
    )

# Delete the index if it already exists
if es.indices.exists(index="travel_plans"):
    es.indices.delete(index="travel_plans")

# Create the index with mappings
es.indices.create(
    index="travel_plans",
    body={
        "mappings": {
            "properties": {
                "origin": {"type": "keyword"},
                "destination": {"type": "keyword"},
                "days": {"type": "integer"},
                "budget": {"type": "float"},
                "annotated_plan": {"type": "nested"}  # To store the detailed itinerary
            }
        }
    }
)

# Read the CSV file
df = pd.read_csv(r"D:\ASU\DDS\DDS Bonus\travel_data_random_places.csv")


# Convert the annotated_plan string to a dictionary
import ast
df['annotated_plan'] = df['annotated_plan'].apply(ast.literal_eval)

# Index each row into Elasticsearch
for _, row in df.iterrows():
    document = {
        "origin": row["origin"],
        "destination": row["destination"],
        "days": row["days"],
        "budget": row["budget"],
        "annotated_plan": row["annotated_plan"]
    }
    es.index(index="travel_plans", document=document)

print("Dataset indexed successfully!")
