## tailspind

> Group: ⬆️ Updated

```diff

 
 (deny generic-issue-extension)
 
-(deny iokit-issue-extension)
+(deny iokit-get-properties)
 
-(deny iokit-open-user-client)
-(allow iokit-open-user-client
+(deny iokit-open*)
+(allow iokit-open*
 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")

 	)
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "AppleHWAccess")
 		(iokit-registry-entry-class "AppleKeyStore")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.*")
 		(ipc-posix-name "apple.cfprefs.daemonv1")

 	)
 )
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))

 	)
 )
 
+(deny process-codesigning
+	(require-all
+		(require-not (literal "/usr/bin/tailspin"))
+		(require-not (literal "/usr/bin/plutil"))
+		(require-not (literal "/bin/sh"))
+	)
+)
+(deny process-codesigning
+	(require-all
+		(literal "/usr/local/bin/darwinup")
+		(require-not (system-attribute internal-build))
+	)
+)
+
 (deny process-exec*
 	(require-all
 		(require-not (literal "/usr/bin/tailspin"))

 		SYS_sysctl
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_fgetattrlist
 		SYS_getxattr

 			(sysctl-name "kperf.timer.period")
 		))
 		(require-not (sysctl-name "vm.debug_range_enabled"))
+		(require-not (sysctl-name "ktrace.init_background"))
 		(require-not (require-any
+			(sysctl-name "kperf.lazy.cpu_action")
 			(sysctl-name "kperf.lazy.cpu_time_threshold")
-			(sysctl-name "ktrace.init_background")
 		))
 		(require-not (require-any
 			(sysctl-name "kperf.lightweight_pet")
 			(sysctl-name "kperf.timer.pet_timer")
 		))
-		(require-not (sysctl-name "kperf.lazy.cpu_action"))
 		(require-not (sysctl-name "kern.grade_cputype"))
 		(require-not (sysctl-name "kern.wq_limit_cooperative_threads"))
 		(require-not (system-attribute developer-mode))
```
