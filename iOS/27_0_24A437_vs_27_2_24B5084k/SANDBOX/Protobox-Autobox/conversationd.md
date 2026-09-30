## conversationd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.generativeexperiences.agentSessionStore"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
-		(require-not (require-any
-			(global-name "com.apple.EligibilityQuorum.com.apple.AudioIntelligence")
-			(global-name "com.apple.deviceconfigurationd.consumer")
-		))
+		(require-not (global-name "com.apple.deviceconfigurationd.consumer"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.coreduetd.context"))
 		(require-not (global-name "com.apple.terminusd"))
 		(require-not (global-name "com.apple.audio.AudioQueueServer"))
-		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
+		(require-not (global-name "com.apple.EligibilityQuorum.com.apple.AudioIntelligence"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.securepairingd"))

 		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
 		(require-not (xpc-service-name "com.apple.speech.localspeechrecognition"))
+		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.Carousel.contextuallock"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
```
