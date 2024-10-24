import csv,json
#csv_file = open('compile.csv', 'w', newline='')
totalv=0
totalc=0
#fw = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
for i in range(275):
    try:
        with open(str(i+1)+'.txt',"r") as f:
            d=json.load(f)
            r=d['records']
            for i in r:
                totalv=totalv+i['vote_count']
                if(i['vote_count']>1):
                    totalc=totalc+int(i['vote_count'])*5
                    #fw.writerow([i["contestant"]["name"],i['vote_count']])#,i['created_on']]),i["contest"],
    except:
        pass

print(totalv,totalc,totalc/totalv)
#csv_file.close()
