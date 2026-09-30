## lockdownmoded

> Group: ⬆️ Updated

```diff

 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.assistant.settings"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))

 		SYS_writev
 		SYS_fchmod
 		SYS_rename
+		SYS_flock
 		SYS_sendto
 		SYS_mkdir
 		SYS_rmdir

 		F_SETFD
 		F_GETFL
 		F_SETLKW
+		F_NOCACHE
 		F_GETPATH
+		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
 		F_ADDFILESIGS_RETURN
 		F_CHECK_LV)
```
