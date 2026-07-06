## MobileBackup

> Group: ⬆️ Updated

```diff

 (deny file-mknod)
 
 (allow file-mount
-	(require-not (subpath "/private/var"))
+	(require-not (require-any
+		(subpath "${FRONT_USER_HOME}")
+		(subpath "${HOME}")
+	))
 )
 (deny file-mount
 	(require-any

 )
 
 (allow file-mount-update
-	(require-not (subpath "/private/var"))
+	(require-not (require-any
+		(subpath "${FRONT_USER_HOME}")
+		(subpath "${HOME}")
+	))
 )
 (deny file-mount-update
 	(require-any

 )
 
 (allow file-unmount
-	(require-not (subpath "/private/var"))
+	(require-not (require-any
+		(subpath "${FRONT_USER_HOME}")
+		(subpath "${HOME}")
+	))
 )
 (deny file-unmount
 	(require-any
```
