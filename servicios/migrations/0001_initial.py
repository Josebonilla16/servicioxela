# Generated by Django 2.1.3 on 2018-11-04 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=200)),
                ('linea', models.CharField(max_length=200)),
                ('modelo', models.IntegerField()),
                ('color', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Carro')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='detalle',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='carro',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Cliente'),
        ),
        migrations.AddField(
            model_name='carro',
            name='servicios',
            field=models.ManyToManyField(through='servicios.Detalle', to='servicios.Servicio'),
        ),
    ]
