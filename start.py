#pip install flask 
#pip install requests
from flask import Flask, render_template, request, url_for, redirect, session, jsonify
import json
import re
from bson import ObjectId

import webbrowser

class MyFlaskApp:
    def __init__(self):
        # GLOBAL VARS
        self.curr_email = ''
        self.selected_result = ''

        # Initialize Flask app
        self.app = Flask(__name__, static_url_path='/static')   # COLE - Added "static_url_path='/static" to reference static files in code
        self.app.secret_key = 'your_secret_key_here'

        ### APP ROUTES ###
        
        # HOME / SINGLE PAGES
        self.app.add_url_rule('/', 'index', self.index)
        
        self.app.add_url_rule('/genieBot', 'genieBot', self.genieBot, methods=['POST','GET'])
        
        
        
        
        
        
        webbrowser.open("http://127.0.0.1:5000")
        

    ######################################
    ######################################
    ############# ACTUAL APP #############
    ######################################
    ######################################
    
    ###############################
    ######## LAUCH POINTS #########
    ###############################
    def index(self):
        return render_template('index.html')
    
    
    
    ###############################
    ############# FORMS ###########
    ###############################
    
    
    
    
    ###############################
    ####### FORM VALIDATION #######
    ###############################
    
    def genieBot(self):
        """_summary_: do stuff then return home

        Returns:
            _type_: _description_
        """
        # we are asking them for a transcript from csu stanislaus
        # so we will be receiving a pdf and we will have to parse 
        # to get all the classes they have taken and we will give that in a dictionary of itself
        
        if request.method == 'POST':
            # Extract form data
            name = request.form.get('name', '')
            year = request.form.get('year', '')
            if year == None:
                pass
            else: 
                year = int(year)
                
            hours_can_work = request.form.get('hoursCanWork', '')
            if hours_can_work == 'time1':
                hours_can_work = 10
            if hours_can_work == 'time2':
                hours_can_work = 20
            if hours_can_work == 'time3':
                hours_can_work = 30
            
            uploaded_file = request.files.get('file')

            # Process the uploaded file if any
            if uploaded_file:
                uploaded_file = True
            
            # Additional form fields processing
            teacher_liked = request.form.get('teacherLiked', '')
            teacher_hate = request.form.get('teacherHate', '')

            # Store form data in a dictionary
            data = {
                "name": name,
                "year": year,
                "hours_can_work": hours_can_work,
                "teacher_liked": teacher_liked,
                "teacher_hate": teacher_hate
            }

            # Render a template with the data
            return render_template('genieBot.html', dictionary=data)

        # If GET request, render the form
        return render_template('genieBot.html')

    #################################
    #################################
    ######## HELPER FUCTIONS ########
    #################################
    #################################
        
    def parseStringToDict(self, stringedDictionary:str):
        # Define a regular expression pattern to match key-value pairs
        pattern = r"'(\w+)': (?:'([^']*)'|(?:\[(.*?)\])|(\d+\.\d+)|ObjectId\('([^']*)'\))"

        # Find all key-value pairs in the string
        matches = re.findall(pattern, stringedDictionary)

        # Create a dictionary from the matches
        data = {}
        for key, value_str, list_str, float_str, obj_id in matches:
            value = value_str if value_str else (list_str.split(', ') if list_str else (float(float_str) if float_str else obj_id))
            data[key] = value
        
        # data = self.remove_double_quotes(data)
        return data
    
    
    def check_empty(self, results):
        results_list = list(results)
        return results_list, len(results_list) == 0
        
if __name__ == "__main__":
    x = MyFlaskApp()
    x.app.run(host="0.0.0.0", port=5000)
def main():
    pass

if __name__ == "__main__":
    main()