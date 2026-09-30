## intentrecommendd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.healthd.server"))
 		(require-not (global-name "com.apple.linkd.registry"))
+		(require-not (global-name "com.apple.healthd.server"))
 		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.CARenderServer"))

 			SYS___pthread_kill
 			SYS___pthread_sigmask
 			SYS___sigwait
+			SYS___pthread_markcancel
+			SYS___pthread_canceled
 			SYS_proc_info
 			SYS_getdirentries64
 			SYS_getfsstat64
+			SYS___pthread_chdir
+			SYS___pthread_fchdir
 			SYS_thread_selfid
 			SYS___mac_syscall
 			SYS_read_nocancel
```
