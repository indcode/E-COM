# Generated by Django 2.0 on 2020-08-18 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20200818_0814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='identity',
        ),
        migrations.AddField(
            model_name='user_data',
            name='contact',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user_data',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
