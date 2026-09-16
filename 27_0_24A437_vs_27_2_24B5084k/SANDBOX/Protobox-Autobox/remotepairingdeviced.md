## remotepairingdeviced

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.PineBoardServices"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (require-any

 		))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.remoted"))

 		MSC__kernelrpc_mach_port_type_trap
 		MSC__kernelrpc_mach_port_request_notification_trap
 		MSC_mach_timebase_info_trap
-		MSC_mk_timer_create)
+		MSC_mk_timer_create
+		MSC_mk_timer_destroy)
 )
 
 (deny syscall-mig)

 		io_server_version
 		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
+		io_service_add_notification_bin_64
 		io_registry_entry_get_property_bin_buf
 		mach_port_get_refs
 		mach_port_request_notification
```
