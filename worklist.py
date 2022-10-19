import re
def splitdata(data):

    r = re.compile('.*G44-FIBER')
    G44list1 = list(filter(r.match, data)) # Read Note below
    pattern = r'G44-FIBER:'
    G44list = [re.sub(r'G44-FIBER:', '', s) for s in G44list1]
    print(G44list)
    G44String = " " # Our string
    # for x in G44list :
    #     G44String += x
    # print(G44String)

    r = re.compile('.*G45-FIBER')
    G45list1 = list(filter(r.match, data)) # Read Note below
    pattern = r'G45-FIBER:'
    G45list = [re.sub(r'G45-FIBER:', '', s) for s in G45list1]
    print(G45list)

    r = re.compile('.*KWT-FIBER')
    KWTlist1 = list(filter(r.match, data)) # Read Note below
    pattern = r'KWT-FIBER:'
    KWTlist = [re.sub(r'KWT-FIBER:', '', s) for s in KWTlist1]
    print(KWTlist)

    r = re.compile('.*ZMM-FIBER')
    ZMMlist1 = list(filter(r.match, data)) # Read Note below
    pattern = r'ZMM-FIBER:'
    ZMMlist = [re.sub(r'ZMM-FIBER:', '', s) for s in ZMMlist1]
    print(ZMMlist)

    r = re.compile('.*ROY-FIBER')
    ROYlist1 = list(filter(r.match, data)) # Read Note below
    pattern = r'ROY-FIBER:'
    ROYlist = [re.sub(r'ROY-FIBER:', '', s) for s in ROYlist1]
    print(ROYlist)

    r = re.compile('.*LSM-FIBER')
    LSMlist1 = list(filter(r.match, data)) # Read Note below
    pattern = r'LSM-FIBER:'
    LSMlist = [re.sub(r'LSM-FIBER:', '', s) for s in LSMlist1]
    print(LSMlist)

    r = re.compile('.*HTR-FIBER')
    HTRlist1 = list(filter(r.match, data)) # Read Note below
    pattern = r'HTR-FIBER:'
    HTRlist = [re.sub(r'HTR-FIBER:', '', s) for s in HTRlist1]
    print(HTRlist)

    compressed = f"G44 REGION:\n {G44list}\n\n ZMM REGION:\n {ZMMlist}\n\n G45 REGION:\n {G45list}\n\n R&M REGION:\n {ROYlist}\n\n KWT REGION:\n {KWTlist}\n\n LSM REGION:\n {LSMlist}\n\n HTR REGION:\n {HTRlist}"
    print(compressed)
    return compressed

def main():

    #data = ['G44-FIBER:Chalo', 'G44-FIBER:Classic_Apt', 'G44-FIBER:Elgon_[R]', 'G44-FIBER:Glory', 'G44-FIBER:Helpers', 'G44-FIBER:Imani', 'G44-FIBER:Kwa_Guka', 'G44-FIBER:Lynn', 'G44-FIBER:Magnet', 'G44-FIBER:Mamba_Village', 'G44-FIBER:Ngugi', 'G44-FIBER:PK_Hse', 'G44-FIBER:Uncle_Blue', 'G44-FIBER:Wa_Ruth', 'G44-FIBER:Witu_hse_2', 'G45-FIBER:Counter', 'G45-FIBER:Heri_Points', 'G45-FIBER:Kapkoi_Hse', 'G45-FIBER:Little_Leaders', 'G45-FIBER:Mammy_Wairimu', 'G45-FIBER:Miracle', 'G45-FIBER:Miracle_House', 'G45-FIBER:Mushae', 'G45-FIBER:Suntex', 'G45-FIBER:Zara', 'KWT-FIBER:Jura', 'KWT-FIBER:Wasonga', 'KWT-FIBER:Westham', 'LSM-FIBER:Aeneah', 'LSM-FIBER:Michigan', 'LSM-FIBER:NJ', 'LSM-FIBER:Nike', 'LSM-FIBER:Phonex', 'LSM-FIBER:Rwanda', 'LSM-FIBER:Simba', 'ROY-FIBER:By', 'ROY-FIBER:Deograts', 'ROY-FIBER:Digo', 'ROY-FIBER:Patma', 'ROY-FIBER:Pinkerton', 'ROY-FIBER:Rowan', 'ROY-FIBER:Tallic', 'ZMM-FIBER:Alsina', 'ZMM-FIBER:Hay_Hse', 'ZMM-FIBER:Helsinki', 'ZMM-FIBER:Mt._Nebo', 'ZMM-FIBER:Ring_Ting', 'ZMM-FIBER:Tosheka', 'ZMM-FIBER:Wadosi', 'ZMM-FIBER:Wahome']
    splitdata(data)

if __name__ == "__main__":
    main()