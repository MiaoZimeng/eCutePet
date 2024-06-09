# Generated by Django 4.2.13 on 2024-06-09 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_doctorinfo_id_number_and_more'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscomment',
            name='content',
            field=models.CharField(help_text='评论内容', max_length=300, verbose_name='评论内容'),
        ),
        migrations.AlterField(
            model_name='goodscomment',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='goodscomment',
            name='good',
            field=models.ForeignKey(help_text='商品', on_delete=django.db.models.deletion.CASCADE, to='shop.goodsinfo', verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='goodscomment',
            name='modify_time',
            field=models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='goodscomment',
            name='user',
            field=models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to='users.userinfo', verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='category',
            field=models.IntegerField(choices=[(1, '宠物食品'), (2, '宠物药品'), (3, '宠物玩具')], help_text='商品分类', verbose_name='商品分类'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='click_num',
            field=models.IntegerField(default=0, help_text='点击数', verbose_name='点击数'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='comment_count',
            field=models.PositiveIntegerField(default=0, help_text='评论数', verbose_name='评论数'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='favor_count',
            field=models.PositiveIntegerField(default=0, help_text='赞数', verbose_name='赞数'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='id',
            field=models.AutoField(help_text='商品ID', primary_key=True, serialize=False, verbose_name='商品ID'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='image_url',
            field=models.ImageField(blank=True, help_text='商品封面url', max_length=200, null=True, upload_to='image/shop', verbose_name='商品封面url'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='modify_time',
            field=models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='售价', max_digits=10, verbose_name='售价'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='sold_num',
            field=models.PositiveIntegerField(default=0, help_text='销量', verbose_name='销量'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='text',
            field=models.TextField(help_text='商品介绍', verbose_name='商品介绍'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='title',
            field=models.CharField(help_text='商品标题', max_length=255, verbose_name='商品标题'),
        ),
    ]
