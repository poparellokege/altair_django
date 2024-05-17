# Generated by Django 3.2.3 on 2021-06-06 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INDICOapp', '0003_category_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('instagram_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='team/')),
                ('details', models.TextField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]