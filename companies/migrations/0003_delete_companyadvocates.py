# Generated by Django 3.2.8 on 2022-10-19 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_alter_companyadvocates_company'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CompanyAdvocates',
        ),
    ]