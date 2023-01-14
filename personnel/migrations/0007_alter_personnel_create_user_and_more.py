# Generated by Django 4.1.5 on 2023-01-14 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personnel', '0006_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='create_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personals', to='personnel.department'),
        ),
    ]
