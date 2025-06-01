## SpaceAttribution

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution`

```diff

-180.60.4.0.0
-  __TEXT.__text: 0xd4a4
+180.102.1.0.0
+  __TEXT.__text: 0xd6b0
   __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_methlist: 0xc40
+  __TEXT.__objc_methlist: 0xc94
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0xc49
-  __TEXT.__oslogstring: 0xc3f
-  __TEXT.__gcc_except_tab: 0x4e0
-  __TEXT.__unwind_info: 0x44c
+  __TEXT.__cstring: 0xb87
+  __TEXT.__oslogstring: 0xc4e
+  __TEXT.__gcc_except_tab: 0x500
+  __TEXT.__unwind_info: 0x450
   __TEXT.__objc_classname: 0x13a
-  __TEXT.__objc_methname: 0x1fb9
-  __TEXT.__objc_methtype: 0x6a7
-  __TEXT.__objc_stubs: 0x1620
-  __DATA_CONST.__got: 0x58
+  __TEXT.__objc_methname: 0x20a4
+  __TEXT.__objc_methtype: 0x6e1
+  __TEXT.__objc_stubs: 0x15a0
+  __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x3d8
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1190
-  __DATA_CONST.__objc_selrefs: 0x8f8
+  __DATA_CONST.__objc_const: 0x1270
+  __DATA_CONST.__objc_selrefs: 0x908
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__cfstring: 0xe00
-  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__cfstring: 0xd40
+  __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_const: 0x7e0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__auth_got: 0x2b8
   __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0xd8
-  __DATA.__objc_superrefs: 0x58
-  __DATA.__objc_ivar: 0xcc
+  __DATA.__objc_ivar: 0xdc
   __DATA.__data: 0x180
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BCD977EE-A9C4-32D2-BA25-B8D2BD987D89
-  Functions: 412
-  Symbols:   1405
-  CStrings:  824
+  UUID: CA3F91E5-CB06-3D86-881E-D9235CB09E63
+  Functions: 423
+  Symbols:   1423
+  CStrings:  825
 
Symbols:
+ +[SAInternalAPI importFromPlist:reply:]
+ +[SASupport getLSAppRecordForBundle:reply:]
+ +[SAVolumeSizer computeSizeOfVolumeAtURL:completionHandler:].cold.2
+ -[SAAppSizerResults appsList]
+ -[SAAppSizerResults setAppsList:]
+ -[SAAppSizerResults setTotalCDAvailable:]
+ -[SAAppSizerResults setTotalPurgeableClones:]
+ -[SAAppSizerResults setZeroSizeApps:]
+ -[SAAppSizerResults totalCDAvailable]
+ -[SAAppSizerResults totalPurgeableClones]
+ -[SAAppSizerResults zeroSizeApps]
+ GCC_except_table45
+ _OBJC_IVAR_$_SAAppSizerResults._appsList
+ _OBJC_IVAR_$_SAAppSizerResults._totalCDAvailable
+ _OBJC_IVAR_$_SAAppSizerResults._totalPurgeableClones
+ _OBJC_IVAR_$_SAAppSizerResults._zeroSizeApps
+ ___38-[SADaemonXPC setInvalidationHandler:]_block_invoke.84
+ ___38-[SADaemonXPC setInvalidationHandler:]_block_invoke.84.cold.1
+ ___39+[SAInternalAPI importFromPlist:reply:]_block_invoke
+ ___39+[SAInternalAPI importFromPlist:reply:]_block_invoke_2
+ ___39+[SAInternalAPI importFromPlist:reply:]_block_invoke_3
+ ___57-[SAAppSizerResults postProcessFilteringWithAppPathList:]_block_invoke.325
+ ___62-[SAPathManager unregisterURLs:forBundleID:completionHandler:]_block_invoke.144
+ ___62-[SAPathManager unregisterURLs:forBundleID:completionHandler:]_block_invoke.144.cold.1
+ ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.44
+ ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.44.cold.1
+ ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.45
+ ___block_literal_global.86
+ __unnamed_array_storage.126
+ __unnamed_array_storage.53
+ __unnamed_array_storage.56
+ _objc_msgSend$appsList
+ _objc_msgSend$importFromPlist:reply:
+ _objc_msgSend$totalCDAvailable
+ _objc_msgSend$totalPurgeableClones
- +[SASupport getLSAppRecordForBundle:]
- +[SASupport isAppUserVisible:]
- +[SASupport isAppsSetUserVisible:]
- ___30+[SASupport isAppUserVisible:]_block_invoke
- ___38-[SADaemonXPC setInvalidationHandler:]_block_invoke.79
- ___38-[SADaemonXPC setInvalidationHandler:]_block_invoke.79.cold.1
- ___57-[SAAppSizerResults postProcessFilteringWithAppPathList:]_block_invoke.309
- ___62-[SAPathManager unregisterURLs:forBundleID:completionHandler:]_block_invoke.141
- ___62-[SAPathManager unregisterURLs:forBundleID:completionHandler:]_block_invoke.141.cold.1
- ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.41
- ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.41.cold.1
- ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.42
- ___block_literal_global.35
- ___block_literal_global.81
- ___kCFBooleanFalse
- ___kCFBooleanTrue
- __unnamed_array_storage.123
- __unnamed_array_storage.50
- __unnamed_array_storage.92
- _isAppUserVisible:.forceHiddenApps
- _isAppUserVisible:.forceVisible
- _objc_msgSend$applicationState
- _objc_msgSend$developerType
- _objc_msgSend$getLSAppRecordForBundle:
- _objc_msgSend$isAppUserVisible:
- _objc_msgSend$isDeletable
- _objc_msgSend$isRestricted
- _objc_msgSend$isSystemPlaceholder
- _objc_msgSend$targetDeviceIsIpad
CStrings:
+ "\x01I"
+ "%s: url is nil"
+ "@\"NSMutableArray\""
+ "Apps List"
+ "T@\"NSMutableArray\",&,V_zeroSizeApps"
+ "T@\"NSMutableDictionary\",&,V_appsList"
+ "TQ,V_totalCDAvailable"
+ "TQ,V_totalPurgeableClones"
+ "TotalCDAvailable"
+ "TotalPurgeableClones"
+ "_appsList"
+ "_totalCDAvailable"
+ "_totalPurgeableClones"
+ "_zeroSizeApps"
+ "appsList"
+ "getLSAppRecordForBundle:reply:"
+ "importFromPlist:reply:"
+ "setAppsList:"
+ "setTotalCDAvailable:"
+ "setTotalPurgeableClones:"
+ "setZeroSizeApps:"
+ "totalCDAvailable"
+ "totalPurgeableClones"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "zeroSizeApps"
- "\x01G"
- "applicationState"
- "com.apple.CloudDocs.iCloudDriveFileProvider"
- "com.apple.Health"
- "com.apple.Maps"
- "com.apple.MobileSMS"
- "com.apple.NanoPassbook"
- "com.apple.Passbook"
- "com.apple.Preferences"
- "com.apple.TapToRadar"
- "com.apple.compass"
- "com.apple.fakeapp.SyncedContent"
- "com.apple.mobilephone"
- "com.apple.mobilesafari"
- "com.apple.mobileslideshow"
- "developerType"
- "getLSAppRecordForBundle:"
- "isAppUserVisible:"
- "isAppsSetUserVisible:"
- "isDeletable"
- "isRestricted"
- "isSystemPlaceholder"

```
