# Generated by Django 4.2.5 on 2023-10-27 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogAPI', '0004_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='postDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]