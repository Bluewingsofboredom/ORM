# Generated by Django 5.1.3 on 2024-11-12 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankLoan',
            fields=[
                ('loanid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('loantype', models.CharField(max_length=30)),
                ('amount', models.IntegerField()),
                ('c_acnt_num', models.IntegerField()),
            ],
        ),
    ]