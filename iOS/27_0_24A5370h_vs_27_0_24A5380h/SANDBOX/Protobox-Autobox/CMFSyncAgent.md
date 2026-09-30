## CMFSyncAgent

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.research.adtcd"))
-		(require-not (global-name "com.apple.contactsd"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.nanoprefsync"))
-		(require-not (global-name "com.apple.contacts.poster.api"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.kvsdebug"))
-		(require-not (global-name "com.apple.StatusKit.publish"))
-		(require-not (global-name "com.apple.kvsd"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
-		(require-not (global-name "com.apple.privacyaccountingd"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
+		(require-not (global-name "com.apple.nanoprefsync"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.tccd"))
-		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.kvsd"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.contacts.poster.api"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.kvsdebug"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.StatusKit.publish"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.research.adtcd"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.contactsd"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.ABDatabaseDoctor"))
 		(require-not (system-attribute developer-mode))

 		io_service_get_matching_service_bin
 		io_registry_entry_get_properties_bin_buf
 		io_registry_entry_get_property_bin_buf
+		mach_port_deallocate
 		mach_port_request_notification
 		mach_port_set_attributes
 		mach_port_get_context_from_user

 		semaphore_destroy
 		task_set_exc_guard_behavior
 		thread_terminate
+		thread_suspend
 		vm_map_external
 		vm_remap_external
 		vm_reallocate
```
