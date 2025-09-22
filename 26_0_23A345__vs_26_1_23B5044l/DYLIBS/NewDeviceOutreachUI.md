## NewDeviceOutreachUI

> `/System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/NewDeviceOutreachUI`

```diff

-502.0.0.0.0
-  __TEXT.__text: 0x4ce14
-  __TEXT.__auth_stubs: 0x1890
+511.0.0.0.0
+  __TEXT.__text: 0x4f368
+  __TEXT.__auth_stubs: 0x1930
   __TEXT.__objc_methlist: 0x14a4
-  __TEXT.__const: 0xe54
-  __TEXT.__cstring: 0x2e75
-  __TEXT.__oslogstring: 0x1ba0
+  __TEXT.__const: 0xfd4
+  __TEXT.__cstring: 0x2f75
+  __TEXT.__oslogstring: 0x1bd0
   __TEXT.__gcc_except_tab: 0x3a0
-  __TEXT.__swift5_typeref: 0x196e
-  __TEXT.__swift5_capture: 0xab4
-  __TEXT.__constg_swiftt: 0x788
-  __TEXT.__swift5_fieldmd: 0x3d4
-  __TEXT.__swift5_reflstr: 0x657
-  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__constg_swiftt: 0x820
+  __TEXT.__swift5_typeref: 0x1a46
+  __TEXT.__swift5_fieldmd: 0x484
+  __TEXT.__swift5_types: 0x54
+  __TEXT.__swift5_capture: 0xaa8
+  __TEXT.__swift5_reflstr: 0x707
+  __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__swift5_proto: 0x34
-  __TEXT.__swift5_types: 0x40
-  __TEXT.__swift_as_entry: 0x58
-  __TEXT.__swift_as_ret: 0x58
-  __TEXT.__unwind_info: 0x1170
-  __TEXT.__eh_frame: 0xd70
+  __TEXT.__swift5_proto: 0x40
+  __TEXT.__swift_as_entry: 0x60
+  __TEXT.__swift_as_ret: 0x5c
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__unwind_info: 0x1210
+  __TEXT.__eh_frame: 0xde0
   __TEXT.__objc_classname: 0x232
   __TEXT.__objc_methname: 0x46ae
   __TEXT.__objc_methtype: 0xc00
   __TEXT.__objc_stubs: 0x37c0
-  __DATA_CONST.__got: 0x7a8
-  __DATA_CONST.__const: 0x840
+  __DATA_CONST.__got: 0x7b8
+  __DATA_CONST.__const: 0x850
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0xc58
-  __AUTH_CONST.__const: 0x1c50
+  __AUTH_CONST.__auth_got: 0xca8
+  __AUTH_CONST.__const: 0x1e50
   __AUTH_CONST.__cfstring: 0xd00
   __AUTH_CONST.__objc_const: 0x3798
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x810
-  __AUTH.__data: 0xa78
+  __AUTH.__data: 0xaf8
   __DATA.__objc_ivar: 0x100
-  __DATA.__data: 0xb00
-  __DATA.__bss: 0x930
+  __DATA.__data: 0xb30
+  __DATA.__bss: 0xb00
   __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0x28
   __DATA_DIRTY.__data: 0x28

   - /System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/NDOUI.framework/NDOUI
   - /System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D0686F11-B768-3F21-AE7C-DC9A814EDA41
-  Functions: 1586
-  Symbols:   2469
-  CStrings:  1501
+  UUID: CB959E62-972E-3848-A422-9E57F10CFEAA
+  Functions: 1654
+  Symbols:   2497
+  CStrings:  1510
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_OS_os_log
+ ___swift_memcpy1_1
+ ___swift_memcpy9_8
+ ___swift_noop_void_return
+ _associated conformance 19NewDeviceOutreachUI11NDOSignpostV5EventOSHAASQ
+ _block_copy_helper.25
+ _block_descriptor.27
+ _block_destroy_helper.26
+ _symbolic SS_So8NSObjectCt
+ _symbolic Sb16forUniversalLink_t
+ _symbolic Si11forConsumer_t
+ _symbolic Si5inApp_t
+ _symbolic So30NDODeviceDetailsViewControllerCSgXwz_Xx
+ _symbolic _____ 19NewDeviceOutreachUI11NDOAnalyticO
+ _symbolic _____ 19NewDeviceOutreachUI11NDOSignpostV
+ _symbolic _____ 19NewDeviceOutreachUI11NDOSignpostV5EventO
+ _symbolic _____ 19NewDeviceOutreachUI19NDOAnalyticsManagerO
+ _symbolic _____ 19NewDeviceOutreachUI19NDOSignpostsManagerO
+ _symbolic _____ 2os12OSSignpostIDV
+ _symbolic ______AAt 19NewDeviceOutreachUI9NDOErrorsO
+ _symbolic _____ySSSo8NSObjectCG s18_DictionaryStorageC
+ _symbolic _____ySS_So8NSObjectCtG s23_ContiguousArrayStorageC
- _block_copy_helper.2
- _block_copy_helper.9
- _block_descriptor.11
- _block_descriptor.4
- _block_destroy_helper.10
- _block_destroy_helper.3
- _objectdestroy.6Tm
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "Sending analytic event: %s with payload %s"
+ "com.apple.graphic-icon.applecare"
+ "com.apple.newdeviceoutreach."
+ "coverage.viewload"
+ "coverageCentralLoaded"
+ "followupDisplayCount"
+ "getCachedCoverageDetails"
+ "loadCoverage"
+ "loadCoverageCentral"
- "com.apple.graphic-icon.gear"

```
