from flask import Flask, render_template, flash, redirect, url_for
from datetime import datetime
from TestForms import HateListRegistrationForm
import csv, os
import pandas as pd
app = Flask(__name__)

#randomly generated secret key I may use for something later
app.config['SECRET_KEY'] = '31271d66321b32a7f3e9ad4c27106e85'

    #variables
#grab date time
currentDateTime = datetime.now()
listOfGarbage = [
    {
        'title': 'Google',
        'link': 'https://www.google.com',
        'text': 'visit google to search for garbage and stuff'
    },
    {
        'title': 'Amazon',
        'link': 'https://www.amazon.com',
        'text': 'visit amazon to buy garbage and stuff'
    },
    {
        'title': 'Instagram',
        'link': 'https://www.instagram.com',
        'text': 'visit instagram to take pictures of the garbage and stuff you bought'
    }
]

#ul elements
ulElements = [
    "first unordered item",
    "also unordered",
    "third, maybe fourth unordered item",
    "this is something too"
]

schedule = [
    "4:00, wallow in self pity",
    "4:30, stare into the abyss",
    "5:00, solve world hunger, tell no one",
    "5:30, jazzercize",
    "6:30, dinner with me - I can't cancel that again",
    "7:00, wrestle with my self-loathing"
]

def get_image_path_list():
    pathList = []
    for file in os.listdir("./static/images"):
        if file.endswith(".jpg") or file.endswith(".jpeg"):
            stringPath = os.path.join("/static/images", file)
            pathList.append(stringPath)
    return pathList

def get_data_fame(csvName):
    dataFrame = pd.read_csv(csvName)
    dataFrame.reset_index()
    return dataFrame

    #set routes
#index route
@app.route('/', methods=['GET', 'POST'])
def index():
    #form variables 
    form = HateListRegistrationForm()

    #image paths
    imagePaths = get_image_path_list()
    #dataFrame HTML
    data_frame_HTML = get_data_fame('HateRegistry.csv').to_html()
    
    if form.validate_on_submit():
        flash(f'Succesfully added {form.firstName.data} {form.lastName.data} to the list of people I hate', 'success')
        #submit was succesful can write data to file
        with open('HateRegistry.csv', mode='a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([form.firstName.data, form.lastName.data, form.reasonForHate.data])
        return redirect(url_for('index'))

    #return the page
    return render_template('index.html', 
                            dateTime=currentDateTime, 
                            garbage=listOfGarbage, 
                            lElements=ulElements, 
                            schedule=schedule, 
                            form=form, 
                            imagePaths=imagePaths,
                            table_html=data_frame_HTML)

#set debugging
if __name__ == '__main__':
    app.run(debug=True)

