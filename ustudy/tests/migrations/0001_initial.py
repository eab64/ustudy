# Generated by Django 4.2 on 2023-04-23 11:06

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
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Город',
            },
        ),
        migrations.CreateModel(
            name='DrivingCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_multiple_choice', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='question_images/')),
                ('language', models.CharField(choices=[('kz', 'Kz'), ('ru', 'Ru')], default='ru', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('name_kz', models.CharField(blank=True, max_length=255, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_kz', models.TextField(blank=True, null=True)),
                ('time_to_pass', models.PositiveSmallIntegerField(default=30)),
                ('max_errors', models.PositiveSmallIntegerField(default=3)),
                ('questions_count', models.PositiveSmallIntegerField(default=30)),
                ('driving_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='tests.drivingcategory')),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_question_showed', models.DateTimeField(auto_now_add=True)),
                ('last_question_closed', models.DateTimeField(null=True)),
                ('finished', models.BooleanField(default=False)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.question')),
                ('test_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='tests.testresult')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='tests.test'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='tests.question'),
        ),
    ]