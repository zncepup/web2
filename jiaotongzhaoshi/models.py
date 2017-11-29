# -*- coding: UTF-8 -*-
from django.db import models
import MySQLdb
# Create your models here.


class jiaotongzhaoshi(models.Model):
    id=models.IntegerField(primary_key=True)
    filename=models.CharField(max_length=100,null=True, blank=True)
    # 文档信息
    AwardID = models.CharField(max_length=100,null=True,blank=True)
    IndictmentID = models.CharField(max_length=100, null=True, blank=True)
    TrialTime = models.CharField(max_length=30, null=True, blank=True)
    Judge = models.CharField(max_length=1000, null=True, blank=True)
    Province = models.CharField(max_length=30, null=True, blank=True)
    City = models.CharField(max_length=30, null=True, blank=True)
    CountyDistrict = models.CharField(max_length=30, null=True, blank=True)
    # 主体（被告人）
    status = models.CharField(max_length=10, null=True, blank=True)
    IncidentAge= models.IntegerField(null=True, blank=True)
    EducationalBackground= models.CharField(max_length=10, null=True, blank=True)
    pedigree = models.CharField(max_length=1, null=True, blank=True)
    recividist = models.CharField(max_length=1, null=True, blank=True)
        # 态度
    zishou = models.CharField(max_length=1, null=True, blank=True)
    tanbai = models.CharField(max_length=1, null=True, blank=True)
    ligong = models.CharField(max_length=1, null=True, blank=True)
    renzui = models.CharField(max_length=1, null=True, blank=True)
    huizui = models.CharField(max_length=1, null=True, blank=True)
    # 客观方面
    #     车辆
    keche = models.CharField(max_length=1, null=True, blank=True)
    motuoche = models.CharField(max_length=1, null=True, blank=True)
    huoche = models.CharField(max_length=1, null=True, blank=True)
    jiaoche = models.CharField(max_length=1, null=True, blank=True)
    diandongchejidong = models.CharField(max_length=1, null=True, blank=True)
    baofeiche = models.CharField(max_length=1, null=True, blank=True)
    taopaiche = models.CharField(max_length=1, null=True, blank=True)
    qitajidongcheliang = models.CharField(max_length=1, null=True, blank=True)
    feijidongche = models.CharField(max_length=1, null=True, blank=True)
    # 危害行为（情节）
    Reaing = models.CharField(max_length=1, null=True, blank=True)
    jiujia = models.CharField(max_length=1, null=True, blank=True)
    zuijia = models.CharField(max_length=1, null=True, blank=True)
    OverSpeed = models.CharField(max_length=1, null=True, blank=True)
    OverLoad = models.CharField(max_length=1, null=True, blank=True)
    DangerousCargo = models.CharField(max_length=1, null=True, blank=True)
    Alcohol= models.CharField(max_length=20, null=True, blank=True)
    # 审判结果
    # 主刑
    Surveillans = models.CharField(max_length=20, null=True, blank=True)
    Dentention = models.CharField(max_length=20, null=True, blank=True)
    FixtedTerm = models.CharField(max_length=20, null=True, blank=True)
    Surveillans_huanxing = models.CharField(max_length=20, null=True, blank=True)
    Dentention_huanxing = models.CharField(max_length=20, null=True, blank=True)
    FixtedTerm_huanxing = models.CharField(max_length=20, null=True, blank=True)
    UnfixtedTerm = models.CharField(max_length=20, null=True, blank=True)
    Death = models.CharField(max_length=1, null=True, blank=True)
    LifeImprisonment = models.CharField(max_length=1, null=True, blank=True)
    # 附加刑
    Fine = models.CharField(max_length=20, null=True, blank=True)
    ConfiscationOfProperty = models.CharField(max_length=1, null=True, blank=True)#没收财产
    DeprivalOfPoliticalRight = models.CharField(max_length=1, null=True, blank=True)#剥夺政治权利
    Deportation = models.CharField(max_length=1, null=True, blank=True)#驱逐出境
    CaptureIllegalProperty = models.CharField(max_length=1, null=True, blank=True)#收缴非法财产
    #危害结果
    #致人死亡
    DeathNum=models.IntegerField(null=True, blank=True)
    InjuredNum=models.IntegerField(null=True, blank=True)
    DegreeOfPropertyLosses = models.CharField(max_length=100, null=True, blank=True)
    AmountOfCompensation = models.CharField(max_length=500, null=True, blank=True)
    VictimUnderstanding = models.CharField(max_length=3, null=True, blank=True)
    confirmationOfResponsibility = models.CharField(max_length=10, null=True, blank=True)
    Abscond = models.CharField(max_length=3, null=True, blank=True)
    DeathCausedByAbscond = models.CharField(max_length=3, null=True, blank=True)