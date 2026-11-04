## chronod

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.lsd.xpc"))
 		(require-not (global-name "com.apple.apsd"))
-		(require-not (global-name "com.apple.proactive.infoSuggestion.xpc"))
+		(require-not (require-any
+			(global-name "com.apple.localizationswitcherd")
+			(global-name "com.apple.proactive.infoSuggestion.xpc")
+		))
 		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
 		(require-not (global-name "com.apple.hangtelemetryd"))
 		(require-not (global-name "com.apple.watchnotificationsui.alertservice"))

 		(require-not (require-any
 			(global-name "com.apple.WatchGestures.WAGUIBSActionProxyMachServiceName")
 			(global-name "com.apple.carousel.duet_background_action_service")
-			(global-name "com.apple.localizationswitcherd")
 			(global-name "com.apple.shortcuts.systemshortcutservice")
 			(global-name "com.apple.siri.VoiceShortcuts.xpc;")
 		))

 		(require-not (global-name "com.apple.carkit.app.service"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.linkd.autoShortcut"))
 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
 		(require-not (global-name "com.apple.springboard.services"))
 		(require-not (global-name "com.apple.backboard.display.services"))
-		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (global-name "com.apple.uiintelligencesupport.agent"))
 		(require-not (global-name "com.apple.sessionservices"))
 		(require-not (global-name "com.apple.pasteboard.pasted"))

 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
-		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
+		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
 		(require-not (global-name "com.apple.breadboardservices"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))

 		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.hangtracermonitor"))
+		(require-not (global-name "com.apple.linkd.application-service"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.parsecd"))

 
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
