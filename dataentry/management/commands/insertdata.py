# i want to add some data to the database using custom command.

from django.core.management.base import BaseCommand
from dataentry.models import Student
class Command(BaseCommand):
    help="It will insert data to the database"
    
    def handle(self,*args, **kwargs):
        #logic goes here
        #add 1 data
        #Student.objects.create(roll_no="22a81a61a3",name="surya",age=20)
        
        #mulitple records
        dataset=[
            {'roll_no':"22a81a6136",'name':'usha','age':20},
            {'roll_no':"22a81a6123",'name':'abhi','age':21},
             {'roll_no':"22a81a6196",'name':'vamsi','age':22},
             
        ]
        
        for data in dataset:
            Student.objects.create(roll_no=data['roll_no'],name=data['name'],age=data['age'])
            
        self.stdout.write(self.style.SUCCESS('Data inserted sucessfully!'))
    