# Generated by Django 5.1.5 on 2025-02-02 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0006_rename_contact_contact_message_contact_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['created_at']},
        ),
        migrations.RemoveField(
            model_name='contact',
            name='post',
        ),
    ]
