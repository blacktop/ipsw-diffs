## SPIHelper-iOS

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationUserClient")
 		(iokit-registry-entry-class "IOGPUDeviceUserClient")
 		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
+		(iokit-registry-entry-class "IOSurfaceAcceleratorParavirtClient")
 		(iokit-registry-entry-class "IOSurfaceRootUserClient")
 	)
 )

 		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.bird.token"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))

 		SYS_getsockopt
 		SYS_readv
 		SYS_writev
+		SYS_rename
 		SYS_sendto
 		SYS_mkdir
+		SYS_rmdir
 		SYS_pread
 		SYS_pwrite
 		SYS_statfs
 		SYS_fstatfs
+		SYS_quotactl
 		SYS_csops
 		SYS_csops_audittoken
 		SYS_kdebug_typefilter

 		SYS_recvfrom_nocancel
 		SYS_fcntl_nocancel
 		SYS_select_nocancel
+		SYS_fsync_nocancel
 		SYS_connect_nocancel
 		SYS_sigsuspend_nocancel
 		SYS_readv_nocancel

 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_openat_nocancel
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64

 		SYS_getentropy
 		SYS_necp_open
 		SYS_necp_client_action
+		SYS___nexus_set_opt
 		SYS___channel_open
 		SYS___channel_get_info
 		SYS___channel_sync
+		SYS___channel_get_opt
+		SYS___channel_set_opt
 		SYS_ulock_wait
 		SYS_ulock_wake
 		SYS_terminate_with_payload

 		F_GETFD
 		F_SETFD
 		F_GETFL
+		F_SETFL
 		F_SETLKW
 		F_RDADVISE
 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
+		F_BARRIERFSYNC
 		F_OFD_SETLK
+		F_OFD_GETLK
+		F_OFD_SETLKWTIMEOUT
 		F_SETCONFINED
 		F_GETCONFINED
 		F_ADDFILESIGS_RETURN

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 5))
+			(require-not (mac-syscall-number 4))
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

 		NECP_CLIENT_ACTION_COPY_RESULT
 		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
 		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
-		NECP_CLIENT_ACTION_REMOVE)
+		NECP_CLIENT_ACTION_MAP_SYSCTLS
+		NECP_CLIENT_ACTION_REMOVE
+		NECP_CLIENT_ACTION_REMOVE_FLOW
+		NECP_CLIENT_ACTION_UPDATE_CACHE)
 )
 
 (allow process-exec-update-label)
```
