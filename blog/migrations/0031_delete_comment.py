# Generated by Django 5.0.4 on 2024-05-12 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
