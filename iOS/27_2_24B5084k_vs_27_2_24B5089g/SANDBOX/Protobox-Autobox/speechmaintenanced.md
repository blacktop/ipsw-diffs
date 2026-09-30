## speechmaintenanced

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.modelcatalog.catalog"))
 		(require-not (global-name "com.apple.intelligenceplatform.View"))
+		(require-not (global-name "com.apple.coreduetd.people"))
 		(require-not (global-name "com.apple.speechmaintenanced"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.siri.analytics.assistant"))
 		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (xpc-service-name "com.apple.speech.localspeechrecognition"))
+		(require-not (xpc-service-name "com.apple.siri.embeddedspeech"))
+		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (system-attribute developer-mode))
 	)
```
