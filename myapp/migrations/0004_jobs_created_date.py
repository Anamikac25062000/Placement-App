# Generated by Django 5.0 on 2023-12-17 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_studentprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]