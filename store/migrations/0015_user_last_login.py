# Generated by Django 3.2.5 on 2022-02-12 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]