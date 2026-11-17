## assistant_service

> Group: ⬆️ Updated

```diff

 		(require-not (require-any
 			(global-name "com.apple.CascadeSetsDifferentialUpdateService")
 			(global-name "com.apple.TextUnderstanding.SmartReplies.Inference")
-			(global-name "com.apple.agentboardd.telemetry")
 			(global-name "com.apple.assistant.flow_service")
 			(global-name "com.apple.assistant.notification_service")
 			(global-name "com.apple.itunescloud.delegate-account-store")

 		(require-not (global-name "com.apple.bulletinboard.settingsconnection"))
 		(require-not (global-name "com.apple.assistant.multiuser.service"))
 		(require-not (global-name "com.apple.findmy.findmylocate.locationservice"))
+		(require-not (global-name "com.apple.agentboardd.telemetry"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
 		(require-not (global-name "com.apple.cfnetwork.AuthBrokerAgent"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationsettingsservice"))
```
