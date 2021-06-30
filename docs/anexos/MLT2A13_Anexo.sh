#!/bin/bash
VAR=13
echo $VAR
unset VAR
echo ${VAR:-5}
echo $VAR