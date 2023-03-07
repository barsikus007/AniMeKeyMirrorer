# AniMe Key Mirrorer
## Info
This program is for ASUS ROG lineups with AniMe matrix on lid
[![Demo Video](https://cdn.discordapp.com/attachments/736971456650412114/1081972900044734595/PXL_20230305_1611064473.mp4)](https://cdn.discordapp.com/attachments/736971456650412114/1081972900044734595/PXL_20230305_1611064473.mp4)
## Installation
Install deps via poetry then you can run `python3 main.py` to start the keylogging program.
## TODO
- new README video
- animations
  - async
- rewritings
  - change key detecting backend
    - different languages resolve
    - add arrow keys and ctrl based movement (unpredictable due to ctrl+x or alt+x inconsistency, ide specific movement and etc)
  - is pillow best way to render?
  - is it hard to rewrite this to rust?
    - is it worth to do?
- add easier installation
  - add daemon
  - add cli
- ROG14 2022 and other non standart matrix support
