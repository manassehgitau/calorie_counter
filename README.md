# Calorie Counter

This is a simple Django web app to track daily calorie intake.

## Features

- Add food items and calorie counts
- View total calories consumed today
- Delete individual food items
- Reset calorie count for the day

## Tech Stack

- Django 3.x
- PostgreSQL
- Tailwind CSS

## Setup

1. Clone the repo  
2. Create a virtual environment and activate it  
3. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
4. Update `settings.py` with your PostgreSQL DB credentials.
5. Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Run the server:
    ```bash
    python manage.py runserver
    ```


## License

MIT
