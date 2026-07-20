## thermalmonitord

> Group: ⬆️ Updated

```diff

 
 (deny generic-issue-extension)
 
-(deny iokit-issue-extension)
+(deny iokit-get-properties)
 
-(deny iokit-open-user-client)
-(allow iokit-open-user-client
+(deny iokit-open*)
+(allow iokit-open*
 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")

 	)
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "AppleCLPC")
 		(iokit-registry-entry-class "ApplePPMCPMS")

 	)
 )
 
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-all
 		(iokit-property "AppleChargeRateLimitIndex")
 		(require-not (iokit-registry-entry-class "AppleSmartBattery"))
 		(require-not (iokit-registry-entry-class "AppleARMPMUCharger"))
 	)
 )
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-all
 		(iokit-property "CPUPowerTarget")
 		(require-not (iokit-registry-entry-class "AppleT8010CLPC"))
 		(require-not (iokit-registry-entry-class "AppleS8000CLPC"))
 	)
 )
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-all
 		(require-any
 			(iokit-property "AppleARMPerformanceControllerDVDFactor1-hip")

 		(require-not (iokit-registry-entry-class "AppleT8011PMGR"))
 	)
 )
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-all
 		(require-any
 			(iokit-property "BaselineSystemCapability")

 		(require-not (iokit-registry-entry-class "AppleT8020PPM"))
 	)
 )
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-all
 		(iokit-property "LifetimeServoDieTemperatureTargetPropertyKey")
 		(require-not (iokit-registry-entry-class "ApplePMP"))
 		(require-not (iokit-registry-entry-class "AppleDieTempController"))
 	)
 )
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-all
 		(iokit-property "ApplePreUVLOIndex")
 		(require-not (iokit-registry-entry-class "AppleDialogPMU"))
 	)
 )
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-all
 		(require-any
 			(iokit-property "CameraStrobeMaxLoad")

 		(require-not (iokit-registry-entry-class "AppleDieTempController"))
 	)
 )
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-all
 		(require-any
 			(iokit-property "`cpu-avg-limiter-input-w2r")

 		(require-not (iokit-registry-entry-class "AppleCLPC"))
 	)
 )
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-any
 		(require-not (iokit-registry-entry-class "AGXAccelerator"))
 		(require-not (require-any

 	)
 )
 
+(deny iokit-set-properties)
+
 (deny ipc*)
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
 	)
 )
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))

 	)
 )
 
+(deny process-codesigning
+	(require-all
+		(require-not (literal "/usr/bin/killall"))
+		(require-not (literal "/bin/bash"))
+	)
+)
+(deny process-codesigning
+	(require-all
+		(literal "/usr/local/bin/smcif")
+		(require-not (system-attribute internal-build))
+	)
+)
+
 (deny process-exec*
 	(require-all
 		(require-not (literal "/usr/bin/killall"))
```
