# pokemon-tcg-tracker
A CLI tool that calls tcgdexsdk API to display information about Pokemon cards.

## Features
- User inputs card name.
- A list of card names and card IDs appears in a numbered list.
- The user selects the card they want by entering a number in the list.
- The API is called and retrieves card data for the specified card.
- The user is given an output of formatted data.
- The user can chose to search for another card or end the program.

## Requirements
- Python 3
- colorama
- TCGdex SDK

## Installation
```
pip install colorama
pip install tcgdex-sdk
```

## Usage
Run the command in your terminal:
```
python tracker.py
```

Then follow the prompt:
```
Enter the name of your card -> (ie. "Pikachu")
```

Once you are satisfied with your data:
```
Y/N would you like to search for another card? -> N
```

## Example Output
```
==========POKEMON TCG CARD LOCATOR==========
Enter the name of your card -> Charizard
1. Charizard | pl4-1
2. Charizard | 2024sv-1
3. Charizard | dp3-3
4. Charizard | sm7.5-3
5. Charizard | lc-3
6. Charizard | cel25-4A
7. Charizard | base4-4
8. Charizard | base1-4
9. Charizard | det1-5
10. Charizard | ecard1-6
11. Charizard | ex16-6
12. Charizard | swsh10.5-010
13. Charizard | xy12-11
14. Charizard | B1a-013
15. Charizard | sm9-14
16. Charizard | bw11-19
17. Charizard | bw7-20
18. Charizard | swsh4-25
19. Charizard | A1-035
20. Charizard | ecard1-39
21. Charizard | ecard1-40
22. Charizard | B1a-091
23. Charizard | ex3-100
24. Charizard | dp7-103
25. Charizard | bw8-136
26. Charizard | ecard3-146
27. Charizard | g1-RC5
28. Charizard | smp-SM158
29. Charizard | smp-SM226
30. Charizard | swshp-SWSH066
31. Charizard | swsh11-TG03
 Chose the card that matches your ID (1 to 31) -> 3
Item          dp3-3

Name:          Charizard
HP:            130
Types:
Type #1        Fire
Rarity:        Rare Holo
Stage:         Stage2
Evolved From:  Charmeleon
Set Name:      Secret Wonders
Abilities:
Ability #1     Fury Blaze - If your opponent has 3 or less Prize cards left, each of Charizard's attacks does 50 more damage to the Active Pokémon (before applying Weakness and Resistance).
Retreat Cost:  3
       Legal
Standard:      False
Expanded:      False
Y/N would you like to search for another card? -> n
==========POKEMON TCG CARD LOCATOR==========
```

## Notes
- You can only search by card name (ie. "N", "Charizard V", "Fishing Net")
- Abilities text is not formatted to remain on the right hand side.
- Future iterations are intended to include I/O to allow users to save data.

## Errors with TCGDex API
In the event the API call fails, you will be prompted with:
```
ERROR! - {Error Message}
API Call Has Failed. Type CLS to close the program
Enter the name of your card ->
```

You may choose to enter "CLS" to close the program.

## Attributions

[TCGDex API](https://tcgdex.dev/)


## What This Taught Me
- Calling APIs
- Using getSync
- Analyzing dictionaries
- Pulling data from dictionaries
- Query()
- Furthered OOP understanding
- Furthered formatting and colorama use
- Pushing iterations to GitHub
- Error handling with APIs using try/except
- Using Except as e to output a clean error without crashing the code
- Git workflow and commits through VS Code
