#!/bin/bash

cd $(echo $0 | rev | cut -d'/' -f2- | rev)

./main.py