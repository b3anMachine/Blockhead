#!/usr/bin/python

import re
import sys

binary_term = re.compile("(\w+)\(([\d\w]+),([\d\w]+)\)")

def display_maze(facts):
  """turn a list of ansprolog facts into a nice ascii-art maze diagram"""
  max_x = 1
  max_y = 1
  blockOnGoal = {}
  playerOnGoal = {}
  goal = {}
  block = {}
  player = {}
  floor = {}
  wall = {}  
  
  for fact in facts:
    m = binary_term.match(fact)
    if m:
      functor, x, y = m.groups()
      x, y = int(x), int(y)
      pos = (x,y)
      max_x, max_y = max(x, max_x), max(y, max_y)
      if functor == "blockOnGoal":
        blockOnGoal[pos] = True
      elif functor == "playerOnGoal":
        playerOnGoal[pos] = True
      elif functor == "goal":
        goal[pos] = True
      elif functor == "block":
        block[pos] = True
      elif functor == "player":
        player[pos] = True        
      elif functor == "floor":
        floor[pos] = True
      elif functor == "wall":
        wall[pos] = True        
        
  def code(x,y):
    """decide how a maze cell should be tpyeset"""
    pos = (x,y)
    if pos in blockOnGoal:
      return "*"
    if pos in playerOnGoal:
      return "+"
    if pos in goal:
      return "."
    if pos in block:
      return "$"
    if pos in player:
      return "@"
    if pos in floor:
      return " "
    if pos in wall:
      return "#"
    else:
      return "E"

  for y in range(1,max_y+1):
    print "".join([code(x,y)*1 for x in range(1,max_x+1)])

def main():
  """look for lines that contain logical facts and try to turn each of those
  into a maze"""
  for line in sys.stdin.xreadlines():
    line = line.strip()
    if line:
      if line[0].islower():
        facts = line.split(' ')
        display_maze(facts)
      else:
        print "% " + line

if __name__ == "__main__":
  main() 