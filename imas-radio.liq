#!/usr/bin/liquidsoap
 
set("log.file.path", "/home/takane/radio.log")
 
# Music
myplaylist = mksafe(playlist(mode="normal","/home/takane/imas-music/"))
 
# Start building the feed with music
radio = myplaylist
 
output.icecast(
        %mp3(bitrate=128),
        host = "localhost",
        port = 8000,
        name = "Idolmaster Radio (mp3-128)",
        password = "password",
        mount = "imas-radio-lq.mp3",
        radio
)
 
output.icecast(
        %vorbis,
        host = "localhost",
        port = 8000,
        name = "Idolmaster Radio (ogg)",
        password = "password",
        mount = "imas-radio.ogg",
        radio
)