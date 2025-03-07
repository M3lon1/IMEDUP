This repository contains the source code for the university project IMEDUP from the Bauhaus University in Weimar.

## Problem Description
Given a set of images, locate the ones that are essentially copies of each other.
Pick out the one that seems to be the “original”

## Our Part
In this repository you will find an attempt to solve one part of the problem. We focus on finding duplicates of each other and comparing pictures to identify which ones are very similar to each other.

## Methodes
For each picture eighter a visual hash or a cryptographic hash is calculated. After the hashes are calculated they are stored in a database and compared against each other.
We use cryptographic hasing to identify similar pictures and visual hashing to find similar pictures.

## Problems
Visual hashing tries to be robust against certain types of modification like rotation, cropping, color changes ... 
Most of the visual hashing functions that we found lack to be robust against large rotations. 

## Solution
We tried to implement a pipeline that deals with the problem of identifying similar pictures with large rotations

## Pipeline
![Drag Racing](doc/Pipeline_sketch.drawio.png)

We take one picture and rotate it around a given angle, n times. 
Then we calculate a hash value for each picture and store it in a database.
We do this for every picture in a given dataset that we want to analyse. 
After the Database is filled up with all the hash values of all the images and their rotations, we compare the hash values against eacht other to find out which ones are close to each other