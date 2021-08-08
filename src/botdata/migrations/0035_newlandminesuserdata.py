# Generated by Django 3.2.5 on 2021-08-08 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('botdata', '0034_alter_landminesuserdata_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewLandminesUserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_played', models.DateTimeField(auto_now_add=True)),
                ('last_seen', models.DateTimeField(auto_now_add=True)),
                ('messages_sent', models.IntegerField(default=0)),
                ('words_sent', models.IntegerField(default=0)),
                ('points_won', models.IntegerField(default=0)),
                ('points_recovered', models.IntegerField(default=0)),
                ('points_acquired', models.IntegerField(default=0)),
                ('points_current', models.IntegerField(default=0)),
                ('points_exploded', models.IntegerField(default=0)),
                ('points_spent', models.IntegerField(default=0)),
                ('defuse_kits_bought', models.IntegerField(default=0)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='new_landmines_data', to='botdata.discordmember')),
            ],
            options={
                'db_table': 'landmines_userdata',
            },
        ),
    ]
