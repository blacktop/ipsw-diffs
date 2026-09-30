## online-auth-agent

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.networkscored"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.online-auth-agent.xpc"))
-		(require-not (global-name "com.apple.lsd.icons"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.misagent"))
-		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.mobileassetd.v2"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.mobileactivationd"))
-		(require-not (global-name "com.apple.ctkd.token-client"))
-		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.lsd.icons"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.networkscored"))
+		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.timed.xpc"))
+		(require-not (global-name "com.apple.cloudd"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.online-auth-agent.xpc"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.misagent"))
 		(require-not (xpc-service-name "com.apple.AppleVirtualPlatform.IdentityService"))
 		(require-not (xpc-service-name "com.apple.pvappidentityservice"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))

 		SYS_munmap
 		SYS_mprotect
 		SYS_madvise
+		SYS_dup2
 		SYS_fcntl
 		SYS_select
 		SYS_fsync
```
