# Generated by Django 3.1.7 on 2021-03-13 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_auto_20210309_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
