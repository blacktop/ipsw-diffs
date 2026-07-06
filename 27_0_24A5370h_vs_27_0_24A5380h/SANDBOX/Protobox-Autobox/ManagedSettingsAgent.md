## ManagedSettingsAgent

> Group: ⬆️ Updated

```diff

 
 (deny mach-lookup
 	(require-all
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.deviceconfigurationd.provider"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.pluginkit.pkd"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.nanoprefsync"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
-		(require-not (global-name "com.apple.debug.telemetry"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.pluginkit.pkd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.erm.logging"))
-		(require-not (global-name "com.apple.duetactivityscheduler"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.datamigrator"))
-		(require-not (global-name "com.apple.frontboard.systemappservices"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.deviceconfigurationd.provider"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.MSTestApplication.MSTestExtension")
 			(xpc-service-name "com.apple.MSTestApplication.MSTestShieldConfigurationExtension")
 		))
-		(require-not (xpc-service-name "com.apple.datamigrator"))
 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")

 			(require-all
 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
+				(require-not (xpc-service-name "com.apple.datamigrator"))
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
 				(require-not (global-name "com.apple.FileCoordination"))
 				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))

 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
+			(require-not (mac-syscall-number 80))
 			(require-not (mac-syscall-number 7))
 			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 4))
```
