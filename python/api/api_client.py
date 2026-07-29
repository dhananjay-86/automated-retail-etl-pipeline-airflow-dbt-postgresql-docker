import requests


class APIClient:
    """
    Handles communication with the DummyJSON API.
    """

    BASE_URL = "https://dummyjson.com"

    def get_data(self, endpoint: str):
        """
        Fetch data from the given API endpoint.

        Args:
            endpoint (str): API endpoint (e.g. '/users')

        Returns:
            dict: JSON response from the API
        """

        url = f"{self.BASE_URL}{endpoint}"

        response = requests.get(url, timeout=30)

        response.raise_for_status()

        return response.json()