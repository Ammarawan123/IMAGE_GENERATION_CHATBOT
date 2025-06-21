import requests

# Replace with your actual API key
API_KEY = "sk-yeCWQamWQ3iNgdVzIciE9AlgwsXDDx4aA1aDsquQ5nF892SL"

# Define API URL
url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"

# Define request headers
headers = {
    "authorization": f"Bearer {API_KEY}",
    "accept": "image/*"
}

# Define request data
payload = {
    "prompt": "a men is flying in sky with a lighthouse in the background",
    "output_format": "jpeg"
}

# Send request to the API using multipart/form-data
response = requests.post(url, headers=headers, files={"none": (None, "")}, data=payload)

# Handle response
if response.status_code == 200:
    image_path = "./lighthouse.jpeg"
    save_option = input("Do you want to save the image? (yes/no): ").strip().lower()
    if save_option == "yes":
        with open(image_path, "wb") as file:
            file.write(response.content)
        print(f"Image saved successfully at {image_path}")
    else:
        print("Image not saved.")
else:
    try:
        error_message = response.json()
    except requests.exceptions.JSONDecodeError:
        error_message = response.text
    raise Exception(f"Error {response.status_code}: {error_message}")