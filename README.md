# Pure Joy — entry for make.fun "Make the AI judge happy" (ai-happy-01)

`main.py` writes one image to `/output/entry.png`: a kitten and a puppy
laughing together at a birthday party — party hats, cake, sparklers, hearts.
The image is stored in this repository as `happy.png` (1024×1024, PNG,
under 1 MiB) and the program simply copies it, so two runs always produce
byte-identical output. No network access, no dependencies beyond the
Python 3 standard library.

Run it:

```bash
python3 main.py   # writes /output/entry.png
```

MIT licensed.
