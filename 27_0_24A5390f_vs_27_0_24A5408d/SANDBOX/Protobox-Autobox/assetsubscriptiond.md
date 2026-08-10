## assetsubscriptiond

> Group: ⬆️ Updated

```diff

 
 (deny system-fsctl)
 (allow system-fsctl
-	(fsctl-command FSIOC_CAS_BSDFLAGS)
+	(fsctl-command FSIOC_CAS_BSDFLAGS FSIOC_EXCLAVE_FS_REGISTER)
 )
 
 (deny system-kas-info)
```
