# Generated by Django 4.2.7 on 2023-11-22 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snake_app', '0006_deeplearningmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deeplearningmodel',
            name='architecture',
            field=models.TextField(verbose_name='model_files/'),
        ),
    ]