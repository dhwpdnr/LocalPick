

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='X', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(default='----', max_length=30)),
                ('store_time', models.TextField(blank=True)),
                ('store_adress', models.CharField(default='----', max_length=50)),
                ('store_tel', models.CharField(default='----', max_length=20)),
                ('category', models.ForeignKey(db_column='category_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='stores.category')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_tag', models.TextField(null=True)),
                ('store', models.ForeignKey(db_column='store_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='stores.store')),
            ],
        ),
    ]
