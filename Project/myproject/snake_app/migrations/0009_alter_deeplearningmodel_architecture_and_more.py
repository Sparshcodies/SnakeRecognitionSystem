# Generated by Django 4.2.7 on 2023-11-23 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snake_app', '0008_remove_snake_caption_snake_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deeplearningmodel',
            name='architecture',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='deeplearningmodel',
            name='weights',
            field=models.FileField(upload_to='models'),
        ),
    ]
