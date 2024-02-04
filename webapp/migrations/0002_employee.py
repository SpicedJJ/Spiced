# Generated by Django 4.2.7 on 2023-12-10 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Name', models.CharField(max_length=65, null=True)),
                ('Employee_ID', models.IntegerField(blank=True, max_length=65)),
                ('Employee_Contact_Number', models.IntegerField(blank=True, max_length=65)),
            ],
        ),
    ]
