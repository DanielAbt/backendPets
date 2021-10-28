from django.core.management import BaseCommand, call_command
# if you use a common User Model
#from django.contrib.auth.models import User 

# if you have a custom user Model
from pets.models import CustomUser 

class Command(BaseCommand):
    help = "DEV COMMAND: Fill databasse with a set of data for testing purposes"

    def handle(self, *args, **options):
        call_command('loaddata','initdata')
        # Fix the passwords of fixtures
        for user in CustomUser.objects.all():
            user.set_password(user.password)
            user.save()