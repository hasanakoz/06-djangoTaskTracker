# Generated by Django 4.1.4 on 2022-12-27 17:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasktracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktracker',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasktracker',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tasktracker',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tasktracker',
            name='priority',
            field=models.SmallIntegerField(choices=[(2, 'Medium'), (1, 'High'), (3, 'Low')], default=3),
        ),
    ]