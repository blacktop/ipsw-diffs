## mediasetupd

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.aned.read-only")
+		(extension-class "com.apple.mediaserverd.read-write")
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.HomeKit/com.apple.mediasetupd")
 			(subpath "${HOME}/Library/Caches/com.apple.iTunesCloud")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.mediaserverd.read")
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.HomeKit/com.apple.mediasetupd")
 			(subpath "${HOME}/Library/Caches/com.apple.iTunesCloud")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.HomeKit/com.apple.mediasetupd")

 )
 (allow file-read*
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.mediasetupd")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.iTunesCloud")

 )
 (allow file-read*
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
-			(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PayloadDependency.plist")
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.mediasetupd")
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.iTunesCloud")

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.mediasetupd")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.iTunesCloud")

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
-			(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PayloadDependency.plist")
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.mediasetupd")
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.iTunesCloud")

 
 (allow file-write*
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.mediasetupd")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.iTunesCloud")

 )
 (allow file-write*
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.mediasetupd")

 )
 (allow file-write-create
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.mediasetupd")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.iTunesCloud")

 )
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.mediasetupd")

 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.mediasetupd")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.iTunesCloud")

 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.HomeKit/com.apple.mediasetupd")
```
