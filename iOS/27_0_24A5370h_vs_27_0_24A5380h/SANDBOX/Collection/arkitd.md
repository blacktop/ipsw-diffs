## arkitd

> Group: ⬆️ Updated

```diff

 		(subpath "${HOME}/Library/ARKit")
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "${HOME}/Library/ARKit")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${HOME}/Library/ARKit")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-all
-				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.aned.read-only")
 				(require-any
-					(require-any
-						(subpath "/AppleInternal/Applications")
-						(subpath "/System/Developer/Applications")
-					)
 					(require-any
 						(subpath "/private/var/factory_mount/[^/]+/Applications")
 						(subpath "/private/var/personalized_automation/Applications")

 						(subpath "/private/var/personalized_factory/[^/]+/Applications")
 					)
 					(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+					(subpath "/AppleInternal/Applications")
 					(subpath "/Applications")
 					(subpath "/Developer/Applications")
+					(subpath "/System/Developer/Applications")
 					(subpath "/private/var/containers/Bundle")
 				)
 			)

 			(literal "${FRONT_USER_HOME}/Library/DeviceRegistry")
 			(require-all
 				(subpath "/private/var")
-				(subpath "${FRONT_USER_HOME}")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+$")
+				(subpath "${FRONT_USER_HOME}")
 			)
 		)
 	)
```
