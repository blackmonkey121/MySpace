# Generated by Django 2.0.1 on 2020-07-23 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cookingtag',
            options={'ordering': ['-id']},
        ),
    ]
