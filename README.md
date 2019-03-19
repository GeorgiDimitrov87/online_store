The project is still not working properly and needs a lot of debugging.
I am using SQL Alchemy with SQLite to save time, but it could easily be changed to another database.
There JWT security tokenisation and in order to GET or POST the user must be loged in.
Make sure you have python 3.5 or above.
1.Make virtual environment in which to run the app. Open the terminal and navigate to the folder in which you want to have the the app.Choose a name and type: virtualenv <name>
2.Activate the virtual environmment. Type source <name>/bin/activate
3. Install the dependancies:
  pip install Flask
  pip install Flask-JWT-Extended
  pip install Flask-RESTful
  pip install Flask-SQLAlchemy
  
4. Navigate to the folder if not there already  and type  python app.py to run the server.
5.The app can be tested with Postman.

GET all stores http://127.0.0.1:5000/stores

GET store name http://127.0.0.1:5000/store/<name>
  
POST store  http://127.0.0.1:5000/store/<name>
  
DELETE store  http://127.0.0.1:5000/store/<name>
  
GET all items http://127.0.0.1:5000/items

GET specific item http://127.0.0.1:5000/item/<name>
  
POST  item http://127.0.0.1:5000/item/<name>
  
UPDATE  item http://127.0.0.1:5000/item/<name>
  
DELETE  item http://127.0.0.1:5000/item/<name>
  
Authorisation POST  http://127.0.0.1:5000/auth

Register      POST  http://127.0.0.1:5000/register
   
After finishing the app the next step is to add My SQL database(for example)with the english_shops.json data.
Putting the app in a Docker container and writing some Unit testing 

  




