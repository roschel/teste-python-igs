# How to run this project

1. Clone this repository in your machine: <br>
`git clone git@github.com:roschel/teste-python-igs.git`
2. Access the directory of the cloned repository: <br>
`cd teste-python-igs`
3. Create the virtualenv: <br>
`make virtualvenv`
4. Run the following command to migrate the components: <br>
`make migrate`
5. Create your superuser and when asked, insert your super secret password ont he terminal: <br>
`make create-user`
6. Build and run your application with docker by running the following command: <br>
`make build`

## Accessing the application
Now, you are good to go to your browser in http://loclahost:8000/ <br>
Here you'll see a empty screen just like that: <br>
![image](https://user-images.githubusercontent.com/52433168/229001624-7f7050b0-aaf4-4273-bba4-c3d0241834e7.png)
(Sorry, my skills in frontend are very limited)

Now, to create a employee, you can create first a department in http://localhost:8000/api/v1/departments/ <br>

And then you will see a screen just like that:
![image](https://user-images.githubusercontent.com/52433168/229001891-1ba10311-c386-490b-ba13-5b846a0abfec.png)

Feel free to create any department you want. Or, if you prefer, just go to http://localhost:8000/admin and you'll see the admin page from django and there you can create your objects too!

That's it folks! In case of doubts, please feel free to contact me: joaomroschel@gmail.com