## voicememod

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))

 		MSC_semaphore_timedwait_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
+		MSC_task_name_for_pid
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
 		MSC_swtch_pri

 		io_service_get_matching_service_bin
 		io_registry_entry_get_property_bin_buf
 		mach_port_request_notification
+		mach_port_extract_right
 		mach_port_set_attributes
 		mach_port_get_context_from_user
 		mach_port_is_connection_for_service
```
