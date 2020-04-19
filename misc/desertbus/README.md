# misc - desertbus

## Challenge
Why use a high priority bus when you can take the ascii taxi instead? If you get
to the end you get a flag. (might take 3 hours)

ssh ctf@desertbus.wpictf.xyz password: desertbus

made by rm -k

## Solution
At fiest `screen` - ssh connection to the host. At second `screen` I will keep
running simple script to control first `screen`.

Maintain position when game moves you up:
```
while true; do screen -S screenName -p 0 -X stuff "s"; sleep 2; done
```

Maintain position when game moves you down:
```
while true; do screen -S screenName -p 0 -X stuff "w"; sleep 2; done
```

Additionally, swing up and down to avoid obstacles (pseudocode):
```
while true; do up; sleep 0.5; up; sleep 0.5; [...]; sleep 5; down; sleep 0.5;
down; sleep 0.5; [...]; sleep 5; done
```

Result:
```
Password:
Use WASD to drive the car.

Score: 108000

------------------------------------------------------------------------------
 ______
 /|_||_\`._
(         _\                           X
=`-(_)--(_)-'                          X
                                       X
                                       X
                                       X
                                       X
 - - - - - - - - - - - - - - - - - - - -X- - - - - - - - - - - - - - - - - - -
                                       X
WPI{f@R3_i$_tr33_fIddie}
Connection to desertbus.wpictf.xyz closed.
```

## Flag
```
WPI{f@R3_i$_tr33_fIddie}
```
