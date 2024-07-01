def seperate(l2):

    l2=list(dict.fromkeys(l2))

    try:
        l2.remove('')
    except:
        print("No '' found")

    # print(l2)
    l=l2[1]
    # print(l)
    if "नाम" in l:
        # print("found")
        name = l.split("नाम")
        # print(name)
        name=name[1].replace(":","")
        # print(name)
    else:
        name=""


    f_names=l2[2]
    # print(f_names)
    if "नाम" in f_names:
        print("found")
        father_name = f_names.split("नाम")
        # print(father_name)
        father_name=father_name[1].replace(":","")
        # print(father_name)
    else:
        f_names=""


    makaan = l2[3]
    if "संख्या" in makaan:
        print("found")
        mk = makaan.split("संख्या")
        # print(name)
        mk=mk[1].replace(":","")
        try:
            mk=mk.split('शि')
            # print(mk[0])
            mk=mk[0]
        except:
            mk = ""
    else:
        mk=""


    aayu=l2[4]
    # try:
    if "आयु: " in aayu:
        aayuy=aayu.split("आयु: ")
        aayuy=aayuy[1]
    elif "आयु :" in aayu:
        aayuy=aayu.split("आयु :")
        aayuy=aayuy[1]
    else:
        aayuy=""
    # except:
    #     aayuy=aayu.split("आयु :")
    #     aayuy=aayuy[1]
    # print(aayuy)
    if "लिंग" in aayuy:
        age=aayuy.split("लिंग")
        age=age[0]
        print(age,"ehghghg")

        if "महिला" in aayu:
            ling="महिला"
            # print(ling)
        elif "पुरुष" in aayu:
            ling="पुरुष"
            # print(ling)
        else:
            ling=""
    else:
        ling=""
        age=""
    return name,father_name,mk,age,ling



def trip_ent(data3,un_id,eng_text_new):

    # un_id=[11,22,33]
    try:
        for i in range(4):
            data3.remove('')
    except:
        print("..")

    name_list=[]
    f_name_list=[]
    mk_list=[]
    age_list=[]
    ling_list=[]

    print(data3)
    names = data3[1]
    if "निर्वाचक का नाम" in names:
        names=names.split('निर्वाचक का नाम')
        # print(names)
    elif "नाम" in names:
        names=names.split('नाम')
        # print(names)
    for i in range(len(names)):
        # print(names[i])
        if ":" in names[i]:
            names[i]=names[i].replace(":","")
            name_list.append(names[i])
    # print(name_list)

    f_name=data3[2]
    f_name=f_name.split(":")
    # print(f_name)
    for i in range(len(f_name)-1):
        # print(i)
        if "पिता" in f_name[i+1]:
            f_name[i+1]=f_name[i+1].replace("पिता का नाम"," ")
            # print(f_name[i+1])
            f_name_list.append(f_name[i+1])
        elif "पति" in f_name[i+1]:
            f_name[i+1]=f_name[i+1].replace("पति का नाम"," ")
            # print(f_name[i+1])
            f_name_list.append(f_name[i+1])
        else:
            # print(f_name[i+1])
            f_name_list.append(f_name[i+1])

    mk=data3[3]
    if "संख्या" in mk:
        mk=mk.split("संख्या")
        # print(mk)
    for i in range(len(mk)):
        # print(f_name[i])
        if ":" in mk[i]:
            mk[i]=mk[i].replace(":","")
            mk[i]=mk[i].split("शि")
            # print(mk[i][0])
            mk_list.append(mk[i][0])
        else:
            mk_list.append("")
    print(mk_list)


    age=data3[4]
    if "आयु" in age:
        age=age.split("आयु")
        # print(age)
    for i in range(len(age)):
        # print(f_name[i])
        if ":" in age[i]:
            age[i]=age[i].replace(":","")
            age[i]=age[i].split("लिंग")
            age_list.append(age[i][0])
            print(len(age[i]))
            if len(age[i]) > 1:
                if "महिला" in age[i][1]:
                    ling_list.append("महिला")
                elif "पुरुष" in age[i][1]:
                    ling_list.append("पुरुष")
            else:
                ling_list.append(" ")
    print(age_list)
    print(ling_list)

    makaan_eng=mk_eng(eng_text_new)

    final_list=[]
    uuid=[]
    print(un_id,"list of unid")
    for i in range(4):
        print(len(un_id[i]))
        if len(un_id[i]) > 9:
            uuid.append(un_id[i])
        elif len(un_id[i])==3 and len(un_id[i+1]) != 10:
            uuid.append(un_id[i]+un_id[i+1])
    print(uuid)

    for i in range(len(name_list)):
        # print(uuid[i])
        try:
            # print(uuid[i])
            uuid[i]=uuid[i].split("\n")
            # print(uuid[i][0])
            uuid[i]=uuid[i][0]
            print("final",uuid[i])
        except:
            uuid[i]=uuid[i]
        single_list=[uuid[i],name_list[i],f_name_list[i],mk_list[i],age_list[i],ling_list[i],makaan_eng[i]]
        final_list.append(single_list)
        # print(single_list)

    return final_list


def filter_id(ss):
    ss=ss[::-1]
    # print(ss)
    for i in ss[:5]:
        if i.isalpha() == True:
            # print(i)  
            ss=ss.replace(i,"",1)  
    return ss[::-1]


def mk_eng(string_eng):
    mk=[]
    count = string_eng.count("Photo")
    print(count)
    string = string_eng.split("Photo")
    for i in range(count):
        new=string[i]
        new=new.split(" ")
        mk.append(new[-2])
    print(mk)
    return mk

