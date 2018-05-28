#!/usr/bin/env python
# -*- coding: utf-8 -*-

def question(text, chat_id):
    if text == "Привет":
        return "Здравствуй"
    if text.upper() == "HI":
        return "Hello"
    return "Вы сказали " + text + " Ваш чат айди " + str(chat_id)
