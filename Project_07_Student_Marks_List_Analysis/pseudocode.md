# Pseudocode

```text
START
INPUT 5 marks
CREATE marks list

SET highest = first mark
SET lowest = first mark
SET total = 0

FOR each mark in marks
    total = total + mark
    IF mark > highest
        highest = mark
    END IF
    IF mark < lowest
        lowest = mark
    END IF
END FOR

average = total / 5
DISPLAY marks, highest, lowest, average
STOP
```
