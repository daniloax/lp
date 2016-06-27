import sqlite3
import datetime
import threading
import sys

def ring_ring():
    now = datetime.datetime.now()
    conn = sqlite3.connect('geraDB.db')
    cursor = conn.cursor()

    cursor.execute("""SELECT titulo,descricao FROM atividades 
    WHERE ano=? AND mes=? AND dia=? AND hora=? AND minuto=?
    """, (now.year,now.month,now.day,now.hour,now.minute))

    for test in cursor.fetchall():
        print("\n")
        sys.stdout.write(test[0])
        print("\n")
        sys.stdout.write(test[1])
        print("\n")

    cursor.execute("""UPDATE atividades SET alarme=2 WHERE hora=? AND minuto=?
    """, (now.hour,now.minute))
    conn.commit()

    sys.stdout.flush()

class Clock:
    def __init__(self):
        self.alarm_time = None
        self._alarm_thread = None
        self.update_interval = 1
        self.event = threading.Event()

    def run(self):
        stop = 0
        while True:
            self.event.wait(self.update_interval)
            if self.event.isSet():
                break
            now = datetime.datetime.now()
            if self._alarm_thread and self._alarm_thread.is_alive():
                alarm_symbol = '+'
            else:
                alarm_symbol = ' '
            sys.stdout.write("\r%02d:%02d:%02d %s" 
                % (now.hour, now.minute, now.second, alarm_symbol))
            sys.stdout.flush()

            if stop == 0:
                opcao = input("[S/N] = Manter? ")
                if any(opcao == X for X in ("S", "s")):
                    stop = 1
                    print("\n")
                elif any(opcao == Y for Y in ("N", "n")):
                    break
                else:
                    print("\nDigite S (sim) ou N (não)!\n")


    def set_alarm(self, year, month, day, hour, minute):
        now = datetime.datetime.now()
        print ("hora: ", now)
        alarm = now.replace(year=int(year), month=int(month), day=int(day), hour=int(hour), minute=int(minute))
        print ("alarme: ", alarm)
        delta = int((alarm - now).total_seconds())
        print ("valor delta: ", delta)
        if delta <= 0:
            alarm = alarm.replace(day=alarm.day + 1)
            delta = int((alarm - now).total_seconds())
        if self._alarm_thread:
            self._alarm_thread.cancel()
        self._alarm_thread = threading.Timer(delta, ring_ring)
        self._alarm_thread.daemon = True
        self._alarm_thread.start()



