# DBPersona - Python data generator with PESEL number.
This is a Python console application that generates custom data for filling a MySQL database. The generated data includes PESEL numbers, which are unique identification numbers used in Poland. The script has been tested with up to 10,000 unique values, although it has the capability to generate more records. However, due to limitations in the script, it is only able to generate up to 10,000 unique values at a time. The generated data can be saved to a CSV file for use in the MySQL database.
## How does it work?
* <b>Provide the required number of records.</b><br>
![Welcome screen](/Demo_images/dbpersona.jpg)
* <b>Records created and saved into CSV file.</b>

* <b> Unique PESEL values </b>
PESEL is an acronym that stands for Powszechny Elektroniczny System Ewidencji Ludności, which means Universal Electronic System for Registration of the Population in Polish. It is a unique identification number used in Poland for tracking the personal information of individuals, including their name, date of birth, place of birth, and gender. PESEL numbers are used for a variety of purposes in Poland, such as for social security, healthcare, and voting. They are assigned to all Polish citizens and legal residents at birth or upon arrival in Poland.
PESEL numbers meaning:

YYMMDDPPPPC

YY – last 2 numbers of year of birth,

MM – month of birth (birth year > 1999, add 20 to month value. for example: August (08) + 20 = 28)

DD – day of birth,

PPPP – polish pesel gender number (odd number is for male, even – for female)

C - control value

## Requirements
1. Modify <b>dbpersona_config.ini</b> and provide paths to wordlists files, and path where to save data file.
2. Tested on Ubuntu 22.04. There may be some issues with encoding when using this application on different operating systems.

## License
This project is licensed under the ISC License - see the LICENSE.md file for details

### Authors
M.Witczak

### External scripts used
<b>"removeAccents" credits to Igor Zubrycki</b>
https://gist.github.com/AdoHaha/a76157c6de5155bf6b0adc77988724d9



