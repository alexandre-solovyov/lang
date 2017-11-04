#!/bin/bash -f

source env.sh
pylint datamodel > datamodel.pylint.log
cat datamodel.pylint.log
