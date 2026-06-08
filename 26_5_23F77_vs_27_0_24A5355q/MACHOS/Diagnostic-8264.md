## Diagnostic-8264

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8264.appex/Diagnostic-8264`

```diff

-921.120.4.0.0
-  __TEXT.__text: 0x3de4
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x30c
+1291.0.0.502.1
+  __TEXT.__text: 0x4764
+  __TEXT.__auth_stubs: 0x3d0
+  __TEXT.__objc_stubs: 0xe80
+  __TEXT.__objc_methlist: 0x354
   __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x204
-  __TEXT.__cstring: 0x5b6
-  __TEXT.__oslogstring: 0x5a1
-  __TEXT.__objc_classname: 0x96
-  __TEXT.__objc_methname: 0xb25
-  __TEXT.__objc_methtype: 0x26c
-  __TEXT.__unwind_info: 0xf0
-  __DATA_CONST.__auth_got: 0x1d8
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__auth_ptr: 0x18
+  __TEXT.__gcc_except_tab: 0x190
+  __TEXT.__cstring: 0x81f
+  __TEXT.__oslogstring: 0x6e4
+  __TEXT.__objc_classname: 0x92
+  __TEXT.__objc_methname: 0xdda
+  __TEXT.__objc_methtype: 0x2c4
+  __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__const: 0x78
-  __DATA_CONST.__cfstring: 0x640
+  __DATA_CONST.__cfstring: 0x880
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x598
-  __DATA.__objc_selrefs: 0x3c0
-  __DATA.__objc_ivar: 0x2c
+  __DATA_CONST.__auth_got: 0x1f8
+  __DATA_CONST.__got: 0x168
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA.__objc_const: 0x5f0
+  __DATA.__objc_selrefs: 0x4b0
+  __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
+  - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libFDR.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: 9AD9FB3A-7ECA-3AC0-BCCC-9824759BA888
-  Functions: 54
-  Symbols:   116
-  CStrings:  339
+  UUID: 8C494568-FDC3-3679-ABE7-400560472EA2
+  Functions: 59
+  Symbols:   123
+  CStrings:  424
 
Symbols:
+ _OBJC_CLASS_$_CRDeviceMap
+ _OBJC_CLASS_$_CRMobileAsset
+ _OBJC_CLASS_$_MAAssetQuery
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x27
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
CStrings:
+ "%@.%@"
+ "%X"
+ "-[VeridianFWUpdateController _downloadVeridianFirmwareWithMobileAsset:]"
+ "-[VeridianFWUpdateController _queryAssets:controller:error:]"
+ "-[VeridianFWUpdateController _verifyAndPlaceAsset:error:]"
+ ".plist"
+ "0c88076f-c292-4dad-95e7-304db9d29d34"
+ "@40@0:8@16@24^@32"
+ "Asset has been downloaded to: %@"
+ "Asset has no local URL after download"
+ "B32@0:8@16^@24"
+ "Copy asset successfully to: %@"
+ "Could not find firmware file"
+ "Download asset successfully for %@"
+ "Downloading battery FW from MobileAsset"
+ "Failed to download asset"
+ "Failed to download catalog"
+ "Failed to init %@"
+ "Failed to list contents under: %@"
+ "Failed to query asset"
+ "Failed to query assets"
+ "Failed to set asset audience"
+ "Found asset to use: %@, state: %ld"
+ "Mobile Asset audience overridden: %@"
+ "No matching asset found"
+ "No suitable asset found for download"
+ "Querying for asset with BatteryCode: %@"
+ "RepairBatteryFirmware"
+ "Start to download asset for %@"
+ "Start to download catalog for %@"
+ "Start to query asset for %@"
+ "T@\"NSString\",&,N,V_failedSPC"
+ "T@\"NSString\",R,N,VoverrideMAAudience"
+ "URLByAppendingPathComponent:"
+ "_downloadVeridianFirmwareWithMobileAsset:"
+ "_failedSPC"
+ "_queryAssets:controller:error:"
+ "_verifyAndPlaceAsset:error:"
+ "addKeyValuePair:with:"
+ "assetId"
+ "com.apple.MobileAsset"
+ "contentsOfDirectoryAtPath:error:"
+ "copy"
+ "copyItemAtURL:toURL:error:"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "downloadAssetWithTimeout:asset:error:"
+ "downloadCatalogWithTimeout:error:"
+ "failedSPC"
+ "getLocalUrl"
+ "hasSuffix:"
+ "initWithAssetType:"
+ "initWithType:"
+ "mutableCopy"
+ "overrideMAAudience"
+ "parseErrorStatusForBatteryUpdate:"
+ "path"
+ "q24@0:8@16"
+ "queryAssetsWithTimeout:query:"
+ "refreshState"
+ "results"
+ "returnTypes:"
+ "setDoNotBlockBeforeFirstUnlock:"
+ "setFailedSPC:"
+ "setMobileAssetAudience:"
+ "state"
+ "updateDATFirmware:withReply:"
+ "useMobileAssetForBatteryFWUpdate"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
- "MountPath"
- "PDI mountPath is %@"
- "updateBrunorDATFirmwareWithReply:"
- "updateSavageDATFirmwareWithReply:"

```
