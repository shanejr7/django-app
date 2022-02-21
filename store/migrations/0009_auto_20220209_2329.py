# Generated by Django 3.2.5 on 2022-02-09 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20220206_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='stakeholder',
            name='user_id',
        ),
        migrations.AddField(
            model_name='auction',
            name='application',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.user'),
        ),
        migrations.AddField(
            model_name='stage',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.user'),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.user'),
        ),
    ]
