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

2. POST /create

* It has two query parameter
  * number - number of lifts
  * floors - number of floors
  * return a message if lifts are created (200 ok)
* no payload

3. PUT moveUp/

* It takes two parameter 
    next_floor - next floor for closest lift 
    group - which group does lift belong to
* returns the closest lift with updated floor
* no payload

4. PUT door/:id
 
 * Takes lift id as a parameter
 * update door_open attributes to true or false depends on the motion of the lift with the given id
 * returns the lift with updated data

5. PUT move/:id 
 
 * Take id as a parameter 
 * update in_motion attribute to toggle the whether the lift has stopped or moved
 * returns the lift with updated data
  