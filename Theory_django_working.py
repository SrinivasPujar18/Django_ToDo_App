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
