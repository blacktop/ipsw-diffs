## sirievaluationd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
+		(require-not (global-name "com.apple.linkd.autoShortcut"))
 		(require-not (global-name "com.apple.backboard.display.services"))
 		(require-not (global-name "com.apple.assistant.analytics-observation"))
 		(require-not (global-name "com.apple.logd.admin"))
+		(require-not (global-name "com.apple.siriactionsd.xpc"))
+		(require-not (global-name "com.apple.linkd.application-service"))
 		(require-not (global-name "com.apple.internal.xctestinternalangel.sessions"))
 		(require-not (global-name "com.apple.testmanagerd"))
 		(require-not (global-name "com.apple.assistant.analytics"))
+		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))
 	)
```
