# Flowchart

**Standard symbols:** `( )` Start/Stop, `/ /` Input/Output, `[ ]` Process, `< >` Decision.

```text
              ( START )
                  |
                  v
          / Input two numbers /
                  |
                  v
            / Input operator /
                  |
                  v
             < Operator = +? >
              /          \
            Yes           No
             |             |
             v             v
       [ Add numbers ] < Operator = -? >
                           /       \
                         Yes        No
                          |          |
                          v          v
                 [ Subtract ] < Operator = *? >
                                  /       \
                                Yes        No
                                 |          |
                                 v          v
                         [ Multiply ] < Operator = /? >
                                        /       \
                                      Yes        No
                                       |          |
                                       v          v
                                  [ Divide ] [ Invalid operator ]
                                       \          /
                                        \        /
                                         v      v
                                    / Display result /
                                           |
                                           v
                                        ( STOP )
```
