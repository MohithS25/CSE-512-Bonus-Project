from flask import Flask, request, jsonify, render_template
from elasticsearch import Elasticsearch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Connect to Elasticsearch
es = Elasticsearch(
        'https://localhost:9200',
        basic_auth=('elastic', 'DVkCvO-E*HBr5T6CRleN'),
        verify_certs=False
    )

@app.route("/")
def home():
    """
    Renders the main HTML page for the application.
    """
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search_travel_plans():
    origin = request.args.get("origin", "").strip()
    destination = request.args.get("destination", "").strip()
    days = request.args.get("days", None, type=int)

    # Default to 3 days if no number of days is provided
    default_days = 2
    days = days if days else default_days

    # Build the Elasticsearch query
    body = {
        "query": {
            "bool": {
                "must": [],
                "filter": []
            }
        }
    }

    # Add filters for origin, destination, and number of days
    if origin:
        body["query"]["bool"]["filter"].append({"match": {"origin": origin}})
    if destination:
        body["query"]["bool"]["filter"].append({"match": {"destination": destination}})

    # Query Elasticsearch
    try:
        res = es.search(index="travel_plans", body=body)
        results = []

        for hit in res["hits"]["hits"]:
            record = hit["_source"]

            # Exclude itineraries that don't meet the days requirement
            full_itinerary = record.get("annotated_plan", [])
            if len(full_itinerary) < days:
                continue  # Skip records with fewer days than requested

            # Calculate the adjusted budget
            calculated_budget = (record["budget"] / record["days"]) * days

            # Limit itinerary to the specified number of days
            itinerary = full_itinerary[:days]

            # Format the itinerary
            formatted_itinerary = [
                {
                    "day": i + 1,
                    "details": day
                }
                for i, day in enumerate(itinerary)
            ]

            results.append({
                "origin": record["origin"],
                "destination": record["destination"],
                "days": days,
                "calculated_budget": round(calculated_budget, 2),
                "itinerary": formatted_itinerary
            })

        return jsonify(results)
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500





if __name__ == "__main__":
    app.run(port=8000, debug=True)
