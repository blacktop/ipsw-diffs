## speechmaintenanced

> Group: ⬆️ Updated

```diff

 		(require-not (xpc-service-name "com.apple.speech.localspeechrecognition"))
 		(require-not (xpc-service-name "com.apple.siri.embeddedspeech"))
 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (xpc-service-name "com.apple.siri.embeddedspeech.speechmaintenanced"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (system-attribute developer-mode))
 	)
```
