# Flowchart

**Standard flowchart symbols:**
- `( )` = Start / Stop
- `/ /` = Input / Output
- `[ ]` = Process
- `< >` = Decision

```text
              ( START )
                  |
                  v
        / Input name and marks /
                  |
                  v
        [ Calculate total ]
                  |
                  v
        [ Calculate average ]
                  |
                  v
           < Average >= 90? >
             /           \
          Yes             No
           |               |
           v               v
      [ Grade = A ]  < Average >= 75? >
                         /        \
                      Yes          No
                       |            |
                       v            v
                 [ Grade = B ] < Average >= 60? >
                                  /        \
                               Yes          No
                                |            |
                                v            v
                          [ Grade = C ] < Average >= 50? >
                                             /       \
                                          Yes         No
                                           |           |
                                           v           v
                                     [ Grade = D ] [ Grade = F ]
                                           \           /
                                            \         /
                                             v       v
                                      / Display result /
                                             |
                                             v
                                          ( STOP )
```

This flowchart uses the standard Start/Stop, Input/Output, Process, and Decision symbols taught in basic programming flowcharts.
