## AudioConverterHighCapacityService

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(iokit-registry-entry-class "IOSurfaceRootUserClient")
+		(iokit-registry-entry-class "com_apple_driver_FairPlayIOKitUserClient")
 	)
 )
 

 		SYS_setrlimit
 		SYS_mmap
 		SYS_lseek
+		SYS_ftruncate
 		SYS_sysctl
 		SYS_getumask
 		SYS_getattrlist

 		SYS_fstatat64
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_mremap_encrypted
 		SYS_persona
 		SYS_mach_eventlink_signal
 		SYS_mach_eventlink_wait_until

 
 (deny system-fcntl)
 (allow system-fcntl
-	(fcntl-command F_SETFD F_GETFL F_GETPATH F_ADDFILESIGS_RETURN F_CHECK_LV)
+	(fcntl-command
+		F_GETFD
+		F_SETFD
+		F_GETFL
+		F_GETPATH
+		F_ADDFILESIGS_RETURN
+		F_CHECK_LV)
 )
 
 (deny system-fsctl)

 
 (deny system-kas-info)
 
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
```
