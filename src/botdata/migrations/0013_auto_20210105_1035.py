# Generated by Django 3.1.4 on 2021-01-05 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('botdata', '0012_auto_20210105_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='channel',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='botdata.discordchannel'),
        ),
    ]
