# **Itinerary Planner**

## **Overview**
The Itinerary Planner is a web application designed to help users plan their trips by exploring and filtering travel itineraries stored in Elasticsearch. Users can search for trips based on origin, destination, and the number of days and view itineraries with budgets. The application provides a user-friendly interface and dynamic interactivity.
The dataset includes travel plans and itineraries for various destinations across the USA, featuring  trip plans, budgets, and attractions.

---

## **Features**

### Search Trips
- Filter trips by:
  - **Origin City**
  - **Destination City**
  - **Number of Days**
- View trip details, including:
  - **Origin** and **Destination**
  - **Number of Days**
  - **Budget**
  - **Daily Itinerary**
- Dynamically adjust budgets and itineraries based on the number of days.

---

## **Requirements**

### **Core Technologies**
- **Elasticsearch**
- **Flask**: Backend framework
- **Frontend**: HTML, CSS (Bootstrap), and JavaScript

### **Ports Used**
- Elasticsearch runs on `http://localhost:9200`.
- Flask backend runs on `http://127.0.0.1:8000`.

### **Libraries**
- **Flask**: Handles backend and API routing.
- **pandas**: Processes travel data.
- **requests**: Fetches data and handles HTTP requests.
- **Bootstrap**: Frontend design for responsive UI.

---

## **Step-by-Step Instructions**

1. **Start Elasticsearch:**
   - Navigate to the `bin` directory in Elasticsearch directory and run:
     ```bash
     ./elasticsearch
     ```

2. Load Data into Elasticsearch
   **Open the `index.py` file:**
   - Ensure the Elasticsearch host and port (`localhost:9200`) are correct.
   **This script will:**
   - Define the index mapping for the `travel_plans` index.
   - Load travel data into Elasticsearch.
   **Run the script:**
   ```bash
   python index.py
   ```

3. Run the Backend Server**
   **Open the `app.py` file and Run the backend:**
   ```bash
   python app.py
   ```

4. Run Frontend:
   Navigate to **http://127.0.0.1:8000** on your browser to deploy the frontend
