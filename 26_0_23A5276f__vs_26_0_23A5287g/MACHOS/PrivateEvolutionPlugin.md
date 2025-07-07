## PrivateEvolutionPlugin

> `/System/Library/ExtensionKit/Extensions/PrivateEvolutionPlugin.appex/PrivateEvolutionPlugin`

```diff

-53.0.0.0.0
-  __TEXT.__text: 0x1df14
-  __TEXT.__auth_stubs: 0x1240
+59.0.0.0.0
+  __TEXT.__text: 0x1e104
+  __TEXT.__auth_stubs: 0x12c0
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x1118
-  __TEXT.__cstring: 0x3b7
+  __TEXT.__const: 0x1108
+  __TEXT.__cstring: 0x395
   __TEXT.__objc_methname: 0x2da
   __TEXT.__swift5_typeref: 0x4a5
-  __TEXT.__constg_swiftt: 0x34c
-  __TEXT.__swift5_reflstr: 0x755
+  __TEXT.__constg_swiftt: 0x334
+  __TEXT.__swift5_reflstr: 0x745
   __TEXT.__swift5_fieldmd: 0x5c0
   __TEXT.__swift5_proto: 0xe4
   __TEXT.__swift5_types: 0x40

   __TEXT.__objc_methtype: 0x47
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__oslogstring: 0xdf4
-  __TEXT.__swift_as_entry: 0x5c
-  __TEXT.__swift_as_ret: 0x60
+  __TEXT.__oslogstring: 0xdd4
+  __TEXT.__swift_as_entry: 0x64
+  __TEXT.__swift_as_ret: 0x64
   __TEXT.__swift5_capture: 0x24
   __TEXT.__swift5_protos: 0x4
   __TEXT.__unwind_info: 0x6d0
-  __TEXT.__eh_frame: 0x1020
-  __DATA_CONST.__auth_got: 0x920
-  __DATA_CONST.__got: 0x2f8
-  __DATA_CONST.__auth_ptr: 0x2c8
+  __TEXT.__eh_frame: 0x1060
+  __DATA_CONST.__auth_got: 0x960
+  __DATA_CONST.__got: 0x308
+  __DATA_CONST.__auth_ptr: 0x2d8
   __DATA_CONST.__const: 0xb60
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA.__objc_const: 0x138
+  __DATA.__objc_const: 0x118
   __DATA.__objc_selrefs: 0x108
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x848
+  __DATA.__data: 0x830
   __DATA.__bss: 0x1c00
-  __DATA.__common: 0x28
+  __DATA.__common: 0x20
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML

   - /System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices
   - /System/Library/PrivateFrameworks/Morpheus.framework/Morpheus
   - /System/Library/PrivateFrameworks/MorpheusExtensions.framework/MorpheusExtensions
-  - /System/Library/PrivateFrameworks/PFLLM.framework/PFLLM
+  - /System/Library/PrivateFrameworks/PriMLETL.framework/PriMLETL
   - /System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning
   - /System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4FF82ED3-6A05-3BDF-B5A6-0A644FF5E52C
-  Functions: 454
+  UUID: 080E0728-1FE9-36D1-AB3C-2A4E2661AFFA
+  Functions: 456
   Symbols:   146
-  CStrings:  150
+  CStrings:  149
 
CStrings:
+ "GenerativeModels is available but task required %s."
+ "GenerativeModels is restricted but task required %s."
+ "Loaded %ld in ensureDataAvailability"
+ "Loaded data source config %s."
- "Failed to decode data source config with error %@."
- "Failed to extract data with error %@."
- "GenerativeModels is restricted but task required available."
- "Skipping check for GenerativeModels availability."
- "taskParametersUpdated"

```
