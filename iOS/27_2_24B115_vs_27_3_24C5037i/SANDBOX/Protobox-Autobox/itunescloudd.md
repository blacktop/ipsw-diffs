## itunescloudd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.Carousel.authAlertXPCService"))
+		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.adid.xpc"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc"))

 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.linkd.autoShortcut"))
 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
 		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.springboard.services"))

 		(require-not (global-name "com.apple.SystemConfiguration.helper"))
 		(require-not (global-name "com.apple.cache_delete"))
 		(require-not (global-name "com.apple.homed.xpc"))
+		(require-not (global-name "com.apple.CoreAuthentication.daemon.libxpc"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.adid"))

 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.medialibraryd.xpc"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
+		(require-not (global-name "com.apple.linkd.application-service"))
 		(require-not (global-name "com.apple.servicesanalytics.xpc"))
 		(require-not (global-name "com.apple.fairplaydeviceidentityd"))
 		(require-not (global-name "com.apple.gpumemd.source"))

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 5))
+			(require-not (mac-syscall-number 4))
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
