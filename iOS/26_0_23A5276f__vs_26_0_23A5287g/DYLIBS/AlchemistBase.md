## AlchemistBase

> `/System/Library/PrivateFrameworks/AlchemistBase.framework/AlchemistBase`

```diff

-10.0.14.0.0
-  __TEXT.__text: 0x179d4
-  __TEXT.__auth_stubs: 0xf10
+10.0.16.0.0
+  __TEXT.__text: 0x18b78
+  __TEXT.__auth_stubs: 0xf50
   __TEXT.__objc_methlist: 0xa0
   __TEXT.__const: 0x1c0e
-  __TEXT.__cstring: 0xad0
-  __TEXT.__swift5_typeref: 0x68c
-  __TEXT.__constg_swiftt: 0x974
+  __TEXT.__cstring: 0xb70
+  __TEXT.__swift5_typeref: 0x6bc
+  __TEXT.__constg_swiftt: 0x9d8
   __TEXT.__swift5_reflstr: 0x6a2
   __TEXT.__swift5_fieldmd: 0x850
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x120
-  __TEXT.__oslogstring: 0x729
-  __TEXT.__swift5_proto: 0x14c
+  __TEXT.__oslogstring: 0x879
+  __TEXT.__swift5_proto: 0x148
   __TEXT.__swift5_types: 0xbc
-  __TEXT.__swift5_capture: 0x40
+  __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x640
-  __TEXT.__eh_frame: 0xb30
+  __TEXT.__unwind_info: 0x658
+  __TEXT.__eh_frame: 0xb90
   __TEXT.__objc_classname: 0x12
   __TEXT.__objc_methname: 0x454
   __TEXT.__objc_methtype: 0x47
-  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__got: 0x210
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x148
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x788
-  __AUTH_CONST.__const: 0x1310
+  __AUTH_CONST.__auth_got: 0x7a8
+  __AUTH_CONST.__const: 0x12a0
   __AUTH_CONST.__objc_const: 0xa90
   __AUTH.__objc_data: 0xa0
-  __AUTH.__data: 0x8f0
-  __DATA.__data: 0x4e8
+  __AUTH.__data: 0x968
+  __DATA.__data: 0x508
   __DATA.__bss: 0x2800
-  __DATA.__common: 0x88
+  __DATA.__common: 0xa0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Metal.framework/Metal
+  - /System/Library/PrivateFrameworks/ANEClientSignals.framework/ANEClientSignals
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C796A907-FE28-3B5B-B118-E5BBEA08BDCB
-  Functions: 592
-  Symbols:   500
-  CStrings:  171
+  UUID: 5D52D9D7-EBC6-37A6-97B5-9AC37BA537ED
+  Functions: 609
+  Symbols:   499
+  CStrings:  180
 
Symbols:
+ _block_copy_helper.8
+ _block_descriptor.10
+ _block_destroy_helper.9
+ _sendAneSessionSignal
+ _sendAneSignal
+ _symbolic SS_ypt
+ _symbolic _____Sg 13AlchemistBase12FoVPredictorC
+ _symbolic _____Sg 13AlchemistBase14JointPredictorC
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
- _block_copy_helper.11
- _block_descriptor.13
- _block_destroy_helper.12
- _objc_release_x1
- _swift_deallocPartialClassInstance
- _symbolic x
CStrings:
+ "ANE session started for asset at %{public}s with pages: %ld/%ld"
+ "ANE session stopped for asset at %{public}s"
+ "ANEClientModelAssetPath"
+ "ANEClientResidentPages"
+ "ANEClientTotalPages"
+ "ANEHintClientSessionStart"
+ "ANEHintClientSessionStop"
+ "FoV predictor not created. Call createAndLoadFoVPredictor(_:) first."
+ "FoV predictor not created. Call createAndLoadJointPredictor(_:) first."
+ "Joint predictor not created. Call createAndLoadJointPredictor(_:) first."
+ "Unable to fetch ANE session starting data for asset at %{public}s"
- "Loading the Joint + FOV Predictor model"
- "Unloading the Joint + FOV Predictor model"

```
