# Generated by Django 2.0.2 on 2018-02-11 01:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_auto_20180210_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_name', models.CharField(max_length=256, unique=True)),
                ('company_desc', models.CharField(blank=True, max_length=256)),
                ('company_logo', models.ImageField(blank=None, upload_to='')),
                ('company_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Company'),
        ),
    ]
