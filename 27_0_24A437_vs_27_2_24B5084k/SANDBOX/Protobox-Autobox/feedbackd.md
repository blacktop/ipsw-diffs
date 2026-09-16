## feedbackd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.springboard.services"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.diagnosticextensionsd.session"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.diagd"))

 		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.awdd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (system-attribute developer-mode))

 		SYS_open_dprotected_np
 		SYS_openat_dprotected_np
 		SYS_getattrlist
+		SYS_fsetattrlist
+		SYS_fgetxattr
 		SYS_setxattr
+		SYS_flistxattr
 		SYS_fsctl
 		SYS_shm_open
 		SYS_sysctlbyname

 		io_service_add_interest_notification_64
 		io_server_version
 		io_service_get_matching_service_bin
+		io_registry_entry_get_property_bin_buf
 		mach_port_destroy
 		mach_port_get_refs
 		mach_port_request_notification

 		F_SETFD
 		F_GETFL
 		F_SETFL
+		F_NOCACHE
 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_DUPFD_CLOEXEC
```
