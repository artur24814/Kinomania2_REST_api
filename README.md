# Kinomania2_REST_api
<hr>
<center><img src="https://www.django-rest-framework.org/img/logo.png"></center>
<hr>

<ul>
<h2>Contents</h2>
<li><a href="#info"><h3>Info</h3></a>Information about the resources used in this project</li>
<li><a href="#kinomania2"><h3>KNOMANIA REST API</h3></a>Website for looking translation of words and create your self vocabulary and train your knowledge in a card game</li>
<li><a href="#clone_project"><h3>Clone and Run a Django Project</h3></a>how run projects in your computer</li>
</ul>

<hr>
<center><h1>INFO</h1></center>
<h4>Information about the additional library, external Api used in this project and general information</h4>
<ul>
<li><strong>wikipedia Api</strong> <p>Used when user add movie and 
when he didn't writen description, application found itself appropriate  description using wikipedia Api, if title will be wrong and application couldn't did this, in label 'description' will be put information from label 'tiltle'</p></li>
<li><strong>GeoIP2</strong><p>
Used when user add cinema and didn't writen 'city', in this case application check your public ip (you can check your public ip yourself in website <a href="https://www.whatismyip.com/">https://www.whatismyip.com/</a>) and with using api GeoIP2 found city where user is, and put name of city in label 'city'
</p></li>
<li><strong>django-crontab</strong>
<p>using for delete screening when screening is out-of date.
Every 5 seconds crontab check screening datetime, and when actual date and time is more than date and time in screening it will be delete</p>
<p>don't forget write this command 
<code>python manage.py crontab add</code>
</p></li>
<li><strong>Views</strong>
<p>I write it with using API views, it's my own personal choice because I think in this case you can better see what is going on underneath 
(in further I will use generic views and mixing because it's less writing code  &#128527;)</p>
</li>
<li><strong>Tests</strong>
<p>i used pytest-django to testing my application</p>
<p> run test using command <code>pytests</code></p></li>
</ul>
<hr>

<center><h1 id="kinomania2">KINOMANIA REST API 🆕</h1></center>
<h3>it is additional rest api application to my previous website KINOMANIA </h3>
<p>in this api we have  6 endpoints</p>
<ol>
<li><code>/kinomania/movies/</code>for creating and see list all movies</li>
<li><code>/kinomania/movies/'some Id'/</code>for get movie detail view, update and delete movie</li>
<li><code>/kinomania/cinema/</code>for get ang create cinema</li>
<li><code>/kinomania/cinema/'some Id/</code>for get cinema detail view and delete cinema</li>
<li><code>/kinomania/screening/</code>get and create screening</li>
<li><code>/kinomania/screening/'some Id'/</code>for get screening detail and delete screening</li>
</ol>
<p>when user hit in endpoint <code>/kinomania/movies/</code> he will get list of all movies, every movie has information of this particular url </p>
<p>In this endpoint we have methods like</p>
<ol>
<li>GET</li>
<li>POST</li>
</ol>
<p align="center">
<img src="https://user-images.githubusercontent.com/97242088/180040631-c02be08a-07a5-4246-92d7-592405873557.png" width="350" alt="Home page" title="Home page"> </p>
<p> when user hit on this url <code>/kinomania/movies/'some Id'/</code> he will see information about this film, title, description, director and actors (movie can have many actor, but one director) </p>
<p>In this endpoint we have methods like</p>
<ol>
<li>GET</li>
<li>PUT</li>
<li>DELETE</li>
</ol>
<p align="center">
<img src="https://user-images.githubusercontent.com/97242088/180040741-3d645bd0-cb30-46dc-bace-cd42c95bd858.png" width="350" alt="rest_api_mowie_detail" title="rest_api_mowie_detail"> </p>

<p>next user can hit in endpoint <code>/kinomania/cinema/</code> and he will get list of all cinema with url to films which shown in this cinema</p>
<p>In this endpoint we have methods like</p>
<ol>
<li>GET</li>
<li>POST</li>
</ol>
<p align="center">
<img src="https://user-images.githubusercontent.com/97242088/180040773-11df076f-251f-4a9f-a4c1-910787f229b6.png" width="350" alt="rest_api_cinema_list" title="rest_api_cinema_list"> </p>
<p>next he go to endpoint <code>/kinomania/cinema/'some Id/</code> and wow, he can get all screenings in this cinema with date and time 😎. cinema can have many film in it and screenings in it</p>
<p>In this endpoint we have methods like</p>
<ol>
<li>GET</li>
<li>DELETE</li>
</ol>
<p align="center">
<img src="https://user-images.githubusercontent.com/97242088/180040769-f29ed2f5-67dd-4bf7-9c90-d4377b7313b4.png" width="350" alt="Rest_api_delete_cinema" title="Rest_api_delete_cinema"> </p>

<p>In endpoint <code>/kinomania/screening/</code> we have list of all screenings with date time movie and cinema, particular screening can has only one movie and only one cinema one</p>
<p>In this endpoint we have methods like</p>
<ol>
<li>GET</li>
<li>POST</li>
</ol>
<p align="center">
<img src="https://user-images.githubusercontent.com/97242088/180040748-79322769-af63-493e-a6e0-1cd411be35dd.png" width="350" alt="Rest_api_screening_list" title="Rest_api_screening_list"> </p>

<p>and something go wrong and screening must be deleted before it play(because after it play at the cinema this will do for as crontab) at the cinema, we can do this in endpoint <code>/kinomania/screening/'some Id'/</code></p>
<p>In this endpoint we have methods like</p>
<ol>
<li>GET</li>
<li>DELETE</li>
</ol>
<p align="center">
<img src="https://user-images.githubusercontent.com/97242088/180041959-381764d0-9e9b-497d-ab36-21046da5c97f.png" width="350" alt="Rest_api_delete_screening" title="Rest_api_delete_screening"> </p>To?


<p>run this code <code>python manage.py addactorsdirectorsfilms</code> to add in database actors movies and directors and bee in one wave with me 😉 </p>
<hr>

<h3 id="clone_project">Clone and Run a Django Project</h3>

Before diving let’s look at the things we are required to install in our system.

To run Django prefer to use the Virtual Environment

`pip install virtualenv`

Making and Activating the Virtual Environment:-

`virtualenv “name as you like”`

`source env/bin/activate`

Installing Django:-

`pip install django`

Now, we need to clone project from Github:-
<p>Above the list of files, click Code.</p>
<img src="https://docs.github.com/assets/cb-20363/images/help/repository/code-button.png">

Copy the URL for the repository.
<ul>
<li>To clone the repository using HTTPS, under "HTTPS", click</li>
<li>To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click</li>
<li>To clone a repository using GitHub CLI, click GitHub CLI, then click</li>
</ul>
<img src="https://docs.github.com/assets/cb-33207/images/help/repository/https-url-clone-cli.png">

Open Terminal.

Change the current working directory to the location where you want the cloned directory.

Type git clone, and then paste the URL you copied earlier.

`$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`

Press Enter to create your local clone.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...<br>
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Install the project dependencies:

`pip install -r requirements.txt`

Now go to the setting.py and change the SECRET_KEY.
from
`SECRET_KEY = os.environ.get('SECRET_KEY')`
to
`SECRET_KEY = 'your own secret key'`
and `DEBUG = True`

create admin account (**remember you must be at the main application folder with file manage.py, and do this steps for
each application in this repository!!!!**)

`python manage.py createsuperuser`

then

`python manage.py makemigrations`

then again run

`python manage.py migrate`

run this command to start periodic tasks in application

`python manage.py crontab add`

run this code to add in database actors movies and directors and bee in one wave with me

`python manage.py addactorsdirectorsfilms`

to start the development server

`python manage.py runserver`

and open localhost:8000 on your browser to view the app.

Have fun
<p style="font-size:100px">&#129409;</p>