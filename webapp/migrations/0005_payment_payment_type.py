# Generated by Django 4.2.7 on 2023-12-10 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_Type',
            field=models.CharField(max_length=65, null=True),
        ),
    ]
