# Generated by Django 3.2 on 2021-05-10 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0010_alter_camera_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='active',
            field=models.CharField(blank=True, default=True, max_length=6, null=True),
        ),
    ]