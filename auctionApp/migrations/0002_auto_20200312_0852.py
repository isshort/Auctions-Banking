# Generated by Django 2.0.1 on 2020-03-12 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctionApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctionApp.Register'),
        ),
    ]