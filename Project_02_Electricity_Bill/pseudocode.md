# Pseudocode

```text
START
INPUT units

IF units <= 100
    bill = units * 1
ELSE IF units <= 200
    bill = 100 + (units - 100) * 2
ELSE
    bill = 300 + (units - 200) * 3
END IF

DISPLAY units and bill
STOP
```
