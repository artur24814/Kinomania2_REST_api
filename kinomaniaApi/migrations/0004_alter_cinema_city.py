# Generated by Django 4.0.6 on 2022-07-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinomaniaApi', '0003_alter_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]