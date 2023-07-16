# Django Search Application (With User accounts and Email OTP verification)

Steps to run the application:
1. Clone the repository to your local machine
2. Make sure Python version 3 is installed (Python 3.9.7 used for this project)
3. Make sure the latest version of Django is installed (Django 4.2.3 used for this project)
4. Install Postgresql and Pgadmin 4 for database connection, and create a database with name `worlddb' in Pgadmin 4.
5. Make following changes in `helloworld/setting.py` file for your db specifications:
     in `DATABASES`, change `USERNAME` and `PASSWORD` as per your Postgres account.
6. Also, chnage `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` with the credentials of the account from which you want to send mails.
     To get `EMAIL_HOST_PASSWORD` of your google account:
     1.  Go to "Manage your Account" > Security > 2-Step Verificatiob > App Passwords
     2.  Generate password with any App and Device
     3.  Copy the generated code into `EMAIL_HOST_PASSWORD` field in `settings.py` file.
7. Run the following commands in terminal to create db models:
     $python manage.py makemigrations
     $python manage.py migrate
   This will create required tables in the database.
8. Execute following SQL files in your Postgres query window to insert Country, City and Language data:
     1. SQL/country.sql
     2. SQL/city.sql
     3. SQL/country_language.sql
        
9. Now you can run the application in localhost, create users and "Search The World".
10. $python manage.py runserver
11. Open the localhost URL (http://127.0.0.1:8000/) in your browser, it will open the Sign-Up window.
12. Once the User details are submitted, you will be redirected to the OPT verification page, where you have to enter the OTP you get on your Email id.
13. If the OTP is successfully verified, you will be redirected to the Search page, where you can search with keywords of any Country, City, or Language. You will get suggestions to select from as you type in the search bar.
14. Once selected, you will be redirected to the Country, City, or Language page depending upon your selection on the previous page.
15. Country page can be accessed from the City and Language page with the clickable links.
16. Search page will only be accessible once User is logged in after OTP verification, otherwise user will be redirected to the Login page.
17. User can Logout from any of the pages and will be redirected to the Sign-up/Login page.
    
