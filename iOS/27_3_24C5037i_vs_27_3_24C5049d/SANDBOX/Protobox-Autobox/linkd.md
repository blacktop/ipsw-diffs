## linkd

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(iokit-registry-entry-class "IOGPUDeviceUserClient")
+		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
+		(iokit-registry-entry-class "IOSurfaceAcceleratorParavirtClient")
 	)
 )
 

 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
+		(iokit-registry-entry-class "AppleM2ScalerParavirtDriver")
 	)
 )
 

 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
+		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.uservault"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.linkd.autoShortcut"))

 		SYS_gettimeofday
 		SYS_readv
 		SYS_writev
+		SYS_rename
 		SYS_flock
 		SYS_sendto
 		SYS_mkdir

 		io_registry_entry_from_path
 		io_registry_entry_get_name
 		io_registry_entry_get_parent_iterator
+		io_service_close
 		io_registry_entry_create_iterator
 		io_iterator_is_valid
 		io_service_add_interest_notification
```
