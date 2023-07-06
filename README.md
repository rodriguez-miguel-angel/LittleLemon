# LittleLemon

## Introduction
In this project, I built an API for the Little Lemon restaurant using the Django REST Framework. This Capstone project enables me to demonstrate multiple skills from the Certificate by solving an authentic real-world problems. I used Django to serve static HTML content. I set up the MySQL connection, and created the required models for the web application. Then, I built the menu and table booking APIs using the Django Rest Framework. Finally, I not only set up user registration and authentication but test the application with unit tests and Postman as well.


## Getting Started
* Run 'git clone https://github.com/rodriguez-miguel-angel/LittleLemon.git'   

## Development server
* Run 'pipenv shell'
* Run 'pipenv install'
* Run 'cd littlelemon'
* Run `python manage.py runserver` for a dev server. Navigate to 'http://127.0.0.1:8000/`.

## Usage
### User's Credentials
* Usename: arod
* Email: arod@abc.net
* Password: insecure-password
* Token: 255449495c0561bb30405eef44317c83c15103c0
* Authorization: Token 255449495c0561bb30405eef44317c83c15103c0

<h2>Backend Routes: Menu API</h2>
<ul>
  <li><strong>Backend:</strong> [CRUD] HTTP methods supported</li>
  <ul>
    <li>GET [Secured Endpoint]: /restaurant/menu </li>
    <li>POST [Secured Endpoint]: /restaurant/menu </li>
    <li>GET: /restaurant/menu/n </li>
    <li>PUT: /restaurant/menu/n </li>
    <li>DELETE: /restaurant/menu/n </li>
  </ul>
</ul>

<h2>Backend Routes: Booking API</h2>
<ul>
  <li><strong>Backend:</strong> [CRUD] HTTP methods supported</li>
  <ul>
    <li>GET [Secured Endpoint]: /restaurant/booking/tables/ </li>
  </ul>
</ul>

<h2>Backend Routes: djoser.</h2>
<ul>
  <li><strong>Backend:</strong> Used the djoser library to implement registration, login, and logout features</li>
  <ul>
    <li>POST: /restaurant/api-token-auth/ </li>
  </ul>
</ul>

## Technologies Used
### Backend
* Django Web Framework
* Django 
* MySQL
* Python
* Djoser

### Frontend
* JavaScript
* HTML
* CSS

### DevOps
* Git
* GitHub

### Testing
* Pytest
* Postman


## Contributors
#### Coursera. Meta. Miguel Angel Rodriguez.
