# Generated by Django 2.0 on 2020-08-20 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0010_auto_20200819_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='ingridients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('buyer', models.ForeignKey(on_delete='DO_NOTHING', to='registration.user_data')),
                ('product', models.ForeignKey(on_delete='DO_NOTHING', to='shopping.ingridients')),
            ],
        ),
    ]
