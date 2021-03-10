import csv
# Открыть файл
hiscore = [['we',100],['qwer',200],['we',50]]

'''
with open('urls.txt', 'w', newline='') as file:
    csv.writer(file).writerows(hiscore)   # write rows


with open('urls.txt', newline='') as file:
    rows = list(csv.reader(file))      # read rows
print (rows)
'''


def write_score ():
    # Открываем  файл и записываем двумерный массив
    with  open("andreyex.txt", "w+") as f :
        for i in range(len(hiscore)):
            f.writelines(' '.join(map(str,hiscore[i])))
            f.writelines('\n')

def read_score ():
    hiscore2=[]
    # Открываем и читаем файл  список
    with  open("andreyex.txt", "r") as f :
            for line in f:
                hiscore2.append(line.rstrip().split(','))

            print (hiscore2)
read_score ()


