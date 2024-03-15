# Generated by Django 5.0.2 on 2024-03-15 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeScreens', '0013_contactusform'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadResearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=500)),
                ('Profile', models.ImageField(blank=True, null=True, upload_to='researchProfile/')),
                ('paper', models.ImageField(blank=True, null=True, upload_to='researchpaper/')),
            ],
        ),
    ]