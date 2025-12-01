Geometry App - Flask Web Application
Overview

The Geometry App is a Flask-based web application designed to demonstrate dynamic web page rendering using HTML templates. Unlike basic Flask scripts that return simple text responses, this application serves fully structured HTML pages for user interaction. The app currently supports calculating the volumes of cylinders and spheres, and includes unit tests to ensure accuracy of the calculations.

This project also serves as an example of how to containerize a Python web application using Docker to simplify deployment to production environments.

Features

Cylinder Volume Calculation: Users can input cylinder dimensions (radius and height) and get the calculated volume.

Sphere Volume Calculation: Users can input the sphere's radius and get the calculated volume.

HTML Templates: Pages are rendered using Flask templates for a clean and user-friendly interface.

Unit Testing: Automated tests (cylindertest.py and spheretest.py) validate correctness of volume calculations.

Dockerized Deployment: Provides a Dockerfile for building a lightweight container that can run the app consistently across environments.

Repository Structure
inet4031-geometry-app/
├── GeometryCalcWeb.py       # Main Flask application
├── cylinder.py              # Cylinder volume calculation module
├── sphere.py                # Sphere volume calculation module
├── cylindertest.py          # Unit tests for cylinder module
├── spheretest.py            # Unit tests for sphere module
├── templates/               # HTML templates for web pages
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker container definition
├── README.md                # Project documentation

Notes on Structure:

templates/ contains the HTML files that Flask uses to render pages.

.venv/ (virtual environment) is not included in the repo to avoid unnecessary files.

requirements.txt lists all required Python packages for easy installation.

Installation and Setup
1. Clone Your Repository

Clone the repository to your local machine or VM:

git clone https://github.com/escob138/inet4031-geometry-app1.git
cd inet4031-geometry-app1
2. Create a Virtual Environment

Creating a virtual environment ensures dependencies do not conflict with system Python packages:

python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Install Dependencies

Install all required Python packages using pip:

pip install -r requirements.txt
Running the Application Locally

Start the Flask application:

flask --app GeometryCalcWeb.py run

By default, Flask runs on http://127.0.0.1:5000. Open a browser and navigate to that URL to access the app.

Using the App

Navigate to the Home Page.

Select Cylinder or Sphere calculations.

Enter the required dimensions.

View the calculated volume.

Run unit tests to verify correctness:

python cylindertest.py
python spheretest.py
Docker Containerization

To containerize the application:

Make sure you are in the project root directory (where Dockerfile is located).

Build the Docker image:

docker build -t inet4031geometryappflask:latest .

Run the container:

docker run -p 5000:5000 inet4031geometryappflask:latest

Access the application in a browser using the IP address of your VM or localhost if running locally.

Note: 127.0.0.1 won’t work if the container is running in a VM because it refers to the container’s own network namespace. Use the VM’s IP address to access the app externally.

Submission Items for Lab

Screenshot of the home page.

Screenshot of a cylinder calculation result.

Screenshot of a sphere calculation result.

Screenshot showing unit tests passing.

Provide your GitHub repository link.

Development Notes

Ensure all HTML templates are included in the templates/ directory.

Keep the repository clean: do not commit the virtual environment or temporary files.

The Dockerfile uses the python:3.8-slim base image for a lightweight, reproducible environment.

Use modular Python code (cylinder.py, sphere.py) to separate calculation logic from the web interface.

