# Generated by Django 3.1 on 2020-08-19 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_auto_20200803_1413'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='member',
            constraint=models.UniqueConstraint(fields=('user', 'project'), name='accounts_member_no_duplicates'),
        ),
    ]