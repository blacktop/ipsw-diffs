## newsd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.adid.xpc"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (require-any
 			(global-name "com.apple.coremedia.mediaplaybackd.figcontentkeyboss.xpc")
 			(global-name "com.apple.coremedia.mediaplaybackd.figcontentkeysession.xpc")

 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.cfnetwork.AuthBrokerAgent"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.nsurlsessiond"))
 		(require-not (global-name "com.apple.coremedia.figcontentkeysession.xpc"))

 		SYS_recvmsg
 		SYS_sendmsg
 		SYS_recvfrom
+		SYS_getsockname
 		SYS_access
 		SYS_kill
 		SYS_crossarch_trap
```
