## com.apple.siri.ClientFlow.ClientScripter

> Group: ⬆️ Updated

```diff

 			(literal "${FRONT_USER_HOME}/Library/DeviceRegistry")
 			(require-all
 				(subpath "/private/var")
-				(subpath "${FRONT_USER_HOME}")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+$")
+				(subpath "${FRONT_USER_HOME}")
 			)
 		)
 	)

 					(literal "${FRONT_USER_HOME}/Library/DeviceRegistry")
 					(require-all
 						(subpath "/private/var")
-						(subpath "${FRONT_USER_HOME}")
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+$")
+						(subpath "${FRONT_USER_HOME}")
 					)
 				)
 			)
```
