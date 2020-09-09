#!/usr/bin/python3
import json
from bs4 import BeautifulSoup as bs

def soupit(html):
    soup = bs(html, "lxml")
    raw_info = soup.findAll("div", {"class" : "voterInformation"})
    text_info = raw_info[0].text
    spaced_info = " ".join(text_info.split())
    a = spaced_info.replace("This is not me | ", " ")
    b = a.replace("My name has changed ", " ") 
    c = b.replace("You can view your sample ballot closer to the next election. ", " ")
    d = c.replace("Is this address incorrect? Is this address incorrect?", " ")
    e = d.replace("Effective Date of Registration:", "<li>Effective Date of Registration:")
    f = e.replace("Residence Address:", "<li>Residence Address:")
    g = f.replace("Mailing Address:", "<li>Mailing Address:")
    h = g.replace("Voter Unique Identification:", "<li>Voter Unique Identification:")
    i = h.replace("Precinct", "<li>Precinct")
    clean_info = i.strip("  ")
    formatted = "<li>" 
    formatted += clean_info.replace("\n", "</li>")
    return formatted

def jsonify(voter_data):
    values_dict = {
        "vuid": "",
        "fname": "",
        "lname": "",
        "rdate": "",
        "bdate": "",
        "raddress": "",
        "maddress": "",
        "precinct": ""
    }

    d = soupit(voter_data.data)

    a = d.split("<li>")
    values = []

    for v in a:
        t = v.strip()
        h = t.replace("\n", "")
        i = h.replace("  ", "")
        j = i.strip()
        values.append(j)

    values.pop(0)
    values_dict["fname"] = values[0].split(" ")[0] 
    values_dict["lname"] = values[0].split(" ")[1]
    values.pop(0)
    values_dict["vuid"] = values[0].split(":")[1]
    values_dict["rdate"] = str(values[1].split(":")[1])
    values_dict["raddress"] = values[2].split(":")[1]
    values_dict["maddress"] = values[3].split(":")[1]
    values_dict["precinct"] = values[4].split(":")[1]
    values_dict["bdate"] = str(voter_data.bdate)

    print(json.dumps(values_dict, sort_keys=False, default=None))
    return json.dumps(values_dict, indent=0, sort_keys=False, default=None)




