# Generated by Django 4.2 on 2023-04-11 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ghb', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
