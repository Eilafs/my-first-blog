# Generated by Django 2.1.1 on 2018-12-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]