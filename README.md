
*****************************************************************************************

Introdução ao FastAPI - Live com Tyrone Damasceno


Link: https://www.youtube.com/watch?v=OQtcCejrPoY


*****************************************************************************************


That's a simple CRUD application using FastAPI, an awsome framework that it's very intuitive
and, as the name says, freaking lightning fast !!!


I followed the link in the description above but I did some changes, like the use of pytest since
the beggining to result in a project with less bugs and some additional features, like the function
of list_pets with a name filter. It was very challenging create tests since I don't have much experience
doing it, particularly after the creation of db. Although it's been a rough time, it increased a lot my
skills in my personal projects. It became more like a reinterpretation of the tutorial, with my
personal implements of what would make it a better project. Another simple and well-know file
that almost all projects have is the .gitignore, that I started including in my projects. As always,
I hope that it helps you achieve your goal and increases your skills as it increased mine.


I confess that creating tests since the beggining of the code is not something very funny, but it
really keeps it less buggy and more trustful. One example of how it empowers your debugging skills
is a problem I had during the development of list_pets with the name filter. It was returning an
empty list instead of return the correct pets. By creating a test to raise a HTTPResponse with
a detail message helped me to understand the semantic error I commited. To check more details about
checkout the function list_pets() in file 'main.py'.


The project is already done according to the link, but I think it can get better yet. It may change
a few more additional features, like more tests and optimize the structure of code. Like any code,
it can always get more clean and better, but I think it seems nice already. Hope it may help you to
achieve your goals and thanks for your time !
