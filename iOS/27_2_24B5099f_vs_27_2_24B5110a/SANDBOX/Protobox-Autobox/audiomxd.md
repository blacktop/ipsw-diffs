## audiomxd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.rtcreportingd"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.soundanalysisd"))
 		(require-not (global-name "com.apple.backboardd.virtualframebuffer"))
 		(require-not (global-name "com.apple.WirelessCoexManager"))

 		SYS_munmap
 		SYS_mprotect
 		SYS_madvise
+		SYS_mincore
 		SYS_dup2
 		SYS_fcntl
 		SYS_select
```
