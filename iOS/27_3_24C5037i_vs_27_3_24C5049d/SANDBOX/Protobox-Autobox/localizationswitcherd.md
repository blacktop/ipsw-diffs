## localizationswitcherd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.intelligenceplatform.View"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.biome.compute.publisher.service"))
 		(require-not (global-name "com.apple.corefollowup.agent"))
 		(require-not (global-name "com.apple.diagd"))

 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		SYS_gettimeofday
 		SYS_readv
 		SYS_writev
+		SYS_fchmod
 		SYS_flock
 		SYS_sendto
 		SYS_mkdir
+		SYS_rmdir
 		SYS_pread
 		SYS_pwrite
 		SYS_statfs

 		SYS_memorystatus_control
 		SYS_guarded_open_np
 		SYS_guarded_close_np
+		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
 		SYS_renameat

 		io_service_get_matching_service
 		io_server_version
 		io_service_get_matching_service_bin
+		io_service_get_matching_services_bin
 		mach_port_get_refs
 		mach_port_request_notification
 		mach_port_set_attributes

 		F_SETFD
 		F_GETFL
 		F_SETLKW
+		F_RDADVISE
 		F_NOCACHE
 		F_GETPATH
 		F_GETPROTECTIONCLASS
```
