# Generated by Django 4.2.5 on 2023-12-21 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_FINAL', '0002_alter_models_inscritos_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models_inscritos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='models_instituciones',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]