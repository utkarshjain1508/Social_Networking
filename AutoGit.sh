#!/bin/bash

git config credential.helper store
git push origin master	

git config --global credential.helper 'cache --timeout 36000'

git pull origin master

echo "Enter the Commit Name"
read mycommit
#echo $mycommit
git add .
git commit -m "$mycommit"
git push origin master
