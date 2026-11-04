## servicesintelligenced

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (xpc-service-name "com.apple.ServicesIntelligenceXPCService"))
 		(require-not (global-name "com.apple.FileCoordination"))
+		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
 	)

 		SYS___sigwait_nocancel
 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
+		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_guarded_open_np
 		SYS_guarded_close_np

 		io_registry_entry_from_path
 		io_service_open_extended
 		io_connect_method
+		io_service_add_interest_notification_64
 		io_server_version
 		io_service_get_matching_service_bin
 		io_registry_entry_get_property_bin_buf

 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
+		F_DUPFD_CLOEXEC
 		F_BARRIERFSYNC
 		F_OFD_SETLK
 		F_OFD_GETLK

 
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
