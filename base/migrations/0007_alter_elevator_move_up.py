# Generated by Django 4.2.2 on 2023-06-29 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_move_down_elevator_in_motion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevator',
            name='move_up',
            field=models.BooleanField(default=True),
        ),
    ]
