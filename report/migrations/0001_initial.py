# Generated by Django 4.2.6 on 2023-11-02 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='report.district')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='report.school')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answers', models.IntegerField()),
                ('wrong_answers', models.IntegerField()),
                ('total_questions', models.IntegerField()),
                ('percentage', models.DecimalField(decimal_places=1, max_digits=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='report.student')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='report.region'),
        ),
    ]
