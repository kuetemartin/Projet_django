# Generated by Django 4.1.4 on 2022-12-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAgents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useragent', models.CharField(max_length=30)),
                ('popularity', models.IntegerField()),
            ],
        ),
    ]
