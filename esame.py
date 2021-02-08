class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    #dichiarazione variabile nome
    def __init__(self,name):
        self.name=name
    
    #dichiarazione funzione
    def get_data(self):
        #apro file
        try:
            time_s_file = open(self.name, 'r')
        except:
            raise ExamException('errore, lista non leggibile')
        #creo lista
        values = []
        #leggo linee del file
        code = time_s_file.readlines()
        for line in code:
            #per ogni linea separo epoch e 
            #temperatura
            valore = line.split(",")
            #controllo che i valori epoch siano 
            #interi e che quelli di temperatura
            #siano floating point
            try:
                data = int(float(valore[0]))
                temp = float(valore[1])
            except:
                continue
            #assegno valori alla lista
            values.append([data,temp])
        #controllo che i valori epoch siano 
        #ordinati e non duplicati
        for i in range(len(values)-1):
            if values[i][0] >= values[i+1][0]:
                raise ExamException ('errore, timestamp epoch fuori ordine o duplicato')
        return values

def daily_stats(time_series):
    j = 0
    #creo lista che conterrà le liste con le 
    #statistiche giornaliere
    a = []
    while (j < len(time_series)):
        #inizializzo inizio e fine del giorno
        day_start = time_series[j][0] - (time_series[j][0] % 86400)
        day_end = day_start + 86400
        #inizializzo minimo massimo e media
        mi = time_series[j][1]
        ma = time_series[j][1] 
        med = 0
        d = 0
        #calcolo minimo massimo e media giorno per 
        #giorno
        while (j < len(time_series) and time_series[j][0] < day_end):
            if(mi > time_series[j][1]):
                mi = time_series[j][1]
            if (ma < time_series[j][1]):
                ma = time_series[j][1]
            med += time_series[j][1]
            d += 1
            j += 1
        med = med/d
        #creo lista in cui inserire i valori 
        #ottenuti
        stat=[mi,ma,med]
        #inserisco lista in quella finale
        a.append(stat)
    return a

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
d_stats=daily_stats(time_series)
for i in range(len(d_stats)):
    print(d_stats[i],"\n")
print(len(d_stats))

