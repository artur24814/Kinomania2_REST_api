# Generated by Django 4.0.6 on 2022-07-17 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinomaniaApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='position',
            field=models.CharField(choices=[('actor', 'actor'), ('director', 'director')], default='actor', max_length=128),
        ),
    ]