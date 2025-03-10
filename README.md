Project Title:
"Django REST APIs for AI Chat"

Description:
This API manages user accounts with registration and login, facilitates token-based chat interactions with an external AI, and provides token balance checks.

Installation Instructions: These commands are for windows!! 
* Create a virtual environment (python -m venv .venv)
* Activate the virtual environment (.venv\scripts\activate)
* Install Django, Django rest framework and simplejwt (pip install django djangorestframework djangorestframework_simplejwt)
* install langchain_groq (pip install langchain_groq) ## langchain open source framework with model provider groq for AI  chat bot integration
* Install dotenv (pip install python-dotenv) # To load api key from .env
* Create a requirements.txt file with all the dependencies ( pip freeze > requirements.txt) 

Usage guidelines: These commands are for windows!! 
* Run migrations to save to the database (python manage.py makemigrations) and (python manage.py migrate)
* Create a super user to access django admin panel (python manage.py createsuperuser) 
* Get a groq api key for free form https://groq.com/ 
* Create a .env in your root directory and input your key ( export GROQ_API_KEY="your_api_key" )
* Run the development server (python manage.py runserver)
* Download an API tool. (i used Apidog desktop).
* Initiate a new request.
* To register a new user, paste the url path your_localhost/api/regiser(for me, http://127.0.0.1:8000/api/register/)
* ##"Check Output Result" Folder to see input format...
* To login a user, paste the url path your_localhost/api/regiser(for me http://127.0.0.1:8000/api/login/) 
##"Check Output Result " Folder to see input format...
* To send queries to the model, paste the url path your_localhost/api/regiser(for me http://127.0.0.1:8000/api/chat/)
* ##"Check Output Result" Folder to see input format...
* To get token balance, paste the url path your_localhost/api/regiser(for me http://127.0.0.1:8000/api/balance/) 
##"Check Output Result" Folder to see input format...


