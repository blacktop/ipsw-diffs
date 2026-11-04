## spotlightknowledged.updater

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.cascade.donationrequest.SensedUserContext.Place")
 			(global-name "com.apple.cascade.donationrequest.Siri.Transcript.Turn")
 		))
-		(require-not (global-name "com.apple.corepersonalization.server.graphEmbedding"))
+		(require-not (require-any
+			(global-name "com.apple.corepersonalization.server.graphEmbedding")
+			(global-name "com.apple.spotlight.IndexAgent.test")
+		))
 		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))

 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.FileDerivativeService"))
+		(require-not (global-name "com.apple.spotlight.SearchAgent.test"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.corespotlight.scheduled.receiver.textunderstandingd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 80))
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(with-filter (mac-policy-name "vnguard")
+	(deny system-mac-syscall
+		(require-not (mac-syscall-number 1))
 	)
 )
 (deny system-mac-syscall
```
