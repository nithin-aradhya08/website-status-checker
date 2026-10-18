
import requests
import time

print("=" * 40)
print("      WEBSITE STATUS CHECKER")
print("=" * 40)

website = input("Enter website URL: ").strip()

# Add HTTPS if the user does not enter a protocol
if not website.startswith(("http://", "https://")):
    website = "https://" + website

print("\nChecking website...")

try:
    start_time = time.time()

    response = requests.get(
        website,
        timeout=10
    )

    end_time = time.time()
    response_time = end_time - start_time

    print("\nWebsite:", website)
    print("HTTP Status Code:", response.status_code)
    print(f"Response Time: {response_time:.2f} seconds")

    if 200 <= response.status_code < 300:
        print("Result: Website responded successfully!")
    elif 300 <= response.status_code < 400:
        print("Result: Website redirected the request.")
    elif 400 <= response.status_code < 500:
        print("Result: Client error response.")
    else:
        print("Result: Server error response.")

except requests.exceptions.Timeout:
    print("Result: Request timed out.")

except requests.exceptions.ConnectionError:
    print("Result: Could not connect to the website.")

except requests.exceptions.RequestException as error:
    print("Result: Request failed.")
    print("Error:", error)
