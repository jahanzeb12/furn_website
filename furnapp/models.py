from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class customer(models.Model):

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email_id = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.name)


class order(models.Model):

    customer_id = models.ForeignKey(customer, on_delete=models.CASCADE, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=100, null=True)
    #Status= (('accepted','accepted'),('not accepted','not accepted'),('delivered','delivered'),('on process','on process'))
    #status=models.CharField(max_length=20,null= True,choices=Status,blank=True)
    # delivery_address=models.CharField(max_length=100,null=True,blank=True)
    # total_bill=models.IntegerField(null=True,blank=True)
    # order_num=models.AutoField(default=0)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.ordered_item_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_item_total(self):
        orderitems = self.ordered_item_set.all()
        total = sum([item.quantity for item in orderitems])
        if(total > 0):
            return total
        else:
            return 0

    @property
    def get_total_with_del(self):

        total = self.get_cart_total
        total += 50
        return total


class shipping(models.Model):

    customer = models.ForeignKey(
        customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(order, on_delete=models.SET_NULL, null=True)
    contact_no = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    zipcode = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.customer)


class category(models.Model):
    category_name = (('sofa', 'sofa'), ('bed', 'bed'), ('chair', 'chair'), ('tables', 'tables'), ('wardrobe', 'wardrobe'),
                     ('lightning', 'lightning'))
    category = models.CharField(
        max_length=20, null=True, choices=category_name)

    def __str__(self):
        return self.category


class product(models.Model):
    product_id = models.CharField(max_length=200, null=True, unique=True)
    title = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    quantity = models.IntegerField(null=True)
    category = models.ForeignKey(
        category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ordered_item(models.Model):
    order_number = models.ForeignKey(order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order_number)

    @property
    def get_total(self):
        total = self.product_id.price*self.quantity
        return total
class review(models.Model):
    Product = models.ForeignKey(product, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, null=True)
    name=models.CharField(max_length=200, null=True)
    email=models.EmailField(max_length=200,null=True)
    date_enter=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class cart(models.Model):
    product_id = models.ManyToManyField(product)
    customer_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0, blank=True)
    quantity = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return str(self.customer_id)
class contact(models.Model):
    message = models.CharField(max_length=200, null=True)
    name=models.CharField(max_length=200, null=True)
    email=models.EmailField(max_length=200,null=True)
    subject=models.CharField(max_length=200,null=True)
    date_enter=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name