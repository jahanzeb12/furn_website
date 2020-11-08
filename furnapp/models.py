from django.db import models

# Create your models here.
class customer(models.Model):
    user_name=models.CharField(max_length=100,null=True)
    contact_no=models.CharField(max_length=100,null=True)
    email_id=models.CharField(max_length=100,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    name=models.CharField(max_length=50,null=True)
    #password yhan dalna hai

    def __str__(self):
        return self.name


