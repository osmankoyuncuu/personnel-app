# Generated by Django 4.1.5 on 2023-01-10 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('is_staffed', models.BooleanField(default=False)),
                ('title', models.SmallIntegerField(choices=[(1, 'Team Lead'), (2, 'Mid Lead'), (3, 'Junior')], default=3)),
                ('gender', models.SmallIntegerField(choices=[(1, 'Female'), (2, 'Male'), (3, 'Other'), (4, 'Prefer Not Say')], default=4)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('create_user', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='personnel.department')),
            ],
        ),
    ]
