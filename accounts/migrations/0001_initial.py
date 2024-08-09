# Generated by Django 5.0.7 on 2024-08-06 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAuthentication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('used_at', models.DateTimeField()),
            ],
        ),
    ]
