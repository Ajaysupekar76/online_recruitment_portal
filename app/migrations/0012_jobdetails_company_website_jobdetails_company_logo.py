# Generated by Django 4.2.5 on 2024-02-07 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_jobdetails_user_id_jobdetails_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetails',
            name='Company_website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobdetails',
            name='company_logo',
            field=models.ImageField(default=1, upload_to='img/company'),
            preserve_default=False,
        ),
    ]
