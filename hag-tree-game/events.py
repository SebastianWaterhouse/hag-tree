class events(object):
  init(evst, tree_req, outcomes):
    self.event_statement=evst
    self.needs_tree=tree_req
    self.outcomes=outcomes
lawn1 = events("Some lousy kids are trashing your lawn! What'll you do to these cretins?! Say 1 if you will crush them, or say 2 if you will simply yell.", 0, {"I WILL CRUSH YOU!":"mood_level=mood_level-15", "GET OFF MY LAWN YOU LOUSY KIDS!":"mood_level=mood_level-5"}
flowers1 = ("Some kids are giving you flowers! Isn't that sweet? Say 1 if you thank the kids, or say 2 if you tell them to scamper.", 0, {"Thank you, kind children!":"mood_level=mood_level+10", "Go away!":"mood_level=mood_level-5"}
