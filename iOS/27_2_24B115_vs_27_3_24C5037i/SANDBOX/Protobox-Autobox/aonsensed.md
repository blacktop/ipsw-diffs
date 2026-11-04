## aonsensed

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 		(iokit-registry-entry-class "AFKEndpointInterfaceUserClient")
 		(iokit-registry-entry-class "AFKSharedMemoryUserClient")
+		(iokit-registry-entry-class "AppleJPEGDriverUserClient")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(iokit-registry-entry-class "AppleSPUHIDDeviceUserClient")
 		(iokit-registry-entry-class "H11ANEInDirectPathClient")

 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.logd.admin"))
+		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.polaris.cache"))
 		(require-not (global-name "com.apple.siri.uaf.service"))
 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))

 		(require-not (xpc-service-name "com.apple.aonsensed.camera-xpc"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.AppleDeviceQueryService"))
-		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (system-attribute developer-mode))
 	)

 		SYS_readv
 		SYS_writev
 		SYS_fchown
+		SYS_fchmod
 		SYS_rename
 		SYS_flock
 		SYS_sendto

 		SYS_fgetattrlist
 		SYS_fsetattrlist
 		SYS_getxattr
+		SYS_fgetxattr
 		SYS_fsetxattr
 		SYS_listxattr
+		SYS_flistxattr
 		SYS_fsctl
 		SYS_posix_spawn
 		SYS_ffsctl

 		SYS_stat_extended
 		SYS_lstat_extended
 		SYS_fstat_extended
+		SYS_fchmod_extended
 		SYS_gettid
 		SYS_mkdir_extended
 		SYS_shared_region_check_np

 		SYS_change_fdguard_np
 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
+		SYS_clonefileat
 		SYS_openat
 		SYS_renameat
 		SYS_faccessat

 		F_GETFL
 		F_SETFL
 		F_SETLKW
+		F_PREALLOCATE
 		F_NOCACHE
 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_SETNOSIGPIPE
+		F_SINGLE_WRITER
 		F_BARRIERFSYNC
 		F_OFD_SETLK
 		F_OFD_GETLK

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 5))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(with-filter (mac-policy-name "vnguard")
+	(deny system-mac-syscall
+		(require-not (mac-syscall-number 1))
 	)
 )
 (deny system-mac-syscall
```
