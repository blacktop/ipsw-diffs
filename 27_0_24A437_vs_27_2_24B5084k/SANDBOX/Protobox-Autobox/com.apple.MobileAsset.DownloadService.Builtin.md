## com.apple.MobileAsset.DownloadService.Builtin

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
-		(require-not (xpc-service-name "com.apple.STExtractionService"))
+		(require-not (require-any
+			(xpc-service-name "com.apple.STExtractionService")
+			(xpc-service-name "com.apple.STExtractionService.privileged")
+		))
 		(require-not (xpc-service-name "com.apple.StreamingUnzipService"))
 		(require-not (global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent"))
 		(require-not (system-attribute developer-mode))

 	(ioctl-command
 		CTLIOCGINFO
 		SIOCGCONNINFO
+		SIOCGIFAGENTDATA
 		SIOCGIFCONSTRAINED
 		SIOCGIFDELEGATE
 		SIOCGIFEXPENSIVE

 			SYS_recvmsg
 			SYS_sendmsg
 			SYS_recvfrom
+			SYS_getsockname
 			SYS_crossarch_trap
 			SYS_dup
 			SYS_pipe

 			SYS_kdebug_trace
 			SYS_sigreturn
 			SYS_pathconf
+			SYS_fpathconf
 			SYS_lseek
 			SYS_ftruncate
 			SYS_sysctl

 			SYS_open_dprotected_np
 			SYS_openat_dprotected_np
 			SYS_fgetattrlist
+			SYS_fsetattrlist
+			SYS_listxattr
 			SYS_fsctl
 			SYS_posix_spawn
 			SYS_sysctlbyname
```
