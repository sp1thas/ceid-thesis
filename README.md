#Feature extraction for text categorization
##Geolocation authorship attribution

**more infos at main.py**


---
###Prerequirements:

* **[Python 2.7](https://www.python.org/)**

* **[NLTK](http://www.nltk.org/install.html)**

    - RegexpTokenizer

    - nltk.data

  

* Python Modules

    - [arff](https://pypi.python.org/pypi/arff)

    - [decodes](https://pypi.python.org/pypi/decodes)

    - [unicodecsv](https://pypi.python.org/pypi/unicodecsv)

    - Installation:

          `[sudo] pip install arff decodes unicodecsv`
---

### Input .csv file template:
![](https://raw.githubusercontent.com/sp1thas/geo-nltk-feature/master/csv-template.png)


####Text ID:
- unique id for each text

####Author's gender:
- "M" for Male
- "F" for Female

####Author's age category:
- A: 14-19
- B: 20-24
- C: 25-34
- D: 35-44
- E: 45-59
- F: >60

####Author's exact age:
- >14

####Social Media:
- Facebook/Twitter

####Author's thematic area:
Based on facebook page categories etc
- Actor/Director
- Artist
- Athlete
- Author
- Business Person
- Chef
- Coach
- Doctor
- Entertainer
- Journalist
- Lawyer
- Musician/Band
- Politician
- Teacher
- Writer

####Other infos
- anything else about the author
