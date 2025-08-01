# Generated by Django 5.2.4 on 2025-08-02 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_feedback_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=500, verbose_name='Вопросы'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
