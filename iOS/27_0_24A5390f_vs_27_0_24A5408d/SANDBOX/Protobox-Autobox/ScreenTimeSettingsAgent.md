## ScreenTimeSettingsAgent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.ScreenTimeAgent.persistence"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.ScreenTimeSettingsAgent.private"))

 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.asktod"))
 		(require-not (global-name "com.apple.DeviceConfigurationAgent.provider"))
+		(require-not (global-name "com.apple.contactsd"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
 		(require-not (xpc-service-name "com.apple.imdpersistence.IMDPersistenceAgent"))
 		(require-not (xpc-service-name "com.apple.ctcategories.service"))

 (allow socket-ioctl
 	(ioctl-command
 		CTLIOCGINFO
+		SIOCGCONNINFO
 		SIOCGIFCONSTRAINED
 		SIOCGIFDELEGATE
 		SIOCGIFEXPENSIVE

 		SYS_recvmsg
 		SYS_sendmsg
 		SYS_recvfrom
+		SYS_getsockname
 		SYS_access
 		SYS_crossarch_trap
 		SYS_dup

 		SYS_munmap
 		SYS_mprotect
 		SYS_madvise
+		SYS_dup2
 		SYS_fcntl
 		SYS_select
 		SYS_fsync
```
