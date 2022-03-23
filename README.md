IGS Manager
====================

IGS Manager is a backend service responsible for Employee CRUD's

## Running with Docker

* Install Docker and Docker Compose

- Clone the project and access the IGSManager folder to start the service with the commands below

* IMPORTANT To create the environment variables, run the command "make config-env" and the .env file will be created in the root folder. "env.exemple" is a sample file in contrib folder
```
$ make config-env
```

* Run the following make command "$ make build" to build the image
```
$ make build
```

* To build and run the project run the command "$ make up"
```
$ make up
```

* After the command '$ make up' 
 - You can access swagger on http://127.0.0.1:8000
 - You can access redoc on http://127.0.0.1:8000/redoc/
 - You can access PGAdmin go to: http://localhost:5050 
 - user = admin@igs.com.br password = admin

* If you want to load initial data such as admin user and department and employee data: run the command: '$ make demo'
 - You can access http://127.0.0.1:8000/admin with
 - user = admin password = admin
```
$ make demo
```

* To create a superuser run the command: "$ make createsuperuser"
```
$ make createsuperuser
```

* Run Tests with the command "$ make tests":
```
$ make tests
```

* Run Flake8 with the command "$ make flake8"
```
$ make flake8
```

* Run the linter with the command "$ make pylint"
```
$ make pylint
```

* Run the code pytest - coverage with the command "$ make tests-cov"
```
$ make tests-cov
```

* Run the command "$ make down" to stop the containers
```
$ make down
```