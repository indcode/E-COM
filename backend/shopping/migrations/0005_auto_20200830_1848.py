# Generated by Django 2.0 on 2020-08-30 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_auto_20200830_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
