# Generated by Django 4.2.7 on 2023-12-02 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_professor'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='image',
            field=models.ImageField(default=1, upload_to='static/profile1/images'),
        ),
        migrations.AddField(
            model_name='professor',
            name='slug',
            field=models.CharField(default=1, max_length=40, unique=True),
        ),
    ]
