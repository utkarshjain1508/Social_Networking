#!/bin/bash

myname=$

git config credential.helper store
git push origin master	

while [[ true ]]; do
	git add .
	git commit -m "$USER $(date)"
	git push origin master

	sleep 120
	git pull origin master
	sleep 120
done
