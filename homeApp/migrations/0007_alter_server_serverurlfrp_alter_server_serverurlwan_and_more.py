# Generated by Django 5.0.6 on 2024-09-16 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0006_alter_project_projectdetail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='serverUrlFrp',
            field=models.URLField(blank=True, null=True, verbose_name='服务器穿透址'),
        ),
        migrations.AlterField(
            model_name='server',
            name='serverUrlWan',
            field=models.URLField(blank=True, null=True, verbose_name='服务器公网IPv4地址'),
        ),
        migrations.AlterField(
            model_name='server',
            name='serverUrlWan6',
            field=models.URLField(blank=True, null=True, verbose_name='服务器公网IPv6地址'),
        ),
    ]
