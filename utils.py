#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 0024 14:12
# @Author  : Hadrianl 
# @File    : utils.py
# @Contact   : 137150224@qq.com

import logging
import sys
_format = "%(asctime)-15s [%(levelname)s] [%(name)s] %(message)s"
_datefmt = "%Y/%m/%d %H:%M:%S"
_level = logging.DEBUG

handlers = [logging.StreamHandler(sys.stdout)]

logging.basicConfig(format=_format, datefmt=_datefmt, level=_level, handlers=handlers)
KLine = ['1min', '5min', '15min', '30min', '60min', '1day', '1mon', '1week', '1year']