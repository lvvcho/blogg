# Generated by Django 4.1.4 on 2022-12-24 17:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
