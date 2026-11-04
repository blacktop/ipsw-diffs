## axassetsd

> Group: ⬆️ Updated

```diff

 		SYS_guarded_pwrite_np
 		SYS_guarded_writev_np
 		SYS_persona
+		SYS_mach_eventlink_signal
+		SYS_mach_eventlink_wait_until
 		SYS_mach_eventlink_signal_wait_until
 		SYS_getentropy
 		SYS_necp_open

 
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
