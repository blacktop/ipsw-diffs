## SoftwareUpdateUIService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
 		(require-not (global-name "com.apple.Safari.SafeBrowsing.Service"))
+		(require-not (global-name "com.apple.ScreenTimeAgent"))
 		(require-not (global-name "com.apple.hangtelemetryd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.accessibility.gax.backboard"))

 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (local-name "com.apple.iphone.axserver"))
+		(require-not (local-name "com.apple.accessibility.gax.client"))
 		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))

 				io_service_get_matching_service_bin
 				io_service_get_matching_services_bin
 				io_service_add_notification_bin_64
+				io_registry_entry_get_properties_bin_buf
 				io_registry_entry_get_property_bin_buf
 				mach_port_get_refs
 				mach_port_request_notification
```
