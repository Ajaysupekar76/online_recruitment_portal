# Generated by Django 4.2.5 on 2024-02-04 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_jobdetails_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobdetails',
            name='user_id',
        ),
        migrations.AddField(
            model_name='jobdetails',
            name='company_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.company'),
            preserve_default=False,
        ),
    ]
