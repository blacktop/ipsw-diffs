## SystemUIDisplayUtilities

> `/System/Library/PrivateFrameworks/SystemUIDisplayUtilities.framework/SystemUIDisplayUtilities`

```diff

-102.0.0.0.0
-  __TEXT.__text: 0xabe4
-  __TEXT.__objc_methlist: 0x770
+104.100.0.0.0
+  __TEXT.__text: 0xb538
+  __TEXT.__objc_methlist: 0x818
   __TEXT.__const: 0x248
-  __TEXT.__cstring: 0x6ab
-  __TEXT.__gcc_except_tab: 0x108
-  __TEXT.__oslogstring: 0xbeb
+  __TEXT.__cstring: 0x70b
+  __TEXT.__gcc_except_tab: 0x120
+  __TEXT.__oslogstring: 0xc4b
   __TEXT.__constg_swiftt: 0x110
   __TEXT.__swift5_typeref: 0xa4
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__unwind_info: 0x3e0
+  __TEXT.__unwind_info: 0x408
   __TEXT.__eh_frame: 0x1b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2b0
-  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__const: 0x328
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a8
+  __DATA_CONST.__objc_selrefs: 0x6e8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__got: 0x190
-  __AUTH_CONST.__const: 0x578
+  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__got: 0x198
+  __AUTH_CONST.__const: 0x598
   __AUTH_CONST.__cfstring: 0x300
-  __AUTH_CONST.__objc_const: 0xf78
-  __AUTH_CONST.__auth_got: 0x498
-  __AUTH.__objc_data: 0x388
+  __AUTH_CONST.__objc_const: 0x1158
+  __AUTH_CONST.__auth_got: 0x4b0
+  __AUTH.__objc_data: 0x3d8
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x84
+  __DATA.__objc_ivar: 0xa0
   __DATA.__data: 0x408
   __DATA.__bss: 0x30
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 287
-  Symbols:   722
-  CStrings:  78
+  Functions: 303
+  Symbols:   761
+  CStrings:  80
 
Symbols:
+ -[SDUDisplayBlankingDescription .cxx_destruct]
+ -[SDUDisplayBlankingDescription blankingState]
+ -[SDUDisplayBlankingDescription bundleIDs]
+ -[SDUDisplayBlankingDescription initWithRegionIdentifier:blankingState:bundleIDs:previousBlankingState:previousBundleIDs:]
+ -[SDUDisplayBlankingDescription previousBlankingState]
+ -[SDUDisplayBlankingDescription previousBundleIDs]
+ -[SDUDisplayBlankingDescription regionIdentifier]
+ -[SDUDisplayRegionBlankingController _liveBundleIDs]
+ -[SDUDisplayRegionBlankingController _waitForPendingDeliveries]
+ -[SDUDisplayRegionBlankingCoordinator blankingStateUpdated:]
+ _BSEqualArrays
+ _OBJC_CLASS_$_SDUDisplayBlankingDescription
+ _OBJC_IVAR_$_SDUDisplayBlankingDescription._blankingState
+ _OBJC_IVAR_$_SDUDisplayBlankingDescription._bundleIDs
+ _OBJC_IVAR_$_SDUDisplayBlankingDescription._previousBlankingState
+ _OBJC_IVAR_$_SDUDisplayBlankingDescription._previousBundleIDs
+ _OBJC_IVAR_$_SDUDisplayBlankingDescription._regionIdentifier
+ _OBJC_IVAR_$_SDUDisplayRegionBlankingController._blankingBundleIDs
+ _OBJC_IVAR_$_SDUDisplayRegionBlankingController._connectionQueue
+ _OBJC_METACLASS_$_SDUDisplayBlankingDescription
+ __OBJC_$_INSTANCE_METHODS_SDUDisplayBlankingDescription
+ __OBJC_$_INSTANCE_VARIABLES_SDUDisplayBlankingDescription
+ __OBJC_$_PROP_LIST_SDUDisplayBlankingDescription
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SDUDisplayRegionBlankingObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SDUDisplayRegionBlankingRenderer
+ __OBJC_CLASS_RO_$_SDUDisplayBlankingDescription
+ __OBJC_METACLASS_RO_$_SDUDisplayBlankingDescription
+ ___60-[SDUDisplayRegionBlankingCoordinator blankingStateUpdated:]_block_invoke
+ ___60-[SDUDisplayRegionBlankingCoordinator blankingStateUpdated:]_block_invoke_2
+ ___63-[SDUDisplayRegionBlankingController _waitForPendingDeliveries]_block_invoke
+ ___block_descriptor_40_e8_32bs_e8_v16?0Q8ls32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ _dispatch_sync
+ _objc_msgSend$_liveBundleIDs
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$blankingBundleIDsDidChangeForDisplayRegion:onWindowScene:forBundleIDs:
+ _objc_msgSend$blankingStateUpdated:
+ _objc_msgSend$bundleIDs
+ _objc_msgSend$initWithRegionIdentifier:blankingState:bundleIDs:previousBlankingState:previousBundleIDs:
+ _objc_msgSend$previousBlankingState
+ _objc_msgSend$previousBundleIDs
+ _objc_msgSend$regionIdentifier
+ _objc_msgSend$updateBundleIDsOfBlankingViewForRegion:onWindowScene:forBundleIDs:withHandler:
+ _objc_retain_x28
- -[SDUDisplayRegionBlankingCoordinator setBlankingState:ofDisplayRegion:forBundleIDs:]
- GCC_except_table3
- ___85-[SDUDisplayRegionBlankingCoordinator setBlankingState:ofDisplayRegion:forBundleIDs:]_block_invoke
- ___85-[SDUDisplayRegionBlankingCoordinator setBlankingState:ofDisplayRegion:forBundleIDs:]_block_invoke_2
- _objc_msgSend$delegate
- _objc_msgSend$setBlankingState:ofDisplayRegion:forBundleIDs:
CStrings:
+ "$"
+ "SDUDisplayRegionBlankingCoordinator: '%@' region bundle IDs changed while blanked: (%@)"
+ "a"
+ "com.apple.SystemUIDisplayUtilities.SDUDisplayRegionBlankingControllerDelegate.connectionQueue"
- "\""
- "A"
```
