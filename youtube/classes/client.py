class APIClient:
    version = "1.0"              # Same for all clients, like static in java
    max_retries = 3              # Same for all clients, like static in java

    def __init__(self, api_key):
        self.api_key = api_key   # Unique to each client



class APIClient2:
    def __init__(self, api_key, base_url):
        self.api_key = api_key      # Each client has its own key
        self.base_url = base_url    # Each client has its own URL
        self.request_count = 0      # Track requests per client


# Creating instances with named arguments
client1 = APIClient2(api_key="key1", base_url="https://api1.com")
client2 = APIClient2(api_key="key2", base_url="https://api2.com")
