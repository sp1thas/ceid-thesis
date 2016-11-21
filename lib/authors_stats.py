# -*- coding: utf-8 -*-
import unicodecsv as csv

DefaultFile = "out2.csv"
print "Default csv file: 'out2.csv' (Press Enter for default csv file)"
csvFile = raw_input("Insert csv file name: ") or DefaultFile #eisagwgh onomatos arxeiou

textFile = csv.reader(open(csvFile,"rb")) # anoigma to dataset csv
counter = 0
Male_Authors = 0
Gender_Author = {}
Gender_Author['Male'] = 0
Gender_Author['Female'] = 0
Genders = Gender_Author.keys()
Social_Author = {}
Social_Author['Facebook'] = 0
Social_Author['Twitter'] = 0
Socials = Social_Author.keys()
Thematic_Author = {}
Thematic_Author['Actor/Director'] = Thematic_Author['Artist'] = Thematic_Author['Athlete'] = Thematic_Author['Author'] = Thematic_Author['Chef'] = Thematic_Author['Comedian'] = Thematic_Author['Designer'] = Thematic_Author['Entertainer'] = Thematic_Author['Fashion'] = Thematic_Author['Music']=Thematic_Author['Musician/Band']=Thematic_Author['News Personality']=Thematic_Author['Politician']=Thematic_Author['Public Figure']=Thematic_Author['Scientist']=Thematic_Author['Teacher']=Thematic_Author['Teacher/scientist']= 0
AgeCat_Author = {}
AgeCat_Author['A'] = AgeCat_Author['B'] = AgeCat_Author['C'] = AgeCat_Author['D'] = AgeCat_Author['E'] = AgeCat_Author['F'] = 0
AuthorsLang = {}
AuthorsLang['US'] = AuthorsLang['AUS'] = AuthorsLang['CAN'] = AuthorsLang['NNS'] = AuthorsLang['UK'] = 0
for row in textFile:
    if counter == 0:
        tmp = row
        counter += 1
        Authors = 1
    elif tmp[2]!=row[2] or tmp[3]!=row[3] or tmp[4]!=row[4] or tmp[5] != row[5] or tmp[6] != row[6] or tmp[7] != row[7]:
        counter += 1
        Authors += 1
        if tmp[2]=='M':
            Gender_Author['Male'] += 1
        else:
            Gender_Author['Female'] += 1
        if tmp[5] == 'Facebook':
            Social_Author['Facebook'] += 1
        if tmp[5] == 'Twitter':
            Social_Author['Twitter'] += 1
        ##########################
        if tmp[6] == 'Actor/Director':
            Thematic_Author['Actor/Director'] +=1
        elif tmp[6] == 'Artist':
            Thematic_Author['Artist']+=1
        elif tmp[6] == 'Athlete':
            Thematic_Author['Athlete']+=1
        elif tmp[6] == 'Author':
            Thematic_Author['Author']+=1
        elif tmp[6] == 'Chef':
            Thematic_Author['Chef']+=1
        elif tmp[6] == 'Comedian':
            Thematic_Author['Comedian']+=1
        elif tmp[6] == 'Designer':
            Thematic_Author['Designer']+=1
        elif tmp[6] == 'Entertainer':
            Thematic_Author['Entertainer']+=1
        elif tmp[6] == 'Fashion':
            Thematic_Author['Fashion']+=1
        elif tmp[6] == 'Music':
            Thematic_Author['Music']+=1
        elif tmp[6] == 'Musician/Band':
            Thematic_Author['Musician/Band']+=1
        elif tmp[6] == 'News Personality':
            Thematic_Author['News Personality']+=1
        elif tmp[6] == 'Politician':
            Thematic_Author['Politician']+=1
        elif tmp[6] == 'Public Figure':
            Thematic_Author['Public Figure']+=1
        elif tmp[6] == 'Scientist':
            Thematic_Author['Scientist']+=1
        elif tmp[6] == 'Teacher':
            Thematic_Author['Teacher']+=1
        elif tmp[6] == 'Teacher/scientist':
            Thematic_Author['Teacher/scientist']+=1
        else:
            pass
        ###############################################
        if tmp[3] == 'A':
            AgeCat_Author['A']+=1
        elif tmp[3] == 'B':
            AgeCat_Author['B']+=1
        elif tmp[3] == 'C':
            AgeCat_Author['C']+=1
        elif tmp[3] == 'D':
            AgeCat_Author['D']+=1
        elif tmp[3] == 'E':
            AgeCat_Author['E']+=1
        elif tmp[3] == 'F':
            AgeCat_Author['F']+=1
        #############################################
        if tmp[7]=='US' or tmp[7]=='US ':
            AuthorsLang['US']+=1
        elif tmp[7]=='UK':
            AuthorsLang['UK']+=1
        elif tmp[7]=='CAN':
            AuthorsLang['CAN']+=1
        elif tmp[7]=='NNS':
            AuthorsLang['NNS']+=1
        elif tmp[7]=='AUS':
            AuthorsLang['AUS']+=1
        #############################################

        tmp = row
print 'Number of Authors: ',Authors
print 'Male Authors: ', Gender_Author['Male']
print 'Female Authors: ', Gender_Author['Female']
print 'Facebook Authors: ', Social_Author['Facebook']
print 'Twitter Authors: ', Social_Author['Twitter']
print '------------------------------------'
print 'Thematic Area'
for i in Thematic_Author:
    print i,': ',Thematic_Author[i]
print '------------------------------------'
print "Author's age category"
for j in AgeCat_Author:
    print j,': ',AgeCat_Author[j]
print '------------------------------------'
print "AUthor's language"
for l in AuthorsLang:
    print l,': ',AuthorsLang[l]
