## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation`

```diff

-820.2.6.0.0
-  __TEXT.__text: 0x16b764
+820.2.8.2.1
+  __TEXT.__text: 0x16b1d0
   __TEXT.__auth_stubs: 0x2910
-  __TEXT.__objc_methlist: 0x1235c
+  __TEXT.__objc_methlist: 0x12384
   __TEXT.__cstring: 0x19ae3
   __TEXT.__const: 0x6548
   __TEXT.__gcc_except_tab: 0x149c

   __TEXT.__swift_as_entry: 0x190
   __TEXT.__swift_as_ret: 0x1dc
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x65a8
-  __TEXT.__eh_frame: 0x5500
+  __TEXT.__unwind_info: 0x6590
+  __TEXT.__eh_frame: 0x5508
   __TEXT.__objc_classname: 0x1ef7
-  __TEXT.__objc_methname: 0x2733b
-  __TEXT.__objc_methtype: 0x641f
+  __TEXT.__objc_methname: 0x273a1
+  __TEXT.__objc_methtype: 0x644a
   __TEXT.__objc_stubs: 0x14f80
-  __DATA_CONST.__got: 0x10f8
+  __DATA_CONST.__got: 0x1100
   __DATA_CONST.__const: 0x60d0
   __DATA_CONST.__objc_classlist: 0x820
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8588
+  __DATA_CONST.__objc_selrefs: 0x8598
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x280
   __AUTH_CONST.__auth_got: 0x1498
   __AUTH_CONST.__const: 0x59a0
   __AUTH_CONST.__cfstring: 0x11460
-  __AUTH_CONST.__objc_const: 0x24cc0
+  __AUTH_CONST.__objc_const: 0x24d40
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH.__objc_data: 0x2cf8
   __AUTH.__data: 0x1150
-  __DATA.__objc_ivar: 0x1054
+  __DATA.__objc_ivar: 0x1058
   __DATA.__data: 0x3b10
   __DATA.__bss: 0x8490
   __DATA.__common: 0x20

   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AtomicsInternal.framework/AtomicsInternal
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /System/Library/PrivateFrameworks/CopresenceCore.framework/CopresenceCore
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3EB2B78D-A058-39E3-8CAF-FAC61BDF20CD
-  Functions: 10872
-  Symbols:   24717
-  CStrings:  13664
+  UUID: 87B88AE8-52E3-3956-88E0-232618CC4AB4
+  Functions: 10867
+  Symbols:   24727
+  CStrings:  13667
 
Symbols:
+ -[GKInstallMetadata initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:isBeta:sizeOnDeviceInBytes:persistentRecordID:]
+ -[GKInstallMetadata sizeOnDeviceInBytes]
+ _OBJC_CLASS_$_BSAuditToken
+ _OBJC_IVAR_$_GKInstallMetadata._sizeOnDeviceInBytes
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.783
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.784
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.784.cold.1
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.784.cold.2
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.784.cold.3
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.784.cold.4
+ ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.784.cold.5
- -[GKInstallMetadata initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:isBeta:persistentRecordID:]
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke.781
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.782
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.782.cold.1
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.782.cold.2
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.782.cold.3
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.782.cold.4
- ___47-[GKServiceProxy buildServiceLookupIfNecessary]_block_invoke_2.782.cold.5
CStrings:
+ "@120@0:8@16@24@32@40@48@56B64B68q72B80q84q92B100@104@112"
+ "Vv32@0:8@\"NSString\"16@\"BSAuditToken\"24"
+ "clearInstallMetadataCacheWithCompletion:"
+ "initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:isBeta:sizeOnDeviceInBytes:persistentRecordID:"
+ "launchOverlayForGameBundleId:auditToken:"
- "@112@0:8@16@24@32@40@48@56B64B68q72B80q84q92B100@104"
- "initWithBundleID:adamID:bundleShortVersion:name:shortName:estimatedInstallDate:supportsGameController:isArcade:platform:isHidden:metadataEligibility:applicationType:isBeta:persistentRecordID:"

```
