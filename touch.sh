#!/bin/bash
echo "Please enter your name"
read NAME
echo "Please enter your age"
read AGE
echo "Please enter your favourite programming language"
read LANGUAGE

touch user_info.py
echo full_name=$NAME >> user_info.py
echo age=$AGE >> user_info.py
echo favourite_language=$LANGUAGE >> user_info.py
python3 user_info.py

