#!#!/usr/bin/env bash
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
pushd $SCRIPTPATH
source ./virt-env/bin/activate

python .\obs-last-convert.py /path/to/clips mp4

popd
