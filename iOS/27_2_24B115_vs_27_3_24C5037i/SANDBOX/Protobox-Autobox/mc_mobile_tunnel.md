## mc_mobile_tunnel

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "AGXCommandQueue")
 		(iokit-registry-entry-class "AGXDevice")
 		(iokit-registry-entry-class "AGXSharedUserClient")
+		(iokit-registry-entry-class "AppleCredentialManagerUserClient")
 		(iokit-registry-entry-class "AppleJPEGDriverUserClient")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(iokit-registry-entry-class "IOGPUDeviceUserClient")

 (allow iokit-open-service
 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
+		(iokit-registry-entry-class "AppleCredentialManager")
 		(iokit-registry-entry-class "AppleJPEGDriver")
 		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
+		(iokit-registry-entry-class "AppleM2ScalerParavirtDriver")
+		(iokit-registry-entry-class "AppleParavirtGPU")
+		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationDriver")
 		(iokit-registry-entry-class "IOSurfaceRoot")
 	)
 )

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 5))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(with-filter (mac-policy-name "vnguard")
+	(deny system-mac-syscall
+		(require-not (mac-syscall-number 1))
 	)
 )
 (deny system-mac-syscall
```
