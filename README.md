# Spam Detector Project

This project consists of a browser extension for spam detection and a FastAPI server that uses machine learning models to classify messages as spam or ham.

## Table of Contents
1. [Project Setup](#project-setup)
2. [Extension Setup](#extension-setup)
3. [Retraining the Model](#retraining-the-model)
4. [Running the FastAPI Server](#running-the-fastapi-server)
5. [Docker Deployment](#docker-deployment)

## Project Setup

This project uses Astral UV for dependency management and virtual environment creation. Follow these steps to set up the project:

1. Install Astral UV if you haven't already:
   ```bash
   curl -fsSL https://astral.sh/uv/install.sh | bash
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/your-username/spam_detector.git
   cd spam_detector
   ```

3. Create a virtual environment and install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate
   uv sync
   ```

## Extension Setup

To set up the browser extension:

1. Open your browser (Chrome, Firefox, etc.) and navigate to the extensions page.

2. Enable "Developer mode".

3. Click on "Load unpacked" or "Load temporary add-on".

4. Navigate to the `extension` directory in this project and select it.

The extension should now be loaded and visible in your browser.

## Retraining the Model

To retrain the Random Forest model:

1. Ensure you're in the project root directory and your virtual environment is activated.
2. Ensure you have the training data `[Dataset](https://www.kaggle.com/datasets/meruvulikith/190k-spam-ham-email-dataset-for-classification)` 
(properly named `spam_Emails_data.csv`) and you have put it in the right directory `server/models/data`
3. Run the training script:
   ```bash
   python trainer.py
   ```

This will retrain the models using the latest data and save the new model and vectorizer in the `server/models/data` directory.

## Running the FastAPI Server

To run the FastAPI server:

1. Ensure you're in the project root directory and your virtual environment is activated.

2. Start the server:
   ```bash
   fastapi dev main.py 
   ```

The server will start running on `http://127.0.0.1:8000`. You can access the API documentation at `http://127.0.0.1:8000/docs`.

## Docker Deployment

To deploy the project using Docker:

1. Build the Docker image:
   ```bash
   docker build -t spam-detector .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 spam-detector
   ```

The server will be accessible at `http://localhost:8000`.

## Additional Information

- The main server logic is in `server/routes.py`.
- The machine learning models are located in the `server/models` directory.
- The browser extension files are in the `extension` directory.

For more detailed information about each component, please refer to the comments in the respective files.
