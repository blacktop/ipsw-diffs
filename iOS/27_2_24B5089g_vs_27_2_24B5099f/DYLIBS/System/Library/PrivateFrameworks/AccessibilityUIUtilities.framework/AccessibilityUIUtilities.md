## AccessibilityUIUtilities

> `/System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities`

```diff

-3245.8.2.0.0
-  __TEXT.__text: 0x5f690
-  __TEXT.__objc_methlist: 0x6584
-  __TEXT.__const: 0xd38
+3245.8.4.2.0
+  __TEXT.__text: 0x5f7e8
+  __TEXT.__objc_methlist: 0x6594
+  __TEXT.__const: 0xd40
   __TEXT.__dlopen_cstrs: 0x450
   __TEXT.__constg_swiftt: 0x848
   __TEXT.__swift5_typeref: 0xabb

   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x15c
-  __TEXT.__cstring: 0x5cf1
+  __TEXT.__cstring: 0x5d2f
   __TEXT.__swift5_assocty: 0xf8
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_cont: 0x48
-  __TEXT.__oslogstring: 0x1155
+  __TEXT.__oslogstring: 0x11dc
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__gcc_except_tab: 0x838
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1f30
+  __TEXT.__unwind_info: 0x1f38
   __TEXT.__eh_frame: 0x43c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xde8
+  __DATA_CONST.__const: 0xe18
   __DATA_CONST.__objc_classlist: 0x398
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x51d8
+  __DATA_CONST.__objc_selrefs: 0x51e8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x270
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__got: 0x11a0
-  __AUTH_CONST.__const: 0xa38
-  __AUTH_CONST.__cfstring: 0x6a60
+  __AUTH_CONST.__const: 0xa58
+  __AUTH_CONST.__cfstring: 0x6aa0
   __AUTH_CONST.__objc_const: 0xa2e8
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x11f8
+  __AUTH_CONST.__auth_got: 0x1200
   __AUTH.__objc_data: 0x22b0
   __AUTH.__data: 0x508
   __DATA.__objc_ivar: 0x59c

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2418
-  Symbols:   4671
-  CStrings:  1077
+  Functions: 2420
+  Symbols:   4679
+  CStrings:  1081
 
Symbols:
+ -[AXCameraSceneDescriber _describeCameraSceneWithOptions:featureDescriptionOptions:handler:remainingAttempts:]
+ -[AXCameraSceneDescriber visionResultHandler:withFeatureDescriptionOptions:options:result:error:remainingAttempts:]
+ GCC_except_table1408
+ GCC_except_table1525
+ GCC_except_table1636
+ GCC_except_table1845
+ GCC_except_table1868
+ GCC_except_table1876
+ GCC_except_table1889
+ GCC_except_table1892
+ GCC_except_table1899
+ GCC_except_table1924
+ _AXCameraSceneDescriberErrorDomain
+ _AXUIDeviceSupportsDynamicIsland.onceToken
+ _AXUIDeviceSupportsDynamicIsland.supportsDynamicIsland
+ ___110-[AXCameraSceneDescriber _describeCameraSceneWithOptions:featureDescriptionOptions:handler:remainingAttempts:]_block_invoke
+ ___110-[AXCameraSceneDescriber _describeCameraSceneWithOptions:featureDescriptionOptions:handler:remainingAttempts:]_block_invoke_2
+ ___115-[AXCameraSceneDescriber visionResultHandler:withFeatureDescriptionOptions:options:result:error:remainingAttempts:]_block_invoke
+ ___AXUIDeviceSupportsDynamicIsland_block_invoke
+ ___block_descriptor_56_e8_32s40s48bs_e21_v16?0^{__CVBuffer=}8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e37_v24?0"AXMVisionResult"8"NSError"16ls32l8s56l8s40l8s48l8
+ _objc_retain_x28
- -[AXCameraSceneDescriber visionResultHandler:withFeatureDescriptionOptions:result:error:]
- GCC_except_table1407
- GCC_except_table1524
- GCC_except_table1635
- GCC_except_table1842
- GCC_except_table1867
- GCC_except_table1875
- GCC_except_table1888
- GCC_except_table1891
- GCC_except_table1898
- GCC_except_table1923
- ___84-[AXCameraSceneDescriber imageDescriptionForCurrentCameraScene:withPreferredLocale:]_block_invoke
- ___84-[AXCameraSceneDescriber imageDescriptionForCurrentCameraScene:withPreferredLocale:]_block_invoke_2
- ___block_descriptor_56_e8_32s40s48bs_e37_v24?0"AXMVisionResult"8"NSError"16ls32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e21_v16?0^{__CVBuffer=}8ls32l8s40l8s56l8s48l8
CStrings:
+ "AXCameraSceneDescriberErrorDomain"
+ "Camera scene detection failed after retries: %@"
+ "Camera scene detection returned no description, retrying: %@"
+ "DeviceSupportsDynamicIsland"
+ "Starting camera scene detection, %lu attempt(s) remaining: %@"
- "Starting camera scene detection: %@"
```
