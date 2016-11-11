# StartupFairy
IMD 4

[Apiary Docs](http://docs.startupfairy.apiary.io/)
[Travis](https://travis-ci.org/cs373gc-fall-2016/Startup-Fairy)

### Setup 
You'll need
- [Docker](https://docs.docker.com/engine/installation/mac/)
- [Docker-compose](https://docs.docker.com/compose/install/)

1. Run `docker-compose up -d`. 
2. Do `docker-compose ps` to see all your availble containers and the status of them.
3. Once `startupfairy` the app is up and running, run `docker exec -it startupfairy bash`. You'll be inside the `startupfairy` container.
4. Run `bower install --allow-root`

You will only need to do steps 3 & 4 if you are creating the containers for the first time or if you're missing the `app/static/bower_components` directory.

If you need to set up a password for postgres, make sure you `export POSTGRES_PASSWORD=<your password>` and `export POSTGRES_USER=<your username>`.

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

http://yuml.me/96b7f61e
   
  
