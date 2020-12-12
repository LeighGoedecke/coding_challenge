#!/usr/bin/env bash

BASEDIR=`dirname "$0"`
PYTHON_BASEPATH=$BASEDIR/..
export PYTHONPATH=$PYTHON_BASEPATH/resources:$PYTHON_BASEPATH/test:$PYTHON_BASEPATH/src:$PYTHON_BASEPATH

python3 src/main.py