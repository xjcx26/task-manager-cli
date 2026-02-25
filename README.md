# Task Manager (CLI)

A command-line task manager built in Python.

This project allows users to manage tasks through a structured CLI interface with persistent JSON storage.

## Features

- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Clear completed tasks
- Persistent storage using JSON
- Object-oriented design
- Dictionary-based dispatch pattern for menu handling
- Separation between business and interface layer

## Architecture

The project is structured with separation of concerns.

### TaskManager Class

Handles:

- Task storage
- Business logic
- JSON persistence
- State management

### Interface Layer

Handles:

- User input
- Validation
- CLI display
- Command dispatching

### Dispatch Pattern

A dictionary-based system maps menu options to interface handlers, removing long conditional chains and improving scalability.

## How It Works

- Tasks are stored in a `tasks.json` file.
- Data is loaded when the program starts.
- Changes are saved automatically after modifications.
- The CLI loop routes user input through the dispatch dictionary.
- Interface handlers collect user input and call business logic methods.

## Technologies Used

- Python
- JSON for data persistence
- Git for version control

## Learning Goals

This project was built to practice:

- CRUD operations (Create, Read, Update, Delete)
- Object-Oriented Programming (OOP)
- Separation of concerns
- Dictionary-based command dispatching
- Refactoring from procedural to structured architecture
- Clean version control practices

## Future Improvements

- Fully remove print statements from business layer
- Add due dates and priority levels
- Add search functionality
- Replace JSON storage with database backend
- Build a web-based version
