
#ImagesStore = new FS.Store.FileSystem('images-original', {
#	path: '~/uploads'
#});
#
#@Attachments = new FS.Collection('images', {
#	stores: [ImagesStore],
#	filter: {
#		maxSize: 1048576 * 4, #in bytes
#		allow: {
#			contentTypes: ['image/jpeg'],
#			extensions: ['jpg']
#		}
#	}
#});

@Attachments = new FS.Collection("Attachments",
	stores: [
#		new FS.Store.FileSystem("images"),
		new FS.Store.GridFS("attachments", {
			transformWrite: (fileObj, readStream, writeStream)->
				if gm.isAvailable
					if fileObj.original.type.substr(0,5) == 'image'
						gm(readStream, fileObj.name()).autoOrient().stream().pipe(writeStream);
					else
					  readStream.pipe(writeStream);
				else
					readStream.pipe(writeStream)
		}
#			path: '~/uploads'
#		}
		)
	]
)