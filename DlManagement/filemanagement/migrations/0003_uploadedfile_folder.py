# Generated by Django 5.0.6 on 2024-06-26 00:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filemanagement", "0002_folder"),
    ]

    operations = [
        migrations.AddField(
            model_name="uploadedfile",
            name="folder",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="files",
                to="filemanagement.folder",
            ),
        ),
    ]
