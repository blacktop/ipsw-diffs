## syncdefaultsd

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.aned.read-only")
+		(extension-class "com.apple.mediaserverd.read-write")
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.syncdefaultsd")
 			(subpath "${HOME}/Library/HTTPStorages/com.apple.syncdefaultsd")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.mediaserverd.read")
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.syncdefaultsd")
 			(subpath "${HOME}/Library/HTTPStorages/com.apple.syncdefaultsd")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(extension "com.apple.sandbox.container")
 			(require-all

 					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
 				)
 			)
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(extension "com.apple.security.exception.files.absolute-path.read-only")
-					(extension "com.apple.security.exception.files.absolute-path.read-write")
-					(extension "com.apple.security.exception.files.home-relative-path.read-only")
-					(extension "com.apple.security.exception.files.home-relative-path.read-write")
-					(require-all
-						(extension-class "com.apple.mediaserverd.read")
-						(require-any
-							(require-all
-								(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-								(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-							)
-							(require-all
-								(extension "com.apple.librarian.ubiquity-container")
-								(require-any
-									(require-all
-										(subpath "/private/var")
-										(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-										(subpath "${FRONT_USER_HOME}")
-									)
-									(subpath "${HOME}/Library/Mobile Documents")
-									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-									(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-								)
-							)
-						)
-					)
-				)
-			)
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.syncdefaultsd")
 				(subpath "${HOME}/Library/HTTPStorages/com.apple.syncdefaultsd")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.mediaserverd.read")
 		(extension "com.apple.sandbox.container")
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.quicklook.readonly")
+		(extension-class "com.apple.mediaserverd.read-write")
 		(extension "com.apple.sandbox.container")
 	)
 )

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.quicklook.readonly")
 		(require-any
 			(extension "com.apple.sandbox.container")
 			(require-all
 				(subpath "${HOME}/Library/Caches/com.apple.syncdefaultsd")
-				(extension-class "com.apple.mediaserverd.read")
+				(require-any
+					(extension-class "com.apple.mediaserverd.read")
+					(extension-class "com.apple.mediaserverd.read-write")
+				)
 			)
 		)
 	)

 )
 (allow file-write*
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.syncdefaultsd")
+		(vnode-type SYMLINK)
+		(require-any
+			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+		)
+		(extension "com.apple.revisiond.staging")
 	)
 )
 (allow file-write*

 )
 (allow file-write*
 	(require-all
-		(vnode-type SYMLINK)
-		(require-any
-			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-		)
-		(extension "com.apple.revisiond.staging")
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.syncdefaultsd")
 	)
 )
 (allow file-write*
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-all
 				(require-any

 )
 (allow file-write-create
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.syncdefaultsd")
+		(vnode-type SYMLINK)
+		(require-any
+			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+		)
+		(extension "com.apple.revisiond.staging")
 	)
 )
 (allow file-write-create

 )
 (allow file-write-create
 	(require-all
-		(vnode-type SYMLINK)
-		(require-any
-			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-		)
-		(extension "com.apple.revisiond.staging")
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.syncdefaultsd")
 	)
 )
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-all
 				(require-any

 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.syncdefaultsd")
+		(vnode-type SYMLINK)
+		(require-any
+			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/.DocumentRevisions-V100/staging")
+			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+		)
+		(extension "com.apple.revisiond.staging")
 	)
 )
 (allow file-write-unlink

 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type SYMLINK)
-		(require-any
-			(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/.DocumentRevisions-V100/staging")
-			(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-		)
-		(extension "com.apple.revisiond.staging")
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.syncdefaultsd")
 	)
 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-all
 				(require-any
```
