# Generated by Django 3.0.7 on 2020-06-23 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='profile_picture',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
