# Generated by Django 4.1.3 on 2022-11-30 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_studentproxy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentproxy',
            options={'ordering': ['-id']},
        ),
    ]
