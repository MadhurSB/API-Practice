import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "madhur1910"
TOKEN = "MADHURSB1902"
GRAPH_ID = "graph1"
QUANTITY = (input("How many hours did you study"))
# Step 1: Create a User (only if the user doesn't already exist)
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Uncomment and run this only if the user hasn't been created yet
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Step 2: Create a Graph (run only if the graph is not created yet)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Study Graph",
    "unit": "Hrs",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Uncomment this to create the graph (run this once)
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Step 3: Post Pixel Data (Adding a pixel entry for the current date)
# Generate today's date in YYYYMMDD format
today = datetime.datetime.now().strftime("%Y%m%d")

pixel_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today,  # Use dynamically generated date
    "quantity": QUANTITY,  # Number of study hours (float as string)
}

# Post the pixel data to the graph
response = requests.post(url=pixel_graph_endpoint, json=pixel_data, headers=headers)
print(response.text)
