# Generated by Django 4.2.4 on 2023-08-08 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0006_postimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="CommentReply",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reply", models.TextField()),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_reply",
                        to="posts.postcomment",
                    ),
                ),
            ],
        ),
    ]
