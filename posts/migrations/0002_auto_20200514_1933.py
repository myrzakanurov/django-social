# Generated by Django 3.0.5 on 2020-05-14 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
    ]
