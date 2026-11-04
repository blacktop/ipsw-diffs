## CoreAIDelegates

> `/System/Library/SubFrameworks/CoreAIDelegates.framework/CoreAIDelegates`

```diff

-3605.6.4.0.0
-  __TEXT.__text: 0x399b8
-  __TEXT.__const: 0x1e2c
+3610.5.1.0.0
+  __TEXT.__text: 0x3a97c
+  __TEXT.__const: 0x1e44
   __TEXT.__constg_swiftt: 0x548
-  __TEXT.__swift5_typeref: 0x67c
+  __TEXT.__swift5_typeref: 0x684
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x72e
-  __TEXT.__swift5_fieldmd: 0x860
+  __TEXT.__swift5_reflstr: 0x74e
+  __TEXT.__swift5_fieldmd: 0x86c
   __TEXT.__swift5_assocty: 0x180
   __TEXT.__swift5_proto: 0x164
   __TEXT.__swift5_types: 0x84
-  __TEXT.__cstring: 0x18fd
+  __TEXT.__cstring: 0x19c6
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_types2: 0x4
   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x28
   __TEXT.__swift_as_cont: 0x78
   __TEXT.__oslogstring: 0x10f
-  __TEXT.__swift5_capture: 0x24
+  __TEXT.__swift5_capture: 0x28
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xcd8
-  __TEXT.__eh_frame: 0x19f8
+  __TEXT.__unwind_info: 0xce0
+  __TEXT.__eh_frame: 0x1a30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
-  __DATA_CONST.__got: 0x2f0
-  __AUTH_CONST.__const: 0x2750
-  __AUTH_CONST.__objc_const: 0x230
-  __AUTH_CONST.__auth_got: 0xce8
+  __DATA_CONST.__got: 0x318
+  __AUTH_CONST.__const: 0x2778
+  __AUTH_CONST.__objc_const: 0x250
+  __AUTH_CONST.__auth_got: 0xd78
   __AUTH.__objc_data: 0xf0
-  __AUTH.__data: 0x460
-  __DATA.__data: 0x740
-  __DATA.__common: 0xd8
+  __AUTH.__data: 0x468
+  __DATA.__data: 0x758
+  __DATA.__common: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph
   - /System/Library/PrivateFrameworks/BNNSCoreAIDelegate.framework/BNNSCoreAIDelegate
+  - /System/Library/PrivateFrameworks/ParavirtualizedCoreAI.framework/ParavirtualizedCoreAI
   - /System/Library/SubFrameworks/CoreAIAsset.framework/CoreAIAsset
   - /System/Library/SubFrameworks/CoreAICache.framework/CoreAICache
   - /System/Library/SubFrameworks/CoreAICommon.framework/CoreAICommon

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 872
-  Symbols:   157
-  CStrings:  173
+  Functions: 873
+  Symbols:   160
+  CStrings:  176
 
Symbols:
+ _swift_release_x26
+ _swift_retain_x24
+ _swift_retain_x26
CStrings:
+ "COREAI_FORCE_DEBUG_OPTIONS override active — forcing debuggable configuration"
+ "Failed to remove host-side resource via context "
+ "PVCoreAI context is active but PVCoreAIDelegate(resourcesURL:) failed; falling back to MPSGraph delegate. Resources: "
+ "preferredCompute="
+ "preferredCompute=GPU"
+ "preferredCompute=NeuralEngine"
- "COREAI_FORCE_DEBUG_OPTIONS override active — ignoring caller-supplied debugConfiguration"
- "preferredDevice=GPU"
- "preferredDevice=NeuralEngine"
```
