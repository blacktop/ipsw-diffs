## heard

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
 		(require-not (global-name "com.apple.bluetoothaudiod.cb"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))

 		io_service_get_matching_services_bin
 		io_registry_entry_get_properties_bin_buf
 		io_registry_entry_get_property_bin_buf
+		mach_port_deallocate
 		mach_port_request_notification
 		mach_port_set_attributes
 		mach_port_get_context_from_user

 		task_set_exc_guard_behavior
 		task_create_identity_token
 		thread_terminate
+		thread_suspend
 		thread_info
 		thread_policy
 		thread_policy_set
```
