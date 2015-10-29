# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_inicio', models.DateTimeField()),
                ('data_final', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'anuncio',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AnuncioHasInteressado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('anuncio', models.ForeignKey(to='core.Anuncio')),
                ('interessado', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'anuncio_has_interessado',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Beneficio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, null=True, blank=True)),
                ('tipo', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'beneficio',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Disponibilidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_inicio', models.DateTimeField()),
                ('data_final', models.DateTimeField()),
            ],
            options={
                'db_table': 'disponibilidade',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cidade', models.CharField(max_length=50, null=True, blank=True)),
                ('bairro', models.CharField(max_length=100, null=True, blank=True)),
                ('rua', models.CharField(max_length=100, null=True, blank=True)),
                ('complemento', models.CharField(max_length=100, null=True, blank=True)),
                ('cep', models.CharField(max_length=100, null=True, blank=True)),
                ('tipo', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'endereco',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Gosto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'gosto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('metro_quadrado', models.FloatField(null=True, blank=True)),
                ('bairro', models.CharField(max_length=45, null=True, blank=True)),
                ('nome_rua', models.CharField(max_length=100, null=True, blank=True)),
                ('numero_casa_ap', models.IntegerField(null=True, blank=True)),
                ('cep_imovel', models.CharField(max_length=45, null=True, blank=True)),
                ('observacoes', models.TextField(null=True, blank=True)),
                ('cidade', models.CharField(max_length=45, null=True, blank=True)),
                ('venda', models.BooleanField(default=False)),
                ('disponivel', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('proprietario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'imovel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImovelHasAvaliacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estrelas', models.IntegerField()),
                ('mensagem', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('avaliador', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('imovel', models.ForeignKey(to='core.Imovel')),
            ],
            options={
                'db_table': 'imovel_has_avaliacao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImovelHasBeneficio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('metro_quadrado', models.FloatField(null=True, blank=True)),
                ('quantidade', models.IntegerField(null=True, blank=True)),
                ('beneficio', models.ForeignKey(to='core.Beneficio')),
                ('imovel', models.ForeignKey(to='core.Imovel')),
            ],
            options={
                'db_table': 'imovel_has_beneficio',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImovelHasDisponibilidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disponibilidade', models.ForeignKey(to='core.Disponibilidade')),
                ('imovel', models.ForeignKey(to='core.Imovel')),
            ],
            options={
                'db_table': 'imovel_has_disponibilidade',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImovelHasItemIncluso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imovel', models.ForeignKey(to='core.Imovel')),
            ],
            options={
                'db_table': 'imovel_has_item_incluso',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImovelHasLugarProximo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imovel', models.ForeignKey(to='core.Imovel')),
            ],
            options={
                'db_table': 'imovel_has_lugar_proximo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImovelHasPeriodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imovel', models.ForeignKey(to='core.Imovel')),
            ],
            options={
                'db_table': 'imovel_has_periodo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImovelHasRegra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('possibilidade', models.BooleanField()),
                ('imovel', models.ForeignKey(to='core.Imovel')),
            ],
            options={
                'db_table': 'imovel_has_regra',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImovelHasValor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imovel', models.ForeignKey(to='core.Imovel')),
            ],
            options={
                'db_table': 'imovel_has_valor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImovelHasVisita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateTimeField()),
                ('observacoes', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('imovel', models.ForeignKey(to='core.Imovel')),
                ('visitante', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'imovel_has_visita',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImovelIndicadoGosto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gosto', models.ForeignKey(to='core.Gosto')),
                ('imovel', models.ForeignKey(to='core.Imovel')),
            ],
            options={
                'db_table': 'imovel_indicado_gosto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Intencao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, null=True, blank=True)),
                ('tipo', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'intencao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ItemIncluso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, null=True, blank=True)),
                ('tipo', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'item_incluso',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LugarProximo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=45, null=True, blank=True)),
                ('tipo', models.CharField(max_length=12, null=True, blank=True)),
            ],
            options={
                'db_table': 'lugar_proximo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=45, null=True, blank=True)),
                ('mensagem', models.TextField(max_length=45, null=True, blank=True)),
                ('enviada', models.DateTimeField(null=True, blank=True)),
                ('visualizada', models.DateTimeField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('de', models.ForeignKey(related_name='de', to=settings.AUTH_USER_MODEL)),
                ('para', models.ForeignKey(related_name='para', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'mensagem',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Midia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=255, null=True, blank=True)),
                ('tipo', models.CharField(max_length=6, null=True, blank=True)),
                ('imovel', models.ForeignKey(to='core.Imovel')),
            ],
            options={
                'db_table': 'midia',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CPF', models.CharField(max_length=11, null=True, blank=True)),
                ('whatsapp', models.CharField(max_length=15, null=True, blank=True)),
                ('facebook', models.CharField(max_length=100, null=True, blank=True)),
                ('data_nascimento', models.DateField(null=True, blank=True)),
                ('sexo', models.CharField(max_length=1, null=True, blank=True)),
                ('nacionalidade', models.CharField(max_length=50, null=True, blank=True)),
                ('alugo_procuro', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'perfil',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PerfilHasGostos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gosto', models.ForeignKey(to='core.Gosto')),
                ('perfil', models.ForeignKey(to='core.Perfil')),
            ],
            options={
                'db_table': 'perfil_has_gostos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, null=True, blank=True)),
                ('tipo', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'periodo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Regra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, null=True, blank=True)),
                ('tipo', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'regra',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField(null=True, blank=True)),
                ('ddd', models.IntegerField(null=True, blank=True)),
                ('tipo', models.CharField(max_length=50, null=True, blank=True)),
                ('operadora', models.CharField(max_length=50, null=True, blank=True)),
                ('perfil', models.ForeignKey(to='core.Perfil')),
            ],
            options={
                'db_table': 'telefone',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoImovel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, null=True, blank=True)),
                ('tipo', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'tipo_imovel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Valor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=45, null=True, blank=True)),
                ('tipo', models.CharField(max_length=12, null=True, blank=True)),
            ],
            options={
                'db_table': 'valor',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='imovelhasvalor',
            name='valor',
            field=models.ForeignKey(to='core.Valor'),
        ),
        migrations.AddField(
            model_name='imovelhasregra',
            name='regra',
            field=models.ForeignKey(to='core.Regra'),
        ),
        migrations.AddField(
            model_name='imovelhasperiodo',
            name='periodo',
            field=models.ForeignKey(to='core.Periodo'),
        ),
        migrations.AddField(
            model_name='imovelhaslugarproximo',
            name='lugar_proximo',
            field=models.ForeignKey(to='core.LugarProximo'),
        ),
        migrations.AddField(
            model_name='imovelhasitemincluso',
            name='item',
            field=models.ForeignKey(to='core.ItemIncluso'),
        ),
        migrations.AddField(
            model_name='imovel',
            name='tipo_imovel',
            field=models.ForeignKey(to='core.TipoImovel'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='perfil',
            field=models.ForeignKey(to='core.Perfil'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='imovel',
            field=models.ForeignKey(to='core.Imovel'),
        ),
    ]
