# Generated by Django 3.0.5 on 2020-04-10 03:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(default=0, verbose_name='type')),
                ('agreement', models.BooleanField(default=False, verbose_name='agreement')),
                ('mail', models.CharField(default=None, max_length=256, null=True, verbose_name='mail')),
                ('name', models.CharField(default=None, max_length=256, null=True, unique=True, verbose_name='name')),
                ('description', models.CharField(default=None, max_length=256, null=True, verbose_name='description')),
                ('addr_sel', models.CharField(default=None, max_length=256, null=True, verbose_name='addr_sel')),
                ('addr', models.CharField(default=None, max_length=256, null=True, verbose_name='addr')),
                ('area_sel', models.CharField(default=None, max_length=256, null=True, verbose_name='area_sel')),
                ('takeaway', models.CharField(default=None, max_length=256, null=True, verbose_name='takeaway')),
                ('takeaway_menu', models.CharField(default=None, max_length=256, null=True, verbose_name='takeaway_menu')),
                ('takeaway_note', models.CharField(default=None, max_length=256, null=True, verbose_name='takeaway_note')),
                ('delivery_demaekan', models.BooleanField(default=False, verbose_name='delivery_demaekan')),
                ('delivery_ubereats', models.BooleanField(default=False, verbose_name='delivery_ubereats')),
                ('delivery_own', models.BooleanField(default=False, verbose_name='delivery_own')),
                ('delivery_other', models.BooleanField(default=False, verbose_name='delivery_other')),
                ('delivery_menu', models.CharField(default=None, max_length=256, null=True, verbose_name='delivery_menu')),
                ('delivery_note', models.CharField(default=None, max_length=256, null=True, verbose_name='delivery_note')),
                ('phone', models.CharField(default=None, max_length=256, null=True, verbose_name='phone')),
                ('opening_hours', models.CharField(default=None, max_length=256, null=True, verbose_name='opening_hours')),
                ('close_day', models.CharField(default=None, max_length=256, null=True, verbose_name='close_day')),
                ('payment_cash', models.BooleanField(default=False, verbose_name='payment_cash')),
                ('payment_card', models.BooleanField(default=False, verbose_name='payment_card')),
                ('payment_qr', models.BooleanField(default=False, verbose_name='payment_qr')),
                ('payment_emoney', models.BooleanField(default=False, verbose_name='payment_emoney')),
                ('payment_note', models.CharField(default=None, max_length=256, null=True, verbose_name='payment_note')),
                ('website', models.CharField(default=None, max_length=256, null=True, verbose_name='website')),
                ('twitter', models.CharField(default=None, max_length=256, null=True, verbose_name='twitter')),
                ('facebook', models.CharField(default=None, max_length=256, null=True, verbose_name='facebook')),
                ('instagram', models.CharField(default=None, max_length=256, null=True, verbose_name='instagram')),
                ('line', models.CharField(default=None, max_length=256, null=True, verbose_name='line')),
                ('sns_other', models.CharField(default=None, max_length=256, null=True, verbose_name='sns_other')),
                ('transportation', models.CharField(default=None, max_length=256, null=True, verbose_name='transportation')),
                ('diet_note', models.CharField(default=None, max_length=256, null=True, verbose_name='diet_note')),
                ('allergy_note', models.CharField(default=None, max_length=256, null=True, verbose_name='allergy_note')),
                ('latitude', models.FloatField(default=0.0, verbose_name='latitude')),
                ('longitude', models.FloatField(default=0.0, verbose_name='longitude')),
                ('covid19', models.CharField(default=None, max_length=256, null=True, verbose_name='covid19')),
                ('note', models.TextField(blank=True, default='', max_length=512, verbose_name='note')),
                ('expired_shop_date', models.DateTimeField(null=True)),
                ('closes_shop_date', models.DateTimeField(null=True)),
                ('soldout_takeaway_date', models.DateTimeField(null=True)),
                ('soldout_delivery_date', models.DateTimeField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('update_date', models.DateTimeField(blank=True, null=True, verbose_name='修正日')),
            ],
            options={
                'verbose_name': '店',
                'verbose_name_plural': '店',
            },
        ),
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_data', models.ImageField(blank=True, default='/static/brownbags/images/none.png', null=True, upload_to='images/', verbose_name='画像')),
                ('image_data_class', models.IntegerField(choices=[(0, 'その他'), (1, '店舗'), (2, 'テイクアウト'), (3, 'デリバリー'), (-1, '---')], default=-1, verbose_name='区分')),
                ('expired_date', models.DateTimeField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='brownbags.Shop', verbose_name='Shop')),
            ],
            options={
                'verbose_name': '画像',
                'verbose_name_plural': '画像',
            },
        ),
    ]
