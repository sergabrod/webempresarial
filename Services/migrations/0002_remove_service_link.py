# Generated by Django 2.1 on 2018-09-26 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='link',
        ),
    ]
