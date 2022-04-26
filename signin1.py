import requests
import time

values = {
            # What is your full name? 
            # or 278721327
            #"entry.1264666384": "Jake Tsuchiyama",

            # I am a...
            # or 1660567039
            #"entry.1268903977": "Undergraduate Student",

            # What college are you in?
            # or 1997944194
            #"entry.1795708489": "School of Engineering",

            # What is/are your majors(s)?
            # or 1222822512
            #"entry.536694640": "COEN",

            # Main Purpose of visit (Specify other projects)
            # or 2138302888
            #"entry.1078672043": "Imaginet (Guild System)",

            # Expected duration of visit
            # or 348582369
            #"entry.1825447454": "1-3 hours",

            # What areas are you interested in?
            # or 1194417129
            #"entry.677187119": "Game Design",

            #"entry.1977811139": "Yes",
            "entry.321941539": "Yes",
        }

def send_attendance(url, data):
    """It takes google form url which is to be submitted and also data which is a list of data to be submitted in the form iteratively."""

    try:
        requests.post(url, data)
        print("Form Submitted.")
        time.sleep(5)
    except:
        print("Error Occured!")

#url = 'https://docs.google.com/forms/d/e/1FAIpQLSeNP1YoUEjgucQggxYWmVPVeHMBmTuBA3FKRijpuJXvjMfn5Q/viewform'
url = 'https://docs.google.com/forms/d/e/1FAIpQLSfq-NpCCUbVG6HrwUkTOmNv8J2gcsUYTW_3Wa0PObjezsMAmg/viewform'

send_attendance(url, values)
