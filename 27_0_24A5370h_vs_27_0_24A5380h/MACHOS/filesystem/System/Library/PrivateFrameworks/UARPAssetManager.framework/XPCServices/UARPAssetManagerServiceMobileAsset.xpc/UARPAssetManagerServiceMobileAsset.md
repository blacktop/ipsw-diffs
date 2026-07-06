## UARPAssetManagerServiceMobileAsset

> `/System/Library/PrivateFrameworks/UARPAssetManager.framework/XPCServices/UARPAssetManagerServiceMobileAsset.xpc/UARPAssetManagerServiceMobileAsset`

```diff

-  __TEXT.__text: 0xf338
-  __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_stubs: 0x21e0
-  __TEXT.__objc_methlist: 0xc44
-  __TEXT.__objc_classname: 0x24d
-  __TEXT.__cstring: 0x1134
-  __TEXT.__objc_methname: 0x2106
-  __TEXT.__objc_methtype: 0x5cc
-  __TEXT.__oslogstring: 0x1406
+  __TEXT.__text: 0x103ac
+  __TEXT.__auth_stubs: 0x4a0
+  __TEXT.__objc_stubs: 0x22c0
+  __TEXT.__objc_methlist: 0xd14
+  __TEXT.__objc_classname: 0x269
+  __TEXT.__cstring: 0x12b5
+  __TEXT.__objc_methname: 0x2305
+  __TEXT.__objc_methtype: 0x5f1
+  __TEXT.__oslogstring: 0x14cf
   __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__unwind_info: 0x390
-  __DATA_CONST.__const: 0x360
-  __DATA_CONST.__cfstring: 0xf00
-  __DATA_CONST.__objc_classlist: 0x68
+  __TEXT.__unwind_info: 0x3c0
+  __DATA_CONST.__const: 0x3e0
+  __DATA_CONST.__cfstring: 0x1160
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x258
-  __DATA_CONST.__got: 0x140
-  __DATA.__objc_const: 0x19e0
-  __DATA.__objc_selrefs: 0x9c0
-  __DATA.__objc_ivar: 0xbc
-  __DATA.__objc_data: 0x410
+  __DATA_CONST.__auth_got: 0x260
+  __DATA_CONST.__got: 0x148
+  __DATA.__objc_const: 0x1b70
+  __DATA.__objc_selrefs: 0xa08
+  __DATA.__objc_ivar: 0xd0
+  __DATA.__objc_data: 0x460
   __DATA.__data: 0x300
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 318
-  Symbols:   225
-  CStrings:  851
+  Functions: 342
+  Symbols:   238
+  CStrings:  916
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
Symbols:
+ _CFPreferencesCopyAppValue
+ _OBJC_CLASS_$_UARPAssetSubscriptioniCloud
+ _OBJC_CLASS_$_UARPEndpointPersonalityiCloud
+ _OBJC_METACLASS_$_UARPAssetSubscriptioniCloud
+ _containerIDForAssetContainerType
+ _createPersonalityForiCloudSubscription
+ _createiCloudSubscriptionForPersonality
+ _getContainerIDFromCFPrefs
+ _kUARPAssetManagerServiceCacheRegistryFileExtension
+ _kUARPAssetManagerServiceCacheVerificationCertsFileName
+ _kUARPAssetManagerServiceReleaseNotesFileName
+ _kUARPAssetManagerServiceiCloudCertificateFileName
+ _kUARPAssetManagerServiceiCloudTokenFileName
CStrings:
+ "%@-%@"
+ "%s: ContainerID override found for %@: %@"
+ "-[UARPAssetManagerServiceAssetCache pruneExpiredRegistryEntries:]_block_invoke"
+ "<%@: pgpn=%@-%@, containerID=%@ releaseNotes=%@ domain=%@>"
+ "@56@0:8@16@24@32B40B44@48"
+ "B20@0:8B16"
+ "NO"
+ "Only iCloud accessory personalities are currently supported"
+ "Only iCloud accessory subscriptions are currently supported"
+ "T@\"NSString\",R,V_containerID"
+ "T@\"NSString\",R,V_productGroup"
+ "T@\"NSString\",R,V_productNumber"
+ "TB,R,V_downloadOnCellularAllowed"
+ "TB,R,V_releaseNotesAsset"
+ "UARPAssetSubscriptioniCloud"
+ "UARPVerificationCertificates.plist"
+ "UARPiCloudTokens.plist"
+ "Unsupported container type %{public}ld"
+ "YES"
+ "_containerID"
+ "_downloadOnCellularAllowed"
+ "_productGroup"
+ "_productNumber"
+ "_releaseNotesAsset"
+ "cellularDownload"
+ "clearCacheRecordForSubscription:"
+ "com.apple.uarp.beta"
+ "com.apple.uarp.staging"
+ "com.apple.uarp.staging.beta"
+ "com.apple.uarp.staging.uat"
+ "com.apple.uarp.uat"
+ "containerID"
+ "downloadOnCellularAllowed"
+ "getContainerIDFromCFPrefs"
+ "initWithProductGroup:productNumber:containerID:releaseNotesAsset:downloadOnCellularAllowed:domain:"
+ "initWithProductGroup:productNumber:domain:"
+ "plist"
+ "productGroup"
+ "productNumber"
+ "pruneExpiredRegistryEntries:"
+ "releaseNotes"
+ "releaseNotesAsset"
+ "releasenotes"
+ "setContainerID:"
+ "vid0x%04lXpid0x%04lX"
- "-[UARPAssetManagerServiceAssetCache pruneExpiredRegistryEntries]_block_invoke"
- "pruneExpiredRegistryEntries"

```
