## deleted

> Group: ⬆️ Updated

```diff

 	(require-all
 		(vnode-type DIRECTORY)
 		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches*")
 			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp*")
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/Library/Caches*")
 			(require-all
 				(subpath "/private/var")
 				(require-any

 					)
 				)
 			)
+			(require-any
+				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches*")
+				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/Library/Caches*")
+			)
 		)
 	)
 )

 
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.CacheDelete")
 	)
 )

 		(vnode-type DIRECTORY)
 		(require-any
 			(literal "${HOME}/Library/Caches")
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches*")
 			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp*")
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/Library/Caches*")
 			(require-all
 				(subpath "/private/var")
 				(require-any

 					)
 				)
 			)
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.CacheDelete")
+			)
+			(require-any
+				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches*")
+				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/Library/Caches*")
+			)
 		)
 	)
 )
```
