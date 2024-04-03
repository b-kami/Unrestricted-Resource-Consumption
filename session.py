import requests
import threading

# Set the number of threads (connections) to create
num_threads = 1000

# Set the server URL to connect to


server_url = "http://192.168.110.131/virus.iso"


# Define the function that will be run in each thread
def create_session():
    while True:
        try:
            # Send a request to create a new session
            response = requests.get(server_url)

            # Check if the request was successful
            if response.status_code == 200:
                # Print a success message
                print(f"Created session {response.cookies.get_dict()['session_id']}")
            else:
                # Print an error message
                print(f"Error creating session: {response.status_code}")

        # Catch any exceptions and print an error message
        except Exception as e:
            print(f"Error creating session: {e}")

# Create the threads and start them
for i in range(num_threads):
    thread = threading.Thread(target=create_session)
    thread.start()