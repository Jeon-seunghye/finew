# Generated by Django 4.2.4 on 2023-11-22 02:35

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('banks', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('nickname', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('age', models.IntegerField(null=True)),
                ('money', models.IntegerField(null=True)),
                ('salary', models.IntegerField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FinancialProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposits', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='banks.depositoption')),
                ('savings', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='banks.savingoption')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='deposit_options',
            field=models.ManyToManyField(blank=True, related_name='users', through='accounts.FinancialProduct', to='banks.depositoption'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='saving_options',
            field=models.ManyToManyField(blank=True, related_name='users', through='accounts.FinancialProduct', to='banks.savingoption'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
