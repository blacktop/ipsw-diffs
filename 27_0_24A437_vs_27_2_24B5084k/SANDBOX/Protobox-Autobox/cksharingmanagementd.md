## cksharingmanagementd

> Group: ⬆️ Updated

```diff

 			SYS_lseek
 			SYS_sysctl
 			SYS_getumask
+			SYS_openat_dprotected_np
 			SYS_fgetattrlist
+			SYS_fgetxattr
 			SYS_fsctl
 			SYS_sysctlbyname
 			SYS_gettid

 			SYS_fsgetpath
 			SYS_memorystatus_control
 			SYS_openat
+			SYS_renameat
 			SYS_fstatat
 			SYS_fstatat64
 			SYS_mkdirat

 			SYS_memorystatus_available_memory
 			SYS_preadv
 			SYS_preadv_nocancel
+			SYS_proc_info_extended_id
 			SYS_map_with_linking_np))
 		(require-any
 			(require-all

 		io_connect_method
 		io_service_get_matching_service
 		io_server_version
+		io_service_get_matching_service_bin
+		io_registry_entry_get_property_bin_buf
 		mach_port_request_notification
 		mach_port_set_attributes
 		mach_port_get_context_from_user

 
 (deny system-fcntl)
 (allow system-fcntl
-	(fcntl-command F_GETFL F_GETPATH F_ADDFILESIGS_RETURN F_CHECK_LV)
+	(fcntl-command F_GETFL F_NOCACHE F_GETPATH F_ADDFILESIGS_RETURN F_CHECK_LV)
 )
 
 (deny system-fsctl)

 
 (deny system-kas-info)
 
-(with-filter (mac-policy-name "Sandbox")
+(with-filter (mac-policy-name "AMFI")
 	(deny system-mac-syscall
 		(require-all
-			(require-not (mac-syscall-number 4))
-			(require-not (mac-syscall-number 67))
-			(require-not (mac-syscall-number 2))
+			(require-not (mac-syscall-number 95))
+			(require-not (mac-syscall-number 96))
+			(require-not (mac-syscall-number 90))
+			(require-not (mac-syscall-number 102))
 		)
 	)
 )
 (deny system-mac-syscall
 	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
+		(require-not (mac-policy-name "Sandbox"))
+		(require-not (mac-syscall-number 2))
 	)
 )
 
```
