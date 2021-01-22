from bottle import route,get,post,request,run,template
import datetime

def check(password): #ログイン判定
    if password=="applmic":
        return True
    else:
        return False


def protein_mass(protein): #分子量計算
    protein=protein.upper()

    protein_mass_table="""
    A 71.03711 C 103.00919 D 115.02694
    E 129.04259 F 147.06841 G 57.02146
    H 137.05891 I 113.08406 K 128.09496
    L 113.08406 M 131.04049 N 114.04293
    P 97.05276 Q 128.05858 R 156.10111
    S 87.03203 T 101.04768 V 99.06841
    W 186.07931 Y 163.06333"""

    temp = protein_mass_table.split()
    amino_list=[str(k) for k in temp[0::2]]
    weight_list=[float(k) for k in temp[1::2]]

    protein_mass=[]
    for amino in protein:
        if amino in amino_list:
            i=amino_list.index(amino)
            protein_mass.append(weight_list[i])
        else:
            return "Undefined character was detected. Check the sequence."
    
    mass=sum(protein_mass)
    return mass


@route("/login") #GETメソッドで/loginにアクセスした時の処理
def login_form():
    dt_now=datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
    return template('view/login', t=dt_now)


@post('/index')
def login():
    #POSTされた情報にアクセス
    name=request.forms.get('username')
    pasw=request.forms.get('password')
    #判定
    if check(pasw):
        return template('view/index', nm=name)
    else:
        return "<p>Login failed. </p>"


@post('/result')
def result():
    #POSTされた情報にアクセス
    protein=str(request.forms.get('protein'))
    #計算
    mass=protein_mass(protein)
    return template('view/result', Result=mass)

run(host="localhost", port=8080, debug=True)




