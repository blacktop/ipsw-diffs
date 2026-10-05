## ManagedSettingsAgent

> Group: ⬆️ Updated

```diff

 
 (deny ipc*)
 
+(deny ipc-posix-shm-read-data)
+(allow ipc-posix-shm-read-data
+	(ipc-posix-name "apple.shm.notification_center")
+)
+
 (deny job-creation)
 
 (deny mach-issue-extension)

 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.nanoprefsync"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.diagnosticd"))

 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.deviceconfigurationd.consumer"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.datamigrator"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.deviceconfigurationd.provider"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.MSTestApplication.MSTestExtension")
```
