## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4257.40.57.0.1
-  __TEXT.__text: 0x311514
+4257.40.63.0.1
+  __TEXT.__text: 0x312420
   __TEXT.__auth_stubs: 0x1b40
-  __TEXT.__objc_methlist: 0x1a24c
+  __TEXT.__objc_methlist: 0x1a33c
   __TEXT.__const: 0x500
-  __TEXT.__cstring: 0x7d6ac
-  __TEXT.__oslogstring: 0x3c1d5
-  __TEXT.__gcc_except_tab: 0x1a568
+  __TEXT.__cstring: 0x7d737
+  __TEXT.__oslogstring: 0x3c2d4
+  __TEXT.__gcc_except_tab: 0x1a688
   __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0x9fb0
-  __TEXT.__objc_classname: 0x2acc
-  __TEXT.__objc_methname: 0x446a2
+  __TEXT.__unwind_info: 0xa020
+  __TEXT.__objc_classname: 0x2b0f
+  __TEXT.__objc_methname: 0x44819
   __TEXT.__objc_methtype: 0x905f
-  __TEXT.__objc_stubs: 0x2f160
+  __TEXT.__objc_stubs: 0x2f2c0
   __DATA_CONST.__got: 0x1718
   __DATA_CONST.__const: 0x95f0
-  __DATA_CONST.__objc_classlist: 0xa60
+  __DATA_CONST.__objc_classlist: 0xa70
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe6f8
+  __DATA_CONST.__objc_selrefs: 0xe750
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x920
+  __DATA_CONST.__objc_superrefs: 0x930
   __DATA_CONST.__objc_arraydata: 0xe58
   __AUTH_CONST.__auth_got: 0xdb0
-  __AUTH_CONST.__const: 0x2b80
-  __AUTH_CONST.__cfstring: 0x22a20
-  __AUTH_CONST.__objc_const: 0x3d2b8
+  __AUTH_CONST.__const: 0x2ba0
+  __AUTH_CONST.__cfstring: 0x22a40
+  __AUTH_CONST.__objc_const: 0x3d458
   __AUTH_CONST.__objc_intobj: 0xbb8
   __AUTH_CONST.__objc_arrayobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH.__objc_data: 0x2788
+  __AUTH.__objc_data: 0x2828
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x1fac
+  __DATA.__objc_ivar: 0x1fb8
   __DATA.__data: 0x2740
-  __DATA.__bss: 0x208
+  __DATA.__bss: 0x210
   __DATA_DIRTY.__objc_data: 0x4038
   __DATA_DIRTY.__data: 0xd0
-  __DATA_DIRTY.__bss: 0x408
+  __DATA_DIRTY.__bss: 0x410
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F650AD1B-A0CC-39AB-93AF-8EAB9B85663B
-  Functions: 13600
-  Symbols:   44272
-  CStrings:  23303
+  UUID: E06C61C0-6CF1-305C-8B16-9AE68075F220
+  Functions: 13620
+  Symbols:   44348
+  CStrings:  23327
 
Symbols:
+ +[BRCUploadV1PerformanceTrackerManager sharedManager]
+ +[BRCUploadV1PerformanceTrackerManager sharedManager].cold.1
+ -[BRCLocalItem _trackUploadV1PerformanceIfNeeded]
+ -[BRCSignpostTracker dropSignpostEvent]
+ -[BRCUploadV1PerformanceTracker .cxx_destruct]
+ -[BRCUploadV1PerformanceTracker _initWithCapacity:]
+ -[BRCUploadV1PerformanceTracker _stopTrackingItemWithIdentifier:endEvent:]
+ -[BRCUploadV1PerformanceTracker cancelTrackingItemWithIdentifier:]
+ -[BRCUploadV1PerformanceTracker close]
+ -[BRCUploadV1PerformanceTracker dealloc]
+ -[BRCUploadV1PerformanceTracker finishTrackingItemWithIdentifier:]
+ -[BRCUploadV1PerformanceTracker startTrackingItemWithIdentifier:]
+ -[BRCUploadV1PerformanceTracker startTrackingItemWithIdentifier:].cold.1
+ -[BRCUploadV1PerformanceTrackerManager .cxx_destruct]
+ -[BRCUploadV1PerformanceTrackerManager _init]
+ -[BRCUploadV1PerformanceTrackerManager _removeAllTrackers]
+ -[BRCUploadV1PerformanceTrackerManager removeTrackerForCurrentPersona]
+ -[BRCUploadV1PerformanceTrackerManager trackerForCurrentPersona]
+ -[BRCUserDefaults uploadV1PerformanceTrackerCap]
+ GCC_except_table156
+ GCC_except_table575
+ _OBJC_CLASS_$_BRCUploadV1PerformanceTracker
+ _OBJC_CLASS_$_BRCUploadV1PerformanceTrackerManager
+ _OBJC_IVAR_$_BRCUploadV1PerformanceTracker._itemsToSignpostTracker
+ _OBJC_IVAR_$_BRCUploadV1PerformanceTracker._maxCapacity
+ _OBJC_IVAR_$_BRCUploadV1PerformanceTrackerManager._personaToTrackers
+ _OBJC_METACLASS_$_BRCUploadV1PerformanceTracker
+ _OBJC_METACLASS_$_BRCUploadV1PerformanceTrackerManager
+ __OBJC_$_CLASS_METHODS_BRCUploadV1PerformanceTrackerManager
+ __OBJC_$_INSTANCE_METHODS_BRCUploadV1PerformanceTracker
+ __OBJC_$_INSTANCE_METHODS_BRCUploadV1PerformanceTrackerManager
+ __OBJC_$_INSTANCE_VARIABLES_BRCUploadV1PerformanceTracker
+ __OBJC_$_INSTANCE_VARIABLES_BRCUploadV1PerformanceTrackerManager
+ __OBJC_CLASS_RO_$_BRCUploadV1PerformanceTracker
+ __OBJC_CLASS_RO_$_BRCUploadV1PerformanceTrackerManager
+ __OBJC_METACLASS_RO_$_BRCUploadV1PerformanceTracker
+ __OBJC_METACLASS_RO_$_BRCUploadV1PerformanceTrackerManager
+ ___37-[BRCAccountSession destroyLocalData]_block_invoke.322
+ ___37-[BRCAccountSession destroyLocalData]_block_invoke.322.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.324
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.324.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.324.cold.2
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.324.cold.3
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.324.cold.4
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.331
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.331.cold.1
+ ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.334
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.356
+ ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.356.cold.1
+ ___53+[BRCUploadV1PerformanceTrackerManager sharedManager]_block_invoke
+ ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.370
+ ___66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.386
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.362
+ ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.362.cold.1
+ ___block_literal_global.309
+ ___block_literal_global.321
+ ___block_literal_global.333
+ ___block_literal_global.367
+ ___block_literal_global.946
+ _objc_msgSend$_initWithCapacity:
+ _objc_msgSend$_removeAllTrackers
+ _objc_msgSend$_stopTrackingItemWithIdentifier:endEvent:
+ _objc_msgSend$_trackUploadV1PerformanceIfNeeded
+ _objc_msgSend$cancelTrackingItemWithIdentifier:
+ _objc_msgSend$dropSignpostEvent
+ _objc_msgSend$finishTrackingItemWithIdentifier:
+ _objc_msgSend$removeTrackerForCurrentPersona
+ _objc_msgSend$startTrackingItemWithIdentifier:
+ _objc_msgSend$trackerForCurrentPersona
+ _objc_msgSend$uploadV1PerformanceTrackerCap
+ _sharedManager.sharedInstance
- GCC_except_table574
- ___37-[BRCAccountSession destroyLocalData]_block_invoke.321
- ___37-[BRCAccountSession destroyLocalData]_block_invoke.321.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.323
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.323.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.323.cold.2
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.323.cold.3
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.323.cold.4
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.330
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.330.cold.1
- ___45-[BRCAccountSession _loadClientZonesFromDisk]_block_invoke.333
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.355
- ___45-[BRCAccountSession destroySharedClientZone:]_block_invoke.355.cold.1
- ___60-[BRCAccountSession fetchUserRecordIDWithCompletionHandler:]_block_invoke.368
- ___66-[BRCAccountSession setOptimizeStorageEnabled:forKey:synchronous:]_block_invoke.385
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.361
- ___84-[BRCAccountSession _getOrCreateAppLibraryAndPrivateZonesIfNecessary:creationFlags:]_block_invoke.361.cold.1
- ___block_literal_global.308
- ___block_literal_global.320
- ___block_literal_global.332
- ___block_literal_global.366
- ___block_literal_global.945
CStrings:
+ "-[BRCUploadV1PerformanceTracker close]"
+ "-[BRCUploadV1PerformanceTracker startTrackingItemWithIdentifier:]"
+ "BRCUploadV1PerformanceTracker"
+ "BRCUploadV1PerformanceTrackerManager"
+ "UploadV1"
+ "[CRIT] Assertion failed: signpostTracker%@"
+ "[WARNING] Item with identifier %@ is already tracked%@"
+ "[WARNING] UploadV1 tracker has no available spots, rejecting request%@"
+ "[WARNING] UploadV1PerformanceTracker deallocating with %lu active trackers%@"
+ "_initWithCapacity:"
+ "_itemsToSignpostTracker"
+ "_maxCapacity"
+ "_personaToTrackers"
+ "_removeAllTrackers"
+ "_stopTrackingItemWithIdentifier:endEvent:"
+ "_trackUploadV1PerformanceIfNeeded"
+ "bird.upload-v1-performace-tracker"
+ "cancelTrackingItemWithIdentifier:"
+ "dropSignpostEvent"
+ "finishTrackingItemWithIdentifier:"
+ "removeTrackerForCurrentPersona"
+ "startTrackingItemWithIdentifier:"
+ "trackerForCurrentPersona"
+ "uploadV1PerformanceTrackerCap"

```
