# Generated by Django 5.2 on 2025-04-08 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcareprovider',
            name='email',
            field=models.EmailField(default='aubrey10302000@yahoo.com', max_length=254),
        ),
    ]
