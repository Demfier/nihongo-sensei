# nihongo-sensei
A tool to help with my Japanese (日本語: pronounced Nihongo) practice.

**Note:** This is kinda a living repository.
I will add more functionalities as I finish different milestones in Japanese.

# Features
1. `kana.py`: This script is to practice different Japanese kanas (characters).
A kana will pop up in one of the Japanese scripts (Hiragana/Katakana) and you'll
need to guess its romaji (English transliteration of a kana)
    - **Usage:**
    ```python3
    python kana.py --column columns --script scripts
    ```
    Here, `columns` string denotes the columns to practice as comma seperated values.
    For instance, `--columns a,k` means the 'a' and 'k' columns.
    `scripts` follows similar pattern with 'hiragana' and 'katakana' as the
    options. You can also use 'all' to practice *all* the kanas in a script(s)!

    **TODO:** Currently only supports the "a" column in Hiragana.
    Add support for all the columns!
