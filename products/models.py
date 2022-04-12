from django.db import models
from auths.models import User, Clerk, Admin


class Store(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    clerk = models.ForeignKey(Clerk, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_store(self):
        self.save()

    def delete_store(self):
        self.delete()

    @classmethod
    def all_stores(cls):
        return cls.objects.all()


class Product(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    cost = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_product(self):
        self.save()

    def delete_product(self):
        self.delete()

    @classmethod
    def all_product(cls):
        return cls.objects.all()


class Stock(models.Model):
    PAYMENT_CHOICE = (
        ('paid', 'Paid'),
        ('Unpaid', 'Unpaid'),

    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    received_quantity = models.IntegerField(default=0)
    payment = models.CharField(max_length=10, choices=PAYMENT_CHOICE)
    spoilt_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name

    def save_stock(self):
        self.save()

    def delete_stock(self):
        self.delete()

    @classmethod
    def search_payment(cls, title):
        return cls.objects.filter(title__icontains='name').all()

    @classmethod
    def all_stock(cls):
        return cls.objects.all()


class Order_request(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.product.name

    def save_request(self):
        self.save()

    def delete_request(self):
        self.order()

    @classmethod
    def all_requests(cls):
        return cls.objects.all()


class Order_post(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    spoilt_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name

    def save_post(self):
        self.save()

    def delete_post(self):
        self.order()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()
