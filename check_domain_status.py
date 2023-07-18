import requests


def check_domain_status(domain_url):
    """Check the status of a domain.

    Args:
        domain_url (str): The domain URL to check.

    Returns:
        tuple: A tuple containing the domain URL and its status.
    """
    full_url = "https://" + domain_url

    try:
        response = requests.get(full_url)
        if response.status_code != 200:
            return (domain_url, f"Down with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        return (domain_url, f"Down with an error: {e}")

    return (domain_url, "Up and running")
