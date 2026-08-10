## askpermissiond

> Group: ⬆️ Updated

```diff

 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
+		(iokit-registry-entry-class "AppleJPEGDriverUserClient")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
+		(iokit-registry-entry-class "IOSurfaceRootUserClient")
 	)
 )
 
 (deny iokit-open-service)
 (allow iokit-open-service
-	(iokit-registry-entry-class "AppleKeyStore")
+	(require-any
+		(iokit-registry-entry-class "AppleJPEGDriver")
+		(iokit-registry-entry-class "AppleKeyStore")
+		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationDriver")
+		(iokit-registry-entry-class "IOSurfaceRoot")
+	)
 )
 
 (deny iokit-set-properties)

 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.xpc.amstreatmentstoreservice"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.amsservicesanalytics.xpc"))

 		(require-not (global-name "com.apple.ScreenTimeAgent.exception"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.private"))
 		(require-not (global-name "com.apple.lsd.open"))
+		(require-not (global-name "com.apple.contactsd"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-any
 			(require-all

 		SYS_sysctl
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_fgetattrlist
 		SYS_getxattr

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64

 		MSC_mk_timer_create
 		MSC_mk_timer_destroy
 		MSC_mk_timer_arm
-		MSC_mk_timer_cancel)
+		MSC_mk_timer_cancel
+		MSC_iokit_user_client_trap)
 )
 
 (deny syscall-mig)

 		mach_exception_raise
 		mach_exception_raise_state
 		mach_exception_raise_state_identity
+		io_iterator_next
 		io_registry_entry_from_path
+		io_service_close
 		io_service_open_extended
 		io_connect_method
 		io_service_add_interest_notification_64
 		io_server_version
 		io_service_get_matching_service_bin
+		io_service_get_matching_services_bin
 		io_registry_entry_get_property_bin_buf
 		mach_port_get_refs
 		mach_port_request_notification
```
