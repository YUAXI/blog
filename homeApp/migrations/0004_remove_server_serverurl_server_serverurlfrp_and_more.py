# Generated by Django 5.0.6 on 2024-09-15 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0003_project_projecturl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='serverUrl',
        ),
        migrations.AddField(
            model_name='server',
            name='serverUrlFrp',
            field=models.URLField(default='', null=True, verbose_name='服务器穿透址'),
        ),
        migrations.AddField(
            model_name='server',
            name='serverUrlLan',
            field=models.URLField(default='', verbose_name='服务器内网IPv4地址'),
        ),
        migrations.AddField(
            model_name='server',
            name='serverUrlWan',
            field=models.URLField(default='', null=True, verbose_name='服务器公网IPv4地址'),
        ),
        migrations.AddField(
            model_name='server',
            name='serverUrlWan6',
            field=models.URLField(default='', null=True, verbose_name='服务器公网IPv6地址'),
        ),
        migrations.AlterField(
            model_name='server',
            name='serverImg',
            field=models.ImageField(upload_to='serverImg/', verbose_name='服务标'),
        ),
    ]