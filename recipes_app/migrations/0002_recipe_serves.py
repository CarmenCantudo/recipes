# Generated by Django 3.2.16 on 2022-12-21 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='serves',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
