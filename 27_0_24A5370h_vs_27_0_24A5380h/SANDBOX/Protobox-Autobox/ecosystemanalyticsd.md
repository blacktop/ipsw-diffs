## ecosystemanalyticsd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.debug.telemetry"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
-		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.coresymbolicationd"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.lsd.advertisingidentifiers"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.debug.telemetry"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (system-attribute developer-mode))

 		mach_vm_read
 		mach_vm_copy
 		mach_vm_read_overwrite
+		mach_vm_behavior_set
 		mach_vm_map_external
 		mach_vm_remap_external
 		mach_vm_region_recurse

 		mach_vm_range_create
 		mach_vm_reallocate
 		mach_memory_entry_ownership
+		mach_voucher_extract_all_attr_recipes
 		mach_voucher_attr_command
 		task_restartable_ranges_register
 		task_restartable_ranges_synchronize)
```
