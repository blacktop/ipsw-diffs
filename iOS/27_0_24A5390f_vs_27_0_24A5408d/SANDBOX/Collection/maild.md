## maild

> Group: ⬆️ Updated

```diff

 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.MusicKit.UI")
-		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.storekit.cloud-service-exempted-from-tcc-access")
+			(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+		)
 	)
 )
 (allow mach-lookup

 		(%entitlement-is-present "com.apple.developer.appmanagedfeatures")
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.merchantd.engagement")
+		(%entitlement-is-present "com.apple.developer.proximity-reader.customer-engagement")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.merchantd.discovery")

 		)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.merchantd.engagement")
-		(%entitlement-is-present "com.apple.developer.proximity-reader.customer-engagement")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.merchantd.storage")
```
