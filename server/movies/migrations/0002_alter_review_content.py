# Generated by Django 3.2.13 on 2022-11-21 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.CharField(max_length=100),
        ),
    ]
