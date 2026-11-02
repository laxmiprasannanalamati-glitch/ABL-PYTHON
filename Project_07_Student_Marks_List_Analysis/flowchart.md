# Flowchart

**Standard symbols:** `( )` Start/Stop, `/ /` Input/Output, `[ ]` Process, `< >` Decision.

```text
             ( START )
                 |
                 v
          / Input 5 marks /
                 |
                 v
 [ Set highest, lowest and total ]
                 |
                 v
          [ Take next mark ]
                 |
                 v
          [ Add mark to total ]
                 |
                 v
          < Mark > highest? >
             /          \
           Yes           No
            |             |
            v             |
     [ Update highest ]   |
            |             |
            +-------> < Mark < lowest? >
                         /          \
                       Yes           No
                        |             |
                        v             |
                 [ Update lowest ]   |
                        |             |
                        +-------> < More marks? >
                                      /       \
                                    Yes        No
                                     |          |
                                     v          v
                              [ Take next mark ] [ Calculate average ]
                                     |          |
                                     +          v
                                          / Display results /
                                                 |
                                                 v
                                              ( STOP )
```
