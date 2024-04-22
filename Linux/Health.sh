#!/bin/bash

check_disk() {
    # $1 is the minimum free disk space percentage
    local min_free=$1
    local disk_usage=$(df / | grep / | awk '{ print $5 }' | sed 's/%//g')
    if [ "$disk_usage" -gt $((100 - min_free)) ]; then
        echo "Disk space is sufficient."
    else
        echo "Disk space critical: less than $min_free% free."
    fi
}

check_memory() {
    # $1 is the minimum free memory percentage
    local min_free=$1
    local memory_usage=$(free | grep Mem | awk '{ print $3/$2 * 100.0 }')
    if (( $(echo "$memory_usage > $min_free" | bc) )); then
        echo "Memory level is sufficient."
    else
        echo "Memory is low."
    fi
}

check_disk 20
check_memory 10
