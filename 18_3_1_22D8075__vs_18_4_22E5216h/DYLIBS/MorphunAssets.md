## MorphunAssets

> `/System/Library/PrivateFrameworks/MorphunAssets.framework/MorphunAssets`

```diff

-3402.12.1.0.0
-  __TEXT.__text: 0x8f38
-  __TEXT.__auth_stubs: 0x420
+3404.47.1.0.0
+  __TEXT.__text: 0x8f6c
+  __TEXT.__auth_stubs: 0x430
   __TEXT.__objc_methlist: 0x418
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x7f8
   __TEXT.__cstring: 0xd0d
-  __TEXT.__oslogstring: 0xe15
-  __TEXT.__unwind_info: 0x2e8
+  __TEXT.__oslogstring: 0x1035
+  __TEXT.__unwind_info: 0x308
   __TEXT.__objc_classname: 0x70
   __TEXT.__objc_methname: 0xed8
   __TEXT.__objc_methtype: 0x139

   __DATA_CONST.__objc_selrefs: 0x4d8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__auth_got: 0x230
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x760
   __AUTH_CONST.__objc_const: 0x328

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 133
-  Symbols:   259
+  Functions: 141
+  Symbols:   268
   CStrings:  356
 
Symbols:
+ _objc_retain_x26
CStrings:
+ "%s \"%{public}@\" is not delivered OTA. Skipping download."
+ "%s %{public}@"
+ "%s %{public}@ Sending back an error."
+ "%s %{public}@ is embedded, download not needed."
+ "%s %{public}@ is not ready."
+ "%s %{public}@ is ready to use (does not need data)."
+ "%s %{public}@ is ready to use."
+ "%s %{public}@: %{public}@"
+ "%s %{public}@: Blocking On-Demand download for \"%{public}@\" completed successfully!"
+ "%s %{public}@: Blocking On-Demand download for \"%{public}@\" failed: %{public}@"
+ "%s %{public}@: Download status: %{public}@"
+ "%s %{public}@: Failed to subscribe to morphun assets for: \"%{public}@\""
+ "%s A nil array was found for this process (key = %{public}@)"
+ "%s A nil dictionary was returned from the NSUserDefaults database (key = %{public}@)."
+ "%s AFPreferences returned %{public}@"
+ "%s Adding %{public}@ to subscribed languages for %{public}@"
+ "%s Already subscribed to %{public}@ for %{public}@"
+ "%s Blocking On-Demand removal for \"%{public}@\" completed successfully!"
+ "%s Blocking On-Demand removal for \"%{public}@\" failed: %{public}@"
+ "%s Configuration parser returned a nil value for key %{public}@"
+ "%s Creating process subscription array (key = %{public}@)."
+ "%s Error parsing version strings:\nInput version: %{public}@\nlibmorphun version:%{public}@"
+ "%s Existing UAFAssetSet does not contain asset for usage value %{public}@"
+ "%s Failed to parse configuration file at %{public}@"
+ "%s Failed to read configuration file at %{public}@"
+ "%s Locale \"%{public}@\" does not need to be downloaded."
+ "%s Locale \"%{public}@\" is not a supported locale: %{public}@."
+ "%s New UAFAssetSet does not contain asset for usage value %{public}@, but the existing one does"
+ "%s No UAFAssetSet found for usage value %{public}@"
+ "%s No existing UAFAssetSet found for usage value %{public}@"
+ "%s No subscription array found for process key %{public}@."
+ "%s Not subscribed to %{public}@ for %{public}@. Nothing to do."
+ "%s Old UAFAssetSet has asset path %{public}@, new UAFAssetSet has asset path %{public}@ for usage value %{public}@"
+ "%s Reading configuration file %{public}@"
+ "%s Received update to UAF Asset set, updating all existing UAFAssetSets %{public}@"
+ "%s Reference count for %{public}@ is %u, path is %{public}@, download not needed."
+ "%s Reference count for %{public}@ is %u, path is nil, download needed."
+ "%s Reference count for %{public}@ is %u, path is nil, removal not needed."
+ "%s Reference count for %{public}@ is %u, path is not nil, removal needed."
+ "%s Reference count for %{public}@ is %u, removal needed."
+ "%s Reference count for %{public}@ is 0, download needed."
+ "%s Reference count for %{public}@ is nil, download needed."
+ "%s Reference count for %{public}@ is nil, removal needed."
+ "%s Remote version (%{public}@) vs. Local version (%{public}@)"
+ "%s Removing %{public}@ from subscribed locales of %{public}@"
+ "%s Retreived language path for %{public}@ : %{public}@"
+ "%s Retreived path for locale %{public}@ : %{public}@"
+ "%s Retrieved configuration returned an empty dictionary for %{public}@"
+ "%s Retrieving subscription dictionary from user defaults cache (Suite = %{public}@) (key = %{public}@)"
+ "%s Starting blocking On-Demand removal for: \"%{public}@\""
+ "%s Unsubscribing from UAF subscription: %{public}@"
+ "%s Updating UAFAssetSet for usage value %{public}@"
+ "%s Will not update the UAFAssetSet for usage value %{public}@"
- "%s \"%@\" is not delivered OTA. Skipping download."
- "%s %@"
- "%s %@ Sending back an error."
- "%s %@ is embedded, download not needed."
- "%s %@ is not ready."
- "%s %@ is ready to use (does not need data)."
- "%s %@ is ready to use."
- "%s %{public}@: %@"
- "%s %{public}@: Blocking On-Demand download for \"%@\" completed successfully!"
- "%s %{public}@: Blocking On-Demand download for \"%@\" failed: %@"
- "%s %{public}@: Download status: %@"
- "%s %{public}@: Failed to subscribe to morphun assets for: \"%@\""
- "%s A nil array was found for this process (key = %@)"
- "%s A nil dictionary was returned from the NSUserDefaults database (key = %@)."
- "%s AFPreferences returned %@"
- "%s Adding %@ to subscribed languages for %@"
- "%s Already subscribed to %@ for %@"
- "%s Blocking On-Demand removal for \"%@\" completed successfully!"
- "%s Blocking On-Demand removal for \"%@\" failed: %@"
- "%s Configuration parser returned a nil value for key %@"
- "%s Creating process subscription array (key = %@)."
- "%s Error parsing version strings:\nInput version: %@\nlibmorphun version:%@"
- "%s Existing UAFAssetSet does not contain asset for usage value %@"
- "%s Failed to parse configuration file at %@"
- "%s Failed to read configuration file at %@"
- "%s Locale \"%@\" does not need to be downloaded."
- "%s Locale \"%@\" is not a supported locale: %@."
- "%s New UAFAssetSet does not contain asset for usage value %@, but the existing one does"
- "%s No UAFAssetSet found for usage value %@"
- "%s No existing UAFAssetSet found for usage value %@"
- "%s No subscription array found for process key %@."
- "%s Not subscribed to %@ for %@. Nothing to do."
- "%s Old UAFAssetSet has asset path %@, new UAFAssetSet has asset path %@ for usage value %@"
- "%s Reading configuration file %@"
- "%s Received update to UAF Asset set, updating all existing UAFAssetSets %@"
- "%s Reference count for %@ is %u, path is %@, download not needed."
- "%s Reference count for %@ is %u, path is nil, download needed."
- "%s Reference count for %@ is %u, path is nil, removal not needed."
- "%s Reference count for %@ is %u, path is not nil, removal needed."
- "%s Reference count for %@ is %u, removal needed."
- "%s Reference count for %@ is 0, download needed."
- "%s Reference count for %@ is nil, download needed."
- "%s Reference count for %@ is nil, removal needed."
- "%s Remote version (%@) vs. Local version (%@)"
- "%s Removing %@ from subscribed locales of %@"
- "%s Retreived language path for %@ : %@"
- "%s Retreived path for locale %@ : %@"
- "%s Retrieved configuration returned an empty dictionary for %@"
- "%s Retrieving subscription dictionary from user defaults cache (Suite = %@) (key = %@)"
- "%s Starting blocking On-Demand removal for: \"%@\""
- "%s Unsubscribing from UAF subscription: %@"
- "%s Updating UAFAssetSet for usage value %@"
- "%s Will not update the UAFAssetSet for usage value %@"

```
