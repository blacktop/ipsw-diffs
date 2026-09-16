## replayd

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationUserClient")
+		(iokit-registry-entry-class "H1xANELoadBalancerDirectPathClient")
 		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 		(iokit-registry-entry-class "IOSurfaceRootUserClient")
 	)

 		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
 		(iokit-registry-entry-class "AppleM2ScalerParavirtDriver")
 		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationDriver")
+		(iokit-registry-entry-class "H1xANELoadBalancer")
 		(iokit-registry-entry-class "IOPMrootDomain")
 		(iokit-registry-entry-class "IOSurfaceRoot")
 	)

 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
+		(require-not (global-name "com.apple.systemstatus"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.bird.token"))

 		SYS_getumask
 		SYS_getattrlist
 		SYS_fgetattrlist
+		SYS_fsetattrlist
 		SYS_fgetxattr
 		SYS_listxattr
 		SYS_fsctl

 		MSC__kernelrpc_mach_port_get_attributes_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
+		MSC_task_name_for_pid
 		MSC_pid_for_task
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port

 		mach_vm_region_recurse
 		mach_vm_region
 		_mach_make_memory_entry
+		mach_vm_page_range_query
 		mach_vm_deferred_reclamation_buffer_flush
 		mach_vm_range_create
 		mach_vm_reallocate
```
