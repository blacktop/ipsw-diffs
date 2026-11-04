## com.apple.photos.VideoConversionService

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "AGXSharedUserClient")
 		(iokit-registry-entry-class "AppleJPEGDriverUserClient")
 		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationUserClient")
+		(iokit-registry-entry-class "AppleVirtIONeuralEngineDeviceUserClient")
 		(iokit-registry-entry-class "H1xANELoadBalancerDirectPathClient")
 		(iokit-registry-entry-class "IOGPUDeviceUserClient")
 		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
+		(require-not (global-name "com.apple.coremedia.mediaplaybackd.bytestream.xpc"))
 		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))

 		SYS_psynch_rw_unlock2
 		SYS_psynch_cvclrprepost
 		SYS_iopolicysys
+		SYS_process_policy
 		SYS_issetugid
 		SYS___pthread_kill
 		SYS___pthread_sigmask

 
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
-			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 5))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 2))
```
