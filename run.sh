#!/bin/bash

python3 ./i18n.py

msg="update"
if [ $# -ne 0 ]
  then
    $msg=$1
fi

git add --all
git commit -a -m "$msg"
git push
