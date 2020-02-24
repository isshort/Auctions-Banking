# Generated by Django 2.0 on 2020-02-23 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('inn', models.CharField(max_length=100)),
                ('okpo', models.CharField(max_length=100)),
                ('L_addr', models.CharField(max_length=150)),
                ('L_addr1', models.CharField(max_length=150)),
                ('R_person', models.CharField(max_length=100)),
                ('B_contact', models.CharField(max_length=150)),
                ('S_contact', models.CharField(max_length=150)),
                ('currentBalance', models.DecimalField(decimal_places=4, default=0, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='FeedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents', models.FileField(blank=True, default='/media/index.jpeg', upload_to='media')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='managers.Bank')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
