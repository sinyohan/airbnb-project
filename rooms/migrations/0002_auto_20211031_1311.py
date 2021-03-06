# Generated by Django 2.2.5 on 2021-10-31 04:11

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
