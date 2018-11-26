# Installation

- Create virtualenv `virtualevn -p python3 env`
- Activate virtualenv `source env/bin/activate`
- Install dependencies `pip install -r requirements.txt`


# Load DB

- Makemigrations `python manage.py makemigrations`
- Migrate `python manage.py migrate`
- Load mock data `python manage.py load_db`


# API's Instructions

- `api/v1/tasks` List all the tasks
- `api/v1/categories` List all the categories
- `api/v1/tags` List all the tags
- `api/v1/task/<task_id>` CRUD operation on specific task