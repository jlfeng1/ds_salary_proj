#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:02:05 2021

@author: erhao
"""

import glassdoor_scraper as gs
import pandas as pd
path = "/Users/erhao/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 15, False, path, 15)