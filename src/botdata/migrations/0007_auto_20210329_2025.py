# Generated by Django 3.1.7 on 2021-03-29 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botdata', '0006_auto_20210329_1146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supportticket',
            options={'ordering': ['-opened_at']},
        ),
    ]
