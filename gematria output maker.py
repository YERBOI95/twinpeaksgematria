import pandas as pd
import json

allWords = "laura palmer,dale cooper,leland palmer,bob,owl,uti,stele of jeu,sarah palmer,ishtar,phillip jeffries,palmer,gordon cole,dougie jones,diane,twin peaks,the giant,sycamore tree,sycamore trees,sycamore,horne,josie,judy,packard,josie packard,benjamin horne,one eyed jacks,normas diner,rr diner,double r diner,pale horse,log lady,the giant,the arm,arm,daath bag,daath,bag,hurley,james,james hurley,wally,waldo,leo johnson,leo,canada,jesus,jesus christ,lamb,deer,bunny,hawk,ill catch you with my death bag,ill catch jeu with my daath bag,the owls are not what they seem,emerald tablet,washington,washington dc,washington state,fbi,did you find him,him,operation paperclip,operation neptune,donna,amen,blue ape of thoth,duck eye,sacred mound,cooper,dale cooper,truman,briggs,hayward,windom earle,jennings,mike,martel,eckhardt,blue rose,john justice wheeler,audrey horne,carrie page,woodsmen,homeless,did jeu find him,jeu uti,jeu uta,log,pierre,sarah palmer,chalfont,tremond,mrs chalfont,mrs tremond,donna hayward,cathrine martell,the muffin,the great went,maddy ferguson,muffin,what year is this,abrahadabra,odessa,fire walk with me,white horse,stele of jeuuti,richard,dale,linda,richardandlinda,laura,creamed corn,garmonbozia,pain and suffering,diane evans,witch,silver star,nuit,fish,carrie,page,priestess,cia,navy,good bunny,bad bunny,milk and cookies,coffee,milk,the dreamer,major garland briggs,garland briggs,dreamer,babylon,scarlet woman,moonchild,the beast,babalon,thefireman,fireman,oil,david lynch,gordon,mark frost,fire,air,water,earth,electricity,buck,truck,pierre tremond,pierre chalfont,black lodge,white lodge,the white lodge,tibet,chemicals,engine oil,nag hammadi,insurance,richard horne,owl of athena,athena,justice,TZEDEK,ra,hathor,tria prima,monkey,jack,jack parsons,blue monkey,kpjk,the fool,the book of the law,book of the law,law,thelema,the ring,ring,rose,white rose,red rose,cherry pie,pie,ipsos,thmaist,true will,the little girl who lives down the lane, the little girl who lived down the lane,horus,maat,Sarah Novack,novack,the owls are not what they seem,owls,the owls,the owl,doppelganger,mrc,hows annie,night of pan,l ron hubbard,hubbard,Sarah Judith Novack,Sara Northrup Hollister,sara hollister,hollister,northrup,sara northrup,Bernice,Lafayette Ronald Hubbard,Marjorie Cameron,marjorie,cameron,marjorie parsons,Marjorie Cameron Parsons Kimmel,parsons,cocaine,bridal chamber, kettle, percolator, theres a fish in the percolator, convenience store, temple, alice tremond, alice,mary reber,jeu,lilit,lilith,Cameron Solar Francis Moniz Tarle,Aloster Kerval,The Great Went,went,great went,fart,blank as a fart, blank,Jacques Renault,diary,petal,flower,wowbobwow,wow,mom,jade"
allWords = allWords.upper().split(",")
query = allWords
print(allWords)

#english Qaballa
engQaballa ={}
engQaballa['A'] = 1
engQaballa ['L'] = 2  
engQaballa ['W'] = 3
engQaballa ['H'] = 4
engQaballa ['S'] = 5
engQaballa ['D'] =6
engQaballa ['O'] =7
engQaballa ['Z'] =8
engQaballa['K'] =9
engQaballa['V'] =10
engQaballa['G'] =11
engQaballa['R'] =12
engQaballa['C'] =13
engQaballa['N'] =14
engQaballa['Y'] =15
engQaballa['J'] =16
engQaballa['U'] =17
engQaballa['F'] =18
engQaballa['Q'] =19
engQaballa['B'] =20
engQaballa['M'] =21
engQaballa['X'] =22
engQaballa['I'] =23
engQaballa['T'] =24
engQaballa['E'] =25
engQaballa['P'] =26

#number to letter
#print(list(engQaballa.keys())[list(engQaballa.values()).index(1)])

#letter to number
#engQaResult = [sum(engQaballa[k]) for k in query if k in engQaballa]
engQaResult = {}
for x in query:
    y = list(x)
    print(x)
    engQaResult[x] = sum([engQaballa[k] for k in y if k in engQaballa])
print(engQaResult)
#print("English Qaballa = ", sum(engQaResult))

#english Qaballa
TrigramEngQaballa ={}
TrigramEngQaballa ['A'] = 5
TrigramEngQaballa ['L'] = 1  
TrigramEngQaballa ['W'] = 8
TrigramEngQaballa ['H'] = 3
TrigramEngQaballa ['S'] = 15
TrigramEngQaballa ['D'] =23
TrigramEngQaballa ['O'] =10
TrigramEngQaballa ['Z'] =19
TrigramEngQaballa ['K'] =17
TrigramEngQaballa ['V'] =22
TrigramEngQaballa ['G'] =11
TrigramEngQaballa ['R'] =14
TrigramEngQaballa['C'] =2
TrigramEngQaballa['N'] =24
TrigramEngQaballa['Y'] =18
TrigramEngQaballa['J'] =7
TrigramEngQaballa['U'] =25
TrigramEngQaballa['F'] =12
TrigramEngQaballa['Q'] =16
TrigramEngQaballa['B'] =20
TrigramEngQaballa['M'] =21
TrigramEngQaballa['X'] =6
TrigramEngQaballa['I'] =0
TrigramEngQaballa['T'] =9
TrigramEngQaballa['E'] =13
TrigramEngQaballa['P'] =4

#letter to number
TengQaResult = {}
for x in query:
    y = list(x)
    print(x)
    TengQaResult[x] = sum([TrigramEngQaballa[k] for k in y if k in TrigramEngQaballa])
print(TengQaResult)


stdreng ={}
stdreng['A'] = 6
stdreng['B'] = 12
stdreng['C'] = 18
stdreng['D'] = 24
stdreng['E'] = 30
stdreng['F'] = 36
stdreng['G'] = 42
stdreng['H'] = 48
stdreng['I'] = 54
stdreng['J'] = 60
stdreng['K'] = 66
stdreng['L'] = 72
stdreng['M'] = 78
stdreng['N'] = 84
stdreng['O'] = 90
stdreng['P'] = 96
stdreng['Q'] = 102
stdreng['R'] = 108
stdreng['S'] = 114
stdreng['T'] = 120
stdreng['U'] = 126
stdreng['V'] = 132
stdreng['W'] = 138
stdreng['X'] = 144
stdreng['Y'] = 150
stdreng['Z'] = 156

#letter to number
#stdrengresult = [stdreng[k] for k in query if k in stdreng]
#print("Standard English = ", sum(stdrengresult))

stdrengresult = {}
for x in query:
    y = list(x)
    print(x)
    stdrengresult[x] = sum([stdreng[k] for k in y if k in stdreng])
print(stdrengresult)


stdrheb = {}
stdrheb['א'] = 1
stdrheb['A'] = 1
stdrheb['B'] = 2
stdrheb['ב'] = 2
stdrheb['C'] = 3
stdrheb['ג'] = 3
stdrheb['ד'] = 4
stdrheb['D'] = 4
stdrheb['E'] = 5
stdrheb['ה'] = 5
stdrheb['F'] = 6
stdrheb['ו'] = 6
stdrheb['ז'] = 7
stdrheb['G'] = 7
stdrheb['H'] = 8
stdrheb['ח'] = 8
stdrheb['I'] = 9
stdrheb['ט'] = 9
stdrheb['K'] = 10
stdrheb['י'] = 10
stdrheb['L'] = 20
stdrheb['כ'] = 20
stdrheb['ך'] = 20
stdrheb['ל'] = 30
stdrheb['M'] = 30
stdrheb['ם'] = 40
stdrheb['מ'] = 40
stdrheb['N'] = 40
stdrheb['O'] = 50
stdrheb['נ'] = 50
stdrheb['ן'] = 50
stdrheb['P'] = 60
stdrheb['ס'] = 60
stdrheb['Q'] = 70
stdrheb['ע'] = 70
stdrheb['ף'] = 80
stdrheb['פ'] = 80
stdrheb['R'] = 80
stdrheb['ץ'] = 90
stdrheb['צ'] = 90
stdrheb['S'] = 90
stdrheb['T'] = 100
stdrheb['ק'] = 100
stdrheb['ר'] = 200
stdrheb['U'] = 200
stdrheb['X'] = 300
stdrheb['ש'] = 300
stdrheb['Y'] = 400
stdrheb['ת'] = 400
stdrheb['Z'] = 500
stdrheb['J'] = 600
stdrheb['V'] = 700
stdrheb['W'] = 900


#letter to number
#stdrhebresult = [stdrheb[k] for k in query if k in stdrheb]
#print("Standard Hebrew = ", sum(stdrhebresult))

stdrhebresult = {}
for x in query:
    y = list(x)
    print(x)
    stdrhebresult[x] = sum([stdrheb[k] for k in y if k in stdrheb])
print(stdrhebresult)

simpeng = {}
simpeng['A'] = 1
simpeng['B'] = 2
simpeng['C'] = 3
simpeng['D'] = 4
simpeng['E'] = 5
simpeng['F'] = 6
simpeng['G'] = 7
simpeng['H'] = 8
simpeng['I'] = 9
simpeng['J'] = 10
simpeng['K'] = 11
simpeng['L'] = 12
simpeng['M'] = 13
simpeng['N'] = 14
simpeng['O'] = 15
simpeng['P'] = 16
simpeng['Q'] = 17
simpeng['R'] = 18
simpeng['S'] = 19
simpeng['T'] = 20
simpeng['U'] = 21
simpeng['V'] = 22
simpeng['W'] = 23
simpeng['X'] = 24
simpeng['Y'] = 25
simpeng['Z'] = 26

#letter to number
#simpengresult = [simpeng[k] for k in query if k in simpeng]
#print("Simple English = ", sum(simpengresult))

simpengresult = {}
for x in query:
    y = list(x)
    print(x)
    simpengresult[x] = sum([simpeng[k] for k in y if k in simpeng])
print(simpengresult)

#look up numbers in the liber#
"""tmpList = {sum(simpengresult), sum(stdrhebresult), sum(stdrengresult), sum(engQaResult)}
delim = "|"
temp = list(map(str, tmpList))
finlist = str(delim.join(temp))

# open file
with open('liber777.json', 'r', encoding="utf8")as file:
    df = pd.DataFrame.from_dict(json.load(file))

#print(df.head())
df = df.rename(columns=df.iloc[0])
print(df[df.apply(lambda row: row.astype(str).str.contains(finlist, case=False).any(), axis=1)])"""
#look up numbers in the liber END#
"""
test = pd.DataFrame.from_dict([simpengresult, stdrhebresult, stdrengresult, engQaResult]).transpose()
test = test.rename(columns={0: "Simple English", 1: "Hebrew Gematria", 2: "Standard English", 3:"English Qabbala"})
print(test)
test.to_csv('gem.csv')
"""
test = pd.DataFrame.from_dict([stdrhebresult, stdrengresult, engQaResult]).transpose()
test = test.rename(columns={0: "Hebrew Gematria", 1: "Standard English", 2: "English Qaballa"})
print(test)
test.to_csv('gem.csv')
