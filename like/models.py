from django.db import models

# Create your models here.

class Like(models.Model):
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE, db_column='user_id')
    store_id = models.ForeignKey("stores.Store", on_delete=models.CASCADE, db_column='store_id')
    is_liked = models.BooleanField(default=False)
    
    def __str__(self):
        return "[%s %s %d]" % (self.store_id, self.user_id, self.is_liked)