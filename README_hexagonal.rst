python-chess-hexagonal: a Python library for hexagonal chess
========================================

**Long-term goal:** Help popularize Gliński's hexagonal chess by providing a broad-featured client that supports this variant, even if those features are not yet backed by data for hexagonal chess.

**Shorter long-term goal:** Modify a fork of the github repo niklasf/python-chess to support Gliński's hexagonal chess.

**Status:** Very, very early on. Not suitable for any kind of use.

For more on Gliński's hexagonal chess (e.g., piece movement and other rules), see the `Wikipedia page for <https://en.wikipedia.org/wiki/Hexagonal_chess>`.  Hereafter, for simplicity, we will call this variant Glinski chess, without the diacritical mark, and without the possessive.

**Q:** Why this parent repo in particular?
**A:** While the repo pychess/pychess is more popular, it is also broader and more loosely structured. The repo of niklasf seems to be a more likely vehicle to success. It supports these features:
  - Basic chess functionality (listing available moves, detecting checks, mates, absolute pins, board repetitions, etc.)
  - PGN parsing and writing
  - Polyglot opening book reading
  - Gaviota and Syzygy endgame tablebase use
  - UCI / XBoard communication
  - An existing structure for supporting chess variants using square boards.
  - SVG rendering in Jupyter notebooks

Terminology:
  - **Cell.**
    Since hexagonal boards do not have "squares", let's call its spaces "cells".
  - **Row.**
    Let's define a row as the cell of a board lying on the same West-East line.
    In classic chess, with its square board, this is the same thing as the squares sharing the same rank.
    In Glinski hexagonal chess, with its 91-cell board, there are 21 interleaved rows.

A Short List of Steps:
  - [DONE] Choose a system of hexagonal coordinates:
    * The lower-left (SW) corner from the perspective of White will have hex coords (0, 0).
    * hex0 will increase toward the bottom (S) corner.
    * hex1 will increase toward the upper-left (NW) corner.
    * Thus the corners of the board will have these hex coordinates:
      + A1  = SW corner: (0,   0)
      + A6  = NW corner: (0,   5)
      + F1  = S  corner: (5,   0)
      + F11 = N  corner: (5,  10)
      + L1  = SE corner: (10,  5)
      + L6  = NE corner: (10, 10)
    * Also, the (1-based, numeric) values of file and rank can be computed as follows:
      + file = hex0 + 1
      + rank = hex1 + 1 - (hex0 > 5 ? hex0 - 5 : 0)
      + So the center cell (F6, with hex coords (5, 5)) has file = 6 and rank = 6.
    * Let's define the row number of a cell as 2 * hex1 - hex0 - 5.
      Then the center cell in in row 0, the South corner (F1=(5,0)) is the lone cell in row -10, and the North corner (F11=(5,10)) is the lone cell in row 10.
  - [DONE] Adopt the algebraic move representation from the Wikipedia article on Hexagonal Chess.
  - [DONE, but not shown here] Design and implement a FEN representation.
  - [In progress] Board geometry. Move basic board-shape attributes to separare board-shape classes, such as BG_Square and BG_Hexagonal, where "BG" represents "Board Geometry".
  - [TODO] Add test-based hexagonal board representation.
  - [TODO] Add hexagonal analogs for the many algorithms (many using bit magic) in place for classic chess: move generation, check detection, Zobrist hashing to detect board duplication, etc.
  - [TODO] SVG: Write a hexagonal analog for the existing SVG support.
  - [TODO] UCI: Design a hexagonal analog for the existing UCI representation.

Performance consideration:
  - Adding a layer of indirection to support different board geometries polymorphically (e.g., self.bg = chess.BG_Square) will cause some performance hit to the classical board version. This will be benchmarked.
  - Hexagonal chess will not be able to use most high performance big magic techniques applied to classical chess. Thus game tree searches for hexagonal chess will likely be far slower than for classic chess.
