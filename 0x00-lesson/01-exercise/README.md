What this does is it first imports the Flask package in `app.py`, then it
instantiates a Flask object, and finally, it assigns it to the `app` variable.
We have created the main function as the entry point for our startup script.

This subsequently brings up the Flask web server. After that, we have defined
our first API function, `hello`, which returns a "Hello World" response. Using
the Flask decorator, we can route the GET request URL to this function.

Now open the browser and type `http://localhost:5000`. You will see the string
`Hello World!`. No special format, just plaintext. This means your first web
service passed the test, it works!
