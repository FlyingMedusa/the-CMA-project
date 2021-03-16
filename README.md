# the Cognitive Metaphor Analysis

## Table of contents

* General info
* General technologies
* Full requirements
* An advised form of setup
* Screenshots

## General info

The Cognitive Metaphor Analysis is a program in a form of a web page that aims to provide frequencies of:

- mappings of target and source domains
- target domains
- source domains

Moreover, the CMA generates three exploded pie charts that present abstractness of the analyzed domains.

(The screenshots can be seen below the readme description)

## General technologies

- Python & Flask & Jinja2 + HTML & CSS

## Full requirements

Unsurprisingly, the requirements can be found in the <strong>requirements.txt</strong> file. However, at this moment not all of the libraries are necessary. The project is still under development as I plan to switch from uploading the .xls file to .csv (which data would be inserted into an SQL database). The page is to be deployed on Heroku in the near future.

## An advised form of setup

- create a virtual environment with the libraries from the requirements.txt and activate it
- run core.py through the cmd - 
- the full instruction on how to use the CMA if provided for future users on the home page

### A small remark:

It is important to add an empty folder named 'files' in the 'static' folder.

## Screenshots

![HOME PAGE](./screens/01main.jpg)

![UPLOAD PAGE](./screens/02upload.jpg)

![DATA 01](./screens/03data01.jpg)

![DATA 02](./screens/04data02.jpg)
