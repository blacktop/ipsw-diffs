## healthd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.Carousel.contextuallock"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))

 			(xpc-service-name "com.apple.HeartRhythmAlgorithms.ClassifierService")
 			(xpc-service-name "com.apple.WorkoutKitXPCService")
 			(xpc-service-name "com.apple.health.RemoteHeartRateStreamService")
+			(xpc-service-name "com.apple.health.records.assembler")
 			(xpc-service-name "com.apple.health.records.legacy-ingestion")
 		))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))

 		mach_vm_region_recurse
 		mach_vm_region
 		_mach_make_memory_entry
+		mach_vm_page_range_query
 		mach_vm_deferred_reclamation_buffer_flush
 		mach_vm_range_create
 		mach_vm_reallocate

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
-	)
-)
-(deny system-mac-syscall
-	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
-	)
-)
+(deny system-mac-syscall)
 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
```
