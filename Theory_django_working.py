#In "Django_ToDo" project folder has,
#"todo" --> App or Application
#"Templates" --> To store images
#"toDo_main" it contains 'manage.py' file also --> DjangoProject folder
#" " --> external static files
#"db.sqlite3" --> built-in database
#"Theory_django_working.py" --> Theory of Django


#0) Advanced Django
#Building some more complex project like "ToDo app" project
#create an new folder "Django_ToDo", and check the path directory on terminal. In terminal 'pwd' Enter, shows path name of 'Django_Learning'
#To enter the path ToDo use 'cd Django_ToDo' in terminal and Enter, you will be there in ToDo path and check by 'pwd' it shows path name.
#Now we have to create a VirtualEnvironment (Env) for this project:
#To install Env --->                                 "pip install virtualenv"  (In DjangoPython, it is an built-in package, you can directly create the Env in terminal or gitbash cmd )
#To create Env --->                                  "python -m venv pujar2(folderName)" 
#To activate Env in git bash cmd--->                  "source pujarEnv2(foldername)/scripts/activate" (in vs code use ". pujarEnv2(foldername)/scripts/activate")
#To check the any packages it contains in Env--->    "pip freeze"
#To exit from current Env --->                       "deactivate"



#1) First we have to create folder "ToDo_part2" in Django_Learning folder, and open that folder in vsCode.

#2) create env in that folder, in terminal "python -m env envpart2", and activate it by, ". envpart2/scripts/activate", you can see that enpart2 folder in directory.

#3) Then create djangoproject folder, in terminal "django-admin startproject toDo_main .", it creates toDo_main folder in directory, 
# it contains "__init__.py" ,"asgi.py", "settings.py", "urls.py", "wsgi.py" and outside this folder "manage.py" file is there.

#4) start write the code in "urls.py" line:23 (  path('', views.home, name='home'),   ) and (    import the views file   )
#create a new file called "views.py " in 'toDo_main' folder and write code for it.

#5) run the project and check django working or not in server by "python manage.py runserver"

#6) Then you have 18 unapplied migrations to complete allmigrations use in terminal "python manage.py migrate" 
# and check by copying that server link and admin for it "http://127.0.0.1:8000/admin" .

#7)And then create the super user by in terminal "python manage.py createsuperuser", 
# it asks for userName: 'SrinivasPujar', email: 'seenupujar0309@gmail.com', password: 'Pujar@2818', re-enter pwd: 'Pujar@2818', it creates admin ID. 
# Then in server make login by entering userName and password. 

#8) create "Templates" folder in directory, in Templates create a file 'home.html' write some code in it,
#in "settings.py" line:57 add templates in [] (    'DIRS': ['Templates'],     ) and run server it will give output.

#9) In 'home.html'  the code for ToDo App.  



#10) GitHub
#The above ToDo project storing in git repository by using git commands.
# open gitHub account, and open NewRepository by in gitHub rightSide click '+' icon and add Newrepository.
#fill Repository name 'Django_toDo' and make public and create Repository.
#in terminal "git init" to intialize new empty repo, and "git add -A" for storing all files (if you use "git add manage.py" it only stores that file).
#(it takes time)After completion of adding all files, " git commit -m "first commit(toDo_App_intialize)" " (it takes time)
#after that "git branch -M main" it makes main branch in our git repo, 
# "git remote add origin linkOfGitHubRepo(https://github.com/SrinivasPujar18/Django_toDo_.git) " this will create path for our gitHub repo.
#After that we have to push code by "git push -u origin main", this is the main cmd after pushing you can see code in gitHubRepo.


# Git commands:-

#…or create a new repository on the command line

# echo "# Django_toDo_" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/SrinivasPujar18/Django_toDo_.git
# git push -u origin main


# …or push an existing repository from the command line
# git remote add origin https://github.com/SrinivasPujar18/Django_toDo_.git
# git branch -M main
# git push -u origin main



#11) App and Models
# Start implementing HomePage by working dynamically ToDo_App in server, create App in terminal by "python manage.py startapp todo" then it creates App and contains files like,
#folder 'migrations', files '__init__.py', 'admin.py', 'apps.py', 'models.py', 'tests.py', 'views.py'
#After that in "settings.py" line:33 (adding 'todo' App in INSTALLED_APPS). After that in "todo/models.py" write code for it.
#In "todo/models.py" write code and in "todo/admin.py" write code
#Then make migrations and apply those migrations by "python manage.py makemigrations" this will generate the sql queries, and creates migration file of "0001_initial.py" in migrations folder
#In that "0001_initial.py" file the model Task is created. Then we apply this migration in database by "python manage.py migrate",
#"python manage.py migrate" this will shows the database in Django-admin-panel --> login admin-panel, that shows 'todo' App and it contains 'Task' database in it.
#After that in 'Task' database and AddTask in it.



#12) Fetching Task
#(In server by Adding task in it, after completing task markAsDone in server, then it shows in completed task).
#We have created manually some Task in django-admin server, 2 task created 1)complete Assignment 2)Learn python and Django
#In "toDo_main/views.py" in 'home' func line:7 and edit code, after that edit code in 'home.html'
#Now we displaying the tasks in web server page line by line. but buttons not working


#13) Admin list_display
#Now we have to make buttons to work properly, before that we make 
#Admin list_display --> this helps to display the proper task is complted or not in server. By changing in "todo/admin.py" line:4 edit code (class TaskAdmin():) and you see the result in server whether completed or not.
#We can also create 'search_Button' in Task database on django-admin-panel server, by editing code in "todo/admin.py" line:4 (class TaskAdmin():) with some Attributes, then we can see in server.
#we can use many Attributes to edit in Task database on django-admin-panel server.


#14) Add Task with CSRF(cross site request forgery) Token
#How to add task from server page by clicking button 'Add', and then that task should be stored in django-admin-panel database.
#In "toDo_main/urls.py" edit code (path of "todo.urls"), and then create 'urls.py' file in "todo" folder. In "todo/urls.py" write code for (path of AddTask),and it connected to "todo/views.py".
#In "todo/views.py" write code for (def addTask, and declare the views). after that make edit code in 'home.html' in 'add a task' form that CSRF token, 
#CSRF --> is used to prevent the cross site request forgery attacks. (cyber attack for user credentials)
#After that runserver and click the 'Add' button, it triggers to next page, and prints accordingly...


#15) Add Task func
#In "todo/views.py" edited code of 'addTask' func, then it adds task in homePage according to the user by clicking button on server.
#we can alter the added task in server by edit code in "toDo_main/views.py" in(5)--> ('home' func).       (order_by('updated_at')) shows task in ascending (order_by('-updated_at')) show task in descending.

#16) we have store these updated codes to GitHub
#In terminal "git status" it shows the updated or modified 
