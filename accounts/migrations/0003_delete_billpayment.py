# Generated by Django 5.1.4 on 2024-12-28 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_billpayment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BillPayment',
        ),
    ]
