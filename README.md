# StartupFairy
IMD 4

[Apiary Docs](http://docs.startupfairy.apiary.io/)
[Travis](https://travis-ci.org/cs373gc-fall-2016/Startup-Fairy)

### Setup 
You'll need
- [Docker](https://docs.docker.com/engine/installation/mac/)
- [Docker-compose](https://docs.docker.com/compose/install/)

Run `docker-compose up -d`. 

If you need to set up a password for postgres, make sure you `export POSTGRES_PASSWORD=<your password>`.


### Development
You'll see the app at `localhost`. There is parity between the content on your local machine and the content inside the docker container.

If you shut down your computer/Docker machine, the next time you boot up docker, you will need to run `docker-compose start` in order to start up all the services (postgres and app) again.

### Deployment

Same steps as development.

### Models
* Company
  * Name
  * Summary
  * Employees
  * City
  * Investors
  * Twitter
  * Website
  
* Financial Org
  * Name
  * Summary
  * City
  * Companies invested in
  * Twitter
  * Website
 
* People
  * Name
  * Bio
  * City
  * Company
  * Role
  * Twitter
 
* City
  * Name
  * State
  * Country 
  * Companies
  * Financial Orgs
  * People

### UML Diagram

http://yuml.me/83988bfb
   
  
