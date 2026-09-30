## quicklookd

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
```
