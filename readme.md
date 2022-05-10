The flask performs the following functions, performs the following functions:
- the service receives requests, in turn, requests from the public API 
(English-language quiz questions);
- the received questions are saved in the database;
- the following fields are saved; ID, answer, questions, creation date.
***
#How to launch?
- Create the root folder of the project and place the source code
- In the docker-compose file, add your database: 
  DATABASE_URL=postgresql+psycopg2://postgres:your password@db:5432/your database
- In the terminal, go to the project folder and type the command:
  [docker-compose build], after the container is assembled, run it 
  [docker-compose up]
-  Execute the request using the postman.
![Request example!](/images/postman.png)
