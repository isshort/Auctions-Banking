# Generated by Django 2.0.1 on 2020-03-12 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionApp', '0002_auto_20200312_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]
