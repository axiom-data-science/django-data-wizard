# Generated by Django 2.2.12 on 2020-06-23 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_wizard', '0003_identifier_allow_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identifier',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='spreadsheet value'),
        ),
    ]