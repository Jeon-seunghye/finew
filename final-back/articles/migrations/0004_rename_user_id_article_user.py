# Generated by Django 4.2.4 on 2023-11-18 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_user_article_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='user_id',
            new_name='user',
        ),
    ]
