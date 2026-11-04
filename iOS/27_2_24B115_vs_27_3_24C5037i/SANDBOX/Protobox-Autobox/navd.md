## navd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.lsd.icons"))
+		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.Maps.MapsSync.store"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))

 		(require-not (global-name "com.apple.Maps.xpc.connectionBroker.endpointRecorder"))
 		(require-not (global-name "com.apple.systemstatus"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
+		(require-not (global-name "com.apple.AudioAccessoryServices"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.geoanalyticsd"))
 		(require-not (global-name "com.apple.NetworkLinkConditioner"))
 		(require-not (global-name "com.apple.appprotectiond.guard"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.relatived.status"))

 		(require-not (global-name "com.apple.carkit.app.service"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.linkd.autoShortcut"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
 		(require-not (global-name "com.apple.relatived.public"))

 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.audio.AudioQueueServer"))
 		(require-not (global-name "com.apple.maps.destinationd.sources"))
+		(require-not (global-name "com.apple.linkd.application-service"))
 		(require-not (global-name "com.apple.passd.library"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.gpumemd.source"))

 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
-				(require-not (global-name "com.apple.CARenderServer"))
-				(require-not (global-name "com.apple.AudioAccessoryServices"))
+				(require-not (require-any
+					(global-name "P.-")
+					(global-name "P.S")
+				))
+				(require-not (global-name "P.o"))
 				(require-not (system-attribute developer-mode))
 			)
 			(require-all
 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
-				(require-not (global-name "com.apple.CARenderServer"))
-				(require-not (global-name "com.apple.AudioAccessoryServices"))
+				(require-not (require-any
+					(global-name "P.-")
+					(global-name "P.S")
+				))
+				(require-not (global-name "P.o"))
 				(require-not (system-attribute developer-mode))
 			)
 		)

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 5))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(with-filter (mac-policy-name "vnguard")
+	(deny system-mac-syscall
+		(require-not (mac-syscall-number 1))
 	)
 )
 (deny system-mac-syscall
```
