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
import csv
while 0!=1:
    mekletais=input("Ievadi kļūdas līmeni (INFO, WARNING, ERROR, CRITICAL): ")
    if mekletais == "INFO":
        break
    elif mekletais == "WARNING":
        break
    elif mekletais == "ERROR":
        break
    elif mekletais == "CRITICAL":
        break
    else:
        print("Lūdzu ievadi ar lieliem burtiem un pārbaudi ka uzrakstīts pareizi!")
skaits=0
with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        dalas=rinda.split()
        if len(dalas) >=3 and dalas[2]== mekletais:
            skaits+=1
print("Meklētias līmenis:", mekletais)
print("Rindu skaits:", skaits)
with open(f"{mekletais}.csv","w", encoding="utf-8-sig",newline="") as b:
    raks=csv.writer(b, delimiter=";")
    raks.writerow(dalas)
