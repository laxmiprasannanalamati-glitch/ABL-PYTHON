# Flowchart

```mermaid
flowchart TD
    A([START]) --> B[/Input units/]
    B --> C{Units <= 100?}
    C -- Yes --> D[Bill = units * 1]
    C -- No --> E{Units <= 200?}
    E -- Yes --> F[Bill = 100 + (units - 100) * 2]
    E -- No --> G[Bill = 300 + (units - 200) * 3]
    D --> H[/Display bill/]
    F --> H
    G --> H
    H --> I([STOP])
```
