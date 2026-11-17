## anomalydetectiond

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.mobileactivationd"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.biome.compute.publisher.service"))
 		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.sos"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))

 		MSC__kernelrpc_mach_port_get_attributes_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
+		MSC_task_name_for_pid
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
 		MSC_swtch_pri

 		MSC__exclaves_ctl_trap
 		MSC_mach_timebase_info_trap
 		MSC_mk_timer_create
+		MSC_mk_timer_destroy
 		MSC_mk_timer_arm
 		MSC_mk_timer_cancel)
 )

 		io_registry_entry_get_registry_entry_id
 		io_server_version
 		io_service_get_matching_service_bin
+		io_service_get_matching_services_bin
 		io_service_add_notification_bin
 		io_service_add_notification_bin_64
 		io_registry_entry_get_property_bin_buf
```
