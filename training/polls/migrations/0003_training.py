# Generated by Django 3.2.9 on 2021-11-27 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('organiser', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
