## axassetsd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (global-name "com.apple.PrototypeTools.domainserver"))

 		SYS_fsync
 		SYS_socket
 		SYS_connect
+		SYS_setsockopt
 		SYS_listen
 		SYS_sigsuspend
 		SYS_gettimeofday
```
