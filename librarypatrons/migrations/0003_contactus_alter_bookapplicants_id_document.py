# Generated by Django 5.0.1 on 2024-03-10 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarypatrons', '0002_bookapplicants'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('firstname', models.TextField(max_length=255)),
                ('lastname', models.TextField(max_length=255)),
                ('email', models.TextField(primary_key=True, serialize=False)),
                ('book_id', models.TextField(max_length=255)),
                ('feedback', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'contactus',
            },
        ),
        migrations.AlterField(
            model_name='bookapplicants',
            name='id_document',
            field=models.FileField(upload_to='id_document/'),
        ),
    ]