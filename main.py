import json

running = True
HQs = True
Troops = True
Elites = True
FastAttack = True
HeavySupport = True
Transport = True

c = open('ChaosMarines.json')
chaos_marines = json.load(c)


def look_up(i):
    for r in chaos_marines['ChaosMarines']:
        if r['NAME'].lower() == i.lower():
            csm_return = "Name: " + r["NAME"] + "\n" + "Points Per Model: " + str(r["Points"])
            print(csm_return)
            p = r["Points"]
            return p


HQP = 0
HQP2 = 0
HQP3 = 0
SN = 0
SN2 = 0
SN3 = 0
SN4 = 0
SN5 = 0
SN6 = 0
ESN = 0
ESN2 = 0
ESN3 = 0
ESN4 = 0
ESN5 = 0
ESN6 = 0
FASC = 0
FASC2 = 0
FASC3 = 0
FASC4 = 0
FASC5 = 0
FASC6 = 0
HSSC = 0
HSSC2 = 0
HSSC3 = 0
HSSC4 = 0
HSSC5 = 0
HSSC6 = 0
TRSPC = 0
TRSPC2 = 0

HQSum = 0
TroopSum = 0
EliteSum = 0
FastAttackSum = 0
HeavySupportSum = 0

while running is True:
    HQCheck = input("Have HQs?: ")
    if HQCheck.lower() != "No".lower():
        while HQs is True:
            if HQCheck.lower() != "No".lower():
                HQ = input("Enter HQ: ")
                HQP = look_up(HQ)
            else:
                HQs = False
                break
            HQCheck2 = input("More HQs?: ")
            if HQCheck2.lower() != "No".lower():
                HQ2 = input("Enter second HQ: ")
                HQP2 = look_up(HQ2)
            else:
                HQs = False
                break
            HQCheck3 = input("Any More HQs?: ")
            if HQCheck3.lower() != "No".lower():
                HQ3 = input("Enter second HQ: ")
                HQP3 = look_up(HQ2)
                HQs = False
                break
            else:
                HQs = False
                break
    else:
        HQs = False
    HQSum = HQP + HQP2 + HQP3
    print("Total HQ Cost: " + str(HQSum))

    while Troops is True:
        TroopCheck = input("Have Troops?: ")
        if TroopCheck.lower() != "No".lower():
            Troop = input("Enter Troop:")
            TNumber = int(input("Number in Squad: "))
            TP = look_up(Troop)
            SN = TP*TNumber
        else:
            Troops = False
            break
        TroopCheck2 = input("Have More Troops?: ")
        if TroopCheck2.lower() != "No".lower():
            Troop2 = input("Enter Troop:")
            TNumber2 = int(input("Number in Squad: "))
            TP2 = look_up(Troop2)
            SN2 = TP2 * TNumber2
        else:
            Troops = False
            break
        TroopCheck3 = input("Have More Troops?: ")
        if TroopCheck3.lower() != "No".lower():
            Troop3 = input("Enter Troop:")
            TNumber3 = int(input("Number in Squad: "))
            TP3 = look_up(Troop3)
            SN3 = TP3 * TNumber3
        else:
            Troops = False
            break
        TroopCheck4 = input("Have More Troops?: ")
        if TroopCheck4.lower() != "No".lower():
            Troop4 = input("Enter Troop:")
            TNumber4 = int(input("Number in Squad: "))
            TP4 = look_up(Troop4)
            SN4 = TP4 * TNumber4
        else:
            Troops = False
            break
        TroopCheck5 = input("Have More Troops?: ")
        if TroopCheck5.lower() != "No".lower():
            Troop5 = input("Enter Troop:")
            TNumber5 = int(input("Number in Squad: "))
            TP5 = look_up(Troop5)
            SN5 = TP5 * TNumber5
        else:
            Troops = False
            break
        TroopCheck6 = input("Have More Troops?: ")
        if TroopCheck6.lower() != "No".lower():
            Troop6 = input("Enter Troop:")
            TNumber6 = int(input("Number in Squad: "))
            TP6 = look_up(Troop6)
            SN6 = TP6 * TNumber6
            Troops = False
            break
        Troops = False
    TroopSum = SN + SN2 + SN3 + SN4 + SN5 + SN6
    print("Total Troop Cost:" + str(TroopSum))

    while Elites is True:
        EliteCheck = input("Have Elites?: ")
        if EliteCheck.lower() != "No".lower():
            Elite = input("Enter Elite: ")
            ENumber = int(input("Number in Squad: "))
            EP = look_up(Elite)
            ESN = EP * ENumber
        else:
            Elites = False
            break
        EliteCheck2 = input("Have More Elites?: ")
        if EliteCheck2.lower() != "No".lower():
            Elite2 = input("Enter Elite: ")
            ENumber2 = int(input("Number in Squad: "))
            EP2 = look_up(Elite2)
            ESN2 = EP2 * ENumber2
        else:
            Elites = False
            break
        EliteCheck3 = input("Have More Elites?: ")
        if EliteCheck3.lower() != "No".lower():
            Elite3 = input("Enter Elite: ")
            ENumber3 = int(input("Number in Squad: "))
            EP3 = look_up(Elite3)
            ESN3 = EP3 * ENumber3
        else:
            Elites = False
            break
        EliteCheck4 = input("Have More Elites?: ")
        if EliteCheck4.lower() != "No".lower():
            Elite4 = input("Enter Elite: ")
            ENumber4 = int(input("Number in Squad: "))
            EP4 = look_up(Elite4)
            ESN4 = EP4 * ENumber4
        else:
            Elites = False
            break
        EliteCheck5 = input("Have More Elites?: ")
        if EliteCheck5.lower() != "No".lower():
            Elite5 = input("Enter Elite: ")
            ENumber5 = int(input("Number in Squad: "))
            EP5 = look_up(Elite5)
            ESN5 = EP5 * ENumber5
        else:
            Elites = False
            break
        EliteCheck6 = input("Have More Elites?: ")
        if EliteCheck6.lower() != "No".lower():
            Elite6 = input("Enter Elite: ")
            ENumber6 = int(input("Number in Squad: "))
            EP6 = look_up(Elite6)
            ESN6 = EP6 * ENumber6
            Elites = False
            break
        Elites = False
    EliteSum = ESN + ESN2 + ESN3 + ESN4 + ESN5 + ESN6
    print("Total Elite Cost: " + str(EliteSum))

    while FastAttack is True:
        FACheck = input("Have Fast Attack?: ")
        if FACheck.lower() != "No".lower():
            FA = input("Enter Fast Attack: ")
            FANumber = int(input("Number in Squad: "))
            FP = look_up(FA)
            FASC = FP * FANumber
        else:
            FastAttack = False
            break
        FACheck2 = input("Have More Fast Attack?: ")
        if FACheck2.lower() != "No".lower():
            FA2 = input("Enter Fast Attack: ")
            FANumber2 = int(input("Number in Squad: "))
            FP2 = look_up(FA2)
            FASC2 = FP2 * FANumber2
        else:
            FastAttack = False
            break
        FACheck3 = input("Have More Fast Attack?: ")
        if FACheck3.lower() != "No".lower():
            FA3 = input("Enter Fast Attack: ")
            FANumber3 = int(input("Number in Squad: "))
            FP3 = look_up(FA3)
            FASC3 = FP3 * FANumber3
        else:
            FastAttack = False
            break
        FACheck4 = input("Have More Fast Attack?: ")
        if FACheck4.lower() != "No".lower():
            FA4 = input("Enter Fast Attack: ")
            FANumber4 = int(input("Number in Squad: "))
            FP4 = look_up(FA4)
            FASC4 = FP4 * FANumber4
        else:
            FastAttack = False
            break
        FACheck5 = input("Have More Fast Attack?: ")
        if FACheck5.lower() != "No".lower():
            FA5 = input("Enter Fast Attack: ")
            FANumber5 = int(input("Number in Squad: "))
            FP5 = look_up(FA5)
            FASC5 = FP5 * FANumber5
        else:
            FastAttack = False
            break
        FACheck6 = input("Have More Fast Attack?: ")
        if FACheck6.lower() != "No".lower():
            FA6 = input("Enter Fast Attack: ")
            FANumber6 = int(input("Number in Squad: "))
            FP6 = look_up(FA6)
            FASC6 = FP6 * FANumber6
        else:
            FastAttack = False
            break
    FastAttackSum = FASC + FASC2 + FASC3 + FASC4 + FASC5 + FASC6
    print("Total Cost of Fast Attack: " + str(FastAttackSum))

    while HeavySupport is True:
        HSCheck = input("Have Heavy Support?: ")
        if HSCheck.lower() != "No".lower():
            HS = input("Enter Fast Attack: ")
            HSNumber = int(input("Number in Squad: "))
            HSP = look_up(HS)
            HSSC = HSP * HSNumber
        else:
            HeavySupport = False
            break
        HSCheck2 = input("Have More Heavy Support?: ")
        if HSCheck2.lower() != "No".lower():
            HS2 = input("Enter Fast Attack: ")
            HSNumber2 = int(input("Number in Squad: "))
            HSP2 = look_up(HS2)
            HSSC2 = HSP2 * HSNumber2
        else:
            HeavySupport = False
            break
        HSCheck3 = input("Have More Heavy Support?: ")
        if HSCheck3.lower() != "No".lower():
            HS3 = input("Enter Fast Attack: ")
            HSNumber3 = int(input("Number in Squad: "))
            HSP3 = look_up(HS3)
            HSSC3 = HSP3 * HSNumber3
        else:
            HeavySupport = False
            break
        HSCheck4 = input("Have More Heavy Support?: ")
        if HSCheck4.lower() != "No".lower():
            HS4 = input("Enter Fast Attack: ")
            HSNumber4 = int(input("Number in Squad: "))
            HSP4 = look_up(HS4)
            HSSC4 = HSP4 * HSNumber4
        else:
            HeavySupport = False
            break
        HSCheck5 = input("Have More Heavy Support?: ")
        if HSCheck5.lower() != "No".lower():
            HS5 = input("Enter Fast Attack: ")
            HSNumber5 = int(input("Number in Squad: "))
            HSP5 = look_up(HS5)
            HSSC5 = HSP5 * HSNumber5
        else:
            HeavySupport = False
            break
        HSCheck6 = input("Have More Heavy Support?: ")
        if HSCheck6.lower() != "No".lower():
            HS6 = input("Enter Fast Attack: ")
            HSNumber6 = int(input("Number in Squad: "))
            HSP6 = look_up(HS6)
            HSSC6 = HSP6 * HSNumber6
        else:
            HeavySupport = False
            break
        HeavySupportSum = HSSC + HSSC2 + HSSC3 + HSSC4 + HSSC5 + HSSC6
        print("Total Heavy Support Cost: " + str(HeavySupportSum))

    while Transport is True:
        TRSPCheck = input("Have Trasports?: ")
        if TRSPCheck.lower() != "No".lower():
            TRSP = input("Enter Transport: ")
            TRSPNumber = int(input("Number of this transport: "))
            TRSPP = look_up(TRSP)
            TRSPC = TRSP * TRSPNumber
        else:
            FastAttack = False
            break
        TRSPCheck2 = input("Have Other Transports?: ")
        if TRSPCheck2.lower() != "No".lower():
            TRSP2 = input("Enter Transport: ")
            TRSPNumber2 = int(input("Number of this transport: "))
            TRSPP2 = look_up(TRSP)
            TRSPC2 = TRSP2 * TRSPNumber2
        else:
            FastAttack = False
            break
    TransportSum = TRSPC + TRSPC2
    print("Total Transport Cost: " + str(TransportSum))

    ArmyTotal = HQSum + TroopSum + EliteSum + FastAttackSum + HeavySupportSum + TransportSum
    print("Total Army Cost: " + str(ArmyTotal))
    running = False

