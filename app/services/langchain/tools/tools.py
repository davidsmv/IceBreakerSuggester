from googlesearch import search
import time

def get_profile_url(text: str) -> str:
    """Searches for Linkedin or Twitter Profile Page

    Args:
        text (str): name of the person and
        aditional descriptions if neccesary

    Returns:
        str: URL
    """
    # first_result = next(search(text, num_results=1), None)
    # return first_result

    max_retries = 5
    retry_count = 0
    backoff_time = 1  # Time in seconds to wait before retries

    while retry_count < max_retries:
        try:
            # Attempt to get the first search result
            first_result = next(search(text, num_results=1), None)
            if first_result:
                return first_result
        except Exception as e:
            print(f"Attempt {retry_count + 1} failed with error: {e}")
            time.sleep(backoff_time)  # Wait before retrying
            backoff_time *= 2  # Exponential backoff
            retry_count += 1  # Increment the retry counter