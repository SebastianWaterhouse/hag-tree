class moods(object):
  init(req, name, col):
    self.req=req
    self.name=name
    self.color=col

#base moods#

fine = moods(0, 'Fine', '07')

angry = moods(-10, 'Angry', '0c')

happy = moods(10, 'Happy', '0a')
