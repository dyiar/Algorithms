#!/usr/bin/python

import sys

def rock_paper_scissors(n, result = []):
  answers = []
  rps = ["rock", "paper", "scissors"]

  def find_outcomes(turns_left, result = []):
    if turns_left == 0:
      answers.append(result)
      return

    for i in rps:
      find_outcomes(turns_left-1, result + [i])

  find_outcomes(n)
  return answers


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')