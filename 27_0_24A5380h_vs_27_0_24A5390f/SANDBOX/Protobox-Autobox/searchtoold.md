## searchtoold

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
 		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "AppleVirtIONeuralEngineDevice")

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
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
 	)
 )
 
-(deny ipc-posix-shm-write-data)
-(allow ipc-posix-shm-write-data
+(deny ipc-posix-shm-write-create)
+(allow ipc-posix-shm-write-create
 	(ipc-posix-name "apple.cfprefs.user.daemonv1")
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

 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.Maps.xpc.connectionBroker.endpointRecorder"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
+		(require-not (global-name "com.apple.healthd.server"))
 		(require-not (global-name "com.apple.biome.access.system"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
+		(require-not (global-name "com.apple.appprotectiond.guard"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.mobilemail.services.xpc"))

 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (global-name "com.apple.spotlight.SearchAgent"))
 		(require-not (global-name "com.apple.contactsd"))
+		(require-not (global-name "com.apple.generativelearning.server.memory"))
 		(require-not (global-name "com.apple.calaccessd"))
 		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))

 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.WorkflowKit.BackgroundShortcutRunner"))
 		(require-not (xpc-service-name "com.apple.imdpersistence.IMDPersistenceAgent"))
+		(require-not (xpc-service-name "com.apple.FileBrowsingServices.PathResolver"))
 		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.CARenderServer"))

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
