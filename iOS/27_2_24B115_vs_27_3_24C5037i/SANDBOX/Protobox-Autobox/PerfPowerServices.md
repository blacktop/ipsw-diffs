## PerfPowerServices

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
+		(require-not (require-any
+			(global-name "P.-")
+			(global-name "P.S")
+		))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.batteryintelligenced.chargetimeestimator"))

 		(require-not (global-name "com.apple.ExposureNotification"))
 		(require-not (global-name "com.apple.centaurid.xpc"))
 		(require-not (global-name "com.apple.trial.status"))
+		(require-not (xpc-service-name "com.apple.PerfPowerServicesSignpostReader"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.ind.cloudfeatures"))

 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.wifip2pd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "P.o"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.xpc.amsaccountsd"))

 			(xpc-service-name "com.apple.PPSRelay")
 			(xpc-service-name "com.apple.PerfPowerServicesSignpostService")
 		))
-		(require-not (xpc-service-name "com.apple.PerfPowerServicesSignpostReader"))
-		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		SYS_kdebug_trace
 		SYS_seteuid
 		SYS_sigreturn
+		SYS_thread_selfcounts
 		SYS_stat
 		SYS_fstat
 		SYS_lstat

 
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
