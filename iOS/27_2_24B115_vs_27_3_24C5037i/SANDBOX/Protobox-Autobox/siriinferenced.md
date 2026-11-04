## siriinferenced

> Group: ⬆️ Updated

```diff

 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
+		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 		(iokit-registry-entry-class "RootDomainUserClient")
 	)
 )

 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.linkd.transcript"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
-		(require-not (require-any
-			(global-name "com.apple.findmy.findmylocate.friendshipservice")
-			(global-name "com.apple.findmy.findmylocate.settings")
-		))
+		(require-not (global-name "com.apple.findmy.findmylocate.friendshipservice"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.backlightd"))
 		(require-not (global-name "com.apple.uservault"))

 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.modelmanager"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.linkd.autoShortcut"))
 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
 		(require-not (global-name "com.apple.springboard.backgroundappservices"))
 		(require-not (global-name "com.apple.fontservicesd"))

 		(require-not (global-name "com.apple.mediaremoted.xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.siri.VoiceShortcuts.xpc"))
-		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
+		(require-not (global-name "com.apple.findmy.findmylocate.settings"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
 		(require-not (global-name "com.apple.FileCoordination"))
+		(require-not (global-name "com.apple.generativeexperiences.agentSessionStore"))
 		(require-not (global-name "com.apple.homed.xpc"))
 		(require-not (global-name "com.apple.siri.uaf.service"))
 		(require-not (global-name "com.apple.Maps.xpc.SharedTrip"))
 		(require-not (global-name "com.apple.imagent.embedded.auth"))
 		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.linkd.application-service"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
 		(require-not (global-name "com.apple.logd.events"))

 			(xpc-service-name "com.apple.SiriTasksEvaluation.SiriTasksEvaluationPlugin")
 			(xpc-service-name "com.apple.siri.SuggestionsBookkeepingService")
 		))
-		(require-not (xpc-service-name "com.apple.ctcategories.service"))
+		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (xpc-service-name "com.apple.extensionkitservice"))
 		(require-not (xpc-service-name "com.apple.datamigrator"))
 		(require-not (xpc-service-name "com.apple.itunescloud.music-subscription-status-service"))
+		(require-not (xpc-service-name "com.apple.ctcategories.service"))
 		(require-not (global-name "com.apple.CallHistorySyncHelper"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.ABDatabaseDoctor"))

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
-	)
-)
-(deny system-mac-syscall
-	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
-	)
-)
+(deny system-mac-syscall)
 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
```
