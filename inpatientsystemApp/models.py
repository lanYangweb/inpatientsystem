# models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils import timezone


class Department(models.Model):
    id_department = models.AutoField(primary_key=True)
    name_department = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name_department

class Patient(models.Model):
    id_patient = models.AutoField(primary_key=True, verbose_name="Patient ID")
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    id_bed = models.ForeignKey('Bed', on_delete=models.SET_NULL, null=True)
    id_doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True)
    id_department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    patient_department = models.CharField(max_length=50)
    gender_patient = models.CharField(max_length=10)

    @property
    def get_patient_department(self):
        # 获取关联的 Department 的 name_department
        if self.id_department:
            return self.id_department.name_department
        return None

    def save(self, *args, **kwargs):
        # 在保存时填充 patient_department
        self.patient_department = self.get_patient_department
        super().save(*args, **kwargs)

    # @receiver(post_delete, sender=Patient)
    # def patient_deleted(sender, instance, **kwargs):
    #     # 获取病人关联的床位
    #     bed = instance.id_bed
    #
    #     if bed:
    #         # 在病人删除时将床位的 id_patient 字段设置为 NULL
    #         bed.id_patient = None
    #         bed.save()
    def __str__(self):
        return f"Patient {self.id_patient} - {self.first_name} - {self.last_name}"


class Doctor(models.Model):
    id_doctor = models.AutoField(primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_department = models.ForeignKey(Department, on_delete=models.CASCADE, to_field='name_department')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True)
    description_doctor = models.TextField()
    profile_pic = models.ImageField(upload_to='doctor_profile_pic/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor', null=True, blank=True)
    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.name_department}'
class Bed(models.Model):
    id_bed = models.AutoField(primary_key=True, verbose_name="Bed ID")
    id_patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    id_department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    bed_department = models.CharField(max_length=50)

    def __str__(self):
        return f"Bed {self.id_bed} - {self.bed_department}"


class Operation(models.Model):
    id_operation = models.AutoField(primary_key=True, verbose_name="Operation ID")
    id_operating_room = models.ForeignKey('OperatingRoom', on_delete=models.CASCADE)
    id_patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    id_doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True)
    name_operation = models.CharField(max_length=50)  
    date_of_operation = models.DateField()

    def get_patient_name(self):
        return f"{self.id_patient.first_name} - {self.id_patient.last_name}"

    def get_doctor_name(self):
        return f"{self.id_doctor.first_name} - {self.id_doctor.last_name}"
    def __str__(self):
        return f"Operation {self.id_operation} - {self.id_operating_room} - {self.date_of_operation}"

class OperatingRoom(models.Model):  
    id_operating_room = models.AutoField(primary_key=True, verbose_name="OperatingRoom ID")
    class_operating_room = models.CharField(max_length=50)
    def __str__(self):
        return f"OperatingRoom {self.id_operating_room} - {self.class_operating_room}"




class OperatingRoomSchedule(models.Model):
    id_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    id_operating_room = models.ForeignKey(OperatingRoom, on_delete=models.CASCADE)
    class_operating_room = models.CharField(max_length=50)
    scheduled_time = models.DateTimeField()
    finish_time = models.DateTimeField()

    constraints = [
        models.CheckConstraint(
            check=(
                    models.Q(id_operating_room__class_operating_room='C',
                             scheduled_time__iso_week_day__in=[1, 2, 3, 4, 5],
                             scheduled_time__hour__gte=8,
                             scheduled_time__hour__lt=16,
                             finish_time__hour__lte=16) |
                    models.Q(id_operating_room__class_operating_room='B',
                             scheduled_time__hour__gte=8,
                             finish_time__hour__lte=20) |
                    models.Q(id_operating_room__class_operating_room='A',
                             scheduled_time__hour__gte=0,
                             finish_time__hour__lte=24)
            ),
            name='valid_scheduling_time'
        )
    ]

    def is_expired(self):
        return self.finish_time < timezone.now()

    def release_operating_room(self):
        # Your logic for releasing the operating room goes here
        pass



