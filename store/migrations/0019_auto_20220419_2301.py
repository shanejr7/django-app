# Generated by Django 3.2.5 on 2022-04-19 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20220419_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='timestamp',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='follower',
            name='timestamp',
            field=models.TextField(null=True),
        ),
    ]