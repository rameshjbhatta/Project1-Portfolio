# Generated by Django 4.2 on 2023-08-21 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='session_key',
            field=models.CharField(blank=True, default='guest_session', max_length=40, null=True),
        ),
    ]