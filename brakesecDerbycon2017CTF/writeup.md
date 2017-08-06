# Challenge 1

## Description
The first challenge was announce on [Episode 2017-025](http://brakeingsecurity.com/2017-025-how-will-gdpr-affect-your-biz-with-wendyck-and-derbycon-ctf-info). For this one Ms Amanda Berlin left a few flags around the internet, only hint we had is that she created a fake company called Big Bob's Chemistry Lab and we had to send the flags to the [form](https://goo.gl/forms/iUEVHNuSYr34OZA22) created for that, if we got them, we will get the next challenge sent to us.


## Solving
A google search returned a [blogspot base site](http://bigbobschemistrylab.blogspot.pe/), and as people say around "the world is in the comments", and checking [one of them](http://bigbobschemistrylab.blogspot.pe/2017/07/lab-fanfic.html#comments) had some weird text on it: `send in this flag here flag:AmandaisAwesoem`. I first was a little doubtious about it being the actual flag or someone was trolling us. It was the correct one.

# Challenge 2

## Description
Saturday 10am my time, i literally woke up to see i had got a message on twitter 2 minutes ago with the [link to the next challenge](https://docs.google.com/document/d/1Vl4esXSorZGEPOwRjJmFgp9m3XW1vnm5utGu4zLe9rE/edit). 

Content of the doc:
```
You started your new job last week.  You were excited about it until you found out the only security dude in the company quit the week before you arrived.  To add insult to injury, the training was disorganized and you found out that the company's core online applications were highly unstable.  It's Monday morning, and you arrive to clusters of people in the support area shoulder-surfing two admins and arguing.  

Despite the many challenges you perceive from this seemingly chaotic environment, you convince yourself that this is a good opportunity to gain experience quickly, and help a young company become more mature and stable.

You were going to dedicate this week to setting up whatever alerts your predecessor set up for himself.  That was going to be a challenge since he left you very little documentation.  Hopefully the IT department didn't wipe his computer.  Maybe you could get an idea of what alerts he had by reviewing his emails.

Ahh, emails!  You checked your inbox and noticed one from Bob.  He was a fellow newbie in orientation, hired on as an operator (Level 1 application support).  They assign all the new operators to work the night shift.  Apparently he started this weekend and probably went home a few hours ago.  Bob's a smart dude, but this is his first job out of high school so he lacks experience.  Below is his email.

----------

Anna,
Wow, first real day after orentation and SHTF. Wonder how often this happens in companys.
Long story short, the client database is totally borked.
The on-call DBA is going to try to restore from backup.
I'm just trying to stay out of the way because these guys are talking greek
But I got curious and started looking at the server logs and there was one entry that was just wierd.
I showed it to my boss, and he said that's nothing, the app would just throw that gibberish out.
Doesn't look normal and was the only entry like that. Just a hunch.
Thoughts?

root@foxtrot logs]# zgrep pwned *
2017_07_15.request.log:10.3.184.253 -  -  
[15/Jul/2017:13:05:02 -0500] "GET /deploy/05/index.cfm?isndsl&user=
CHAR(97 100 109 105 110 39 32 65 78 68 32 50 43 50 61 53 32 85 78 73 79 78 32 65 76 76 32 83 69 76 69 67 84 32 39 97 100 109 105 110 39 44 32) '15bb7112e138f1af4020618fcf745394fcfc15a1'&pass=pwned456--%20%20 HTTP/1.0" 302 0
root@foxtrot logs]#

Bob Sacamano
Support Analyst



--------------------------




Need the ‘user’ (with spaces and ALL special characters) to unlock the next challenge



NEXT CHALLENGE Located at : 

https://goo.gl/UZ9kqR
```

# Solution
So on the logs we can spot an SQL injection attempt, so we just need to decode what is attempting to decode. Since it's using the `CHAR` command we first have to figure out what it does. Quick google search and we get the [documentation from microsoft](https://docs.microsoft.com/en-us/sql/t-sql/functions/char-transact-sql), nothing to complicated, just an ASCII decoder. So let's try some python:

```python
chars = '97 100 109 105 110 39 32 65 78 68 32 50 43 50 61 53 32 85 78 73 79 78 32 65 76 76 32 83 69 76 69 67 84 32 39 97 100 109 105 110 39 44 32'
''.join([chr(y) for y in [int(x) for x in chars.split()]])
```

This returns the following code: `admin' AND 2+2=5 UNION ALL SELECT 'admin', `, so i dowloaded the challenge3 7z file and tried to extract it and use that as a password, which failed. I got stuck here. Started playing with the token `15bb7112e138f1af4020618fcf745394fcfc15a1` and even with the password. Download mysql and tried to run the SQL there as well to see if i was missing something: no luck. Someone on the twitter messages was claiming to solve it, a bunch of us where frustrated and not being able to solve it. I needed some help to find out the bug on my code, the correct script was as follows:


```python
chars = '97 100 109 105 110 39 32 65 78 68 32 50 43 50 61 53 32 85 78 73 79 78 32 65 76 76 32 83 69 76 69 67 84 32 39 97 100 109 105 110 39 44 32'
' '.join([chr(y) for y in [int(x) for x in chars.split()]])
```

Which returns `a d m i n '   A N D   2 + 2 = 5   U N I O N   A L L   S E L E C T   ' a d m i n ' ,`, and that opened the 7z file.

# Challenge 3

## Description

After opening the file [downloaded from the previous challenge](https://goo.gl/UZ9kqR) using the solution found there as well i was presented with an image of a 16x16 Sudoku board with some cells highlighted with dots and the following text on a text file:

```
Solve the puzzle. If you know what kind of puzzle this is, it will make it easier.
A specific set of rules must be followed to logically solve it
The gray circles will hold the 16 digit hex value you need to decrypt the final puzzle.
The answer will be gleaned in this order:

 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16

We've triple checked the answer to ensure it will unlock the final level


Once you have the code, go to

https://drive.google.com/open?id=0B-qfQ-gWynwiUWlQSTB1TXVkRDQ

and hurry, someone might be ahead of you!

Remember, once you solve the last puzzle,
the phrase MUST be emailed to "[REDACTED]"  And first to get it wins...

GOOD LUCK, and may the odds ever be in your favor!
```

## Solution
So we have to solve the SUDOKU, since i'm lazy AF, i just googled for sudoku solvers and found a [couple](http://sudokuspoiler.azurewebsites.net/Sudoku/Sudoku16) [of them](http://www.sudokuwiki.org/sudokuhex.htm), only issue is that the one in the image was proper hex, so 0-F, and the ones i found where 1-16 and 1-G respectively, so i just had to add one to each number when filling the boards, get the results and substract one again, getting `6c424c175db55bd8` as the key for the next one.

# Challenge 4

## Description
Again we had to download a [7z file](https://drive.google.com/open?id=0B-qfQ-gWynwiUWlQSTB1TXVkRDQ) which was password protected with the hex token we got from previous challenge.

## Solution
Opening it there was only a video, so i opened it, it was a blank screen with some music, so i started listening pretty careful to the lyrics, so i looked away from the monitor, and as i was having some trouble hearing i watched again just to find a sequence of numbers on the video flashing. That must be it.
Rewinded, opened a notepad and starting taking notes of the numbers i was seeing (a lot of play/pause clicking), final list was:

```
02201
01012
10121
11000
11102
10121
11111
11021
01012
11011
11020
10202
10210
10202
11020
11020
10202
10201
01012
02111
10212
11020
10220
11021
11021
11111
01201
```

Ok, so all of them contain only 0-2, so it must be ternary numbers, so let's do some python magic again:

```python
chars = [
'02201',
'01012',
'10121',
'11000',
'11102',
'10121',
'11111',
'11021',
'01012',
'11011',
'11020',
'10202',
'10210',
'10202',
'11020',
'11020',
'10202',
'10201',
'01012',
'02111',
'10212',
'11020',
'10220',
'11021',
'11021',
'11111',
'01201'
]

print ''.join([chr(int(x, 3)) for x in chars])
```

Which returned: `I always preferred Chrissy.`. And there it was. Just mailed that and got confirmation.