## sucontrollerd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.mobileasset.autoasset"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.GSSCred"))
-		(require-not (global-name "com.apple.mobileassetd.v2"))
-		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
-		(require-not (global-name "com.apple.nehelper"))
-		(require-not (global-name "com.apple.appstored.xpc.request"))
-		(require-not (global-name "com.apple.cache_delete"))
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.mobile.softwareupdated"))
 		(require-not (global-name "com.apple.remoted"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.nehelper"))
+		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
+		(require-not (global-name "com.apple.cache_delete"))
+		(require-not (global-name "com.apple.appstored.xpc.request"))
+		(require-not (global-name "com.apple.GSSCred"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (xpc-service-name "com.apple.sucore.SUCoreHelperService"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (system-attribute developer-mode))

 					mach_exception_raise_state
 					mach_exception_raise_state_identity))
 				(require-not (kernel-mig-routine mach_vm_range_create))
+				(require-not (kernel-mig-routine vm_remap_external))
 				(require-not (kernel-mig-routine task_restartable_ranges_register))
 				(require-not (kernel-mig-routine task_restartable_ranges_synchronize))
-				(require-not (kernel-mig-routine semaphore_create))
 				(require-not (kernel-mig-routine mach_vm_reallocate))
+				(require-not (kernel-mig-routine semaphore_create))
 				(require-not (kernel-mig-routine task_info_from_user))
-				(require-not (kernel-mig-routine vm_remap_external))
 				(require-not (kernel-mig-routine io_service_open_extended))
 				(require-not (kernel-mig-routine vm_reallocate))
 			)
```
