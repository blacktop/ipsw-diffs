## uiautomationd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.commcenter.xpc"))
-		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.dnssd.service"))
-		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
-		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.trustd"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.iohideventsystem"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.iohideventsystem"))
+		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (local-name "com.apple.iphone.axserver"))
 		(require-not (global-name "com.apple.CARenderServer"))

 							mach_exception_raise_state_identity
 							mach_port_get_context_from_user))
 						(require-not (kernel-mig-routine mach_vm_range_create))
+						(require-not (kernel-mig-routine vm_remap_external))
 						(require-not (kernel-mig-routine task_restartable_ranges_register))
 						(require-not (kernel-mig-routine task_restartable_ranges_synchronize))
-						(require-not (kernel-mig-routine semaphore_create))
 						(require-not (kernel-mig-routine mach_vm_reallocate))
+						(require-not (kernel-mig-routine semaphore_create))
 						(require-not (kernel-mig-routine task_info_from_user))
-						(require-not (kernel-mig-routine vm_remap_external))
 						(require-not (kernel-mig-routine io_service_open_extended))
 						(require-not (kernel-mig-routine vm_reallocate))
 					)
```
