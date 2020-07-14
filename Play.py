import pyglet
music = pyglet.media.load('Intro1.mp3')
looper = pyglet.media.SourceGroup(music.audio_format, None)
looper.loop = True
looper.queue(music)
p = pyglet.media.Player()
p.queue(looper)
p.play()
