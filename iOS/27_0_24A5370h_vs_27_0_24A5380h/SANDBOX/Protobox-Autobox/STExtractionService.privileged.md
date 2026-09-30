## STExtractionService.privileged

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.fairplayd.versioned"))
-		(require-not (global-name "com.apple.fairplayd.xpc"))
 		(require-not (global-name "com.apple.installcoordinationd"))
-		(require-not (xpc-service-name "com.apple.backgroundassets.managed.relay.service"))
+		(require-not (global-name "com.apple.fairplayd.xpc"))
 		(require-not (xpc-service-name "com.apple.StreamingUnzipService"))
+		(require-not (xpc-service-name "com.apple.backgroundassets.managed.relay.service"))
 		(require-not (xpc-service-name "com.apple.backgroundassets.managed.helper.service"))
 		(require-not (system-attribute developer-mode))
 	)

 			SYS_sigprocmask
 			SYS_sigpending
 			SYS_sigaltstack
+			SYS_symlink
 			SYS_readlink
 			SYS_umask
 			SYS_mprotect

 			SYS_open_dprotected_np
 			SYS_openat_dprotected_np
 			SYS_fsetattrlist
+			SYS_flistxattr
 			SYS_fsctl
 			SYS_sysctlbyname
 			SYS_gettid

 		io_service_open_extended
 		io_connect_method
 		io_server_version
+		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
 		mach_port_set_attributes
 		mach_port_get_context_from_user

 		F_SETFL
 		F_NOCACHE
 		F_GETPATH
+		F_GETPROTECTIONCLASS
+		F_SETPROTECTIONCLASS
+		F_SINGLE_WRITER
 		F_ADDFILESIGS_RETURN
 		F_CHECK_LV
 		F_PUNCHHOLE

 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
+			(require-not (mac-syscall-number 80))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 67))
 			(require-not (mac-syscall-number 2))
```
