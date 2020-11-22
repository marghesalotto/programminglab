# Inizializzo una lista vuota per salvare i valori
values = []
# apro e leggo il file, linea per linea
my_file = open("shampoo_sales.csv", "r")
for line in my_file:
 # faccio lo split di ogni riga sulla virgola
    elements = line.split(',')
 # se NON sto processando l'intestazione
    if elements[0] != 'Date':
     # setto la data e il valore
        date = elements[0]
        value = elements[1]
     # aggiungo alla lista dei valori questo valore
        try:
            values.append(float(value))
        except Exception as e:
            print ("errore\n {}".format(e))   

print (values)
def my_list_sum(the_list):
    sum = 0
    for item in the_list:
        sum = sum+item
    print ("\nLa somma degli shampoo venduti negli ultimi tre anni corrisponde a: {}".format(sum))
my_list_sum(values)