## SiriHeadlessService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.coreduetd.knowledge"))
 		(require-not (global-name "com.apple.assistantd.odeon-remote"))
-		(require-not (require-any
-			(global-name "com.apple.assistant.device-context")
-			(global-name "com.apple.siri.attendingstates.xpc")
-		))
+		(require-not (global-name "com.apple.siri.attendingstates.xpc"))
 		(require-not (global-name "com.apple.siri.audiopowerupdate.xpc"))
 		(require-not (global-name "com.apple.wifi.manager"))
 		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
-		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
+		(require-not (global-name "com.apple.assistant.device-context"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
 		(require-not (global-name "com.apple.homed.xpc"))
 		(require-not (global-name "com.apple.siri.uaf.service"))
+		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
+		(require-not (global-name "com.apple.intelligenceflow.activation.prewarm"))
 		(require-not (global-name "com.apple.SiriVOXService.client"))
 		(require-not (system-attribute developer-mode))
 	)

 		SYS_kdebug_trace_string
 		SYS_kdebug_trace64
 		SYS_kdebug_trace
+		SYS_seteuid
 		SYS_sigreturn
 		SYS_pathconf
 		SYS_getrlimit

 		F_GETFL
 		F_GETPATH
 		F_OFD_SETLK
+		F_OFD_GETLK
 		F_SETCONFINED
 		F_GETCONFINED
 		F_ADDFILESIGS_RETURN
```
