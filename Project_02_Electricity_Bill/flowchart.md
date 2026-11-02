# Flowchart

**Standard symbols:** `( )` Start/Stop, `/ /` Input/Output, `[ ]` Process, `< >` Decision.

```text
        ( START )
            |
            v
   / Input units /
            |
            v
      < Units <= 100? >
        /          \
      Yes           No
       |             |
       v             v
[ Bill = units*1 ] < Units <= 200? >
                     /          \
                   Yes           No
                    |             |
                    v             v
       [ Bill = 100 +          [ Bill = 300 +
         (units-100)*2 ]        (units-200)*3 ]
                    \             /
                     \           /
                      v         v
                    / Display bill /
                         |
                         v
                      ( STOP )
```
