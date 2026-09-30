## misagent

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.mobile.heartbeat"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.trustd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.mobile.heartbeat"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))

 		vm_remap_external
 		vm_reallocate
 		mach_vm_copy
+		mach_vm_behavior_set
 		mach_vm_map_external
 		mach_vm_region_recurse
+		mach_vm_region
 		_mach_make_memory_entry
 		mach_vm_page_range_query
 		mach_vm_range_create
 		mach_vm_reallocate
 		mach_memory_entry_ownership
+		mach_voucher_extract_all_attr_recipes
 		mach_voucher_attr_command
 		UNDNotificationCreated_rpc
 		task_restartable_ranges_register
```
