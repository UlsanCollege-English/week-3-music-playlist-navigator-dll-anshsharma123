[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/0OQ6FX4F)
# Music Playlist Navigator (DLL)

## Story (why this matters)
You’re building a lightweight music app. Users press **next/prev**, can **insert**
a surprise track **after the current song**, and can **remove** the current song
without breaking navigation. You’ll model the playlist so movement is smooth.

## Technical description (what to build)
In `src/playlist.py`, implement a **doubly linked list** playlist with a cursor:

- `add_song(title)` → append at end
- `play_first()` → set `current = head`, return title or `None`
- `next()` → move right if possible; return title or `None`
- `prev()` → move left if possible; return title or `None`
- `insert_after_current(title)`
- `remove_current()` → unlink current; move to next if possible else to prev; return `True/False`
- `to_list()` → list of titles

## Hints
1. A tiny `_append(node)` helper makes head/tail updates consistent.
2. When removing, fix head/tail **before** picking the new `current`.
3. Insertion between `current` and `current.next` must link both directions.

## Run tests locally
```bash
python -m pytest -q

OR

python -m pytest -q tests/test_playlist.py
```

## Common problems
- Updating one direction only (remember prev and next).

- Dangling current after removal.

- Forgetting head/tail edges on first/last insertions.