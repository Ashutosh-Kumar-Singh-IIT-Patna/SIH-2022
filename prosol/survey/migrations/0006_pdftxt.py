# Generated by Django 4.1 on 2022-08-26 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_jobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='pdftxt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]