## installd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))

 		F_OFD_SETLKWTIMEOUT
 		F_SETCONFINED
 		F_ADDFILESIGS_RETURN
-		F_CHECK_LV)
+		F_CHECK_LV
+		F_PUNCHHOLE)
 )
 
 (deny system-fsctl)
 (allow system-fsctl
-	(fsctl-command FSIOC_CAS_BSDFLAGS)
+	(fsctl-command FSIOC_CAS_BSDFLAGS FSIOC_GET_GRAFT_INFO)
 )
 
 (deny system-kas-info)
```
