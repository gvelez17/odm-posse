# Generated by Django 2.1.1 on 2018-09-26 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adfacts', '0002_auto_20180924_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='last_name',
        ),
        migrations.AddField(
            model_name='donor',
            name='donor_type',
            field=models.CharField(blank=True, choices=[('individual', 'Individual'), ('business', 'For profit business'), ('501c4', '501c4'), ('PAC', 'PAC'), ('other', 'Other')], max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='country',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='email',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='full_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='state',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='zip',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='org',
            name='donors',
            field=models.ManyToManyField(blank=True, null=True, to='adfacts.Donor'),
        ),
    ]
