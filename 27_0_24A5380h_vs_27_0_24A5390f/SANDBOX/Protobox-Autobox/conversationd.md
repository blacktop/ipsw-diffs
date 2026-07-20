## conversationd

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
 		(iokit-registry-entry-class "AppleKeyStore")

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

 		(require-not (global-name "com.apple.generativeexperiences.agentSessionStore"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
-		(require-not (global-name "com.apple.deviceconfigurationd.consumer"))
+		(require-not (require-any
+			(global-name "com.apple.EligibilityQuorum.com.apple.AudioIntelligence")
+			(global-name "com.apple.deviceconfigurationd.consumer")
+		))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.coreduetd.context"))
 		(require-not (global-name "com.apple.terminusd"))
 		(require-not (global-name "com.apple.audio.AudioQueueServer"))
+		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.securepairingd"))

 		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
 		(require-not (xpc-service-name "com.apple.speech.localspeechrecognition"))
-		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.Carousel.contextuallock"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))

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
