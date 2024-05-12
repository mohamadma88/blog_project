# Generated by Django 5.0.4 on 2024-05-11 22:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_comments_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.article'),
        ),
    ]
