from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


# Create your models here.

class Review(models.Model):
    amount = models.PositiveIntegerField(default=0,
                                         validators=[
                                             MaxValueValidator(5),
                                             MinValueValidator(1)
                                         ]
                                         )
    kindness = models.PositiveIntegerField(default=0,
                                           validators=[
                                               MaxValueValidator(5),
                                               MinValueValidator(1)
                                           ])
    hygiene = models.PositiveIntegerField(default=0,
                                          validators=[
                                              MaxValueValidator(5),
                                              MinValueValidator(1)
                                          ])
    price = models.PositiveIntegerField(default=0,
                                        validators=[
                                            MaxValueValidator(5),
                                            MinValueValidator(1)
                                        ])
    star_rating = models.FloatField(default=3.0,
                                    validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
                                    )

    description = models.TextField(null=True)
    created = models.DateTimeField(default=datetime.now(), blank=True, null=True)
    store_id = models.ForeignKey("stores.Store", on_delete=models.CASCADE, null=True, db_column="store_id")
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, db_column="user_id")
    local = models.CharField(default='N', max_length=1)

    def __str__(self):
        return "<%d %f>" % (self.pk, self.star_rating)
