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
    python kana.py --column columns --script scripts --number n
    ```
    Here, `columns` string denotes the columns to practice as comma seperated values.
    For instance, `--columns a,k` means the 'a' and 'k' columns.
    `scripts` follows similar pattern with 'hiragana' and 'katakana' as the
    options. You can use 'all' to practice *all* the kanas in a script(s)!
    `number` is the number of characters to practice in one setting.

    **TODO:** Currently only supports main kana.
    Add Dakuten, Combo Hiragana, and Katakana support (See [#3][i3] [#5][i5] [#6][i6])!

[i3]: https://github.com/Demfier/nihongo-sensei/issues/3
[i5]: https://github.com/Demfier/nihongo-sensei/issues/5
[i6]: https://github.com/Demfier/nihongo-sensei/issues/6
