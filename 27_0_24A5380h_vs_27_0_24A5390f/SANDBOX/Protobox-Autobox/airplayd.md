## airplayd

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
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleAVE2Driver")

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
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
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
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.figcpecryptor.xpc"))

 		(require-not (require-any
 			(global-name "com.apple.airplay.agent.services")
 			(global-name "com.apple.airplay.receiver.contra-services")
+			(global-name "com.apple.airplay.videoplayback")
 			(global-name "com.apple.coremedia.mediaplaybackd.audiodeviceclock.xpc")
 			(global-name "com.apple.mediaexperience.carplaymodecontroller.xpc")
 		))

 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
 		(require-not (global-name "com.apple.FileCoordination"))
-		(require-not (global-name "com.apple.airplay.receiver.services"))
 		(require-not (xpc-service-name "com.apple.corespeech.xpc"))
+		(require-not (global-name "com.apple.airplay.receiver.services"))
+		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
 		(require-not (global-name "com.apple.lskdd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.adid"))

 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
-		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.wifip2pd"))
 		(require-not (global-name "com.apple.timesync.expositor"))
 		(require-not (global-name "com.apple.xpc.amstoold"))
-		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.PairingManager"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))

 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
-		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.CarPlayApp.service"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))
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

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
