# Generated by Django 3.2 on 2021-04-21 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='image/Pottawatomie County State Lake #2 in Manhattan, KS.png', upload_to=''),
        ),
    ]
