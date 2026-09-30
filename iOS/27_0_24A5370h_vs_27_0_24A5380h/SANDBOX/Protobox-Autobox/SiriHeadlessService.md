## SiriHeadlessService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.mobileasset.autoasset"))
-		(require-not (global-name "com.apple.wifi.manager"))
-		(require-not (global-name "com.apple.audio.AudioSession"))
-		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.coreduetd.knowledge"))
+		(require-not (global-name "com.apple.assistantd.odeon-remote"))
 		(require-not (require-any
 			(global-name "com.apple.assistant.device-context")
 			(global-name "com.apple.siri.attendingstates.xpc")
 		))
 		(require-not (global-name "com.apple.siri.audiopowerupdate.xpc"))
+		(require-not (global-name "com.apple.wifi.manager"))
+		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
+		(require-not (global-name "com.apple.audio.AudioSession"))
+		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
+		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
 		(require-not (global-name "com.apple.homed.xpc"))
-		(require-not (global-name "com.apple.assistantd.odeon-remote"))
-		(require-not (global-name "com.apple.symptom_diagnostics"))
-		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
-		(require-not (global-name "com.apple.coreduetd.knowledge"))
 		(require-not (global-name "com.apple.siri.uaf.service"))
 		(require-not (global-name "com.apple.SiriVOXService.client"))
 		(require-not (system-attribute developer-mode))

 		MSC_mach_timebase_info_trap)
 )
 
-(deny syscall-mig
-	(require-all
-		(require-not (kernel-mig-routine
-			host_info
-			host_get_clock_service
-			mach_exception_raise
-			mach_exception_raise_state
-			mach_exception_raise_state_identity
-			io_service_open_extended
-			mach_port_get_context_from_user
-			task_info_from_user
-			semaphore_create
-			vm_remap_external
-			vm_reallocate
-			mach_vm_range_create
-			mach_vm_reallocate
-			task_restartable_ranges_register
-			task_restartable_ranges_synchronize))
-		(require-any
-			(kernel-mig-routine mach_vm_region_recurse)
-			(kernel-mig-routine task_set_exc_guard_behavior)
-			(require-all
-				(require-not (kernel-mig-routine
-					host_info
-					host_get_clock_service
-					mach_exception_raise
-					mach_exception_raise_state
-					mach_exception_raise_state_identity
-					mach_port_get_context_from_user))
-				(require-not (kernel-mig-routine mach_vm_range_create))
-				(require-not (kernel-mig-routine task_restartable_ranges_register))
-				(require-not (kernel-mig-routine task_restartable_ranges_synchronize))
-				(require-not (kernel-mig-routine semaphore_create))
-				(require-not (kernel-mig-routine mach_vm_reallocate))
-				(require-not (kernel-mig-routine task_info_from_user))
-				(require-not (kernel-mig-routine vm_remap_external))
-				(require-not (kernel-mig-routine io_service_open_extended))
-				(require-not (kernel-mig-routine vm_reallocate))
-			)
-		)
-	)
+(deny syscall-mig)
+(allow syscall-mig
+	(kernel-mig-routine
+		host_info
+		host_get_clock_service
+		mach_exception_raise
+		mach_exception_raise_state
+		mach_exception_raise_state_identity
+		io_service_open_extended
+		mach_port_get_context_from_user
+		task_info_from_user
+		semaphore_create
+		vm_remap_external
+		vm_reallocate
+		mach_vm_range_create
+		mach_vm_reallocate
+		task_restartable_ranges_register
+		task_restartable_ranges_synchronize)
 )
 
 (deny sysctl*
```
