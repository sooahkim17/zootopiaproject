# Generated by Django 2.2.3 on 2019-07-23 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disney', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disney',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='disney',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]