# Generated by Django 4.2.5 on 2024-02-03 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_user_candidate_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='lobo_pic',
            new_name='logo_pic',
        ),
    ]
