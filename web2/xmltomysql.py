#coding=utf-8
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","web2.settings")
django.setup()
import  xml.dom.minidom
from jiaotongzhaoshi.models import jiaotongzhaoshi
from weixianjiashi.models import weixianjiashi


dir=r'F:\xml\jtzs/'
list=os.listdir(dir)
for i in range(0,len(list)):
    path = os.path.join(dir,list[i])
    if os.path.isfile(path):
        if i>6770:
            print(list[i],i)
            dom = xml.dom.minidom.parse(path)
            AwardID = dom.getElementsByTagName('AwardID')[0].firstChild.data
            IndictmentID = dom.getElementsByTagName('IndictmentID')[0].firstChild.data
            Province = dom.getElementsByTagName('Province')[0].firstChild == None and 'unknown' or \
                       dom.getElementsByTagName('Province')[0].firstChild.data
            City = dom.getElementsByTagName('City')[0].firstChild == None and 'unknown' or \
                   dom.getElementsByTagName('City')[0].firstChild.data
            CountyDistrict = dom.getElementsByTagName('CountyDistrict')[0].firstChild == None and 'unknown' or \
                             dom.getElementsByTagName('CountyDistrict')[0].firstChild.data
            TrialTime = dom.getElementsByTagName('TrialTime')[0].firstChild.data
            Judge = dom.getElementsByTagName('Judge')[0].firstChild.data  # 很长
            Status = dom.getElementsByTagName('Status')[0].firstChild.data
            EducationalBackground = dom.getElementsByTagName('EducationalBackground')[0].firstChild.data
            IncidentAge = dom.getElementsByTagName('IncidentAge')[0].firstChild.data
            Birthday = dom.getElementsByTagName('Birthday')[0].firstChild == None and 'unknown' or \
                       dom.getElementsByTagName('Birthday')[0].firstChild.data
            EducationalBackground = dom.getElementsByTagName('EducationalBackground')[0].firstChild.data

            leifan = dom.getElementsByTagName('Pedigree')[0].getAttribute("累犯")
            qianke = dom.getElementsByTagName('Pedigree')[0].getAttribute("前科")
            renzui = dom.getElementsByTagName('Attitude')[0].getAttribute("认罪")
            zishou = dom.getElementsByTagName('Attitude')[0].getAttribute("自首")
            ligong = dom.getElementsByTagName('Attitude')[0].getAttribute("立功")
            tanbai = dom.getElementsByTagName('Attitude')[0].getAttribute("坦白")
            huizui = dom.getElementsByTagName('Attitude')[0].getAttribute("悔罪")
            feijidongche = dom.getElementsByTagName('Vehicle')[0].getAttribute("非机动车")
            jiaoche = dom.getElementsByTagName('Vehicle')[0].getAttribute("轿车")
            huoche = dom.getElementsByTagName('Vehicle')[0].getAttribute("货车")
            diandongchejidong = dom.getElementsByTagName('Vehicle')[0].getAttribute("电动车-机动")
            motuoche = dom.getElementsByTagName('Vehicle')[0].getAttribute("摩托车")
            baofeiche = dom.getElementsByTagName('Vehicle')[0].getAttribute("报废车")
            keche = dom.getElementsByTagName('Vehicle')[0].getAttribute("客车")
            taopaiche = dom.getElementsByTagName('Vehicle')[0].getAttribute("套牌车")
            qitajidongcheliang = dom.getElementsByTagName('Vehicle')[0].getAttribute("其他机动车辆")
            wuzhengjiashi = dom.getElementsByTagName('Plot')[0].getAttribute("无证驾驶")
            wupaijiashi = dom.getElementsByTagName('Plot')[0].getAttribute("无牌驾驶")
            DrunkDriving = dom.getElementsByTagName('DrunkDriving')[0].getAttribute("酒驾")
            Alcohol = dom.getElementsByTagName('Alcohol')[0].getAttribute("酒精含量")
            OverSpeed = dom.getElementsByTagName('OverSpeed')[0].firstChild.data
            OverLoad = dom.getElementsByTagName('OverLoad')[0].firstChild.data
            SurveillansDuration = dom.getElementsByTagName('SurveillansDuration')[0].firstChild.data.split('/')[0]
            SurveillansDuration_huanxing = \
            dom.getElementsByTagName('SurveillansDuration')[0].firstChild.data.split('/')[1]
            DententionDuration = dom.getElementsByTagName('DententionDuration')[0].firstChild.data.split('/')[0]
            DententionDuration_huanxing = dom.getElementsByTagName('DententionDuration')[0].firstChild.data.split('/')[
                1]
            FixtedTermDuration = dom.getElementsByTagName('FixtedTermDuration')[0].firstChild.data.split('/')[0]
            FixtedTermDuration_huanxing = dom.getElementsByTagName('FixtedTermDuration')[0].firstChild.data.split('/')[
                1]
            Amount = dom.getElementsByTagName('Amount')[0].firstChild.data

            DeathNum = dom.getElementsByTagName('DeathNum')[0].firstChild.data
            InjuredNum = dom.getElementsByTagName('InjuredNum')[0].firstChild.data
            DegreeOfPropertyLosses = dom.getElementsByTagName('DegreeOfPropertyLosses')[0].firstChild.data
            AmountOfCompensation = dom.getElementsByTagName('AmountOfCompensation')[0].firstChild.data
            VictimUnderstanding = dom.getElementsByTagName('VictimUnderstanding')[0].firstChild.data
            confirmationOfResponsibility = dom.getElementsByTagName('confirmationOfResponsibility')[0].firstChild.data
            Abscond = dom.getElementsByTagName('Abscond')[0].firstChild.data
            DeathCausedByAbscond = dom.getElementsByTagName('DeathCausedByAbscond')[0].firstChild.data



            jiaotongzhaoshi.objects.get_or_create(id=i + 1, filename=list[i],AwardID=AwardID,IndictmentID=IndictmentID
                                                  ,TrialTime=TrialTime
                                                  ,Judge=Judge
                                                  ,Province=Province
                                                  ,City=City
                                                  ,CountyDistrict=CountyDistrict
                                                  ,status=Status
                                                  ,IncidentAge=IncidentAge
                                                  ,EducationalBackground=EducationalBackground
                                                  ,pedigree=qianke
                                                  ,recividist=leifan
                                                  ,zishou=zishou
                                                  ,tanbai=tanbai
                                                  ,ligong=ligong
                                                  ,renzui=renzui
                                                  ,huizui=huizui
                                                  ,keche=keche
                                                  ,motuoche=motuoche
                                                  ,huoche=huoche
                                                  ,jiaoche=jiaoche
                                                  ,diandongchejidong=diandongchejidong
                                                  ,baofeiche=baofeiche
                                                  ,taopaiche=taopaiche
                                                  ,qitajidongcheliang=qitajidongcheliang
                                                  ,feijidongche=feijidongche
                                                  ,jiujia=DrunkDriving
                                                  ,OverSpeed=OverSpeed
                                                  ,OverLoad=OverLoad
                                                  ,Alcohol=Alcohol,
                                                  Surveillans=SurveillansDuration,
                                                  Dentention=DententionDuration,
                                                  FixtedTerm=FixtedTermDuration,
                                                  Surveillans_huanxing=SurveillansDuration_huanxing,
                                                  Dentention_huanxing=DententionDuration_huanxing,
                                                  FixtedTerm_huanxing=FixtedTermDuration_huanxing,
                                                  Fine=Amount,
            #
            #
                                                  DeathNum=DeathNum,
                                                  InjuredNum=InjuredNum,
                                                  DegreeOfPropertyLosses=DegreeOfPropertyLosses,
                                                  AmountOfCompensation=AmountOfCompensation,
                                                  VictimUnderstanding=VictimUnderstanding,
                                                  confirmationOfResponsibility=confirmationOfResponsibility,
                                                  Abscond=Abscond,
                                                  DeathCausedByAbscond=DeathCausedByAbscond
                                                  )

# def readxml(path):
#     dom = xml.dom.minidom.parse(path)
#     AwardID = dom.getElementsByTagName('AwardID')[0].firstChild.data
#     IndictmentID = dom.getElementsByTagName('IndictmentID')[0].firstChild.data
#     Province = dom.getElementsByTagName('Province')[0].firstChild==None and 'unknown' or dom.getElementsByTagName('Province')[0].firstChild.data
#     City = dom.getElementsByTagName('City')[0].firstChild == None and 'unknown' or \
#                dom.getElementsByTagName('City')[0].firstChild.data
#     CountyDistrict = dom.getElementsByTagName('CountyDistrict')[0].firstChild == None and 'unknown' or \
#                dom.getElementsByTagName('CountyDistrict')[0].firstChild.data
#     TrialTime = dom.getElementsByTagName('TrialTime')[0].firstChild.data
#     Judge = dom.getElementsByTagName('Judge')[0].firstChild.data    #很长
#     Status = dom.getElementsByTagName('Status')[0].firstChild.data
#     EducationalBackground = dom.getElementsByTagName('EducationalBackground')[0].firstChild.data
#     IncidentAge= dom.getElementsByTagName('IncidentAge')[0].firstChild.data
#     Birthday = dom.getElementsByTagName('Birthday')[0].firstChild==None and 'unknown' or dom.getElementsByTagName('Birthday')[0].firstChild.data
#     EducationalBackground = dom.getElementsByTagName('EducationalBackground')[0].firstChild.data
#
#     leifan=dom.getElementsByTagName('Pedigree')[0].getAttribute("累犯")
#     qianke = dom.getElementsByTagName('Pedigree')[0].getAttribute("前科")
#     renzui = dom.getElementsByTagName('Attitude')[0].getAttribute("认罪")
#     zishou = dom.getElementsByTagName('Attitude')[0].getAttribute("自首")
#     ligong = dom.getElementsByTagName('Attitude')[0].getAttribute("立功")
#     tanbai = dom.getElementsByTagName('Attitude')[0].getAttribute("坦白")
#     huizui = dom.getElementsByTagName('Attitude')[0].getAttribute("悔罪")
#     feijidongche = dom.getElementsByTagName('Vehicle')[0].getAttribute("非机动车")
#     jiaoche = dom.getElementsByTagName('Vehicle')[0].getAttribute("轿车")
#     huoche = dom.getElementsByTagName('Vehicle')[0].getAttribute("货车")
#     diandongchejidong = dom.getElementsByTagName('Vehicle')[0].getAttribute("电动车机动")
#     motuoche = dom.getElementsByTagName('Vehicle')[0].getAttribute("摩托车")
#     baofeiche = dom.getElementsByTagName('Vehicle')[0].getAttribute("报废车")
#     keche = dom.getElementsByTagName('Vehicle')[0].getAttribute("客车")
#     taopaiche = dom.getElementsByTagName('Vehicle')[0].getAttribute("套牌车")
#     qitajidongcheliang = dom.getElementsByTagName('Vehicle')[0].getAttribute("其他机动车辆")
#     wuzhengjiashi = dom.getElementsByTagName('Plot')[0].getAttribute("无证驾驶")
#     wupaijiashi = dom.getElementsByTagName('Plot')[0].getAttribute("无牌驾驶")
#     DrunkDriving= dom.getElementsByTagName('DrunkDriving')[0].getAttribute("酒驾")
#     Alcohol= dom.getElementsByTagName('Alcohol')[0].getAttribute("酒精含量")
#     OverSpeed = dom.getElementsByTagName('OverSpeed')[0].firstChild.data
#     OverLoad = dom.getElementsByTagName('OverLoad')[0].firstChild.data
#     SurveillansDuration = dom.getElementsByTagName('SurveillansDuration')[0].firstChild.data.split('/')[0]
#     SurveillansDuration_huanxing = dom.getElementsByTagName('SurveillansDuration')[0].firstChild.data.split('/')[1]
#     DententionDuration = dom.getElementsByTagName('DententionDuration')[0].firstChild.data.split('/')[0]
#     DententionDuration_huanxing = dom.getElementsByTagName('DententionDuration')[0].firstChild.data.split('/')[1]
#     FixtedTermDuration = dom.getElementsByTagName('FixtedTermDuration')[0].firstChild.data.split('/')[0]
#     FixtedTermDuration_huanxing = dom.getElementsByTagName('FixtedTermDuration')[0].firstChild.data.split('/')[1]
#     Amount = dom.getElementsByTagName('Amount')[0].firstChild.data
#
#     DeathNum = dom.getElementsByTagName('DeathNum')[0].firstChild.data
#     InjuredNum = dom.getElementsByTagName('InjuredNum')[0].firstChild.data
#     DegreeOfPropertyLosses = dom.getElementsByTagName('DegreeOfPropertyLosses')[0].firstChild.data
#     AmountOfCompensation = dom.getElementsByTagName('AmountOfCompensation')[0].firstChild.data
#     VictimUnderstanding = dom.getElementsByTagName('VictimUnderstanding')[0].firstChild.data
#     confirmationOfResponsibility = dom.getElementsByTagName('confirmationOfResponsibility')[0].firstChild.data
#     Abscond = dom.getElementsByTagName('Abscond')[0].firstChild.data
#     DeathCausedByAbscond = dom.getElementsByTagName('DeathCausedByAbscond')[0].firstChild.data
#
#     jiaotongzhaoshi.objects.create()





# if __name__ == '__main__':
#     readxml(r'F:\xml\doc2xml\newjtzs\(2007-10-24) 曹某交通肇事案.xml')