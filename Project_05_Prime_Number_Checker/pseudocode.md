# Pseudocode

```text
START
INPUT n
SET prime = True

IF n < 2
    prime = False
ELSE
    FOR i from 2 to n - 1
        IF n % i = 0
            prime = False
            BREAK
        END IF
    END FOR
END IF

IF prime = True
    DISPLAY Prime Number
ELSE
    DISPLAY Not a Prime Number
END IF

STOP
```
