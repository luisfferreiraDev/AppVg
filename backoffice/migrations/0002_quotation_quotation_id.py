# Generated by Django 4.2.1 on 2023-05-28 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='quotation_id',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
