## tailspind

> Group: ⬆️ Updated

```diff

 
 (deny system-fsctl)
 (allow system-fsctl
-	(fsctl-command APFSIOC_GET_DEV_INFO FSIOC_CAS_BSDFLAGS HFSIOC_GET_VERY_LOW_DISK)
+	(fsctl-command
+		APFSIOC_GET_DEV_INFO
+		FSIOC_CAS_BSDFLAGS
+		FSIOC_FD_ONLY_OPEN_ONCE
+		HFSIOC_GET_VERY_LOW_DISK)
 )
 
 (deny system-kas-info)
```
