## iWorkXPC

> Group: ⬆️ Updated

```diff

 		(extension "com.apple.foundation.upload-prep.read-write")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/tmp(/|$)")
 			)
 			(subpath "${FRONT_USER_HOME}/tmp")
```
