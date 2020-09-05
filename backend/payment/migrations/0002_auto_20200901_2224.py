# Generated by Django 2.0 on 2020-09-01 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='paymentdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=50)),
                ('token', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='made_by',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]