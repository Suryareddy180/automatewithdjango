import csv
from django.core.management.base import BaseCommand
from dataentry.models import Student

#Proposed command -python manage.py importdata file_path
class Command(BaseCommand):
    help="Import data from the CSV FILE "

    def add_arguments(self, parser):
        parser.add_argument('file_path',type=str, help='CSV file path')
        
        
    def handle(self,*args, **kwargs):
        #logic will goes here
        
        file_path=kwargs['file_path'] 
        with open(file_path,'r') as file:
            reader=csv.DictReader(file) # coverts all records in the csv file  in the form of list of dictionaries.And consider first row as column header.
            for row in reader:
                Student.objects.create(**row)
        self.stdout.write(self.style.SUCCESS( "Data imported from csv successfully✅"))