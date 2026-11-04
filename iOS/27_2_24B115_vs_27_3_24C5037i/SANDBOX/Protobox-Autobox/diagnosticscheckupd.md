## diagnosticscheckupd

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.HomePodDisplayService.xpc"))
 		(require-not (global-name "com.apple.bluetooth.xpc"))
 		(require-not (global-name "com.apple.corerepair"))

 			SYS_psynch_rw_rdlock
 			SYS_psynch_rw_unlock
 			SYS_psynch_cvclrprepost
+			SYS_iopolicysys
 			SYS_issetugid
 			SYS___pthread_kill
 			SYS___sigwait
```
