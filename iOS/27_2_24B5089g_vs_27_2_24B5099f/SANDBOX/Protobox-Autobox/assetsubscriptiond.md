## assetsubscriptiond

> Group: ⬆️ Updated

```diff

 
 (deny system-fsctl)
 (allow system-fsctl
-	(fsctl-command FSIOC_CAS_BSDFLAGS FSIOC_EXCLAVE_FS_REGISTER)
+	(fsctl-command
+		FSIOC_CAS_BSDFLAGS
+		FSIOC_EXCLAVE_FS_GET_BASE_DIRS
+		FSIOC_EXCLAVE_FS_REGISTER
+		FSIOC_EXCLAVE_FS_UNREGISTER)
 )
 
 (deny system-kas-info)
```
