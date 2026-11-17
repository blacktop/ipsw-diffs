## powerd

> Group: ⬆️ Updated

```diff

 	)
 )
 
-(deny job-creation)
-
 (deny mach-issue-extension)
 
 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.biome.access.user"))
+		(require-not (global-name "com.apple.dt.instruments.dtsecurity.xpc"))
 		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
 		(require-not (global-name "com.apple.biome.compute.source"))
 		(require-not (global-name "com.apple.biome.access.system"))

 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.powerexperienced.resourceusage"))
 		(require-not (global-name "com.apple.timed.xpc"))
+		(require-not (global-name "com.apple.security.cryptexd"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))

 	)
 )
 
-(deny process-exec*
-	(require-any
-		(require-not (require-any
-			(literal "/usr/local/bin/ulpm_reload_sb.sh")
-			(literal "/usr/local/bin/ulpm_sfi.sh")
-		))
-		(require-not (system-attribute internal-build))
-	)
+(deny process-exec*)
+(allow process-exec*
+	(literal "/usr/libexec/debugserver")
 )
 
 (deny process-exec-interpreter
 	(require-all
 		(require-not (literal "/bin/sh"))
 		(require-any
-			(require-not (require-any
-				(literal "/usr/local/bin/ulpm_reload_sb.sh")
-				(literal "/usr/local/bin/ulpm_sfi.sh")
-			))
-			(require-not (system-attribute internal-build))
+			(require-all
+				(system-attribute internal-build)
+				(require-not (require-any
+					(literal "/usr/local/bin/ulpm_reload_sb.sh")
+					(literal "/usr/local/bin/ulpm_sfi.sh")
+				))
+				(require-not (literal "/usr/libexec/debugserver"))
+			)
+			(require-not (literal "/usr/libexec/debugserver"))
 		)
 	)
 )

 (allow syscall-unix
 	(syscall-number
 		SYS_exit
+		SYS_fork
 		SYS_read
 		SYS_write
 		SYS_open

 		SYS_geteuid
 		SYS_access
 		SYS_crossarch_trap
+		SYS_getppid
 		SYS_dup
 		SYS_getegid
 		SYS_sigaction

 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_task_name_for_pid
+		MSC_task_for_pid
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
 		MSC_swtch_pri

 		mach_port_set_attributes
 		mach_port_get_context_from_user
 		mach_port_is_connection_for_service
+		mach_ports_register
 		mach_ports_lookup
 		task_info_from_user
 		task_get_special_port_from_user
```
