# Whispr

Whispr is an open sourced project that aims to give as much privacy possible in communication, utilizing hashing text messages, and dissolving the database associated with the chat after the chat has been deleted. Listed below is a technical installation and deployment of this project and how to contribute if interested!

## Features

- No logs of any conversations held on website.    
- Fully open-sourced, look around.
- Free of use
- Deployable Yourself
- Up to date cryptography and hashing methods to hold as much privacy and security possible.

## Technologies
**Backend**

- Python
- Flask (web framework)
- Flask-SQLAlchemy (ORM)
- Flask-Login (user session management)
- Flask-Bcrypt (password hashing)
- Flask-WTF (form handling and CSRF protection)
- WTForms (form validation)
- SQLAlchemy
- Bcrypt
- email-validator
- Werkzeug
- Jinja2 (templating engine).   

**Frontend**

- HTML (Jinja2 templates)
- Bootstrap 5.3.8 (CSS Framework)
- CSS
- JavaScript. 

**Database**

- SQLite.  

# Project Structure
## Project Structure

```
Whispr/
├── run.py                      
├── requirements.txt           
├── README.md
└── whispr/
    ├── backend/                
    │   ├── __init__.py         
    │   ├── forms.py           
    │   ├── models.py           
    │   └── routes.py           
    └── frontend/
        ├── static/
        │   ├── css/
        │   │   ├── main/
        │   │   │   └── styles.css
        │   │   └── typography/
        │   │       └── colors.css
        │   ├── images/
        │   │   └── logo.svg
        │   └── js/
        │       ├── backend/
        │       └── frontend/
        │           ├── chat-settings.js
        │           ├── navbar-scroll.js
        │           ├── show-password.js
        │           └── toasts.js
        └── templates/
            ├── layout.jinja    
            ├── home.jinja
            ├── chat.jinja
            ├── account.jinja
            └── auth/
                ├── login.jinja
                └── register.jinja
```
#

## Installation

**Clone The Repository**

HTTPS Clone:
```
$ git clone https://github.com/andrefetch/Whispr.git
```
SSH Clone:
```
$ git@github.com:andrefetch/Whispr.git
```

Github CLI:
```
$ gh repo clone andrefetch/Whispr
```

#

**Set up a virtual environment** inside of the root folder of the project.

Mac & Linux (should be for all distributions)
```
$ python3 -m venv path/to/venv
$ source path/to/venv/bin/activate 
```

Windows
```
python -m venv venv
venv\Scripts\activate
```
