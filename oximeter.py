eo1 = 368
ed1 = 3750.12
#red 650nm
eo2 = 816
ed2 = 761.72
#IR 800nm
AM1 = .4
BL1 = 9.7
AM2 = .5
BL2 = 9.7
R = (AM1/BL1)/(AM2/BL2)
SAO2 = (ed1-R*ed2)/(R*(eo2-ed2)+(ed1-eo1))
print(SAO2)
print(R)