# Generated by Django 5.0.1 on 2024-02-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_savedata_submit_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='r_no',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_no', models.CharField(max_length=9)),
            ],
        ),
    ]
