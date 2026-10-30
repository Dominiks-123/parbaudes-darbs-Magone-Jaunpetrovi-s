# ----------------------------------------------------------------------
# C1. Python — rīks, kas atlasa un saglabā
# ----------------------------------------------------------------------

# Uzraksti skriptu, kuram līmeni padod kā argumentu komandrindā. Skripts izvada
#, cik tāda līmeņa rindu žurnālā ir, un saglabā visas šīs rindas failā,
#kura nosaukums sākas ar līmeņa nosaukumu. Ja arguments nav padots,
#skripts izvada pamācību un neavarē.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Mainīgo, kurā glabā līmeni, nosauc ar vārdu meklejamais.

#fixer upper needed
import sys
if len(sys.argv)<2:
    mekletais=input(
        "Ievadi kļūdas līmeni (INFO, WARNING, ERROR, CRITICAL): ").upper()
else:
    mekletais=sys.argv[1].upper()
skaits=0
with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        dalas=rinda.split()
        if len(dalas) >=3 and dalas[2]== mekletais:
            skaits+=1
print("Meklētias līmenis:", mekletais)
print("Rindu skaits:", skaits)
