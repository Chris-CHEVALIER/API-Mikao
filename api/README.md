`curl -H 'Accept: application/json; indent=4' -u admin:bof... http://127.0.0.1:8000/users/`

####Run server :

`python3 manage.py runserver`

####Migrations :

`python3 manage.py makemigrations mikao`
`python3 manage.py migrate`

####Liens utiles :

http://127.0.0.1:8000/api/
http://127.0.0.1:8000/api/admin/
http://127.0.0.1:8000/api/docs/ -> `Swagger`

####Token client side (React) :

`localStorage.set('accessToken', "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0MzQ4MTYwLCJqdGkiOiI0MzA2YmQwYTcxZDg0ZDU5OTExMmZmMjk5YWZmZGM2YSIsInVzZXJfaWQiOjF9.SKBN-paWolAKs2-qLYMGa0sirIyBWRJumS80s_nE7Kc");`

`localStorage.set('refreshToken', "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU3NDQzNDI2MCwianRpIjoiYTFmOTk0NWQ3MWQxNDVhYjlhOWVjOTJkZDAyMTExZTAiLCJ1c2VyX2lkIjoxfQ.5vrgeREEkmx4wHUnx5Bsh4u1sNGoVVds23Wdo2RwjwA")`

`localStorage.get('accessToken')`

`localStorage.get('refreshToken')`