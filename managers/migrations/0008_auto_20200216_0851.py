# Generated by Django 2.0 on 2020-02-16 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0007_auto_20200216_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyclient',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managers.Client'),
        ),
    ]
