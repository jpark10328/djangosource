# Generated by Django 4.1.1 on 2022-09-30 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_post_like"),
    ]

    operations = [
        migrations.RenameField(model_name="post", old_name="like", new_name="likes",),
    ]
