## companiond

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.watchnotificationsui.alertservice"))
 		(require-not (global-name "com.apple.CompanionLink"))
 		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.intelligentroutingd.xpc.media"))
 		(require-not (global-name "com.apple.bluetooth.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))

 		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.sessionservices"))
 		(require-not (global-name "com.apple.SharingServices"))
+		(require-not (global-name "com.apple.photos.service"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.MobileTimer.alarmserver"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))

 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
 		(require-not (global-name "com.apple.breadboardservices"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
+		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
 		(require-not (global-name "com.apple.linkd.application-service"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.logd.events"))

 		SYS_fstat
 		SYS_lstat
 		SYS_pathconf
+		SYS_fpathconf
 		SYS_getrlimit
 		SYS_setrlimit
 		SYS_mmap

 		SYS_open_dprotected_np
 		SYS_openat_dprotected_np
 		SYS_getattrlist
+		SYS_setattrlist
 		SYS_fgetattrlist
+		SYS_fsetattrlist
 		SYS_setxattr
 		SYS_listxattr
 		SYS_fsctl

 		MSC_mk_timer_create
 		MSC_mk_timer_destroy
 		MSC_mk_timer_arm
-		MSC_mk_timer_cancel)
+		MSC_mk_timer_cancel
+		MSC_mk_timer_arm_leeway)
 )
 
 (deny syscall-mig)

 		F_SETFD
 		F_GETFL
 		F_SETFL
+		F_RDAHEAD
+		F_NOCACHE
 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
```
