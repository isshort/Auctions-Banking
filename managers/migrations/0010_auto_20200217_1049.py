# Generated by Django 2.0 on 2020-02-17 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0009_auto_20200217_0236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applyclient',
            name='client',
        ),
        migrations.DeleteModel(
            name='ApplyClient',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]