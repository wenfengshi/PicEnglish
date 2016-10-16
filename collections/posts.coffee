@Posts = new Meteor.Collection('posts');

Schemas.Posts = new SimpleSchema
	title:
		type:String
		max: 60

	content:
		type: String
		autoform:
			rows: 5

	createdAt:
		type: Date
		autoValue: ->
			if this.isInsert
				new Date()

	updatedAt:
		type:Date
		optional:true
		autoValue: ->
			if this.isUpdate
				new Date()

	picture:
		type: String
		autoform:
			afFieldInput:
				type: 'fileUpload'
				collection: 'Attachments'

	owner:
		type: String
		regEx: SimpleSchema.RegEx.Id
		autoValue: ->
			if this.isInsert
				Meteor.userId()
		autoform:
			options: ->
				_.map Meteor.users.find().fetch(), (user)->
					label: user.emails[0].address
					value: user._id

	labeled:
		type: Boolean
		defaultValue: false

	imgtag:
		type: String
		autoValue: ->
			arg1 = '../server/upload/temp.jpg'
			import child_process from 'child_process'
			exec = child_process.exec
#			Meteor.methods callPython: ->
#				fut = new Future
#				exec 'python ~/upload/label.py ' + arg1, (error, stdout, stderr) ->
#
#					new Fiber(->
#						fut.return 'Python was here'
#						return
#					).run()
#			return
#			fut.wait()
			exec 'python ../server/upload/label.py ' + arg1, (error, stdout, stderr) ->
				if stdout.length > 1
					console.log 'you offer args:', stdout
					return stdout
				else
					console.log 'you don\'t offer args'
				if error
					console.info 'stderr : ' + stderr
			return


Posts.attachSchema(Schemas.Posts)

Posts.helpers
	author: ->
		user = Meteor.users.findOne(@owner)
		if user?.profile?.firstName? and user?.profile?.lastName
			user.profile.firstName + ' ' + user.profile.lastName
		else
			user?.emails?[0].address

#			{labeled: false}
