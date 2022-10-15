from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Appetite(models.Model):
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, db_column="user_id")
    spicy = models.PositiveIntegerField(default=0,
                                        validators=[
                                            MaxValueValidator(5),
                                            MinValueValidator(1)
                                        ])
    salty = models.PositiveIntegerField(default=0,
                                        validators=[
                                            MaxValueValidator(5),
                                            MinValueValidator(1)
                                        ])
    sweety = models.PositiveIntegerField(default=0,
                                        validators=[
                                            MaxValueValidator(5),
                                            MinValueValidator(1)
                                        ])
    amount = models.PositiveIntegerField(default=0,
                                        validators=[
                                            MaxValueValidator(5),
                                            MinValueValidator(1)
                                        ])

    def __str__(self):
        return "<%d 식성향>" % (self.user_id)