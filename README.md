# Medicine Corner

Medicine Corner is a web application for efficiently managing medicine information. It offers various features to assist users in organizing and accessing medicine data securely.

## Features

- Display a list of medicines
- Search by name and generic name
- Insert medicines (available for logged-in users only)
- Edit and delete medicine entries (available for logged-in users only)
- User authentication

## Prerequisites

Before starting, ensure you have the following prerequisites installed on your system:

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mdmhjony/Medicle-Index-Application.git
    ```

2. Navigate to the cloned directory:

    ```bash
    cd Medicle-Index-Application
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

### Backend Setup

- Backend folder name: `medicine_index`

1. Run the backend server (Django):

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    ```

    Follow the prompts to create a superuser account.

2. Go to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) in your web browser and log in with the username and password you created using the `createsuperuser` command.

### Frontend Setup

- Frontend folder name: `medinice_website_frontend`

1. Open the frontend folder and open `index.html` in any web browser.

## Usage

- Without logging in, you can view and search for medicines.
- After logging in with the superuser credentials, you can insert, update, and delete medicines.

You are logged in using the username and password you created during the `createsuperuser` process. Enjoy managing your medicine information efficiently with Medicine Corner!
