# Generated by Django 4.2.4 on 2023-11-23 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepositBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('join_member', models.TextField()),
                ('join_way', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('etc_note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cur_unit', models.TextField()),
                ('cur_nm', models.TextField()),
                ('deal_bas_r', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SavingBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('join_member', models.TextField()),
                ('join_way', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('etc_note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SavingOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_trm', models.IntegerField()),
                ('intr_rate_type_nm', models.TextField()),
                ('intr_rate', models.FloatField()),
                ('intr_rate2', models.FloatField()),
                ('savingbase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.savingbase')),
            ],
        ),
        migrations.CreateModel(
            name='DepositOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_trm', models.IntegerField()),
                ('intr_rate_type_nm', models.TextField()),
                ('intr_rate', models.FloatField()),
                ('intr_rate2', models.FloatField()),
                ('depositbase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.depositbase')),
            ],
        ),
    ]
