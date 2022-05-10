This application written with flask performs the following functions:
- the service receives requests from the public API https://jservice.io/api/random?count=1 , (quiz questions in English);
- the received questions are saved in the database;
- the following fields are saved; ID, answer, questions, creation date.
***
# How to launch? #
- Create the root folder of the project and place the source code
- In the docker-compose file, add your database: 
  DATABASE_URL=postgresql+psycopg2://postgres:your password@db:5432/your database
- In the terminal, go to the project folder and type the command:
  __docker-compose build__, after the container is assembled, run it 
  __docker-compose up__
-  Execute the request using the postman.
![Request example!](/images/postman.png)
