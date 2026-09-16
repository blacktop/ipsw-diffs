## askpermissiond

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 		(iokit-registry-entry-class "AppleJPEGDriverUserClient")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
+		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationUserClient")
+		(iokit-registry-entry-class "IOGPUDeviceUserClient")
+		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 		(iokit-registry-entry-class "IOSurfaceRootUserClient")
 	)
 )

 (deny iokit-open-service)
 (allow iokit-open-service
 	(require-any
+		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleJPEGDriver")
 		(iokit-registry-entry-class "AppleKeyStore")
+		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
+		(iokit-registry-entry-class "AppleM2ScalerParavirtDriver")
+		(iokit-registry-entry-class "AppleParavirtGPU")
 		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationDriver")
 		(iokit-registry-entry-class "IOSurfaceRoot")
 	)

 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.appstored.xpc"))
 		(require-not (global-name "com.apple.cfnetwork.AuthBrokerAgent"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.networkserviceproxy"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))

 		(require-not (global-name "com.apple.adid"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.SystemConfiguration.DNSConfiguration"))
+		(require-not (global-name "com.apple.fairplayd"))
 		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.GSSCred"))
 		(require-not (global-name "com.apple.logd.events"))

 		SYS_getfsstat64
 		SYS_bsdthread_create
 		SYS_bsdthread_terminate
+		SYS_kqueue
 		SYS_kevent
 		SYS_bsdthread_register
 		SYS_workq_open

 		SYS_memorystatus_control
 		SYS_guarded_open_np
 		SYS_guarded_close_np
+		SYS_guarded_kqueue_np
 		SYS_change_fdguard_np
 		SYS_proc_rlimit_control
 		SYS_connectx

 		SYS_terminate_with_payload
 		SYS_abort_with_payload
 		SYS_os_fault_with_payload
+		SYS_kqueue_workloop_ctl
 		SYS_memorystatus_available_memory
 		SYS_objc_bp_assist_cfg_np
 		SYS_shared_region_map_and_slide_2_np

 		io_service_close
 		io_service_open_extended
 		io_connect_method
+		io_connect_async_method
 		io_service_add_interest_notification_64
+		io_registry_entry_get_registry_entry_id
 		io_server_version
 		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
```
