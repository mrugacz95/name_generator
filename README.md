# Name generator

Simple script for generating fictional names based on Markov Chains. 

Script based on polish names from names.csv but it is possible to provide any languages names.

### Examples:

* Bosłom
* Drysłarda
* Jakseorotyszy
* Hanabobr
* Słamielewafanir
* Bolcy
* Girowarel chisąc
* Gomisłau
* Kamiz
* Kaczyszybosła
* Wieroraw
* Ewen
* Emangości
* Fresła
* Słanfausare
* Lanawatynd
* Ścet
* Sawa
* Desłantys

### Usage
```
$ python generator.py -h
usage: generator.py [-h] [-p] [-i INPUT] n

positional arguments:
  n                     Number of generated names

optional arguments:
  -h, --help            show this help message and exit
  -p, --plot            Show plot representing probability of changing to
                        another letter
  -i INPUT, --input INPUT
                        Path to csv with names
```