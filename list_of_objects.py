
from csv import reader
# import the App class from the app.py file
from app import App

apps = []

with open('code/advanced/apps.csv') as csv_file:
    csv_reader = reader(csv_file, delimiter=',')
    next(csv_reader)
    for name, description, category in csv_reader:
        apps.append(App(name, description, category))

# Iterate through the list of Apps and display the details of the apps
for app in apps:
    app.display()

# Iterate through the list of Apps and display the details of social media apps
for app in apps:
    if app.category == "social media":
        app.display()
