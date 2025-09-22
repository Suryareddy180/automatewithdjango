from django.core.management.base import BaseCommand

#proposed command=python manage.py greeting Name
# proposed output= welcome {Name}!!!


class Command(BaseCommand):
    help="Greets the User."
    
    def add_arguments(self, parser):
        parser.add_argument('name' , type=str, help='used to specify user name')
        
    def handle(self, *args, **kwargs):
        name=kwargs['name']
        greeting=f'welcome {name}'
        self.stdout.write(self.style.SUCCESS(greeting))