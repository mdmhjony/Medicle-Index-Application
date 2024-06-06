## Medicine Corner
Medicine Corner is a web application for managing medicine information. It allows users to display a list of medicines, search by name and generic name, insert new medicines (available for logged-in users only), and edit/delete existing medicine entries (available for logged-in users only). User authentication is implemented to ensure secure access to the application.

## Features
Display a list of medicines
Search by name and generic name
Insert medicines (available for logged-in users only)
Edit and delete medicine entries (available for logged-in users only)
User authentication
Prerequisites
Before you begin, ensure you have the following prerequisites installed on your system:

Python 3.x
pip (Python package installer)
## Installation
Clone the repository: git clone https://github.com/mdmhjony/Medicle-Index-Application.git
cd Medicle-Index-Application 
Install the dependencies:
pip install -r requirements.txt
## Running the Application Backend Setup: Backend folder name is medicine_index
## Run the backend server (Django):
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Follow the prompts to create a superuser account.

Go to http://127.0.0.1:8000/admin in your web browser and log in with the username and password you created using the createsuperuser command.

##Frontend Setup : forntend folder name is : medinice website frontend
Open the frontend folder and open index.html in any web browser.

Without logging in, you can view and search for medicines.
After logging in with the superuser credentials, you can insert, update, and delete medicines.
You are logged in using the username and password you created during the createsuperuser process.

