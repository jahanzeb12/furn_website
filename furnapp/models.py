from django.db import models

# Create your models here.
class customer(models.Model):
    user_name=models.CharField(max_length=100,null=True)
    # contact_no=models.CharField(max_length=100,null=True)
    email_id=models.CharField(max_length=100,null=True)
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    street_no=models.IntegerField(null=True)
    city=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    zipcode=models.IntegerField(null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    my_name=models.CharField(max_length=100,null=True)
    #password yhan dalna hai
    def __str__(self):
        return self.user_name
class order(models.Model):
    customer_id=models.ForeignKey(customer,on_delete=models.CASCADE)
    Status= (('accepted','accepted'),('not accepted','not accepted'),('delivered','delivered'),('on process','on process'))
    status=models.CharField(max_length=20,null= True,choices=Status)
    delivery_address=models.CharField(max_length=100,null=True)
    total_bill=models.IntegerField(null=True)
    order_num=models.IntegerField(unique=True)
    def __str__(self):
        return self.customer_id

class ordered_item(models.Model):
    order_number=models.ForeignKey(order,on_delete=models.CASCADE)
    #product_id=
    quantity=models.IntegerField()
    def __str__(self):
        return self.order_number
class review(models.Model):
    comment=models.CharField(max_length=200,null=True)
    #rating=
    customer_id=models.ForeignKey(customer,on_delete=models.CASCADE)
    def __str__(self):
        return self.customer_id

class product(models.Model):
    product_id=models.CharField(max_length=200,null=True,unique=True)
    title=models.CharField(max_length=50,null=True)
    price=models.IntegerField()
    description=models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='static/img/gallery',blank=True)
    def __str__(self):
        return self.title

    

class category(models.Model):
    product_id=models.ForeignKey(product,on_delete=models.CASCADE)
    category_name=(('sofa','sofa'),('beds','single beds'),('beds','double beds'),('side tables','side tables'),('wardrobe','single wardrobe'),
    ('wardrobe','double wardrobe'),(''))
    def __str__(self):
        return self.product_id

class cart(models.Model):
    product_id=models.ManyToManyField(product)
    customer_id=models.ForeignKey(customer,on_delete=models.CASCADE)
    total_price=models.IntegerField()
    quantity=models.IntegerField()
    def __str__(self):
        return self.customer_id



