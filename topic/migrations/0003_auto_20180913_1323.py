# Generated by Django 2.0 on 2018-09-13 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0002_auto_20180913_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic_comment',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='topic_comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Topic_Comment',
        ),
    ]
