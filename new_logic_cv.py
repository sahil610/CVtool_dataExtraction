import re

# text = "५॥९१3344853नाम: पिंकीपति का नाम: कन्हैयामकान संख्या : 0 शिएणं0 53आयु: 37 लिंग: महिला 8४8080/6"
def extract_data(text):
    # Extract name
    name = re.search(r"नाम: (.+?)पति", text)
    if name:
        name = name.group(1)
    else:
        name = "Name not found"

    # Extract husband's name
    husband_name = re.search(r"पति का नाम: (.+?)मकान", text)
    if husband_name:
        husband_name = husband_name.group(1)
    else:
        husband_name = "Husband's name not found"

    # Extract age
    # age = re.search(r"आयु: (\d+)", text)
    age = re.search(r"आयु: (.+?)लिंग", text)
    if age:
        age = age.group(1)
    else:
        age = "Age not found"

    # Extract house number
    # house_number = re.search(r"मकान संख्या : (\d+)", text)
    house_number = re.search(r"मकान संख्या : (.+?)शि", text)
    if house_number:
        house_number = house_number.group(1)
    else:
        house_number = "House number not found"

    # Extract ling (gender)
    ling = re.search(r"लिंग: (.+?)\s", text)
    if ling:
        ling = ling.group(1)
    else:
        ling = "Ling not found"

    # Print the extracted information
    # print("Name:", name)
    # print("Husband's name:", husband_name)
    # print("Age:", age)
    # print("House number:", house_number)
    # print("Ling:", ling)
    return ling

# ll=[]

# a=['  23 शि0णं0 [3 मकान ', '  23 शिए0ं0 3 मकान ', '  १24 शिएए0 3']
# for i in range(len(a)):
#     print(a[i])
#     ab=a[i].split("शि")
#     print(ab[0])
#     ll.append(ab[0])
# print(ll)