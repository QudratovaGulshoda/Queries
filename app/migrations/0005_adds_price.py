# Generated by Django 4.2.6 on 2023-11-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_adds_viewers'),
    ]

    operations = [
        migrations.AddField(
            model_name='adds',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]