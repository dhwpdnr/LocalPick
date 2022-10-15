# Generated by Django 4.1.2 on 2022-10-14 01:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0002_review_delete_reiview'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='store_id',
            field=models.ForeignKey(db_column='store_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='stores.store'),
        ),
        migrations.AddField(
            model_name='review',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 14, 10, 26, 15, 505305)),
        ),
    ]
