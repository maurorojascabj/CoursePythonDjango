# Generated by Django 3.2.6 on 2021-08-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210826_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
    ]
