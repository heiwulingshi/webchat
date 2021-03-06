# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-01 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatFriend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ChatHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('content', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='GroupFriend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserCate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('addr', models.CharField(max_length=32)),
                ('cnum', models.IntegerField(max_length=32)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.User')),
            ],
        ),
        migrations.AddField(
            model_name='groupfriend',
            name='friend',
            field=models.ManyToManyField(to='app01.User'),
        ),
        migrations.AddField(
            model_name='groupfriend',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.Group'),
        ),
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.User'),
        ),
        migrations.AddField(
            model_name='chathistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.User'),
        ),
        migrations.AddField(
            model_name='chatfriend',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.User'),
        ),
        migrations.AddField(
            model_name='chatfriend',
            name='history',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.ChatHistory'),
        ),
    ]
