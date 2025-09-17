# 代码生成时间: 2025-09-17 19:48:53
import json
from scrapy.http import Response

"""
A utility tool to format API responses using Scrapy framework.

This tool will take a Scrapy Response object, validate it and format it
into a JSON object with a standardized structure.
"""

def format_api_response(response: Response) -> dict:
    """
    Formats an API response from a Scrapy Response object into a standardized JSON object.

    Args:
        response (Response): A Scrapy Response object to be formatted.

    Returns:
        dict: A dictionary representing the formatted API response.
    
    Raises:
        ValueError: If the response is not a valid JSON.
    """
    try:
        # Check if the response is a Scrapy Response object
        if not isinstance(response, Response):
            raise TypeError("Invalid response type. Expected a Scrapy Response object.")

        # Try to parse the response body as JSON
        response_json = json.loads(response.body)

        # Create a standardized response structure
        formatted_response = {
            "status": response.status,
            "headers": dict(response.headers),
            "body": response_json,
            "url": response.url,
        }

        return formatted_response
    except json.JSONDecodeError:
        # Handle invalid JSON in the response body
        raise ValueError("Invalid JSON in the response body.")
    except Exception as e:
        # Handle any other exceptions
        raise Exception(f"An error occurred: {e}")

# Example usage:
# Assuming 'response' is a Scrapy Response object obtained from a Scrapy Spider
# formatted_response = format_api_response(response)
# print(formatted_response)