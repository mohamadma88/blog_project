# Generated by Django 5.0.4 on 2024-05-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_alter_comment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
