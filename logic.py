#!/usr/bin/env python
# -*- coding: utf-8 -*-

def question(text):
    if text == "Привет":
        return "Здравствуй"
    if text.upper() == "HI":
        return "Hello"
    return "Вы сказали " + text
