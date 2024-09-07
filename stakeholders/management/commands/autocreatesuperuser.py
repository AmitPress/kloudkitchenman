from django.core.management.base import BaseCommand
from stakeholders.models import User

class Command(BaseCommand):
    help = "Create SuperUser for Bootstrapping The Application"
    def add_arguments(self, parser):
        parser.add_argument("--username", type=str, help="Super User's Name")
        parser.add_argument("--email", type=str, help="Super User's Email")
        parser.add_argument("--password", type=str, help="Super User's Password")
    def handle(self, *args, **kwargs):
        username = kwargs.get("username")
        email    = kwargs.get("email")
        password = kwargs.get("password")

        if not (username and email and password):
            self.stdout.write(self.style.ERROR("Username or Email or Password Is Not Set"))
            return
        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.ERROR("Superuser With This Email Already Exists"))
            return
        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f'Superuser with name: "{username}" created successfully'))