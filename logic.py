#!/usr/bin/env python
# -*- coding: utf-8 -*-

names = {}
state = {}

maze = [
    [1,1,1,1,1,1,1,0,1,1,1,1],
    [1,1,1,1,1,0,0,0,1,1,1,1],
    [1,1,1,1,1,0,1,1,1,1,1,1],
    [1,1,1,0,0,0,1,1,1,1,1,1],
    [1,1,1,0,0,0,0,0,1,1,1,1],
    [1,1,1,1,1,1,0,1,1,1,1,1],
    [1,1,1,1,1,0,0,1,1,1,1,1],
    [1,1,1,1,1,0,1,1,1,1,1,1],
]


def position(coordinates, chat_id):
    x, y = coordinates["x"], coordinates["y"]
    walls = []
    if x > 0 and maze[y][x-1] == 1:
        walls.append("left")
    if x < len(maze[y])-1 and maze[y][x+1] == 1:
        walls.append("right")
    if y > 0 and maze[y-1][x] == 1:
        walls.append("above")
    if y < len(maze)-1 and maze[y+1][x] == 1:
        walls.append("below")
    if x == 0 or y == 0 or x == len(maze[0])-1 or y == len(maze)-1:
        return "Congratulations, " + names[chat_id] + "! You solved the maze!!! "
    return "Great! You are now at position " + str(coordinates) + "\n Walls: " + ",".join(walls)


def question(text, chat_id):
    if chat_id not in state:
        state[chat_id] = {"x": 4, "y": 4}
    if chat_id not in names:
        names[chat_id] = "?"
        return "Hi! what is your name?"
    if names[chat_id] == "?":
        names[chat_id] = text
        return "Hi, " + names[chat_id] + "! Nice to meet you! " + position(state[chat_id], chat_id)

    if text.upper() == "LEFT":
        if maze[state[chat_id]["y"]][state[chat_id]["x"]-1] == 1:
            return "Sorry, there is a wall to the left of you."
        state[chat_id] = {"x": state[chat_id]["x"]-1,"y":state[chat_id]["y"]}
        return position(state[chat_id], chat_id)

    if text.upper() == "RIGHT":
        if maze[state[chat_id]["y"]][state[chat_id]["x"]+1] == 1:
            return "Sorry, there is a wall to the right of you."
        state[chat_id] = {"x": state[chat_id]["x"]+1,"y":state[chat_id]["y"]}
        return position(state[chat_id], chat_id)

    if text.upper() == "UP":
        if maze[state[chat_id]["y"]-1][state[chat_id]["x"]] == 1:
            return "Sorry, there is a wall above you."
        state[chat_id] = {"x": state[chat_id]["x"],"y":state[chat_id]["y"]-1}
        return position(state[chat_id], chat_id)

    if text.upper() == "DOWN":
        if maze[state[chat_id]["y"]+1][state[chat_id]["x"]] == 1:
            return "Sorry, there is a wall below you."
        state[chat_id] = {"x": state[chat_id]["x"],"y":state[chat_id]["y"]+1}
        return position(state[chat_id], chat_id)

    return "Вы сказали " + text + " Ваш чат айди " + str(chat_id)
