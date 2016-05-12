# SLPAssist - Group Week - MVP (minimally viable product)
# MVP
•	Deploy to web
  o	Domain name
  o	Host site
•	SLP role
•	Database
•	Dashboard
  o	List of students
•	Student
•	Name
•	Single score
  o	Add student  - accessed on Dashboard
•	Student name
•	Initial score
  o	Edit score modal (triggered by button in student area)
# Stretch
•	SLP login
  o	Login page
  o	Token login (be specific if this is taken on)
•	Search student


    <li>[ ] License information</li>
      <ul>
        <li>[ ] Python: https://docs.python.org/3/license.html#psf-license-agreement-for-python-release</li>
        <li>[ ] psycopg2: http://initd.org/psycopg/license/</li>
        <li>[ ] bottle: http://bottlepy.org/docs/dev/index.html</li>
      </ul>
</ol>



## Running Python locally (for AJAX dev)
- `$ python3 mybottlecheck.py` (will start local instance of python webserver and tell you what URL to see this in chrome, _should_ be *0.0.0.0:5000*)
- All ajax calls should have a string value of just `/routename` which are listed [here](https://github.com/tiy-sat/SLPAssist/blob/master/mybottlecheck.py#L7) for example `/dashboard`

##To start off  make sure you go to use these sources:
- http://sass-lang.com/install
- http://browserify.org/#install
- https://github.com/substack/watchify make sure to run npm install

##links for http://slpassist-dev.herokuapp.com

http://slpassist-dev.herokuapp.com/login
http://slpassist-dev.herokuapp.com/dashboard
http://slpassist-dev.herokuapp.com/add-student
http://slpassist-dev.herokuapp.com/dashboard/settings
