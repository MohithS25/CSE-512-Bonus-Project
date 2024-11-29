# ITINERARY PLANNER
##Overview

The Itinerary Planner is a powerful web application designed to help users plan their trips seamlessly by exploring and filtering travel itineraries stored in Elasticsearch. Users can search for trips based on origin, destination, and the number of days and view detailed itineraries with budgets. The application provides a user-friendly interface and dynamic interactivity.

The dataset includes travel plans and itineraries for various destinations across the USA, featuring detailed trip plans, budgets, and attractions.
---
Features
Search Trips
Filter trips by:
Origin City
Destination City
Number of Days
View trip details, including:
Origin and Destination
Number of Days
Budget
Daily Itinerary
Dynamically adjust budgets and itineraries based on the number of days.
Dynamic Itineraries
Show detailed daily itineraries, including places to visit, transportation, meals, and accommodations.
Display the adjusted budget based on the input number of days.
Allow users to expand/collapse day-wise itinerary details interactively.
Requirements
Core Technologies
Elasticsearch: Version 8.x
Flask: Backend framework
Frontend: HTML, CSS (Bootstrap), and JavaScript
Ports Used
Elasticsearch runs on http://localhost:9200.
Flask backend runs on http://127.0.0.1:5000.
Libraries
Flask: Handles backend and API routing.
pandas: Processes travel data.
requests: Fetches data and handles HTTP requests.
Bootstrap: Frontend design for responsive UI.
Step-by-Step Instructions
1. Install and Start Elasticsearch
Download Elasticsearch:
Visit the Elasticsearch Official Website.
Start Elasticsearch:
Unzip the downloaded Elasticsearch package.
Navigate to the bin directory and run:
./elasticsearch
2. Load Data into Elasticsearch
Open the load_to_es.py file:
Ensure the Elasticsearch host and port (localhost:9200) are correct.
This script will:
Define the index mapping for the travel_plans index.
Load travel data into Elasticsearch.
Run the script:
python load_to_es.py
3. Run the Backend Server
Open the app.py file:
Ensure the Elasticsearch host and port are correct (http://localhost:9200).
Run the backend:
python app.py
Verify that the backend is running by accessing http://127.0.0.1:5000.
4. Open the Frontend
Open index.html in a browser:
The frontend is built using HTML, CSS, and JavaScript, with Bootstrap for styling.
The frontend interacts with the Flask backend for API calls.
Usage Instructions
Search Trips
Navigate to the search form.
Input:
Origin City: The starting point of the trip.
Destination City: The target location.
Number of Days: Duration of the trip.
Click Search.
View:
Filtered results based on your input.
Trip details: origin, destination, budget, and itinerary.
Expand/collapse day-wise itinerary details.
Dynamic Features
Adjust the number of days, and the application recalculates the budget and itinerary automatically.
View detailed itineraries, including transportation, attractions, meals, and accommodations.
Key Files
load_to_es.py:
Loads travel data into Elasticsearch.
Defines the index mapping for the travel_plans index.
app.py:
Flask backend that handles search queries and interacts with Elasticsearch.
index.html:
The frontend file for user interaction and display of results.
travel_data_extended.csv:
Dataset containing detailed travel plans.
Technologies Used
Elasticsearch: For data storage, querying, and filtering.
Flask: Backend development and API endpoints.
Bootstrap: Frontend design for a responsive and modern UI.
pandas: Data processing for loading and manipulating travel plans.

