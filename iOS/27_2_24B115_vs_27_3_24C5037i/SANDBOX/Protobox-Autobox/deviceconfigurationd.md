## deviceconfigurationd

> Group: ⬆️ Updated

```diff

 			SYS_sigprocmask
 			SYS_sigpending
 			SYS_sigaltstack
+			SYS_readlink
 			SYS_umask
 			SYS_mprotect
 			SYS_fcntl

 			SYS_psynch_mutexwait
 			SYS_psynch_mutexdrop
 			SYS_psynch_cvbroad
+			SYS_psynch_cvsignal
 			SYS_psynch_cvwait
 			SYS_psynch_rw_rdlock
 			SYS_psynch_rw_wrlock

 		task_set_exc_guard_behavior
 		vm_remap_external
 		vm_reallocate
+		mach_vm_copy
 		mach_vm_read_overwrite
 		mach_vm_behavior_set
 		mach_vm_map_external

 
 (deny system-kas-info)
 
-(with-filter (mac-policy-name "Sandbox")
-	(deny system-mac-syscall
-		(require-all
-			(require-not (mac-syscall-number 4))
-			(require-not (mac-syscall-number 67))
-			(require-not (mac-syscall-number 2))
-		)
-	)
-)
-(deny system-mac-syscall
-	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
-	)
-)
+(deny system-mac-syscall)
 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
```
