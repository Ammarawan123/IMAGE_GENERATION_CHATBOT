# AI Image Generation Chatbot

A simple web app that lets users enter a text prompt and generate an AI image using a Flask backend and a polished frontend.

## Features
- Modern and responsive web interface
- Text prompt input for image generation
- Flask API endpoint for processing requests
- Displays generated image directly in the browser

## Project Structure
- app.py - Flask backend that handles image generation requests
- index.html - Frontend UI for entering prompts and viewing results
- main.py - Additional project script (if used)

## Requirements
Install the required Python packages:

```bash
pip install flask requests
```

## Setup
1. Open the project folder.
2. Make sure your image generation API key is configured in app.py.
3. Run the backend:

```bash
python app.py
```

4. Open your browser and go to:

```text
http://127.0.0.1:5000/
```

## Usage
1. Enter a prompt such as "a futuristic city at sunset".
2. Click Generate.
3. Wait for the image to appear on the page.

## Notes
- This project uses an external AI image generation API, so a valid API key is required.
- If the API response format changes, the backend may need to be adjusted accordingly.

## License
This project is for educational and demonstration purposes.
