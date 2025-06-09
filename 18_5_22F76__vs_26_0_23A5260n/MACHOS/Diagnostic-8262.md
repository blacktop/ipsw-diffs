## Diagnostic-8262

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8262.appex/Diagnostic-8262`

```diff

-696.120.5.0.0
-  __TEXT.__text: 0x2f20
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_stubs: 0x980
-  __TEXT.__objc_methlist: 0x254
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x60f
-  __TEXT.__oslogstring: 0x3a6
+921.0.34.0.0
+  __TEXT.__text: 0x375c
+  __TEXT.__auth_stubs: 0x320
+  __TEXT.__objc_stubs: 0xb20
+  __TEXT.__objc_methlist: 0x274
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x816
+  __TEXT.__oslogstring: 0x4c7
   __TEXT.__objc_classname: 0x4c
-  __TEXT.__objc_methname: 0x95e
+  __TEXT.__objc_methname: 0xae0
   __TEXT.__objc_methtype: 0x155
   __TEXT.__gcc_except_tab: 0x1b0
-  __TEXT.__unwind_info: 0xd0
-  __DATA_CONST.__auth_got: 0x190
-  __DATA_CONST.__got: 0xd8
+  __TEXT.__unwind_info: 0xd8
+  __DATA_CONST.__auth_got: 0x1a0
+  __DATA_CONST.__got: 0xf8
   __DATA_CONST.__const: 0x90
-  __DATA_CONST.__cfstring: 0x640
+  __DATA_CONST.__cfstring: 0x860
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x4f0
-  __DATA.__objc_selrefs: 0x328
-  __DATA.__objc_ivar: 0x34
+  __DATA.__objc_const: 0x520
+  __DATA.__objc_selrefs: 0x390
+  __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
+  - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileStorage.framework/MobileStorage
   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5E213EAD-C0BB-3EB8-8DA9-84F062B0072F
-  Functions: 32
-  Symbols:   92
-  CStrings:  302
+  UUID: 0E9E0FB6-D0E4-3E3E-96BE-D1A030763F77
+  Functions: 36
+  Symbols:   99
+  CStrings:  358
 
Symbols:
+ _Diagnostic_8262VersionNumber
+ _Diagnostic_8262VersionString
+ _OBJC_CLASS_$_CRUserDefaults
+ _OBJC_CLASS_$_MAAutoAsset
+ _OBJC_CLASS_$_MAAutoAssetPolicy
+ _OBJC_CLASS_$_MAAutoAssetSelector
+ _objc_alloc
+ _os_variant_has_internal_content
- _createCRError
CStrings:
+ "%@.%@"
+ "%@/FactoryDiskImagePersonalized.dmg"
+ "-[UpdatePluginsController _downloadPDIWithCDN:]"
+ "-[UpdatePluginsController _downloadPDIWithMobileAsset:]"
+ "8262"
+ "Device should reboot to Diagnostics mode"
+ "Download asset successfully, but there is no Mobile Asset PDI at: %@"
+ "Download mobile asset timeout"
+ "Failed to download asset with MobileAsset, error: %@"
+ "Failed to init assetSelector"
+ "Failed to init autoAsset"
+ "Failed to lock asset"
+ "Failed to move Mobile Asset PDI to: %@"
+ "Failed to read file, error: %@"
+ "Failed to unlock asset"
+ "Failed to update plugins, error: %@"
+ "Find Mobile Asset PDI at: %@"
+ "Lock asset successfully, local asset path: %@"
+ "No matching asset to download"
+ "Plugins map is: %@"
+ "Rebuilding DB successfully"
+ "Repair Update plugin path is: %@"
+ "RepairUpdate"
+ "RepairUpdateClient"
+ "Start to download assetType: %@, assetSpecifier: %@"
+ "TB,R,N,VuseMobileAsset"
+ "Unable to find Application after %d retries"
+ "Unlock asset successfully"
+ "Using MobileAsset"
+ "_downloadPDIWithCDN:"
+ "_downloadPDIWithMobileAsset:"
+ "_readUseMobileAssetFromDefaults"
+ "absoluteString"
+ "com.apple.MobileAsset"
+ "com.apple.corerepaird"
+ "com.apple.corerepaird.test"
+ "dictionaryForKey:"
+ "endLockUsageSync:"
+ "https://gs.apple.com:443"
+ "initForAssetType:withAssetSpecifier:"
+ "initForClientName:selectingAsset:error:"
+ "initWithSuiteName:"
+ "lockContentSync:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:"
+ "lockRepairUpdateContent"
+ "moveItemAtPath:toPath:error:"
+ "objectForKey:"
+ "setUserInitiated:"
+ "useMobileAsset"
+ "useMobileAsset: %@"
- " inDiagnosticsmode:%d"
- "-[UpdatePluginsController _downloadDiskImageWithError:]"
- "Failed to read:%@"
- "Map is:%@"
- "Ticket:%@"
- "Unable to find Application after 5 retries"
- "UpdatePlugins failed:%@"
- "_downloadDiskImageWithError:"
- "https://gs.apple.com"
- "plugins Path is:%@"
- "re building DB successsful"

```
