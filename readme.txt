***********Hello! This is a inpatientsystem from Lan****************
-----------------------------------------------------------------------------------------
-------------------------------------INSTRUCTION-----------------------------------------
-----------------------------------------------------------------------------------------
This is a inpatientsystem of Puget hospital, which helps medical institutions and medical
professionals better manage inpatient patients and their surgeries.

In this system, The patient is hospitalized by a doctor from the corresponding department,
occupies a bed in the corresponding department, and may be scheduled for operation. 

The system provides bed and operating room information for inquiry, use and reservation. 
And the system also provides some statistical information, like the bed occupancy and 
operating room occupancy.

The operating rooms are divided into three levels: A, B, and C, which correspond to the 
time period they can be open. Level C operating rooms are open for 8 hours a day and are 
closed on weekends, level B operating rooms are open for 12 hours everyday. level A 
operating rooms are available 24 hours everyday.

-----------------------------------------------------------------------------------------
----------------------------------FOR DOCTOR USER----------------------------------------
-----------------------------------------------------------------------------------------
If you are a doctor, please bring your work identification to the department office for 
account registration. 
Alternatively, you can register by sending an email to the IT department, and please 
include your work identification in the email.

Details to use:
After Logging In:

Dashboard:
Access your personalized dashboard by clicking on Dashboard. Stay updated on key metrics 
and activities.

Add Patient:
Easily add new patient records to the system. Navigate to Add Patient and fill in the 
required information.

My Patients:
View and manage your patients efficiently. Click My Patients to see a comprehensive list 
of your assigned patients. 
You can also search the patients by theirs names and discharge your patients.

My Operation:
Stay organized with your surgical operations. Access My Operation to manage and track 
your scheduled operations.

Add Operation:
Schedule new operations seamlessly. Visit Add Operation to input details and coordinate 
upcoming procedures.

Operating Room Booking:
Reserve operating rooms for your procedures. Plan your surgeries by visiting Operating 
Room Booking.
Note: Scheduled time must be on the whole hour.
      Respect the open times of each class of Operating Rooms.

My Booking Room:
Keep track of your reserved operating rooms. Click My Booking Room to view and manage 
your bookings.

Logout:
Logout securely from your account. Access Logout to end your session.


TRY WEBSITE AS DOCTOR:
https://lena.pythonanywhere.com/
(DOCTOR LOGIN: username: go123 password: go123)
-----------------------------------------------------------------------------------------
--------------------------INSTRUCTION FOR LOCAL RUN--------------------------------------
-----------------------------------------------------------------------------------------

After you finish downloading the project, unzip the project file and head over to the 
project root folder.
You can also create a Virtual Environment and Activate it.
Open your Terminal/Command Prompt on the project’s root folder.
Install the Requirements: pip install -r requirements.txt.
Then, make database migrations: python manage.py makemigrations
python manage.py migrate
And finally, after a successful migration run the application: 	python manage.py 
runserver
At last, open up your favorite web browser
Go to URL “http://127.0.0.1/[ PORT_NUMBER ]/”
For the Admin Panel credentials, you have to create one with a superuser by using: 
python manage.py createsuperuser
For simple test, use username: go123   password: go123
-----------------------------------------------------------------------------------------
-------------------------------------COPYRIGHT-------------------------------------------
-----------------------------------------------------------------------------------------
Calendar: from kaizhelam   https://github.com/kaizhelam/Calendar
Icon: from                 https://fontawesome.com/
-----------------------------------------------------------------------------------------
-------------------------------------CONTACT---------------------------------------------
-----------------------------------------------------------------------------------------
Email address: jaulinexdu@gmail.com

