# Generated by Django 3.0.8 on 2020-08-08 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_auto_20200809_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='billing_address',
        ),
        migrations.AddField(
            model_name='order',
            name='apartment_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='street_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='zip',
            field=models.CharField(max_length=100, null=True),
        ),
    ]