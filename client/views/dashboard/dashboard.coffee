#Template.photo.events
#  'click button': ->
#    MeteorCamera.getPicture {}, (e, pic) ->
#      if e?
#        alert(e.message)
#      else
#        attachments.insert {
#          picture: pic,
#          filename: new Date(),
#        }
#
#
