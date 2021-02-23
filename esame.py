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
            #per ogni linea separo epoch e temperatura
            valore = line.split(",") 
            #controllo che i valori epoch siano interi e che quelli di temperatura siano floating point
            try:
                data = round(float(valore[0]),0)
                temp = float(valore[1])
            except:
                continue
            #assegno valori alla lista
            values.append([data,temp])
        #controllo che i valori epoch siano ordinati e non duplicati
        for i in range(len(values)-1):
            if values[i][0] >= values[i+1][0]:
                raise ExamException ('errore, timestamp epoch fuori ordine o duplicato')
        return values

def hourly_trend_changes(time_series):
    i = 1
    d = 0
    #creo lista 
    trend_change = []
    while (i<len(time_series)-1):
        #inizializzo inizio e fine dell'ora
        hour_start = time_series[i][0] - (time_series[i][0] % 3600)
        hour_end = hour_start + 3600
        #inizializzo andamento a None
        andamento=None
        #inizializzo a zero contatore parziale
        d=0
        #calcolo cambiamenti di andamento ora per ora
        while (i<len(time_series)-1 and time_series[i][0]<hour_end):
            #se andamento uguale a None salvo il primo andamento e passo alla seconda iterazione
            if (andamento==None):
                if (time_series[i-1][1]<time_series[i][1]):
                    andamento=1
                if (time_series[i-1][1]>time_series[i][1]):
                    andamento=0
                i+=1
            #salvo andamento parziale
            else:
                if (time_series[i-1][1]<time_series[i][1]):
                    andamento_parz=1
                if (time_series[i-1][1]>time_series[i][1]):
                    andamento_parz=0
                #confronto andamento parziale con quello precedente
                if (andamento_parz!=andamento):
                    #se sono diversi incremento il contatore parziale
                    d+=1
                #salvo andamento attuale per il confronto successivo
                andamento=andamento_parz
                i+=1
        #inserisco i dati ottenuti nella lista
        trend_change.append(d)
    return trend_change
    
time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
cambio_trend=hourly_trend_changes(time_series)
for i in range(len(cambio_trend)):
    print(cambio_trend[i],"\n")





