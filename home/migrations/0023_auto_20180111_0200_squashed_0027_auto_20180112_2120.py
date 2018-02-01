# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-16 18:17
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20171219_2252_squashed_0065_auto_20180110_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='longevity',
            field=models.CharField(choices=[('3M', '0-3 months'), ('6M', '3-6 months'), ('1Y', '6-12 months'), ('2Y', '1-2 years'), ('OL', 'More than 2 years')], default='3M', help_text='How long has the project accepted publicly submitted contributions?', max_length=2),
        ),
        migrations.AddField(
            model_name='project',
            name='no_proprietary_software',
            field=models.BooleanField(default=False, help_text='I assert that this Outreachy internship project will forward the interests of free and open source software, not proprietary software.'),
        ),
        migrations.AddField(
            model_name='project',
            name='proprietary_software_description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='(Optional) If this internship project furthers the interests of proprietary software, please explain.'),
        ),
        migrations.AddField(
            model_name='project',
            name='unapproved_license_description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='(Optional) If this Outreachy internship project will be released under a license that is not an OSI-approved and FSF-approved license OR a Creative Commons license, please provide a description and links to the non-free licenses.'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='approved_license',
            field=models.BooleanField(help_text='I assert that all Outreachy internship projects under my community will be released under either an <a href="https://opensource.org/licenses/alphabetical">OSI-approved open source license</a> that is also identified by the FSF as a <a href="https://www.gnu.org/licenses/license-list.html">free software license</a>, OR a <a href="https://creativecommons.org/share-your-work/public-domain/freeworks/">Creative Commons license approved for free cultural works</a>'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='no_proprietary_software',
            field=models.BooleanField(help_text='I assert all Outreachy internship projects under my community will forward the interests of free and open source software, not proprietary software.'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='proprietary_software_description',
            field=models.CharField(blank=True, help_text='(Optional) If any internship project under your community furthers the interests of proprietary software, please explain.', max_length=3000),
        ),
        migrations.AlterField(
            model_name='participation',
            name='cfp_text',
            field=models.CharField(max_length=3000, verbose_name="Additional information to provide on a call for mentors and volunteers page (e.g. what kinds of internship projects you're looking for, ways for volunteers to help Outreachy applicants)"),
        ),
        migrations.AlterField(
            model_name='project',
            name='approved_license',
            field=models.BooleanField(help_text='I assert that Outreachy internship projects will released under either an <a href="https://opensource.org/licenses/alphabetical">OSI-approved open source license</a> that is also identified by the FSF as a <a href="https://www.gnu.org/licenses/license-list.html">free software license</a>, OR a <a href="https://creativecommons.org/share-your-work/public-domain/freeworks/">Creative Commons license approved for free cultural works</a>'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='approved_license',
            field=models.BooleanField(default=False, help_text='I assert that all Outreachy internship projects under my community will be released under either an <a href="https://opensource.org/licenses/alphabetical">OSI-approved open source license</a> that is also identified by the FSF as a <a href="https://www.gnu.org/licenses/license-list.html">free software license</a>, OR a <a href="https://creativecommons.org/share-your-work/public-domain/freeworks/">Creative Commons license approved for free cultural works</a>'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='proprietary_software_description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='(Optional) If any internship project under your community furthers the interests of proprietary software, please explain.'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='unapproved_license_description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='(Optional) If your community uses a license that is not an OSI-approved and FSF-approved license OR a Creative Commons license, please provide a description and links to the non-free licenses.'),
        ),
        migrations.AlterField(
            model_name='project',
            name='approved_license',
            field=models.BooleanField(default=False, help_text='I assert that this Outreachy internship projects will released under either an <a href="https://opensource.org/licenses/alphabetical">OSI-approved open source license</a> that is also identified by the FSF as a <a href="https://www.gnu.org/licenses/license-list.html">free software license</a>, OR a <a href="https://creativecommons.org/share-your-work/public-domain/freeworks/">Creative Commons license approved for free cultural works</a>'),
        ),
        migrations.AlterField(
            model_name='mentorapproval',
            name='longevity',
            field=models.CharField(choices=[('3M', '0-2 months'), ('6M', '3-5 months'), ('1Y', '6-11 months'), ('2Y', '1-2 years'), ('OL', 'More than 2 years')], default='3M', help_text='How long have you been contributing to this project?', max_length=2),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='community_size',
            field=models.CharField(choices=[('3', '1-2 people'), ('5', '3-5 people'), ('10', '6-10 people'), ('20', '11-20 people'), ('50', '21-50 people'), ('100', '50-100 people'), ('999', 'More than 100 people')], default='3', help_text='How many people are contributing to this community regularly?', max_length=3),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='longevity',
            field=models.CharField(choices=[('3M', '0-2 months'), ('6M', '3-5 months'), ('1Y', '6-11 months'), ('2Y', '1-2 years'), ('OL', 'More than 2 years')], default='3M', help_text='How long has the community been a free and open source software (FOSS) community?', max_length=2),
        ),
        migrations.AlterField(
            model_name='project',
            name='community_size',
            field=models.CharField(choices=[('3', '1-2 people'), ('5', '3-5 people'), ('10', '6-10 people'), ('20', '11-20 people'), ('50', '21-50 people'), ('100', '50-100 people'), ('999', 'More than 100 people')], default='3', help_text='How many people are contributing to this project regularly?', max_length=3),
        ),
        migrations.AddField(
            model_name='coordinatorapproval',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('W', 'Withdrawn'), ('R', 'Rejected'), ('A', 'Approved')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='coordinatorapproval',
            name='reason_denied',
            field=models.CharField(blank=True, help_text='\n            Please explain why you are withdrawing this request. This\n            explanation will only be shown to Outreachy organizers and\n            approved people within this community.\n            ', max_length=3000),
        ),
        migrations.AddField(
            model_name='mentorapproval',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('W', 'Withdrawn'), ('R', 'Rejected'), ('A', 'Approved')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='mentorapproval',
            name='reason_denied',
            field=models.CharField(blank=True, help_text='\n            Please explain why you are withdrawing this request. This\n            explanation will only be shown to Outreachy organizers and\n            approved people within this community.\n            ', max_length=3000),
        ),
        migrations.AddField(
            model_name='participation',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('W', 'Withdrawn'), ('R', 'Rejected'), ('A', 'Approved')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='participation',
            name='reason_denied',
            field=models.CharField(blank=True, help_text='\n            Please explain why you are withdrawing this request. This\n            explanation will only be shown to Outreachy organizers and\n            approved people within this community.\n            ', max_length=3000),
        ),
        migrations.AddField(
            model_name='project',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('W', 'Withdrawn'), ('R', 'Rejected'), ('A', 'Approved')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='project',
            name='reason_denied',
            field=models.CharField(blank=True, help_text='\n            Please explain why you are withdrawing this request. This\n            explanation will only be shown to Outreachy organizers and\n            approved people within this community.\n            ', max_length=3000),
        ),
    ]
