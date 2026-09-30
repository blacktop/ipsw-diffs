## homed

> Group: ⬆️ Updated

```diff

 	)
 )
 
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
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleJPEGDriver")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.daemonv1")
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")

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
 		(require-not (global-name "com.apple.biome.access.user"))

 		(require-not (require-any
 			(global-name "com.apple.coordination.state")
 			(global-name "com.apple.dropin.xpc")
+			(global-name "com.apple.homecommsd.distributed")
 			(global-name "com.apple.homecommsd.xpc")
 			(global-name "com.apple.homepodsensed")
 			(global-name "com.apple.identityservicesd.xpc")

 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.nanoprefsync"))
 		(require-not (global-name "com.apple.tvosupdate"))
+		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
 		(require-not (global-name "com.apple.appprotectiond.guard"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (xpc-service-name "com.apple.CloudTelemetryService.xpc"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.relevanced.AssertionService"))
 		(require-not (global-name "com.apple.homekitevents.xpc"))

 		(require-not (global-name "com.apple.securityd.general"))
 		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.apsd"))
-		(require-not (xpc-service-name "com.apple.CloudTelemetryService.xpc"))
+		(require-not (xpc-service-name "com.apple.ProductKitService"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.chrono.widgetcenterconnection"))

 		))
 		(require-not (global-name "com.apple.assistant.security"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
-		(require-not (xpc-service-name "com.apple.ProductKitService"))
+		(require-not (xpc-service-name "com.apple.itunescloud.music-subscription-status-service"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))
 		(require-not (global-name "com.apple.aa.daemon.xpc"))
 		(require-not (global-name "com.apple.carkit.app.service"))

 		(require-not (global-name "com.apple.corespeech.corespeechservices"))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
-		(require-not (xpc-service-name "com.apple.itunescloud.music-subscription-status-service"))
+		(require-not (xpc-service-name "com.apple.EnergyKitService"))
 		(require-not (global-name "com.apple.photoanalysisd"))
 		(require-not (global-name "com.apple.securityd.ckks"))
 		(require-not (xpc-service-name "com.apple.intents.intents-helper"))

 		(require-not (global-name "com.apple.seserviced"))
 		(require-not (global-name "com.apple.groupkitd.xpc.groupservice"))
 		(require-not (global-name "com.apple.corefollowup.agent"))
-		(require-not (xpc-service-name "com.apple.EnergyKitService"))
+		(require-not (xpc-service-name "com.apple.WorkflowKit.BackgroundShortcutRunner"))
 		(require-not (global-name "com.apple.mediaanalysisd.homekitsession"))
 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
 		(require-not (global-name "com.apple.SecureBackupDaemon"))
 		(require-not (xpc-service-name "com.apple.StreamingUnzipService"))
 		(require-not (global-name "com.apple.StatusKit.presence"))
 		(require-not (global-name "com.apple.NPKNanoPassDaemonConnection.XPC"))
-		(require-not (xpc-service-name "com.apple.WorkflowKit.BackgroundShortcutRunner"))
+		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
 		(require-not (global-name "com.apple.cloudtelemetryd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command
```
