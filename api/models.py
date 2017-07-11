# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Address(models.Model):
    address_id = models.CharField(primary_key=True, max_length=240)
    address_line_1 = models.CharField(max_length=240)
    address_line_2 = models.CharField(max_length=240)
    zip_code = models.CharField(max_length=240)
    billing = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'address'


class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=240)
    organization_business = models.ForeignKey('OrganizationUnit', models.DO_NOTHING)
    name = models.CharField(max_length=240)
    gender = models.CharField(max_length=240)

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerAddress(models.Model):
    id = models.CharField(primary_key=True, max_length=240)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    address = models.ForeignKey(Address, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'customer_address'


class OrganizationUnit(models.Model):
    organization_business_id = models.CharField(primary_key=True, max_length=240)
    name = models.CharField(max_length=240)
    description = models.CharField(max_length=240)

    class Meta:
        managed = False
        db_table = 'organization_unit'


class Service(models.Model):
    service_id = models.CharField(primary_key=True, max_length=240)
    service_type = models.ForeignKey('ServiceType', models.DO_NOTHING)
    provider = models.ForeignKey(OrganizationUnit, models.DO_NOTHING)
    description = models.CharField(max_length=240)

    class Meta:
        managed = False
        db_table = 'service'


class ServiceLocation(models.Model):
    id = models.CharField(primary_key=True, max_length=240)
    service = models.ForeignKey(Service, models.DO_NOTHING)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_location'


class ServiceType(models.Model):
    id = models.CharField(primary_key=True, max_length=240)
    description = models.CharField(max_length=240)

    class Meta:
        managed = False
        db_table = 'service_type'
