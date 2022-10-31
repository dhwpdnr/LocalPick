from django.db import models
from users.models import User

# Create your models here.


class Store(models.Model):
    store_name = models.CharField(max_length=30, default = "----")
    store_time = models.TextField(blank = True)
    store_adress = models.CharField(max_length=50, default="----")
    store_tel = models.CharField(max_length=20, default="----")
    category = models.ForeignKey("Category", on_delete = models.SET_NULL, null=True, db_column='category_id')
    # like_users = models.ManyToManyField('users.User', related_name="like_users", blank=True)

    # def count_like_users(self):
    #     return self.like_users.count()
    
    def __str__(self):
        return self.store_name


class Category(models.Model):
    category_name = models.CharField(max_length=25, default = "X")
    
    def __str__(self):
        return self.category_name


class Image(models.Model):
    store = models.ForeignKey("Store", on_delete=models.CASCADE, null=True, db_column="store_id")
    image_tag = models.TextField(null=True)