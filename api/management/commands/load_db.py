from django.core.management import BaseCommand

from api import constants
from api import utils


class Command(BaseCommand):
    help = 'Load Sample data in DB'

    def handle(self, *args, **options):
        print('Loading User Data')
        utils.load_user(constants.USER_FILE_PATH, delete_all=True)
        print('User Data Loaded successfully')
        print('Loading Categories Data')
        utils.load_category(constants.CATEGORY_FILE_PATH, delete_all=True)
        print('Categories Data Loaded successfully')
        print('Loading Tags Data')
        utils.load_tag(constants.TAG_FILE_PATH, delete_all=True)
        print('Tag Data Loaded successfully')
        print('Loading Task Data')
        utils.CreateTask().load_task(constants.TASK_FILE_PATH, delete_all=True)
        print('Task Data loading completed')
