## com.apple.siri.embeddedspeech

> Group: ⬆️ Updated

```diff

 
 (deny process-exec*)
 (allow process-exec*
-	(literal "/bin/sh")
+	(require-any
+		(literal "/bin/sh")
+		(literal "/usr/bin/atos")
+	)
 )
 
 (deny socket-ioctl)

 		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
 		io_service_add_notification_bin_64
+		io_registry_entry_get_properties_bin_buf
 		io_registry_entry_get_property_bin_buf
 		mach_port_deallocate
 		mach_port_get_refs

 
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
