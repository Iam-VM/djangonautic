# Generated by Django 3.1.4 on 2021-01-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='thumb',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]