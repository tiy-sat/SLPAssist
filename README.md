# SPLAssist - Group Week - MVP (minimally viable product)
<ol>
  <li>database to store values</li>
  <li>front page when logged in</li>
  <li>login page</li>
  <li>front page when not logged in</li>
  <li>dashboard</li>
    <ul>
      <li>list of students</li>
      <li>student info</li>
        <ol>
          <li>name</li>
          <li>graph</li>
          <li>action</li>
        </ol>
    </ul>    
      <li>user settings page</li>
    <ul>
  <li>role SLP</li>
    </ul>
  <li>notification for SLP login process</li>
  <li>student details</li>
    <ul>
      <li>capturing student data</li>
      <li>graduate student</li>
    </ul>
  <li>action from all pages: logout</li>
  <li>github repository</li>
  <li>deploy to web</li>
    <ul>
      <li>domain name</li>
      <li>host</li>
    </ul>
</ol>

# SPLAssist
Repository for SPLA web app

##To start off  make sure you go to use these sources:
- http://sass-lang.com/install
- http://browserify.org/#install
- https://github.com/substack/watchify make sure to run npm install

# Heroku Setup

## Get credentials

## Login to Heroku

`$ heroku login`

## Create an instance

Only need to do this once:

```
heroku create slpassist-dev
```

## Deploy

```
$ git push heroku master
```
