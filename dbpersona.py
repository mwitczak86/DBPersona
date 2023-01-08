#Copyright 2022 Michal Witczak

#Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

#THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

#!/usr/bin/python3

import random
import os
import csv
import calendar
from configparser import ConfigParser

students_var = input("How many people you want to create? ")
usr_input = int(students_var) + 1
print("Wait...")
#Read config file (path to files)
config_obj = ConfigParser()
config_obj.read("dbpersona_config.ini")
user_info = config_obj["USERINFO"]
npath = user_info["names_wordlist_path"]
lpath = user_info["last_names_wordlist_path"]
dpath = user_info["dbpersona_data_path"]

names = open(os.path.abspath(npath)).read().splitlines()
lastnames = open(os.path.abspath(lpath)).read().splitlines()
data = open(os.path.abspath(dpath),'w')
writer = csv.writer(data)
#students book number
album = random.sample(range(2000, (3000+usr_input)),usr_input)
record_count = 0

for n in range(usr_input):
    
    if n < (usr_input - 1):
        
        pesel_list = []
        nameline = random.choice(names)
        lastnamesline = random.choice(lastnames)
        lchar_name = nameline[-1]
        lchars_last = lastnamesline[-3:]
        #birth year range
        birthy = random.choice(range(1960,2004))
        #birth month
        birthym = random.choice(range(1,12))
        #day of month
        birthyd = 0
        stalbum = str(album[n+1])

#pesel specific numbers
        #polish pesel gender number (odd number is for male, even – for female)
        psl_k = [0,2,4,6,8]
        psl_m = [1,3,5,7,9]
        psl_range = random.choice(range(0,999))
        


#birthday day of the month
        if (birthym % 2) != 0:
            birthyd = random.choice(range(1,31))
            
        
        elif (((birthym % 2) == 0) & (birthym != 2)):
            birthyd = random.choice(range(1,30))
            

        elif ((birthym == 2) & (calendar.isleap(birthy))):
            birthyd = random.choice(range(1,29))
           
        
        else:
            birthyd = random.choice(range(1,28))
            

        psl_full_y = str(birthy)
        psl_y = int(psl_full_y[-2:])
        psl_y1 = int(psl_full_y[-2])
        psl_y2 = int(psl_full_y[-1])

#add pesel numbers to list
        if birthy < 2000:
            
            pesel_list.append(psl_y1)
            pesel_list.append(psl_y2)
            
                
            if birthym < 10:
                pesel_list.append(0)
                pesel_list.append(birthym)
            else:
                psl_full_m = str(birthym)
                psl_m1 = int(psl_full_m[0])
                psl_m2 = int(psl_full_m[1])
                pesel_list.append(psl_m1)
                pesel_list.append(psl_m2)
        
        else:
            
            pesel_list.append(psl_y1)
            pesel_list.append(psl_y2)
            
                
            brithym21st = birthym + 20
            brithym21st_string = str(brithym21st)
            brithym21st_a = brithym21st_string[0]
            brithym21st_b = brithym21st_string[1]
            pesel_list.append(int(brithym21st_a))
            pesel_list.append(int(brithym21st_b))



        if birthyd < 10:
            pesel_list.append(0)
            pesel_list.append(birthyd)
        else:
            psl_full_d = str(birthyd)
            psl_d1 = int(psl_full_d[0])
            psl_d2 = int(psl_full_d[1])
            pesel_list.append(psl_d1)
            pesel_list.append(psl_d2)

        if psl_range < 10:
           pesel_list.append(0)
           pesel_list.append(0)
           pesel_list.append(psl_range)
        elif (psl_range >= 10) & (psl_range < 100):
            
            psl_range_full = str(psl_range)
            psl_range2 = int(psl_range_full[-2])
            psl_range3 = int(psl_range_full[-1])
            pesel_list.append(0)
            pesel_list.append(psl_range2)
            pesel_list.append(psl_range3)
           
        else:
            psl_range_full = str(psl_range)
            psl_range1 = int(psl_range_full[-3])
            psl_range2 = int(psl_range_full[-2])
            psl_range3 = int(psl_range_full[-1])
            pesel_list.append(psl_range1)
            pesel_list.append(psl_range2)
            pesel_list.append(psl_range3)

    

        if lchar_name == 'a':
            pesel_list.append(random.choice(psl_k))
        else:
            pesel_list.append(random.choice(psl_m))





        #print(pesel_list)

        pesel_mult = []
        pesel_mult.append(pesel_list[0] * 1)
        pesel_mult.append(pesel_list[1] * 3)
        pesel_mult.append(pesel_list[2] * 7)
        pesel_mult.append(pesel_list[3] * 9)
        pesel_mult.append(pesel_list[4] * 1)
        pesel_mult.append(pesel_list[5] * 3)
        pesel_mult.append(pesel_list[6] * 7)
        pesel_mult.append(pesel_list[7] * 9)
        pesel_mult.append(pesel_list[8] * 1)
        pesel_mult.append(pesel_list[9] * 3)

        pesel_check = []

          

        #print(pesel_mult)
        for n in pesel_mult:
            if n < 10:
                pesel_check.append(n)
            else:
                n_string = str(n)
                n_split = n_string[1]
                if int(n_split) != 0:
                    pesel_check.append(int(n_split))
                else: 
                    pesel_check.append(0)
        

        #print(pesel_check)

        pesel_check_sum = sum(pesel_check)

        #print(pesel_check_sum)

        pcs_string = str(pesel_check_sum)
        pcs_v = pcs_string[-1]
        pcs_sum = (10 - (int(pcs_v)))
        pcs_sum_string = str(pcs_sum)
        pcs_sum_last = int(pcs_sum_string[-1])
        if pcs_sum > 0:
            pesel_list.append(int(pcs_sum_last))
        else:
            pesel_list.append(0)

        

        

        pesel_joined = ''.join(map(str, pesel_list))
        pesel = str(pesel_joined)

        


        if birthym < 10:
            b1 = '0'
            birthym_string = b1+str(birthym)
        else:
            birthym_string = str(birthym)
        
        birthdate = str(birthy) + '-' + birthym_string + '-' + str(birthyd)
        domain = ['gmail.com','o2.pl','wp.pl','interia.pl']
        #faculties list (could be changed to job titles)
        faculty = ['Wydzial Zarzadzania','Wydzial Biznesu','Wydzial Informatyki', 'Wydzial Historii', 'Wydzial Nauk Spolecznych']


        email = nameline[0].lower() + lastnamesline.lower() +'@'+(random.choice(domain))
        rfaculty = random.choice(faculty)

        
       
        #removeAccents credits to Igor Zubrycki
        strange='ŮôῡΒძěἊἦëĐᾇόἶἧзвŅῑἼźἓŉἐÿἈΌἢὶЁϋυŕŽŎŃğûλВὦėἜŤŨîᾪĝžἙâᾣÚκὔჯᾏᾢĠфĞὝŲŊŁČῐЙῤŌὭŏყἀхῦЧĎὍОуνἱῺèᾒῘᾘὨШūლἚύсÁóĒἍŷöὄЗὤἥბĔõὅῥŋБщἝξĢюᾫაπჟῸდΓÕűřἅгἰშΨńģὌΥÒᾬÏἴქὀῖὣᾙῶŠὟὁἵÖἕΕῨčᾈķЭτἻůᾕἫжΩᾶŇᾁἣჩαἄἹΖеУŹἃἠᾞåᾄГΠКíōĪὮϊὂᾱიżŦИὙἮὖÛĮἳφᾖἋΎΰῩŚἷРῈĲἁéὃσňİΙῠΚĸὛΪᾝᾯψÄᾭêὠÀღЫĩĈμΆᾌἨÑἑïოĵÃŒŸζჭᾼőΣŻçųøΤΑËņĭῙŘАдὗპŰἤცᾓήἯΐÎეὊὼΘЖᾜὢĚἩħĂыῳὧďТΗἺĬὰὡὬὫÇЩᾧñῢĻᾅÆßшδòÂчῌᾃΉᾑΦÍīМƒÜἒĴἿťᾴĶÊΊȘῃΟúχΔὋŴćŔῴῆЦЮΝΛῪŢὯнῬũãáἽĕᾗნᾳἆᾥйᾡὒსᾎĆрĀüСὕÅýფᾺῲšŵкἎἇὑЛვёἂΏθĘэᾋΧĉᾐĤὐὴιăąäὺÈФĺῇἘſგŜæῼῄĊἏØÉПяწДĿᾮἭĜХῂᾦωთĦлðὩზკίᾂᾆἪпἸиᾠώᾀŪāоÙἉἾρаđἌΞļÔβĖÝᾔĨНŀęᾤÓцЕĽŞὈÞუтΈέıàᾍἛśìŶŬȚĳῧῊᾟάεŖᾨᾉςΡმᾊᾸįᾚὥηᾛġÐὓłγľмþᾹἲἔбċῗჰხοἬŗŐἡὲῷῚΫŭᾩὸùᾷĹēრЯĄὉὪῒᾲΜᾰÌœĥტ'
        ascii_replacements='UoyBdeAieDaoiiZVNiIzeneyAOiiEyyrZONgulVoeETUiOgzEaoUkyjAoGFGYUNLCiIrOOoqaKyCDOOUniOeiIIOSulEySAoEAyooZoibEoornBSEkGYOapzOdGOuraGisPngOYOOIikoioIoSYoiOeEYcAkEtIuiIZOaNaicaaIZEUZaiIaaGPKioIOioaizTIYIyUIifiAYyYSiREIaeosnIIyKkYIIOpAOeoAgYiCmAAINeiojAOYzcAoSZcuoTAEniIRADypUitiiIiIeOoTZIoEIhAYoodTIIIaoOOCSonyKaAsSdoACIaIiFIiMfUeJItaKEISiOuxDOWcRoiTYNLYTONRuaaIeinaaoIoysACRAuSyAypAoswKAayLvEaOtEEAXciHyiiaaayEFliEsgSaOiCAOEPYtDKOIGKiootHLdOzkiaaIPIIooaUaOUAIrAdAKlObEYiINleoOTEKSOTuTEeiaAEsiYUTiyIIaeROAsRmAAiIoiIgDylglMtAieBcihkoIrOieoIYuOouaKerYAOOiaMaIoht'
        translator=str.maketrans(strange,ascii_replacements)
        #script src="https://gist.github.com/AdoHaha/a76157c6de5155bf6b0adc77988724d9.js"

        
    
    
             



        #polish names logic (Adjectival surnames, like all Polish adjectives, have masculine and feminine forms)
       
        if (lchar_name == 'a') & (lchars_last == 'ski'):
            replacement = 'ska'
            lastnamesline = lastnamesline.replace(lastnamesline[-3:], replacement)
            lndecode = lastnamesline.translate(translator)
            fndecode = nameline.translate(translator)
            email = fndecode[0].lower() + lndecode.lower() + str(random.choice(stalbum)) + str(random.choice(stalbum)) + str(stalbum) +'@'+(random.choice(domain))

            
            #write row to data.csv file
            row = []
            row.extend((nameline,lastnamesline,birthdate,pesel,email,stalbum,rfaculty))
            #print(row)
            writer.writerow(row)
            record_count = record_count + 1
            #print('\n')
        elif (lchar_name == 'a') & (lchars_last == 'dzki'):
            replacement = 'dzka'
            lastnamesline = lastnamesline.replace(lastnamesline[-3:], replacement)
            lndecode = lastnamesline.translate(translator)
            fndecode = nameline.translate(translator)
            email = fndecode[0].lower() + lndecode.lower() + str(random.choice(stalbum)) + str(random.choice(stalbum)) + str(stalbum) +'@'+(random.choice(domain))
            
            
            #write row to data.csv file
            row = []
            row.extend((nameline,lastnamesline,birthdate,pesel,email,stalbum,rfaculty))
            #print(row)
            writer.writerow(row)
            #print('\n')
            record_count = record_count + 1

        elif (lchar_name == 'a') & (lchars_last == 'cki'):
            replacement = 'cka'
            lastnamesline = lastnamesline.replace(lastnamesline[-3:], replacement)
            lndecode = lastnamesline.translate(translator)
            fndecode = nameline.translate(translator)
            email = fndecode[0].lower() + lndecode.lower() + str(random.choice(stalbum)) + str(random.choice(stalbum)) + str(stalbum) +'@'+(random.choice(domain))
            
           
            #write row to data.csv file
            row = []
            row.extend((nameline,lastnamesline,birthdate,pesel,email,stalbum,rfaculty))
            #print(row)
            writer.writerow(row)
            #print('\n')
            record_count = record_count + 1

        else:
            lndecode = lastnamesline.translate(translator)
            fndecode = nameline.translate(translator)
            email = fndecode[0].lower() + lndecode.lower() + str(random.choice(stalbum)) + str(random.choice(stalbum)) + str(stalbum) +'@'+(random.choice(domain))

           
            
            #write row to data.csv file
            row = []
            row.extend((nameline,lastnamesline,birthdate,pesel,email,stalbum,rfaculty))
            #print(row)
            writer.writerow(row)
            #print('\n')
            record_count = record_count + 1

print(str(record_count) +" people successfully created!")


       