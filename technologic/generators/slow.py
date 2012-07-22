from random import randint

def slow(duration):

    time = 0.0000
    data = []

    def random(max = 10, min = 0):
            return randint(min, max)


    while time <= duration:

        if time < 1:
            data.append({'time': time, 'beat' : time + random(50)})

        if 1 <= time < 2:
            data.append({'time': time, 'beat' : (time + random(100, 50))/2})

        if 2 <= time <= 8:
            data.append({'time': time, 'beat' : 20 - time})


        time = time + .5

    return data