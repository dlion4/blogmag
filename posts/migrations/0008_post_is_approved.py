# Generated by Django 4.2.4 on 2023-08-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0007_commentreply"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="is_approved",
            field=models.BooleanField(default=False),
        ),
    ]
