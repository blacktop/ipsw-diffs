## ReportCrashService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.translation.text"))
+		(require-not (global-name "com.apple.talon.browser"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))

 		SYS_dup2
 		SYS_fcntl
 		SYS_select
+		SYS_fsync
 		SYS_socket
 		SYS_connect
 		SYS_sigsuspend
```
