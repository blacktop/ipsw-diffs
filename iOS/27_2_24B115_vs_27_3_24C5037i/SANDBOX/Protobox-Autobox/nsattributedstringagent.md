## nsattributedstringagent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.TextInput"))
 		(require-not (global-name "com.apple.accessibility.mediaaccessibilityd"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
+		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (require-any
 			(global-name "com.apple.appprotectiond.extensioninfo")
 			(global-name "com.apple.appprotectiond.extensionmonitor")
 		))
 		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.iconservices"))

 		(require-not (global-name "com.apple.audioanalyticsd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.backboard.display.services"))
+		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
 		(require-not (global-name "com.apple.fontservicesd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))

 		SYS_getattrlist
 		SYS_fgetattrlist
 		SYS_fgetxattr
+		SYS_listxattr
 		SYS_fsctl
 		SYS_shm_open
 		SYS_sem_open

 		F_RDADVISE
 		F_GETPATH
 		F_GETPROTECTIONCLASS
+		F_DUPFD_CLOEXEC
 		F_ADDFILESIGS_RETURN
 		F_CHECK_LV)
 )

 
 (deny system-kas-info)
 
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all

 (allow system-necp-client-action
 	(necp-client-action
 		NECP_CLIENT_ACTION_ADD
+		NECP_CLIENT_ACTION_ADD_FLOW
 		NECP_CLIENT_ACTION_COPY_AGENT
 		NECP_CLIENT_ACTION_COPY_INTERFACE
 		NECP_CLIENT_ACTION_COPY_RESULT
```
