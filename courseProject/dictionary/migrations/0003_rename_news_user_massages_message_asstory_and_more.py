# Generated by Django 4.1.3 on 2022-12-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_gender_word_user_blocks_user_friends_user_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='news',
            new_name='Massages',
        ),
        migrations.AddField(
            model_name='message',
            name='asStory',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
