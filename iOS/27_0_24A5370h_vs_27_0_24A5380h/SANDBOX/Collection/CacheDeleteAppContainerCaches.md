## CacheDeleteAppContainerCaches

> Group: ⬆️ Updated

```diff

 	(require-all
 		(vnode-type DIRECTORY)
 		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches*")
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

 	(require-all
 		(vnode-type DIRECTORY)
 		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches*")
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
```
