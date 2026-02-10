# Adventure Game

Small interactive Python adventure demonstrating simple choices and branching.

## Requirements
- Python 3

## Run (interactive)
```
python3 adventure_game.py
```

## Run (non-interactive example)
You can pipe responses for quick tests. Example (name `Tester`, choose forest → river, then no):

```bash
printf "Tester\nforest\nriver\nn\n" | python3 adventure_game.py
```

## Files
- `adventure_game.py`: main game; contains `start_game()`, `forest_path()`, `cave_path()`, and `play()`.

## Notes
- The script prints a startup confirmation when run directly.
- To modify scenarios, edit `adventure_game.py` and run the script again.
