# Generated by Django 2.2.3 on 2019-07-23 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disney', '0002_auto_20190723_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disney',
            name='image',
        ),
        migrations.AddField(
            model_name='disney',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]
