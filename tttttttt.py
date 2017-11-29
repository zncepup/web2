def month2year(string):
    strnyr=''
    m=float(string)
    year=m//12.0
    print(year)
    if year!=0:
        strnyr=str(int(year))+'年'
    month=m%12.0
    if int(month)!=0:
        strnyr = strnyr + str(int(month)) + '个月'
    day=month-int(month)
    day=day*30
    day=round(day)
    if day!=0:
        strnyr=strnyr+str(day)+'天'
    return strnyr
if __name__ == '__main__':
    a=month2year('7')
    print(a)
