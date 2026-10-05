## assetsd

> Group: ⬆️ Updated

```diff

 (deny iokit-open-service)
 (allow iokit-open-service
 	(require-any
+		(iokit-registry-entry-class "AppleH16CamIn")
 		(iokit-registry-entry-class "AppleJPEGDriver")
 		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
 		(iokit-registry-entry-class "AppleM2ScalerParavirtDriver")
 		(iokit-registry-entry-class "AppleParavirtGPU")
 		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationDriver")
+		(iokit-registry-entry-class "AppleVirtIONeuralEngineDevice")
 		(iokit-registry-entry-class "H1xANELoadBalancer")
 		(iokit-registry-entry-class "IOSurfaceRoot")
 	)

 	(require-any
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
+		(ipc-posix-name "apple.shm.notification_center")
 	)
 )
 

 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.sessionservices"))
 		(require-not (global-name "com.apple.cache_delete.public"))
+		(require-not (global-name "com.apple.systemstatus.publisher"))
 		(require-not (global-name "com.apple.fontservicesd"))
 		(require-not (global-name "com.apple.coremedia.deferredmedia.photoprocessor"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.corespotlight.receiver.checkin"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.communication"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.photoanalysisd"))
 		(require-not (global-name "com.apple.coremedia.player.xpc"))
 		(require-not (global-name "com.apple.mediaanalysisd.embeddingstore"))

 		SYS_listxattr
 		SYS_flistxattr
 		SYS_fsctl
+		SYS_posix_spawn
 		SYS_ffsctl
 		SYS_shm_open
 		SYS_sysctlbyname
```
