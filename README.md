# DjangoBookApp
This is a simple BookApp created with Django
# Requirements
To run this app, you will need to have the following installed on your system:
* Python 3.x
* Django 3.x
* PostgreSQL for the database
# Installation
To install the app on your local system, follow these steps:
1. Clone the repository to your local machine:
  <br> git clone https://github.com/DanielH987/DjangoBookApp.git
2. Navigate to the project directory:
  <br> cd DjangoBookApp
3. Create and activate a virtual environment:
  <br> python -m venv env
  <br> source env/bin/activate
4. Install the required packages:
  <br> pip install -r requirements.txt
5. Migrate the database:
  <br> python manage.py migrate
6. Create a superuser:
  <br> python manage.py createsuperuser
7. Run the development server:
  <br> python manage.py runserver
You can now access the app by visiting http://localhost:8000 in your web browser.
# Features
The app offers the following features:
* View book details, including title, author, description, publoshing date, price (not real price)
* Add books to database
* Edit and delete books from the book list
