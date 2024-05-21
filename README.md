# Learning Objectives

By the end of this book, you will be able to:

- Understand the concept of a RESTful API
- Build a RESTful API using Flask and the Flask-Restful extension
- Manipulate a database using Flask-SQLAlchemy and Flask-Migrate
- Send out plaintext and HTML format emails using the Mailgun API
- Implement a pagination function using Flask-SQLAlchemy
- Use caching to improve API performance and efficiently obtain the latest information
- Deploy an application to Heroku and test it using Postman

# Audience

This book is ideal for aspiring software developers who have a basic-to-intermediate knowledge of Python programming and who want to develop web applications using Python. Knowledge of how web applications work will be beneficial, but is not essential.

# Approach

This book takes the learning-by-doing approach to explain concepts to you. You'll build a real-life web application by implementing each concept that you learn in theory. This way, you'll reinforce your new skill.

# Hardware Requirements

For the optimal experience, we recommend the following hardware configuration:

- **Processor:** Intel Core i5 or equivalent
- **Memory:** 4 GB RAM (8 GB preferred)
- **Storage:** 35 GB available space

# Software Requirements

We also recommend that you have the following software installed in advance:

- **OS:** Windows 7 SP1 64-bit, Windows 8.1 64-bit or Windows 10 64-bit, Ubuntu Linux, or the latest version of OS X
- **Browser:** Google Chrome/Mozilla Firefox (the latest version)
- **Python:** Python 3.4+ (the latest version is Python 3.8: from [https://python.org](https://python.org))
- **Pycharm**
- **Postman**
- **Postgres Database**

# Conventions

Code words in the text, database table names, folder names, filenames, file extensions, pathnames, dummy URLs, user input, and Twitter handles are shown as follows:

"Next, we will work on the `create_recipe` function, which creates a recipe in memory. Use the `/recipes` route to trigger the `create_recipe` function and the `methods = [POST]` argument to specify that the route decorator will only respond to POST requests."

New terms and important words are shown in **bold**. Words that you see on screen, for example, in menus or dialog boxes, appear in the text like this: "Then, select **Definition** and set the password. Click **Save**."

A block of code is set as follows:

```python
if not recipe:
    return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND
