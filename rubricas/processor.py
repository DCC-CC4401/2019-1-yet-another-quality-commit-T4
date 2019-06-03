import csv
import os
from rubricas.models import Rubrica as R

def make(p):
    nombre = p['0,0']
    count = R.objects.filter(nombre=nombre).count()
    if(count>0):
        nombre=nombre+"("+str(count)+")"
    duration_min = int(p['min_duration'])
    duration_max = int(p['max_duration'])
    print(duration_min,duration_max)
    path = 'rubricas/storage/'+nombre.replace(" ","")+".csv"
    r = R(nombre=nombre, durationMin=duration_min, durationMax=duration_max, Directory=path)
    r.save()

    keys = p.keys()
    aux = []
    for key in keys:
        aux.append(key)

    n_rows = int(p['n_rows']) #int(aux[-1].split(",")[0]) + 1
    n_collumns = int(p['n_cols']) #int(aux[-1].split(",")[1]) + 1

    list = []
    for i in range(n_rows):
        row = []
        for j in range(n_collumns):
            row.append(p[str(i) + "," + str(j)])
        list.append(row)

    print(list)
    with open(path, 'w', newline='') as file:
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        # wr.writerow([p['0,0'],p['0,1'],p['0,2']])
        for list_row in list:
            wr.writerow(list_row)

def readCSV(o : R):
    path = o.get_path()
    l = []
    with open(path,'r') as f:
        r = csv.reader(f)
        for row in r:
            l.append(row)
    return l

def justMakeFile(p):
    keys = p.keys()
    aux = []
    for key in keys:
        aux.append(key)

    n_rows = int(p['n_rows']) #int(aux[-1].split(",")[0]) + 1
    n_collumns = int(p['n_cols']) #int(aux[-1].split(",")[1]) + 1

    nombre = str(p['0,0'])
    r = R.objects.filter(nombre=nombre).first()
    path = r.get_path()
    list = []
    for i in range(n_rows):
        row = []
        for j in range(n_collumns):
            row.append(p[str(i) + "," + str(j)])
        list.append(row)

    print(list)
    with open(path, 'w', newline='') as file:
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        # wr.writerow([p['0,0'],p['0,1'],p['0,2']])
        for list_row in list:
            print(list_row)
            wr.writerow(list_row)

