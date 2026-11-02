# Flowchart

**Standard flowchart symbols:** `( )` Start/Stop, `/ /` Input/Output, `[ ]` Process, `< >` Decision.

```text
          ( START )
              |
              v
       / Input list elements /
              |
              v
      [ Create empty unique list ]
              |
              v
        [ Take next item ]
              |
              v
       < Item in unique list? >
          /              \
        Yes               No
         |                 |
         |                 v
         |          [ Add item to unique ]
         |                 |
         +--------+--------+
                  |
                  v
            < More items? >
             /          \
           Yes           No
            |             |
            v             v
     [ Take next item ] / Display lists /
            |             |
            +-------------+
                          v
                       ( STOP )
```

This uses the standard Start/Stop, Input/Output, Process, and Decision symbols.
