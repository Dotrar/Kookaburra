# Generated by Django 3.2.8 on 2021-10-31 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kookaburra', '0003_auto_20211031_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='kookaburrapost',
            name='commenting_allowed',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='kookaburracomment',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='kookaburra.kookaburrapost'),
        ),
        migrations.AlterField(
            model_name='kookaburrapost',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='kookaburra.kookaburrasection'),
        ),
    ]