## managedassetsd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.spaceattributiond"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))
-		(require-not (global-name "com.apple.duetactivityscheduler"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.cache_delete"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (system-attribute developer-mode))
 	)
```
