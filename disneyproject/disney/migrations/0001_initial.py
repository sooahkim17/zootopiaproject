# Generated by Django 2.2.3 on 2019-07-23 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_name', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
