# Generated by Django 5.1.4 on 2024-12-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OutfitPlanner', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='clothes',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
