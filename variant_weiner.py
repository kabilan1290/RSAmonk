from sage.all import *

def wiener(e, n):
    m = 12345
    c = pow(m, e, n)
    q0 = 1
 
    list1 = continued_fraction(Integer(e)/Integer(n))
    conv = list1.convergents()
    for i in conv:
        k = i.numerator()
        q1 = i.denominator()
 
        for r in range(20):
            for s in range(20):
                d = r*q1 + s*q0
                m1 = pow(c, d, n)
                if m1 == m:
                    print(d)
        q0 = q1




n=698491229018617866913439446346471163472558208924077226680142788666975310538145321929146447762905069894035917431326487956250957720571978572823687849059920787303025692154070829036217928749360678725398133415179255935742309941010132694576977689456112119629015193398461689794498824641575321133336366067022953975900092198038260902623522501246578776626162635825107771722711940199404818420573142581587276540226521274722941752974216982918201384775694541078556882367813031
e= 473942956098597820220469792845742500778787667370139945336962851836944820611758016955838474056135974449429651523689707189746956503090573007038882592192662108009105988801240992546857461015645973313376512628146439789647175954429224823945115651118751480270762628324283169644336180720618427405011551606650256747631187135571937711488876112426342905154035663354772248678642559769320890564854022113441429962294088612832697262354998514171764811530183386631750738577941129
print(wiener(e, n))

#d = 101163513230017858871883136800341227994997965012215130183396962583124452930473