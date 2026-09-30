## SidecarRelay

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.timesync.expositor"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.accountsd.accountmanager"))
-		(require-not (global-name "com.apple.wifi.manager"))
-		(require-not (global-name "com.apple.private.corewifi-xpc"))
 		(require-not (require-any
 			(global-name "com.apple.timesync.manager")
 			(global-name "com.apple.timesync.ptp.manager")
 		))
-		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.RemoteDisplay"))
-		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.springboard.services"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.videoconference.camera"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.private.corewifi-xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.wifi.manager"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (global-name "com.apple.springboard.services"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.timesync.expositor"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.RemoteDisplay"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.CompanionLink"))
 		(require-not (system-attribute developer-mode))
 	)

 					mach_exception_raise
 					mach_exception_raise_state
 					mach_exception_raise_state_identity))
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
