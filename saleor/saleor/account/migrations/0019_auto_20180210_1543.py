# Generated by Django 2.0.2 on 2018-02-10 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impersonate', '0001_initial'),
        ('social_django', '0008_partial_timestamp'),
        ('order', '0033_auto_20180123_0832'),
        ('cart', '0005_auto_20180108_0814'),
        ('account', '0018_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
