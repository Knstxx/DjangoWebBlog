# Generated by Django 3.2.16 on 2024-02-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240228_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]