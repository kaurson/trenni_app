# Generated by Django 3.2.9 on 2021-11-27 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='autor',
            field=models.CharField(max_length=200, null=True),
        ),
    ]