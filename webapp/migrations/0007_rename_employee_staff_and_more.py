# Generated by Django 4.2.7 on 2023-12-10 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_product_product_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Staff',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='Employee_Contact_Number',
            new_name='Staff_Contact_Number',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='Employee_ID',
            new_name='Staff_ID',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='Employee_Name',
            new_name='Staff_Name',
        ),
    ]
