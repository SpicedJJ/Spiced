# Generated by Django 4.2.7 on 2023-12-10 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_ID', models.IntegerField(blank=True, max_length=65)),
                ('payment_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
