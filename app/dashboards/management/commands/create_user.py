from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Create superuser by cmd'

    def add_arguments(self, parser):
        parser.add_argument('-u', '--user', type=str, nargs='?', const="demo", help='username', )
        parser.add_argument('-p', '--password', type=str, nargs='?', const="demo123", help='password', )
        parser.add_argument('-e', '--email', type=str, nargs='?', const="demo@demo.com", help='email', )

    def handle(self, *args, **kwargs):
        user = kwargs['user']
        password = kwargs['password']
        email = kwargs['email']
        User.objects.create_superuser(user, email, password)
