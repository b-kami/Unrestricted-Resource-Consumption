import requests
import threading

# Set the number of threads (connections) to create
num_threads = 1000

# Set the server URL to connect to
server_url = "http://192.168.110.131/test_file.txt"


# Define the function that will be run in each thread
def create_session():
    num_sessions = 0  # Define the variable here
    session = requests.Session()  # Create a session object to persist cookies
    while num_sessions < num_threads:  # Check if desired number of sessions are created
        try:
            # Send a request to create a new session
            response = session.get(server_url)

            # Check if the request was successful
            if response.status_code == 200:
                # Print a success message
                print(f"Created session {response.cookies.get_dict()['session_id']}")
            else:
                # Print an error message
                print(f"Error creating session: {response.status_code}")

            num_sessions += 1  # Increment the counter

        # Catch any exceptions and print an error message
        except Exception as e:
            print(f"Error creating session: {e}")

    session.close()  # Close the session to release resources

# Create the threads and start them
for i in range(num_threads):
    thread = threading.Thread(target=create_session)
    thread.start()