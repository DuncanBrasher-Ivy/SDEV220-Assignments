#!/usr/bin/env bash

# Since the Canvas listing won't let me submit a link, I'm uploading this file instead. Here's the link I'd have used: https://github.com/DuncanBrasher-Ivy/SDEV220-Assignments/blob/main/M02/DjangoTutorial/M02_CL_Test.sh

mkdir -p M02_CL_Test
cd M02_CL_Test

mkdir -p myfolder
cd myfolder
touch mytext1.txt
touch moveme.txt
cd .. && touch parenttext.txt # Hey, the instructions said change directory and create file and were written on the same line! What more do you wantU+203D
mv myfolder/moveme.txt ./

