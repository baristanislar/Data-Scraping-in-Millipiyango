# Data Scraping in Millipiyango

I still develop this project.

## Table of contents
* [Overview](#overview)
* [Requirements](#requirements)
* [Installation](#installation)
* [Configuration](#configuration)

## Overview
This project is allows you to scrape data of lottery numbers on the https://www.millipiyangoonline.com/sayisal-loto website.

## Requirements
* Python 3.9+
* Selenium
* Google Chrome Driver

## Installation

firstly, let's start installation selenium.
```
pip install selenium
```
then, we need google chrome driver to use Selenium.
download driver from here:
https://chromedriver.chromium.org/downloads

if you get error from google chrome driver 
check your google chrome version. Then download your chrome version.

## Configuration

```
driver = Chrome(executable_path='Your Google Chrome Driver PATH')
```
use notepad++ or any ide for python and configure your google chrome driver folder location. (don't forget this step)

```
#driver.set_window_position(-10000,0)
```
While code running if you don't want see google chrome page you must delete hashtag. (Default is page in visible )

```
aylar = Select(driver.find_element_by_id("draw-month"))
aylar.select_by_value("3")
```
which select the month for searching in here. ("1"=January,"2" = February ...)

```
yillar = Select(driver.find_element_by_id("draw-year"))
yillar.select_by_value("2021")
```
which select the year for searching in here.

then run the code
