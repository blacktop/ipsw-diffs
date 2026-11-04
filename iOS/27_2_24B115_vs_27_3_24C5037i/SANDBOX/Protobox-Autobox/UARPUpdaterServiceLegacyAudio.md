## UARPUpdaterServiceLegacyAudio

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.ExternalAccessory.distributednotification.server"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "h.1"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (require-any
 			(global-name "com.apple.iap2d.ExternalAccessory.distributednotification.server")

 		SYS_psynch_rw_unlock
 		SYS_psynch_rw_unlock2
 		SYS_psynch_cvclrprepost
+		SYS_iopolicysys
 		SYS_issetugid
 		SYS___pthread_kill
 		SYS___pthread_sigmask

 
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
