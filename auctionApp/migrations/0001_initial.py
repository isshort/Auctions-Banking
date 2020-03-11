# Generated by Django 2.0.1 on 2020-03-11 15:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expire_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_rate', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
            ],
        ),
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
            name='BasicInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=100)),
                ('spouse_name', models.CharField(max_length=100)),
                ('dependant', models.CharField(max_length=100)),
                ('birth_date', models.CharField(max_length=100)),
                ('birth_palce', models.CharField(max_length=100)),
                ('passport_no', models.CharField(max_length=100)),
                ('issued_by', models.CharField(max_length=100)),
                ('issued_date', models.CharField(max_length=100)),
                ('register_place', models.CharField(max_length=100)),
                ('residential_add', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('inn', models.CharField(max_length=100)),
                ('contacts', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_activity', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
                ('employee_num', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Collateral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('market_value', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Credit_History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=100)),
                ('receiving_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('maturity_date', models.DateTimeField()),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('currency_unit', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Credit_line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposed_loan', models.CharField(max_length=100)),
                ('credit_amount', models.CharField(max_length=100)),
                ('period', models.DateTimeField()),
                ('goal', models.CharField(max_length=100)),
                ('contribution_amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='FeedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents', models.FileField(blank=True, default='/media/index.jpeg', upload_to='media')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='auctionApp.Bank')),
            ],
        ),
        migrations.CreateModel(
            name='Guarantee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No', models.PositiveIntegerField()),
                ('applicant', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('income', models.CharField(max_length=100)),
                ('market_value', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=42)),
                ('phone', models.CharField(default='', max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(default='')),
                ('password', models.CharField(default=None, max_length=128, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_client', models.BooleanField(default=False)),
                ('is_bank', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('accept_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctionApp.AcceptClient')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctionApp.Bank')),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_activity', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('certificate', models.FileField(blank=True, default='/media/index.jpeg', upload_to='media/clients')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auctionApp.Register')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='guarantee',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auctionApp.Register'),
        ),
        migrations.AddField(
            model_name='credit_line',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auctionApp.Register'),
        ),
        migrations.AddField(
            model_name='credit_history',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auctionApp.Register'),
        ),
        migrations.AddField(
            model_name='collateral',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auctionApp.Register'),
        ),
        migrations.AddField(
            model_name='business',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auctionApp.Register'),
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auctionApp.Register'),
        ),
        migrations.AddField(
            model_name='acceptclient',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctionApp.Register'),
        ),
        migrations.AddField(
            model_name='acceptclient',
            name='collateral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctionApp.Collateral'),
        ),
        migrations.AddField(
            model_name='acceptclient',
            name='credit_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctionApp.Credit_History'),
        ),
        migrations.AddField(
            model_name='acceptclient',
            name='credit_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctionApp.Credit_line'),
        ),
    ]