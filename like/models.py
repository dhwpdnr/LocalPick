from django.db import models

# Create your models here.


class Like(models.Model):
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, db_column="user_id")
    store_id = models.ForeignKey("stores.Store", on_delete=models.CASCADE, null=True, db_column="store_id")
