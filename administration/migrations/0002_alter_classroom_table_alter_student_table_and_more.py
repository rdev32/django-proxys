# Generated by Django 4.1.3 on 2022-11-30 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='classroom',
            table='classroom',
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
        migrations.AlterModelTable(
            name='teacher',
            table='teacher',
        ),
    ]
