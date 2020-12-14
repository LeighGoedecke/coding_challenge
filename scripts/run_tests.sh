#!/usr/bin/env bash

BASEDIR=`dirname "$0"`
PYTHON_BASEPATH=$BASEDIR/..
export PYTHONPATH=$PYTHON_BASEPATH/test:$PYTHON_BASEPATH/src:$PYTHON_BASEPATH


echo 'Running tests'
python3 test/test_DataStore.py
python3 test/test_SearchEngine.py
python3 test/test_functional.py
python3 test/test_DataReader.py
python3 test/test_UserInterface.py