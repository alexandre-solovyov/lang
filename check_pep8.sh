#!/bin/bash -f

source env.sh
pep8 -v datamodel > datamodel.pep8.log
cat datamodel.pep8.log
