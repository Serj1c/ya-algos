# 1. Сайт посетило N человек, для каждого известно время входа на сайт In(i)
# и время выхода с сайт Out(i). Считается, что человек был на сайте с момента
# In(i) по Out(i) включительно.
# Определить, какое максимальное количество человек было на сайте одновременно

def maxvisitorsonline(n, tin, tout):
    events = []
    for i in range(n):
        events.append((tin[i], -1))
        events.append((tout[i], 1))
    events.sort()

    online = 0
    maxonline = 0
    for event in events:
        if event[1] == -1:
            online += 1
        else:
            online -= 1
        maxonline = max(online, maxonline)

    return maxonline

# 2. Сайт посетило N человек, для каждого известно время входа на сайт In(i)
# и время выхода с сайта Out(i). Считается, что человек был на сайте с момента
# In(i) по Out(i) включительно
# Определить, какое суммарное время на сайте был хотя бы 1 человек

def timewithvisitors(n, tin, tout):
    events = []
    for i in range(n):
        events.append((tin[i], -1))
        events.append((tout[i], 1))
    events.sort()

    online = 0
    notemtytime = 0
    for i in range(len(events)):
        if online > 0:
            notemtytime += events[i][0] - events[i-1][0]
        if events[i][1] == -1:
            online += 1
        else:
            online -= 1
    
    return notemtytime

# 3. Сайт посетило N человек, для каждого известно время входа на сайт In(i)
# и время выхода с сайта Out(i). Считается, что человек был на сайте с момента
# In(i) по Out(i) включительно. Начальник заходил на сайт М раз в моменты
# времени Boss(i) и смотрел сколько людей сейчас онлайн. Посещение сайта
# начальником упорядочены по времени.
# Определилить какие показания счетчика людей онлайн увидел начальник

def bosscounters(n, tin, tout, m, tboss):
    events = []
    for i in range(n):
        events.append((tin[i], -1))
        events.append((tout[i], 1))

    for i in range(m):
        events.append((tboss[i], 0))
    events.sort()
    
    online = 0
    bossanswer = []
    for i in range(len(events)):
        if events[i][1] == -1:
            online += 1
        elif events[i][1] == 1:
            online -= 1
        else:
            bossanswer.append(online)
    
    return bossanswer

# 4. На парковке в ТЦ N мест (пронумерованных от 1 до N). За день в ТЦ
# приезжало М автомобилей, при зтом некоторые из них длинные и занимали
# несколько подряд идущих парковочных мест. Для каждого автомобиля известно
# время приезда и отьезда, а также два числа - с какого по по какое парковочное
# место он занимал. Если в какой-то момент времени один автомобиль уехал с 
# парковочного места, то место считается освободившимся и в тот же момент на 
# времени на его место может встать другой.
# Необходимо определить, был ли момент, в который были заняты все парковочные места

def isparkingfull(cars, n):
    events = []
    for car in cars:
        timein, timeout, placefrom, placeto = car
        events.append((timein, 1, placeto - placefrom + 1))
        events.append((timeout, -1, placeto - placefrom + 1))
    events.sort()

    occupied = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
        elif events[i][1] == 1:
            occupied += events[i][2]
        if occupied == n:
            return True

    return False

# 5. На парковке в ТЦ N мест (пронумерованных от 1 до N). За день в ТЦ
# приезжало М автомобилей, при зтом некоторые из них длинные и занимали
# несколько подряд идущих парковочных мест. Для каждого автомобиля известно
# время приезда и отьезда, а также два числа - с какого по по какое парковочное
# место он занимал. Если в какой-то момент времени один автомобиль уехал с 
# парковочного места, то место считается освободившимся и в тот же момент на 
# времени на его место может встать другой.
# Необходимо определить, был ли момент, в который были заняты все парковочные места
# и определить минимальное количество автомобилей, которое заняло все места. Если 
# такого момента не было - вернуть М + 1

def mincarsonfullparking(cars, n):
    events = []
    for car in cars:
        timein, timeout, placefrom, placeto = car
        events.append((timein, 1, placeto-placefrom+1))
        events.append((timeout,-1,placeto-placefrom+1))
    events.sort()
    
    occupied = 0
    nowcars = 0
    mincars = len(cars)+1

    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
        if occupied == n:
            mincars = min(mincars, nowcars)
    return mincars

# 5. На парковке в ТЦ N мест (пронумерованных от 1 до N). За день в ТЦ
# приезжало М автомобилей, при зтом некоторые из них длинные и занимали
# несколько подряд идущих парковочных мест. Для каждого автомобиля известно
# время приезда и отьезда, а также два числа - с какого по по какое парковочное
# место он занимал. Если в какой-то момент времени один автомобиль уехал с 
# парковочного места, то место считается освободившимся и в тот же момент на 
# времени на его место может встать другой.
# Необходимо определить, был ли момент, в который были заняты все парковочные места
# и определить минимальное количество автомобилей, которое заняло все места, а также
# номера этих автомобилей (в том порядке, как они перечисляются в списке). Если 
# парковка никогда не была занята полностью вернуть пустой список

def mincarsonfullparkingbadsolution(cars, n):
    events = []
    for i in range(len(cars)):
        timein, timeout, placefrom, placeto = cars[i]
        events.append((timein, 1, placeto-placefrom+1, i))
        events.append((timeout,-1,placeto-placefrom+1, i))
    events.sort()
    
    occupied = 0
    nowcars = 0
    mincars = len(cars)+1
    carnums = set()
    bestcarnums = set()

    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
            carnums.remove(events[i][3])
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
            carnums.add(events[i][3])
        if occupied == n and nowcars < mincars:
            bestcarnums = carnums.copy()
            mincars = nowcars
    return bestcarnums

def mincarsonfullparkinggoodsolution(cars, n):
    events = []
    for i in range(len(cars)):
        timein, timeout, placefrom, placeto = cars[i]
        events.append((timein, 1, placeto-placefrom+1, i))
        events.append((timeout,-1,placeto-placefrom+1, i))
    events.sort()
    
    occupied = 0
    nowcars = 0
    mincars = len(cars)+1
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
        if occupied == n and nowcars < mincars:
            mincars = nowcars
    
    carnums = set()
    nowcars = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -=  events[i][2]
            nowcars -= 1
            carnums.remove(events[i][3])
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
            carnums.add(events[i][3])
        if occupied == n and nowcars == mincars:
            return carnums
    return set()