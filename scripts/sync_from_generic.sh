#!/usr/bin/env bash
PROJECT="collective.js.leaflet"
IMPORT_URL="git@github.com:collective/collective.js.leaflet.git"
cd $(dirname $0)/..
[[ ! -d t ]] && mkdir t
rm -rf t/*
tar xzvf $(ls -1t ~/cgwb/$PROJECT*z) -C t
files="
base.cfg
"
for f in $files;do
    rsync -aKzv t/$PROJECT/$f $f
done
rm -rf t/*
# vim:set et sts=4 ts=4 tw=80: 
