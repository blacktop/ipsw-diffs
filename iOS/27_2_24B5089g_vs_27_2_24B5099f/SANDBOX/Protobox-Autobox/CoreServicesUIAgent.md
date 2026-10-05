## CoreServicesUIAgent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.hangtracerd"))
+		(require-not (global-name "com.apple.manageddeviced.managed-apps"))
 		(require-not (global-name "com.apple.UIKit.KeyboardManagement.hosted"))
 		(require-not (global-name "com.apple.PrototypeTools.domainserver"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.inputanalyticsd"))
+		(require-not (global-name "com.apple.appprotectiond.guard"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))

 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
+		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (local-name "com.apple.accessibility.gax.client"))

 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
+		SYS_unlinkat
 		SYS_mkdirat
 		SYS_bsdthread_ctl
 		SYS_guarded_open_dprotected_np

 		SYS_guarded_pwrite_np
 		SYS_guarded_writev_np
 		SYS_persona
+		SYS_work_interval_ctl
 		SYS_getentropy
 		SYS_necp_open
 		SYS_necp_client_action

 			mach_vm_region
 			_mach_make_memory_entry
 			mach_vm_deferred_reclamation_buffer_allocate
+			mach_vm_deferred_reclamation_buffer_flush
 			mach_vm_range_create
+			mach_vm_deferred_reclamation_buffer_resize
 			mach_vm_reallocate
 			mach_memory_entry_ownership
 			mach_voucher_attr_command
```
