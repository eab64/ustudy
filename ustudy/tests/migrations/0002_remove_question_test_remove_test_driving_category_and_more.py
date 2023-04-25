# Generated by Django 4.2 on 2023-04-24 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='test',
        ),
        migrations.RemoveField(
            model_name='test',
            name='driving_category',
        ),
        migrations.RemoveField(
            model_name='testresult',
            name='test',
        ),
        migrations.RemoveField(
            model_name='testresult',
            name='user',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='test_result',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='DrivingCategory',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='TestResult',
        ),
        migrations.DeleteModel(
            name='UserAnswer',
        ),
    ]