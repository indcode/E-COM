# Generated by Django 2.0 on 2020-08-19 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_onetimepassword_u'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='user_data',
            name='email',
        ),
        migrations.AddField(
            model_name='user_data',
            name='identity',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
