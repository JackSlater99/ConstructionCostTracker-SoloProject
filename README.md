# Construction Cost Tracker

This solo project was created during week 5 of the CodeClan Proffesional Software Development Course. The project week gave us a choice of 4 project briefs to complete which would showcase the skills learnt in the first 4 weeks of the course.

## Brief

Build an app that allows a user to track their spending:
- The app should allow the user to create and edit `Transaction`s.
- The app should allow the user to create and edit `Merchant`s, e.g. Tesco, Amazon, ScotRail.
- The app should allow the user to create and edit `Tag`s for their spending, e.g. groceries, entertainment, transport.
- The user should be able to assign `Tag`s and `Merchant`s to a `Transaction`, as well as an amount spent on each `Transaction`.
- The app should display all the `Transaction`s that a user has made in a single view, with each `Transaction`'s amount, `Merchant` and `Tag`, as well as the total amount of all transactions.

## Extension Features
- View all `Transaction`s by `Category` or `Supplier`.
- Display Total amount of `Transaction`s for each cattegory.
- Graph using Matplotlib to display total cost per per `Category`.


## Getting Started

To get started, clone this repository to a location of your choice. Commands shown below were used for Git Bash on Windows 10 and may vary by system.

### Dependencies

* Python3
* Flask
* PostgreSQL
* Matplotlib

### Installing

* Copy Git Repository: 
```bash
git clone https://github.com/JackSlater99/Week-5---Solo-Python-Project 
```
* Flask: 
```bash 
pip install -U Flask
```
* Matplotlib: 
```bash 
pip install -U matplotlib 
```

### Executing program

* Create Database with pSQL:
```bash
createdb cost_tracker
```
* Link Database and SQL file from project directory:
```bash 
psql -d cost_tracker -f db/cost_tracker.sql 
```
* Run Flask:
```bash
flask run 
```

Navigate to http://127.0.0.1:5000 (default route for Flask) in your browser or click on the link in the terminal.

## Help

## Authors

Contributors names and contact info:

Jack Slater - https://www.linkedin.com/in/j-slater99/

## Version History

1.0
    * Initial Release
    
## Acknowledgments

* [Dom Pizzie](https://gist.github.com/DomPizzie) - README - Template Author

