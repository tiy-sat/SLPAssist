# SLPAssist - Group Week - MVP (minimally viable product)
# MVP
<ul>
  <li>Deploy to web</li>
    <ul>
      <li>Domain name</li>
      <li>Host site</li>
    </ul>
  <li>SLP role</li>
  <li>Database</li>
  <li>Dashboard</li>
    <ul>
      <li>List of students</li>
    </ul>
  <li>Student</li>
  <li>Name</li>
  <li>Single score</li>
    <ul>
      <li>Add student  - accessed on Dashboard</li>
    </ul>
  <li>Student name</li>
  <li>Initial score</li>
    <ul>
      <li>Edit score modal - triggered by button in student area</li>
    </ul>
</ul>
# Stretch
<ul>
  <li>SLP login</li>
    <ul>
      <li>Login page</li>
      <li>Token login (be specific if this is taken on)</li>
    </ul>
  <li>Search student</li>
</ul>

<ul>
  <li>[ ] License information</li>
    <ul>
      <li>[ ] Python: https://docs.python.org/3/license.html#psf-license-agreement-for-python-release</li>
      <li>[ ] psycopg2: http://initd.org/psycopg/license/</li>
      <li>[ ] bottle: http://bottlepy.org/docs/dev/index.html</li>
    </ul>
</ul>



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
