# Generated by Django 4.1.5 on 2023-02-03 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hero',
            old_name='linkprimary',
            new_name='buttonprimarytext',
        ),
        migrations.RenameField(
            model_name='hero',
            old_name='linksecondary',
            new_name='buttonprimaryurl',
        ),
        migrations.AddField(
            model_name='hero',
            name='buttonsecondarytext',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hero',
            name='buttonsecondaryurl',
            field=models.CharField(default='emptyfornow', max_length=255),
            preserve_default=False,
        ),
    ]
