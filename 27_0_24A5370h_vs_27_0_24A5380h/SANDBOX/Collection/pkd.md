## pkd

> Group: ⬆️ Updated

```diff

 			(require-all
 				(system-attribute internal-build)
 				(require-any
-					(require-any
-						(subpath "/AppleInternal/Applications")
-						(subpath "/System/Developer/Applications")
-					)
+					(subpath "${FRONT_USER_HOME}/Containers/Bundle")
 					(subpath "/AppleInternal")
 				)
 			)
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
 			(require-any
 				(subpath "/private/var/factory_mount/[^/]+/Applications")
 				(subpath "/private/var/personalized_automation/Applications")

 				(subpath "/private/var/personalized_factory/[^/]+/Applications")
 			)
 			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
 			(subpath "/Applications")
 			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
 			(subpath "/private/var/containers/Bundle")
 		)
 	)
```
