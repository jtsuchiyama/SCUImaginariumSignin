import requests

def parse_headers(text):
    # Init dictionary
    headers = {}

    # Loop through lines
    for line in text.split("\n"):
        # Split field name and value up so they can be assigned
        header = line.split(": ")

        if len(header) < 2:
            continue # no ": ", so it's probably just an empty line
        elif len(header) > 2:
            print("Help!") # This shouldn't happen
        else:
            headers[header[0]] = header[1]

    return headers

def send_attendance(url, data, header_text):
    """It takes google form url which is to be submitted and also data which is a list of data to be submitted in the form iteratively."""

    try:
        headers = parse_headers(header_text)
        r = requests.post(url, data=data, headers=headers)
        print(r.status_code)
        print("Form Submitted.")
    except:
        print("Error Occured!")

#url = 'https://docs.google.com/forms/d/e/1FAIpQLSeNP1YoUEjgucQggxYWmVPVeHMBmTuBA3FKRijpuJXvjMfn5Q/viewform'
url = 'https://docs.google.com/forms/d/e/1FAIpQLSfq-NpCCUbVG6HrwUkTOmNv8J2gcsUYTW_3Wa0PObjezsMAmg/formResponse'

data = {
    "entry.321941539": "Yes",
}

header_text = '''
entry.321941539: Yes
'''

send_attendance(url, data, header_text)
