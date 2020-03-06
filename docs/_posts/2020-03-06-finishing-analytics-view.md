---
title: "Finishing the Analytics view"
excerpt: "2020 03 06"

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

## 1. Changing the LOGS format
Previously the events were saved into two different logs, one registering the beginning of it ant another one for the finishing of certain activity, a session or a simulation, this now is changed, with Elasticsearch its easier to unify this logs. With this we achieve a much faster processing avoiding unnecessary and tedious matching between the logs. The new logs have three new parameters (start_date, end_date and duration)  replacing the previous date.

## 2. Adapting the code to the new LOG format
The code is now much simpler, it's unnecessary match the exit event to the start event and calculate the duration of the session/simulation, now simply iterate through the search data and extract the useful information.

## 3. Even more data stored
the previous user_agent field has been replaced with data from the Operative System, the browser and the device the client is using. With this I've done 3 pie charts representing the percentage of each value for each parameter.  

{% capture fig_img %}
![Foo]({{ '/assets/images/posts/pieCharts.png' | relative_url }})
{% endcapture %}

<figure>
  {{ fig_img | markdownify | remove: "<p>" | remove: "</p>" }}
  <figcaption>Pie Charts of User Agent data.</figcaption>
</figure>
