import csv
import json
from random import choice

from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from api.models import Category, Tag, Task


def response(data, code=HTTP_200_OK, error=""):
    res = {'error': error, 'response': data}
    return Response(data=res, status=code)


def load_user(path, delete_all=False):
    if delete_all:
        User.objects.all().delete()
        user = User(username='admin',
                    first_name='admin',
                    last_name='admin',
                    email='admin@gmail.com'
                    )
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.set_password('password@123')
        user.save()
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user = User(username=row['username'],
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        email='email'
                        )
            user.set_password(row['password'])
            user.is_active = True
            user.is_staff = True
            user.is_superuser = False
            user.save()


def load_category(path, delete_all=False):
    if delete_all:
        Category.objects.all().delete()
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category = Category(category=row['category'])
            category.save()


def load_tag(path, delete_all=False):
    if delete_all:
        Tag.objects.all().delete()
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tag = Tag(tag=row['tag'])
            tag.save()


"""
Creating Task
"""


class CreateTask(object):

    def load_task(self, path, delete_all=False):
        if delete_all:
            Task.objects.all().delete()
        with open(path) as jsonfile:
            reader = json.loads(jsonfile.read())
            for row in reader:
                title, desc = row.get('title'), row.get('description')
                created_by, assigned_to = None, None
                if title and desc:
                    description = self.get_clean_description(desc)
                    priority = self.get_priority()
                    while not created_by:
                        created_by = self.get_user()
                    while not assigned_to:
                        assigned_to = self.get_user()
                    while created_by.id == assigned_to.id:
                        assigned_to = self.get_user()  # If assign and user are same
                    task = Task(
                        title=title,
                        description=description,
                        priority=priority,
                        created_by=created_by,
                        assigned_to=assigned_to
                    )
                    task.save()
                    # Add tags and categories
                    [task.category.add(cat) for cat in self.get_categories()]
                    [task.tag.add(tag) for tag in self.get_tags()]

    def get_categories(self):
        # Select any random categories
        categories = []
        for _ in range(0, 2):
            categories.append(self.get_object(Category, choice(range(1, 10))))
        return categories

    def get_tags(self):
        tags = []
        for _ in range(0, 5):
            tags.append(self.get_object(Tag, choice(range(1, 50))))
        return tags

    @staticmethod
    def get_object(model, model_id):
        try:
            model_obj = model.objects.get(pk=model_id)
            return model_obj
        except ObjectDoesNotExist:
            return []

    @staticmethod
    def get_clean_description(description):
        clean_desc = BeautifulSoup(''.join(description)).text
        return clean_desc

    def get_user(self):
        user_id = choice(range(1, 100))
        try:
            user = User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return None
        return user

    @staticmethod
    def get_priority():
        return choice(range(1, 5))
