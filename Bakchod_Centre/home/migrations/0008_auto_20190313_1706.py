# Generated by Django 2.1.5 on 2019-03-13 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20190312_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=1000)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='current_location',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='education',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='education_place',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='job',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='job_place',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='relationship_status',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='connection',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_friend', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='connection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
