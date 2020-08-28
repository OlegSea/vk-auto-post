Русский README будет позже

# vk-auto-post

Automatically makes postponed posts with pictures.

# What does it do

Automatically pulls random file from selected folder, then creates a postponed post.

# How-To

Surely works on Windows and Linux. Didn't tested it on MacOS, but it works theoretically.
1. Install [Python 3](https://www.python.org/downloads/) if you haven't already.
2. Install VK module (```pip3 install vk```)
3. Clone this repo.
4. Rename ```credentials-example.json``` to ```credentials.json``` and open it.
5. Set your Login and Password.
6. Rename ```settings-example.json``` to ```settings.json``` and open it.
7. Change ```groupID``` to your [group ID](https://regvk.com/id/) and ```appID``` to your app ID (you should create standalone one [here](https://vk.com/apps?act=manage)).
8. Change ```inputFolder``` to your folder.
9. Run ```main.py``` (you can use command ```python3 path/to/main.py```.

# Settings
* ```dateStart``` - Day on which the first post will be published (at 0:00).
* ```dateFinish``` - Last post wlll be posted exactly 1 hour before 0:00 of this day.
If you will have **dateStart** set to 01/01/2021, and the **dateFinish** to 03/01/2021, there will be exactly 48 posts. First one will be at 01/01/2021 0:00, and the last one will be at 02/01/2021 23:00. // If Step is set to 1 hour
* ```step``` - Delay between posts, 1 hour by default. Be careful, there is limit of 25 posts per day.
* ```inputFolder``` - Folder with photos to upload.
* ```groupID``` - ID of your group (https://regvk.com/id/)
* ```appID``` - Your App ID (https://vk.com/apps?act=manage)
* ```timeZone``` - your Time Zone (by default it's gmt+3)
* ```postDelay``` - Delay between posting. Default is 2s. MUST BE AT LEAST 1-1.5 SECONDS so there will be no captcha. I can't implement Captcha input because of the reasons below.

# Known issues (VkApi related)
Only Exception that module *vk* has is VkApiError, which means I can't except specific errors. Because of that:
* If program tries to postpone a post on a time, which is already occupied, porgramm will stop.
# Other issues
* There is no check for actual file compatibility, so if there will be any file in the folder which is not ```.jpg```, ```.png``` or ```.gif``` (or more than 50mb), it will crash.
* For some reason, it crashes when there are sub folders in the Input Folder. If you have any idea how to fix this, contact me (down below).
* Kinda bad maths when it comes to dates, so last post can be not exactly at 0:00, I also don't have a clue why tf it's this way.
* There is more problems I don't know about (cuz this program is kinda trash lmao), so if anything goes wrong, contact me(down below).

# How to contact me

* vk.com/olegsea (VK)
* OlegSea#1334 (Discord)
* Or make an Issue here
