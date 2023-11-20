# Generated by Django 4.2.6 on 2023-11-14 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fiche_medicale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_patient', models.CharField(default='')),
                ('age', models.IntegerField(null=True)),
                ('poids', models.IntegerField(null=True)),
                ('description', models.TextField(max_length=500)),
                ('prescription1', models.CharField(max_length=50)),
                ('prescription2', models.CharField(default='Vide', max_length=50, null=True)),
                ('prescription3', models.CharField(default='Vide', max_length=50, null=True)),
                ('lien', models.CharField(max_length=300)),
                ('date_jour', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'fiche_medicale',
                'verbose_name_plural': 'fiche_medicales',
                'db_table': 'fiche_medicale',
            },
        ),
        migrations.CreateModel(
            name='prescription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=250)),
                ('qrcode', models.ImageField(blank=True, null=True, upload_to='qr_img')),
            ],
            options={
                'verbose_name': 'prescription',
                'verbose_name_plural': 'prescriptions',
                'db_table': 'prescription',
            },
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
                'db_table': 'services',
            },
        ),
        migrations.CreateModel(
            name='tsexe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choix', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'tsexe',
            },
        ),
        migrations.CreateModel(
            name='patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('telephone', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_doc_cust.services')),
                ('sexe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_doc_cust.tsexe')),
            ],
            options={
                'verbose_name': 'patient',
                'verbose_name_plural': 'patients',
                'db_table': 'patients',
            },
        ),
        migrations.CreateModel(
            name='file_d_attente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField()),
                ('statut', models.BooleanField(default=False)),
                ('email', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_doc_cust.patients', to_field='email')),
            ],
            options={
                'verbose_name': 'file_d_attente',
                'verbose_name_plural': 'file_d_attentes',
                'db_table': 'file_d_attente',
            },
        ),
    ]