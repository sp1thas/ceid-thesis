# synarthsh h opoia epistrefei to pososto tou keimenou pou emperiexei tis lekseis
# ths listas pou dinw ws orisma
def NationalCommonsPerDoc(text_nation, string_list):
    counter = 0.00
    for j in string_list:
        counter += text_nation.count(j)
    if counter!=0:
        return format(counter/float(len(text_nation)), '.3f')
    else:
        return 0.00
