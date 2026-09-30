## healthcontentd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.figcpecryptor.xpc"))
-		(require-not (global-name "com.apple.xpc.amstoold"))
+		(require-not (global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (require-any
 			(global-name "com.apple.coremedia.mediaplaybackd.figcontentkeyboss.xpc")
 			(global-name "com.apple.coremedia.mediaplaybackd.figcontentkeysession.xpc")
 		))
-		(require-not (global-name "com.apple.xpc.amsaccountsd"))
-		(require-not (global-name "com.apple.fairplaydeviceidentityd"))
-		(require-not (global-name "com.apple.xpc.amsengagementd"))
-		(require-not (global-name "com.apple.amsservicesanalytics.xpc"))
-		(require-not (global-name "com.apple.symptom_diagnostics"))
-		(require-not (global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
-		(require-not (global-name "com.apple.coremedia.mediaplaybackd.asset.xpc"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc"))
-		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.coremedia.mediaplaybackd.asset.xpc"))
+		(require-not (global-name "com.apple.xpc.amsengagementd"))
+		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.coremedia.figcontentkeyboss.xpc"))
+		(require-not (global-name "com.apple.amsservicesanalytics.xpc"))
+		(require-not (global-name "com.apple.fairplaydeviceidentityd"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.xpc.amstoold"))
+		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.adid"))
 		(require-not (system-attribute developer-mode))
 	)

 			SYS_open_dprotected_np
 			SYS_openat_dprotected_np
 			SYS_fgetattrlist
+			SYS_fgetxattr
 			SYS_listxattr
 			SYS_fsctl
 			SYS_sysctlbyname

 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
 		F_DUPFD_CLOEXEC
+		F_RECYCLE
 		F_BARRIERFSYNC
 		F_OFD_GETLK
 		F_OFD_SETLKWTIMEOUT

 
 (deny system-fsctl)
 (allow system-fsctl
-	(fsctl-command FSIOC_CAS_BSDFLAGS)
+	(fsctl-command APFSIOC_GET_CLONE_INFO FSIOC_CAS_BSDFLAGS)
 )
 
 (deny system-kas-info)
```
