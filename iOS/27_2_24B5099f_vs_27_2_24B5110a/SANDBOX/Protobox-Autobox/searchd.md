## searchd

> Group: ⬆️ Updated

```diff

 		(require-not (require-any
 			(xpc-service-name "com.apple.OfficeImport.OfficeSpotlightImporter")
 			(xpc-service-name "com.apple.PassKit.PassKitSpotlightIndexExtension")
+			(xpc-service-name "com.apple.mobilenotes.SpotlightIndexExtension")
 			(xpc-service-name "com.apple.reminders.spotlightindexextension")
 		))
 		(require-not (xpc-service-name "com.apple.ctcategories.service"))
```
