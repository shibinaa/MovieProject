# Generated by Django 3.2.13 on 2022-07-02 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='aaa', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
