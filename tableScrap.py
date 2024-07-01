import re
from PyPDF2 import PdfReader


def remove_empty_values(lst):
    return [value for value in lst if value.strip() != '' and value.strip() != "'" and value.strip() != '"']


def remove_value(lst):
    return list(filter(lambda x: x != 'आयु ', lst))


def remove_gender_values(value):
    return value.replace(" ४8806", "")


x = ['52 (0?./73/357/020428 53 (?./73/357/7020434 54 ५0 894443', 'नाम: शकुन्तला नाम: दौजीराम', 'पति का नाम: नरायन पिता का नाम: नेकसया',

         'मकान संख्या : 3704 शिा00 [5 मकान संख्या : 304 शिषएं0 5', 'आयु: 57 लिंग: महिला ४8896... | | आयु: 57 लिंग: पुरुष #४8॥896.. |']


def struct(x):
    uniqieId = []
    age = []
    gender = []
    name = []
    father_name = []
    house_no = []
    final_list = []
    for i in x:
        # if re.findall("\d\d/\d\d\d/\d\d\d\d\d\d", i):
        #     for id in re.findall("\d\d/\d\d\d/\d\d\d\d\d\d", i):
        #         uniqieId.append(id)
        if "पिता का नाम" in i:
            try:
                for n in i.split("पिता का नाम:"):
                    if "पति का नाम" in n:
                        for a in remove_empty_values(n.split("पति का नाम:")):
                            father_name.append(a)
                    else:
                        father_name.append(n)
            except:
                for n in i.split("पिता का नाम :"):
                    if "पति का नाम" in n:
                        for a in remove_empty_values(n.split("पति का नाम :")):
                            father_name.append(a)
                    else:
                        father_name.append(n)

        elif "नाम:" in i:
            name = remove_empty_values(i.split("नाम: "))
            if len(name) == 0:
                name = remove_empty_values(i.split("नाम : "))
        elif "मकान संख्या" in i:
            house_no = remove_empty_values(i.split("मकान संख्या : "))
            if len(house_no) == 0:
                house_no = remove_empty_values(i.split("मकान संख्या: "))

        elif "आयु" in i:
            temp = remove_empty_values(i.split("... | | "))
            for obj in temp:
                temp2 = remove_value(obj.split(": "))
                for t in temp2:
                    if (' लिंग' in t):
                        age.append(t.replace(' लिंग', ""))
                    else:
                        gender.append(remove_gender_values(t))
    for i in range(len(name)):
        tempdata = {}
        # try:
        #     tempdata["id"] = uniqieId[i]
        # except:
        #     tempdata["id"] = ""
        tempdata["name"] = name[i]
        tempdata["fathername/husbandname"] = father_name[i]
        tempdata["house_no"] = house_no[i]
        tempdata["age"] = age[i]
        tempdata["gender"] = gender[i]

        final_list.append(tempdata)
    return final_list




def count_pdf_pages(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        page_count = len(pdf_reader.pages)
        return page_count
