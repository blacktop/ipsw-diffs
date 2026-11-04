## audioanalyticsd

> Group: ⬆️ Updated

```diff

 	(require-any
 		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "AppleProcessorTraceNub")
+		(iokit-registry-entry-class "AppleSPUGestureDriver")
 		(iokit-registry-entry-class "IOHIDUserDevice")
 		(iokit-registry-entry-class "IOReportHub")
 	)

 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.carousel.backlightxpc"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.diagnosticpipeline.service"))
 		(require-not (global-name "com.apple.logd.events"))

 
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
