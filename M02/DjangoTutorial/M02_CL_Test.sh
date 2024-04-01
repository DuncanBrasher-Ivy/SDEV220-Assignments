#!/usr/bin/env bash

mkdir -p M02_CL_Test
cd M02_CL_Test

mkdir -p myfolder
cd myfolder
touch mytext1.txt
touch moveme.txt
cd .. && touch parenttext.txt # Hey, the instructions said change directory and create file and were written on the same line! What more do you wantU+203D
mv myfolder/moveme.txt ./

