## diagnosticextensionsd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.enhancedloggingd.xpc"))
 		(require-not (global-name "com.apple.PineBoardServices"))
 		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))

 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
+				(require-not (global-name "com.apple.FileCoordination"))
 				(require-not (global-name "com.apple.CARenderServer"))
 				(require-not (system-attribute developer-mode))
 			)

 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
+				(require-not (global-name "com.apple.FileCoordination"))
 				(require-not (global-name "com.apple.CARenderServer"))
 				(require-not (system-attribute developer-mode))
 			)

 
 (deny system-kas-info)
 
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
 			(require-not (mac-syscall-number 80))
-			(require-not (mac-syscall-number 7))
-			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 6 7))
 			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 12))
 			(require-not (mac-syscall-number 67))
 			(require-not (mac-syscall-number 2))
 		)
```
