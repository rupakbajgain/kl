import csv,json
c={}
total=[0,0]
csv_file = open('count_alt.csv', 'w', newline='')
fw = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
fw.writerow(['Name','Free','Paid','Total','Paid(Rs.)'])
for i in range(275):
    try:
        with open(str(i+1)+'.txt',"r") as f:
            d=json.load(f)
            r=d['records']
            for i in r:
                if(True):
                    if(not c.get(i["contestant"]["name"]+i["contest"])):
                       c[i["contestant"]["name"]+i["contest"]]=[0,0]
                    if(i['vote_count']==1):
                        c[i["contestant"]["name"]+i["contest"]][0]=c[i["contestant"]["name"]+i["contest"]][0]+int(i['vote_count'])
                        total[0]=total[0]+int(i['vote_count'])
                    else:
                        c[i["contestant"]["name"]+i["contest"]][1]=c[i["contestant"]["name"]+i["contest"]][1]+int(i['vote_count'])
                        total[1]=total[1]+int(i['vote_count'])
                    #print(c[i["contestant"]["name"]])
                #if(i['vote_count']>1):
                #    fw.writerow([i["contestant"]["name"],i['vote_count']])#,i['created_on']]),i["contest"],
    except UnicodeDecodeError:
        pass

for i in c:
    fw.writerow([i,c[i][0],c[i][1],c[i][0]+c[i][1],c[i][1]*5])
fw.writerow(["Total",total[0],total[1],total[0]+total[1],total[1]*5])
csv_file.close()
