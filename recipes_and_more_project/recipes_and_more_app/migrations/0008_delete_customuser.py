# Generated by Django 4.0.3 on 2022-03-14 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_and_more_app', '0007_customuser_delete_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]