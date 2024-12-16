## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-596.10.0.0.0
-  __TEXT.__text: 0x455d8
-  __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x4308
+596.13.0.0.0
+  __TEXT.__text: 0x4400c
+  __TEXT.__auth_stubs: 0xa30
+  __TEXT.__objc_methlist: 0x4270
   __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x46de
+  __TEXT.__cstring: 0x45fa
   __TEXT.__gcc_except_tab: 0x938
-  __TEXT.__oslogstring: 0x4a04
-  __TEXT.__ustring: 0x62
+  __TEXT.__oslogstring: 0x4976
+  __TEXT.__ustring: 0x24
   __TEXT.__dlopen_cstrs: 0x15e
-  __TEXT.__unwind_info: 0x1390
-  __TEXT.__objc_classname: 0x993
-  __TEXT.__objc_methname: 0xda13
-  __TEXT.__objc_methtype: 0x1e38
-  __TEXT.__objc_stubs: 0x82c0
-  __DATA_CONST.__got: 0x6c0
-  __DATA_CONST.__const: 0x1b50
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __TEXT.__unwind_info: 0x1360
+  __TEXT.__objc_classname: 0x980
+  __TEXT.__objc_methname: 0xd818
+  __TEXT.__objc_methtype: 0x1f00
+  __TEXT.__objc_stubs: 0x8040
+  __DATA_CONST.__got: 0x6b8
+  __DATA_CONST.__const: 0x1b70
+  __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2bb0
+  __DATA_CONST.__objc_selrefs: 0x2b10
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x560
-  __AUTH_CONST.__const: 0x1320
-  __AUTH_CONST.__cfstring: 0x4d40
-  __AUTH_CONST.__objc_const: 0xd990
-  __AUTH_CONST.__objc_intobj: 0xf0
+  __AUTH_CONST.__auth_got: 0x528
+  __AUTH_CONST.__const: 0x1300
+  __AUTH_CONST.__cfstring: 0x4b80
+  __AUTH_CONST.__objc_const: 0xd600
+  __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x3c0
+  __AUTH.__objc_data: 0x320
   __DATA.__objc_ivar: 0x5c4
   __DATA.__data: 0xec8
   __DATA.__bss: 0x358

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2100
-  Symbols:   2749
-  CStrings:  3599
+  Functions: 2083
+  Symbols:   2719
+  CStrings:  3560
 
Symbols:
+ _CARThemeAssetAccessoryFilename
+ _CARThemeAssetPhoneFilename
+ _CRCollectVehicleLogs
- _BOMCopierCopyWithOptions
- _BOMCopierFree
- _BOMCopierNew
- _BOMCopierSetCopyFileFinishedHandler
- _BOMCopierSetUserData
- _BOMCopierUserData
- _CARThemeAssetArchiveFilename
- _CARThemeAssetLayoutFilename
- _CARThemeAssetUnarchivedFolderName
- _kCFBundleVersionKey
- _strlen
CStrings:
+ "CARThemeAssetLibrarianObserving"
+ "CarPlay diagnostics error fetching vehicle logs: %@"
+ "Connecting to CarKit diagnostics service for vehicle logs."
+ "Returning system wallpaper"
+ "Returning wallpaper using themeData for display with id: %@"
+ "Reusing current asset identifier"
+ "Set system wallpaper"
+ "Set wallpaper using themeData and display id: %@"
+ "collectVehicleLogs:"
+ "did notify theme asset observer %@ of found no matching asset for %{public}@"
+ "notifyFoundNoMatchingAssetForAssetIdentifier:nextRequiredCompatibilityVersion:requestDescription:"
+ "notifying theme asset observers of found no matching asset for %{public}@"
+ "received found no matching asset, next required compatibility version: %{public}@"
+ "service_foundNoMatchingAssetForAssetIdentifier:nextRequiredCompatibilityVersion:reply:"
+ "themeAssetLibrary:foundNoMatchingAssetExceptWithNextRequiredCompatibilityVersion:"
+ "v16@?0@\"NSURL\"8"
+ "v24@0:8@\"CARThemeAsset\"16"
+ "v24@0:8@\"CARThemeAssetVersion\"16"
+ "v24@0:8@?<v@?@\"NSURL\">16"
+ "v32@0:8@\"CARThemeAssetVersion\"16@\"NSError\"24"
+ "v40@0:8@\"CARThemeAsset\"16@\"CARThemeAsset\"24@\"NSUUID\"32"
+ "v40@0:8@\"NSString\"16@\"NSNumber\"24@\"NSString\"32"
+ "v40@0:8@\"NSString\"16@\"NSNumber\"24@?<v@?>32"
- "%@"
- "%lu"
- "Asset-%@-%lu"
- "B32@0:8@\"NSURL\"16@\"NSURL\"24"
- "CARArchiving"
- "CARThemeAssetOverrider"
- "CARZipArchiver"
- "CDS Asset Identifier is MISSING!\nError:\n%@"
- "CDS Asset Identifier:\n%@ \nError:\n%@ "
- "CarPlayAccessory.assets"
- "CarPlayApp"
- "No assets found in asset folder %@"
- "Posting Asset Error Message %@"
- "URLsForDirectory:inDomains:"
- "_"
- "_assetURLForVersion:"
- "_carplayLibraryDirectoryForAssetIdentifier:"
- "_carplayLibraryURL"
- "_generatedAssetForSourceAssetURL:version:"
- "_overrideAssetSourceURLForAssetIdentifier:"
- "_queue_applyOverrideAsset:"
- "_readVersionFromAsset:assetIdentifier:"
- "_shouldForceUpdateAsset"
- "applied override asset"
- "applying override asset: %@ for vehicleID: %@"
- "archiveDirectory:toLocation:"
- "asset doesn't have AccessoryContentVersion, using CFBundleVersion"
- "asset is already the latest overall version: %{public}@"
- "checking for override asset"
- "copyItemAtURL:toURL:error:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createPKZip"
- "dd/MM HH:mm:ss"
- "dictionaryWithContentsOfURL:error:"
- "enableLogging"
- "extractPKZip"
- "failed to copy %@ to %@, error: %@"
- "failed to copy %@ to %@: %@"
- "failed to create %@"
- "failed to create %@: %@"
- "failed to prepare override asset"
- "failed to read %@: %@"
- "fileExistsAtPath:"
- "fileExistsAtPath:isDirectory:"
- "force updating asset versions to: iOS %{public}@, accessory %{public}@"
- "hasPrefix:"
- "initWithFormat:"
- "invalid asset identifier %@"
- "latest asset in asset library: %@"
- "libraryAgent:receivedOverrideAsset:forVehicleIdentifier:"
- "no asset source for %@"
- "overrideAssetNewerThanAssetVersion:"
- "postAssetErrorNotification:forAsset:"
- "prepared override asset %@"
- "preparing override asset: %{public}@"
- "removeItemAtURL:error:"
- "service_applyOverrideAsset:forVehicleIdentifier:reply:"
- "stringWithFileSystemRepresentation:length:"
- "unarchive:toLocation:"
- "using override asset folder %@"
- "using override zipped asset %@"
- "v40@0:8@\"CARThemeAsset\"16@\"NSUUID\"24@?<v@?>32"

```
