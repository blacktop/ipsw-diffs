## speechmaintenanced

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (global-name "com.apple.siri.location"))
-		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.familycircle.agent"))
-		(require-not (global-name "com.apple.siri.analytics.assistant"))
-		(require-not (global-name "com.apple.speechmaintenanced"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
-		(require-not (global-name "com.apple.intelligenceplatform.View"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.assistant.settings"))
+		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.modelcatalog.catalog"))
-		(require-not (global-name "com.apple.linkd.registry"))
+		(require-not (global-name "com.apple.intelligenceplatform.View"))
+		(require-not (global-name "com.apple.speechmaintenanced"))
+		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.siri.analytics.assistant"))
+		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (xpc-service-name "com.apple.speech.localspeechrecognition"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (system-attribute developer-mode))
```
