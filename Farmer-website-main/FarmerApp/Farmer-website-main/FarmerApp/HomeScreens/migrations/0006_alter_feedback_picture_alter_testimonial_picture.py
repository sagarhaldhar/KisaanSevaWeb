# Generated by Django 5.0.2 on 2024-03-14 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeScreens', '0005_alter_feedback_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='picture',
            field=models.ImageField(upload_to='feedback/'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='picture',
            field=models.ImageField(upload_to='testimonial/'),
        ),
    ]