## com.apple.SpeechRecognitionCore.brokerd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.kvsd"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.triald.namespace-management"))
+		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (xpc-service-name "com.apple.speech.localspeechrecognition"))
 		(require-not (xpc-service-name "com.apple.SpeechRecognitionCore.speechrecognitiond"))
 		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.analyticsd"))
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
