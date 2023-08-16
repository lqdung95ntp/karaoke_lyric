# Generated by Django 4.2.4 on 2023-08-15 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Karaoke',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('song', models.CharField(max_length=200)),
                ('song_slug', models.CharField(editable=False, max_length=200)),
                ('lyric', models.TextField(max_length=2000)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('user_update', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
