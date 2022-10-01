# Generated by Django 4.1.1 on 2022-09-29 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_lesson_review_comment_bookedlesson'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='caption',
            new_name='video',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=500, null=True),
        ),
    ]