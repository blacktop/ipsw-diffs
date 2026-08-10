## SPIHelper-iOS

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "AppleJPEGDriver")
 		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
+		(iokit-registry-entry-class "AppleM2ScalerParavirtDriver")
+		(iokit-registry-entry-class "AppleParavirtGPU")
 		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationDriver")
 		(iokit-registry-entry-class "IOSurfaceRoot")
 	)

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.dnssd.service"))
-		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.gpumemd.source"))

 		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (global-name "com.apple.quicklook.ThumbnailsAgent"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.ExternalAccessory.distributednotification.server"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))

 				thread_suspend
 				thread_resume
 				thread_info
+				thread_policy_set
 				vm_remap_external
 				vm_reallocate
 				mach_vm_copy
```
