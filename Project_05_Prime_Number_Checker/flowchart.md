# Flowchart

**Standard symbols:** `( )` Start/Stop, `/ /` Input/Output, `[ ]` Process, `< >` Decision.

```text
             ( START )
                 |
                 v
             / Input n /
                 |
                 v
          [ prime = True ]
                 |
                 v
             < n < 2? >
             /        \
           Yes         No
            |           |
            v           v
      [ prime = False ] [ Start loop: i = 2 ]
            |                   |
            |                   v
            |            < n divisible by i? >
            |              /             \
            |            Yes              No
            |             |                |
            |             v                v
            |       [ prime = False ] < More values? >
            |             |             /       \
            |             |           Yes        No
            |             |            |           |
            |             |            v           |
            |             |       [ Next i ]       |
            |             |            |           |
            |             |____________|           |
            |                                      |
            \____________________  _______________/
                                 \/
                           < prime = True? >
                             /          \
                           Yes           No
                            |             |
                            v             v
                     / Display Prime / / Display Not Prime /
                            \             /
                             \           /
                              v         v
                              ( STOP )
```
