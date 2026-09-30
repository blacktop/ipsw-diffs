## ClarityBoard

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.CarPlayApp.non-launching-service"))
 		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
 		(require-not (global-name "com.apple.assistant.client"))
+		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.MobileTimer.timerserver"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc"))
 		(require-not (global-name "com.apple.fullkeyboardaccess"))

 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.conversationmanager"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.audioprocessingtap.xpc"))
 		(require-not (global-name "com.apple.iohideventsystem"))
+		(require-not (global-name "com.apple.AttentionAwareness"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.FileCoordination"))

 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
-				(require-not (global-name "com.apple.CARenderServer"))
-				(require-not (global-name "com.apple.AttentionAwareness"))
-				(require-not (global-name "com.apple.AppSSO.service-xpc"))
 				(require-not (global-name "com.apple.AccessibilityUIServer"))
+				(require-not (global-name "com.apple.AppSSO.service-xpc"))
+				(require-not (global-name "UIASTNotificationCenter"))
 				(require-not (global-name "PurplePPTServer"))
 				(require-not (system-attribute developer-mode))
 			)

 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
-				(require-not (global-name "com.apple.CARenderServer"))
-				(require-not (global-name "com.apple.AttentionAwareness"))
-				(require-not (global-name "com.apple.AppSSO.service-xpc"))
 				(require-not (global-name "com.apple.AccessibilityUIServer"))
+				(require-not (global-name "com.apple.AppSSO.service-xpc"))
+				(require-not (global-name "UIASTNotificationCenter"))
 				(require-not (global-name "PurplePPTServer"))
 				(require-not (system-attribute developer-mode))
 			)
```
