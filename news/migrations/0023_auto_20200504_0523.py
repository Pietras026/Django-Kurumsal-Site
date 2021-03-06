# Generated by Django 3.0.4 on 2020-05-04 02:23

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0022_auto_20200504_0400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='slugs',
            new_name='slug',
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='news.Category'),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Category'),
        ),
    ]
