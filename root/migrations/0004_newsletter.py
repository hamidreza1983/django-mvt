# Generated by Django 4.2 on 2024-08-13 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0003_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
