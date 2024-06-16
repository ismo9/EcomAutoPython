from django.db import models
import datetime
from django.contrib.auth.models import User

# Categories de produits
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'
    

# Les Clients
class Customer(models.Model):
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Telephone = models.CharField(max_length=10)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.Nom} {self.Prenom}'
    
# Les Produits
class Product(models.Model):
    Nom_prod = models.CharField(max_length=100)
    Prix = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    Category =models.ForeignKey(Category, on_delete=models.CASCADE, default=1) 
    Description =models.CharField(max_length=250, default='', blank=True, null=True)
    Image = models.ImageField(upload_to='uploads/product/')
    
    is_sale = models.BooleanField(default=False)
    sale_price= models.DecimalField(default=0, decimal_places=2, max_digits=7)
    def __str__(self):
        return self.Nom_prod


# Les commandes
class Order(models.Model):
    Produit = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE ,default=1)
    Quantity = models.IntegerField(default=1)
    Address = models.CharField(max_length=100, default='', blank=True)
    Telephone = models.CharField(max_length=20, default='', blank=True)
    Date = models.DateField(default=datetime.datetime.today)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'
    

from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    




