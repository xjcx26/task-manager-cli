# Task Manager (CLI)

A command-line task manager built in Python.

This project allows users to manage tasks directly from the terminal using a simple menu-driven interface.

## Features

- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Clear completed tasks
- Persistent storage using JSON

## How It Works

- Tasks are stored in a `tasks.json` file.
- Data is loaded when the program starts.
- Changes are saved automatically after modifications.
- The application runs in a continuous loop until the user exits.

## Technologies Used

- Python
- JSON for data persistence
- Git for version control

## Learning Goals

This project was built to practice:

- CRUD operations (Create, Read, Update, Delete)
- Working with lists and dictionaries
- File handling and JSON serialization
- Input validation
- Control flow design
- Structuring a CLI application

## Future Improvements

- Refactor into object-oriented structure
- Build a web-based version
- Add due dates and priority levels
- Connect to a database instead of JSON
