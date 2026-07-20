## com.apple.Virtualization.VirtualMachine

> Group: ⬆️ Updated

```diff

 
 (deny generic-issue-extension)
 
-(deny iokit-issue-extension)
+(deny iokit-get-properties)
 
-(deny iokit-open-user-client)
-(allow iokit-open-user-client
+(deny iokit-open*)
+(allow iokit-open*
 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 		(iokit-registry-entry-class "AppleAVDUserClient")
 		(iokit-registry-entry-class "AppleAVE2UserClient")
 		(iokit-registry-entry-class "AppleJPEGDriverUserClient")
+		(iokit-registry-entry-class "AppleUSBUserHCIUserClient")
 		(iokit-registry-entry-class "IOGPUDeviceUserClient")
 		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 		(iokit-registry-entry-class "IOSurfaceRootUserClient")

 	)
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleAOPAudioController")

 		(iokit-registry-entry-class "AppleAVE2Driver")
 		(iokit-registry-entry-class "AppleJPEGDriver")
 		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
+		(iokit-registry-entry-class "AppleUSBUserHCIResources")
 		(iokit-registry-entry-class "IOPMrootDomain")
 		(iokit-registry-entry-class "IOSurfaceRoot")
 		(iokit-registry-entry-class "com_apple_driver_FairPlayIOKit")
 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")

 	)
 )
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.system.notification_center"))

 	)
 )
 
+(deny process-codesigning)
+(allow process-codesigning
+	(literal "/bin/rm")
+)
+
 (deny process-exec*)
 (allow process-exec*
 	(literal "/bin/rm")

 	(machtrap-number
 		MSC__kernelrpc_mach_vm_allocate_trap
 		MSC__kernelrpc_mach_vm_deallocate_trap
+		MSC_task_dyld_process_info_notify_get
 		MSC__kernelrpc_mach_vm_protect_trap
 		MSC__kernelrpc_mach_vm_map_trap
 		MSC__kernelrpc_mach_port_allocate_trap

 			io_registry_entry_from_path
 			io_registry_entry_get_parent_iterator
 			io_service_close
+			io_connect_set_properties
 			io_registry_entry_get_path
 			io_service_open_extended
 			io_connect_method
```
