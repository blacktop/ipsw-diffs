## companioncamerad

> Group: ⬆️ Updated

```diff

 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
+		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 	)
 )
 

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.nanoprefsync"))
-		(require-not (global-name "com.apple.audio.AudioSession"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.springboard.services"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
-		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
-		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.springboard.services"))
+		(require-not (global-name "com.apple.audio.AudioSession"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (system-attribute developer-mode))
 	)

 		mach_exception_raise_state
 		mach_exception_raise_state_identity
 		io_registry_entry_from_path
+		io_service_close
 		io_service_open_extended
+		io_connect_method
 		io_server_version
 		io_service_get_matching_service_bin
 		io_registry_entry_get_property_bin_buf
```
