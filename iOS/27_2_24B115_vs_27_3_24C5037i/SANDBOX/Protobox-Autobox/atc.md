## atc

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "AppleJPEGDriverUserClient")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationUserClient")
+		(iokit-registry-entry-class "IOHIDLibUserClient")
 		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 		(iokit-registry-entry-class "IOSurfaceAcceleratorParavirtClient")
 		(iokit-registry-entry-class "IOSurfaceRootUserClient")

 		io_registry_entry_create_iterator
 		io_iterator_is_valid
 		io_service_open_extended
+		io_connect_map_memory_into_task
 		io_connect_method
 		io_connect_async_method
 		io_connect_set_notification_port_64

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 6 7))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 12))
+			(require-not (mac-syscall-number 67))
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
