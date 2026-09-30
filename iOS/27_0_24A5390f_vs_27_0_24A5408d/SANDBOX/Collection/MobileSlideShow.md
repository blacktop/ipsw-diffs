## MobileSlideShow

> Group: ⬆️ Updated

```diff

 			(require-all
 				(global-name "com.apple.MusicKit.UI")
 				(require-any
+					(%entitlement-is-bool-true "com.apple.storekit.cloud-service-exempted-from-tcc-access")
 					(extension "com.apple.tcc.kTCCServiceMediaLibrary")
 					(xpc-service-name "com.apple.WebKit.*")
 				)

 			(require-all
 				(global-name "com.apple.MusicKit.UI")
 				(require-any
+					(%entitlement-is-bool-true "com.apple.storekit.cloud-service-exempted-from-tcc-access")
 					(extension "com.apple.tcc.kTCCServiceMediaLibrary")
 					(xpc-service-name "com.apple.WebKit.*")
 				)

 			(require-all
 				(global-name "com.apple.MusicKit.UI")
 				(require-any
+					(%entitlement-is-bool-true "com.apple.storekit.cloud-service-exempted-from-tcc-access")
 					(extension "com.apple.tcc.kTCCServiceMediaLibrary")
 					(xpc-service-name "com.apple.WebKit.*")
 				)
```
