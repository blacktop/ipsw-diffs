## speechmaintenanced

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.assistant.settings"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.userprofiles"))
+		(require-not (global-name "com.apple.Carousel.contextuallock"))
+		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))
 		(require-not (global-name "com.apple.modelcatalog.catalog"))
 		(require-not (global-name "com.apple.intelligenceplatform.View"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.coreduetd.people"))
+		(require-not (global-name "com.apple.FileCoordination"))
+		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.speechmaintenanced"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.siri.analytics.assistant"))
+		(require-not (global-name "com.apple.backboard.hid.services"))
+		(require-not (global-name "com.apple.assistant.analytics"))
 		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (global-name "com.apple.contactsd"))
 		(require-not (xpc-service-name "com.apple.speech.localspeechrecognition"))
 		(require-not (xpc-service-name "com.apple.siri.embeddedspeech"))
 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
 		(require-not (xpc-service-name "com.apple.siri.embeddedspeech.speechmaintenanced"))
-		(require-not (global-name "com.apple.FileCoordination"))
-		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
+		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		semaphore_create
 		semaphore_destroy
 		task_set_exc_guard_behavior
+		task_create_identity_token
 		thread_terminate
 		thread_suspend
 		thread_resume
```
