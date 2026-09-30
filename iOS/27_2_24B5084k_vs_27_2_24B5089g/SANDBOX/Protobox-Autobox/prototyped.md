## prototyped

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "AppleParavirtGPU")
 		(iokit-registry-entry-class "AppleVirtIONeuralEngineDevice")
+		(iokit-registry-entry-class "IOPMrootDomain")
 		(iokit-registry-entry-class "IOSurfaceRoot")
 	)
 )

 		(require-not (global-name "com.apple.audioanalyticsd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
+		(require-not (global-name "com.apple.biometrickitd"))
 		(require-not (global-name "com.apple.muranod.listener"))
 		(require-not (global-name "com.apple.sharing.sharesheet"))
 		(require-not (require-any

 			io_connect_method
 			io_connect_async_method
 			io_connect_set_notification_port_64
+			io_service_add_interest_notification_64
 			io_registry_entry_get_registry_entry_id
 			io_server_version
 			io_service_get_matching_service_bin
```
