# Generated by Django 4.2 on 2023-08-16 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_projectinfo_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloginfo',
            name='blog_content',
            field=models.TextField(max_length=600),
        ),
    ]
