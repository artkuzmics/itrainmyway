# Generated by Django 3.0 on 2021-05-03 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20210503_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='quize',
            name='session_key',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
