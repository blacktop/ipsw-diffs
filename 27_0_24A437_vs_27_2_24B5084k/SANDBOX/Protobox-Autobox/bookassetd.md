## bookassetd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.cfnetwork.AuthBrokerAgent"))
 		(require-not (global-name "com.apple.biometrickitd"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.nsurlsessiond"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))

 		SIOCGIFFUNCTIONALTYPE
 		SIOCGIFLINKQUALITYMETRIC
 		SIOCGIFMTU
-		SIOCGIFULTRACONSTRAINED)
+		SIOCGIFULTRACONSTRAINED
+		TIOCGETA)
 )
 
 (deny syscall-unix)

 		SYS_recvmsg
 		SYS_sendmsg
 		SYS_recvfrom
+		SYS_getsockname
 		SYS_access
 		SYS_crossarch_trap
 		SYS_dup
```
