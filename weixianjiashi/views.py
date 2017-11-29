from django.shortcuts import render
from jiaotongzhaoshi.views import bool2num,month2year
from .models import weixianjiashi
import codecs
# Create your views here.
def index(request):
    return render(request,'weixianjiashi.html')

def results(request):
    sheng = request.GET.get('sheng')
    shi = request.GET.get('shi')
    xian = request.GET.get('xian')
    jiujia = request.GET.get('jiujia')
    zuijia = request.GET.get('zuijia')
    chaosu = request.GET.get('chaosu')
    chaozai = request.GET.get('chaozai')
    zhuizhujingshi = request.GET.get('zhuizhujingshi')
    weixianpinyunshu = request.GET.get('weixianpinyunshu')
    # taoyi = request.GET.get('taoyi')
    # taoyizhirensiwang = request.GET.get('taoyizhirensiwang')
    # zerenrending = request.GET.get('zerenrending')
    # beihairenliangjie = request.GET.get('beihairenliangjie')
    # siwangrenshu = request.GET.get('siwangrenshu')
    # zhongshangrenshu = request.GET.get('zhongshangrenshu')
    qianke = request.GET.get('qianke')
    leifan = request.GET.get('leifan')
    zishou = request.GET.get('zishou')
    tanbai = request.GET.get('tanbai')
    ligong = request.GET.get('ligong')
    renzui = request.GET.get('renzui')
    huizui = request.GET.get('huizui')
    keche = request.GET.get('keche')
    motuoche = request.GET.get('motuoche')
    huoche = request.GET.get('huohe')
    jiaoche = request.GET.get('jiaoche')
    diandongchejidong = request.GET.get('diandongchejidong')
    baofeiche = request.GET.get('baofeiche')
    taopaiche = request.GET.get('taopaiche')
    qitajidongcheliang = request.GET.get('qitajidongcheliang')
    feijidongche = request.GET.get('feijidongche')

    objects = weixianjiashi.objects.all()
    if sheng != '省':
        objects = objects.filter(Province=sheng)
    if shi != '市':
        objects = objects.filter(City=shi)
    if xian != '区(县)':
        objects = objects.filter(CountyDistrict=xian)
    if jiujia == '是':
        objects = objects.filter(jiujia=1)
    if jiujia == '否':
        objects = objects.filter(jiujia=0)
    if chaosu == '是':
        objects = objects.filter(OverSpeed=1)
    if chaosu == '否':
        objects = objects.filter(OverSpeed=0)
    if chaozai == '是':
        objects = objects.filter(OverLoad=1)
    if chaozai == '否':
        objects = objects.filter(OverLoad=0)
    if zhuizhujingshi == '是':
        objects = objects.filter(Reaing=1)
    if zhuizhujingshi == '否':
        objects = objects.filter(Reaing=0)
    if weixianpinyunshu == '是':
        objects = objects.filter(DangerousCargo=1)
    if weixianpinyunshu == '否':
        objects = objects.filter(DangerousCargo=0)

    # if siwangrenshu != '':
    #     objects = objects.filter(DeathNum=siwangrenshu)
    # if zhongshangrenshu != '':
    #     objects = objects.filter(InjuredNum=zhongshangrenshu)
    # if taoyi == '是':
    #     objects = objects.filter(Abscond='yes')
    # if taoyi == '否':
    #     objects = objects.filter(Abscond='no')
    # if taoyizhirensiwang == '是':
    #     objects = objects.filter(DeathCausedByAbscond='yes')
    # if taoyizhirensiwang == '否':
    #     objects = objects.filter(DeathCausedByAbscond='no')
    # if beihairenliangjie == '是':
    #     objects = objects.filter(VictimUnderstanding='yes')
    # if beihairenliangjie == '否':
    #     objects = objects.filter(VictimUnderstanding='no')
    # if zerenrending != '':
    #     objects = objects.filter(confirmationOfResponsibility=zerenrending)

    qianke = bool2num(qianke)
    leifan = bool2num(leifan)
    zishou = bool2num(zishou)
    tanbai = bool2num(tanbai)
    ligong = bool2num(ligong)
    renzui = bool2num(renzui)
    huizui = bool2num(huizui)
    keche = bool2num(keche)
    motuoche = bool2num(motuoche)
    huoche = bool2num(huoche)
    jiaoche = bool2num(jiaoche)
    diandongchejidong = bool2num(diandongchejidong)
    baofeiche = bool2num(baofeiche)
    taopaiche = bool2num(taopaiche)
    qitajidongcheliang = bool2num(qitajidongcheliang)
    feijidongche = bool2num(feijidongche)
    if qianke == 1:
        objects = objects.filter(pedigree=qianke)
    if leifan == 1:
        objects = objects.filter(recividist=leifan)
    if zishou == 1:
        objects = objects.filter(zishou=zishou)
    if tanbai == 1:
        objects = objects.filter(tanbai=tanbai)
    if ligong == 1:
        objects = objects.filter(ligong=ligong)
    if renzui == 1:
        objects = objects.filter(renzui=renzui)
    if huizui == 1:
        objects = objects.filter(huizui=huizui)
    if keche == 1:
        objects = objects.filter(keche=keche)
    if motuoche == 1:
        objects = objects.filter(motuoche=motuoche)
    if huoche == 1:
        objects = objects.filter(huoche=huoche)
    if jiaoche == 1:
        objects = objects.filter(jiaoche=jiaoche)
    if diandongchejidong == 1:
        objects = objects.filter(diandongchejidong=diandongchejidong)
    if baofeiche == 1:
        objects = objects.filter(baofeiche=baofeiche)
    if taopaiche == 1:
        objects = objects.filter(taopaiche=taopaiche)
    if qitajidongcheliang == 1:
        objects = objects.filter(qitajidongcheliang=qitajidongcheliang)
    if feijidongche == 1:
        objects = objects.filter(feijidongche=feijidongche)
    n = objects.count()
    for anli in objects:
        anli.filename = anli.filename.split('.')[0]
        if anli.Dentention_huanxing == '0.0':
            anli.Dentention_huanxing = 'unknown'
        if anli.FixtedTerm_huanxing == '0.0':
            anli.FixtedTerm_huanxing = 'unknown'
        if anli.Surveillans_huanxing == '0.0':
            anli.Surveillans_huanxing = 'unknown'
        if anli.Dentention_huanxing != 'unknown':
            anli.Dentention_huanxing = month2year(anli.Dentention_huanxing)
        if anli.Dentention != 'unknown':
            anli.Dentention = month2year(anli.Dentention)
        if anli.FixtedTerm != 'unknown':
            anli.FixtedTerm = month2year(anli.FixtedTerm)
        if anli.FixtedTerm_huanxing != 'unknown':
            anli.FixtedTerm_huanxing = month2year(anli.FixtedTerm_huanxing)
        if anli.Surveillans_huanxing != 'unknown':
            anli.Surveillans_huanxing = month2year(anli.Surveillans_huanxing)
        if anli.Surveillans != 'unknown':
            anli.Surveillans = month2year(anli.Surveillans)
    return render(request, 'results_wxjs.html', {'x': objects, 'n': n})

def result_wxjs(request):
    id = request.GET.get('id', 0)
    object=weixianjiashi.objects
    anli=object.filter(id=id)[0]
    dir='F:\wenshu\weixianjiashi-all/'+anli.filename.split('.')[0]+'.txt'
    if anli.Dentention_huanxing == '0.0':
        anli.Dentention_huanxing = 'unknown'
    if anli.FixtedTerm_huanxing == '0.0':
        anli.FixtedTerm_huanxing = 'unknown'
    if anli.Surveillans_huanxing == '0.0':
        anli.Surveillans_huanxing = 'unknown'
    if anli.Dentention_huanxing != 'unknown':
        anli.Dentention_huanxing = month2year(anli.Dentention_huanxing)
    if anli.Dentention != 'unknown':
        anli.Dentention = month2year(anli.Dentention)
    if anli.FixtedTerm != 'unknown':
        anli.FixtedTerm = month2year(anli.FixtedTerm)
    if anli.FixtedTerm_huanxing != 'unknown':
        anli.FixtedTerm_huanxing = month2year(anli.FixtedTerm_huanxing)
    if anli.Surveillans_huanxing != 'unknown':
        anli.Surveillans_huanxing = month2year(anli.Surveillans_huanxing)
    if anli.Surveillans != 'unknown':
        anli.Surveillans = month2year(anli.Surveillans)
    with codecs.open(dir,'r','utf-8') as f:
        f=f.read()
        f=f.split('\n')
        contents=[]
        for x in f :
            s=x.strip()
            if s!='':
                contents.append(s)
    return render(request,'result_jtzs_deatil.html',{'anli':anli,'file':contents})