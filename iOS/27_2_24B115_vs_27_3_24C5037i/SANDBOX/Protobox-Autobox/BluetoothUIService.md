## BluetoothUIService

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "AppleEmbeddedNVMeController")
 		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "AppleUserHIDDevice")
+		(iokit-registry-entry-class "AppleVirtIONeuralEngineDevice")
 		(iokit-registry-entry-class "IOHIDUserDevice")
 		(iokit-registry-entry-class "IOSurfaceRoot")
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
