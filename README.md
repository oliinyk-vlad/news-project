News Project
=======================
Simple news board API.

CRUD API for managing news posts and comments. Created endpoint for upvoting posts. At midnight, upvotes are reset to zero by celery task. 
#### Launching
Run the following commands:

```
git clone https://github.com/oliinyk-vlad/news-project.git
cd news-project
docker-compose up --build -d
docker-compose up
```





#### Info

Postman collection [json](https://www.getpostman.com/collections/bc1c7fd05f05cbe266d8)

Project deployed at heroku 

[super-news-app.herokuapp.com](https://super-news-app.herokuapp.com)
