## com.apple.dext

> Group: ⬆️ Updated

```diff

 
 (allow file-read*
 	(require-all
-		(literal "/private")
+		(literal "/System")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private/preboot")
 		(process-attribute is-apple-signed-executable)
 	)
 )

 )
 (allow file-read*
 	(require-all
-		(literal "/System")
-		(process-attribute is-apple-signed-executable)
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/private/preboot")
+		(literal "/private")
 		(process-attribute is-apple-signed-executable)
 	)
 )

 
 (allow file-read-metadata
 	(require-all
-		(literal "/private")
+		(literal "/System")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(literal "/private/preboot")
 		(process-attribute is-apple-signed-executable)
 	)
 )

 )
 (allow file-read-metadata
 	(require-all
-		(literal "/System")
-		(process-attribute is-apple-signed-executable)
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(literal "/private/preboot")
+		(literal "/private")
 		(process-attribute is-apple-signed-executable)
 	)
 )

 (deny file-test-existence)
 (allow file-test-existence
 	(require-all
-		(literal "/private")
+		(literal "/System")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow file-test-existence
+	(require-all
+		(literal "/private/preboot")
 		(process-attribute is-apple-signed-executable)
 	)
 )

 )
 (allow file-test-existence
 	(require-all
-		(literal "/System")
-		(process-attribute is-apple-signed-executable)
-	)
-)
-(allow file-test-existence
-	(require-all
-		(literal "/private/preboot")
+		(literal "/private")
 		(process-attribute is-apple-signed-executable)
 	)
 )

 
 (deny iokit-open-service)
 (allow iokit-open-service
-	(require-all
-		(iokit-registry-entry-class "IOPlatformExpert")
-		(require-not (state-flag "driverkit-post-launch"))
-	)
+	(iokit-registry-entry-class "IOPlatformExpertDevice")
 )
-(allow iokit-open-service
+(deny iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "IOPlatformExpertDevice")
-		(require-not (state-flag "driverkit-post-launch"))
+		(state-flag "driverkit-post-launch")
 	)
 )
 

 (allow syscall-unix
 	(require-all
 		(system-attribute internal-build)
-		(require-not (syscall-number SYS_shm_open))
-		(require-not (syscall-number SYS_fstatfs64))
 		(require-not (syscall-number SYS_getegid))
-		(require-not (syscall-number SYS_objc_bp_assist_cfg_np))
 		(require-not (syscall-number SYS_getdirentries64))
+		(require-not (syscall-number SYS_shm_open))
+		(require-not (syscall-number SYS_objc_bp_assist_cfg_np))
+		(require-not (syscall-number SYS_fstatfs64))
 		(require-any
 			(syscall-number SYS_setrlimit)
 			(syscall-number SYS_sigaction)

 		(sysctl-name "vm.debug_range_enabled")
 	)
 )
+(deny sysctl*
+	(require-all
+		(system-attribute internal-build)
+		(sysctl-name "vm.debug_range_enabled")
+		(require-any
+			(sysctl-name "vm.footprint_suspend")
+			(sysctl-name "vm.task_no_footprint_for_debug")
+		)
+	)
+)
 (deny sysctl*)
 
 (allow sysctl-read)
```
