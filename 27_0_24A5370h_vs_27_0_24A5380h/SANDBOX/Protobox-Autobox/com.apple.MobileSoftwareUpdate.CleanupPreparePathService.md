## com.apple.MobileSoftwareUpdate.CleanupPreparePathService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.mobileasset.autoasset"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.seeding.client"))
-		(require-not (global-name "com.apple.commcenter.xpc"))
-		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.commcenter.xpc"))
+		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.seeding.client"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.cache_delete"))
 		(require-not (global-name "com.apple.analyticsd"))

 (deny sysctl-write
 	(require-all
 		(sysctl-name "vm.debug_range_enabled")
-		(require-not (sysctl-name "vm.debug_range_enabled"))
 		(require-not (sysctl-name "vfs.generic.apfs.proc_free_blocks_threshold"))
+		(require-not (sysctl-name "vm.debug_range_enabled"))
 		(require-not (sysctl-name "kern.rage_vnode"))
 		(require-not (sysctl-name "kern.wq_limit_cooperative_threads"))
 		(require-not (system-attribute developer-mode))
```
