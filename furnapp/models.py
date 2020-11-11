from django.db import models

# Create your models here.
class customer(models.Model):
    user_name=models.CharField(max_length=100,null=True)
    contact_no=models.CharField(max_length=100,null=True)
    email_id=models.CharField(max_length=100,null=True)
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    street_no=models.IntegerField(null=True)
    city=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    zipcode=models.IntegerField(null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    #password yhan dalna hai
    def __str__(self):
        return self.user_name
class order(models.Model):
    customer_id=models.ForeignKey(customer,on_delete=models.CASCADE)
    Status= (('accepted','not accepted'),('delivered','on process'))
    status=models.CharField(max_length=20,null= True,choices=Status)
    delivery_address=models.CharField(max_length=100,null=True)
    total_bill=models.IntegerField(null=True)
    order_num=models.IntegerField(unique=True)

