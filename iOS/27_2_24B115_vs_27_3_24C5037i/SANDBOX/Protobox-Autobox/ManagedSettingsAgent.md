## ManagedSettingsAgent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.deviceconfigurationd.consumer"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))

 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
-				(require-not (global-name "com.apple.FileCoordination"))
 				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
+				(require-not (global-name "com.apple.DeviceConfigurationAgent.consumer"))
 				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 				(require-not (global-name "com.apple.CARenderServer"))
 				(require-not (system-attribute developer-mode))

 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (xpc-service-name "com.apple.datamigrator"))
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
-				(require-not (global-name "com.apple.FileCoordination"))
 				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
+				(require-not (global-name "com.apple.DeviceConfigurationAgent.consumer"))
 				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 				(require-not (global-name "com.apple.CARenderServer"))
 				(require-not (system-attribute developer-mode))

 		SYS___sigwait_nocancel
 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
+		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_guarded_close_np
 		SYS_proc_rlimit_control

 
 (deny system-kas-info)
 
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
```
