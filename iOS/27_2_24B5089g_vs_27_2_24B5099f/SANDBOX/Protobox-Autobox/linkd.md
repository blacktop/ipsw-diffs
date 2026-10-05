## linkd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.siri.VoiceShortcuts.xpc"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))

 		SYS_kdebug_trace
 		SYS_sigreturn
 		SYS_pathconf
+		SYS_fpathconf
 		SYS_getrlimit
 		SYS_setrlimit
 		SYS_mmap
```
