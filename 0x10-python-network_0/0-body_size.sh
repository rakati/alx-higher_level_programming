#!/usr/bin/env bash
# get size of response body
curl -Is "$1" | grep -w '^Content-Length:' | cut -d ' ' -f2
