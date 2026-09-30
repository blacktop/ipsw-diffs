## OTACrashCopier

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.cfnetwork.AuthBrokerAgent"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.nehelper"))

 		SYS_recvfrom
 		SYS_access
 		SYS_fchflags
+		SYS_kill
 		SYS_crossarch_trap
 		SYS_dup
 		SYS_getegid
```
