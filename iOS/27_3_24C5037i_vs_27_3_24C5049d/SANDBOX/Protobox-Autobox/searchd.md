## searchd

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.corespotlight.receiver.images")
 			(global-name "com.apple.corespotlight.receiver.textunderstandingd")
 		))
+		(require-not (global-name "com.apple.appprotectiond.guard"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.siri.context.service"))

 		(require-not (require-any
 			(xpc-service-name "com.apple.OfficeImport.OfficeSpotlightImporter")
 			(xpc-service-name "com.apple.PassKit.PassKitSpotlightIndexExtension")
+			(xpc-service-name "com.apple.Preferences.SettingsImportExtension")
 			(xpc-service-name "com.apple.mobilenotes.SpotlightIndexExtension")
 			(xpc-service-name "com.apple.reminders.spotlightindexextension")
 		))
```
