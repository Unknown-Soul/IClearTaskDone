# Generated by Django 3.2.8 on 2021-10-24 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip',
            name='status',
            field=models.CharField(default='Down', max_length=10),
        ),
    ]
