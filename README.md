# Django Search Application (With User accounts and Email OTP verification)

Steps to run the application:
1. Clone the repository to your local machine
2. Make sure Python version 3 is installed (Python 3.9.7 used for this project)
3. Make sure the latest version of Django is installed (Django 4.2.3 used for this project)
4. Install Postgresql and Pgadmin 4 for database connection, and create a database with name `worlddb` in Pgadmin 4.
5. Make the following changes in `helloworld/setting.py` file for your DB specifications:

   in `DATABASES`, change `USERNAME` and `PASSWORD` as per your Postgres account.
7. Also, chnage `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` in `settings.py` with the credentials of the account from which you want to send emails.
     To get `EMAIL_HOST_PASSWORD` of your Google account:
     1.  Go to "Manage your Account" > Security > 2-Step Verification > App Passwords
     2.  Generate a password with any App and Device
     3.  Copy the generated code into `EMAIL_HOST_PASSWORD` field in `settings.py` file.
8. Install module `psycopg2`, required for Postgres connection.

     $pip install psycopg2
   
8. Run the following commands in the terminal to create db models:

     $python manage.py makemigrations

     $python manage.py migrate
   This will create required tables in the database.
10. Execute following SQL files (in the same order as below, to refrain from getting Foreign key constraint violation) in your Postgres query window to insert Country, City and Language data:
     1. postgres_data/country.sql
     2. postgres_data/city.sql
     3. postgres_data/country_language.sql
        
11. Now you can run the application in localhost, create users and "Search The World".
12. $python manage.py runserver
13. Open the localhost URL (http://127.0.0.1:8000/) in your browser, it will open the Sign-Up window.
14. Once the User details are submitted, you will be redirected to the OPT verification page, where you have to enter the OTP you get on your Email id.
15. If the OTP is successfully verified, you will be redirected to the Search page, where you can search with keywords of any Country, City, or Language. You will get suggestions to select from as you type in the search bar.
16. Once selected, you will be redirected to the Country, City, or Language page depending upon your selection on the previous page.
17. Country page can be accessed from the City and Language page with the clickable links.
18. Search page will only be accessible once User is logged in after OTP verification, otherwise user will be redirected to the Login page.
19. User can Logout from any of the pages and will be redirected to the Sign-up/Login page.

    SignUp Page:
    <img width="957" alt="signup_page" src="https://github.com/sahilunagar/django_search_app/assets/36361441/e3babcc6-6966-4c17-a9d7-a2df1ba2ce22">

    Login Page:
    <img width="960" alt="login_page" src="https://github.com/sahilunagar/django_search_app/assets/36361441/7d5587ed-5ac9-496c-ab80-84a5c0fe94ca">

    Search Page:
    <img width="956" alt="search_page2" src="https://github.com/sahilunagar/django_search_app/assets/36361441/c50714fc-a173-40e9-be82-72d4977cac49">

    City Description Page:
    <img width="959" alt="city_description" src="https://github.com/sahilunagar/django_search_app/assets/36361441/87091af4-b724-44cf-a0e7-ec4f03ceae41">

    Language Description Page:
    <img width="956" alt="language description" src="https://github.com/sahilunagar/django_search_app/assets/36361441/3798903c-b819-4d5e-9ee2-f2b5f50f999a">

    Country Description Page:
    <img width="960" alt="country_description" src="https://github.com/sahilunagar/django_search_app/assets/36361441/a982577e-2404-4ecb-9a6b-fe714eeeecd4">






