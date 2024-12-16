## carkitd

> `/usr/libexec/carkitd`

```diff

-596.10.0.0.0
-  __TEXT.__text: 0x74920
+596.13.0.0.0
+  __TEXT.__text: 0x78ac4
   __TEXT.__auth_stubs: 0x1140
-  __TEXT.__objc_stubs: 0xedc0
-  __TEXT.__objc_methlist: 0x551c
+  __TEXT.__objc_stubs: 0xf1c0
+  __TEXT.__objc_methlist: 0x56bc
   __TEXT.__const: 0x198
-  __TEXT.__gcc_except_tab: 0x1970
-  __TEXT.__objc_methname: 0x1469a
-  __TEXT.__cstring: 0x5304
-  __TEXT.__oslogstring: 0xcd3d
-  __TEXT.__objc_classname: 0xf18
-  __TEXT.__objc_methtype: 0x3f62
+  __TEXT.__gcc_except_tab: 0x1b00
+  __TEXT.__objc_methname: 0x14d93
+  __TEXT.__cstring: 0x5547
+  __TEXT.__oslogstring: 0xd6d4
+  __TEXT.__objc_classname: 0xf4f
+  __TEXT.__objc_methtype: 0x4066
   __TEXT.__dlopen_cstrs: 0x1c6
-  __TEXT.__unwind_info: 0x1a90
+  __TEXT.__unwind_info: 0x1b38
   __DATA_CONST.__auth_got: 0x8b0
-  __DATA_CONST.__got: 0x7c0
-  __DATA_CONST.__const: 0x2a68
-  __DATA_CONST.__cfstring: 0x5ec0
-  __DATA_CONST.__objc_classlist: 0x258
+  __DATA_CONST.__got: 0x7e0
+  __DATA_CONST.__const: 0x2c40
+  __DATA_CONST.__cfstring: 0x6060
+  __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x208
+  __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__objc_superrefs: 0x1a0
-  __DATA_CONST.__objc_intobj: 0x858
+  __DATA_CONST.__objc_protorefs: 0x88
+  __DATA_CONST.__objc_superrefs: 0x1a8
+  __DATA_CONST.__objc_intobj: 0x870
   __DATA_CONST.__objc_arraydata: 0x940
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x13fc0
-  __DATA.__objc_selrefs: 0x4208
-  __DATA.__objc_ivar: 0x690
-  __DATA.__objc_data: 0x1770
-  __DATA.__data: 0x1868
+  __DATA.__objc_const: 0x143a8
+  __DATA.__objc_selrefs: 0x4320
+  __DATA.__objc_ivar: 0x6a8
+  __DATA.__objc_data: 0x17c0
+  __DATA.__data: 0x18c8
   __DATA.__bss: 0x140
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 2695
-  Symbols:   535
-  CStrings:  5670
+  Functions: 2767
+  Symbols:   539
+  CStrings:  5786
 
Symbols:
+ _CARThemeAssetAccessoryFilename
+ _CARThemeAssetInfoFilename
+ _CARThemeAssetPhoneFilename
+ _kCFBundleVersionKey
+ _kCFPreferencesAnyApplication
- _CARThemeAssetArchiveFilename
CStrings:
+ "\b"
+ "\x12\x11\x13\x13"
+ "\x16\x12\x11"
+ "%@ { Compatibility: %lu, SDK: %@, UpdateCatalog: %@ }"
+ "%@ { assetID: %@, sdkVersion: %@, compatibilityVersion: %lu updateCatalog: %@}"
+ "%lu"
+ "@\"CRThemeAssetOverrider\""
+ "@44@0:8@16@24Q32B40"
+ "AccessoryDeveloperEnabled"
+ "AlwaysUpdateAsset"
+ "An asset is available but requires CompatibilityVersion %@"
+ "Asset-%@-%lu"
+ "B24@?0@\"CRThemeAssetDownloadRequest\"8@\"NSDictionary\"16"
+ "CARThemeAssetLibrarianObserving"
+ "CRThemeAssetOverrider"
+ "CarPlayApp"
+ "Create dismiss timer for CRAlert: %@, dismissTime: %f"
+ "Dictation will begin"
+ "Dictation will begin."
+ "Dismissal timer fired"
+ "Presenting diagnostics alert: %@, timeOut Interval: %f"
+ "Received vehicle log url reply: %@"
+ "T@\"CRThemeAssetOverrider\",R,N,V_assetOverrider"
+ "T@\"NSMutableDictionary\",R,N,V_overallProgressForVehicleIDs"
+ "T@\"NSMutableDictionary\",R,N,V_untrackedDownloadProgressForAssetIDs"
+ "T@\"NSString\",&,N,V_assetUnavailableDescription"
+ "T@\"NSTimer\",&,N,V_dictationInProgressTimer"
+ "TB,R,N,V_requireCatalogUpdate"
+ "Trying to collect vehicle logs but currentSession doesn't support vehicle data"
+ "Trying to collect vehicle logs but currentSession is nil"
+ "URLByStandardizingPath"
+ "Vehicle logs gathered"
+ "Will prompt for internal sysdiagnose"
+ "[Internal]\nRequested asset matching:\n%@"
+ "_"
+ "_assetOverrider"
+ "_assetQueue_nextRequiredCompatibilityVersionToMatchAssetRequest:inAssets:"
+ "_assetQueue_notifyObserverOfFoundNoAssetForAssetRequest:nextRequiredCompatibilityVersion:"
+ "_assetUnavailableDescription"
+ "_carplayLibraryDirectoryForAssetIdentifier:"
+ "_carplayLibraryURL"
+ "_dictationInProgressTimer"
+ "_enablesOverrideAssets"
+ "_internalQueue_generatedAssetForSourceAssetURL:version:"
+ "_mainQueue_applyOverrideAssetForVehicle:"
+ "_mainQueue_handleVehicleAssetConfigurationChanged"
+ "_mainQueue_hasAsset:forAssetRequest:"
+ "_mainQueue_removeAssetProgressForVehicleID:assetID:"
+ "_mainQueue_trackAssetProgressForVehicle:"
+ "_mainQueue_updateOverallProgress"
+ "_overallProgressForVehicleIDs"
+ "_presentAssetUnavailablePromptWithCompletion:"
+ "_presentCheckSoftwareUpdatesWithCompletion:"
+ "_readMetadataFromAsset:assetIdentifier:completion:"
+ "_requireCatalogUpdate"
+ "_shouldForceUpdateAsset"
+ "_untrackedDownloadProgressForAssetIDs"
+ "absoluteString"
+ "added download progress for assetID %{public}@: %{public}@"
+ "added override progress for assetID %{public}@: %{public}@"
+ "added untracked download, overall progress is now: %{public}@"
+ "adding download asset request: %@"
+ "asset doesn't have AccessoryContentVersion, using CFBundleVersion"
+ "asset is already the latest overall version: %{public}@"
+ "asset unavailable"
+ "asset unavailable prompt: check for updates"
+ "asset's minimum compatibility version of %@ is valid for supported compatibility version: %lu"
+ "assetDownloader:foundNoAssetForAssetRequest:nextRequiredCompatibilityVersion:"
+ "assetOverrider"
+ "assetUnavailableDescription"
+ "check software updates"
+ "collectDiagnosticsWithDeviceScreenshotURL"
+ "collectDiagnosticsWithDeviceScreenshotURL infoURL added"
+ "collectDiagnosticsWithDeviceScreenshotURL screenshotURL added"
+ "collectVehicleLogs:"
+ "collectVehicleLogsWithReceiver:completionHandler:"
+ "com.apple.carkit.themeAssetOverrider"
+ "completed present check for software updates"
+ "copyItemAtURL:toURL:error:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "created asset progress %{public}@ for vehicleID: %{public}@"
+ "dictationInProgressTimer"
+ "download failed for asset request: %{public}@ version: %{public}@ error: %@"
+ "downloader found no asset for asset request: %{public}@"
+ "failed to copy %@ to %@, error: %@"
+ "failed to create %@: %@"
+ "failed to find available asset, should offer software update: %{public}@"
+ "failed to prepare override asset"
+ "failed to read %@: %@"
+ "force updating asset versions to: iOS %{public}@, accessory %{public}@"
+ "found no asset for asset request: %{public}@"
+ "found no asset for asset request: %{public}@, however an asset exists for compatibility version %{public}@"
+ "handleFailedToFindAssetForMessagingVehicle:shouldOfferSoftwareUpdate:description:"
+ "hasOverrideAssetForAssetIdentifier:"
+ "initWithAssetIdentifier:maximumSDKVersion:maximumCompatibilityVersion:requireCatalogUpdate:"
+ "initWithVehicleStore:sessionStatus:"
+ "invalid asset identifier %@"
+ "no override asset available for %{public}@"
+ "no override asset found at %@"
+ "no override asset to stage that is newer than %@"
+ "notifyFoundNoMatchingAssetForAssetIdentifier:nextRequiredCompatibilityVersion:requestDescription:"
+ "now"
+ "online asset %@"
+ "overallProgressForVehicleIDs"
+ "override asset %@"
+ "override asset does not have a correct versioning"
+ "override asset does not have a minimum SDK version"
+ "override asset does not have a minimum compatibility version"
+ "override asset's minimum SDK version of %@ is not valid for SDK: %@"
+ "override asset's minimum compatibility version of %@ is not valid for supported compatibility version: %lu"
+ "prepared override asset %@"
+ "preparing override asset: %{public}@"
+ "presentAssetUnavailablePromptWithDescription:responseHandler:"
+ "presentAssetUnavailableWithDescription:responseHandler:"
+ "presentCheckForSoftwareUpdatesWithCompletionHandler:"
+ "presented check for software updates"
+ "received response from asset unavailable prompt, check for updates: %{public}@"
+ "removeObjectsForKeys:"
+ "removing asset progress for vehicleID: %{public}@ assetID: %{public}@"
+ "replacing download progress for assetID %{public}@, previous progress: %{public}@"
+ "replacing override progress for assetID %{public}@, previous progress: %{public}@"
+ "requesting theme assets catalog update: out of date"
+ "requesting theme assets catalog update: required by request"
+ "requireCatalogUpdate"
+ "setAssetUnavailableDescription:"
+ "setDictationInProgressTimer:"
+ "setupOverrideAssetForRequest:newerThanVersion:completion:"
+ "untrackedDownloadProgressForAssetIDs"
+ "using override asset %@"
+ "using override asset for asset request: %@"
+ "v24@0:8@\"CARThemeAsset\"16"
+ "v24@0:8@\"CARThemeAssetVersion\"16"
+ "v24@0:8@?<v@?@\"NSURL\">16"
+ "v24@?0@\"CARThemeAsset\"8@\"NSNumber\"16"
+ "v32@0:8@\"CARThemeAssetVersion\"16@\"NSError\"24"
+ "v32@?0@\"CARThemeAssetVersion\"8@\"NSNumber\"16@\"NSString\"24"
+ "v32@?0@\"NSString\"8@\"NSProgress\"16^B24"
+ "v32@?0@\"NSUUID\"8@\"NSProgress\"16^B24"
+ "v40@0:8@\"CARThemeAsset\"16@\"CARThemeAsset\"24@\"NSUUID\"32"
+ "v40@0:8@\"CRThemeAssetDownloader\"16@\"CRThemeAssetDownloadRequest\"24@\"NSNumber\"32"
+ "v40@0:8@\"NSString\"16@\"NSNumber\"24@\"NSString\"32"
- "\x06"
- "\x12\x11\x13\x12"
- "\x16\x12"
- "%@ { assetID: %@, sdkVersion: %@, compatibilityVersion: %lu }"
- "@\"CARThemeAssetLibraryAgent\""
- "Presenting diagnostics alert: %@"
- "T@\"CARThemeAssetLibraryAgent\",R,N,V_libraryAgent"
- "T@\"NSMutableDictionary\",R,N,V_assetProgressForVehicleIdentifiers"
- "_assetProgressForVehicle:"
- "_assetProgressForVehicleIdentifiers"
- "_libraryAgent"
- "_mainQueue_handleVehiclesChanged"
- "_removeAssetProgressForVehicleIdentifier:"
- "assetProgressForVehicleIdentifiers"
- "attempting download for vehicle %@, overall progress is now: %@"
- "created asset progress %@ for vehicleID: %@"
- "download failed for asset request: %@ version: %@ error: %@"
- "initWithAssetIdentifier:maximumSDKVersion:maximumCompatibilityVersion:"
- "initWithLibraryAgent:vehicleStore:sessionStatus:"
- "libraryAgent"
- "libraryAgent:receivedOverrideAsset:forVehicleIdentifier:"
- "removing asset progress for vehicleID: %@"
- "staging override asset %{public}@"
- "theme assets catalog out of date"
- "v40@0:8@\"CARThemeAssetLibraryAgent\"16@\"CARThemeAsset\"24@\"NSUUID\"32"

```
