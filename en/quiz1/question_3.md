
--- question ---

---
legend: Question 3 of 3
---

You have created a game with a player that can move around, procedurally generated obstacles, increasing levels of difficulty, and a scoring system. If you wanted to let players save their game, which of the following is the smallest set of values you could store to recreate the game as they left it? This might not matter much in a game this size, but imagine you had millions of players, with thousands of pieces of information related to each of their characters — learning to save space like this is important!

--- choices ---

- ( ) The value of `frame_count`.

  --- feedback ---
`frame_count` is the key to a lot of the game's state at any given moment. A lot of the other numbers can be calculated from it, but not quite all of them.
  --- /feedback ---

- ( ) The values of `frame_count`, `level`, `score`, and the player's `x` and `y` coordinates.

  --- feedback ---
This is all the information you need to re-create the game at a given moment, but you can recreate some of these values from some of the others.
  --- /feedback ---

- (x) The value of `frame_count` and the player's `x` and `y` coordinates. 

  --- feedback ---
Correct! You can calculate everything you need to recreate the game state using `frame_count` — from which you can calculate `level` and `score` — and the player's `x` and `y` coordinates.
  --- /feedback ---

- ( ) The values of `frame_count`, `score`, and the player's `x` and `y` coordinates.


  --- feedback ---
You're close: you can calculate `level` from `score`, so you don't need to store it. However, you can calculate one more of these variables instead of storing it, too.
  --- /feedback ---

--- /choices ---

--- /question ---
