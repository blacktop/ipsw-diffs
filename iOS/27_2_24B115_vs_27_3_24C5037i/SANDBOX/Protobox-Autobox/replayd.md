## replayd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
+		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (global-name "com.apple.systemstatus"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
 		(require-not (global-name "com.apple.lsd.mapdb"))

 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.coremedia.mediaparserd.mutablemovie.xpc"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.photos.service"))
 		(require-not (global-name "com.apple.controlcenter.remoteservice"))

 		io_registry_entry_from_path
 		io_registry_entry_get_name
 		io_registry_entry_get_property_bytes
+		io_registry_entry_get_child_iterator
 		io_registry_entry_get_parent_iterator
 		io_service_close
 		io_registry_entry_create_iterator

 
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
```
