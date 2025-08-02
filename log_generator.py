import time, random
from datetime import datetime

users = ['rawan', 'habiba', 'mohamed', 'omar']
actions = ['book', 'cancel', 'update']
trains = ['Train_901', 'Train_1102', 'Train_876']
classes = ['First', 'Second', 'Sleeper']
stations = ['Cairo', 'Alex', 'Aswan', 'Tanta', 'Mansoura']

def generate_log():
    user = random.choice(users)
    action = random.choice(actions)
    train = random.choice(trains)
    cls = random.choice(classes)
    from_station = random.choice(stations)
    to_station = random.choice([s for s in stations if s != from_station])
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"USER: {user} - ACTION: {action} - TRAIN: {train} - CLASS: {cls} - FROM: {from_station} - TO: {to_station} - DATE: {date}"

while True:
    log = generate_log()
    with open("train_booking.log", "a") as f:
        f.write(log + "\n")
    time.sleep(1)
