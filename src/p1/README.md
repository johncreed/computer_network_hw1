# Prerequisites

1. Use python3.x

# How to run server

```python
python socket_server.py
```

Server will be hosted on **127.0.0.1::5000**

# How to connect to server

```python
python client_server.py
```

# Funcion supported by server

Definition:
```text
NONZERO = ([1-9][0-9]*) | (0.[0-9]*[1-9])  | ([1-9][0-9]*.[0-9]+)
NUM = NONZERO | 0
INT = ([1-9]+[0-9]*) | 0
```

| Operator name | Operator | Format | Example |  Result |
|---------------|----------|--------|---------|---------|
| Plus | + | NUM + NUM | 2 + 3 | 5 |
| Minus | - | NUM - NUM | 1 - 1 | 0 |
| Multiply | * | NUM * NUM | 1 * 2 | 2 |
| Divide | / | NUM / NONZERO | 1 / 2 | 0.5 |
| Power | ** | INT ** INT | 2 ** 3 | 8 |
| Mod | % | INT % INT | 12 % 10 | 2 |
| AND | & | \[01\] & \[01\] | 1 & 1 | 1 |
| OR | \| | \[01\] \| \[01\] | 0 \| 1 | 1 |
| Factorial | ! | INT ! | 4 ! | 24 |

# Screenshot

## Plus:

![alt text](https://github.com/johncreed/computer_network_hw1/blob/master/screenshots/p1/plus.png)

## Minus:

![alt text](https://github.com/johncreed/computer_network_hw1/blob/master/screenshots/p1/minus.png)

## Multiply:

![alt text](https://github.com/johncreed/computer_network_hw1/blob/master/screenshots/p1/mult.png)

## Divide:

![alt text](https://github.com/johncreed/computer_network_hw1/blob/master/screenshots/p1/div.png)

## Power:

![alt text](https://github.com/johncreed/computer_network_hw1/blob/master/screenshots/p1/power.png)

## Mod:

![alt text](https://github.com/johncreed/computer_network_hw1/blob/master/screenshots/p1/mod.png)

## AND:

![alt text](https://github.com/johncreed/computer_network_hw1/blob/master/screenshots/p1/and.png)

## OR:

![alt text](https://github.com/johncreed/computer_network_hw1/blob/master/screenshots/p1/or.png)

## Factorial:

![alt text](https://github.com/johncreed/computer_network_hw1/blob/master/screenshots/p1/factorial.png)

