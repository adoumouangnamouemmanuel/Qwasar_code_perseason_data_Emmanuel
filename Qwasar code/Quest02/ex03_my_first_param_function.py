def detonation_in(timer):
    seconds_left = timer
    print("detonation in... "+str(seconds_left)+" secondes.")

timer = 10
while timer >0:
    detonation_in(timer)
    timer = timer - 1