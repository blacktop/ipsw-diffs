## stickersd

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "AppleJPEGDriverUserClient")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationUserClient")
+		(iokit-registry-entry-class "AppleVirtIONeuralEngineDeviceUserClient")
 		(iokit-registry-entry-class "IOGPUDeviceUserClient")
 		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 		(iokit-registry-entry-class "IOSurfaceAcceleratorParavirtClient")

 		(iokit-registry-entry-class "AppleM2ScalerParavirtDriver")
 		(iokit-registry-entry-class "AppleParavirtGPU")
 		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationDriver")
+		(iokit-registry-entry-class "AppleVirtIONeuralEngineDevice")
+		(iokit-registry-entry-class "H1xANELoadBalancer")
 		(iokit-registry-entry-class "IOSurfaceRoot")
 	)
 )

 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
 		(require-not (global-name "com.apple.biome.compute.source"))
+		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))

 		SYS_munmap
 		SYS_mprotect
 		SYS_madvise
+		SYS_dup2
 		SYS_fcntl
 		SYS_fsync
 		SYS_socket

 		SYS_lstat_extended
 		SYS_fstat_extended
 		SYS_fchmod_extended
+		SYS_access_extended
 		SYS_gettid
 		SYS_mkdir_extended
 		SYS_shared_region_check_np

 		io_server_version
 		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
+		io_service_add_notification_bin_64
 		io_registry_entry_get_property_bin_buf
 		mach_port_deallocate
 		mach_port_get_refs

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
-	)
-)
-(deny system-mac-syscall
-	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
-	)
-)
+(deny system-mac-syscall)
 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
```
