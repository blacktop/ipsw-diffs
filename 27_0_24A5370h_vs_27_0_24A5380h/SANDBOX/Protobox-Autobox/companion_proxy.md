## companion_proxy

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.nanosystemsettings"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.mobile.heartbeat"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.trustd"))
-		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
-		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.mobile.heartbeat"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.nanosystemsettings"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (system-attribute developer-mode))
 	)

 		mach_exception_raise_state
 		mach_exception_raise_state_identity
 		io_registry_entry_from_path
+		io_service_close
 		io_service_open_extended
+		io_connect_method
+		io_service_get_matching_service
 		io_server_version
 		io_service_get_matching_service_bin
 		io_registry_entry_get_property_bin_buf
```
