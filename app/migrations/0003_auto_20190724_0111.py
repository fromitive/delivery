# Generated by Django 2.2.3 on 2019-07-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190724_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='delivery',
            name='name',
            field=models.TextField(),
        ),
    ]
