import csv
from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from dataentry.models import Student

#Proposed command -python manage.py importdata file_path model_path
class Command(BaseCommand):
    help="Import data from the CSV FILE "

    def add_arguments(self, parser):
        parser.add_argument('file_path',type=str, help='CSV file path')
        parser.add_argument('model_name',type=str,help="Name of the model")
        
    def handle(self,*args, **kwargs):
        #logic will goes here
        
        file_path=kwargs['file_path'] 
        model_name=kwargs['model_name']
        
        #Search for the model across all installed apps
        model=None
        for appconfig in apps.get_app_configs():
             #Try to search for the model
             try:
                model=apps.get_model(appconfig.label,model_name)
                break #stop searching once the model is found 
             except LookupError:
                continue # model not found this app, cotinue searching in next app.
        if not model:
            raise CommandError(f"Model {model_name} not found in any app!")
            
                
                
        with open(file_path,'r') as file:
            reader=csv.DictReader(file) # coverts all records in the csv file  in the form of list of dictionaries.And consider first row as column header.
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS( "Data imported from csv successfully✅"))