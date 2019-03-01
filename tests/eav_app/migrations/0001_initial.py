# Generated by Django 2.1.7 on 2019-02-28 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'entities',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('units', models.TextField(blank=True, null=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eav_app.Attribute')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='values', to='eav_app.Entity')),
            ],
        ),
    ]
