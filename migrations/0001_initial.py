# Generated by Django 5.1 on 2024-09-17 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('complete', models.BooleanField()),
                ('expenseList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.expenseblock')),
            ],
        ),
        migrations.AddField(
            model_name='expenseblock',
            name='ExpenseBlockList',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.expensetracker'),
        ),
    ]
