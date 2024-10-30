# Pressure Extraction App

## Overview

The Pressure Extraction App is a web application designed to extract pressure readings from images using Optical Character Recognition (OCR). Built with React on the frontend and Flask on the backend, this application allows users to upload images and receive extracted pressure values in real-time.

## Features

-   Upload images for pressure extraction.
-   Extract pressure readings using Tesseract OCR.
-   Display error messages when image reading fails or if no file is selected.
-   User-friendly interface for a seamless experience.

## Tech Stack

-   **Frontend**: React
-   **Backend**: Flask
-   **OCR**: Tesseract
-   **Image Processing**: OpenCV
-   **Styling**: Custom CSS for enhanced aesthetics

## Installation

### Prerequisites

1. **Python 3.x**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **Node.js**: Ensure you have Node.js installed for the frontend. Download it from [nodejs.org](https://nodejs.org/).

### Backend Setup

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install required Python packages:

    ```bash
    pip install Flask Flask-CORS opencv-python pytesseract
    ```

4. Install Tesseract OCR:

    - Download and install Tesseract from [Tesseract's GitHub page](https://github.com/tesseract-ocr/tesseract).
    - Ensure that the Tesseract executable is added to your system's PATH.

5. Start the Flask backend:

    ```bash
    python app.py
    ```

### Frontend Setup

1. Navigate to the frontend directory (if separate):

    ```bash
    cd frontend-directory
    ```

2. Install required Node.js packages:

    ```bash
    npm install
    ```

3. Start the React development server:

    ```bash
    npm start
    ```

## Usage

1. Open your web browser and navigate to `http://localhost:3000`.
2. Upload an image containing pressure readings by clicking the "Upload" button.
3. The extracted pressure readings will be displayed below the upload form.
4. If no pressure readings are detected, an error message will indicate that the image could not be read properly.

## API Endpoints

### `/upload`

-   **Method**: `POST`
-   **Description**: Uploads an image file for pressure extraction.
-   **Request Body**: Form-data containing the image file.
-   **Response**:
    -   **Success**: Returns a JSON object with the extracted pressure readings.
    -   **Error**: Returns a JSON object with an error message.

## Troubleshooting

-   Ensure that Tesseract OCR is installed correctly and is accessible in your system's PATH.
-   Verify that the image contains clear pressure readings for optimal results.
-   Check the browser console for any errors related to CORS or network issues.

## Future work

Contributions are welcome! Please submit a pull request for any improvements or bug fixes. Improve image processing further like when image is blurred/rotated.
