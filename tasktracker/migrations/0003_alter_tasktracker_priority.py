# Generated by Django 4.1.4 on 2022-12-27 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasktracker', '0002_tasktracker_created_date_tasktracker_is_done_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasktracker',
            name='priority',
            field=models.SmallIntegerField(choices=[(3, 'Low'), (1, 'High'), (2, 'Medium')], default=3),
        ),
    ]
