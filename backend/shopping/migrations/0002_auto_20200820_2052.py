# Generated by Django 2.0 on 2020-08-20 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingridients',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='ingridients',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
