from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from inpatientsystemApp.models import Department, Patient, Doctor, Bed, Operation, OperatingRoom, OperatingRoomSchedule
from django.contrib.auth.forms import UserCreationForm
#login admin/doctor
# ---------------------------------------------------------------------------------
# -------------------------------LOGIN AND USER FORMS -----------------------------
# ---------------------------------------------------------------------------------
class admin_login_Form(forms.Form):
    username = forms.CharField(max_length=63, label='Username')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Password')

class doctor_login_Form(forms.Form):
    username = forms.CharField(max_length=63, label='Username')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Password')


# for admin signup

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']
        widgets = {
            'password': forms.PasswordInput()
        }

class SuperuserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'is_staff', 'is_superuser')

# class DoctorUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'username', 'password']
#         widgets = {
#             'password': forms.PasswordInput()
#         }
# ---------------------------------------------------------------------------------
# -------------------------------DATABASE FORMS -----------------------------------
# ---------------------------------------------------------------------------------
class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ['name_department', 'first_name', 'last_name', 'description_doctor']

# for patient related form
# for patient related form
class PatientForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender_patient = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Dynamically set the choices for 'id_bed' based on availability
        available_beds = Bed.objects.filter(id_patient__isnull=True)
        self.fields['id_bed'].queryset = available_beds
    class Meta:
        model = Patient
        fields = ['id_bed', 'id_doctor', 'id_department', 'first_name', 'last_name', 'date_of_birth',
                  'gender_patient']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name_department']
# for bed related form
class BedForm(forms.ModelForm):
    class Meta:
        model = Bed
        fields = ['id_patient', 'id_department', 'bed_department']

# for operation related form
class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['id_operating_room', 'id_patient', 'id_doctor',  'name_operation', 'date_of_operation']

        widgets = {
            'date_of_operation': forms.DateInput(attrs={'type': 'date'}),
            # Add any additional customization for the date_of_operation field here
        }

# for operating room related form
class OperatingRoomForm(forms.ModelForm):
    class Meta:
        model = OperatingRoom
        fields = ['class_operating_room']

# for operating room schedule related form
class OperatingRoomScheduleForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        scheduled_time = cleaned_data.get('scheduled_time')
        finish_time = cleaned_data.get('finish_time')

        if scheduled_time and finish_time and finish_time < scheduled_time:
            raise forms.ValidationError("Finish time cannot be earlier than scheduled time.")

        self.confirm_no_overlap(scheduled_time, finish_time)


    def confirm_no_overlap(self, scheduled_time, finish_time):
        overlapping_schedules = OperatingRoomSchedule.objects.filter(
            finish_time__gt=scheduled_time,
            scheduled_time__lt=finish_time
        )

        if overlapping_schedules.exists():
            raise forms.ValidationError(
                "The selected time overlaps with an existing schedule. Please choose a different time.")
        # overlapping_schedules = OperatingRoomSchedule.objects.filter(
        #     finish_time__gt=scheduled_time,
        #     scheduled_time__lt=finish_time
        # )

        # if overlapping_schedules.exists():
        #     raise forms.ValidationError(
        #         "The selected time overlaps with an existing schedule. Please choose a different time.")

    class Meta:
        model = OperatingRoomSchedule
        fields = ['id_doctor', 'id_operating_room', 'scheduled_time', 'finish_time']

        widgets = {
            'scheduled_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'min': timezone.now().isoformat(), 'step': '3600'}),
            'finish_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'min': timezone.now().isoformat(), 'step': '3600',
                       'onchange': 'validateFinishTime()'}),
        }


# for operation performing related form


# for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

# class DoctorSignupForm(UserCreationForm):
#     name_department = forms.CharField(max_length=50, required=True)
#     description_doctor = forms.CharField(required=True, widget=forms.Textarea)
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.save()
    #     doctor = Doctor.objects.create(
    #         user=user,
    #         name_department=self.cleaned_data['name_department'],
    #         first_name=self.cleaned_data['first_name'],
    #         last_name=self.cleaned_data['last_name'],
    #         description_doctor=self.cleaned_data['description_doctor']
    #     )
    #     return user