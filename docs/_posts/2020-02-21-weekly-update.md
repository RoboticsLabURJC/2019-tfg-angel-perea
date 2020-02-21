---
title: "Weekly Update 2020 02 17"
excerpt: "2020 02 17"

sidebar:
  nav: "docs"

toc: true
toc_label: "Navigation"
toc_icon: "cog"


categories:
- Progress
tags:
- python
- django
- logs
- plotting
- Elasticsearch
- git
- ip
author: Angel Perea Arias
pinned: true
---

## 1. Fixing IP Image
With the change to python 3.X I lose the compatibility with the module i was using to access latitude and longitude, I parched it making HTTP requests to IPInfo.com but it was really slow, fixed it this week with a new package (geolite2 for python3) easier to use and way faster to retrieve data.

## 2. Recover LOGS Script
With the DDBB change to the ELK Stack we had to migrate our data, by doing this i avoid to lose too many valuable data. But with the recent ejercise ID changes had to fix the ones I had, this also has been fixed, and will be in the production DDBB soon.

## 3. Improving local installation recipe
I've added a few lines with a problem I've encountered on the various installations of Kibotics I've done.

## 4. New view and new Data stored.
Now Kibotics It's saving the visit of annonimous users to the page, with this data I've made a new view with a world map and statistics of weekly and hourly visits
