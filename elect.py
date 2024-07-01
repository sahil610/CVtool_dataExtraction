import cv2
import numpy as np
import pdf2image
import pytesseract
import xlwt
from new_logic_cv import extract_data
from separater import seperate,trip_ent, filter_id, mk_eng
from tableScrap import struct, count_pdf_pages

# book = xlwt.Workbook()
# sheet=book.add_sheet('detail')


# global row
# row=0
# column=0

# content = ["निर्वाचन संख्या","निर्वाचक का नाम","पति/पिता का नाम","गृह संख्या","आयु","लिंग"]
# for item in content:
#     sheet.write(row,column,item)
#     column+=1


def write_to_sheet(row,one,two,three,four,five,six,sheet,seven):
    print(row,one)
    sheet.write(row,0,one)
    sheet.write(row,1,two)
    sheet.write(row,2,three)
    sheet.write(row,3,four)
    sheet.write(row,4,five)
    sheet.write(row,5,six)
    sheet.write(row,6,seven)

# # Extract page 3 from PDF in proper quality
# page_3 = np.array(pdf2image.convert_from_path('/home/hs/AI projects/OpenAI/testst_230426_200035.pdf',
#                                               first_page=3, last_page=3,
#                                               dpi=300, grayscale=True)[0])

def main(path,filename):


    book = xlwt.Workbook()
    sheet=book.add_sheet('detail')


    global row
    row=0
    column=0

    content = ["निर्वाचन संख्या","निर्वाचक का नाम","पति/पिता का नाम","गृह संख्या","आयु","लिंग","गृह संख्या english"]
    for item in content:
        sheet.write(row,column,item)
        column+=1

    lenght=count_pdf_pages(path)

    for i in range(lenght):
        if i ==  200:
            break
        else:
            # Extract page 3 from PDF in proper quality
            page_3 = np.array(pdf2image.convert_from_path(path,
                                                        first_page=i+1, last_page=i+1,
                                                        dpi=300, grayscale=True)[0])


            # Inverse binarize for contour finding
            thr = cv2.threshold(page_3, 128, 255, cv2.THRESH_BINARY_INV)[1]

            # Find contours w.r.t. the OpenCV version
            cnts = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]

            # STEP 1: Extract texts outside of the two tables

            # Mask out the two tables
            cnts_tables = [cnt for cnt in cnts if cv2.contourArea(cnt) > 10000]
            no_tables = cv2.drawContours(thr.copy(), cnts_tables, -1, 0, cv2.FILLED)

            # Find bounding rectangles of texts outside of the two tables
            no_tables = cv2.morphologyEx(no_tables, cv2.MORPH_CLOSE, np.full((21, 51), 255))
            cnts = cv2.findContours(no_tables, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]
            rects = sorted([cv2.boundingRect(cnt) for cnt in cnts], key=lambda r: r[1])

            # Extract texts from each bounding rectangle
            print('\nExtract texts outside of the two tables\n')
            for (x, y, w, h) in rects:
                text = pytesseract.image_to_string(page_3[y:y+h, x:x+w],
                                                config='--psm 6', lang='hin')
                text = text.replace('\n', '').replace('\f', '')
                print('x: {}, y: {}, text: {}'.format(x, y, text))

            # STEP 2: Extract texts from inside of the two tables

            rects = sorted([cv2.boundingRect(cnt) for cnt in cnts_tables],
                        key=lambda r: r[1])

            try:
                # Iterate each table
                for i_r, (x, y, w, h) in enumerate(rects, start=1):

                    # Find bounding rectangles of cells inside of the current table
                    cnts = cv2.findContours(page_3[y+2:y+h-2, x+2:x+w-2],
                                            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
                    inner_rects = sorted([cv2.boundingRect(cnt) for cnt in cnts],
                                        key=lambda r: (r[1], r[0]))

                    # Extract texts from each cell of the current table
                    print('\nExtract texts inside table {}\n'.format(i_r))
                    for (xx, yy, ww, hh) in inner_rects:

                        # Set current coordinates w.r.t. full image
                        xx += x
                        yy += y

                        # Get current cell
                        cell = page_3[yy+2:yy+hh-2, xx+2:xx+ww-2]
                        print(i_r)
                        
                        if i_r == 1:
                            entry=content_extractor(cell,xx,yy)
                            for i in range(len(entry)):
                                row=row+1
                                write_to_sheet(row,entry[i][0],entry[i][1],entry[i][2],entry[i][3],entry[i][4],entry[i][5],sheet,entry[i][6])
                        
                        if i_r == 2:
                            entry=content_extractor(cell,xx,yy)
                            for i in range(len(entry)):
                                row=row+1
                                write_to_sheet(row,entry[i][0],entry[i][1],entry[i][2],entry[i][3],entry[i][4],entry[i][5],sheet,entry[i][6])

                        if i_r == 3:
                            entry=content_extractor(cell,xx,yy)
                            for i in range(len(entry)):
                                row=row+1
                                write_to_sheet(row,entry[i][0],entry[i][1],entry[i][2],entry[i][3],entry[i][4],entry[i][5],sheet,entry[i][6])

                        if i_r == 4:
                            entry=content_extractor(cell,xx,yy)
                            for i in range(len(entry)):
                                row=row+1
                                write_to_sheet(row,entry[i][0],entry[i][1],entry[i][2],entry[i][3],entry[i][4],entry[i][5],sheet,entry[i][6])

                        if i_r == 5:
                            entry=content_extractor(cell,xx,yy)
                            for i in range(len(entry)):
                                row=row+1
                                write_to_sheet(row,entry[i][0],entry[i][1],entry[i][2],entry[i][3],entry[i][4],entry[i][5],sheet,entry[i][6])

                        if i_r == 6:
                            entry=content_extractor(cell,xx,yy)
                            for i in range(len(entry)):
                                row=row+1
                                write_to_sheet(row,entry[i][0],entry[i][1],entry[i][2],entry[i][3],entry[i][4],entry[i][5],sheet,entry[i][6])

                        if i_r == 7:
                            entry=content_extractor(cell,xx,yy)
                            for i in range(len(entry)):
                                row=row+1
                                write_to_sheet(row,entry[i][0],entry[i][1],entry[i][2],entry[i][3],entry[i][4],entry[i][5],sheet,entry[i][6])

                        if i_r == 8:
                            entry=content_extractor(cell,xx,yy)
                            for i in range(len(entry)):
                                row=row+1
                                write_to_sheet(row,entry[i][0],entry[i][1],entry[i][2],entry[i][3],entry[i][4],entry[i][5],sheet,entry[i][6])

                        if i_r == 9:
                            entry=content_extractor(cell,xx,yy)
                            for i in range(len(entry)):
                                row=row+1
                                write_to_sheet(row,entry[i][0],entry[i][1],entry[i][2],entry[i][3],entry[i][4],entry[i][5],sheet,entry[i][6])

                        if i_r == 10:
                            entry=content_extractor(cell,xx,yy)
                            for i in range(len(entry)):
                                row=row+1
                                write_to_sheet(row,entry[i][0],entry[i][1],entry[i][2],entry[i][3],entry[i][4],entry[i][5],sheet,entry[i][6])
            except Exception:
                print(Exception,"Blank Page")

        book.save(filename)




def content_extractor(cell,xx,yy):
    hindi_text = pytesseract.image_to_string(cell, config='--psm 6',
                                    lang='hin')
    print(len(hindi_text),"length")
    hin_text=hindi_text.split('\n')
    print(hin_text)

    english_text = pytesseract.image_to_string(cell, config='--psm 6',
                                        lang='eng')
    # print(english_text)
    # eng_text = english_text.replace('\n', '').replace('\f', '')

    eng_text_new = english_text.replace('\n', '').replace('\f', '')
    # print(eng_text,"outside if")
    blank=[]
    if len(hindi_text)<200:
        name,father_name,mk,age,gender=seperate(hin_text)
        eng=english_text.split("\n")
        un_id=eng[0]
        # gender=extract_data(hindi_text)
        # print(eng_text)
        mkaan_eng=mk_eng(eng_text_new)
        # eng_text=eng_text.split('a')
        # un_id = eng_text[0]
        # un_id=filter_id(un_id)
        entry=[un_id,name,father_name,mk,age,gender,mkaan_eng[0]]
        print(entry,"in 181")
        blank.append(entry)
        return blank
    else:
        print("More than 200 characters")
        count=3
        eng_text=english_text.split(" ")
        # data=struct(te)
        # print(eng_text)
        # un_id_list = []
        # for i in range(3):
        #     un_id_list.append(eng_text[i])
        print(eng_text,"list of unid")
        # detail=triple_entry(hin_text,eng_text)
        detail=trip_ent(hin_text,eng_text,eng_text_new)
        print(detail,"from triple")
        un_id=name=father_name=mk=age=gender=""
        return detail


def triple_entry(x,un_id_list):
    data=struct(x)
    detail=[]
    for i in range(len(data)):
        # print(data[i]["id"])
        print(un_id_list[i])
        print(data[i]["name"])
        print(data[i]["fathername/husbandname"])
        print(data[i]["house_no"])
        try:
            mk=data[i]["house_no"]
            mk=mk.split('शि')
            mk=mk[0]
        except:
            mk=data[i]["house_no"]
        print(data[i]["age"])
        print(data[i]["gender"])
        single_list=[un_id_list[i],data[i]["name"],data[i]["fathername/husbandname"],mk,data[i]["age"],data[i]["gender"]]
        detail.append(single_list)

    return detail

# path='/home/hs/AI projects/Testing5/pdfs/UP1.pdf'
# directory_path, filename = path.rsplit('/', 1)
# filename=filename.replace("pdf","xls")
# print(filename)
# main(path,filename)

