# Generated by Django 4.1.5 on 2023-01-28 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='completado',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
