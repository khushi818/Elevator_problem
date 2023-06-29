# API Contract

1. GET /lift

* Takes no parameter or payload
* return all the lifts created by user 

```
    floor = the current floor in which the lift is 
    door_open - it is true when door open
    maintainence  - it is true if lift is in maintainance
    move_up - lift moves up if true
    in_motion - whether the lift is moving or not
    group_number - list of elevator in one group
    total_floors - number of floors present for each lift
```