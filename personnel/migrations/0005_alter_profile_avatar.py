# Generated by Django 4.1.5 on 2023-01-12 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0004_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='pictures/avatar.webp', upload_to='pictures'),
        ),
    ]
