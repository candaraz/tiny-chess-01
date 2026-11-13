# tiny-chess-01: a 4 KB chess engine in Python

`main.py` (at most 4,096 bytes) is the whole engine: a 0x88 board, full
legal move generation (castling, en passant, queen promotion), alpha-beta
search with iterative deepening, null-move pruning, quiescence with SEE
and delta pruning, MVV-LVA + history move ordering, and material +
piece-square evaluation — under a fixed 40,000-node budget per move, no
clock, no randomness, so every trial replays move for move. It plays
the house gauntlet through the env at `MAKEFUN_ENV_URL`.
