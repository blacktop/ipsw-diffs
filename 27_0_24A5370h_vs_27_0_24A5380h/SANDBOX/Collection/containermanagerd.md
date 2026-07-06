## containermanagerd

> Group: ⬆️ Updated

```diff

 
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
+		(extension-class "com.apple.app-sandbox.read")
 		(require-any
 			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]")
 			(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/([^/])+")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.sandbox.application-group")
+		(extension-class "com.apple.app-sandbox.read-write")
 		(require-any
 			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]")
 			(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/([^/])+")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.app-sandbox.read")
+		(extension-class "com.apple.sandbox.application-group")
 		(require-any
-			(require-all
-				(extension-class "com.apple.app-sandbox.read")
-				(require-any
-					(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]")
-					(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/([^/])+")
-				)
-			)
-			(require-any
-				(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]")
-				(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/([^/])+")
-				(subpath "${ANY_USER_HOME}/Containers/Shared/AppGroup")
-			)
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]")
+			(regex #"/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/([^/])+")
+			(subpath "${ANY_USER_HOME}/Containers/Shared/AppGroup")
 		)
 	)
 )

 
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.containermanagerd")
 	)
 )
```
