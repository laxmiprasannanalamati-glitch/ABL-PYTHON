# Flowchart

**Standard symbols:** `( )` Start/Stop, `/ /` Input/Output, `[ ]` Process, `< >` Decision.

```text
             ( START )
                 |
                 v
          / Input a, b, c /
                 |
                 v
        < a >= b AND a >= c? >
             /          \
           Yes           No
            |             |
            v             v
     [ largest = a ] < b >= a AND b >= c? >
                           /          \
                         Yes           No
                          |             |
                          v             v
                   [ largest = b ] [ largest = c ]
                          \             /
                           \           /
                            v         v
                         / Display largest /
                                |
                                v
                             ( STOP )
```
