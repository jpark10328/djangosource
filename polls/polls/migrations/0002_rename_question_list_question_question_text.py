# Generated by Django 4.1.1 on 2022-09-26 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question", old_name="question_list", new_name="question_text",
        ),
    ]