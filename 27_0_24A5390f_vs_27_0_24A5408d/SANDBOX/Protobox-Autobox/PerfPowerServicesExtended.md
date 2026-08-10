## PerfPowerServicesExtended

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "ApplePPMUserClient")
 		(iokit-registry-entry-class "AppleSMCClient")
 		(iokit-registry-entry-class "AppleSPUHIDDeviceUserClient")
+		(iokit-registry-entry-class "AppleSPUHIDDriverUserClient")
 		(iokit-registry-entry-class "AppleSPUUserClient")
 		(iokit-registry-entry-class "IOGPUMemoryInfoUserClient")
 		(iokit-registry-entry-class "IOHIDLibUserClient")

 		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.ExternalAccessory.distributednotification.server"))
+		(require-not (global-name "com.apple.CarPlayApp.non-launching-service"))
 		(require-not (global-name "com.apple.basebandd.xpc"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.icloud.searchpartyd.beaconmanager"))

 			(xpc-service-name "com.apple.PerfPowerServicesSignpostService")
 		))
 		(require-not (xpc-service-name "com.apple.PerfPowerServicesSignpostReader"))
-		(require-not (global-name "com.apple.CarPlayApp.non-launching-service"))
 		(require-not (global-name "com.apple.CARenderServer"))
+		(require-not (global-name "com.apple.AttentionAwareness"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		SYS_getattrlistbulk
 		SYS_clonefileat
 		SYS_openat
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
