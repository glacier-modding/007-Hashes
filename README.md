# 007-Hashes
<!-- BADGES_START -->
<!-- BADGES_END -->
## Statistics
<details>
<summary>Show table</summary>

<!-- STATISTICS_TABLE_START -->
<!-- STATISTICS_TABLE_END -->
</details>

## Game flags
| Game          | Bit Representation (Binary) |
|---------------|-----------------------------|
| FirstLight    | 0b00000001                  |

## Scripts
This repository contains four main scripts merge.py, add_paths.py, add_new_hashes.py and extract_hashes.py. They must be ran from the repository's root directory like `python ./scripts/add_paths.py`.

### merge.py
Generates hash_list.txt. Takes a version number as an argument and optionally `--game` (separate games by spaces if you wish to include multiple). Example: `python ./scripts/merge.py 0` or `python ./scripts/merge.py 0 --game FirstLight`.

### add_paths.py
Adds paths to their assoicated hashes within the path folder's JSON files.

Defaults to reading a file called `new_paths.txt` in the repository's root directory which needs to contain data structured like this (resource type is optional, although it will make adding paths slightly slower if omitted):

```
000A4FB9B5FDAB19.WSGT,[assembly:/sound/wwise/exportedwwisedata/states/levelspecific_states/paris/fashionshowmusic_level_state.wwisestategroup].pc_entitytype
004B66043E12A8E3.WSGB,[assembly:/sound/wwise/exportedwwisedata/states/levelspecific_states/paris/fashionshowmusic_level_state.wwisestategroup].pc_entityblueprint
005EA1E72FC62DEC.WSGT,[assembly:/sound/wwise/exportedwwisedata/states/levelspecific_states/paris/paris_rain_puddle_state.wwisestategroup].pc_entitytype
0054C5081030A3D0.WSGB,[assembly:/sound/wwise/exportedwwisedata/states/levelspecific_states/paris/paris_rain_puddle_state.wwisestategroup].pc_entityblueprint
```

### add_new_hashes.py
Adds new hashes into the JSON files.

Requires a `new_hashes.txt` file in the repository's root directory which contains data structured like:

```
000A4FB9B5FDAB19.WSGT:FirstLight
004B66043E12A8E3.WSGB:FirstLight
005EA1E72FC62DEC.WSGT:FirstLight
0054C5081030A3D0.WSGB:FirstLight
003B993A25498AE6.AIBB:FirstLight
```

Possible games are: `FirstLight`.

### extract_hashes.py
Extracts a list of hashes from RPKG files into a text file. This is for use with the `add_new_hashes.py` script. Example: `python .\scripts\extract_hashes.py --input C:\Epic\HITMAN3\Runtime --game h3`.