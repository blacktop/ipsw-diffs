## icloudwebd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.kvsd"))
 		(require-not (global-name "com.apple.assistant.cdm"))
 		(require-not (global-name "com.apple.bird"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
+		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.aa.daemon.xpc"))
 		(require-not (global-name "com.apple.intelligenceplatform.View"))

 			SYS_psynch_rw_unlock
 			SYS_psynch_rw_unlock2
 			SYS_psynch_cvclrprepost
+			SYS_iopolicysys
 			SYS_issetugid
 			SYS___pthread_kill
 			SYS___pthread_sigmask

 			SYS_pwrite_nocancel
 			SYS___sigwait_nocancel
 			SYS_fsgetpath
+			SYS_fileport_makefd
 			SYS_memorystatus_control
 			SYS_guarded_open_np
 			SYS_change_fdguard_np

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
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
