## HealthUI

> `/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI`

```diff

-6200.2.11.2.0
-  __TEXT.__text: 0x3d6278
-  __TEXT.__auth_stubs: 0x5120
-  __TEXT.__objc_methlist: 0x39e84
-  __TEXT.__const: 0x7554
-  __TEXT.__cstring: 0x24bb7
-  __TEXT.__oslogstring: 0x6bd6
+6200.2.12.0.0
+  __TEXT.__text: 0x3d849c
+  __TEXT.__auth_stubs: 0x5190
+  __TEXT.__objc_methlist: 0x39e9c
+  __TEXT.__const: 0x7584
+  __TEXT.__cstring: 0x24c17
+  __TEXT.__oslogstring: 0x6c96
   __TEXT.__gcc_except_tab: 0x24d0
   __TEXT.__ustring: 0x56
   __TEXT.__dlopen_cstrs: 0x367
-  __TEXT.__constg_swiftt: 0x3d78
-  __TEXT.__swift5_typeref: 0x2986
-  __TEXT.__swift5_reflstr: 0x222e
-  __TEXT.__swift5_fieldmd: 0x2298
+  __TEXT.__constg_swiftt: 0x3d84
+  __TEXT.__swift5_typeref: 0x298c
+  __TEXT.__swift5_reflstr: 0x228e
+  __TEXT.__swift5_fieldmd: 0x22bc
   __TEXT.__swift5_builtin: 0x280
   __TEXT.__swift5_assocty: 0x710
   __TEXT.__swift5_proto: 0x2cc
   __TEXT.__swift5_types: 0x318
-  __TEXT.__swift5_capture: 0xa64
+  __TEXT.__swift5_capture: 0xa68
   __TEXT.__swift5_protos: 0x44
-  __TEXT.__swift_as_entry: 0x3c
-  __TEXT.__swift_as_ret: 0x34
+  __TEXT.__swift_as_entry: 0x48
+  __TEXT.__swift_as_ret: 0x40
   __TEXT.__swift5_mpenum: 0x34
-  __TEXT.__unwind_info: 0xdfa8
-  __TEXT.__eh_frame: 0x21dc
-  __TEXT.__objc_classname: 0x90a3
-  __TEXT.__objc_methname: 0x7e21a
-  __TEXT.__objc_methtype: 0x109e2
+  __TEXT.__unwind_info: 0xe030
+  __TEXT.__eh_frame: 0x22ec
+  __TEXT.__objc_classname: 0x90b7
+  __TEXT.__objc_methname: 0x7e30a
+  __TEXT.__objc_methtype: 0x109fa
   __TEXT.__objc_stubs: 0x493a0
-  __DATA_CONST.__got: 0x3468
-  __DATA_CONST.__const: 0x7848
-  __DATA_CONST.__objc_classlist: 0x20b0
+  __DATA_CONST.__got: 0x3488
+  __DATA_CONST.__const: 0x7850
+  __DATA_CONST.__objc_classlist: 0x20b8
   __DATA_CONST.__objc_catlist: 0x2a0
   __DATA_CONST.__objc_protolist: 0x690
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x182e8
+  __DATA_CONST.__objc_selrefs: 0x18310
   __DATA_CONST.__objc_protorefs: 0x168
   __DATA_CONST.__objc_superrefs: 0x1858
   __DATA_CONST.__objc_arraydata: 0x2000
-  __AUTH_CONST.__auth_got: 0x28a0
-  __AUTH_CONST.__const: 0x5e88
+  __AUTH_CONST.__auth_got: 0x28d8
+  __AUTH_CONST.__const: 0x5eb0
   __AUTH_CONST.__cfstring: 0x1eb40
-  __AUTH_CONST.__objc_const: 0x63be8
+  __AUTH_CONST.__objc_const: 0x63cc0
   __AUTH_CONST.__objc_arrayobj: 0xf30
   __AUTH_CONST.__objc_intobj: 0x2940
   __AUTH_CONST.__objc_doubleobj: 0x320
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x16040
-  __AUTH.__data: 0x2068
+  __AUTH.__objc_data: 0x160a8
+  __AUTH.__data: 0x2058
   __DATA.__objc_ivar: 0x402c
-  __DATA.__data: 0x7200
-  __DATA.__bss: 0x5c68
-  __DATA.__common: 0x1e0
+  __DATA.__data: 0x7250
+  __DATA.__bss: 0x5c58
+  __DATA.__common: 0x1e8
   __DATA_DIRTY.__objc_data: 0x1e50
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/HealthDomains.framework/HealthDomains
   - /System/Library/PrivateFrameworks/HealthHearing.framework/HealthHearing
   - /System/Library/PrivateFrameworks/HealthKitAdditions.framework/HealthKitAdditions
+  - /System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
+  - /System/Library/PrivateFrameworks/_IconServices_SwiftUI.framework/_IconServices_SwiftUI
   - /usr/lib/libCTGreenTeaLogger.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 30F4C208-30E4-3B06-8B03-30A1AE315F73
-  Functions: 24399
-  Symbols:   65211
-  CStrings:  30160
+  UUID: 80F50B22-BBA0-361E-8BE9-CAA475513339
+  Functions: 24433
+  Symbols:   65236
+  CStrings:  30171
 
Symbols:
+ +[HKIconServicesImage createImageFromIcon:withDescriptor:]
+ +[HKIconServicesImage fetchIconForBundleIdentifier:imageDescriptor:completion:]
+ +[HKIconServicesImage fetchIconForUTTypeIdentifier:imageDescriptor:completion:]
+ -[HKOverlayRoomViewController viewWillTransitionToSize:withTransitionCoordinator:]
+ -[HKSourceAuthorizationController _updateAuthorizationStatusWithTypes:].cold.1
+ GCC_except_table113
+ GCC_except_table128
+ GCC_except_table133
+ GCC_except_table138
+ _OBJC_CLASS_$_HKIconServicesImage
+ _OBJC_CLASS_$_IFImage
+ _OBJC_METACLASS_$_HKIconServicesImage
+ __IVARS__TtC8HealthUI15SleepScoreYAxis
+ __OBJC_$_CLASS_METHODS_HKIconServicesImage
+ __OBJC_CLASS_RO_$_HKIconServicesImage
+ __OBJC_METACLASS_RO_$_HKIconServicesImage
+ ___79+[HKIconServicesImage fetchIconForBundleIdentifier:imageDescriptor:completion:]_block_invoke
+ ___79+[HKIconServicesImage fetchIconForBundleIdentifier:imageDescriptor:completion:]_block_invoke_2
+ ___79+[HKIconServicesImage fetchIconForUTTypeIdentifier:imageDescriptor:completion:]_block_invoke
+ ___79+[HKIconServicesImage fetchIconForUTTypeIdentifier:imageDescriptor:completion:]_block_invoke_2
+ _objc_msgSend$createImageFromIcon:withDescriptor:
+ _objc_msgSend$initWithType:
+ _symbolic _____ 11SleepHealth0A21ScoreAlgorithmVersionO
- +[HKSelectedRangeLabel clearCaches]
- +[_WDSelectedRangeIcon _cacheKeyForData:foregroundColor:font:]
- +[_WDSelectedRangeIcon _iconCache]
- -[HKSelectedRangeLabel traitCollectionDidChange:]
- GCC_except_table112
- GCC_except_table127
- GCC_except_table132
- GCC_except_table137
- _HKFeatureFlagBloodOxygenSaturationEnabled
- __iconCache._cache
- _objc_msgSend$_cacheKeyForData:foregroundColor:font:
- _objc_msgSend$_iconCache
CStrings:
+ "-[HKSourceAuthorizationController _updateAuthorizationStatusWithTypes] called with 0 types. _types = %{public}@ _typesEnabledForSharing.count = %ld _typesEnabledForReading.count = %ld"
+ "HKIconServicesImage"
+ "_createCheckedContinuation(_:)"
+ "algorithmVersion"
+ "createImageFromIcon:withDescriptor:"
+ "fetchIconForBundleIdentifier:imageDescriptor:completion:"
+ "fetchIconForUTTypeIdentifier:imageDescriptor:completion:"
+ "getImageForImageDescriptor:completion:"
+ "initWithCGImage:scale:orientation:"
+ "initWithType:"
+ "v16@?0@\"IFImage\"8"
+ "v40@0:8{CGSize=dd}16@32"
+ "viewWillTransitionToSize:withTransitionCoordinator:"
- "_cacheKeyForData:foregroundColor:font:"
- "_iconCache"

```
